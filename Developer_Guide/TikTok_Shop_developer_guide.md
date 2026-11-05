# TikTok Shop developer guide

Welcome to the TikTok Shop API Developer Guide. The TikTok Shop API gives application and service integrators programmatic access to the TikTok Shop platform — products, orders, fulfillment, finance, affiliate, and more.
## Which developer are you?
Before you dive in, identify your developer type — it determines which path you follow and which `user_type` you receive during authorization.
| You are… | Build type | Data you access | During authorization you are |
| --- | --- | --- | --- |
| **Seller (in-house) developer** — a seller building for your own shop | Custom app | Your own shop's data only | Seller (`user_type=0`) |
| **App developer / ISV / system integrator** — serving multiple merchants | Public app | Authorized sellers' data | Seller (`user_type=0`) on behalf of the seller |
| **Creator / affiliate integrator** | Public app | Creator-side affiliate data | Creator (`user_type=1`) |
| **Partner (TAP) integrator** | Public app | Partner business data (Affiliate Partner / TAP) | Partner (`user_type=3`) |
See Get started overview for the full breakdown of developer types.
## Getting started — the 4-step path
If this is your first time, follow these steps in order:

1. **Onboard** — Create a Partner Center account and register as a developer. See Developer onboarding. (US/UK and some markets also require a compliance & legal review — budget 3+ weeks.)
2. **Create your app** — Register a TikTok Shop app (OAuth client) and enable the API scopes you need. See Create a TikTok Shop App (OAuth client).
3. **Authorize and get a token** — Have a seller/creator/partner authorize your app, then exchange the `auth_code` for an `access_token`. Start with the Authorization overview.
4. **Make your first API call** — Sign and send your first request. See Make your first API call overview.

## API reference
A full API reference is organized by TikTok Shop data domain. Open the **API Reference** tab in the top navigation of Partner Center, or start with these overviews:

   * [Seller API overview](https://partner.tiktokshop.com/docv2/page/seller-api-overview)
   * [Products API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview)
   * [Order API overview](https://partner.tiktokshop.com/docv2/page/order-api-overview)
   * [Fulfillment API overview](https://partner.tiktokshop.com/docv2/page/fulfillment-api-overview)
   * [Logistic API overview](https://partner.tiktokshop.com/docv2/page/logistic-api-overview)
   * [Finance API overview](https://partner.tiktokshop.com/docv2/page/finance-api-overview)

All remaining domains are available under the **API Reference** tab.
## Use case guides and webhooks

* **Use case guides** walk you through common integration scenarios (connecting shops, product categories, and more) with code-flow diagrams. See the **Use case guides** section of this guide.
* **Webhooks** let your app subscribe to platform notifications. See the Webhooks overview.
* To list your app in the TikTok Shop App Store, see the App development overview.

## Next steps
Pick the next step that matches your goal:

* **I need to set up access** → [Developer onboarding](https://partner.tiktokshop.com/docv2/page/developer-onboarding)
* **I'm ready to build and authorize** → [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)
* **I want to call an API now** → [Make your first API call overview](https://partner.tiktokshop.com/docv2/page/make-your-first-api-call-overview)

> Stuck at any point? See How to contact support for the right channel.



