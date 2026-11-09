# 访问权限范围

# 了解访问权限范围的运作方式
当你为 TikTok Shop 开发应用时，必须明确定义你需要访问的具体数据。这就是访问权限范围（access 权限范围）发挥作用的地方。访问权限范围充当守门人，限制应用对某些数据（特定 API）的访问。它们提供了精确描述应用所需访问类型的方式。
同样重要的是，这些权限范围为授权你的应用访问其数据的卖家提供了清晰的认知。卖家需要了解应用在其 Seller Center 账户数据方面的能力和限制。在授权应用访问其数据时，每个权限范围都明确了应用可以访问的 endpoint。例如，一个应用可能获得访问店铺内订单和产品数据的授权。
| 访问权限范围类型 | 描述 |
| --- | --- |
| Public（公开） | 归类在公开权限范围下的 API 对所有开发者开放。这些 API 是构建支持 TikTok Shop 卖家应用功能的基础。在 Partner Center 创建应用后，你将默认获得所有公开权限范围 API 的访问权限。但是，你的应用需要获得卖家授权后，才能访问特定店铺相关的数据。 |
| Custom（自定义） | 归类在自定义权限范围下的 API 包含敏感数据。要访问此权限范围内的 API，你可以通过 Partner Center 申请访问权限，导航至 **合作伙伴 Console >> App & Service >> Manage >> Manage API。** 与公开权限范围类似，你的应用需要获得卖家授权后才能访问特定店铺相关的数据。 |
# 可用访问权限范围列表
以下表格列出了 TikTok Shop API 的部分访问权限范围示例。
📌 要查看你的应用可用的完整 API 访问权限范围列表，请前往 **合作伙伴 Console >> App & Service >> Manage >> Manage API**。
| 权限范围名称 | 描述 | 类型 |
| --- | --- | --- |
| **Shop Authorized Information（店铺授权信息）** | 服务商将有权访问卖家的 TikTok Shop 店铺 ID。 | Public |
| **Product Basic（产品基础）** | 服务商将能够将产品信息同步到卖家的 TikTok Shop。 | Public |
| **Product Modify（产品修改）** | 服务商将能够管理卖家的产品信息，包括访问产品列表、编辑产品属性、更改产品状态和同步产品库存等。 | Public |
| **Product Delete & Recover（产品删除与恢复）** | 服务商将能够管理卖家的产品，从店铺中删除和恢复产品。 | Public |
| **Order Information（订单信息）** | 服务商将能够通过 API 实时访问卖家的所有订单数据。 | Public |
| **Fulfillment Basic（履约基础）** | 服务商将能够代表卖家处理和管订单，并提供订单状态的实时更新。 | Public |
| **Package Split And Combine（包裹拆分与合并）** | 服务商将能够代表卖家拆分和合并订单。 | Public |
| **Update Delivery Status（更新配送状态）** | 服务商将能够为具有运输能力（3PL 配送）的卖家将包裹推送至已送达状态。 | Public |
| **Logistics Basic（物流基础）** | 服务商将能够获取卖家的物流和仓库信息。 | Public |
| **Return & Refund Basic（退货与退款基础）** | 服务商将能够管理卖家的退货和退款请求。 | Public |
| **Finance Information（财务信息）** | 服务商将能够按订单访问交易和结算金额信息，并将卖家在 TikTok Shop 的结算与订单进行对账。 | Public |
| **Promotion Information（促销信息）** | 服务商将能够获取卖家的促销列表和促销活动详情。 | Public |
| **Promotion Modify（促销修改）** | 服务商将能够在 TikTok Shop 上创建和管理卖家的折扣和促销活动。 | Public |
| **Global Shop Information（全球店铺信息）** | 服务商将能够访问卖家的全球店铺信息。 | Public |
| **Global Product Information（全球产品信息）** | 服务商将能够访问卖家的全球产品信息。 | Public |
| **Global Product Modify（全球产品修改）** | 服务商将能够管理卖家的全球产品信息等。 | Public |
| **Global Product Delete（全球产品删除）** | 服务商将能够代表卖家删除全球产品。 | Public |
| **Global Category Information（全球类目信息）** | 服务商将能够访问卖家的全球产品类目信息。 | Public |
| 以及更多... <!-- colSpan:3 --> |  |  |
