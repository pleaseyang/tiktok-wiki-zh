# 测试你的应用

在上线应用之前，请在 Partner Center 中使用 Development Shop（Sandbox）和 API Testing Tool 进行测试。这些 Partner Center 工具帮助你模拟卖家工作流、授权测试卖家账户到未发布的应用，并在发布前验证 API 请求和响应。
部分测试流程会为测试卖家账户打开 Seller Center。请仅在 Development Shop（Sandbox）测试流程中使用 Seller Center；应用创建、测试账户、API 权限范围、授权和 API 测试请从 Partner Center 管理。
使用以下工具进行应用测试：

* 开发店铺（Sandbox）
* API 测试工具
* Postman 或 cURL 用于本地和脚本化 API 测试

# Development Shop
Development Shop 是 Partner Center 中的沙箱测试环境。相关指南也可能将此工具称为 Sandbox 或 Development Shop（Sandbox）。在本指南中，使用 Development Shop（Sandbox）指代同一个 Partner Center 测试工具。
Development Shop 允许你通过模拟卖家和买家工作流来构建和测试应用，而不会影响生产店铺数据。Full Function 测试账户可以支持类似生产的卖家工作流，包括商品管理、订单、退货、退款、促销和客户支持功能。
对于未发布的应用，你只能使用通过 Development Shop（Sandbox）创建的测试卖家账户进行测试。创建测试卖家账户，从该测试卖家账户授权你的应用，然后使用生成的授权数据调用 API 并验证集成。
**了解更多：** [Development Shop](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops)
# Development Shop 限制
在创建测试账户之前，请查看以下限制：

* 不要将生产 TikTok 账户用作官方测试账户或买家测试账户。
* 一旦 TikTok 账户在 Development Shop（Sandbox）中关联，它将被转换为测试账户。此操作是永久性的，无法撤销。
* TikTok 账户必须与测试店铺在同一地区。如果你不在同一地区，请在创建和关联测试账户之前使用所需的地区设置，例如移除 SIM 卡并使用与测试店铺地区匹配的 VPN/IP 位置。
* Development Shop（Sandbox）数据与生产环境隔离。测试操作不会影响真实订单、真实用户或生产店铺数据。
* API Testing Tool 保持应用和店铺授权限制与线上一致，而沙箱店铺可能会跳过地区限制验证以方便测试。

# 如何测试 API
测试应用与 TikTok Shop 的集成涉及配置 API 权限范围、完成授权以及调用应用使用场景所需的 API。
根据你需要测试的内容选择指南：

* [API Testing Tool](https://partner.tiktokshop.com/docv2/page/api-testing-tool) - 当你想直接在 Partner Center 中测试并检查确切的请求参数、响应参数、示例代码和 API 文档指引时使用。
* [调用 Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/call-get-authorized-shops) - 当你拥有 access token 和签名后，作为第一个 API 调用指南使用。它解释了 Open API 域名、必需的请求头、必需的 query 参数和 Get Authorized Shops 请求。
* [如何使用 Postman 调用 API](https://partner.tiktokshop.com/docv2/page/call-tts-apis-with-postman) - 当你需要使用 Postman 环境、变量、预请求脚本和保存的请求进行本地、可重复或脚本化 API 测试时使用。

使用 API Testing Tool 进行快速 Partner Center 测试和请求/响应检查。当你需要重复测试同一 API 流程、自动化签名或调试本地集成时，使用 Postman、cURL 或你自己的后端代码。
# 最低测试检查清单
在提交 public 应用审查或发布 custom 应用之前，请使用此检查清单：

1. 在 Partner Center 中创建或确认你的应用。
2. 为你支持的使用场景配置所需的 API 权限范围和 webhook 设置。
3. 创建 Development Shop（Sandbox）测试卖家账户和买家测试账户。
4. 使用 Development Shop（Sandbox）测试卖家账户授权应用。
5. 安全地生成和存储测试 access token。
6. 调用应用的核心 API，如授权、商品、订单、履约、物流、退货、退款或客户服务 API，具体取决于你的权限范围。
7. 确认你的应用正确处理 `shop_cipher`、卖家/店铺地区、token 过期、token 刷新、错误码和 API 签名。
8. 触发并验证所需的 webhook，包括投递、重试处理、去重和幂等处理。
9. 在 Development Shop（Sandbox）中端到端运行卖家和买家工作流，包括商品设置、下单、订单状态变更、取消、退货或退款流程（视情况而定）。
10. 在进入应用审查或上线之前，记录测试证据、关键请求 ID、webhook 事件 ID 和未解决的问题。

# 如何获取测试帮助
如果你对测试应用有疑问，可以通过以下方式联系 Partner Center 支持团队：

* [通过电子邮件联系我们](https://partner.tiktokshop.com/docv2/page/how-to-contact-support#Option%201:%20Contact%20us%20through%20email)
* [通过 Partner Center 提交工单](https://partner.tiktokshop.com/docv2/page/how-to-contact-support#Option%202:%20Submit%20a%20ticket%20through%20the%20Partner%20Console)（需要登录）

# 后续步骤
继续前往[应用上线概述](https://partner.tiktokshop.com/docv2/page/app-launch-overview)，了解如何在 TTS App & Service Store 上发布和上架你的应用。
