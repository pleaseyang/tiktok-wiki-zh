# 更新 SDK

# 本页面涵盖内容
当您已集成 TikTok Shop SDK，且因应用、API 访问权限范围、API 版本或 SDK 框架发生变更而需要刷新时，请使用本页面。
有关首次 SDK 下载流程，请前往[下载 SDK](https://partner.tiktokshop.com/docv2/page/download-sdk)。为减少重复说明，请保持以下分工：
| 页面 | 用途 |
| --- | --- |
| [下载 SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) | 查找 SDK 下载页面，选择语言，并下载 SDK 进行首次集成。 |
| 更新 SDK | 了解何时出现更新的 SDK、如何触发更新检查、兼容性含义以及如何迁移现有项目。 |
# SDK 更新何时生成
当您的有效应用发生以下任何变更时，为您应用显示的 SDK 包可能会变化：

* API 访问权限范围被添加到您的应用或从应用中移除。
* API 在您应用的 API 访问权限范围集合内被添加、移除、升级或弃用。
* SDK 框架被升级。
* 受支持的语言版本被升级。

TikTok Shop 通过 [TikTok Shop 消息中心](https://partner.tiktokshop.com/message/list) 发送 SDK 更新通知。
[图片：TikTok Shop 消息中心 SDK 更新通知](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/message_center.png)
# 查找更新入口
要检查更新的 SDK，请打开您最初用于下载 SDK 的同一页面：

1. 前往 Partner Center。
2. 打开您要更新 SDK 的应用的控制台页面。
3. 打开[下载 SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) 中描述的 SDK 下载页面。
4. 检查 SDK 生成时间、SDK 版本、支持的语言和可用的 API 权限范围/API 集合。
5. 如果需要最新生成的包，请从此页面再次下载 SDK。

`check for updates` 按钮位于 SDK 下载页面上。当您刚更改了权限范围、应用配置、API 访问或语言要求，且不想等待下一次计划 SDK 生成时，请使用它。
[图片：SDK 下载页面上的 check for updates 按钮](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/check_for_updates.png)
# 每日生成和手动检查
SDK 按每日周期生成。手动 `check for updates` 按钮请求为下载页面上显示的应用和语言提前刷新。
点击 `check for updates` 后：

* 等待 SDK 页面显示更新的生成时间、包版本或下载包。
* 如果权限范围、API 访问、API 版本、SDK 框架或受支持语言版本没有实质性变更，生成的 SDK 可能保持不变。
* 如果生成仍在进行中，请稍后刷新 SDK 下载页面或查看消息中心的更新通知。
* 下载页面上显示的版本或生成时间是您应下载的包的权威来源。

# 兼容性和 API 退役
TikTok Shop 致力于保持新 SDK 版本的向后兼容性，但兼容性取决于您的应用使用的 API 版本和权限范围。
评估 SDK 更新时请使用以下规则：
| 变更类型 | 预期情况 | 您应执行的操作 |
| --- | --- | --- |
| 非破坏性 SDK 或 API 变更 | 现有 SDK 调用通常继续工作。可能会添加新方法或字段。 | 更新 SDK，运行构建/测试，并对关键流程进行冒烟测试。 |
| 具有破坏性变更的新 API 版本 | 破坏性 API 变更通过新 API 版本引入。旧版本可能在有限时间内仍可用。 | 在将代码更改为更新的 API 版本之前，阅读 API 参考和 [API 版本管理](https://partner.tiktokshop.com/docv2/page/api-versioning) 说明。 |
| API 版本退役 | 在新版本发布后，先前 API 版本至少保持 2 个月可用。退役将在[更新日志](https://partner.tiktokshop.com/docv2/changelog)中至少提前 2 个月公告。 | 在退役日期之前规划迁移。如果您调用已退役或无效的 API 版本，API 可能返回 `36009014`，提示版本名称无效。 |
| 权限范围或应用访问变更 | SDK 方法可能基于有效应用权限范围/API 集合而出现或消失。 | 确认您的应用权限范围，如果新权限需要重新授权则请卖家重新授权，然后下载重新生成的 SDK。 |

在更新生产流量之前，请查看：

* [更新日志](https://partner.tiktokshop.com/docv2/changelog)，了解发布、破坏性变更和退役通知。
* [API 版本管理](https://partner.tiktokshop.com/docv2/page/api-versioning)，了解版本命名、选择和退役行为。
* 您调用的每个 endpoint 的 API 参考页面，包括版本下拉菜单和迁移说明。

# 迁移步骤
每当您下载更新的 SDK 包时，请按照以下步骤操作：

1. 查看 SDK 下载页面和更新日志。确认变更内容：权限范围集合、API 版本、SDK 框架或语言支持。
2. 下载与项目使用的相同语言的 SDK 包。
3. 创建独立分支，并在该分支中替换生成的 SDK 文件夹、本地模块或包。
4. 更新依赖引用到新的 SDK 包或本地模块路径。
5. 为您的语言重新安装或重新构建依赖项。
6. 编译项目并修复 import、包、类或方法的变更。
7. 运行您的应用使用的 API 域的单元测试和集成测试。
8. 对每个更新的 API 域进行授权、token 刷新、请求签名和一个核心 API 调用的冒烟测试。
9. 逐步部署并监控 API 错误，特别是无效版本、权限、权限范围和签名错误。

# 各语言更新说明
| 语言 | 典型更新操作 |
| --- | --- |
| Java | 替换生成的 SDK 模块或 JAR，更新依赖版本或本地路径，然后运行 `mvn clean test`、`mvn install` 或您的 Gradle 构建命令。 |
| Go | 替换生成的 SDK 模块，根据需要更新模块路径或版本，然后运行 `go mod tidy`、`go test ./...` 和 `go build ./...`。 |
| Node.js | 替换生成的 SDK 文件夹或包，保留您的应用代码和配置文件，然后运行 `npm install`、`yarn install` 或 `pnpm install`，接着运行 TypeScript 构建和测试。 |

如果您的语言特定集成指南仍显示占位符版本（如 `1.0.0`），不要假设它是最新的 SDK 版本。请使用 SDK 下载页面为您的应用显示的版本或生成时间戳。
# 权限范围和授权检查
SDK 更新不会自动授予新的 API 权限。
如果更新包含新的权限范围或 API：

* 确认应用在 Partner Center 中具有所需的 API 访问权限范围。
* 如果需要新的卖家权限，请根据需要要求卖家授权或重新授权应用。
* 确认重新生成的 SDK 包含您期望的 API 方法。
* 在将更新的 SDK 用于生产之前，使用开发店铺或 sandbox 流程进行测试。

# 相关链接
| 链接 | 用途 |
| --- | --- |
| [下载 SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) | 从 SDK 下载页面下载 SDK 包。 |
| [API 版本管理](https://partner.tiktokshop.com/docv2/page/api-versioning) | 了解 API 版本命名、版本选择和退役行为。 |
| [更新日志](https://partner.tiktokshop.com/docv2/changelog) | 跟踪 API 变更、破坏性变更和退役通知。 |
| [TTS API 概述](https://partner.tiktokshop.com/docv2/page/overview) | 返回 API 概述和导航。 |

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/d650c57863e9440c86355e51dc41ca19~tplv-k9wyc2ijk0-image.image" width="1280px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/95dc1a7287ae4ef6bb4471ac1877ee59~tplv-k9wyc2ijk0-image.image" width="1082px" /></div>

