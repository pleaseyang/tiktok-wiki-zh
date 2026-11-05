# Methods and endpoints

# Methods
TikTok Shop API reference pages define the HTTP method for each endpoint. Most TTS Open APIs use **GET** or **POST**. A small number of endpoints may use other RESTful methods, but developers should always follow the exact method shown on the endpoint reference page.
Using a method that does not match the endpoint reference can cause errors such as `36009010 Invalid method`.
| **Method** | **Typical use** | **Implementation note** |
| --- | --- | --- |
| **GET** | Retrieve resources from TikTok Shop. | Commonly used for query and list APIs. |
| **POST** | Send data or execute an action. | Commonly used when the API has a request body or performs a state-changing operation. |
| **PUT** | Update an existing resource. | Use only when the endpoint reference explicitly lists `PUT`. |
| **DELETE** | Remove a resource. | Use only when the endpoint reference explicitly lists `DELETE`. |
# Endpoints
TikTok Shop API endpoints are organized by resource type and follow the pattern:
**https://{domain}/{category}/{version}/{resource}**
The `/{category}/{version}/{resource}` segment can be found in the corresponding reference doc for any TikTok Shop API. Starting with the `202309` API style, the API version is part of the request path, for example `/authorization/202309/shops`. When you calculate the request signature, use the request path exactly as shown after the domain, including the category, version, and resource segments. For signing rules, refer to [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request).
For example, to call [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309), the endpoint is:
```Plain Text
https://open-api.tiktokglobalshop.com/authorization/202309/shops
```

# Domains and environments
For **business API calls**, TTS Open API currently uses the following domain:
| **Environment** | **URI** | **Use case** |
| --- | --- | --- |
| Production | `https://open-api.tiktokglobalshop.com` | The request host used by developers to call TTS Open API endpoints after creating an app. Use HTTPS. |

Do not use authorization or token domains as the business API request host. They have different purposes:
| **Purpose** | **Domain or entry** | **Use case** | **Reference** |
| --- | --- | --- | --- |
| Business API calls | `https://open-api.tiktokglobalshop.com` | Call API endpoints such as authorization, product, order, fulfillment, and webhook APIs. | Current page |
| Seller authorization | `https://services.us.tiktokshop.com/open/authorize` for US; `https://services.tiktokshop.com/open/authorize` for ROW | Start seller or shop authorization and obtain an authorization code. Do not use this host as an API endpoint host. | [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
| Partner authorization | `https://partner.us.tiktokshop.com/open/authorize` for US; `https://partner.tiktokshop.com/open/authorize` for ROW | Start partner authorization and obtain an authorization code. Do not use this host as an API endpoint host. | [Partner authorization guide](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide) |
| Creator authorization | `https://shop.tiktok.com/alliance` | Start creator authorization. Do not use this host as an API endpoint host. | [Creator authorization guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide) |
| Token exchange | `https://auth.tiktok-shops.com` | Exchange an authorization code for tokens or refresh tokens. | [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) |
| Sandbox and API testing |  <br/>  | Use Sandbox app setup and the [API testing tool](https://partner.tiktokshop.com/dev/api-testing-tool) to test calls, while still following the endpoint reference for the exact path and method. | [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
# Category quick reference
The category segment groups endpoints by business area. Always copy the final method and path from the endpoint reference page, because version and resource names can differ by API.
| **Business area** | **Common category segment** | **Example resource** | **Reference** |
| --- | --- | --- | --- |
| Authorization | `authorization` | `shops` | [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| Product | `product` | `products`, `categories`, `inventory` | [Product API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview) |
| Order | `order` | `orders` | [Order API overview](https://partner.tiktokshop.com/docv2/page/order-api-overview) |
| Fulfillment | `fulfillment` | `packages`, `shipping_documents` | [Fulfillment API overview](https://partner.tiktokshop.com/docv2/page/fulfillment-api-overview) |
| Return & Refund | `return_refund` | `returns`, `refunds`, `cancellations` | [Return & Refund API overview](https://partner.tiktokshop.com/docv2/page/return-refund-and-cancel-api-overview) |
| Logistics | `logistics` | `warehouses`, `delivery_options`, `shipping_providers` | [Logistics API overview](https://partner.tiktokshop.com/docv2/page/logistic-api-overview) |
| Promotion | `promotion` | `promotions`, `discounts` | [Promotion API overview](https://partner.tiktokshop.com/docv2/page/promotion-api-overview) |
| Finance | `finance` | `payments`, `settlements` | [Finance API overview](https://partner.tiktokshop.com/docv2/page/finance-api-overview) |
| Seller | `seller` | `shops` | [Seller API overview](https://partner.tiktokshop.com/docv2/page/seller-api-overview) |
| Events | `event` | `webhooks` | [Events API](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) |
| Supply Chain | `supply_chain` | `packages`, `shipments` | [Supply Chain API](https://partner.tiktokshop.com/docv2/page/confirm-package-shipment) |
# Version and path guidance
The version segment is part of the endpoint path and must match the API reference page. Do not assume that all endpoints use the same version. For version selection and migration guidance, refer to [TTS API versioning](https://partner.tiktokshop.com/docv2/page/api-versioning).
When troubleshooting request failures, check the following first:
| **Symptom** | **Likely cause** | **What to check** |
| --- | --- | --- |
| `36009010 Invalid method` | The HTTP method does not match the endpoint reference. | Reopen the endpoint reference and use the exact method shown there. |
| Signature validation failure | The signed path or timestamp does not match the actual request. | Confirm that the signed path includes `/{category}/{version}/{resource}` and follow [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request). |
| Host or DNS confusion | An authorization, token, or testing domain was used as the business API host. | Use `https://open-api.tiktokglobalshop.com` for business API calls. |
