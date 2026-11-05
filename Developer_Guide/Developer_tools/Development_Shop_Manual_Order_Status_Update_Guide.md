# Development Shop Manual Order Status Update Guide

# Document Overview
This guide applies to merchants, testers, and developers working in the Full Function Account development shop environment. It explains how to manually simulate order status progression for test orders placed through the TikTok App, without relying on real fulfillment operations such as warehousing or logistics.
Use this guide when you need to validate end-to-end order status display, fulfillment callbacks, cancellation, or refund behavior in a development shop.
# 1. Feature Overview
In the Development Shop environment, merchants usually cannot rely on real fulfillment events to drive order status changes. The manual order status update capability allows testers to trigger status progression manually in Partner Center for test orders created from the TikTok App.
It covers both the forward flow, from order placement to delivered, and the reverse flow, including order cancellation and refund. This lets teams validate business logic and front-end status display end to end in the sandbox.
| Dimension | Description |
| --- | --- |
| Applicable environment | Development Shop, Full Function Account |
| Supported markets | Local Full Function Account development shops. See the country-level table below. |
| Supported flows | Forward flow and reverse flow |
| Entry point | Development Shop order management page in Partner Center / Seller Center |
| Target users | Merchant testers, developer debugging engineers, and operation reviewers |
## 1.1 Supported Markets
Use the same country-level market scope as the Seller Center Development Shops guide. For Full Function Accounts, supported local regions are the same as Core Function Accounts, while cross-border seller support is currently unavailable.
| Country/Region | Country Code | Full Function Local |
| --- | --- | --- |
| Austria | AT (40) | Supported |
| Belgium | BE (56) | Supported |
| Brazil | BR (76) | Supported |
| Czech Republic | CZ (203) | Supported |
| France | FR (250) | Supported |
| Germany | DE (276) | Supported |
| Greece | GR (300) | Supported |
| Hungary | HU (348) | Supported |
| Indonesia | ID (360) | Supported |
| Ireland | IE (372) | Supported |
| Italy | IT (380) | Supported |
| Japan | JP (392) | Supported |
| Malaysia | MY (458) | Supported |
| Mexico | MX (484) | Supported |
| Netherlands | NL (528) | Supported |
| Philippines | PH (608) | Supported |
| Poland | PL (616) | Supported |
| Portugal | PT (620) | Supported |
| Singapore | SG (702) | Supported |
| Vietnam | VN (704) | Supported |
| Spain | ES (724) | Supported |
| Thailand | TH (764) | Supported |
| United Kingdom | GB (826) | Supported |
| United States | US (840) | Supported |
Market-specific UI text, shipping settings, tax requirements, payment behavior, and test assets may still vary by country. Always use the test product deeplink, buyer test account, and shop account that belong to the same country as the development shop.
# 2. Prerequisites
## 2.1 Environment Requirements

* You have a Full Function Account development shop.
* The development shop setup is complete in Partner Center / Seller Center.
* The buyer account used to log in to TikTok App has already been linked to the Development Shop.
* The buyer account, official test account, test product, and development shop belong to the same country/region.

## 2.2 Test Product Preparation
Before placing an order in TikTok App, make sure a product has already been successfully published in the development shop.
Acceptance criteria:

* The product is visible to the linked buyer test account in TikTok App.
* The product can be added to cart.
* The full checkout and payment flow can be completed in the test environment.

# 3. Workflow Overview
The following diagram shows the full path for manually driving order status changes in the sandbox after an order is placed in TikTok App, including both forward and reverse flows.
Text version of the workflow:

1. Create a test order in TikTok App with the linked buyer test account.
2. Confirm that the order appears in Partner Center / Seller Center with status **On Hold**.
3. Choose one of the following paths:
   * Forward flow: **On Hold -> Pending Shipment -> Awaiting Collection / In Transit -> Delivered**.
   * Seller-side reverse flow: **On Hold / Pending Shipment -> Cancelled**, or refund request -> merchant approval -> refund status update.
   * Consumer-side reverse flow: buyer cancels the order in TikTok App -> backend order status updates to **Cancelled**.
4. After each action, verify the corresponding order status in both the backend and TikTok App.
5. Run regression validation for backend-created orders to ensure existing order operations still work.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f90f283ffc2f41d1a6e4bb72fa6154cc~tplv-k9wyc2ijk0-image.image)
# 4. Detailed Steps
## 4.1 Step 1: Place an Order in TikTok App and Confirm It in Partner Center
First, place an order through the buyer account in TikTok App, then confirm that the order has been synced to the development shop backend.

1. Use the buyer account to open the product detail page in TikTok App.
2. Complete the full process: select SKU, add to cart, place the order, and finish payment.
3. Go to the development shop backend and open **Order Management**.
4. Search for the order ID or filter by time.
5. Confirm that the order is visible and the status is **On Hold**.

Text alternative to the screenshot:

* In Partner Center / Seller Center, the test order should appear in the order list.
* The order detail page should show the order ID, buyer information, product information, and current status.
* The expected initial status for this flow is **On Hold**.

Acceptance criteria: The order placed in TikTok App can be found in Partner Center and the status is synced correctly, which means the TikTok App order placement path is working as expected.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b65c33efef574d498e6306d8678348d0~tplv-k9wyc2ijk0-image.image)
## 4.2 Step 2: Forward Flow - Manually Drive Status Progression in the Backend
### 4.2.1 On Hold -> Pending Shipment

1. Find the target order in the backend. The current status should be **On Hold**.
2. Open the order details page and locate the **manual status push** action button.
3. Select **Pending Shipment** and confirm the submission.
4. Open **My Orders** in TikTok App and verify that the order status has been updated to **Pending Shipment**.

Text alternative to the screenshots:

* The backend order detail page should expose a manual status push action when the order is eligible.
* After you submit the target status, the backend status should change first.
* TikTok App should then show the same target status after synchronization.

Note: After the backend status is pushed manually, the TikTok App status is usually synced within a few seconds. If the update is not visible yet, wait briefly and refresh the page.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/25a87058567f40869aa990ced2c6d037~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/26403bcf61ba453997c1abe3047c7993~tplv-k9wyc2ijk0-image.image)
### 4.2.2 Pending Shipment -> Awaiting Collection -> In Transit

1. Confirm that the current order status is **Pending Shipment**.
2. Click **Ship Order** in the backend.
3. Fill in simulated logistics information. The tracking number can be a test value.
4. Submit the shipment information.
5. Confirm that the backend status changes to **Awaiting Collection / Shipped**.
6. Continue to manually push the order to **In Transit** when the action is available.
7. Verify that the corresponding order status in **My Orders** in TikTok App is updated accordingly.

Text alternative to the screenshot:

* The backend should show a **Ship Order** action for orders in **Pending Shipment**.
* The simulated logistics form should include the fields required by the market, such as carrier and tracking number.
* After shipping information is submitted, the status should move into the shipment stage and can be progressed to **In Transit**.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a5e21a5dbebc4630a2384187b85c5768~tplv-k9wyc2ijk0-image.image)
### 4.2.3 In Transit -> Delivered

1. Confirm that the current order status is **In Transit**.
2. Manually push the order to **Delivered** in the backend.
3. Verify in TikTok App that the order status is updated to **Delivered**.
4. Confirm that the forward flow is complete.

Text alternative to the screenshots:

* The backend should allow the final manual progression only after the order reaches the shipment stage.
* The expected final status in both backend and TikTok App is **Delivered**.

Acceptance criteria: After each manual status push in the backend, the order status in TikTok App is updated accordingly, which confirms that the forward status sync path is working properly.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/99fa0f6200474aafb821328a7952c446~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1e89b9064a1a4ed0bcbf358d8da301e3~tplv-k9wyc2ijk0-image.image)
## 4.3 Step 3: Reverse Flow - Initiate Cancellation or Refund from the Backend
### 4.3.1 Cancel an Order

1. Find the target order in the backend when the status is **On Hold** or **Pending Shipment**.
2. Click **Cancel Order**.
3. Select a cancellation reason and confirm the submission.
4. Verify in TikTok App that the order status is updated to **Cancelled**.

Acceptance criteria: Both backend and TikTok App show **Cancelled** for the target order.
### 4.3.2 Initiate a Refund

1. Find the target order in the backend and click **Initiate Refund**.
2. Fill in the refund reason and refund amount.
3. Submit the refund request.
4. In the Seller Center refund management page, locate the request and click **Approve Refund**.
5. After refund approval is completed, verify in TikTok App that the refund status has been updated.

Important: The refund flow requires two backend actions: **submit the refund request** and **approve the refund as the merchant**. The TikTok App status changes only after the approval step is completed.
## 4.4 Step 4: Reverse Flow Initiated in TikTok App - Cancellation Synced Back to the Backend
This test case verifies whether a cancellation initiated by the user in TikTok App is synced back to the backend correctly.

1. Use a test account to place an order in TikTok App.
2. Confirm in the backend that the order has been created with status **On Hold**.
3. In **My Orders** in TikTok App, find the order and click **Cancel Order**.
4. Complete the cancellation in TikTok App.
5. Switch to Seller Center.
6. Refresh the order list and confirm that the order status has been updated to **Cancelled**.

Acceptance criteria: After the cancellation is initiated in TikTok App, the backend order status is updated successfully, which confirms that the reverse status callback path from TikTok App is working correctly.
## 4.5 Step 5: Regression Validation for Existing Online Capability
After completing the TikTok App-related test cases above, also run regression testing for the existing forward and reverse flows of backend-created orders to make sure the new feature does not affect the original order operation path.

1. Use **Create Order Manually** in the backend to create a test order that is not placed through TikTok App.
2. Execute the full forward flow: **On Hold -> Pending Shipment -> In Transit -> Delivered**.
3. Create another test order and execute the reverse flow: **Cancel / Refund**.
4. Confirm that all existing functions still work correctly and there are no regression issues.

# 5. Quick Reference: Status Transitions
| Action type | Starting status | Target status | Entry point |
| --- | --- | --- | --- |
| Forward | On Hold | Pending Shipment | Backend -> Order details -> Manual status push |
| Forward | Pending Shipment | Awaiting Collection / In Transit | Backend -> Ship Order |
| Forward | In Transit | Delivered | Backend -> Manual progression |
| Reverse | On Hold / Pending Shipment | Cancelled | Backend -> Cancel Order |
| Reverse | Any status eligible for refund | Refunding / Refunded | Backend -> Initiate Refund -> Approve Refund |
| Consumer-side reverse | On Hold | Cancelled | TikTok App -> My Orders -> Cancel Order |
# 6. FAQ
## Q1: I Cannot Find the Order in the Backend After Placing It in TikTok App. What Should I Do?

* Confirm that the logged-in development shop account and the shop used in TikTok App are the same shop.
* Confirm that the correct country/region is selected. Orders are not shared across development shop countries.
* Confirm that the buyer test account, official test account, test product, and development shop belong to the same country/region.
* Confirm that the payment flow in TikTok App has been fully completed, including payment confirmation. Unpaid orders will not be synced to the backend.
* Wait about 30 seconds, refresh the order list in the backend, and try again.

## Q2: The TikTok App Order Status Does Not Update After I Manually Push the Status. How Should I Handle It?

* Wait 10 to 30 seconds and manually refresh **My Orders** in TikTok App.
* Check whether the backend status push was submitted successfully and whether the backend order status has changed.
* If the backend status has changed but TikTok App is not updated yet, this is likely due to delayed status delivery. Wait a little longer or ask the technical team to check the message queue.

## Q3: Are the Test Flows the Same Across Supported Countries?
Yes. The core process is the same across supported Full Function local development shop countries. The differences are usually market-specific test assets, tax setup, shipping settings, payment behavior, menu text, or eligibility of specific backend actions.
Use the test product deeplink, shop account, buyer test account, and official test account for the corresponding country. Confirm required market-specific test assets with the business owner before testing.
## Q4: Why Does the TikTok App Status Not Change During the Refund Flow?

* The refund flow requires two actions in Seller Center: **submit refund request** and **approve refund**.
* If only the refund request is submitted, the TikTok App status will not change immediately.
* Make sure the request has been found on the refund management page and **Approve Refund** has been clicked.

## Q5: Will the Sandbox Manual Status Push Capability Affect Production Data?
No. Sandbox and production are fully isolated. The development shop environment is isolated from production, and all test operations will not affect real orders or real user data.
## Q6: Does This Feature Support Bulk Manual Status Pushing?
The current feature is designed mainly for single-order operations. If bulk verification is needed, repeat the process order by order or confirm with the engineering team whether a bulk interface is available.
