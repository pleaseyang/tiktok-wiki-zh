# 常见错误

在发送 API 请求时，确保正确的结构和格式是与 TikTok Shop 服务器顺畅通信的关键。本主题涵盖与 **请求 query**、**header** 和 **body 格式** 相关的常见网关和跨域错误。这些基础错误在业务逻辑处理之前发生，必须解决后才能成功处理请求。
**注意：** 响应 code 中的 `0` 表示请求已成功处理。
**业务错误码：** 本页未详尽列出特定 endpoint 的业务错误。对于业务逻辑失败，请打开相应的 endpoint reference 页面，查看该页面底部的 **Errorcode** 部分。有关完整的 API reference 入口，请参阅 [TTS API reference docs](https://partner.tiktokshop.com/docv2/page/create-product)。
**建议的故障排除路径：**

1. 首先确认 HTTP 状态码，特别是 `401`、`403`、`404`、`408`、`429` 和 `5xx`。
2. 同时检查 API 响应的 `code` 和 `message`。一些常见的请求验证失败会重复使用相同的数字 code。
3. 如果失败是特定于 endpoint 的，请查看 endpoint reference 页面的 **Errorcode** 部分。
4. 如果失败与授权相关，请将 endpoint 所需的 scope 与 Partner Center 中应用的 scope 以及 token 的 `granted_scopes` 字段进行比较。

# `36009004` 的消息关键词索引
code `36009004` 被用于多种不同的请求验证失败。不要仅使用数字 code 进行程序化分支处理。请结合响应 `message` 关键词使用，并记录包含 `request_id` 的完整响应。
| **消息关键词** | **可能的含义** | **需要检查的内容** |
| --- | --- | --- |
| `Missing credentials`、`signature` | 缺少必需的 `sign` query 参数。 | 参考 Sign your API request 生成有效的签名。 |
| `access_token header is invalid` | `access_token` header 无效。 | 传入从 Get Access Token 获取的 access token。 |
| `x-tts-access-token header is invalid` | `x-tts-access-token` header 无效。 | 传入从 Get Access Token 获取的 access token，并确认该 token 属于正确的授权主体。 |
| `Invalid app_key` | `app_key` query 参数无效、已禁用、已删除或无法解析。 | 在 **Partner Center** 的 **App details** 页面检查 app key。 |
| `timestamp`、`lesser than 0` | `timestamp` query 参数为负数。 | 使用在可接受时间窗口内的 Unix 时间戳。 |
| `timestamp`、`earlier than 5 minutes` | 时间戳过于陈旧。 | 将时间戳保持在当前时间之前 5 分钟以内。 |
| `timestamp`、`more than 30 seconds` | 时间戳过于超前。 | 将时间戳保持在当前时间之后不超过 30 秒。 |
| `shop_cipher`、`not required` | 请求包含了不必要的 `shop_cipher`。 | 移除 `shop_cipher` 并检查 endpoint 所需的标识符。 |
| `category_asset_cipher`、`not required` | 请求包含了不必要的 `category_asset_cipher`。 | 移除 `category_asset_cipher` 并检查 endpoint 所需的标识符。 |
| `shop_id`、`invalid` | `shop_id` query 参数无效。 | 从 Get Authorized Shops 获取正确的店铺标识符。 |
| `Invalid API version` | API 版本无效或不受支持。 | 请参阅 **Parameter errors** 中的版本说明。API versioning 指南可能使用 `36009014`，而旧版/常见网关响应可能仍显示 `36009004`；请验证所调用的 endpoint/版本的实际响应。 |
# 通用错误
| **Code** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情和指导** |
| --- | --- | --- |
| 36009002 | Too many requests. You've made too many requests in a short period of time. | 将此视为速率限制条件。HTTP 响应应与业务 code 一起处理：`HTTP 429` 和 `36009002` 都表示速率限制。应用重试/退避逻辑，如果存在则遵循 `Retry-After`，详情请参阅 Rate limits。 |
| 36009007 | Request timeout. The request to the endpoint timed out. | 请重试，或考虑将其拆分为更小的请求。 |
| 36009009 | Invalid path. The specified path does not match any available endpoint. | 详情请参阅 API 文档。 |
| 36009010 | Invalid method. The HTTP method used is not supported by this endpoint. | 详情请参阅 API 文档。 |
| 36009021 | Invalid file size. The uploaded file size exceeds the maximum limit. | 详情请参阅 API 文档。 |
| 36009022 | Invalid request format. The request body format must be `application/json` for structured data or `multipart/form-data` for binary files. | 详情请参阅 API 文档。 |
| 36009023 | Invalid request format. The value of the `content-type` header must be `multipart/form-data`. | 详情请参阅 API 文档。 |
# 授权错误
| **Code** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情和指导** |
| --- | --- | --- |
| **105005** | **Access denied. The app is not authorized to access the endpoint because the access scopes granted for the app or the access token do not contain the required access scope for the endpoint.** | **最常见的 access-scope 失败。当 API 调用因"Access denied"失败，或在应用设置后来自 Developer Tool / API Testing Tool 的调用失败时，请首先检查此项。** <br/>  <br/> 建议检查：  <br/> 1. 在 **Partner Center** > **App & Service** > **Manage API** 中检查应用的已授权 scope。如果缺少所需的 scope，请在 Partner Center 中申请或启用它。  <br/> 2. 在 Get Access Token 响应的 `granted_scopes` 字段中检查 token 的已授权 scope。如果缺少所需的 scope，请请求用户重新授权所需的 scope，然后相应地生成新 token。 |
| 101000 | Invalid query or header. The `category_asset_cipher` query parameter or `x-tts-access-token` header is invalid. | 对于 `category_asset_cipher`，请确保从 Get Authorized Category Assets endpoint 获取正确的值。  <br/>  <br/> 对于 `x-tts-access-token`，可能的原因包括：  <br/> - 该 token 对此 endpoint 具有无效的 `user_type`。请参阅 Generate a test access token 中的 `user_type` 值定义，并检查 API entity tags 中 endpoint 的 entity tag，以确认它期望的是 seller、creator、partner、shop 还是 asset-level token。  <br/> - 该 token 未关联到店铺，或关联的店铺与提供的 `shop_cipher` query 参数不匹配。  <br/>  <br/> 详情请参阅授权指南。 |
| 36009033 | Access denied. Your IP address is not in the IP allow list configured for this app. | 在 **Partner Center** > **App & Service** 中添加你的 IP 地址。 |
# 认证错误
| **Code** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情和指导** |
| --- | --- | --- |
| 105002 | Expired credentials. The `access_token` or `x-tts-access-token` header has expired. | 通过使用 Get Refresh Token endpoint 刷新你的 token。 |
| 106001 | Invalid credentials. The `sign` query parameter is invalid. | 确保通过参考签名请求指南生成有效的签名。 |
| 36009004 | Missing credentials. The request does not include a required signature in the query. | 通过参考签名请求指南生成签名。 |
| 36009004 | Invalid credentials. The `access_token` header is invalid. | 请传入从 Get Access Token endpoint 获取的 `access_token`。 |
| 36009004 | Invalid credentials. The `x-tts-access-token` header is invalid. | 请传入从 Get Access Token endpoint 获取的 `access_token`。 |
| 36009004 | Invalid credentials. Invalid `app_key` query parameter. | 可能的原因包括 key 格式无效、应用未找到、应用已禁用或删除，或获取所需授权时出错。确保从 **Partner Center** 的 **App details** 页面获取正确的值。 |
| 36009004 | Invalid timestamp. The value of the `timestamp` query parameter must not be lesser than 0. | 时间戳必须在当前时间之前 5 分钟到之后 30 秒的范围内。 |
| 36009004 | Invalid timestamp. The value of the `timestamp` query parameter must not be earlier than 5 minutes before the current time. | 时间戳必须在当前时间之前 5 分钟到之后 30 秒的范围内。 |
| 36009004 | Invalid timestamp. The value of the `timestamp` query parameter must not exceed the current time by more than 30 seconds. | 时间戳必须在当前时间之前 5 分钟到之后 30 秒的范围内。 |
# 参数错误
| **Code** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情和指导** |
| --- | --- | --- |
| 106013 | Missing identifier. The `shop_cipher` query parameter is required to identify the target shop. | 从 Get Authorized Shops endpoint 获取此值。 |
| 36009004 | Unexpected identifier. The `shop_cipher` query parameter is not required for this request. | 移除它并重试。详情请参阅 API 文档中关于所需标识符的说明。 |
| 36009004 | Unexpected identifier. The `category_asset_cipher` query parameter is not required for this request. | 移除它并重试。详情请参阅 API 文档中关于所需标识符的说明。 |
| 36009004 | Invalid identifier. The `shop_id` query parameter is invalid. | 从 Get Authorized Shops endpoint 获取正确的值。 |
| 36009014 / 36009004 | Invalid API version. The `version` value is invalid or unsupported. | API versioning 主题使用 `36009014` 标识无效的 API 版本，而旧版/常见网关示例可能显示 `36009004` 和相同的 `Invalid API version` 消息。在所有文档和运行时响应对齐之前，通过同时检查 code 和 `Invalid API version` 消息关键词来处理此情况，并验证你正在调用的 endpoint/版本的实际响应。请参阅 TTS API versioning 和 endpoint reference 页面获取有效版本。 |
| 36004004 | Invalid auth code. | `auth_code` 已被使用、已过期或无效。 |
