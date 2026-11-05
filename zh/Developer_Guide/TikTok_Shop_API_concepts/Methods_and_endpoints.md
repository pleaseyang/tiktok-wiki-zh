# 方法与端点

# 方法
TikTok Shop API reference 页面定义了每个 endpoint 的 HTTP 方法。大多数 TTS Open API 使用 **GET** 或 **POST**。少量 endpoint 可能使用其他 RESTful 方法，但开发者应始终遵循 endpoint reference 页面上显示的确切方法。
使用与 endpoint reference 不匹配的方法可能导致 `36009010 Invalid method` 等错误。
| **方法** | **典型用途** | **实现说明** |
| --- | --- | --- |
| **GET** | 从 TikTok Shop 检索资源。 | 通常用于查询和列表 API。 |
| **POST** | 发送数据或执行操作。 | 通常用于 API 有请求体或执行状态变更操作时。 |
| **PUT** | 更新现有资源。 | 仅在 endpoint reference 明确列出 `PUT` 时使用。 |
| **DELETE** | 删除资源。 | 仅在 endpoint reference 明确列出 `DELETE` 时使用。 |
# Endpoint
TikTok Shop API endpoint 按资源类型组织，遵循以下模式：
**https://{domain}/{category}/{version}/{resource}**
`/{category}/{version}/{resource}` 段可以在任何 TikTok Shop API 的相应 reference 文档中找到。从 `202309` API 风格开始，API 版本是请求路径的一部分，例如 `/authorization/202309/shops`。计算请求签名时，请使用 domain 之后显示的请求路径，包括 category、version 和 resource 段。签名规则请参阅 [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。
例如，要调用 [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)，endpoint 为：
```Plain Text
https://open-api.tiktokglobalshop.com/authorization/202309/shops
```

# Domain 和环境
对于 **业务 API 调用**，TTS Open API 当前使用以下 domain：
| **环境** | **URI** | **使用场景** |
| --- | --- | --- |
| 生产环境 | `https://open-api.tiktokglobalshop.com` | 开发者在创建应用后调用 TTS Open API endpoint 使用的请求 host。使用 HTTPS。 |

不要将授权或 token domain 用作业务 API 请求 host。它们有不同的用途：
| **用途** | **Domain 或入口** | **使用场景** | **参考** |
| --- | --- | --- | --- |
| 业务 API 调用 | `https://open-api.tiktokglobalshop.com` | 调用授权、商品、订单、履约和 webhook 等 API endpoint。 | 当前页面 |
| 卖家授权 | 美国：`https://services.us.tiktokshop.com/open/authorize`；其他地区：`https://services.tiktokshop.com/open/authorize` | 发起卖家或店铺授权并获取授权码。不要将此 host 用作 API endpoint host。 | [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
| Partner 授权 | 美国：`https://partner.us.tiktokshop.com/open/authorize`；其他地区：`https://partner.tiktokshop.com/open/authorize` | 发起 partner 授权并获取授权码。不要将此 host 用作 API endpoint host。 | [Partner authorization guide](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide) |
| Creator 授权 | `https://shop.tiktok.com/alliance` | 发起 creator 授权。不要将此 host 用作 API endpoint host。 | [Creator authorization guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide) |
| Token 交换 | `https://auth.tiktok-shops.com` | 将授权码交换为 token 或刷新 token。 | [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) |
| 沙盒和 API 测试 |  <br/>  | 使用 Sandbox 应用设置和 [API testing tool](https://partner.tiktokshop.com/dev/api-testing-tool) 来测试调用，同时仍遵循 endpoint reference 获取确切的路径和方法。 | [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) |
# Category 快速参考
category 段按业务领域对 endpoint 进行分组。请始终从 endpoint reference 页面复制最终的方法和路径，因为 version 和 resource 名称可能因 API 而异。
| **业务领域** | **常用 category 段** | **示例 resource** | **参考** |
| --- | --- | --- | --- |
| 授权 | `authorization` | `shops` | [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| 商品 | `product` | `products`、`categories`、`inventory` | [Product API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview) |
| 订单 | `order` | `orders` | [Order API overview](https://partner.tiktokshop.com/docv2/page/order-api-overview) |
| 履约 | `fulfillment` | `packages`、`shipping_documents` | [Fulfillment API overview](https://partner.tiktokshop.com/docv2/page/fulfillment-api-overview) |
| 退货与退款 | `return_refund` | `returns`、`refunds`、`cancellations` | [Return & Refund API overview](https://partner.tiktokshop.com/docv2/page/return-refund-and-cancel-api-overview) |
| 物流 | `logistics` | `warehouses`、`delivery_options`、`shipping_providers` | [Logistics API overview](https://partner.tiktokshop.com/docv2/page/logistic-api-overview) |
| 促销 | `promotion` | `promotions`、`discounts` | [Promotion API overview](https://partner.tiktokshop.com/docv2/page/promotion-api-overview) |
| 财务 | `finance` | `payments`、`settlements` | [Finance API overview](https://partner.tiktokshop.com/docv2/page/finance-api-overview) |
| 卖家 | `seller` | `shops` | [Seller API overview](https://partner.tiktokshop.com/docv2/page/seller-api-overview) |
| 事件 | `event` | `webhooks` | [Events API](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) |
| 供应链 | `supply_chain` | `packages`、`shipments` | [Supply Chain API](https://partner.tiktokshop.com/docv2/page/confirm-package-shipment) |
# 版本和路径指南
version 段是 endpoint 路径的一部分，必须与 API reference 页面匹配。不要假设所有 endpoint 使用相同的版本。有关版本选择和迁移指南，请参阅 [TTS API versioning](https://partner.tiktokshop.com/docv2/page/api-versioning)。
在排查请求失败时，请首先检查以下内容：
| **症状** | **可能的原因** | **需要检查的内容** |
| --- | --- | --- |
| `36009010 Invalid method` | HTTP 方法与 endpoint reference 不匹配。 | 重新打开 endpoint reference 并使用其中显示的确切方法。 |
| 签名验证失败 | 签名的路径或时间戳与实际请求不匹配。 | 确认签名路径包含 `/{category}/{version}/{resource}`，并遵循 [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。 |
| Host 或 DNS 混淆 | 将授权、token 或测试 domain 用作了业务 API host。 | 对于业务 API 调用，使用 `https://open-api.tiktokglobalshop.com`。 |
