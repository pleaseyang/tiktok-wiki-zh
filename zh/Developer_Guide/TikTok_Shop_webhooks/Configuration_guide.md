# 配置指南

Webhook 在已订阅的 TikTok Shop 事件发生时通知你的 HTTPS 端点。你可以在 Partner Center 控制台或通过 Events API 配置 Webhook 订阅。
# Webhook 配置概述
支持两种配置方式：
| 方式 | 适用场景 | 管理位置 |
| --- | --- | --- |
| Partner Center 控制台 | 手动设置、首次设置以及可视化确认 Webhook URL 和已选主题。 | **Partner Center 控制台 > 应用与服务 > 选择你的应用或服务 > 基本信息 > 开发中** |
| Events API | 编程式的店铺级 Webhook 配置、自动化配置或跨店铺配置同步。 | `PUT /event/202309/webhooks`、`GET /event/202309/webhooks` 和 `DELETE /event/202309/webhooks` |

每个应用或店铺请使用一个运维来源作为真实来源。Partner Center 和 Events API 管理的是同一个 Webhook 配置界面；在一个地方所做的更改可能会影响你在另一个地方看到的内容。
# 前提条件
在配置 Webhook 之前，请确保：

* 你了解 Webhook 事件模型和 payload 格式。参见 [Webhook 概述](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview)。
* 你的应用拥有要订阅的事件所需的 API 权限范围和主题权限。
* 你的接收服务暴露一个可访问的 HTTPS 端点，并满足以下 Webhook URL 要求。
* 如果你使用 Events API，你能够发送签名的 TikTok Shop API 请求，并在端点需要时提供有效的 `x-tts-access-token`。参见 [签名你的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。

# Webhook URL 要求
| 要求 | 详情 |
| --- | --- |
| 协议 | 使用 `https://`。 |
| TLS | 支持 TLS v1.2 或更高版本。 |
| 主机 | 使用域名。不要使用 IP 地址。 |
| 端口 | 不要在 Webhook URL 中包含自定义端口。 |
| 成功确认 | 在通知被接受时 3 秒内返回 HTTP `200`。 |
| 认证失败 | 仅在你的服务拒绝 Webhook 签名或认证时返回 HTTP `401`。`401` 不是成功的投递确认。 |
# 方式一：在 Partner Center 控制台配置 Webhook
使用以下路径进行 Webhook URL 和主题配置：
```Plain Text
Partner Center 控制台
  -> 应用与服务
  -> 选择你的应用或服务
  -> 基本信息
  -> 开发中
  -> Webhook URL / 事件订阅
```

**开发工具包 > Webhook 日志** 仅在你想查看投递历史时使用。它是监控入口，不是 Webhook 配置入口。
# 第 1 步：配置 Webhook URL
在 **基本信息** 下的 **开发中** 部分添加你的 HTTPS Webhook 接收 URL。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/84d2e7f5f4a94851b923a1308308aabc~tplv-k9wyc2ijk0-image.image)
截图参考：Webhook URL 字段位于应用或服务配置区域，而非 **开发工具包** 中。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5ab7fe180c1041f3ac0726950f072196~tplv-k9wyc2ijk0-image.image)

# 第 2 步：选择 Webhook 主题
Partner Center 可能会为你的应用预选默认的 Webhook 通知。确切的默认集合可能因应用类型、市场、卖家类型和已批准的权限范围而异，因此请在上线前在 Partner Center 订阅 UI 中确认已选的默认主题。
对于可选主题，仅选择你的集成实际处理的事件。常见的 Webhook 类别包括：
| 主题类别 | 示例使用场景 | 何时订阅 |
| --- | --- | --- |
| 订单状态更新 | 当订单创建或订单状态变更时接收通知。 | 你的应用需要同步订单、履约状态或订单生命周期变更。 |
| 订单收件人地址更新 | 当订单收件人地址信息变更时接收通知。 | 你的应用需要在地址变更后更新物流、仓库或履约数据。 |
| 退货、退款或换货更新 | 当退货、退款或换货状态变更时接收通知。 | 你的应用管理售后工作流程。 |
| 商品状态更新 | 当商品状态变更时接收通知。 | 你的应用需要同步商品上架状态或上架健康度。 |
| 包裹或履约更新 | 当你的应用和市场支持时，接收包裹相关的状态变更。 | 你的应用管理履约、发货或配送工作流程。 |
| 授权生命周期事件 | 支持时接收 `UPCOMING_AUTHORIZATION_EXPIRATION` 或 `SELLER_DEAUTHORIZATION`。 | 你的应用存储卖家授权 token，需要维护或停止店铺访问。 |

完整且最新的事件列表，请使用 [Webhook 概述](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview) 中的事件列表以及从该概述链接的事件特定参考页面。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/796b668db0b44dc196622dab013fc56d~tplv-k9wyc2ijk0-image.image)
截图参考：使用此区域确认哪些主题是默认选中的，以及你启用了哪些可选主题。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/7e97002885864b27921395d63794ea6e~tplv-k9wyc2ijk0-image.image)

# 第 3 步：接收和验证 Webhook 通知
当已订阅的事件发生时，TikTok Shop 向你配置的 URL 发送 HTTP `POST` 请求。请求体包含该事件的 JSON 数据。
TikTok Shop 在向 HTTPS Webhook 地址投递 payload 时会验证 SSL 证书。请确保你的服务器证书有效且受信任。
TikTok Shop 将 Webhook 签名放在 `Authorization` 请求头中。此 Webhook 签名与你的应用调用 TikTok Shop API 时生成的签名不同。对于 Webhook 验证：

1. 按接收时的原始内容读取请求体。
2. 将 `{app_key}{raw_webhook_payload}` 拼接在一起，不添加任何空格或重新格式化。
3. 使用你的 app secret 作为 HMAC-SHA256 密钥。
4. 将生成的小写十六进制值与 `Authorization` 请求头的值进行比较。

不要在验证之前解析并重新序列化 JSON 请求体。重新格式化请求体可能会改变空格或字段顺序，导致签名验证失败。有关 Webhook 签名示例，请参见 [Webhook 概述](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview) 中的 **Webhook 请求头和 Body** 部分。
# 第 4 步：响应 Webhook 通知
每个通知请在 3 秒内返回响应。
| 情况 | HTTP 状态码 | 响应体 | 含义 | 重试行为 |
| --- | --- | --- | --- | --- |
| 通知已接受并排队或处理 | `200` | 空响应体 | 成功的投递确认。 | TikTok Shop 将通知视为已投递。 |
| 签名或认证失败 | `401` | 空响应体 | 你的服务拒绝了通知。这是认证失败的有效语义响应，但不是成功确认。 | 视为投递失败。TikTok Shop 可能按照重试计划进行重试。 |
| 超时、网络故障或其他非 200 响应 | 非 `200` 或无响应 | 任意 | 投递失败或未在规定时间内确认。 | TikTok Shop 按照重试计划进行重试。 |

TikTok Shop 在第 4 次重试失败后停止重试。
| 重试 | 触发条件 |
| --- | --- |
| 第 1 次重试 | 初始投递失败后 2 分钟 |
| 第 2 次重试 | 第 1 次重试失败后 30 分钟 |
| 第 3 次重试 | 第 2 次重试失败后 3 小时 |
| 第 4 次重试 | 第 3 次重试失败后 12 小时 |

Webhook 投递为至少一次投递。你的监听器必须是幂等的，因为同一事件在重试期间可能被投递多次。当 payload 中存在 `tts_notification_id` 时，请存储并基于其进行去重。如果事件特定的 payload 不包含 `tts_notification_id`，请使用最稳定的可用组合，例如事件类型、`shop_id`、时间戳和业务对象 ID。
# 方式二：通过 Events API 配置 Webhook
当你需要以编程方式创建、查看或删除 Webhook 订阅时，请使用 Events API。
在调用这些 API 之前：
| 前提条件 | 检查内容 |
| --- | --- |
| API 访问权限 | 你的应用必须拥有对 Events API 和你正在配置的事件主题的访问权限。请检查端点参考以及 **应用与服务 > 管理 API** 中所需的权限范围或许可。 |
| 卖家/店铺授权 | 当端点需要卖家范围的授权时，使用有效的 `x-tts-access-token`。 |
| 请求签名 | 包含所需的 OpenAPI 查询参数，例如 `app_key`、`timestamp` 和 `sign`。按照 TikTok Shop API 请求签名规则生成 `sign`。 |
| 店铺上下文 | 当端点或店铺类型需要店铺级上下文时，包含 `shop_cipher`。 |
| 主题值 | 使用事件特定参考页面中的确切 `event_type` 值。 |

Events API 配置与 Partner Center 配置并不互斥。它们更新的是同一个底层订阅配置。如果你对通过手动配置的店铺和事件调用 **Update Shop Webhook**，该 API 可以更新或替换该店铺-事件的配置。在任何 API 更改之后，请调用 **Get Shop Webhooks** 或检查 Partner Center 以确认最终状态。
可用的 Events API 操作：
| API | 用途 |
| --- | --- |
| [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) | 为特定事件创建或更新店铺 Webhook 订阅。这对应于在 Partner Center 中设置回调 URL 和选定主题。 |
| [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) | 获取现有的店铺 Webhook 配置，验证当前的回调 URL 和事件订阅。 |
| [Delete Shop Webhook](https://partner.tiktokshop.com/docv2/page/delete-shop-webhook) | 取消特定事件的店铺 Webhook 订阅。仅在你想有意停止接收该事件时使用。 |
# 查看 Webhook 事件历史
使用以下路径查看 Webhook 投递日志：
```Plain Text
Partner Center 控制台
  -> 开发工具包
  -> Webhook 日志
  -> 选择应用或服务
```

Webhook 日志用于监控和调试投递历史。用它来确认 TikTok Shop 是否发送了通知、使用了哪个回调 URL 以及你的服务器返回了什么响应。
截图参考：此截图显示 **开发工具包** 下的日志和调试入口，与 **应用与服务 > 开发中** 下的应用配置入口是分开的。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5a30e72db1614b4ea89547aac013dc70~tplv-k9wyc2ijk0-image.image)

# 相关页面
| 页面 | 用途 |
| --- | --- |
| [Webhook 概述](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview) | Webhook 概念、事件列表、payload 格式和 Webhook 签名验证示例。 |
| [签名你的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | 签名你的应用发出的 TikTok Shop API 请求，包括 Events API 请求。不要将此算法用作 Webhook 接收端验证算法。 |
| [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) | 通过 API 创建或更新店铺 Webhook 订阅。 |
| [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) | 通过 API 验证当前店铺 Webhook 配置。 |
| [Delete Shop Webhook](https://partner.tiktokshop.com/docv2/page/delete-shop-webhook) | 通过 API 删除店铺 Webhook 订阅。 |
