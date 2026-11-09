# 创建你的应用

# 在 Partner Center 中创建你的应用
在 Partner Center 中创建应用可建立与 TikTok Shop 服务集成所需的工作空间和凭据。在此工作空间中，你选择应用类型、服务类别、市场、卖家类型、API 权限范围、redirect URL、webhook 设置和应用凭据。
本指南说明如何创建 **Public 应用** 或 **Custom 应用**，以及应用开发者（ISV）如何向现有应用添加符合条件的目标市场。
对于仅 OAuth 设置流程，请使用[创建 TikTok Shop 应用 OAuth client](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client)。该页面应专注于 OAuth client 配置：redirect URL、授权链接、授权码、token 交换和 refresh token 处理。
# 创建应用之前
在点击 **Create app & service** 之前，请完成以下检查清单：
| 检查项 | 重要性 |
| --- | --- |
| 开发者账户和入驻已完成或进行中 | Partner Center 应用创建取决于你的开发者账户状态和开发者类型。请参阅[开发者入驻](https://partner.tiktokshop.com/docv2/page/developer-onboarding)。 |
| 开发者类型已明确 | ISV、卖家开发者、系统集成商和合作伙伴可能遵循不同的审查和上线路径。 |
| 应用类型已明确 | 如果卖家应在 App and Service Store 中发现应用，选择 **Public app**。如果应用通过授权链接私下分发，选择 **Custom app**。 |
| 服务类别已明确 | 类别影响可用权限范围、审查预期和应用定位。Connector 应用可能有额外审查要求。 |
| 目标市场和卖家类型已确认 | 选择与应用预期用户匹配的市场和卖家类型。符合条件的 ISV 应用可以使用下方 **向现有应用添加市场** 中的步骤稍后添加目标市场。添加市场与更改现有市场或卖家类型配置不同。 |
| Redirect URL 已就绪 | 需要在卖家或合作伙伴授权你的应用后接收授权 `code`。使用安全的后端控制 endpoint。 |
| Webhook URL 已就绪（如需要） | 需要接收订单、商品、履约、授权和其他事件的推送通知。 |
| 合规和法律审查路径已了解 | 审查要求因应用类型、类别、市场和数据访问而异。美国和英国合作伙伴应尽早启动合规/法律审查，因为这可能需要三周或更长时间。 |
# 应用类型决策
有两种主要应用类型：public 和 custom。
| 项目 | Public 应用 | Custom 应用 |
| --- | --- | --- |
| 可见性 | 批准后在 TikTok Shop App and Service Store 中上架。卖家可以发现、安装和授权它。 | 不公开上架。开发者与选定的卖家分享私有授权链接。 |
| 典型使用场景 | 面向众多卖家的 SaaS 或集成应用。 | 卖家特定或合作伙伴管理的解决方案，通常为单个卖家或有限卖家群体构建。 |
| 应用列表详情 | 店铺上架必需。 | 通常不需要，除非 Partner Center 要求。 |
| 分发方式 | App and Service Store 上架。 | 私有授权链接。 |
| 审查标准 | Public 应用在上架前需要应用审查。 | Custom 应用通常通过授权链接私下上线，无需 public 应用上架审查，但如果应用是 Connector 应用、达到 25 个或以上卖家授权，或 Partner Center / 你的合作伙伴 manager 指示所选类别或市场需要审查，则需要应用审查。 |
可在相关文档中复用的标准措辞：
```Plain Text
Custom 应用通常通过授权链接私下上线。仅适用的 custom 应用需要应用审查，如 Connector 应用、拥有 25 个或以上卖家授权的 custom 应用，或 Partner Center 要求审查的类别或市场中的应用。
```

# Connector 和 25 卖家审查规则
**Connector** 应用是一个应用类别，用于将 TikTok Shop 与外部系统连接的集成，如电商平台、ERP、OMS、WMS、3PL、feed 工具或其他卖家操作系统。Connector 应用通常跨系统同步商品、订单、库存、履约或其他卖家数据，因此即使应用私下分发，TikTok Shop 也可能要求审查。
对于 custom 应用：

* 如果应用类别为 **Connector**，请准备应用审查。
* 如果应用达到 **25 个或以上卖家授权**，请在更广泛使用之前准备应用审查。
* 如果 Partner Center 显示审查要求状态、审查横幅、发布限制或 **Submission materials for review** 入口，请在扩展分发之前按照该流程操作。
* 如果你认为应用低于阈值但仍看到审查要求，请联系你的合作伙伴 manager 或提交 Partner Center 支持工单，附上 app key、service ID、应用类别、市场、卖家类型和截图。

# 创建应用
创建应用的步骤：

1. 登录目标市场对应的 Partner Center。
2. 从导航面板打开 **App & Service**。
3. 点击 **Create app & service**。
4. 选择 **Public** 或 **Custom**。
5. 选择 **Service category** 并设置 **default name**。
6. 可选上传 logo。
7. 选择 **Market** 和 **Seller type**。
8. 如果应用将调用 TikTok Shop API，开启 **Enable API**。
9. 配置 redirect URL 和 webhook URL。
10. 点击 **Create**。

字段参考：
| 字段 | 含义 | 备注 |
| --- | --- | --- |
| App type | Public 或 Custom。 | 根据卖家如何发现和授权应用来选择。 |
| Service category | 应用的业务类别，如 Connector 或 Partner Center 中显示的其他类别。 | 类别可能影响可用权限范围、审查要求和上线流程。 |
| Default name | Partner Center 中显示的默认应用/服务名称，用作后备显示文本。 | Public 应用可能稍后需要本地化列表内容。 |
| Logo | 应用图标或 logo。 | 初始创建时可选，但 public 列表通常需要精美的品牌资产。 |
| Market | 应用将运营或上架的市场。 | 选择应用将运营的市场。要将现有 ISV 应用扩展到另一个符合条件的市场，请按照下方 **向现有应用添加市场** 操作。 |
| Seller type | 应用支持的卖家模式。 | **Local** 通常表示本地到本地的卖家/店铺场景。**Cross-border** 表示跨境卖家场景，可能需要额外标识符如 `shop_cipher` 或全球商品流程。 |
| Enable API | 为应用开启 API 集成设置。 | 如果应用需要 OpenAPI 权限范围、卖家授权、token 交换或 webhook，请启用此选项。 |
| Redirect URL | 接收授权 `code` 的回调 endpoint。 | Token API 使用返回的 `code` 值作为 `auth_code` 参数。 |
| Webhook URL | 接收事件通知的回调 endpoint。 | 你也可以稍后通过 Events API 和 Partner Center webhook 设置管理店铺 webhook。 |
# 向现有应用添加市场
如果你是应用开发者或系统集成商（ISV），可以向现有的 **Public** 或 **Custom** 应用添加符合条件的目标市场。你不需要仅为了扩展到另一个市场而创建新应用。
可用市场取决于你公司的注册区域和应用的业务类别。此流程适用于 ISV 应用；卖家开发者应用和代理服务遵循各自的入驻流程。
## 从你的应用开始

1. 在 Partner Center 中打开 **App & Service**，点击要扩展的应用的 **Manage**。
2. 在应用详情中，点击 **+ Add market（Seller type）**。
3. 如果所需市场可选，选择它并继续下方的 **将市场保存到你的应用**。
4. 要注册尚无该类别资格记录的其他市场，请在 **Target market** 下拉菜单中点击 **Add manually**。从该表单中提供的市场中进行选择。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/06db076e14974d0995142c834af6e249~tplv-k9wyc2ijk0-image.image)

如果市场已列出但不可选，请检查你个人资料中该市场的现有资格记录并完成所需操作。如果它已添加到应用中，请管理现有市场条目。创建另一个资格记录不会移除这些限制。
## 为新市场提供信息

1. 检查 **Business category**。它设置为你来自的应用的类别，在此流程中无法更改。
2. 选择要添加的可用 **Target market** 选项。你一次最多可以选择 **10 个市场**，然后点击 **Next**。
3. 查看 **合作伙伴 info** 表单。使用相同表单的市场可能归在一起；具有不同要求的市场有单独的表单。检查任何预填信息并完成每个表单中的所有必填字段。
4. 点击 **Submit** 将你的资格信息保存为草稿并返回原始应用。对于有资格添加的市场，添加市场对话框将打开并显示你的选择。

保存此草稿不会启动资格审查。如果 Partner Center 要求你在添加市场之前完成资格审查：

1. 打开你的个人资料，找到该类别和市场的资格记录。
2. 点击 **Edit**，完成所需信息并在资格表单中点击 **Submit** 提交审查。
3. 查看审查结果，当市场可添加时返回应用。

> **已添加？** 具有该类别现有资格记录的市场不能在此新市场流程中再次选择，即使该记录仍是草稿、审查中或未批准。在你的个人资料中打开现有记录以检查其状态和可用操作。现有资格记录不一定意味着该市场已添加到此应用中。

## 将市场保存到你的应用

1. 在添加市场对话框中，检查每个市场并选择其 **Seller type**。如果显示，完成所需的跨境基础国家。
2. 点击 **Save**。
3. 确认市场出现在应用的目标市场列表中。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/93988071c12a4466b042662bb5443c34~tplv-k9wyc2ijk0-image.image)

当对话框在你从合作伙伴 info 返回后打开时，它仅预填市场。你仍需完成卖家设置并点击 **Save**。如果你在保存之前关闭对话框，请重新打开 **+ Add market（Seller type）** 完成添加。
## 完成每个市场的要求
添加资格信息、向应用添加市场以及在该市场上线应用是不同的步骤。在应用详情中检查每个市场的审查状态和可用操作。
如果你已添加市场但其资格信息仍是草稿，请在应用详情中展开该市场并点击资格审查项上的 **Edit**。完成所需信息并在审查表单中点击 **Submit**。该表单中的 **Save** 仅保存草稿；不会提交信息进行审查。

* 对于 **Public 应用**，完成所需的市场语言列表和审查，然后按照[发布和上架 public 应用](https://partner.tiktokshop.com/docv2/page/publish-and-list-public-app)中的发布步骤操作。
* 对于 **Custom 应用**，完成所选市场显示的要求，并按照[发布 custom 应用](https://partner.tiktokshop.com/docv2/page/publish-custom-app)操作。

有关解释审查进度或重新提交材料的帮助，请参阅[应用审查流程](https://partner.tiktokshop.com/docv2/page/app-review-process)。
# 授权域名和 token 交换
不要混淆授权入口域名、token 域名和 OpenAPI 资源域名。它们服务于不同目的。
| 用途 | 美国域名 / endpoint | 其他地区域名 / endpoint | 使用时机 |
| --- | --- | --- | --- |
| Partner Center 账户、应用创建和文档 | `https://partner.us.tiktokshop.com` | `https://partner.tiktokshop.com` | 创建或管理开发者账户、应用、服务、审查和支持工单。 |
| 卖家授权入口 | `https://services.us.tiktokshop.com/open/authorize` | `https://services.tiktokshop.com/open/authorize` | 卖家授权你的应用访问卖家拥有的店铺数据。 |
| 合作伙伴授权入口 | `https://partner.us.tiktokshop.com/open/authorize` | `https://partner.tiktokshop.com/open/authorize` | 合作伙伴授权访问合作伙伴拥有的业务类目数据，如已批准的 Affiliate Partner API。 |
| Token 交换 | `https://auth.tiktok-shops.com/api/v2/token/get` | 相同 | 将授权码交换为 `access_token` 和 `refresh_token`。 |
| Token 刷新 | `https://auth.tiktok-shops.com/api/v2/token/refresh` | 相同 | 刷新过期的 access token。 |
| OpenAPI 资源调用 | `https://open-api.tiktokglobalshop.com` | 相同 | 在拥有有效 token 和签名后调用业务 API。 |
使用与数据所有者匹配的授权指南：

* 卖家拥有的店铺数据：[Authorization guide](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) 或 [Authorization overview](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)
* 合作伙伴拥有的数据：[Partner authorization guide](https://partner.tiktokshop.com/docv2/page/partner-authorization-guide)
* 达人拥有的数据：[Creator authorization guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide)

授权后，TikTok Shop 使用一次性授权码重定向到你配置的 **Redirect URL**。重定向参数通常显示为 `code`；将该值作为 `auth_code` 传递给 token API。
Token 交换示例：
```HTTP
GET https://auth.tiktok-shops.com/api/v2/token/get?app_key={app_key}&app_secret={app_secret}&auth_code={code_from_redirect}&grant_type=authorized_code
```

必需的 token 参数：
| 参数 | 是否必需 | 描述 |
| --- | --- | --- |
| `app_key` | 是 | 在 Partner Center 中为你的应用生成的 App Key。 |
| `app_secret` | 是 | 为你的应用生成的 App Secret。仅存储在服务器端，永远不要在前端代码、日志、截图或工单中暴露。 |
| `auth_code` | 是 | 返回到你的 Redirect URL 的授权码。该码短期有效且只能使用一次。 |
| `grant_type` | 是 | 必须准确为 `authorized_code`。不要使用标准 OAuth 拼写 `authorization_code`。 |
# 应用凭据
创建后，Partner Center 显示应用或服务详情页面。你可以稍后从以下位置找到应用凭据：
```Plain Text
Partner Center
  -> App & Service
  -> 选择你的应用或服务
  -> App credentials / Basic information
```

| 凭据 | 含义 | 处理要求 |
| --- | --- | --- |
| App Key | 应用/服务的公共标识符。 | 用于 token 请求和签名的 OpenAPI 请求。 |
| App Secret | 为应用/服务生成的密钥。 | 仅在服务器端存储。用于 token 交换和请求签名。不要将其暴露给浏览器、移动应用、客户端脚本、截图或日志。 |
| Service ID | 某些授权链接流程使用的标识符。 | 在手动构建授权链接或 Partner Center 要求服务级别标识时使用。 |
# Scope 和授权检查
创建应用不足以调用 API。在要求卖家授权之前：

1. 仅启用你的应用所需的 API 权限范围。
2. 在 API 参考文档中确认 endpoint 所需的权限范围。
3. 在启用所需权限范围后完成卖家授权。
4. 检查 token 响应中的 `granted_scopes` 字段，确认卖家授予了预期的权限范围。
5. 如果你稍后添加权限范围，请要求卖家重新授权，以便新 token 包含新权限范围。

# 文档边界
一起使用这些页面，但保持其职责分离：
| 页面 | 负责 | 不负责 |
| --- | --- | --- |
| 创建您的应用 | 应用类型选择、应用创建字段、向现有 ISV 应用添加符合条件的目标市场、凭据和高级审查规则。 | 详细的 OAuth 回调实现或 token 刷新逻辑。 |
| [Create a TikTok Shop app OAuth client](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client) | OAuth client 设置、redirect URL 行为、授权码处理、token 交换和 refresh token 流程。 | Public 与 custom 应用策略或应用上线审查路径。 |
| [App development overview](https://partner.tiktokshop.com/docv2/page/app-development-overview) | 端到端开发生命周期：设计、创建、测试、审查、上线。 | 逐字段的应用创建说明。 |
| [App launch overview](https://partner.tiktokshop.com/docv2/page/app-launch-overview) | Public 和 custom 应用的发布和上线路径。 | 初始应用创建详情。 |
| [App review process](https://partner.tiktokshop.com/docv2/page/app-review-process) | 审查材料、审查工作流和审查状态。 | OAuth token 交换或 API 签名。 |
# 后续步骤
创建应用后：

1. 在 Partner Center 中配置所需的 API 权限范围。
2. 配置并测试 Redirect URL。
3. 如果应用依赖事件通知，配置 webhook 主题。
4. 生成测试授权码并将其交换为 token。
5. 调用 [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) 确认 token 和店铺映射。
6. 使用 [Development Shop](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops) 和 [API Testing Tool](https://partner.tiktokshop.com/dev/api-testing-tool) 进行测试。
7. 按照适用于应用类型、类别、市场和卖家授权规模的上线或审查路径操作。
