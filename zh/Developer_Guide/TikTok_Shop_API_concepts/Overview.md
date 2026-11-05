# 概述

TikTok Shop 提供了全面的 API 系列，统称为 **TTS API**。这些 API 允许开发者访问已授权的 TikTok Shop 数据，包括商品目录、订单、物流、支付等。
借助 TTS API，开发者可以创建扩展 Seller Center 现有功能的应用。这些应用可以增强商品目录列表、简化订单履约流程、减少运营工作量，并加速客户互动。
# 主要功能
借助 TikTok Shop API，您可以：

* 设置[授权工作流](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)，开发者可从 TTS App & Service Market 详情页或您自己的网站发起授权。
* 配置 [webhook](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview)，以接收来自 TikTok Shop Open Platform 的通知。
* 在 Sandbox 中测试应用功能，或使用 [API 测试工具](https://partner.tiktokshop.com/dev/api-testing-tool) 发起 API 调用。

# API 分类
| **序号** | **API 类别** | **API 描述** |
| --- | --- | --- |
| 1 | [Product API](https://partner.tiktokshop.com/docv2/page/products-api-overview) | Product API 是 TTS 中最重要的 API 之一。开发者可以使用 Product API 访问商品类目规则和属性，上传商品图片、视频、认证文件等，创建商品、编辑商品信息，以及更新库存和价格。TikTok Shop 还为跨境电商开发者提供 Global Product API。借助 Global Product API，跨境电商开发者可以为在多个区域市场销售的跨境卖家提供统一的商品管理解决方案。 |
| 2 | [Order API](https://partner.tiktokshop.com/docv2/page/order-api-overview) | 开发者可以使用 Order API 从 TikTok Shop 卖家的店铺中获取订单信息。卖家获取订单信息后，可以执行订单履约操作以及取消订单和退货等操作。 |
| 3 | [Fulfillment API](https://partner.tiktokshop.com/docv2/page/fulfillment-api-overview) | 开发者可以使用 Fulfillment API 将 TikTok Shop 订单的履约状态与第三方物流服务商（3PL）同步。也可以使用 TikTok 提供的物流面单服务（4PL）来履约订单。此外，还可以使用 TikTok 履约（FBT）服务，开发者可以通过 Fulfillment API 访问 TikTok Shop 订单的履约状态。 |
| 4 | [Return & Refund API](https://partner.tiktokshop.com/docv2/page/return-refund-and-cancel-api-overview) | 当消费者发起退货或退款请求时，开发者可以使用 Return & Refund API 获取退货或退款订单信息，并协助卖家审核或拒绝消费者发起的请求。 |
| 5 | [Logistics API](https://partner.tiktokshop.com/docv2/page/logistic-api-overview) | 当卖家使用 TikTok Shop 提供的物流服务时，开发者可以使用 Logistics API 帮助卖家获取仓库列表、全球仓库列表、已订阅的配送方式和物流服务商。 |
| 6 | [Promotion API](https://partner.tiktokshop.com/docv2/page/promotion-api-overview) | 开发者可以使用 Promotion API 协助卖家为特定商品设置促销、折扣和其他优惠活动。 |
| 7 | [Finance API](https://partner.tiktokshop.com/docv2/page/finance-api-overview) | 开发者可以使用 Finance API 协助卖家获取其 TikTok Shop 的支付和结算信息。 |
| 8 | [Seller API](https://partner.tiktokshop.com/docv2/page/seller-api-overview) | Seller API 支持跨境运营，一个卖家可以在多个区域市场开设店铺。开发者可以使用 Seller API 获取跨境卖家的店铺状态，并确定特定跨境市场是否符合 Global Product 功能的使用条件。 |
| 9 | [Authorization API](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) | 开发者可以使用 Authorization API 交换授权 token 并获取应用的已授权店铺信息。 |
| 10 | [Events API](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) | 开发者可以使用 Events API 订阅和取消订阅 TikTok Shop 业务事件的 Open Platform webhook。 |
| 11 | Data Reconciliation API | 开发者可以使用 Data Reconciliation API 将外部数据传输到 Open Platform 进行质量引擎对账。 |
| 12 | [Supply Chain API](https://partner.tiktokshop.com/docv2/page/confirm-package-shipment) | 此 API 面向 TikTok Shop 认证的仓库合作伙伴。开发者可以使用 Supply Chain API 将认证仓库履约的订单包裹履约详情回传至 TTS。 |

有关可用 API 的完整列表，请参阅 [TTS API 参考文档](https://partner.tiktokshop.com/docv2/page/create-product)。
# 授权和 token 导航
TTS API 根据数据所有者使用不同的授权流程。token 响应中的 `user_type` 字段有助于识别授权主体，例如卖家、达人或合作伙伴。有关确切的 token 响应字段和枚举值，请参阅[生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token)。
请使用与数据所有者匹配的授权指南：
| 授权类型 | 数据所有者 | 美国站授权入口 | 其他区域授权入口 | 主要指南 |
| --- | --- | --- | --- | --- |
| 卖家授权 | 卖家 / 店铺 | `https://services.us.tiktokshop.com/open/authorize` | `https://services.tiktokshop.com/open/authorize` | [授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
| 达人授权 | 达人 | `https://shop.tiktok.com/alliance` | `https://shop.tiktok.com/alliance` | [达人授权指南](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide) |
| 合作伙伴授权 | 合作伙伴 | `https://partner.us.tiktokshop.com/open/authorize` | `https://partner.tiktokshop.com/open/authorize` | [合作伙伴授权指南](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide) |
选择 API 时，还需检查 endpoint 的实体标签和访问要求。有关标签级别的指南，请参阅 [API 实体标签](https://partner.tiktokshop.com/docv2/page/api-entity-tags)。有关权限级别的指南，请参阅[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)。
# API 版本
TTS API 具有版本管理。一些较旧的 API 版本可能仍可访问，但不受支持的版本可能随时停止工作。强烈建议开发者使用其调用的 endpoint 所支持的最新版本。
不要依赖硬编码的示例来确定最新版本。在每个 API 参考页面上，使用版本选择器或版本下拉菜单确认该 endpoint 的最新支持版本，然后按照页面上显示的迁移说明或弃用通知操作。
有关更多详情，请参阅 [TTS API 版本管理](https://partner.tiktokshop.com/docv2/page/api-versioning)。
