# API entity tags

In the TikTok Shop API Reference, each endpoint is grouped under one **entity tag**. Entity tags help developers quickly understand:

* The business entity that the API operates on, such as seller, shop, account, creator, or asset.
* The data boundary of the API, such as seller-account data, local-shop data, account-level data, creator-account data, or asset-level data.
* The authorization type required to call the API, such as a seller access token, creator access token, or partner access token.
* Whether an additional encrypted identifier, such as `shop_cipher` or `category_asset_cipher`, is required.

Entity tags do not replace API scopes. Before calling an endpoint, check both the endpoint's entity tag and the required scope. For more information, refer to [Access scope](https://partner.tiktokshop.com/docv2/page/access-scope) and [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407).
<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f571db0c87ae4e8f872b882e3cf70776~tplv-k9wyc2ijk0-image.image" width="900px" /></div>

Example of an API entity tag
# Entity tag and access requirements
Use the following table as a quick checklist when choosing the access token and additional identifier for an endpoint. The exact API scope still comes from the API Reference and [Access scope](https://partner.tiktokshop.com/docv2/page/access-scope).
| API entity tag | Access token required | Additional identifier | How to read it |
| --- | --- | --- | --- |
| `Seller` | Seller access token | None for seller-level endpoints | Use for seller account-level data and cross-shop operations. |
| `Shop` | Seller access token | `shop_cipher` | Use for one local shop's products, orders, and shop-specific data. |
| `Account` | Partner access token | Usually none for account-level endpoints | Use for account-level APIs. |
| `Creator` | Creator access token | None for creator-level endpoints | Use for creator-owned data. |
| `Asset` | Partner access token | `category_asset_cipher` | Use for partner campaign asset-level data, such as Affiliate Partner campaign data. |
# Ciphers used by entity tags
Some entity tags require an access token plus an encrypted identifier. These identifiers are not meant to be decrypted by developers.
| Cipher | What it identifies | Required for | How to get it |
| --- | --- | --- | --- |
| `shop_cipher` | One shop that a seller has authorized for the app. | `Shop` tag endpoints. | Call [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) with a seller access token and use `data.shops[].cipher` from the response. |
| `category_asset_cipher` | One partner business category asset authorized for the app. | `Asset` tag endpoints. | Call [Get Authorized Category Assets](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) with a partner access token and use `data.category_assets[].cipher` from the response. |

If an endpoint is tagged `Shop`, a seller access token alone is not enough; the request must also include the correct `shop_cipher` for the target shop. If an endpoint is tagged `Asset`, a partner access token alone is not enough; the request must also include the correct `category_asset_cipher` for the target partner asset.
# Text example of an API entity tag
If an API Reference page shows the `Shop` entity tag, read it as follows:
| Item | Meaning |
| --- | --- |
| Entity tag | `Shop` |
| Data boundary | One local TikTok Shop. Data is isolated from other shops under the same seller. |
| Access token | Seller access token in the `x-tts-access-token` header. |
| Additional identifier | `shop_cipher`, obtained from [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309). |
| Scope check | The endpoint still requires its own API scope. Check the API Reference and [Access scope](https://partner.tiktokshop.com/docv2/page/access-scope). |
# Types of entity tag
# Seller tag
Endpoints with the `Seller` tag operate at the **seller account level**. A [seller access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) is required to access the seller's data.
These endpoints are mainly used to manage seller-level data that supports cross-shop operations. This includes seller-wide metadata, such as retrieving shops owned by the seller; reusable assets, such as uploading shop-agnostic images; and global product data used to replicate local product listings across multiple shops, such as creating global products.
They cannot be used to access or manage individual local shop data, such as local products or a shop's orders. For local shop data, use a `Shop` tag endpoint with a seller access token and the target `shop_cipher`.
# Shop tag
Endpoints with the `Shop` tag operate at the **local shop level**. A [seller access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) and a [shop_cipher](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) are required to access the shop data. Each shop has its own `shop_cipher`, and the data is isolated from other shops.
These endpoints are mainly used to manage data within a shop, such as listing products in a shop, retrieving shop orders, managing local inventory, and so on.
They cannot be used to access or manage data that spans across multiple shops under the same seller account. For seller-wide or cross-shop operations, use a `Seller` tag endpoint.
# Account tag
Endpoints with the `Account` tag operate at the **partner account level**. A [partner access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) is required to access the partner's account-level data.
These endpoints are mainly used for managing data related to the partner account, such as retrieving the list of business category assets that a partner has authorized for an app.
They cannot be used to access or manage a partner's campaign assets directly. For partner campaign asset-level data, use an `Asset` tag endpoint with a partner access token and the relevant `category_asset_cipher`.
# Creator tag
Endpoints with the `Creator` tag operate at the **creator account level**. A [creator access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) is required to access the creator's data.
These endpoints are mainly used to manage data related to a creator, such as obtaining a creator's profile, retrieving affiliate orders generated by the creator, searching for open collaboration items, and so on.
They cannot be used to access seller-owned shop data, account-level data, or asset-level data.
# Asset tag
Endpoints with the `Asset` tag operate at the **partner campaign asset level**. A [partner access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) and the relevant [category_asset_cipher](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) are required to access a partner's campaign data.
These endpoints are mainly used to manage affiliate marketing campaigns and handle campaign products.
They cannot be used to manage the partner account itself, seller-owned shop data, or creator-owned data. For partner account-level data, use an `Account` tag endpoint with a partner access token.
# Related authorization and scope docs
Use these documents together when deciding which token and identifier to use:
| Need | Documentation |
| --- | --- |
| Understand authorization concepts and token exchange | [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
| Check API permission scopes | [Access scope](https://partner.tiktokshop.com/docv2/page/access-scope) |
| Get a shop cipher for `Shop` tag APIs | [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| Get a category asset cipher for `Asset` tag APIs | [Get Authorized Category Assets](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) |
| Set up seller authorization | [Seller authorization guide](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) |
| Set up creator authorization | [Creator authorization guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide) |
| Set up partner authorization | [Partner authorization guide](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide) |
# Common mistakes to avoid
Do not choose an access token only by looking at the API path. First check the endpoint's entity tag, then confirm the required token type, cipher, and API scope.
Do not use a seller access token to call creator or partner APIs. Do not use a partner access token to call seller shop APIs. Do not use a creator access token to call seller, shop, account, or asset APIs.
Do not confuse seller-level and shop-level APIs. `Seller` tag APIs operate at the seller account level. `Shop` tag APIs operate on one local shop and require `shop_cipher`.
Do not confuse account-level and asset-level APIs. `Account` tag APIs operate at the account level. `Asset` tag APIs operate on a campaign asset and require `category_asset_cipher`.
