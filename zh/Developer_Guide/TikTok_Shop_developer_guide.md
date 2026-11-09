# TikTok Shop 开发者指南

欢迎使用 TikTok Shop API 开发者指南。TikTok Shop API 为应用和服务集成商提供对 TikTok Shop 平台的编程访问能力——涵盖商品、订单、履约、财务、联盟营销等功能。
## 你属于哪种开发者类型？
在开始之前，请先确认你的开发者类型——它决定了你所遵循的路径以及在授权过程中获得的 `user_type`。
| 你的身份 | 应用类型 | 可访问的数据 | 授权时你的身份为 |
| --- | --- | --- | --- |
| **卖家（内部）开发者** — 为自己的店铺进行开发的卖家 | 自定义应用 | 仅限你自己店铺的数据 | 卖家（`user_type=0`） |
| **应用开发者 / ISV / 系统集成商** — 为多个卖家提供服务 | 公开应用 | 已授权卖家的数据 | 代表卖家的卖家身份（`user_type=0`） |
| **达人 / 联盟营销集成商** | 公开应用 | 达人侧的联盟营销数据 | 达人（`user_type=1`） |
| **合作伙伴（TAP）集成商** | 公开应用 | 合作伙伴业务数据（Affiliate Partner / TAP） | 合作伙伴（`user_type=3`） |
完整的开发者类型说明，请参见"开始使用"概述。
## 入门指南 — 4 步流程
如果你是首次接入，请按以下步骤依次操作：

1. **入驻** — 创建 Partner Center 账户并注册为开发者。参见开发者入驻。（美国/英国及部分市场还需要合规与法律审查——请预留 3 周以上时间。）
2. **创建你的应用** — 注册 TikTok Shop 应用（OAuth 客户端）并启用所需的 API 权限范围。参见创建 TikTok Shop 应用（OAuth 客户端）。
3. **授权并获取 token** — 让卖家/达人/合作伙伴授权你的应用，然后将 `auth_code` 换取 `access_token`。请从授权概述开始。
4. **发起你的第一次 API 调用** — 签名并发送你的第一个请求。参见发起第一次 API 调用概述。

## API 参考
完整的 API 参考按 TikTok Shop 数据领域进行组织。打开 Partner Center 顶部导航栏中的 **API 参考** 标签页，或从以下概述开始：

   * [卖家 API 概述](https://partner.tiktokshop.com/docv2/page/seller-api-overview)
   * [商品 API 概述](https://partner.tiktokshop.com/docv2/page/products-api-overview)
   * [订单 API 概述](https://partner.tiktokshop.com/docv2/page/order-api-overview)
   * [履约 API 概述](https://partner.tiktokshop.com/docv2/page/fulfillment-api-overview)
   * [物流 API 概述](https://partner.tiktokshop.com/docv2/page/logistic-api-overview)
   * [财务 API 概述](https://partner.tiktokshop.com/docv2/page/finance-api-overview)

所有其他领域均可在 **API 参考** 标签页下找到。
## 场景指南与 Webhook

* **场景指南** 通过代码流程图引导你完成常见的集成场景（连接店铺、商品类目等）。参见本指南的 **场景指南** 部分。
* **Webhook** 让你的应用订阅平台通知。参见 Webhook 概述。
* 如需在 TikTok Shop 应用店铺上架你的应用，请参见应用开发概述。

## 后续步骤
根据你的目标选择下一步操作：

* **我需要设置访问权限** → [开发者入驻](https://partner.tiktokshop.com/docv2/page/developer-onboarding)
* **我已准备好构建和授权** → [授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)
* **我想立即调用 API** → [发起第一次 API 调用概述](https://partner.tiktokshop.com/docv2/page/make-your-first-api-call-overview)

> 在任何环节遇到问题？请参见如何联系支持以获取对应的帮助渠道。


