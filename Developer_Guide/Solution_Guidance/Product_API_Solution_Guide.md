# Product API Solution Guide

**Integration principle: APIs are the source of truth; webhooks are change triggers.** Product create, edit, price, inventory, special listing, and catalog maintenance operations should write through the current Product Open API contract, then verify platform state through Get Product or the relevant search API. Webhooks should wake up reconciliation, not replace read-after-write or scheduled polling.inv

# Purpose and Audience
This guide is for sellers, ISVs, PIM systems, connector apps, and self-developed merchant systems that want to integrate directly with TikTok Shop product APIs instead of relying on the 1P connector path for product listing and daily catalog maintenance.
**This is a reference integration guide, not a product requirements document.** It translates the current product-domain integration pattern into a seller-facing architecture: what to prepare before listing, which product operations to call, how to handle review and listing state, and how to consume product webhooks safely.
Primary references used while drafting: [TikTok Shop Products API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview), [TikTok Shop developer guide](https://partner.tiktokshop.com/docv2/page/tts-developer-guide), [Create Product API](https://partner.tiktokshop.com/docv2/page/create-product-202309), [Edit Product API](https://partner.tiktokshop.com/docv2/page/edit-product-202509), [Update Price API](https://partner.tiktokshop.com/docv2/page/update-price-202309), [Update Inventory API](https://partner.tiktokshop.com/docv2/page/update-inventory-202309), [Partial Edit Product API](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309), [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405), [Product status change webhook](https://partner.tiktokshop.com/docv2/page/5-product-status-change), [Inventory status change webhook](https://partner.tiktokshop.com/docv2/page/27-inventory-status-change), [Product audit status change webhook](https://partner.tiktokshop.com/docv2/page/37-product-audit-status-change), [Combined listing change webhook](https://partner.tiktokshop.com/docv2/page/42-combined-listing-change), and [Combined Listings - Merge into Variants Function Guide](https://seller-us.tiktok.com/university/essay?knowledge_id=1016792318773006&role=1&course_type=1&from=search), [[External] TikTok Shop Catalog Integration Solutions V2023.Q2.01](https://bytedance.sg.larkoffice.com/docx/GYCFd9SVXomiNhxfaQMcYLIznkf)
# Terminology
| Term | Meaning in this guide |
| --- | --- |
| **Seller system** | The seller's PIM, ERP, OMS, commerce platform, or middleware that owns the source catalog and calls TikTok Shop APIs. |
| **TikTok product** | The listing entity created in TikTok Shop. It has product-level content, SKU-level commercial data, platform status, and review state. |
| **SKU** | The sellable variant under a product. Price, inventory, seller SKU, and SKU status are maintained at SKU level. |
| **Full edit** | A product update that resubmits the product object. Omitted fields can be treated as removed except documented exceptions such as price and inventory. |
| **Partial edit** | A targeted product update for selected properties. Use it when the seller system intentionally changes only part of a listing. |
| **Interlink / Combined listing** | A TikTok Shop product relationship that groups multiple related product IDs so shoppers can switch between them from the PDP. This is different from virtual bundle. |
| **GWP / Non-sellable** | Gift with purchase. Products marked as `non_sellable: true` in the Create Product API. These are treated as gift items and cannot be purchased individually. |
| **Idempotency** | The property where a create request can be retried without creating duplicate products. In this guide, `external_product_id` is treated as the Create Product idempotency key. |
# Integration Architecture
The seller's catalog, OMS, and WMS should call TikTok Shop through one integration layer that validates product payloads, signs API requests, stores mappings, and handles webhook-triggered reconciliation.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e47ffdd9b7384a36bc6816af30d1b98c~tplv-k9wyc2ijk0-image.image)
**Recommended state model.** Store external product IDs, TikTok product IDs, SKU IDs, seller SKUs, category IDs, TikTok attribute IDs, seller attribute mapping, warehouse IDs, inventory quantities by warehouse, price by SKU, listing status, audit status, review reason, webhook event timestamp, last successful API request ID, and last TikTok update time.
# Prerequisites Before Listing
Product listing fails most often because the seller system starts with a product payload before the shop, category, brand, warehouse, shipping, and compliance data are ready. Run these checks once at onboarding and again when the seller changes market, category, brand, warehouse, or shipping template.
| Area | Seller action | Why it matters | Testing guidlelines |
| --- | --- | --- | --- |
| Developer app readiness | Follow the [TikTok Shop developer guide](https://partner.tiktokshop.com/docv2/page/tts-developer-guide) to prepare the app, authorization, request signing, token refresh, and webhook callback configuration. | Product API calls should not start until the seller app can sign requests, refresh tokens safely, and receive webhook callbacks for the authorized shop. |  |
| Shop authorization | Confirm the shop is authorized and active; store shop cipher / shop ID per tenant. | Product write APIs require a valid seller authorization context and active shop. |  |
| Listing prerequisites | Call `GET /product/202309/prerequisites` before building bulk create or edit payloads. | Use the response to identify missing setup such as category eligibility, shop readiness, brand, warehouse, logistics, or other product listing requirements before the seller submits Create Product. |  |
| KYC and eligibility | Confirm the seller has completed market onboarding and can list in the target region. | The Edit Product API documentation calls out active sellers / shops with completed KYC as an applicability condition. |  |
| Category mapping | Map the external taxonomy to TikTok category IDs and fetch category rules / attributes before creating payloads. | Required attributes, certifications, package dimensions, and variation rules are category-specific. |  |
| Brand and compliance | Resolve brand authorization and required certifications before listing regulated or restricted categories. | Missing brand or compliance data typically moves the product into rejection or review loops. | For testing purposes, when the seller is in their development phase, we can use "No brand". This doesn't need any brand authorization |
| Warehouse and shipping | Map each external warehouse to a TikTok warehouse ID and confirm shipping settings. | Create and inventory operations need warehouse-level stock data and valid shipping configuration. |  |
| Media readiness | Upload images and files so product media meets platform rules before submission. | Image or file issues can block listing and are hard to fix after a bulk upload has entered review. |  |
# Product Lifecycle Flow
The direct integration should model product sync as a small set of stable states. Create and content/SKU updates can enter review; price and inventory updates usually maintain the live listing operationally. Keep the last live version separate from the submitted version until TikTok confirms approval or rejection.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/937037440e324d1c97420c2cf4db71d7~tplv-k9wyc2ijk0-image.image)
## Product status reference
Use product status to decide what the seller system can do next. The lifecycle diagram uses simplified states; the seller UI and integration logs should keep the TikTok product status, audit status, rejection reason, and the last submitted version separately.
| Status group | What it means for sellers | Integration handling |
| --- | --- | --- |
| **Draft** | The product is saved but not visible to shoppers. | Allow the seller to complete missing product data, media, category rules, logistics inputs, or compliance fields before activation or submission. |
| **Pending / Under review** | The create or edit request is being reviewed by TikTok Shop. | Keep the previous live version and SKU mapping active. Use product status and audit webhooks to know when the submitted version is approved or rejected. |
| **Failed / Rejected** | The submitted listing version did not pass review. | Show the rejection reason to the seller, keep the last live version unchanged, and let the seller fix the payload before resubmitting through Create Product, Edit Product, or Partial Edit Product. |
| **Live** | The product is visible and can be sold if SKU, price, inventory, and shop conditions allow it. | Allow normal price and inventory maintenance through the dedicated APIs. Use Get Product when the seller system needs the authoritative live product snapshot. |
| **Deactivated** | The listing is not actively selling because it was deactivated by the seller or listing controls. | Use the documented Activate Product or Deactivate Products API flow when the seller intentionally changes selling availability. |
| **Suspended / Frozen** | The listing is blocked by platform-side policy, risk, or compliance handling. | Do not treat this as a normal seller deactivation. Store the status reason, surface the required seller action, and refresh with Get Product or the relevant status webhook after the issue is resolved. |
| **Deleted** | The product has been removed. | Stop price and inventory pushes for that `product_id`. After deletion is confirmed, the seller can reuse the same `external_product_id` for a new Create Product request if needed. |

Product status and audit status are related but not identical. Product status tells whether the listing is draft, live, inactive, suspended, or deleted; audit status tells whether a submitted create or edit version is still being reviewed, approved, or rejected.
## Operation routing flow

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c451f893c7f24b979a8ce739aae24ff7~tplv-k9wyc2ijk0-image.image)

**Routing summary.** The flow separates product-domain changes by what the seller is trying to change, because each operation has a different API contract, review behavior, and reconciliation need.

* **Create-path changes:** Use Create Product for new listings and create-only listing attributes such as GWP/non-sellable, scheduled listing, auction, pre-sale, and supported virtual bundle fields. After submission, store `product_id`, `sku_id`, submitted version, and request ID, then track approval through product status and audit webhooks.
* **Content and SKU-model changes:** Use Partial Edit for a small documented field subset, and use full Edit when the seller changes the full listing payload or SKU model. If SKUs are added, removed, or remapped during review, keep the previous live product/SKU mapping active until TikTok confirms the approved state.
* **Commercial operation changes:** Route price-only and inventory-only changes to their dedicated APIs instead of Edit Product. Store the latest price and inventory values sent for each SKU and warehouse. Use webhooks and periodic search/get APIs to confirm TikTok Shop reflects the seller system’s expected state.
* **Relationship and special-listing changes:** Use the specific API path or Create/Edit Product field listed in the relevant feature section. For example, route GWP through `non_sellable`, auction through `product_tag_operations.product_tag = AUCTION`, scheduled listing through `scheduled_sale`, SNS through `subscribe_info` / `subscribe_info_edit`, and supported virtual bundle creation through `primary_combined_product_id` and `combined_skus`.
* **Read-after-write rule:** Webhooks should trigger follow-up handling, but they are not the final source of truth. Call Get Product when the seller system needs the authoritative listing status, audit result, rejection reason, or final SKU mapping.

## Create and update products
A typical Create Product integration should complete authorization, listing prerequisites, category metadata, media, logistics inputs, product creation, and approval tracking in that order. This keeps the Create Product payload focused on submission instead of using Create Product to discover missing setup.
### Typical create product sequence

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b17484ebce884c8f9fa62c6387265e96~tplv-k9wyc2ijk0-image.image)

Create Product and Product Edit share the same integration discipline: build a complete product model, validate category and market requirements, store TikTok IDs, and handle review state before treating the submitted version as live.
| Operation | API / field to use | Seller-facing guidance |
| --- | --- | --- |
| Create product | `POST /product/202309/products` ([Create Product API](https://partner.tiktokshop.com/docv2/page/create-product-202309)) | Use when no TikTok product exists yet. Send the full product object and store returned `product_id` and `sku_id` values. |
| Full edit | `PUT /product/202309/products/{product_id}` ([Edit Product API](https://partner.tiktokshop.com/docv2/page/edit-product-202509#Back%20To%20Top)) | Use when changing the product object or SKU model. Fetch latest product first, merge intended changes, submit, then wait for audit / status outcome before replacing live mappings. <br/> The Edit Product response can return `audit_status`. Treat `AUDITING` as pending review, `APPROVED` as accepted, and `NONE` as not applicable to review because the product may be draft, frozen, deactivated, or otherwise not submitted for listing. |
| Partial edit | `PATCH /product/202309/products/{product_id}/partial_edit` ([Partial Edit Product API](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309)) | Use for targeted product-content edits. Do not use it for price-only or inventory-only changes. |
| Get product | `GET /product/202309/products/{product_id}` ([Get Product API](https://partner.tiktokshop.com/docv2/page/get-product)) | Use when the integration needs authoritative state after webhook notification, audit completion, error recovery, or scheduled reconciliation. |
```JSON
{
  "save_mode": "LISTING",
  "title": "Example cotton T-shirt",
  "description": "HTML product description",
  "category_id": "123456",
  "brand_id": "987654",
  "non_sellable": false,
  "scheduled_sale": {"start_time": 1790000000},
  "pre_sale": {"type": "PRE_ORDER"},
  "product_tag_operations": [{"operation": "ADD", "tag": "AUCTION"}],
  "main_images": [{"uri": "tos-image-uri"}],
  "skus": [{
    "seller_sku": "TSHIRT-BLACK-M",
    "price": {"amount": "19.99", "currency": "USD"},
    "inventory": [{"warehouse_id": "7000714532876273410", "quantity": 100}]
  }]
}
```


### Category Recommendation
Resolve the TikTok category before building the create or edit payload. The seller can browse a category tree, ask the platform for a recommended category, then fetch attributes and rules for the selected category.
| Step | API / field to use | How sellers should use it |
| --- | --- | --- |
| Browse/select category | `GET /product/202309/categories` ([Get Categories API](https://partner.tiktokshop.com/docv2/page/get-categories-202309)) | Use when the seller UI lets merchants choose a TikTok category from the available category tree. |
| Recommend category | `POST /product/202309/categories/recommend` ([Recommend Category API](https://partner.tiktokshop.com/docv2/page/recommend-category-202309)) | Use when the seller does not know the best category to auto recommend category; send title, description, and product signals, then ask the seller to confirm the selected category. |
| Confirm rules | `GET /product/202309/categories/{category_id}/rules` ([Get Category Rules API](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309)) | Use to validate category constraints, certifications, package dimensions, size chart, and other listing requirements. This provides the required attributes/conditions that needs to be met for success product listing. |

### Warehouse Mapping
Store a warehouse mapping before product creation and product updates. The seller's warehouse code should map to the TikTok `warehouse_id` used in the create / edit payload and later inventory maintenance.

* Reject listing rows that have stock but no mapped TikTok warehouse.

### Attribute Mapping
Use `GET /product/202309/categories/{category_id}/attributes` ([Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)) to build the product template for the selected category. These attributes contain the required fields that should be populated for the listing to be submitted successfully.
**Store TikTok Attribute ID, not only display name.** Attribute names and value labels can change by market, language, or category version. Persisting the TikTok attribute ID lets the seller system rebuild edit payloads and reconcile product state without guessing from translated labels.

### Media, size chart, and logistics assets
Upload or resolve every asset ID before calling Create Product or Edit Product. The create/edit payload should reference TikTok Shop asset identifiers returned by product media APIs, not seller-local file paths or external image URLs.
| Asset / setup need | API / reference to use | How sellers should use it |
| --- | --- | --- |
| Product images | `POST /product/202309/images/upload` ([Upload Product Image API](https://partner.tiktokshop.com/docv2/page/upload-product-image-202309)) | Upload main product images, detail images, and other listing images before create/edit. Store the returned image URI and reference it in product image fields. |
| Product files | `POST /product/202309/files/upload` ([Upload Product File API](https://partner.tiktokshop.com/docv2/page/upload-product-file-202309)) | Upload product files required by the selected category or market, such as certificates, compliance files, labels, or other file assets accepted by the Product API. Store the returned file identifier for create/edit payloads. |
| Existing size chart | [Search Size Charts API](https://partner.tiktokshop.com/docv2/page/search-size-charts-202407) | Use when category rules require a size chart and the seller may already have one. Store the selected size chart ID and reference it in the listing payload where required. |
| New or updated size chart | [Create Size Chart API](https://partner.tiktokshop.com/docv2/page/create-size-chart-202608) and [Edit Size Charts API](https://partner.tiktokshop.com/docv2/page/edit-size-charts-202608) | Create or update a seller size chart before listing submission, then attach the resulting size chart ID to products in categories that require size guidance. |
| Image optimization | [Optimized Images API](https://partner.tiktokshop.com/docv2/page/optimized-images-202404) | Use when the seller wants platform-generated image improvements. Only reference optimized images in create/edit payloads after seller review and approval. |
| Image translation | [Create Image Translation Tasks API](https://partner.tiktokshop.com/docv2/page/create-image-translation-tasks-202505) and [Get Image Translation Tasks API](https://partner.tiktokshop.com/docv2/page/get-image-translation-tasks-202506) | Use for image text translation workflows when selling across markets. Poll the task result, let the seller review translated assets, then use the approved image URI in create/edit. |
| Logistics and shipping inputs | `GET /product/202309/prerequisites` and category rules | Resolve required package dimensions, logistics settings, shipping option IDs, and market-specific listing inputs before submission. These are setup identifiers, not media uploads. |

### Best Practice
| Topic | What to store | Best practice |
| --- | --- | --- |
| Product mapping | product_id, product status | After the creation/updation, store the products product id and sku id details along with the product status information. Use this information to support future edits for the product |
| SKU mapping | `product_id`, `sku_id`, seller SKU, live status, submitted version, pending removal flag | Keep mappings for both the current live SKU set and the submitted SKU set while an edit is under review. If live SKUs are A, B, C and the seller submits B, C, D, keep SKU A mapped as pending removal until TikTok confirms the new version is live. Orders can still be placed against SKU A during review. |
| Idempotency key | `external_product_id` along with the shop details or any information which would help avoid duplicate product creation | The same key cannot create another product while the previous product is non-deleted. After that product is deleted, the seller can create a new product with the same key. Use this idempotency key to avoid duplicate product creation.  |
| Category mapping | External category to Tiktok category mapping | Provide a tool to the sellers to allow them to map the external category to TikTok category. This will help with listing products and help avoid sellers to reselect the TikTok category and facilitate auto mapping category.  |
| Attribute mapping | External attribute to Tiktok attribute mapping | Provide a tool to allow the sellers to map the product properties from external system to TikTok attributes and values. This will help with listing products and sellers wouldn't have to manually re-add all the attribute information. Attribute Ids change based on category.  |
| Approval tracking | `product_id`, `sku_id`, submitted version, request ID, audit status, product status | After Create Product, wait for Product status change and product audit events before showing the listing as live. Use webhook events as triggers and call Get Product when the seller system needs the final approved state, rejection reason, or SKU mapping confirmation. |
| Review handling | Submitted product version, live product version, audit status, rejection reason | Do not replace live mapping, SKU availability, or seller-facing sellable state until product status / audit webhook or Get Product confirms the submitted version is live. You can also store multiple versions of the sku mapping one for live and one for reviewing. The mapping will be helpful to fulfill orders. |

### Advanced Feature
| Feature | API / field to use | Seller-facing guidance |
| --- | --- | --- |
| Scheduled publishing | `scheduled_sale` in `POST /product/202309/products` | Store the intended schedule in the seller system and verify final live status through Product status webhook and Get Product. |
| Pre-create optimization | [Diagnose and Optimize Product API](https://partner.tiktokshop.com/docv2/page/diagnose-and-optimize-product-202411#Back%20To%20Top) | Use before the product has a TikTok `product_id`. Show suggestions to the seller and submit only seller-approved content. |
| Post-create title / description optimization | [Get Recommended Product Title and Description API](https://partner.tiktokshop.com/docv2/page/get-recommended-product-title-and-description-202405#Back%20To%20Top) | Use only after product creation; this API requires `product_id`. Apply approved changes through Edit Product or Partial Edit Product. |
| Image optimization | [Optimized Images API](https://partner.tiktokshop.com/docv2/page/optimized-images-202404) | Use where supported to improve product images, then reference seller-approved image URIs in Create Product, Edit Product, or Partial Edit Product. |
## Update price
Use `POST /product/202309/products/{product_id}/prices/update` ([Update Price API](https://partner.tiktokshop.com/docv2/page/update-price-202309)) for SKU-level price maintenance. Keep price-only changes out of full product edit flows unless the product payload is intentionally being rebuilt.
```JSON
{
  "skus": [{
    "id": "1729382476852921560",
    "price": {"amount": "19.99", "currency": "USD"}
  }]
}
```

**Price update handling:** For each SKU, send the final price that should appear on TikTok Shop. Store the intended price, seller-side price update time, request ID, and TikTok response status for each `product_id` + `sku_id`. Use this record to safely retry the same price update, ignore older retries after a newer price change, and reconcile TikTok Shop’s current price against the seller system’s latest intended price.
## Update inventory
Use `POST /product/202309/products/{product_id}/inventory/update` ([Update Inventory API](https://partner.tiktokshop.com/docv2/page/update-inventory-202309)) for warehouse-level SKU stock. Use `POST /product/202309/inventory/search` ([Inventory Search API](https://partner.tiktokshop.com/docv2/page/inventory-search-202309)) for scheduled reconciliation and backfill.
```JSON
{
  "skus": [{
    "id": "1729382476852921560",
    "inventory": [{"warehouse_id": "7000714532876273410", "quantity": 80}]
  }]
}
```

### Inventory best practice

* Send final available quantity by SKU and warehouse; do not send source deltas unless the API reference for the target market explicitly supports delta behavior.
* For normal volume, sellers can push each source inventory change directly to Update Inventory.
* For high order volume, high stock-change frequency, or oversell risk, sellers can optionally use aggregation / controlled cadence before calling Update Inventory. The aggregation layer should collapse rapid source changes into the latest safe quantity
* When adding a new warehouse to an existing SKU, include all warehouses that should remain attached to that SKU. If updating quantity for existing warehouse, directly just pass only that warehouse and quantity.
* Run scheduled reconciliation with Inventory Search so missed webhooks, failed pushes, or manual Seller Center edits do not leave stock stale.


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2c9f2a30402b47f8b7c75cd82c4141a0~tplv-k9wyc2ijk0-image.image)

## Webhook Strategy
Register product-domain webhooks on the seller's app and route every event to the same reconciliation queue. The webhook payload should identify what changed; the seller system should pull product state before making downstream decisions.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/eda4611ca8e044ffac7bea70457f5bfc~tplv-k9wyc2ijk0-image.image)

| Webhook | Primary payload fields | How sellers should use it |
| --- | --- | --- |
| Product status change | `product_id`, `status`, `suspended_reason`, `update_time` | Update seller product status, show whether a product is live / inactive / deleted / suspended, and trigger Get Product when authoritative state is needed. |
| Product audit status change | `product_id`, audit status, reason fields, `update_time` | Notify sellers when a submitted create / edit passes or fails review. On approval, finalize submitted mapping changes. On rejection, keep the previous live mapping and expose fix guidance. |
| Product information change | `product_id`, `changed_fields`, `change_source` | Detect edits made directly in Seller Center or another app. Pull the product and decide whether the seller source catalog or TikTok state wins for each field. |
| SKU status change | `product_id`, SKU list with `sku_id` and `status` | Update variant availability and prevent future price / inventory updates from targeting deactivated SKUs without seller review. |
| Inventory status change | Inventory status, available quantity signals, product / SKU references | Alert sellers for LOW_STOCK or OUT_OF_STOCK and optionally trigger inventory reconciliation before sending a corrective update. |
| Combined listing change | `combined_listing_id`, products, status, `change_type` | Keep grouped listing display state in sync when the combined listing is created, updated, deactivated, or deleted. |

# Special Listing Scenarios
Special listing features should be feature-gated by market, category, and seller eligibility before the seller can submit the payload. If a feature is not available through the Product API for that seller scenario, describe the supported seller workflow instead of sending unsupported fields.
| Scenario | API / field to use | Seller-facing guidance | Suggested Flow |
| --- | --- | --- | --- |
| Sku Level Virtual bundle | `POST /product/202309/products` with `primary_combined_product_id` and SKU-level `combined_skus` | Create the bundle only after component products and SKUs are live and mapped. Store bundle PID, bundle SKU, component `product_id` / `sku_id`, and component quantity. Use edit only when the target API version documents update support for the same fields. This is only establishing sku level bundle.  <br/>  <br/> For **product level bundle** there is no API currently, the seller has to modify this in the seller center directly. https://seller-us.tiktok.com/university/essay?knowledge_id=894944353240878&role=1&course_type=1&from=search |  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/55ad19e1fdc94f12852ce0ccee0277b0~tplv-k9wyc2ijk0-image.image) <br/>  <br/>  |
| Combined listing / interlink | `POST /product/202506/combined_listing_recommendations/search` ([Products API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview)) <br/>  | Use this API only to retrieve recommended groups of products that could be merged into a combined listing, based on shared option attributes such as color, style, flavor, or similar variant dimensions. The request takes product IDs, for example `{"product_ids":["123423536575","123423536576"]}`, and the response returns recommendation groups such as `option_name`, product `id`, `option_value`, `next_page_token`, and `total_count`. This API does not create the combined listing, submit the Seller Center merge, or perform child SKU mapping. For the actual Merge into variants flow, sellers should use Seller Center under Manage Products → Combined Listings → Merge products. After the relationship exists, store the main product, child products, generated variant mapping, child SKU to combined-listing SKU mapping, and combined listing status because changing selected products or deleting a variant dimension can reset generated SKU mappings. |  |
| Gift with purchase (GWP) | `non_sellable: true` in `POST /product/202309/products` | Treat GWP type as create-time immutable. To convert between GWP and sellable, delete the listing first, wait until deletion is confirmed, then recreate. The same idempotency key can be reused only after the prior product is deleted. |  |
| Auction listing | `product_tag_operations.product_tag = AUCTION` in Create Product | Validate market and category eligibility before showing auction to the seller. Confirm Edit Product support separately before allowing post-create auction tag maintenance. |  |
| Pre-sale | `pre_sale` when supported by category and market | Validate category rules before submission and keep seller UI copy clear that pre-sale is different from scheduled listing. |  |
| SNS | `POST /product/202502/products/search` with `sns_filter`; `GET /product/202309/products/{product_id}` returns `subscribe_info`; `PUT /product/202309/products/{product_id}` or `POST /product/202309/products/{product_id}/partial_edit` with `subscribe_info_edit` | Assuming SNS means Subscribe and Save, sellers can discover SNS products with `sns_filter`: use `CONFIGURED` for products already configured for SNS and `ELIGIBLE` for products eligible for SNS. Use Get Product to read `subscribe_info`, including `support_subscribe`, `subscribe_status`, discount details, and available discount constraints. Enable, disable, or update SNS through Edit Product or Partial Edit Product by sending `subscribe_info_edit.subscribe_status` as `ENABLED` or `NOT_ENABLED` with `discount_details`. Actual configuration still depends on seller and product eligibility shown by `support_subscribe`. |  |
# Seller Whitelist and Listing Eligibility Controls
[Product Listing Whitelist and Eligibility Guide for Sellers](https://bytedance.us.larkoffice.com/docx/FMjjdgUTroFxuixUFShu9H9Wsdd)
# Market Requirements
Product payloads are not identical across markets. The seller system should resolve category rules, compliance fields, warehouse configuration, and listing features for the target shop before create or edit.
| Market / surface | Required seller preparation | Implementation guidance |
| --- | --- | --- |
| EU GPSR | Prepare manufacturer and responsible person records, then pass `manufacturer_ids` and `responsible_person_ids` for applicable categories. | Block listing submission until the seller has selected the required records. Do not silently omit these fields because the product may fail compliance validation or review. |
| Category-specific compliance | Fetch category rules for certifications, safety labels, package dimensions, product attributes, and invite-only categories. | Keep a per-market category rule cache and refresh it before bulk listing. Rules can differ for the same external category in US, UK, EU, SEA, and LATAM. |
| Warehouse and inventory | Map seller warehouses to TikTok warehouse IDs and validate warehouse-level inventory fields. | Inventory updates should target SKU + warehouse. Reject listing rows that have stock but no mapped TikTok warehouse. |
| Listing features | Check whether auction, pre-sale, scheduled sale, temporary listing, SNS, GWP, and virtual bundle are enabled for the seller's market and category. | Feature-gate unsupported fields in the seller UI so unsupported features do not create review failures or silent no-ops. |
# Global Products and Market Expansion
Use this flow when one seller wants to offer the same product through more than one UK or EU shop. Each shop is a separate market: it has its own Shop ID, product ID, SKU IDs, listing rules, price, inventory, and compliance requirements.
## Use Local Replication
For new integrations, create the product in one local shop and use Replicate Product to copy it to each target market. TikTok Shop keeps the relationship between the products, while every target shop receives its own product ID and SKU IDs.
| Method | What it does | When to use it |
| --- | --- | --- |
| Local Replication | Copies a product from one local shop to another supported market and keeps the products related. | Use for all new Direct API integrations. |
| Seller Center Global Listings | Creates and manages related market listings through Seller Center rules. | Your integration may read the relationship, but it should not recreate or overwrite it without checking the current product data. |
| Legacy Global Product APIs | The older cross-market product method that used global product records. | Use only to migrate existing legacy products. Do not use it for new products. |
## Public APIs for Market Expansion
The Product API reference is the source of truth for request fields, permissions, supported markets, and current limits.
| API or event | What it does | When to use it |
| --- | --- | --- |
| [Get Global Listing Rules](https://partner.tiktokshop.com/docv2/page/get-global-listing-rules-202507) | Returns the global listing methods and inventory rules available to the shop. | Call before showing or starting a Sell Across EU flow. Continue only when Local Replication is supported. |
| [Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309) | Creates the product in the selected source shop. | Use when the product does not yet exist in the source shop. |
| [Replicate Product](https://partner.tiktokshop.com/docv2/page/replicate-product-202507) | Starts an asynchronous copy from the source shop to a supported target market. | Use after the source product is ready and the target market requirements have been checked. |
| Global Replication Status Change event | Notifies your application when a replication request finishes or needs attention. | Use the event instead of repeatedly sending Replicate Product or treating submission as final success. |
| [Get Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) | Returns the latest product data and replication information for one local product. | Use after an event, during reconciliation, and before retrying an update. |
| [Partial Edit Product](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309) | Adds or corrects selected fields on a local product. | Use when replication creates a target-shop draft that needs market-specific information. |
| [Get Global Replicated Products](https://partner.tiktokshop.com/docv2/page/get-global-replicated-products-202507) | Returns the local products related through replication. | Use for onboarding existing products, mapping repair, and regular reconciliation. |
| [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | Finds products already present in a shop. | Use before creating or replicating when the seller may already have a matching product. |

See the [Products API Overview](https://partner.tiktokshop.com/docv2/page/products-api-overview) and the Product section of the [TikTok Shop API reference](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) for the complete public API list.
## Implementation Flow
This flow shows the recommended seller journey. Replication is asynchronous: accepting a request is the start of processing, not confirmation that the target listing is ready.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/34008b80ce4943c3ae1fdff7ca4a1c06~tplv-k9wyc2ijk0-image.image)

*If Local Replication is not supported, keep the product as a local listing for that market. If replication creates a draft or fails, update the existing target product and confirm its latest state before retrying.*
## Direct API Flow

1. **Authorize every shop.** Obtain access for the source shop and each target shop. Confirm that the application has the required Product API scopes.
2. **Check shop readiness.** Get the seller's authorized shops and call Get Listing Prerequisites for each shop that will create or receive a product.
3. **Check the listing method.** Call Get Global Listing Rules. Continue only when the response allows Local Replication for the intended market and inventory model.
4. **Prepare each target market.** Fetch the target shop's categories, attributes, category rules, and authorized category assets. Requirements can differ by country even when the physical product is the same.
5. **Create the source product.** Use Create Product in the selected local shop. Save its local product ID and SKU IDs.
6. **Start replication.** Call Replicate Product for each supported target market. A successful API response means that TikTok Shop accepted the request; it does not mean that the target listing is ready to sell.
7. **Wait for the result.** Subscribe to the Global Replication Status Change event. When an event arrives, call Get Product to read the latest target-shop state.
8. **Complete drafts or fix failures.** Replication can create a draft when the target market needs extra data. Use Get Product to find the missing fields, then use Partial Edit Product or the relevant price and inventory APIs before resubmission.
9. **Save the market mapping.** Store the Shopify product and variant IDs together with the Shop ID, country, local product ID, and local SKU IDs for every market.

## Implementation Best Practices
These practices describe a safe integration approach without requiring sellers to copy TikTok Shop's internal design.
### Product Identity and Mapping

* Use the seller's own stable product and variant identifiers as the starting point for mapping.
* Store a separate record for every shop. Include the Shop ID, country, local product ID, and local SKU IDs.
* Never assume that the same product has the same product or SKU ID in two markets.
* Before creating or replicating, search the target shop and check the saved mapping to avoid duplicates.

### Asynchronous Processing and Safe Retries

* Treat Replicate Product as an asynchronous request. Show the seller that processing has started, then wait for the Global Replication Status Change event.
* Use each event as a signal to call Get Product. The latest product response should decide the next action.
* Allow only one active replication request for the same source product and target shop.
* Before retrying, check whether TikTok Shop already created a live product or draft. Update an existing draft instead of creating another product.
* Use delayed retries for temporary errors. Do not repeatedly call the API in a short period.

### Market-Specific Data

* Validate categories, attributes, qualifications, certifications, Manufacturer, Responsible Person, price, warehouse, and inventory for each target shop.
* Keep product content, price, and inventory updates as separate operations. This makes failures easier to explain and retry.
* Use shared inventory only when Get Global Listing Rules confirms that the market and warehouse support it.
* When a target listing needs local information, collect only the missing fields and update that market's product.

### Monitoring and Seller Experience

* Run regular reconciliation with Search Products, Get Product, and Get Global Replicated Products. Webhooks can be delayed or missed.
* Keep an audit trail of the source product, target shop, request time, latest result, and seller action required.
* Show errors in seller-friendly language, for example: “Certification required for France” instead of displaying only an API error code.
* Roll out one or two target markets first. Confirm mappings, webhooks, compliance handling, price, and inventory before enabling more markets.

**Recommended seller statuses:** Processing, Needs action, and Ready. Keep detailed API states in the integration logs, while the seller sees the next action in plain English.

## Existing Products
Do not assume that a product is unrelated just because your application did not create it. Seller Center or another integration may already have created the market relationship.

* Use Search Products to find products already present in each shop.
* Use Get Product and check `is_replicated` to see whether a local product came from replication.
* Read `global_product_association` to match related SKUs across shops.
* Use Get Global Replicated Products to find the full set of related local products.
* If Get Product returns `global_listing_policy`, preserve the Seller Center Global Listing relationship and follow its policy.

## Market Data and Inventory
Replication reuses product information where possible, but it does not remove local listing requirements. Validate the following for every target shop:

* Category and required product attributes
* Brand or category authorization
* Certifications and supporting files
* Manufacturer and Responsible Person information where required
* Target-market price, tax settings, warehouse, and inventory

Use shared inventory only when Get Global Listing Rules allows it for the selected market and warehouse. Otherwise, maintain inventory separately for each shop.
## Retries and Duplicate Prevention

* Before creating or replicating, search the target shop and check your saved mapping.
* After sending Replicate Product, save the request context and wait for the status event.
* Before retrying, call Get Product or Get Global Replicated Products to confirm whether a target product or draft already exists.
* If a draft exists, update that draft. Do not create another copy.
* If two live products already exist in one shop, ask the seller which listing to keep before changing mappings or deleting a listing.

## Legacy Product Migration
The Local Replication whitelist was removed on June 30, 2026. New integrations should use Local Replication without a whitelist dependency.
Legacy Global Product APIs are scheduled for retirement on October 30, 2026. For products that still use the legacy method, follow the [migration announcement](https://partner.tiktokshop.com/docv2/page/6z874qqu), start migration with [Create GPA Upgrade Task](https://partner.tiktokshop.com/docv2/page/create-gpa-upgrade-task-202604), and subscribe to the [Global Listing Method Change](https://partner.tiktokshop.com/docv2/page/g2wnrb57) event. This migration flow is for existing legacy products only.
## Seller and Partner Checklist

* Use only public TikTok Shop Open APIs documented in Partner Center.
* Use Local Replication for new cross-market products.
* Store product and SKU IDs separately for every shop.
* Wait for the replication event and confirm the latest product state before retrying.
* Complete target-market compliance, price, warehouse, and inventory data.
* Do not depend on `global_product_id` or any internal service.

# API Operation Index
| Operation | Public API or reference | When to use it |
| --- | --- | --- |
| Get listing prerequisites | `GET /product/202309/prerequisites` | Check whether a shop is ready to create or receive a listing. |
| Get categories | [Get Categories](https://partner.tiktokshop.com/docv2/page/get-categories-202309) | Show the seller the categories available in the selected shop. |
| Recommend category | [Recommend Category](https://partner.tiktokshop.com/docv2/page/recommend-category-202309) | Suggest a category when the seller does not know which one to choose. |
| Get attributes | [Get Attributes](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) | Find the required and optional attributes for the selected category. |
| Get category rules | [Get Category Rules](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309) | Check certifications, package dimensions, size charts, and other category rules. |
| Get authorized category assets | [Get Authorized Category Assets](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) | Check which seller or category qualifications can be used for the listing. |
| Upload product image | [Upload Product Image](https://partner.tiktokshop.com/docv2/page/upload-product-image-202309) | Upload images before using the returned reference in a create or edit request. |
| Upload product file | [Upload Product File](https://partner.tiktokshop.com/docv2/page/upload-product-file-202309) | Upload size charts, labels, certificates, and other product files. |
| Pre-create optimization | [Diagnose and Optimize Product](https://partner.tiktokshop.com/docv2/page/diagnose-and-optimize-product-202411#Back%20To%20Top) | Check a product payload before the product has a TikTok Shop product ID. |
| Post-create optimization | [Get Recommended Product Title and Description](https://partner.tiktokshop.com/docv2/page/get-recommended-product-title-and-description-202405#Back%20To%20Top) | Improve the title or description after product creation. |
| Get global listing rules | [Get Global Listing Rules](https://partner.tiktokshop.com/docv2/page/get-global-listing-rules-202507) | Check whether Local Replication and a shared-inventory method are supported for the shop. |
| Create product | [Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309) | Create the product in a selected local shop after its required data is ready. |
| Replicate product across markets | [Replicate Product](https://partner.tiktokshop.com/docv2/page/replicate-product-202507) | Start an asynchronous copy to another supported market. Each target shop receives its own product and SKU IDs. |
| Track replication result | Global Replication Status Change event | Wait for the event, then call Get Product. Do not treat request acceptance as final listing success. |
| Get product | [Get Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) | Read the latest product state after an event, during reconciliation, and before retrying. |
| Full edit | [Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202509) | Fetch the latest product first, then send the full intended state. |
| Partial edit | [Partial Edit Product](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309) | Add or correct selected product fields, including fields missing from a replicated draft. |
| Update price | [Update Price](https://partner.tiktokshop.com/docv2/page/update-price-202309) | Maintain prices for the local SKUs in one shop. |
| Update inventory | [Update Inventory](https://partner.tiktokshop.com/docv2/page/update-inventory-202309) | Maintain stock by local SKU and warehouse. |
| Search inventory | [Inventory Search](https://partner.tiktokshop.com/docv2/page/inventory-search-202309) | Reconcile stock, check low-stock products, or backfill inventory during onboarding. |
| Search products | [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | Find existing products before create or replicate, and reconcile products already in the shop. |
| Get related market products | [Get Global Replicated Products](https://partner.tiktokshop.com/docv2/page/get-global-replicated-products-202507) | Find local products related through replication and repair cross-market mappings. |
| Migrate legacy global products | [Create GPA Upgrade Task](https://partner.tiktokshop.com/docv2/page/create-gpa-upgrade-task-202604) | Use only for products that still use the legacy Global Product API method. |
| Subscribe to product events | [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) | Subscribe to supported product, SKU, audit, inventory, and replication events. |
