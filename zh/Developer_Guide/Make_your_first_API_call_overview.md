# 首次 API 调用概述

在开始本教程进行首次 TikTok Shop API 调用之前，你需要拥有一个 [TikTok Shop Partner Center](https://partner.tiktokshop.com) 账户，并且该账户必须已[注册为开发者](developer-onboarding)。
如果你已完成上述步骤，首次 TikTok Shop API 调用教程包含以下步骤：

1. [创建 TikTok Shop 应用（OAuth 客户端）](create-tts-app-oauth-client)：在 Partner Center 中创建应用，获取 API 认证所需的 App Key 和 App Secret。
2. [创建测试卖家账户](create-test-seller-account)：在 Development Shop 环境中设置测试卖家账户，用于 API 集成和测试。
3. [生成测试 access token](generate-test-access-token)：授权测试卖家账户并生成 access token 以访问 TikTok Shop API。
4. [创建签名哈希](create-hash-to-sign-your-test-api-call)：使用 App Secret 生成请求签名，确保 API 请求经过认证且安全。
5. [调用 Get Authorized Shops](call-get-authorized-shops)：进行首次 API 调用，验证认证流程和 API 集成是否正常工作。

或者，也可以直接在 Postman 中一键完成。详情请参阅 [Postman](https://partner.tiktokshop.com/docv2/page/call-your-first-api-using-postman) 文档。
## 后续步骤
进行首次 TikTok Shop API 调用的第一步是[创建 TikTok Shop 应用（OAuth 客户端）](create-tts-app-oauth-client)。

