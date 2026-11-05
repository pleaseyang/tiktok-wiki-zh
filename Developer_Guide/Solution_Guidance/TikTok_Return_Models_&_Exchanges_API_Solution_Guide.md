# TikTok Return Models & Exchanges API Solution Guide

# **Aftersales Transactions Overview**
Returns/refunds, cancellations, & exchanges are post-sales (after-sales) actions that can be initiated by either buyers or sellers. TikTok Shop provides API scopes for sellers to programatically handle these cases:

* **Cancel API**: Supports buyer-initiated cancellation requests and seller-initiated order cancellations.
* **Return API**: Supports buyer-initiated refund or return-and-refund requests.


**Cancel Order**
Orders can be canceled at the buyer’s request or directly by the seller. Each canceled order includes the cancel reason, status, creation time, and seller processing time. In the US and UK, sellers can also partially cancel orders when items are out of stock.
**Return Order**
Return orders occur when a buyer requests a return or refund only for one or more items after delivery. Each return order includes the return/refund reason, status, request time, seller processing time, and refund amount.

**This document will focus on Return transactions**, nuanced return label models, and give guidance on developing end-to-end solutions using the TikTok Shop open APIs based on the different return models.
--
For a more **generalized** overview of all TikTok Shop Aftersales workflows, please see our documentation below:

* [Return, refund, and cancel API overview](https://partner.tiktokshop.com/docv2/page/return-refund-and-cancel-api-overview)
* [Return reasons](https://partner.tiktokshop.com/docv2/page/return-reasons)
* [Refund reasons](https://partner.tiktokshop.com/docv2/page/refund-reasons)
* [Cancel reasons](https://partner.tiktokshop.com/docv2/page/cancel-reasons)




# **Aftersales Stages**
Before diving into the detailed API sequence, it's important to understand the **stages** of an aftersales/return record in TikTok Shop. TikTok Shops measures the seller's actions in these different return stages, to ensure the buyer communications/experience meets our SLAs/policies. **Note**: These measured **stages** are *different* from the granular return **status** that are exposed in the API/webhooks
| **Stage** | **What Happens** | **Seller Action** | **SLA / Deadline** | **Outcome / Notes** |
| --- | --- | --- | --- | --- |
| **1st Review Stage:**  <br/> Return Request | Buyer submits a return request. TikTok now auto-approves **95%** of requests based on product category. Once approved, TikTok generates the official **RMA_ID** for the seller/ISV to capture the return and related line items.  | For ~5% of requests that still require review, the seller must **approve or reject** the **request** via API or Seller Center. <br/>  | **24 hours** from request submission | If no decision is made within 24 hours, TikTok will **auto-approve** the request and generate the return shipping label. Some requests may require review due to restricted categories or suspicious buyer return activity. |
| **2nd Review Stage:**  <br/> Return Decision | After the returned package is received and inspected, the seller reviews the refund decision. | Seller must **approve or reject the return,** based on their item inspection SOP or automated rules. | **4 business days** after return package's tracking shows `DELIVERED`  | If no decision is made within 4 business days , TikTok will **auto-approve** the return, and the buyer will be refunded the money associated with their original payment. |

For all return transactions, TikTok Shop API/webhooks expose the necessary return status updates, and delivery signals that enable sellers to indentify what action they need to perform next within the return lifecycle.


# **Return Actions by Status**
During the lifecycle of a return, there are specific actions buyers or sellers are allowed to perform, based on the forward `order_id` status, as well as what the `return_id` status.

The following table illustrates when a "Return" can be **initiated** based on the current order status.
|  | **Initiator** | **`UNPAID` ** | **`ON_HOLD`** | **`AWAITING_SHIPMENT`** | **`AWAITING_COLLECTION`** | **`IN_TRANSIT`** | **`DELIVERED`** | **`Completed`** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Return** <br/> **Initiation** | Buyer | No | No | No | No | **Yes** | **Yes** | No |
|  | Seller | No <br/>  | No | No | No <br/>  | No <br/>  | Depends on market policy. US allows for seller to create an offline return record, but it must be automatically approved for the refund amount to the buyer, | No |

The following table illustrates what actions a seller or buyer may perform on a return, based on the current return status. 
| **Return Status** | **Request Type / ID** | **Description** | **Seller Action** | **Buyer Action** |
| --- | --- | --- | --- | --- |
| `RETURN_OR_REFUND_REQUEST_PENDING` <br/>  | Aftersales <br/>  | Buyer initiates a return request which creates an Aftersales Request ID. Although TikTok auto-approves 95% of these requests, there are some records that are pending seller review. | Approve or reject the request |  |
| `AWAITING_BUYER_RETURN` <br/>  | RMA  | The Aftersales return request has been approved and the official RMA `id` is created. Awaiting for the buyer to ship the item. | - <br/>  | Ship the items back to seller |
| `RETURN_IN_TRANSIT` | RMA | The buyer has shipped the item and carrier tracking confirms the return is on-route. | Seller can approve the refund of the return if needed, even before it arrives at their facility.  | - |
| `PENDING_PACKAGE_REVIEW` | RMA | The return package is confirmed `DELIVERED` by the carrier. | Inspect/grade items and make a decision to either approve or reject the refund of the return line items. | - |
| `PACKAGE_REVIEW_COMPLETED` | RMA | The return package has finished inspection and final decisions for refunds.  | Arbitration with buyer and TT CS if the results are not agreed upon. | Arbitration with buyer and TT CS if the results are not agreed upon. |



# **Return Label Models**
TikTok has **2 return label models** - and the API integration path will be defined by which model is right for the sellers' specific operations/system architecture. Once the seller selects which return label model is required for their systems, they can build a holistic returns management integration with TikTok's open APIs for either of these return models.
| **Return Model** | **Description** |
| --- | --- |
| ###  **4PL Model:** <br/> **TikTok Return Labels** <br/>  | TikTok is responsible for generating the return shipping label, using our own TikTok carrier accounts. <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/d10e9007db6147e1b81876a7a9db4d82~tplv-k9wyc2ijk0-image.image) <br/>  |
| ###  **3PL Model:** <br/> **External Return Labels** <br/>  | The seller/or external return platforms are responsible for generating a return shipping label, **AND** also responsible for **uploading** that shipping label to TikTok through our open API.  <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/10ffa64b8edf488ea2f1ab1fa6c784c0~tplv-k9wyc2ijk0-image.image) <br/>  <br/>  <br/> ***Note****: The TikTok Shop definition for 3PL labels means this is a 3rd party logistics* ***label,*** *not necessarily coming from a 3rd party logistics fulfillment provider. 3PL labels can come from a seller's own UPS/USPS/Fedex accounts, or these labels could be generated by a return platform such as:* ***Loop Returns****,* ***Happy Returns*** *etc.* <br/>  <br/> *This ability to generate and upload a 3rd party return shipping label is* ***commonly referred to as V2 Returns*** *within the TikTok ecosystem.*  <br/>  |


# **4PL Model: TikTok Return Labels**
The standard returns behavior for TikTok Shop is use TikTok's return shipping labels for the buyers. At a high-level, sellers can use our open APIs to build an end-to-end integration for returns management that will allow them:

1. Capture the new return/RMA details
2. Submit the return/RMA details to their return warehouse's systems (WMS/DB)
3. Buyers use the TikTok shipping label to send the return package to the seller's return warehouse location
4. Warehouse operations identify the return package, inspect and grade the items
5. Based on the warehouse grading, send TikTok the decision to either APPROVE or REJECT the return refund to the buyer.


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4af84bdf9ebf4bbaa50a6e0a1251b28f~tplv-k9wyc2ijk0-image.image)


> ### **4PL Model API documentation** 


Returns API and webhook documentation below: 

* [Aftersales Request Status Update Webhook](https://partner.tiktokshop.com/docv2/page/h4cxaxub)
* [Search Aftersales Request API](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603)
* [RMA Status Update Webhook](https://partner.tiktokshop.com/docv2/page/2f0jrrxc)
* [Search Return Merchandise Authorization (RMA) API](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604)
* [Review Aftersales API](https://partner.tiktokshop.com/docv2/page/review-aftersales-202603)
* [Refund Success Webhook](https://partner.tiktokshop.com/docv2/page/8y10pibm)


> ### **4PL Solution Architecture & Implementation** 


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3bb8248cfccb4af9a5baebfce08b79ed~tplv-k9wyc2ijk0-image.image)


| # **Aftersales** <br/> # **Stage** | # **Step** | # **System** | # **Requirement Details** |
| --- | --- | --- | --- |
| ### Buyer initiates a return and starts the (1st Review Stage) |  |  |  |
| **1st Review** <br/>  <br/>   <br/>  <br/>   <br/>   <br/>   <br/>  | **[1]** Buyer Submits Return Request <br/>  | **TikTok**  <br/>  | Buyer has selected the return method in TT app and submits a return request. |
|  | **[2]** Webhook: `AFTERSALES_REQUEST_STATUS_UPDATE` <br/> Webhook topic: **64** <br/>  | **TikTok** <br/>  | TikTok triggers the webhook topic: **Aftersales Request Status Update** <br/> "aftersales_request_status" : `PENDING_REQUEST_REVIEW` <br/> [Webhook topic 64 documentation](https://partner.tiktokshop.com/docv2/page/h4cxaxub) <br/>  |
|  | **[3]** Search Aftersales Request API | **Seller/ISV** <br/>  | Use the aftersales_request_id provided in the webhook as a search parameter when calling the "Search Aftersales Reques API". The response will expose all return_line_item_id (s) associated with this unified aftersales request <br/> [Search Aftersales Request API documentation](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603) <br/>  |
|  | **[4]** Sync Aftersales Request to Seller OMS <br/>  | **Seller/ISV** | Aftersales request details synced to sellers OMS/UI/Workbench etc for review  |
|  | **[5]** Decision to approve or reject the **request** <br/>  | **Seller/ISV** | Seller to decide if they want to **approve** or **reject** the **request** to return. This is considered the 1st review decisioning step.  <br/> > **Note**: For the majority of sellers, this 1st review step is **automatically** approved, based on their product category of the items in the return request. And for any auto-approved aftersale request, the seller does not need to perform any approval of the request, but they still must perform a refund decision within our policy SLA of 48H once return package shows delivered scan at the warehouse.  |
|  | **[6]** Review Aftersales API | **Seller/ISV** | Use this API to make a decision on whether to **approve** or **reject** the return request. Specify **request_id_type**: **`AFTERSALES`** <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
|  | **[7]** Webhook: `AFTERSALES_REQUEST_STATUS_UPDATE` | **TikTok** | **Webhook: AFTERSALES_REQUEST_STATUS_UPDATE** <br/> status: `REQUEST_REVIEW_COMPLETED` <br/> [Webhook topic 64 documentation](https://partner.tiktokshop.com/docv2/page/h4cxaxub) |
| ### Once the 1st review process is completed, the official RMA workflow will begin (2nd Review Stage) |  |  |  |
| **2nd Review** <br/>  | **[8]** TikTok RMA Created  | **TikTok** <br/>  | Once the aftersales request has been approved, TikTok will immediately create an RMA, which is a unified return identifyer that encompasses all unique sku lines and quantity associated with the return submission from the buyer |
|  | **[9]** Webhook: `RMA_STATUS_UPDATE` <br/> Webhook topic: **65** | **TikTok** <br/>  | **Webhook: RMA_STATUS_UPDATE** <br/> **status**: **`RMA_CREATED`** <br/> This webhook will trigger as soon as the official TikTok RMA has been created in TikTok's system <br/> [Webhook topic 65 documentation](https://partner.tiktokshop.com/docv2/page/2f0jrrxc) |
|  | **[10]** Search RMA Requests API | **Seller/ISV** | Call this API to obtain the full details of the return, including all nested return order and line level item details.  <br/> [Search Return Merchandise Authorization API documentation](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604) <br/>  |
|  | **[11]** Sync Return RMA  | **Seller/ISV** | Feed the return RMA details in OMS & WMS layers to ensure the RMA is recorded in the database for operations to identify once received. |
|  | **[12A] & [12B]** Buyer Ships/Drop-off items | **TTS Buyer** | Buyer takes items to nearest carrier drop-off or ships items to warehouse |
|  | **[13]** Warehouse operations receives RMA package | **Warehouse OPS** | Warehouse operations to receive and identify the RMA package with the RMA record in the WMS for processing.  |
|  | **[14]** Warehouse operations inspection | **Warehouse OPS** | Warehouse operations to perform grading/inspection SOPs for RMA's return line_items |
| ### 2nd review inspection results have 4 possible paths (A,B,C,D) |  |  |  |
| ### **PATH A:** All expected items received and accepted for full refund |  |  |  |
| **PATH A** <br/>  | **[15.A]** WMS updates OMS | **WMS** <br/>  | Warehouse associates inspect items and update the RMA status that all line_items associated with the RMA are in "good' condition <br/>  |
| **PATH A** <br/>  | **[16.A]** OMS updates TikTok Application | **OMS** <br/>  | Based on warehouse items grading results that all items are in good condition, OMS updates the Return app that all items are eligible for full refund amount. <br/>  |
| **PATH A** | **[17.A]** Review Aftersales API <br/>  | **ISV** | Triggers the refund of all return_line_item_id(s) in the RMA. <br/> request_id_type: `RMA` <br/> action: `APPROVE_RETURN_PACKAGE` <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH A** | **[18.A]** Refund Buyer  | **TikTok** | Buyer's refund payment is completed |
| ### **PATH B:** Some items don't meet warehouse grading acceptance criteria (some items missing/damaged). |  |  |  |
| **PATH B** <br/>  | **[15.B]** WMS RMA status = Some items graded as "damaged/missing" <br/>  | **WMS** | Warehouse associates inspect items and update the RMA status **some** line_items associated with the RMA are in "good' condition, some are "damaged/missing" |
| **PATH B** <br/>  | **[16.B]** Instruct TTS app with mixed refund decision (all lines) | **OMS** | Based on warehouse items grading results that some line_items are in "good' condition, some are "damaged/missing", update Return platform RMA with partial refunds based on line items. |
| **PATH B** | **[17.B]** Review Aftersales API <br/>  <br/>  | **Seller/ISV** <br/>  | Triggers the refund of approved line_items and rejection of the line_items that are missing/damaged. When using the "Review Aftersales API", you can define different decision/action enumerations for the different return_line_item_id(s). Example: <br/> return_line_item_id: 111 = Good condition. <br/> action: `APPROVE_RETURN_PACKAGE` <br/> - <br/> return_line_item_id: 222 = damaged/missing <br/> Action: `REJECT_RETURN_PACKAGE`  <br/>  <br/> > **Note**: TTS does **not** allow the same exact sku_id to have **different** decisions (known platform limitation). The seller must make the same action/decision for multiple quantities of the same sku_id. We are solving this platform issue by end of Q3, 2026, to allow truly flexible return_line_item_id decisions regardless of the sku_id profiles. <br/>  <br/>  <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH B** | **[18.B]** Mixed Refund by SKU lines <br/>  | **TikTok** | Buyer's partial refund payment is completed based on different sku_id decisions.  |
| ### **PATH C:** All items don't meet warehouse grading acceptance criteria (missing/damaged).  |  |  |  |
| **PATH C** | **[15.C]** OMS RMA status = All items graded as "damaged/missing" | **WMS** | Warehouse associates inspect items and update the RMA status ALL line_items associated with the RMA are "damaged/missing" |
| **PATH C** | **[16.C]** Instruct TTS app to REJECT RMA (all lines) <br/>  | **OMS** | Based on warehouse items grading results that ALL line_items are in "damaged/missing' condition, update return platform RMA to reject refund of all line items |
| **PATH C** | **[17.C]** Review Aftersales API | **Seller/ISV** | Triggers the rejection of the refund of all line_items within the RMA <br/> request_id_type: `RMA` <br/> action: `REJECT_RETURN_PACKAGE` <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH C** | **[18.C]** Return Refund Rejected (all lines) | **TikTok** | Refund is rejected for all return items and notification is sent to buyer |
| ### **PATH D:** Some quantity of same sku_id do not meet warehouse grading acceptance criteria (missing/damaged). Offer partial refund |  |  |  |
| **PATH D** | **[15.D]** OMS RMA status = Same sku / multiple quantity has different conditions. <br/>  | **WMS** | RMA contains multiple quantities of the exact same sku (SKU:A x 2 QTY) Warehouse associated inspects the package/items and finds that: <br/>  QTY 1 is in good condition <br/>  QTY 2 is completely damaged/or missing altogether.  |
| **PATH D** | **[16.D] Instruct TTS app** `OFFER_PARTIAL_REFUND` <br/>  | **OMS** | Based on warehouse items grading results, 1 QTY should be refunded, 1 QTY should be rejected due to the damage. However, as previously stated, TikTok shop platform has a known gap where we do not allow different refund decisions if there are multiple quantities of the same sku_id. To solve for this platform behavior, OMS must perform calculations to trigger a partial refund amount for each qty/line, which is meant to equate to the total amount the buyer should receive. Example:  <br/> Buyer orders SKU:A x 2 QTY. Each item original cost paid = $10.00 <br/> QTY 1 is received in "good/sellable" condition <br/> QTY 2 is damaged or missing. <br/> - <br/> The seller wants to **approve** QTY 1 and **reject** QTY 2, so that the buyer is only refunded **$10.00** out of the original $20.00 amount paid for both lines. However, the TTS platform/API does not allow different decisions for the same SKU (known platform behavior/limitation).  <br/>  <br/> The seller can use the Review Aftersales API and use the `OFFER_PARTIAL_REFUND` enumeration for both lines. However, OMS logic **must** calculate the amount using the formula  <br/> (Total amount to refund buyer) / (total # of return_line_item_ids) <br/> Example from above: <br/> $10.00 (total amount to refund buyer) / (2 return_lines) = $5.00 <br/> The `OFFER_PARTIAL_REFUND` amount will be `5.00` for **both** lines of the same SKU, to ensure the buyer will receive $10.00 for their refund amount. <br/>  |
|  **PATH D** | **[17.D]** Review Aftersales API <br/> request_id_type: `RMA` <br/> action: `OFFER_PARTIAL_REFUND` | **Seller/ISV** | Triggers `OFFER_PARTIAL_REFUND` action for all line_items of that same SKU <br/> request_id_type: `RMA` <br/> action: `OFFER_PARTIAL_REFUND` <br/> - <br/> Within the alternative_solutions_details object: <br/> Define `partial_refund_amount` & `currency` <br/>  <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH D** | **[18.D]** Buyer is refunded the accurate partial amount | **TikTok** | Partial refund amount and notification is sent to buyer |
| **PATH D** |  |  | **Buyer Appeasement Use-Case** <br/> The `OFFER_PARTIAL_REFUND` can also be used as an appeasment mechanism. For example <br/> **IF**: the buyer was only expected to send back SKU A, QTY 1, but the item was slightly damaged, noticeably worn, package slightly damaged etc <br/> **THEN**: the seller can make a decision to `OFFER_PARTIAL_REFUND` for that single return_line_item_id, and TikTok will refund that buyer the amount specified by the seller.  |




# **3PL Model: External Return Labels**
***Also known as: V2 Returns***
The **most common** use-case for the 3PL label model is when sellers want to leverage their existing DTC return platforms with TikTok return activity. Oftentimes, sellers' DTC process will leverage **return platforms** that are responsible for **generating a shipping label** for the buyers, and **orchestrating the data flows** and for operational functions between the return platform and their own DTC/OMS/WMS layers. 

By leveraging these **existing** return platform workflows for TikTok Shop returns, sellers can **alleviate engineering efforts and costs**. And maintain a **consistent** end-to-end process between their DTC and TikTok Shop returns. Also, some sellers have customized attributes/barcodes rendered on the return shipping label through these return platforms. These label attributes are part of their warehouse SOPs for scanning and identifying return packages once received at their warehouse facilities. 

### Return platforms that have partnered with TikTok to build the 3PL label/QR code model:

* Loop Returns
* Happy Returns
* Amazon MCF
* Redo Returns
* Narvar (scoping in progress)


At a high-level, these existing return platform integrations follow this model outlined below

1. Capture the new return/RMA details
2. Generate a 3rd party return shipping label (3PL, off TikTok's platform)
3. Upload that the 3rd party return back to TikTok to render/email to the buyer
4. Submit the return/RMA details to their return warehouse's systems (WMS/DB)
5. Buyers use the seller's 3PL label to send the return package to the seller's return warehouse location
6. Warehouse operations identify the return package, inspect and grade the items
7. Based on the warehouse grading, send return status to an OMS layer for refund decision to return platform/app.
8. Return Platform app to send TikTok the decision to either APPROVE or REJECT the return refund to the buyer.


However, sellers **do not** have to leverage these existing return platform integrations. They are also able to **develop their own 3PL label model**. **** This essentially allows the seller to perform the exact steps the return platforms are managing outlined above, but the seller **use their own label** and upload directly between their systems and TikTok's API. 



![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/6f1e289079bf429b9306a3087f211caf~tplv-k9wyc2ijk0-image.image)


> ### **3PL Model Prerequisites Checklist**

There are multiple prerequisite configurations required for each sellers' shops. Sellers must have the following checklist completed **before** they are able to test the label generation & label upload flow back to the TikTok app buyer view. 
| **Checklist Tasks** | **Owner** | **Comments** |  |
| --- | --- | --- | --- |
| Define which **`seller_id`**(s) needs 3PL label functionality | Seller/TTS | Share sandbox and production **`seller_id`**(s) with TikTok solutions POC for backend configuration | - [ ]  |
| Define which **`app_key`** will be managing return APIs | Seller/TTS | Share **`app_key`** with TikTok solutions POC for backend configuration | - [ ]  |
| Define which exact carrier return methods to offer buyers <br/>  | Seller/TTS <br/>  | TikTok needs to configure the **`seller_id`** to only display the seller's expected return methods in buyer UX journey. Carrier return methods vary between carriers: **`USPS`**, **`UPS`**, **`Fedex`**. And each carrier has variations in return methods for shipping labels vs dropoff QR codes.  | - [ ]  |
| Request API access for [Upload Shipping Document API](https://partner.tiktokshop.com/docv2/page/upload-shipping-document-and-tracking-info-202405) | Seller/TTS | TTS solutions POC must whitelist your **`app_key`** to access this API scope. | - [ ]  |
| Request API access for new batch returns API/Webhooks <br/>  | Seller/TTS | Background: TikTok released a new set of API/webhooks to manage returns in May 2026. The new APIs follow the industry standards in terms of RMA data structure. For more details about the legacy behaviors, and why we deployed the new version, please see this document [here](https://bytedance.us.larkoffice.com/docx/JSUAdGU59ol2uexgVeFuvi0ssrc).  | - [ ]  |
| Create a TikTok user account for testing <br/>  | Seller | Share the TikTok **`user_id`** with TikTok solutions POC to flag as "test" user, which can access test shop products to perform order creation, and return submission to validate the 3PL label upload is properly rendered in the TikTok app.  <br/> **Steps to obtain TikTok UID (insert doc)** | - [ ]  |
| Create a test product in your sandbox TikTok Shop account | Seller  | Set price to $1.00, as this will require actual credit card checkout | - [ ]  |
| Create order with test product with TikTok test user account | Seller | This order will appear in your Partner Center development shop console, where you can force the status to `DELIVERED` .  | - [ ]  |
Once these prerequisites are completed, when a return is initiated within the TikTok app against the test order, the expectation is that the seller is coordinating the webhook and API calls to then upload the shipping label to Tiktok. 

**The definition of success for this test is that the return shipping label will be rendered directly into the TikTok users view (as seen below)**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/66ea5f2f2b7840d8a895d62bb84b20b4~tplv-k9wyc2ijk0-image.image)


> ### **3PL Model API documentation** 

Returns API and webhook documentation below: 

* [Aftersales Request Status Update Webhook](https://partner.tiktokshop.com/docv2/page/h4cxaxub)
* [Search Aftersales Request API](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603)
* [RMA Status Update Webhook](https://partner.tiktokshop.com/docv2/page/2f0jrrxc)
* [Search Return Merchandise Authorization (RMA) API](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604)
* [Get External Order Reference API](https://partner.tiktokshop.com/docv2/page/get-external-order-references-202406) (requires TikTok enablement) **OPTIONAL USE**
* [Upload Shipping Document API](https://partner.tiktokshop.com/docv2/page/upload-shipping-document-and-tracking-info-202405) (requires TikTok enablement)
* [Review Aftersales API](https://partner.tiktokshop.com/docv2/page/review-aftersales-202603)
* [Refund Success Webhook](https://partner.tiktokshop.com/docv2/page/8y10pibm)


> ### **3PL Solution Architecture & Implementation Steps (3PL Model)**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5a20c6f3f49c48878615866292948fcb~tplv-k9wyc2ijk0-image.image)



| # **Aftersales** <br/> # **Stage** | # **Step** | # **System** | # **Requirement Details** |
| --- | --- | --- | --- |
| ### Buyer initiates a return and starts the (1st Review Stage) |  |  |  |
| **1st Review** <br/>  <br/>   <br/>  <br/>   <br/>   <br/>   <br/>  | **[1]** Buyer Submits Return Request <br/>  | **TikTok**  <br/>  | The buyer has selected the return method in TT app and submits a return request. |
|  | **[2]** Webhook:`AFTERSALES_REQUEST_STATUS_UPDATE` <br/> Webhook Topic ID: 64 <br/>  | **TikTok** <br/>  | TikTok triggers the webhook topic: **Aftersales Request Status Update** <br/> "aftersales_request_status" : `PENDING_REQUEST_REVIEW` <br/> [Webhook topic 64 documentation](https://partner.tiktokshop.com/docv2/page/h4cxaxub) <br/>  |
|  | **[3]** Search Aftersales Request API | **Seller/ISV** <br/>  | Use the aftersales_request_id provided in the webhook as a search parameter when calling the "Search Aftersales Reques API". The response will expose all return_line_item_id (s) associated with this unified aftersales request <br/> [Search Aftersales Request API documentation](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603) <br/>  |
|  | **[4]** Sync Aftersales Request to Seller OMS <br/>  | **Seller/ISV** <br/>  | Aftersales request details synced to sellers OMS/UI/Workbench etc for review  |
|  | **[5]** Decision to approve or reject the **request** <br/>  | **Seller** | Seller to decide if they want to **approve** or **reject** the **request** to return. This is considered the 1st review decisioning step.  <br/> > **Note**: For the majority of sellers, this 1st review step is **automatically** approved, based on their product category of the items in the return request. And for any auto-approved aftersale request, the seller does not need to perform any approval of the request, but they still must perform a refund decision within our policy SLA of 48H once return package shows delivered scan at the warehouse.  <br/>  <br/>  |
|  | **[6]** Review Aftersales API | **Seller/ISV** | Use this API to make a decision on whether to **approve** or **reject** the return request. Specify **request_id_type**: **`AFTERSALES`** <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) |
|  | **[7]** Webhook: `AFTERSALES_REQUEST_STATUS_UPDATE` | **TikTok** | **Webhook: AFTERSALES_REQUEST_STATUS_UPDATE** <br/> status: `REQUEST_REVIEW_COMPLETED` <br/> [Webhook topic 64 documentation](https://partner.tiktokshop.com/docv2/page/h4cxaxub) |
| ### Once the 1st review process is completed, the official RMA workflow will begin (2nd Review Stage) |  |  |  |
| **2nd Review** <br/>  | **[8]** TikTok RMA Created  | **TikTok** <br/>  | Once the aftersales request has been approved, TikTok will immediately create an RMA, which is a unified return identifyer that encompasses all unique sku lines and quantity associated with the return submission from the buyer |
|  | **[9]** Webhook: `RMA_STATUS_UPDATE` <br/> Webhook topic: **65** <br/>  | **TikTok** | **Webhook: RMA_STATUS_UPDATE** <br/> **status**: **`RMA_CREATED`** <br/> This webhook will trigger as soon as the official TikTok RMA has been created in TikTok's system. <br/> [Webhook topic 65 documentation](https://partner.tiktokshop.com/docv2/page/2f0jrrxc) |
|  | **[10]** Search Return Merchandise Authorization API | **Seller/ISV** | Call this API to obtain the full details of the return, including all return order and line level identifyers.  <br/> [Search Return Merchandise Authorization API documentation](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604) <br/>  |
|  | **[11]** Get External Order References API | **Seller/ISV** | Obtain Seller's OMS order_id to reference with the TikTok order_id <br/> [Get External Order References API documentation](https://partner.tiktokshop.com/docv2/page/get-external-order-references-202406) |
|  | **[12.1]** Create Return API / Workflow | **Seller/ISV** | Create Return API endpoint will vary based on what return platform is being leveraged for the RMA records/label/QR code generation. |
|  | **[12.2]** Return Label / QR Code Generated | **Return Platform** | RMA QR code supplied in response body |
|  | **[13]** Upload Shipping Document API | **Seller/ISV** | Uploads the label/QR code document to TikTok Shop <br/> [Upload Shipping Document API documentation](https://partner.tiktokshop.com/docv2/page/upload-shipping-document-and-tracking-info-202405) |
|  | **[14]** Render QR Code + Email Buyer | **TikTok** | TikTok app will render the QR code within buyers app UX |
|  | **[15]** Sync Return Platform RMA  | **Return Platform** | Return Platform to signal Seller of new RMA (existing integration path) |
|  | **[16]** Buyer Ships/Drop-off items | **TTS Buyer** | Buyer takes items to nearest carrier drop-off or ships items to warehouse |
|  | **[17]** Buyer shipped signal | **Carrier** | Carrier signal confirming the return package/items have shipped/dropped-off |
| ### 2nd review inspection results have 4 possible paths (A,B,C,D) |  |  |  |
| ### **PATH A:** All expected items received and accepted for full refund |  |  |  |
| **PATH A** <br/>  | **[18.A]** WMS updates OMS | **WMS** <br/>  | Warehouse associates inspect items and update the RMA status that all line_items associated with the RMA are in "good' condition <br/>  |
| **PATH A** <br/>  | **[19.A]** OMS updates TikTok Application | **OMS** <br/>  | Based on warehouse items grading results that all items are in good condition, OMS updates the Return app that all items are eligible for full refund amount. <br/>  |
| **PATH A** | **[20.A]** Review Aftersales API <br/>  | **Seller/ISV** | Triggers the refund of all return_line_item_id(s) in the RMA. <br/> request_id_type: `RMA` <br/> action: `APPROVE_RETURN_PACKAGE` <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) |
| **PATH A** | **[21.A]** Refund Buyer  | **TikTok** | Buyer's refund payment is completed |
| ### **PATH B:** Some items don't meet warehouse grading acceptance criteria (some items missing/damaged). |  |  |  |
| **PATH B** <br/>  | **[18.B]** WMS RMA status = Some items graded as "damaged/missing" <br/>  | **WMS** | Warehouse associates inspect items and update the RMA status **some** line_items associated with the RMA are in "good' condition, some are "damaged/missing" |
| **PATH B** <br/>  | **[19.B]** Instruct TTS app with mixed refund decision (all lines) | **OMS** | Based on warehouse items grading results that some line_items are in "good' condition, some are "damaged/missing", update Return platform RMA with partial refunds based on line items. |
| **PATH B** | **[20.B]** Review Aftersales API <br/>  | **Seller/ISV** <br/>  | Triggers the refund of approved line_items and rejection of the line_items that are missing/damaged. When using the "Review Aftersales API", you can define different decision/action enumerations for the different return_line_item_id(s). Example: <br/> return_line_item_id: 111 = Good condition. <br/> action: `APPROVE_RETURN_PACKAGE` <br/> - <br/> return_line_item_id: 222 = damaged/missing <br/> Action: `REJECT_RETURN_PACKAGE`  <br/>  <br/> > **Note**: TTS does **not** allow the same exact sku_id to have **different** decisions (known platform limitation). The seller must make the same action/decision for multiple quantities of the same sku_id. We are solving this platform issue by end of Q3, 2026, to allow truly flexible return_line_item_id decisions regardless of the sku_id profiles. <br/>  <br/>  <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH B** | **[21.B]** Mixed Refund by SKU lines <br/>  | **TikTok** | Buyer's partial refund payment is completed based on different sku_id decisions.  |
| ### **PATH C:** All items don't meet warehouse grading acceptance criteria (missing/damaged).  |  |  |  |
| **PATH C** | **[18.C]** OMS RMA status = All items graded as "damaged/missing" | **WMS** | Warehouse associates inspect items and update the RMA status ALL line_items associated with the RMA are "damaged/missing" |
| **PATH C** | **[19.C]** Instruct TTS app to REJECT RMA (all lines) <br/>  | **OMS** | Based on warehouse items grading results that ALL line_items are in "damaged/missing' condition, update return platform RMA to reject refund of all line items |
| **PATH C** | **[20.C]** Review Aftersales API | **Seller/ISV** | Triggers the rejection of the refund of all line_items within the RMA <br/> request_id_type: `RMA` <br/> action: `REJECT_RETURN_PACKAGE` <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH C** | **[21.C]** Return Refund Rejected (all lines) | **TikTok** | Refund is rejected for all return items and notification is sent to buyer |
| ### **PATH D:** Some quantity of same sku_id do not meet warehouse grading acceptance criteria (missing/damaged). Offer partial refund |  |  |  |
| **PATH D** | **[18.D]** OMS RMA status = Same sku / multiple quantity has different conditions. <br/>  | **WMS** | RMA contains multiple quantities of the exact same sku (SKU:A x 2 QTY) Warehouse associated inspects the package/items and finds that: <br/>  QTY 1 is in good condition <br/>  QTY 2 is completely damaged/or missing altogether.  |
| **PATH D** | **[19.D] Instruct TTS app** `OFFER_PARTIAL_REFUND` <br/>  | **OMS** | Based on warehouse items grading results, 1 QTY should be refunded, 1 QTY should be rejected due to the damage. However, as previously stated, TikTok shop platform has a known gap where we do not allow different refund decisions if there are multiple quantities of the same sku_id. To solve for this platform behavior, OMS must perform calculations to trigger a partial refund amount for each qty/line, which is meant to equate to the total amount the buyer should receive. Example:  <br/> Buyer orders SKU:A x 2 QTY. Each item original cost paid = $10.00 <br/> QTY 1 is received in "good/sellable" condition <br/> QTY 2 is damaged or missing. <br/> - <br/> The seller wants to **approve** QTY 1 and **reject** QTY 2, so that the buyer is only refunded **$10.00** out of the original $20.00 amount paid for both lines. However, the TTS platform/API does not allow different decisions for the same SKU (known platform behavior/limitation).  <br/>  <br/> The seller can use the Review Aftersales API and use the `OFFER_PARTIAL_REFUND` enumeration for both lines. However, OMS logic **must** calculate the amount using the formula  <br/> (Total amount to refund buyer) / (total # of return_line_item_ids) <br/> Example from above: <br/> $10.00 (total amount to refund buyer) / (2 return_lines) = $5.00 <br/> The `OFFER_PARTIAL_REFUND` amount will be `5.00` for **both** lines of the same SKU, to ensure the buyer will receive $10.00 for their refund amount. <br/>  |
|  **PATH D** | **[20.D]** Review Aftersales API <br/>  | **Seller/ISV** | Triggers `OFFER_PARTIAL_REFUND` action for all line_items of that same SKU <br/> request_id_type: `RMA` <br/> action: `OFFER_PARTIAL_REFUND` <br/> - <br/> Within the `alternative_solutions_details` object: <br/> Define `partial_refund_amount` & `currency` <br/>  <br/> [Review Aftersales API documentation](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **PATH D** | **[21.D]** Buyer is refunded the accurate partial amount | **TikTok** | Partial refund amount and notification is sent to buyer |
| **PATH D** |  |  | **Buyer Appeasement Use-Case** <br/> The `OFFER_PARTIAL_REFUND` can also be used as an appeasment mechanism. For example <br/> **IF**: the buyer was only expected to send back SKU A, QTY 1, but the item was slightly damaged, noticeably worn, package slightly damaged etc <br/> **THEN**: the seller can make a decision to `OFFER_PARTIAL_REFUND` for that single return_line_item_id, and TikTok will refund that buyer the amount specified by the seller.  |




# **Exchanges**
TikTok buyers have the ability to perform an exchange, which is initiated through their return journey within the TikTok application. This allows sellers to save GMV, rather than just giving a refund for a returned item. When a buyer submits an exchange, there are API fields within the Returns & Orders API that identify an exchange is required.
| **Markets** <br/>  | * United States (US) <br/> * United Kingdom (UK) |
| --- | --- |
| **Returns APIs** | **Parameter Update** |
| --- | --- |
| [Search Returns API](https://partner.tiktokshop.com/docv2/page/search-returns-202602) <br/> [Search Aftersales Request API](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603#Back%20To%20Top) <br/> [Search Return Merchandise Authorization API](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604#Back%20To%20Top) <br/> [Webhook Topic: Return Status Change](https://partner.tiktokshop.com/docv2/page/12-return-status-change) <br/>  | 1. Added the following enumeration to the `return_type`field: <br/>    * `EXCHANGE` <br/> 2. Added the following enumerations to the `return_status` field: <br/>    * `EXCHANGE_REQUEST_PENDING` <br/>    * `EXCHANGE_REQUEST_REFUND_SUCCESS` <br/>    * `EXCHANGE_REQUEST_CANCEL` <br/>    * `EXCHANGE_REQUEST_COMPLETE` |
|  |  |
|  |  |
| [Get Decision Eligibility API](https://partner.tiktokshop.com/docv2/page/get-decision-eligibility-202601) | 1. Added the following enumeration to the `check_decisions` and `decision` fields: <br/>    *  `ISSUE_EXCHANGE_REFUND` |

| **Orders API Endpoints** | **Parameter Update** |
| --- | --- |
| [Get Order Details API](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507) <br/> [Get Order List API](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) <br/>  <br/>  | 1. `is_exchange_order` : When `true`, this is an exchange order that the seller must fulfill. <br/> 2. `exchange_source_order_id`: If the order is an exchange order, this field returns the original order's order ID, from which the exchange order was generated. Surfaced only if `is_exchange_order`= `true` <br/>  <br/>  <br/> > ***Notes****: When the buyer has shipped/dropped-off the return with the logistics carrier, that signal from the carrier integration with TikTok will confirm the package is in transit, and TikTok will the automatically create the new exchange order.* <br/> > *This new outbound order will also have a $0.00 order value, because the payment/GMV was previously captured within the original* *`order_id`**, and there are no financial transactions required, as TikTok only currently allows exchanges for items with the same exact dollar value.* <br/>  <br/> ` |
|  |  |
|  |  |


> ### **4PL Model: Exchange workflow** 


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/04cede45a9cf4e0fa802a39d4e1a6613~tplv-k9wyc2ijk0-image.image)



1. When a buyer initiates an exchange, they will select which SKU they no longer want, and then select which SKU they want to receive for the exchange. 
2. Once the exchange is submitted, TikTok Shop will create a new `rma_id` associated with the buyer's request and trigger the RMA Status Update webhook with status `rma_created`
   1. TikTok will generate a return shipping label and share that to the buyer's app and email
3. Sellers system to call Search Return Merchandise Authorization API to capture full RMA details:
   1. The `return_type` parameter = `EXCHANGE`
   2. This will allow the seller's OMS to understand the specific use-case of this return being created.
4. The buyer will ship the return (or drop-off) with the specific carrier they selected during the return check-out
5. This carrier shipped/dropped-off signal is synced to TikTok, confirming the buyer has performed their action to return the item
6. Upon receiving the carrier signal, TikTok will **automatically** create a new outbound order for SKU-B. Within the **Get Order Details API & Get Order Lists API,** there are two parameters that identify the exchange scenario:
   1. `is_exchange_order`: Boolean
   2. `exchange_source_order_id`: Original order's order ID, from which the exchange order was generated. Returned only if `is_exchange_order` = `true`.
7. The seller's warehouse is expected to fulfill the order with the exchange item once they receive the order data for this exchange. 



> ### **3PL Model Exchange workflow**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b04ff2f23027418ca033c577d0b8a168~tplv-k9wyc2ijk0-image.image)



1. When a buyer initiates an exchange, they will select which SKU they no longer want, and then select which SKU they want to receive for the exchange. 
2. Once the exchange is submitted, TikTok Shop will create a new `rma_id` associated with the buyer's request and trigger the RMA Status Update webhook with status `rma_created`
   1. TikTok will **not** generate a return shipping label, and we are expecting the seller's external system/return app to provide the label/
3. Sellers system to call Search Return Merchandise Authorization API to capture full RMA details:
   1. The `return_type` parameter = `EXCHANGE`
   2. This will allow the seller's OMS to understand the specific use-case of this return being created.
4. Sellers system/Return app will generate a return shipping label and upload it back to TikTok using the Upload Shipping Document API
5. The buyer will ship the return (or drop-off) with the specific carrier they selected during the return check-out
6. This carrier shipped/dropped-off signal is synced to TikTok, confirming the buyer has performed their action to return the item
7. Upon receiving the carrier signal, TikTok will **automatically** create a new outbound order for SKU-B. Within the **Get Order Details API & Get Order Lists API,** there are two parameters that identify the exchange scenario:
   1. `is_exchange_order`: Boolean
   2. `exchange_source_order_id`: Original order's order ID, from which the exchange order was generated. Returned only if `is_exchange_order` = `true`.
8. The seller's warehouse is expected to fulfill the order with the exchange item once they receive the order data for this exchange. 


# FAQ for Exchanges
**Question 1:** TikTok automatically creates the exchange outbound order as soon as the buyer ships the return package. What happens if I receive the return package, and my warehouse inspects the item(s) to find them either damaged or missing? What processes do I have to dispute with the buyer and TikTok?
**Answer:** As a seller, you can submit an arbitration process to dispute the damaged/missing items you were expecting to receive for this exchange. 

**Question 2:** Is this a breaking change?
**Answer:** No. This is an additive response field. Existing integrations will continue to work

**Question 3**: Does my app need a new authorization scope? 
**Answer:** Apps that already call Returns & Order scopes do not need new authorization. 
