# 概述

# Widget 概述
TikTok Shop Widget 是通过 Widget SDK 提供的前端组件。Widget 将 TikTok Shop 托管的用户界面和平台能力与特定的卖家工作流程相结合，例如仓库设置、运费模板配置、商品优化或订单履约。
Widget 并不替代 TikTok Shop Open API。当你希望在应用中嵌入由 TikTok Shop 管理的 UI，同时仍将授权、token 交换和集成控制保留在自己的后端时，Widget 非常有用。
# API 与 Widget 对比
| 方面 | TikTok Shop Open API | TikTok Shop Widget |
| --- | --- | --- |
| 集成模式 | 后端到后端的 REST API 集成。 | 前端 SDK 集成，使用 TikTok Shop 托管的 UI。 |
| UI 归属 | 你在自己的应用中设计和维护面向卖家的 UI。 | TikTok Shop 为支持的工作流程提供 Widget UI。 |
| 后端工作量 | 需要处理 API 签名、access token 存储、重试机制、数据映射和错误处理。 | 仍需处理授权、access token 存储、widget token 生成和后端安全。 |
| 前端工作量 | 可选，取决于你自己的产品 UI。 | 必需。你的前端需要初始化 SDK、加载 Widget 并传入 `getToken` 回调。 |
| 灵活性 | 灵活性最高，因为你拥有完整的用户体验。 | 对于支持的场景集成更快，但 Widget UI 本身不可自定义。 |
| 适用场景 | 完全自定义的工作流程、后端自动化和数据同步。 | 以较低 UI 开发成本嵌入受支持的 TikTok Shop 工作流程。 |

来源指南中的视觉参考：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e843fec729141ff9c2bcd062983cd38~tplv-k9wyc2ijk0-image.image)
# 优势
Widget 可以帮助开发者：

* 减少受支持卖家工作流程的前端开发工作量；
* 在第三方应用内提供与 TikTok Shop 一致的工作流程体验；
* 减少因缺少卖家端设置（如仓库或运费模板配置）而导致的错误；
* 让卖家无需切换回 Seller Center 即可完成指定的运营步骤。

# 集成流程
集成 Widget 时请使用以下流程：
| 步骤 | 操作内容 | 主要入口或负责方 |
| --- | --- | --- |
| 1. 浏览 Widget | 查看可用的 Widget 选项，并阅读每个 Widget 的详情页面。 | **Partner Center 控制台 > 开发工具包 > Widget** |
| 2. 确认可用性 | 确认该 Widget 支持你的应用类型、卖家市场、卖家类型和使用场景。 | Widget 详情页和 Partner Center UI |
| 3. 配置 Widget | 选择应用并配置 Widget 设置。 | **开发工具包 > Widget > 配置**，或应用详情页 |
| 4. 域名白名单 | 添加 Widget 将被嵌入的前端根域名。 | Widget 配置页面 |
| 5. 构建 token 流程 | 在后端使用卖家 `access_token` 调用 Get Widget Token，然后将短期有效的 widget token 返回给前端。 | 你的后端和 [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) |
| 6. 初始化 SDK | 将 Widget 配置和 `getToken` 回调传入 Widget SDK。 | [Widget SDK 使用指南](https://partner.tiktokshop.com/docv2/page/widget-sdk-user-guide) |
| 7. 测试和上线 | 在发布前使用正确的 app key、shop、market、domain 和 widget name 测试 Widget。 | Partner Center、你的预发布环境以及必要时联系技术支持 |

来源指南中的视觉参考：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a1a917b63a1c400da3def8a0cd80f376~tplv-k9wyc2ijk0-image.image)
# Token 流程
前端不得直接调用 TikTok Shop Open API。请使用以下 token 链路：
| 步骤 | Token 或调用 | 说明 |
| --- | --- | --- |
| 1 | 卖家授权 | 卖家授权你的应用，你的后端获取卖家 `access_token`。 |
| 2 | `GET /authorization/202401/widget_token` | 你的后端使用 `x-tts-access-token` 请求头中的卖家 `access_token` 调用 Get Widget Token。 |
| 3 | `widget_token` | TikTok Shop 返回一个短期有效的 widget token，通常有效期约为 5 分钟。 |
| 4 | SDK `getToken` 回调 | 你的前端调用你的后端 token 接口，并将 `{ token, expire_at }` 返回给 Widget SDK。 |

请将 App Secret、签名逻辑和卖家 `access_token` 保留在你的后端。只有短期有效的 widget token 才应传递给前端 SDK。
# 开始之前
在集成 Widget 之前，请确认：

* 应用已在 Partner Center 中创建；
* 卖家已授权该应用，且应用拥有所需的权限范围；
* Widget 已为你的应用和使用场景启用或可用；
* 你的前端域名已准备好进行 Widget 白名单配置；
* 你的后端能够生成签名的 TikTok Shop Open API 请求；
* 你的前端能够安装并初始化 Widget SDK 包。

# 第 1 步：浏览 Widget 选项
使用 **Partner Center 控制台 > 开发工具包 > Widget** 浏览可用的 Widget。如果较早的截图使用 **Development kits > Widget**，请将其视为 **开发工具包** 下的同一个 Widget 入口。
对于每个 Widget，点击 **了解更多** 或打开 Widget 详情页，查看最新的说明、前提条件、市场可用性和集成指南。
| 截图 | 展示内容 | 使用方式 |
| --- | --- | --- |
| Widget 标签页入口 | **开发工具包 > Widget** 标签页，列出可用的 Widget。 | 打开此页面浏览 Widget 选项并比较使用场景。 |
| Widget 详情入口 | 带有了解更多操作的 Widget 卡片或详情入口。 | 点击详情入口查看 Widget 前提条件和集成说明。 |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2d7fb32d36704133bc10cf9a9946f613~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/765bcb50a6754ec4909bf353232d21ab~tplv-k9wyc2ijk0-image.image)
# 第 2 步：配置 Widget 设置
在 **开发工具包 > Widget** 中，检查应用列表以及每个应用是否启用了 Widget 设置。点击目标应用的 **配置** 打开应用详情或 Widget 配置页面。
你也可以在创建或编辑应用时从应用详情页开始 Widget 预配置。
| 截图 | 展示内容 | 使用方式 |
| --- | --- | --- |
| 应用列表和 Widget 状态 | 应用列表以及每个应用是否启用了 Widget。 | 选择目标应用并点击 **配置**。 |
| 配置操作 | Widget 设置的配置按钮或入口。 | 使用此按钮跳转到应用详情或 Widget 配置页面。 |
| 应用详情 Widget 设置 | 应用详情页上的 Widget 预设置配置。 | 在创建或编辑应用并需要配置 Widget 选项时使用。 |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8943ab9293824232bf4252c8c5f1fc61~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e0becb76e1e54345b42494d3a75ff8af~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/913e5f9d2e924d76b6838867538342f1~tplv-k9wyc2ijk0-image.image)
# 第 3 步：配置域名白名单
添加你的应用将嵌入 Widget 的前端根域名。
规则：

* 使用你自己的生产或预发布前端域名。不要使用示例中的占位符域名。
* 包含协议和主机名，例如 `https://app.example.com`。
* 不要包含路径，例如 `/settings/widgets`。
* 配置所有将加载 Widget 的前端根域名。
* 来源指南说明最多可添加 10 个 URL。如果 Partner Center 显示不同的限制，请以实际 UI 为准。

| 截图 | 展示内容 | 使用方式 |
| --- | --- | --- |
| 域名白名单页面 | Widget 域名 URL 配置。 | 添加将托管 Widget 的前端根域名并保存配置。 |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/0304ca539d2248868f29b3ba558f4899~tplv-k9wyc2ijk0-image.image)
# 第 4 步：集成和测试
Widget 配置完成后：

1. 按照 Widget 特定的集成指南操作。
2. 安装 Widget SDK 包。
3. 实现一个后端 token 接口，调用 [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token)。
4. 使用 app key、shop ID、卖家地区、widget name 和 `getToken` 初始化 SDK。
5. 在域名已加入白名单的预发布环境中进行测试。
6. 确认浏览器错误不是由域名不匹配、widget token 过期、app key 不匹配、shop 不匹配或地区不匹配引起的。

# Widget 使用场景
Widget 的可用性可能因市场、应用类型、卖家类型和 TikTok Shop 启用状态而异。不要依赖复制的市场列表（如"美国"或"美国和英国"）作为真实来源。请在 **开发工具包 > Widget**、Widget 详情页或为你的应用提供的集成材料中确认当前的市场可用性。
| Widget | 使用场景 | 市场可用性 | 集成指南 |
| --- | --- | --- | --- |
| 仓库 Widget | 让卖家输入或更新发货仓库和退货仓库信息，包括联系人、地址和销售范围。这可以减少因缺少仓库设置而导致的商品上架失败。 | 请在 Partner Center 确认。 | [仓库 Widget 指南](https://partner.tiktokshop.com/docv2/page/66599ca675ead002e4e0c3fb) |
| 运费模板 Widget | 让卖家设置卖家自配送商品所需的运费模板，尤其适用于 3PL 工作流程。 | 请在 Partner Center 确认。 | [运费模板 Widget 指南](https://partner.tiktokshop.com/docv2/page/66599c6d36f34802de23344e) |
| 商品优化 Widget | 在商品同步后提供改善商品信息质量和商品表现的推荐。 | 请在 Partner Center 确认。 | [商品优化 Widget 指南](https://partner.tiktokshop.com/docv2/page/66599c4236f34802de23338d) |
| TikTok Shipping 订单 Widget | 帮助使用 TikTok Shipping 的卖家处理订单、创建标签、打印标签以及从第三方应用处理发货。 | 请在 Partner Center 确认。 | [TikTok Shipping 订单 Widget 指南](https://partner.tiktokshop.com/docv2/page/665999a9e5764002e59be4e2) |
# Widget 演示截图
以下截图保留自来源指南作为视觉示例。请使用实际的 Widget 详情页确认当前 UI 和支持的市场。
| Widget | 截图 |
| --- | --- |
| 仓库 Widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/7407a25b6dec45318669705c9fe1e659~tplv-k9wyc2ijk0-image.image) |
| 运费模板 Widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/280f49b7ef964c38b41f83fe8e45aa0e~tplv-k9wyc2ijk0-image.image) |
| 商品优化 Widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8fded8be498840c39c90597662675a41~tplv-k9wyc2ijk0-image.image) <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fd90ebe76bc04eda9b7695eb71e3e431~tplv-k9wyc2ijk0-image.image) |
| TikTok Shipping 订单 Widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/331c80590868472d9ebf9ef49eff392c~tplv-k9wyc2ijk0-image.image) |
# 相关页面
| 页面 | 用途 |
| --- | --- |
| [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) | 后端将卖家 `access_token` 交换为短期有效的 `widget_token`。 |
| [Widget SDK 使用指南](https://partner.tiktokshop.com/docv2/page/widget-sdk-user-guide) | 前端 SDK 安装、初始化、`getToken` 和 Widget 问题排查。 |
| [授权指南](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) | 卖家授权和 access token 流程。 |
