# Get started overview

This page introduces the **types of TikTok Shop developers** and points you to the rest of the getting-started path. After you've identified your developer type below, continue to Developer onboarding, then Authorization, and finally Make your first API call.
## The three developer types
| Developer type | Builds | Stores seller OAuth credentials? | Data access | Typical scenario |
| --- | --- | --- | --- | --- |
| **eCommerce platform plugin / connector developer** | Public app | Usually no | Limited, scenario-specific | Plugins for Shopify, WooCommerce, Magento that add TikTok Shop support |
| **eCommerce system integrator / SaaS developer** | Public app | Yes (trusted to store bearer & refresh tokens) | Direct access to authorized sellers' data | SaaS managing advertising, promotion, marketing, and operations for many sellers |
| **TikTok Shop seller developer** | Custom app | Own credentials only | Your own shop's data only | A seller building an integration for their own shop |
## eCommerce platform developers
Developers who create plugins for popular eCommerce platforms such as Shopify, WooCommerce, or Adobe Magento. These plugins extend the platform to support a specific marketplace such as TikTok Shop. This type typically does **not** need to store seller OAuth credentials or data.
## eCommerce system integrators
Developers who build systems to manage advertising, product promotion, marketing, and other business functions on behalf of their seller and merchant customers. Some are SaaS products with a user interface; others manage operations directly. This type typically requires **direct access** to a seller's data and is trusted to store and generate OAuth credentials such as bearer and refresh tokens.
## TikTok Shop seller developers
TikTok Shop sellers who have an active shop and want to build an integration for their own shop's needs. This type has access to **their own** OAuth credentials and data only.
## How developer type maps to `user_type`
When a user authorizes your app, the token response includes a `user_type` field. Platform/integrator developers act on behalf of a **Seller** (`user_type=0`); apps built for affiliate creators receive **Creator** (`user_type=1`); affiliate partner (TAP) apps receive **Partner** (`user_type=3`). See Authorization overview for the complete enumeration.
> **New to OAuth terms?** An *OAuth credential* is what your app uses to act for a user. A *bearer (access) token* authorizes each API call; a *refresh token* lets you obtain a new access token without re-authorizing. The full flow is described in the Authorization overview.

## Next steps
Your complete getting-started path:

1. [Developer onboarding](https://partner.tiktokshop.com/docv2/page/developer-onboarding) — create your account and register as a developer.
2. [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) — understand how apps get access to user data.
3. [Make your first API call overview](https://partner.tiktokshop.com/docv2/page/make-your-first-api-call-overview) — sign and send your first request.


