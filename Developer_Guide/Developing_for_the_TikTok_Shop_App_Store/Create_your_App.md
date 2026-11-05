# Create your App

# Create your app in Partner Center
Creating an app in Partner Center establishes the workspace and credentials you need to integrate with TikTok Shop services. In this workspace, you choose the app type, service category, market, seller type, API scopes, redirect URL, webhook settings, and app credentials.
This guide explains how to create a **Public app** or **Custom app** and how app developers (ISVs) can add eligible target markets to an existing app.
For the OAuth-only setup flow, use [Create a TikTok Shop app OAuth client](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client). That page should focus on the OAuth client configuration: redirect URL, authorization link, authorization code, token exchange, and refresh-token handling.
# Before you create an app
Complete this checklist before clicking **Create app & service**:
| Check | Why it matters |
| --- | --- |
| Developer account and onboarding are complete or in progress | Partner Center app creation depends on your developer account status and developer type. See [Developer onboarding](https://partner.tiktokshop.com/docv2/page/developer-onboarding). |
| Developer type is clear | ISVs, seller developers, system integrators, and partners can follow different review and launch paths. |
| App type is clear | Choose **Public app** if sellers should discover the app in the App and Service Store. Choose **Custom app** if the app is distributed privately by authorization link. |
| Service category is clear | Category affects available scopes, review expectations, and app positioning. Connector apps may have additional review requirements. |
| Target market and seller type are confirmed | Choose the market and seller type that match your app's intended users. Eligible ISV apps can add target markets later using the steps in **Add markets to an existing app** below. Adding a market is separate from changing an existing market or seller-type configuration. |
| Redirect URL is ready | Needed to receive the authorization `code` after a seller or partner authorizes your app. Use a secure backend-controlled endpoint. |
| Webhook URL is ready, if needed | Needed to receive push notifications for order, product, fulfillment, authorization, and other events. |
| Compliance and legal review path is understood | Review requirements vary by app type, category, market, and data access. US and UK partners should start compliance/legal review early because it can take three or more weeks. |
# App type decision
There are two main app types: public and custom.
| Item | Public app | Custom app |
| --- | --- | --- |
| Visibility | Listed in the TikTok Shop App and Service Store after approval. Sellers can discover, install, and authorize it. | Not listed publicly. Developers share a private authorization link with selected sellers. |
| Typical use case | SaaS or integration app intended for many sellers. | Seller-specific or partner-managed solution, often built for one seller or a limited seller group. |
| App listing details | Required for store listing. | Usually not required unless Partner Center requests them. |
| Distribution | App and Service Store listing. | Private authorization link. |
| Review standard | Public apps require app review before listing. | Custom apps usually launch privately without public-app listing review, but app review is required if the app is a Connector app, reaches 25 or more seller authorizations, or Partner Center / your partner manager indicates review is required for the selected category or market. |
Standard wording to reuse across related docs:
```Plain Text
Custom apps usually launch privately by authorization link. App review is required only for applicable custom apps, such as Connector apps, custom apps with 25 or more seller authorizations, or apps in a category or market where Partner Center requests review.
```

# Connector and 25-seller review rule
A **Connector** app is an app category for integrations that connect TikTok Shop with an external system, such as an ecommerce platform, ERP, OMS, WMS, 3PL, feed tool, or other seller operation system. Connector apps typically sync product, order, inventory, fulfillment, or other seller data across systems, so TikTok Shop may require review even if the app is distributed privately.
For custom apps:

* If the app category is **Connector**, prepare for app review.
* If the app reaches **25 or more seller authorizations**, prepare for app review before broader use.
* If Partner Center shows a review-required status, review banner, publish restriction, or **Submission materials for review** entry, follow that flow before expanding distribution.
* If you believe the app is below the threshold but still sees a review requirement, contact your partner manager or submit a Partner Center support ticket with the app key, service ID, app category, market, seller type, and screenshots.

# Create the app
To create your app:

1. Sign in to the correct Partner Center for the target market.
2. Open **App & Service** from the navigation panel.
3. Click **Create app & service**.
4. Select **Public** or **Custom**.
5. Select the **Service category** and set the **default name**.
6. Optionally upload a logo.
7. Select **Market** and **Seller type**.
8. Turn on **Enable API** if the app will call TikTok Shop APIs.
9. Configure the redirect URL and webhook URL.
10. Click **Create**.

Field reference:
| Field | Meaning | Notes |
| --- | --- | --- |
| App type | Public or Custom. | Choose based on how sellers will discover and authorize the app. |
| Service category | The business category of the app, such as Connector or another category shown in Partner Center. | Category can affect available scopes, review requirements, and launch flow. |
| Default name | The default app/service name shown in Partner Center and used as fallback display text. | Public apps may need localized listing content later. |
| Logo | App icon or logo. | Optional during initial creation, but public listings usually require polished brand assets. |
| Market | The market where the app will operate or be listed. | Select the market where your app will operate. To expand an existing ISV app into another eligible market, follow **Add markets to an existing app** below. |
| Seller type | Seller model supported by the app. | **Local** usually means local-to-local seller/shop scenarios. **Cross-border** means cross-border seller scenarios and may require additional identifiers such as `shop_cipher` or global product flows. |
| Enable API | Turns on API integration setup for the app. | Enable this if the app needs OpenAPI scopes, seller authorization, token exchange, or webhooks. |
| Redirect URL | Callback endpoint that receives the authorization `code`. | The token API uses the returned `code` value as the `auth_code` parameter. |
| Webhook URL | Callback endpoint that receives event notifications. | You can also manage shop webhooks later through Events API and Partner Center webhook settings. |
# Add markets to an existing app
If you are an app developer or system integrator (ISV), you can add eligible target markets to an existing **Public** or **Custom** app. You do not need to create a new app just to expand into another market.
The available markets depend on your company's registration region and the app's business category. This flow applies to ISV apps; seller developer apps and agency services follow their own onboarding flows.
## Start from your app

1. Open **App & Service** in Partner Center and click **Manage** for the app you want to expand. 
2. In the app details, click **+ Add market (Seller type)**. 
3. If the market you need is available to select, select it and continue to **Save the markets to your app** below. 
4. To register an additional market that does not yet have a qualification record for this category, click **Add manually** in the **Target market** dropdown. Choose from the markets offered in that form.


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/06db076e14974d0995142c834af6e249~tplv-k9wyc2ijk0-image.image)

If a market is listed but unavailable to select, check its existing qualification record in your profile and complete the required action. If it has already been added to the app, manage the existing market entry. Creating another qualification record does not remove these restrictions.
## Provide information for new markets

1. Check **Business category**. It is set to the category of the app you came from and cannot be changed in this flow. 
2. Select the available **Target market** options you want to add. You can select up to **10 markets** at a time, then click **Next**. 
3. Review the **Partner info** forms. Markets that use the same form may be grouped together; markets with different requirements have separate forms. Check any prefilled information and complete all required fields in each form. 
4. Click **Submit** to save your qualification information as a draft and return to the original app. For markets that are eligible to be added, the Add market dialog opens with your selections. 

Saving this draft does not start qualification review. If Partner Center requires you to complete qualification review before a market can be added:

1. Open your profile and find the qualification record for that category and market. 
2. Click **Edit**, complete the required information and click **Submit** in the qualification form to submit it for review. 
3. Check the review result and return to the app when the market becomes available to add. 

> **Already added?** A market with an existing qualification record for this category cannot be selected again in this new-market flow, even if that record is still a draft, under review or not approved. Open the existing record in your profile to check its status and any available actions. An existing qualification record does not necessarily mean the market has been added to this app.

## Save the markets to your app

1. In the Add market dialog, check each market and select its **Seller type**. Complete the required cross-border base country, if shown. 
2. Click **Save**. 
3. Confirm that the markets appear in the app's target-market list. 


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/93988071c12a4466b042662bb5443c34~tplv-k9wyc2ijk0-image.image)

When the dialog opens after you return from Partner info, it prefills the markets only. You still need to complete the seller settings and click **Save**. If you close the dialog before saving, reopen **+ Add market (Seller type)** to complete the addition.
## Complete the requirements for each market
Adding qualification information, adding a market to your app, and launching the app in that market are separate steps. Check the review status and available actions for each market in the app details.
If you have already added the market but its qualification information is still a draft, expand that market in the app details and click **Edit** on the qualification review item. Complete the required information and click **Submit** in the review form. **Save** in that form keeps a draft; it does not submit the information for review.

* For a **Public app**, complete the required market-language listings and reviews, then follow the publishing steps in [Publish and list a public App](https://partner.tiktokshop.com/docv2/page/publish-and-list-public-app). 
* For a **Custom app**, complete the requirements shown for the selected market and follow [Publish a custom App](https://partner.tiktokshop.com/docv2/page/publish-custom-app). 

For help interpreting review progress or resubmitting materials, see [App review process](https://partner.tiktokshop.com/docv2/page/app-review-process).
# Authorization domains and token exchange
Do not mix authorization entry domains, token domains, and OpenAPI resource domains. They serve different purposes.
| Purpose | US domain / endpoint | ROW domain / endpoint | Use when |
| --- | --- | --- | --- |
| Partner Center account, app creation, and documentation | `https://partner.us.tiktokshop.com` | `https://partner.tiktokshop.com` | Create or manage developer account, apps, services, reviews, and support tickets. |
| Seller authorization entry | `https://services.us.tiktokshop.com/open/authorize` | `https://services.tiktokshop.com/open/authorize` | A seller authorizes your app to access seller-owned shop data. |
| Partner authorization entry | `https://partner.us.tiktokshop.com/open/authorize` | `https://partner.tiktokshop.com/open/authorize` | A partner authorizes access to partner-owned business category data, such as approved Affiliate Partner APIs. |
| Token exchange | `https://auth.tiktok-shops.com/api/v2/token/get` | Same | Exchange an authorization code for `access_token` and `refresh_token`. |
| Token refresh | `https://auth.tiktok-shops.com/api/v2/token/refresh` | Same | Refresh an expired access token. |
| OpenAPI resource calls | `https://open-api.tiktokglobalshop.com` | Same | Call business APIs after you have a valid token and signature. |
Use the authorization guide that matches the data owner:

* Seller-owned shop data: [Authorization guide](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) or [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)
* Partner-owned data: [Partner authorization guide](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide)
* Creator-owned data: [Creator authorization guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide)

After authorization, TikTok Shop redirects to your configured **Redirect URL** with a one-time authorization code. The redirect parameter is commonly shown as `code`; pass that value to the token API as `auth_code`.
Token exchange example:
```HTTP
GET https://auth.tiktok-shops.com/api/v2/token/get?app_key={app_key}&app_secret={app_secret}&auth_code={code_from_redirect}&grant_type=authorized_code
```

Required token parameters:
| Parameter | Required | Description |
| --- | --- | --- |
| `app_key` | Yes | The App Key generated for your app in Partner Center. |
| `app_secret` | Yes | The App Secret generated for your app. Keep it server-side and never expose it in frontend code, logs, screenshots, or tickets. |
| `auth_code` | Yes | The authorization code returned to your Redirect URL. The code is short-lived and one-time use. |
| `grant_type` | Yes | Must be exactly `authorized_code`. Do not use the standard OAuth spelling `authorization_code`. |
# App credentials
After creation, Partner Center displays the app or service detail page. You can find the app credentials later from:
```Plain Text
Partner Center
  -> App & Service
  -> Select your app or service
  -> App credentials / Basic information
```

| Credential | Meaning | Handling requirement |
| --- | --- | --- |
| App Key | Public identifier of the app/service. | Used in token requests and signed OpenAPI requests. |
| App Secret | Secret key generated for the app/service. | Store only on the server side. Use it for token exchange and request signing. Do not expose it to browsers, mobile apps, client-side scripts, screenshots, or logs. |
| Service ID | Identifier used by some authorization-link flows. | Use it when building authorization links manually or when Partner Center asks for service-level identification. |
# Scope and authorization checks
Creating the app is not enough to call APIs. Before asking sellers to authorize:

1. Enable only the API scopes your app needs.
2. Confirm the endpoint's required scope in the API reference.
3. Complete seller authorization after the required scopes are enabled.
4. Check the `granted_scopes` field in the token response to confirm the seller granted the expected scopes.
5. If you add scopes later, ask the seller to reauthorize so the new token includes the new scopes.

# Document boundaries
Use these pages together, but keep their responsibilities separate:
| Page | Owns | Does not own |
| --- | --- | --- |
| Create your App | App type selection, app creation fields, adding eligible target markets to an existing ISV app, credentials, and high-level review rules. | Detailed OAuth callback implementation or token refresh logic. |
| [Create a TikTok Shop app OAuth client](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client) | OAuth client setup, redirect URL behavior, authorization code handling, token exchange, and refresh-token flow. | Public vs custom app strategy or app launch review path. |
| [App development overview](https://partner.tiktokshop.com/docv2/page/app-development-overview) | End-to-end development lifecycle: design, create, test, review, launch. | Field-by-field app creation instructions. |
| [App launch overview](https://partner.tiktokshop.com/docv2/page/app-launch-overview) | Publish and launch path for public and custom apps. | Initial app creation details. |
| [App review process](https://partner.tiktokshop.com/docv2/page/app-review-process) | Review materials, review workflow, and review status. | OAuth token exchange or API signing. |
# Next steps
After creating the app:

1. Configure required API scopes in Partner Center.
2. Configure and test the Redirect URL.
3. Configure webhook topics if the app relies on event notifications.
4. Generate a test authorization code and exchange it for tokens.
5. Call [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) to confirm the token and shop mapping.
6. Test with [Development Shop](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops) and [API Testing Tool](https://partner.tiktokshop.com/dev/api-testing-tool).
7. Follow the applicable launch or review path for the app type, category, market, and seller authorization scale.
