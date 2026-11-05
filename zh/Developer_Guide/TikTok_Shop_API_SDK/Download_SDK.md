# 下载 SDK

# 概述
当您首次需要下载 TikTok Shop Open API SDK 时，请使用本页面。
TikTok Shop SDK 包是根据您的 Partner Center 账户可用的有效应用和 API 访问权限范围生成的。SDK 包可能因应用、语言、API 版本和权限范围集而异。在将 SDK 添加到项目之前，请始终在 SDK 下载页面上确认应用列表、权限范围列表、语言、SDK 版本和生成时间。
# 下载前准备
首次集成请按以下顺序操作：
| 步骤 | 下载前是否需要？ | 调用 SDK API 前是否需要？ | 操作说明 |
| --- | --- | --- | --- |
| 创建 TikTok Shop 应用 | 是 | 是 | 创建应用并配置基本应用信息。请参阅[创建您的应用](https://partner.tiktokshop.com/docv2/page/create-your-app)或[创建 TikTok Shop 应用 OAuth 客户端](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client)。 |
| 配置 API 权限范围 | 是（如果 SDK 需要包含这些 API 域） | 是 | 在 **App & Service > Manage > Manage API** 中，启用或申请集成所需的 API 权限范围。 |
| 下载 SDK | 是 | 是 | 从 SDK 下载页面下载为所选语言生成的 SDK 包。 |
| 创建测试卖家账户或使用已授权卖家 | 否 | 是 | 对于测试调用，创建测试卖家账户或使用符合条件的卖家账户。请参阅[创建测试卖家账户](https://partner.tiktokshop.com/docv2/page/create-test-seller-account)。 |
| 获取 access token | 否 | 是 | 完成卖家授权并将授权码交换为 `access_token`。请参阅[生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token)。 |

这种区分是有意为之：创建应用和配置权限范围是生成有用 SDK 包的必要条件；测试卖家账户和 access token 是在实际运行访问卖家或店铺数据的 SDK 调用时才需要的。
# SDK 下载入口
从 Partner Center 打开 SDK 下载页面：
| 入口类型 | 路径或 URL |
| --- | --- |
| Partner Center 路径 | **Partner Center Console > Development Kits > API SDK** 或 Partner Center 导航中显示的等效 SDK 下载入口。 |
| 直接 URL | [https://partner.tiktokshop.com/openlearn/api-sdk](https://partner.tiktokshop.com/openlearn/api-sdk) |

如果您的 Partner Center UI 使用了略有不同的标签，请在 **Development Kits** 下搜索 **API SDK** 或 **SDK**。请勿将此入口与 **App & Service > Manage API** 混淆，后者用于配置 API 权限范围，而非下载 SDK 包。
# 下载步骤

1. 使用拥有或管理应用的开发者账户登录 Partner Center。
2. 打开 **Development Kits > API SDK**。
3. 查看页面上显示的有效应用。
4. 查看生成的 SDK 中包含的合并 API 访问权限范围。
5. 选择您计划集成的 SDK 语言，例如 Java、Go 或 Node.js（如果页面上提供这些选项）。
6. 检查该语言显示的 SDK 版本和生成时间。
7. 下载 SDK 包。
8. 将下载的包版本、生成时间、app key、语言和权限范围集记录在项目发布说明中，以便未来的 SDK 更新可追溯。

# 截图参考
以下截图保留自原始指南。请结合上方的文字步骤使用。
| 截图 | 查看要点 | 操作 |
| --- | --- | --- |
| SDK 下载页面 | 有效应用、合并 API 访问权限范围、语言选择器或语言标签页、SDK 版本/生成时间和下载按钮。 | 确认 SDK 包含您需要的 API 和权限范围，然后下载适用于项目语言的包。 |

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/download_sdk.PNG)
# 语言和版本选择
SDK 下载页面是当前可用 SDK 语言和包版本的权威来源。
各语言的集成指南目前涵盖：
| 语言 | 集成指南中的最低环境要求 | 版本指南 |
| --- | --- | --- |
| Java | Java 1.8+；Maven 3.8.3+ 或 Gradle 7.2+ | 将示例中的占位符版本（如 `1.0.0`）替换为下载页面显示的 SDK 版本。 |
| Go | Go 1.18+ | 使用下载的 SDK 包中生成的模块路径和版本。 |
| Node.js | 新集成请使用受支持的 Node.js LTS 版本。 | 使用下载页面生成的包或文件夹。不要假设带有占位符版本的示例是最新的包。 |

可能不存在适用于所有开发者的单一全局"最新 SDK 版本"。SDK 包是基于您的有效应用、语言、API 权限范围和 API 版本生成的。如果 SDK 页面显示版本号或生成时间戳，请将该值用于项目记录。
# 权限范围覆盖
SDK 包含您有效应用的合并 API 访问权限范围内的 API。在下载之前，请确认页面上显示的权限范围与您的集成所需的 API 匹配。
| 权限范围类型 | 含义 | 检查事项 |
| --- | --- | --- |
| 公共 API 权限范围 | 在应用设置和卖家授权后，符合条件的开发者可用的标准 API 权限范围。 | 在 **App & Service > Manage > Manage API** 中启用或申请，然后确认其出现在 SDK 权限范围列表中。 |
| 私有 API 权限范围 | 仅在 TikTok Shop 批准、邀请、市场/类目启用或合作伙伴特定访问后授予的限制性权限范围。可能并非对所有开发者可见。 | 如果您的集成需要私有权限范围，请按照 Partner Center 中显示的申请路径操作，或联系您的 Partner Center 支持/合作伙伴经理。批准后，确认私有权限范围出现在有效权限范围列表中，然后再下载 SDK。 |

在下载 SDK 后添加新的权限范围不会自动更新您现有的本地 SDK。确认新权限范围已获批准，如果新权限需要卖家同意则请卖家重新授权，然后下载重新生成的 SDK。
# 下载与更新
本页面涵盖首次 SDK 下载。如果您已集成 SDK 并需要刷新，请使用[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。
| 页面 | 用途 |
| --- | --- |
| 下载 SDK | 查找 SDK 页面，确认有效应用和权限范围，选择语言，并下载 SDK 包进行首次集成。 |
| 更新 SDK | 了解 SDK 何时重新生成、何时点击 **check for updates**、每日生成如何工作，以及如何迁移现有项目。 |
# 故障排除
| 症状 | 可能原因 | 操作 |
| --- | --- | --- |
| SDK 中缺少预期的 API | 有效应用未启用或未批准所需的 API 权限范围。 | 检查 **App & Service > Manage > Manage API** 并与 SDK 权限范围列表进行对比。 |
| 新批准的权限范围不在下载的 SDK 中 | SDK 包尚未重新生成。 | 等待每日生成或使用 SDK 页面上的 **check for updates**（如果可用）。 |
| 卖家 API 调用失败，但 SDK 包含该方法 | 卖家未授权所需的权限范围，或 token 不包含该范围。 | 完成卖家授权或重新授权，并检查 token 响应中的 `granted_scopes`。 |
| 示例中的语言版本与您的包不匹配 | 示例使用了占位符或旧版本。 | 使用下载的 SDK 包中显示的 SDK 版本和包结构。 |
# 相关页面
| 页面 | 用途 |
| --- | --- |
| [更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) | 重新生成触发条件、手动更新检查和迁移步骤。 |
| [创建您的应用](https://partner.tiktokshop.com/docv2/page/create-your-app) | 应用创建、应用类型选择、权限范围、重定向 URL 和应用凭证。 |
| [创建 TikTok Shop 应用 OAuth 客户端](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client) | 用于授权码和 token 交换的 OAuth 客户端设置。 |
| [创建测试卖家账户](https://partner.tiktokshop.com/docv2/page/create-test-seller-account) | 在调用 SDK API 之前设置测试卖家账户。 |
| [生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) | 用于测试 SDK 调用的 access token 生成。 |
| [访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope) | 权限范围概念和访问管理。 |




## 前提条件
如果您是为 TikTok Shop 开发应用的开发者，可以在 [TikTok Shop Partner Center 控制台](https://partner.tiktokshop.com/openlearn/api-sdk)上下载 TikTok Shop API SDK。
如果您是 TikTok Shop 的新开发者，必须在[控制台](https://partner.tiktokshop.com/openlearn/api-sdk)上下载 SDK 之前先[创建 TikTok Shop 应用](create-tts-app-oauth-client)。
## 下载 SDK
SDK 包含与您的有效应用对应的合并访问权限范围内的 API。页面上列出了有效应用和合并的访问权限范围（包括私有 API 权限范围）。在下载 SDK 之前，请确认 SDK 中包含的 API 访问权限范围。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/download_sdk.PNG)

