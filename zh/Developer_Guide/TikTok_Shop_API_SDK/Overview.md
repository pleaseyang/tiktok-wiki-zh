# 概述

TikTok Shop API SDK 帮助您的 TikTok Shop 应用后端以更少的集成工作调用 TikTok Shop API。它们生成请求客户端并处理常见的请求身份验证步骤，因此您无需为每个受支持的 API 调用自行实现签名流程。
# 可用性
拥有有效 TikTok Shop 应用的开发者可以从 Partner Center 访问 API SDK 下载页面。要下载有用的 SDK 包，请使用拥有或管理应用的开发者账户登录，然后确认 SDK 页面上显示的有效应用和 API 访问权限范围。
以 SDK 下载页面作为账户特定访问权限的权威来源。如果您的账户看不到 API SDK 入口，请先确认您已创建 TikTok Shop 应用并启用了集成所需的 API 权限范围。如果入口仍不可用，请联系 Partner Center 支持或您的 TikTok Shop 合作伙伴经理。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/81b2df68-85e8-4ded-8225-59e4f9a3063b.png)
# 支持的语言和版本
SDK 目前支持 Java、Go 和 Node.js。SDK 包根据您的有效应用、已批准的 API 权限范围、所选语言和可用 API 版本生成，因此可能不存在适用于每个开发者的单一全局"最新 SDK 版本"。
在集成或更新 SDK 之前，请在 [API SDK 下载页面](https://partner.tiktokshop.com/openlearn/api-sdk) 上确认语言、SDK 版本、生成时间、包含的应用和包含的 API 权限范围。如果您需要新批准的权限范围、新发布的 API 或 SDK 框架更新，请参阅[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。
| 语言 | 使用的最新 SDK 版本 | 支持的 API 版本 |
| --- | --- | --- |
| Java | 使用 SDK 下载页面或下载的包文件（如 `pom.xml` 或 `build.gradle`）中显示的版本。将示例中的占位符值（如 `1.0.0`）替换为下载的版本。 | 下载的包中包含的 API 版本。Java 指南示例包含版本化客户端，如 `AuthorizationV202309Api` 和 `ProductV202502Api`。 |
| Go | 使用下载的 SDK 包中生成的模块版本。将占位符值（如 `v1.0.0`）替换为您的包中的版本。 | 下载的包中包含的 API 版本。Go 指南示例包含版本化客户端，如 `AuthorizationV202502API` 和 `ProductV202502API`。 |
| Node.js | 使用 SDK 下载页面生成的 Node.js SDK 包或文件夹。不要假设示例依赖版本是最新的 SDK 包版本。 | 下载的包中包含的 API 版本。Node.js 指南示例包含版本化客户端，如 `AuthorizationV202309Api` 和 `ProductV202502Api`。 |
# 选择 SDK 或手动签名
当您使用 Java、Go 或 Node.js 集成且所需 API 包含在生成的 SDK 包中时，请使用 SDK。SDK 是常规 API 调用的首选路径，因为它减少了重复的请求构建和签名工作。
当您从另一种语言调用 TikTok Shop API、使用不使用 SDK 的自定义 HTTP 客户端、调试原始 HTTP 请求，或调用未包含在生成的 SDK 包中的 API 时，请使用手动签名。有关签名算法和语言示例，请参阅[签名您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。
# Webhook 配置
API SDK 用于发起 TikTok Shop API 请求。它不能替代您的 webhook 配置或 webhook 监听器实现。在 Partner Center 或通过 Events API 配置 webhook 回调 URL 和事件订阅，然后实现您自己的 HTTPS endpoint 来接收和处理 webhook 事件。
有关 webhook 设置，请参阅[配置指南](https://partner.tiktokshop.com/docv2/page/configuration-guide)。有关 Events API 参考，请参阅 [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) 和 [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook)。
# 集成指南
使用与您下载的 SDK 包匹配的语言指南：
| 语言 | 集成指南 | 指南中的最低环境要求 |
| --- | --- | --- |
| Java | [集成 Java SDK](https://partner.tiktokshop.com/docv2/page/integrate-java-sdk) | Java 1.8+；Maven 3.8.3+ 或 Gradle 7.2+ |
| Go | [集成 GoLang SDK](https://partner.tiktokshop.com/docv2/page/integrate-golang-sdk) | Go 1.18+ |
| Node.js | [集成 Node.js SDK](https://partner.tiktokshop.com/docv2/page/integrate-nodejs-sdk) | Node.js 16+ |
# 下载和更新流程

1. 创建 TikTok Shop 应用并配置集成所需的 API 权限范围。
2. 在 Partner Center 中打开 [API SDK](https://partner.tiktokshop.com/openlearn/api-sdk)。
3. 查看生成的 SDK 中包含的有效应用和合并 API 访问权限范围。
4. 选择 Java、Go 或 Node.js，并确认页面上显示的 SDK 版本和生成时间。
5. 下载 SDK 包并按照匹配的语言指南进行集成。
6. 当权限范围、API 版本或 SDK 框架支持发生变更时，按照[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) 操作并下载重新生成的包。

# 相关页面
| 页面 | 用途 |
| --- | --- |
| [下载 SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) | 查找 SDK 下载入口，确认有效应用、权限范围、语言、版本和生成时间。 |
| [更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) | 了解 SDK 重新生成触发条件、每日生成和手动更新检查。 |
| [创建您的应用](https://partner.tiktokshop.com/docv2/page/create-your-app) | 创建应用并配置应用类型、权限范围、重定向 URL、webhook URL、app key 和 app secret。 |
| [生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) | 在对卖家或店铺数据发起 SDK 调用之前生成 access token。 |
| [签名您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | 当 SDK 不适合时，手动实现请求签名。 |
| [配置指南](https://partner.tiktokshop.com/docv2/page/configuration-guide) | 配置 webhook 回调 URL 和事件订阅。 |

