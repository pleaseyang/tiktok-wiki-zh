# 应用开发概述


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a7ac69987a034bda96296e0b6be8a4b5~tplv-k9wyc2ijk0-image.image)
本页面概述了 TikTok Shop 应用的典型开发流程。
如果你对任何步骤有疑问，请联系你的合作伙伴 manager 或在 Partner Center 提交支持工单。有关支持入口和工单指南，请参阅[如何联系支持](https://partner.tiktokshop.com/docv2/page/how-to-contact-support)。
**开发者类型很重要：** Public 应用、custom 应用、卖家开发者应用和系统集成商解决方案可能遵循不同的审查路径。在开始之前，请完成或查看[开发者入驻](https://partner.tiktokshop.com/docv2/page/developer-onboarding)，以了解适用于你的使用场景的应用和开发者类型。
**术语：** 本指南使用 **Development Shop（沙盒）** 作为 TikTok Shop 测试环境的标准名称。如果其他页面或 Partner Center 菜单使用 **Sandbox**，它指的是同一个 Development Shop 测试功能。
# 步骤 1：设计你的应用
使用你偏好的方法论规划和设计你的解决方案。在设计解决方案时，我们建议你：

* 查看 TikTok Shop API 和使用场景，确定要将哪些功能集成到你的应用中。
* 浏览 [TikTok Shop Seller Academy](https://seller-us.tiktok.com/university/home?identity=1&role=seller) 获取市场政策指南。了解卖家工作流程和平台政策有助于你设计符合卖家需求的应用。
* 在 [Development Shop（沙盒）](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops) 环境中创建卖家和买家测试账户，以便在上线前测试卖家和买家体验。

**注意：** TikTok Shop 为创建 public 应用的开发者或系统集成商提供设计审查支持。请联系你的合作伙伴 manager 了解详情。
# 步骤 2：在 Partner Center 创建你的应用
在 Partner Center 中创建应用可建立与 TikTok Shop 服务集成所需的工作空间和凭据。此步骤包括：

1. 确定你正在构建的应用类型，如 public 应用或 custom 应用。
2. 指定基本应用信息，如类别、目标市场、应用名称和图标。
3. 获取 TikTok Shop Open API 调用所需的应用 app key 和 app secret。
4. 为你的应用选择 API 权限范围并配置 webhook。

**了解更多：** 请参阅[创建你的应用](https://partner.tiktokshop.com/docv2/page/create-your-app)。我们还建议查看：

* [TikTok Shop API 概述](https://partner.tiktokshop.com/docv2/page/tts-api-concepts-overview)
* [认证指南](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309)
* [Webhook](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview)
* [Development Shop（沙盒）](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops)

# 步骤 3：测试你的应用
在 Partner Center 创建应用并构建集成后，请在上线前使用 TikTok Shop 服务进行测试。
如果你尚未创建，请在 [Development Shop（沙盒）](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops) 中创建卖家和买家测试账户。Development Shop（沙盒）允许你模拟卖家工作流程而不影响真实店铺数据。
**注意：**

* Public 应用必须在上线前完成测试。
* 为单个卖家构建 custom 解决方案的卖家开发者和系统集成商不需要完成 public 应用测试阶段，但仍建议在 Development Shop（沙盒）中进行测试。
* 你只能使用在 Development Shop（沙盒）中创建的测试卖家账户来测试未发布的应用。

**了解更多：** 请参阅[测试你的应用](https://partner.tiktokshop.com/docv2/page/test-your-app)和 [Development Shop（沙盒）](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops)。
# 步骤 4：启动审查并上线你的应用
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Develop_and_launch_a_TikTok_Shop_App/App_development_overview/Step4.jpeg)
上线应用意味着发布它供使用，对于 public 应用，还需将其上架到 TikTok Shop App and Service Store，以便卖家发现它。
审查要求因应用类型、应用类别、目标市场和卖家授权规模而异。Public 应用通常需要完整的上线审查路径。Custom 应用通常可以通过授权链接私下上线，但某些 custom 应用仍需审查，如 Connector 应用或拥有 25 个或以上卖家授权的 custom 应用。
**应用需求文档（ARD）** 是一份审查工作表，用于确认应用范围、所需 API、数据处理、测试证据和上线准备情况。如果你的类别或市场需要 ARD，请从你的合作伙伴 manager 或通过 [Partner Center 支持](https://partner.tiktokshop.com/docv2/page/how-to-contact-support)请求最新的 ARD 模板和提交路径。
## 上线要求快速参考
| 上线项目 | Public 应用 | Custom 应用 | 备注 |
| --- | --- | --- | --- |
| 开发者入驻 | 必需 | 必需 | 使用[开发者入驻](https://partner.tiktokshop.com/docv2/page/developer-onboarding)确认开发者和应用类型。 |
| 设计审查 | 建议或在要求时需要 | 单卖家 custom 解决方案通常不需要 | 如果你的 public 应用需要设计审查支持，请联系你的合作伙伴 manager。 |
| 在 Development Shop（沙盒）中测试 | 必需 | 建议 | 单卖家 custom 应用不需要完成 public 应用测试阶段，但应在生产使用前进行测试。 |
| 注册审查 | 必需 | 通常不需要 | Public 应用上线流程应从注册审查开始。 |
| 语言列表审查 | 每个列表语言或市场必需 | 不需要 | 为每个目标市场准备应用列表内容。 |
| 应用审查 | 必需 | 仅适用的 custom 应用需要 | 如果 custom 应用是 Connector 应用或达到 25 个或以上卖家授权，则可能需要审查。 |
| 合规和法律审查 | 适用时必需 | 适用时必需 | 数据安全、隐私和法律检查取决于应用范围和数据访问。 |
| 上市计划 | public 应用通常在要求时需要 | 单卖家 custom 解决方案通常不需要 | 与你的合作伙伴 manager 协调所需模板和时间线。 |
| Beta 测试 | public 应用通常在要求时需要 | 单卖家 custom 解决方案通常不需要 | Beta 测试可能是 public 应用上线准备的一部分。 |
| 上线方式 | 上架到 TikTok Shop App and Service Store | 私下发布并分享授权链接 | Public 应用可被卖家发现；custom 应用私下分发。 |
## Public 应用的典型上线流程
按以下顺序遵循 public 应用上线检查清单：

1. 启动并通过注册审查。
2. 为你打算上架应用的每个市场或语言启动并通过语言列表审查。
3. 启动并通过应用审查。
4. 当你的应用范围、数据访问、市场或类别要求时，通过合规和法律审查。
5. 将你的应用上架到 TikTok Shop App and Service Store。

## Custom 应用的典型上线流程
对于单卖家 custom 解决方案：

1. 发布你的应用。
2. 与卖家分享私有授权链接。
3. 让卖家授权该应用。

如果你的 custom 应用是 Connector 应用、达到 25 个或以上卖家授权，或属于需要审查的类别或市场，请在更广泛使用之前按照 Partner Center 或你的合作伙伴 manager 的审查说明操作。
**了解更多：** 请参阅[应用上线概述](https://partner.tiktokshop.com/docv2/page/app-launch-overview)、[发布和上架 public 应用](https://partner.tiktokshop.com/docv2/page/publish-and-list-public-app)、[应用审查流程](https://partner.tiktokshop.com/docv2/page/app-review-process)和[合规和法律审查流程](https://partner.tiktokshop.com/docv2/page/data-security-and-privacy-review)。
# 后续步骤
继续前往[创建你的应用](https://partner.tiktokshop.com/docv2/page/create-your-app)在 Partner Center 中创建你的应用。
