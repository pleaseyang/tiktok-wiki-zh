# Seller Center development shops

Seller Center Development Shops let developers create Seller Center test accounts for TikTok Shop API development. These test accounts are created under a Partner Center account and are separate from production seller accounts. Development shops are not discoverable by regular TikTok users in the production TikTok app.
Use this guide to choose the right test account type, create test shops, authorize your app, and generate test product and order data.
# Quick start
Use the current Partner Center path:
**Partner Center Console > Development Kits > Development Shops**
| Task | Path |
| --- | --- |
| Create a Core or Full Function test account | **Development Kits > Development Shops > Manage accounts > Create test account** |
| Enter a test shop or authorize an app | **Development Kits > Development Shops > Manage accounts**  |
| Link a customer(buyer) Test TikTok Account | **Development Kits > Development Shops > Manage accounts > Settings (button)** |

Older screenshots or documents may show **Development Kits > Development Shops**. Treat **Development Shops** as the previous menu name for the Sandbox test-account area.

## **Create test seller account**
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4e741e5e315348c8beb9377ad1f05881~tplv-k9wyc2ijk0-image.image)

## **Authorize app**
> Note: Your app market must include the market where the sandbox is located as well as the seller type; otherwise, authorization will fail.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/81521c8a370b4535bb99dee5479786f0~tplv-k9wyc2ijk0-image.image)

## **Link customer(buyer) test account**
> Note：This action is permanent. Once the TikTok account is linked in development shops, it will be turned into a test account permanently. Unlinking in the future will not reverse this account. You must use a newly created TikTok when linking. Test accounts cannot be linked to production Seller Center accounts. Attempting to do so could severely affect your business operations.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c0c3bd107e434d5b90acabb7b8edeaac~tplv-k9wyc2ijk0-image.image)

# Core vs Full Function accounts
| Question | Choose Core Function Account | Choose Full Function Account |
| --- | --- | --- |
| Main goal | Product, order, fulfillment, cancellation, and return API testing with generated test data. | Full-flow testing that more closely resembles production Seller Center and TikTok app buyer behavior. |
| Business / KYC information | Not required for basic setup. | Required. Business and KYC information must be valid and may be reviewed. |
| TikTok account setup | Not required. | Required for Official Test TikTok Account and Buyer Test TikTok Account scenarios. |
| Payment | No real payment or credit card required. Test orders are created in Buyer View. | Real buyer checkout flow can be tested with Buyer Test TikTok Accounts and payment methods. Use very low test prices, such as `$0.01`. |
| TikTok app product discovery | Not supported through regular buyer accounts. | Supported only through linked test TikTok accounts. |
| Finance, settlements, customer service, and full production-like flows | Not supported or not suitable. | Supported for testing after Full Function setup is complete. |
| Best for | API integration testing for product listing, order updates, fulfillment, cancellations, and returns. | Testing buyer experience, product discovery, payment, settlement, customer service, and end-to-end flows. |
Decision guide:

1. If you only need products, orders, fulfillment, cancellations, or returns without real payment, use **Core Function Account**.
2. If you need TikTok app discovery, buyer checkout, real payment, settlement, customer service, or production-like verification, use **Full Function Account**.
3. If you cannot provide business/KYC information or region-matched TikTok test accounts, start with **Core Function Account**.
4. If an issue reproduces only in the TikTok app buyer journey, use **Full Function Account** with linked test TikTok accounts.

> **Important Core Function limitation:** In **Core Function Account** mode, the sandbox provides built-in tools to directly advance forward and reverse order statuses. Because these tools simulate state changes, some flows may be inconsistent with or not fully aligned with the production environment. Use Core Function mode for core API functionality testing. Use Full Function mode for full-flow or detail-level verification.


# FAQ before setup
This section covers frequent Sandbox and Developer Tool support issues: test account creation, irreversible TikTok account conversion, and region, SIM card, or VPN restrictions.
## Can I use the same TikTok account for production and testing?
Do not use production or personal TikTok accounts for Full Function testing. Once a TikTok account is linked as an Official Test TikTok Account or Buyer Test TikTok Account, it is converted into a test account. This action is permanent and cannot be reversed. The account can no longer be used normally in the TikTok app or TikTok Shop production environment.
## Why does linking a TikTok account fail?
The TikTok account region must match the test shop region. When creating or linking the TikTok account, your physical location should match the test shop country or region. If you cannot be physically located in that region, remove the SIM card from your device and use a VPN with an IP address in the test shop region before creating or linking the TikTok account.
## Why can't I find test products in the TikTok app?
This applies to Full Function testing. Search with the linked Buyer Test TikTok Account, not a regular TikTok account. Also check that the product is published, does not contain prohibited or random test keywords, and that the device location matches the shop region.
## Why does checkout show an error such as "Something went wrong"?
For Full Function orders, check that the buyer test account is linked correctly, the buyer device region matches the shop region, and the payment method is available. If you cannot be physically in the same region as the shop, remove the SIM card and use a VPN with an IP address in that region.
# What you can test
| Capability | Core Function Account | Full Function Account |
| --- | --- | --- |
| Create products | Yes | Yes |
| Create test orders without payment | Yes, through Buyer View | No, use buyer checkout flow instead |
| Place buyer orders with real payment | No | Yes, through linked Buyer Test TikTok Account |
| Fulfill orders | Yes | Yes |
| Process returns and refunds | Yes | Yes |
| Product discovery in TikTok app | No | Yes, through linked test TikTok accounts |
| Financial statements and settlements | No | Yes |
| Customer messaging services | No | Yes |
# Supported markets and seller types
Seller Development Shops are available for cross-border and local shops.
**Note:** The table reflects the supported regions for Core Function Accounts. For Full Function Accounts, the supported local regions are the same as Core Function Accounts, while cross-border seller support is currently unavailable.
| Country/Region | Country Code | Cross-border | Local |
| --- | --- | --- | --- |
| Austria | AT (40) | Yes | Yes |
| Belgium | BE (56) | Yes | Yes |
| Brazil | BR (76) | No | Yes |
| Czech Republic | CZ (203) | Yes | Yes |
| France | FR (250) | Yes | Yes |
| Germany | DE (276) | Yes | Yes |
| Greece | GR (300) | Yes | Yes |
| Hungary | HU (348) | Yes | Yes |
| Indonesia | ID (360) | No | Yes |
| Ireland | IE (372) | Yes | Yes |
| Italy | IT (380) | Yes | Yes |
| Japan | JP (392) | Yes | Yes |
| Malaysia | MY (458) | Yes | Yes |
| Mexico | MX (484) | Yes | Yes |
| Netherlands | NL (528) | Yes | Yes |
| Philippines | PH (608) | Yes | Yes |
| Poland | PL (616) | Yes | Yes |
| Portugal | PT (620) | Yes | Yes |
| Singapore | SG (702) | Yes | Yes |
| Vietnam | VN (704) | Yes | Yes |
| Spain | ES (724) | Yes | Yes |
| Thailand | TH (764) | Yes | Yes |
| United Kingdom | GB (826) | Yes | Yes |
| United States | US (840) | Yes | Yes |
# Terminology
| Term | Definition |
| --- | --- |
| Seller Center Development Account | A Seller Center test account created under Partner Center for development and testing. Events and data in development accounts do not affect production seller accounts. There are two types: Core Function Account and Full Function Account. |
| Core Function Account | A lightweight test account that does not require real business information, TikTok account setup, or credit card information. It is used mainly for product, order, and fulfillment testing inside Partner Center. It does not support real buyer checkout, finance, settlement, or customer-service scenarios. |
| Full Function Account | A production-like test account that requires business and KYC information. It supports Core Account capabilities plus linked Official Test TikTok Accounts and Buyer Test TikTok Accounts. Use it for buyer checkout, product discovery, finance, settlement, customer service, and full-flow testing. |
| TikTok Account | An account created in the TikTok app with an email address or phone number. For testing, create new TikTok accounts and do not use production accounts. |
| Official Test TikTok Account | A TikTok account linked to a Full Function test shop as the shop's official account. After linking, the account is converted into a test account and cannot return to production use. |
| Buyer Test TikTok Account | A TikTok account linked in Partner Center for buyer-side testing. It can search for the test shop, view products, and place test orders in Full Function scenarios. After linking, it is permanently converted into a test account. |
| Shop Type | The seller model and market type of the test shop, such as **Local** or **Cross-border**. Local shops operate in one local market. Cross-border shops represent cross-border seller scenarios where supported. |
| Onboarding Type | The account entity type used during setup, such as **Individual** or **Business**. For Core Function testing, this does not change available functionality. For Full Function testing, business/KYC requirements may vary by market and account context. |
# Setup overview
Most API integration tests require product data and order data. To create this data, use one of the following setups:
| Setup | Assets needed |
| --- | --- |
| Core Function testing | Seller Center Core Function Account |
| Full Function testing | Seller Center Full Function Account, Official Test TikTok Account, and Buyer Test TikTok Account |
After setup, authorize your app with the test shop, create products, create or place orders, and then validate API behavior against the generated test data.
# Core Function Account setup
## Core Function features
Core Function Accounts:

* require minimal setup information;
* do not require TikTok Official or Buyer Test TikTok Accounts;
* do not require payment methods or credit cards;
* support core testing for product listing, order updates, fulfillment, cancellations, and returns;
* should not be used for finance, settlement, customer-service, real checkout, or production-like buyer journey validation.

## Create a Core Function Account

1. In Partner Center Console, go to **Development Kits > Sandbox > Seller test accounts**.
2. Click **Create test account**.
3. Select **Core Function**.
4. Select the **Shop Type**, such as **Local**, based on the target seller scenario.
5. Provide an **Account Nickname**.
6. Select the **Onboarding Type**, such as **Individual** or **Business**.
7. Wait for the Seller Center test account setup to finish.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e58d92b9830a4cc8b0a9dbddfa2e61ff~tplv-k9wyc2ijk0-image.image)
## Authorize your app with a Core Function test shop

1. Go to **Development Kits > Sandbox > Seller test accounts**.
2. In the seller test account section, click **Authorize app**.
3. Select the app that you want to test with this shop.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/854f31907af145ae9c20070ca8459c40~tplv-k9wyc2ijk0-image.image)
## Add and manage products
Create a product in the Core Function test account by entering the required TikTok Shop product information and clicking **Submit for review**. You can also use the Create Product API to create products for the development shop.
After products are created, manage and verify them from the **Products** tab inside the Core Function Seller Center.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a3b85f88ba644df79426a97e4bccde0b~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/cacd3bc3ac9b4c7096887d2f5042c755~tplv-k9wyc2ijk0-image.image)
Only products in **Active** status can be used for Core Function test orders.
## Add shipping templates for seller shipping
**Note:** The screenshots in this section are for the US. Menu options may differ by market.

1. In the Core Function Account, go to **Orders > Shipping Options**.
2. Select TikTok Shipping or Seller Shipping.
3. If Seller Shipping is selected, go to **Orders > Shipping Templates** and set up a shipping template that includes the required buyer regions.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4961c665fe8a44198437732d9f968854~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e9ac605b68e4ffd894c68bfe33d0e78~tplv-k9wyc2ijk0-image.image)
For more information, see [TikTok Shipping and Seller Shipping settings](https://seller-us.tiktok.com/university/essay?knowledge_id=2921116620719915&role=1&course_type=1&from=search&identity=1).
## Use Buyer View to create Core Function test orders
Buyer View lets you trigger test orders without real buyer payment.

1. Click **Create test order** in Buyer View.
2. Select the products for the test order. A test order can include up to 3 products.
3. Select the shipping option for the order.
4. After the test order is created, it appears in Buyer View with **On Hold** status.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3d2c9357a0ee4e21ac552129468f0adb~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a77d72556fa54e089cb763def0e6213f~tplv-k9wyc2ijk0-image.image)
## Test cancellations, returns, and fulfillment
Buyer View supports simulated buyer actions for supported order states:
| Test action | Requirement |
| --- | --- |
| Cancel order | The order must be in **On Hold** or **Awaiting Shipment** status. |
| Request refund or return | The order must be in a supported status such as **Awaiting Collection**, **In Transit**, or **Delivered**. |
Developers can respond to return requests through the API or through **Orders > Manage Returns**.
For order management guidance, see:

* [Manage orders](https://seller-us.tiktok.com/university/essay?knowledge_id=7774796412471041&role=1&course_type=1&from=search&identity=1)
* [Manage returns](https://seller-us.tiktok.com/university/essay?knowledge_id=6837901778454274&role=1&course_type=1&from=search&identity=1)

# Full Function Account setup
## Full Function features
Full Function Accounts:

* include Core Function testing features;
* require valid business and KYC information;
* require full Seller Center setup before production-like flows can be tested;
* can be linked to Official Test TikTok Accounts and Buyer Test TikTok Accounts;
* support product discovery and buyer checkout in the TikTok app through linked test accounts;
* support real payment test orders, finance, settlements, customer service, and other full-flow API testing.

## Requirements before creating Full Function accounts
Before creating a Full Function Account, prepare the required business and KYC information and test accounts. You do not need to create an app in advance. 

* Provide valid business and KYC information. 
* Register at least two new TikTok accounts for testing: one for the Official Test TikTok Account and one for the Buyer Test TikTok Account.
* Use testing email addresses. Do not use personal, production, or high-value TikTok accounts.
* Prepare region-matched device/network conditions for TikTok account creation and linking.

If you cannot provide the required information or region-matched TikTok accounts, use Core Function Accounts first.
## Create a Full Function Account

1. In Partner Center Console, go to **Development Kits > Sandbox > Seller test accounts**.
2. Click **Create test account**.
3. Select **Full Function**.
4. Select the **Shop Type**, such as **Local**, based on the target seller scenario.
5. Provide an **Account Nickname**.
6. Click **Go to Seller Center** and complete [Seller Center onboarding](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10013682&role=1&identity=1).

If you are a seller developer and already have a TikTok Shop linked to your Partner Center account, you may not see the Seller Center onboarding step.
For US and UK Seller Center test accounts:

* US: To publish new products in your test shop, provide the required tax information in Seller Center.
* UK: To receive payouts from TikTok Shop, fill out the tax information for the Seller Center test account.
* After creating test shops, default pickup warehouses are set automatically. You still need to set shipping templates. See [Set up shipping](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10012875&role=1&identity=1).

## Link an Official Test TikTok Account

1. Create a new TikTok account in the TikTok app. Use a testing email address.
2. Do not use a production TikTok account.
3. Link the TikTok account as the test shop's Official TikTok Account.
4. For account-linking details, see [How to link TikTok Shop Official Account](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10012412&role=1&identity=1).

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b471be6835d449b7ba92cf0f09dd6be8~tplv-k9wyc2ijk0-image.image)
**Do not link the account as a Marketing Account for app testing.** Marketing Accounts have additional restrictions for merchandise and shop visibility.
## Link a Buyer Test TikTok Account

1. Create a second new TikTok account in the TikTok app. Use a testing email address.
2. Log into the TikTok app with the account you want to use as the buyer test account.
3. In Partner Center, go to **Development Kits > Sandbox > Buyer test accounts**.
4. Click **Link account**.
5. Use the TikTok app to scan the QR code on the **Link TikTok account as buyer account** page.
6. Follow the **Authorize TikTok Partner Center** process in the TikTok app.
7. Click **Link the account** on the buyer-account linking page.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/08010af0a24a4e6792370acb942fbc6c~tplv-k9wyc2ijk0-image.image)
## Region and account-conversion rules
Use these rules for both Official Test TikTok Accounts and Buyer Test TikTok Accounts:

* The TikTok account region must match the test shop region.
* Your physical location should match the test shop region when creating and linking the TikTok account.
* If you cannot be physically located in the same region, remove the SIM card from your device and use a VPN with an IP address in the test shop region before creating or linking the TikTok account.
* After a TikTok account is linked in Sandbox, it is permanently converted into a test account.
* A converted test account cannot be used normally in the TikTok app or TikTok Shop production environment.
* Use new testing email addresses and keep Official Test TikTok Accounts separate from Buyer Test TikTok Accounts.

# Using Full Function Account to test your app
## Authorize your app

1. Go to **Development Kits > Sandbox > Seller test accounts**.
2. In the seller test account section, click **Authorize app**.
3. Select the app you want to install and test with the test shop.

## Add and publish products
Add and publish products by following production rules. For US test shops, tax information must be submitted before products can be published.
Do not use random strings, the word "test", or prohibited keywords in product titles. Products may be flagged even if they appear published in Seller Center.
## Find products in TikTok
Use the linked Buyer Test TikTok Account to search for the Official Test TikTok Account in the TikTok app. Only linked test accounts can find and interact with the test shop's products. Regular TikTok accounts cannot find the development shop.
If products do not appear:

* confirm that the product is published;
* check whether the title or content was flagged;
* confirm that the buyer account is linked correctly;
* confirm that the device region matches the shop region.

## Create orders with real payment
Full Function test orders are placed through the TikTok app buyer journey.

1. Add a payment method to the Buyer Test TikTok Account.
2. Set a very low product price, such as `$0.01`.
3. Log into the TikTok app with the Buyer Test TikTok Account.
4. Search for the test shop's Official Test TikTok Account.
5. Open the **Shop** tab from the account profile page.
6. Select the test product and complete the purchase.

If checkout fails, check the buyer account linking status, device region, SIM card, VPN, payment method, and product publish status.
## Manage orders
After payment is completed, manage the order in **Seller Center > Orders > Manage orders**. You can fulfill the order through the API according to your app's test cases.
For more details, see:

* [Manage orders](https://seller-us.tiktok.com/university/essay?knowledge_id=7774796412471041&identity=1)
* [Manage seller arranged shipping](https://seller-us.tiktok.com/university/essay?knowledge_id=6837882170099457&identity=1)
* [Manage TikTok Shop logistics shipping](https://seller-us.tiktok.com/university/essay?knowledge_id=8706274700117762&identity=1)

If you need to test order settlement, revenue sharing, or other finance-related functions, use a **Full Function Account**.
# Limitations

1. You can create up to 10 Seller Center test accounts across Full Function and Core Function Accounts.
2. Seller Center Development Shops expire in 180 days but can be reactivated in Partner Center.
3. You can link up to 10 TikTok accounts as Buyer Test TikTok Accounts to one Partner Center account.
4. Buyer Test TikTok Accounts linked to a Partner Center account can be used with any test shop you create in Sandbox.
5. You need at least two real TikTok accounts for Full Function testing: one Official Test TikTok Account and one Buyer Test TikTok Account.
6. You cannot use the same TikTok account as both the Official Test TikTok Account and the Buyer Test TikTok Account.
7. The API call quota for a sandbox shop is QPH < 18,000, exceeding this limit will result in a rate-limiting error.


