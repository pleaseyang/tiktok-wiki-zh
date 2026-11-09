# API 实体标签

在 TikTok Shop API 参考文档中，每个 endpoint 都归在一个**实体标签**下。实体标签帮助开发者快速了解：

* API 所操作的业务实体，例如卖家（卖家）、shop（店铺）、account（账户）、达人（达人）或 asset（资产）。
* API 的数据边界，例如卖家-account 数据、local-shop 数据、account 级别数据、达人-account 数据或 asset 级别数据。
* 调用该 API 所需的授权类型，例如卖家 access token、达人 access token 或合作伙伴 access token。
* 是否需要额外的加密标识符，例如 `shop_cipher` 或 `category_asset_cipher`。

实体标签不能替代 API 权限范围。在调用 endpoint 之前，请同时检查 endpoint 的实体标签和所需的权限范围。更多信息，请参阅[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)和[授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)。
<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f571db0c87ae4e8f872b882e3cf70776~tplv-k9wyc2ijk0-image.image" width="900px" /></div>

API 实体标签示例
# 实体标签与访问要求
使用以下表格作为选择 endpoint 的 access token 和额外标识符的快速检查清单。具体的 API 权限范围仍以 API 参考文档和[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)为准。
| API 实体标签 | 所需 Access Token | 额外标识符 | 解读方式 |
| --- | --- | --- | --- |
| `Seller` | 卖家访问令牌 | 卖家级别 endpoint 无需额外标识 | 用于卖家账户级别数据和跨店铺操作。 |
| `Shop` | 卖家访问令牌 | `shop_cipher` | 用于单个本地店铺的产品、订单和店铺特定数据。 |
| `Account` | 合作伙伴访问令牌 | account 级别 endpoint 通常无需额外标识 | 用于 account 级别的 API。 |
| `Creator` | 达人访问令牌 | 达人级别 endpoint 无需额外标识 | 用于达人自有数据。 |
| `Asset` | 合作伙伴访问令牌 | `category_asset_cipher` | 用于服务商营销活动资产级别的数据，例如 Affiliate Partner 营销活动数据。 |
# 实体标签使用的 Cipher
某些实体标签需要 access token 加一个加密标识符。这些标识符并非供开发者解密使用。
| Cipher | 标识对象 | 适用场景 | 获取方式 |
| --- | --- | --- | --- |
| `shop_cipher` | 卖家已授权给应用的某个店铺。 | `Shop` 标签的 endpoint。 | 使用卖家 access token 调用[Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)，并使用响应中的 `data.shops[].cipher`。 |
| `category_asset_cipher` | 已授权给应用的某个服务商业务类目资产。 | `Asset` 标签的 endpoint。 | 使用合作伙伴 access token 调用[Get Authorized Category Assets](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405)，并使用响应中的 `data.category_assets[].cipher`。 |

如果一个 endpoint 标记为 `Shop`，仅使用卖家 access token 是不够的；请求还必须包含目标店铺的正确 `shop_cipher`。如果一个 endpoint 标记为 `Asset`，仅使用合作伙伴 access token 是不够的；请求还必须包含目标服务商资产的正确 `category_asset_cipher`。
# API 实体标签文本示例
如果 API 参考文档页面显示 `Shop` 实体标签，可按如下方式解读：
| 项目 | 含义 |
| --- | --- |
| 实体标签 | `Shop` |
| 数据边界 | 单个本地 TikTok Shop。数据与同一卖家下的其他店铺隔离。 |
| Access Token | `x-tts-access-token` 请求头中的卖家 access token。 |
| 额外标识符 | `shop_cipher`，从 [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) 获取。 |
| Scope 检查 | 该 endpoint 仍需其自身的 API 权限范围。请查看 API 参考文档和[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)。 |
# 实体标签类型
# 卖家标签
标记为 `Seller` 的 endpoint 在 **卖家账户级别**运行。需要 [seller access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) 来访问卖家数据。
这些 endpoint 主要用于管理支持跨店铺操作的卖家级别数据。包括卖家范围的元数据（例如检索卖家拥有的店铺）、可复用资产（例如上传与店铺无关的图片），以及用于在多个店铺中复制本地产品列表的全球产品数据（例如创建全球产品）。
它们不能用于访问或管理单个本地店铺数据，例如本地产品或店铺订单。对于本地店铺数据，请使用 `Shop` 标签的 endpoint，配合卖家 access token 和目标 `shop_cipher`。
# Shop 标签
标记为 `Shop` 的 endpoint 在 **本地店铺级别**运行。需要 [seller access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) 和 [shop_cipher](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) 来访问店铺数据。每个店铺都有自己的 `shop_cipher`，数据与其他店铺隔离。
这些 endpoint 主要用于管理店铺内的数据，例如列出店铺中的产品、检索店铺订单、管理本地库存等。
它们不能用于访问或管理同一卖家账户下跨多个店铺的数据。对于卖家范围或跨店铺操作，请使用 `Seller` 标签的 endpoint。
# Account 标签
标记为 `Account` 的 endpoint 在 **服务商账户级别**运行。需要 [partner access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) 来访问服务商的账户级别数据。
这些 endpoint 主要用于管理与服务商账户相关的数据，例如检索服务商已授权给应用的业务类目资产列表。
它们不能用于直接访问或管理服务商的营销活动资产。对于服务商营销活动资产级别的数据，请使用 `Asset` 标签的 endpoint，配合合作伙伴 access token 和相关的 `category_asset_cipher`。
# 达人标签
标记为 `Creator` 的 endpoint 在 **达人账户级别**运行。需要 [creator access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) 来访问达人数据。
这些 endpoint 主要用于管理与达人相关的数据，例如获取达人个人资料、检索达人产生的联盟订单、搜索公开协作商品等。
它们不能用于访问卖家拥有的店铺数据、账户级别数据或资产级别数据。
# Asset 标签
标记为 `Asset` 的 endpoint 在 **服务商营销活动资产级别**运行。需要 [partner access token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407#Get%20Access%20Token%20API) 和相关的 [category_asset_cipher](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) 来访问服务商的营销活动数据。
这些 endpoint 主要用于管理联盟营销活动并处理营销活动产品。
它们不能用于管理服务商账户本身、卖家拥有的店铺数据或达人自有数据。对于服务商账户级别的数据，请使用 `Account` 标签的 endpoint 配合合作伙伴 access token。
# 相关授权和权限范围文档
在决定使用哪种 token 和标识符时，可结合使用以下文档：
| 需求 | 文档 |
| --- | --- |
| 了解授权概念和 token 交换 | [授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
| 检查 API 权限范围 | [访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope) |
| 获取 `Shop` 标签 API 的 shop cipher | [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| 获取 `Asset` 标签 API 的 category asset cipher | [Get Authorized Category Assets](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) |
| 设置卖家授权 | [商家授权指南](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) |
| 设置达人授权 | [达人授权指南](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide) |
| 设置服务商授权 | [服务商授权指南](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide) |
# 应避免的常见错误
不要仅通过查看 API 路径来选择 access token。首先检查 endpoint 的实体标签，然后确认所需的 token 类型、cipher 和 API 权限范围。
不要使用卖家 access token 调用达人或合作伙伴 API。不要使用合作伙伴 access token 调用卖家 shop API。不要使用达人 access token 调用卖家、shop、account 或 asset API。
不要混淆卖家级别和 shop 级别的 API。`Seller` 标签 API 在卖家账户级别运行。`Shop` 标签 API 在单个本地店铺运行，需要 `shop_cipher`。
不要混淆 account 级别和 asset 级别的 API。`Account` 标签 API 在账户级别运行。`Asset` 标签 API 在营销活动资产级别运行，需要 `category_asset_cipher`。
