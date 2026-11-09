# 通用错误码

发起 API 请求时，请求结构与格式是否正确，是与 TikTok Shop 服务端正常通信的前提。本文汇总与 **请求查询参数**、**请求头**、**请求体格式** 相关的常见网关层与跨域错误。这类基础错误发生在业务逻辑处理之前，必须先解决，请求才能被成功处理。
**说明：** 响应码 `0` 表示请求已成功处理。
**业务错误码：** 本文不逐一列出各端点专属的业务错误。若属业务逻辑失败，请打开对应端点参考页，查看页面底部的 **Errorcode** 章节。完整 API 参考入口见 [TTS API reference docs](https://partner.tiktokshop.com/docv2/page/create-product)。
**推荐排查路径：**

1. 先确认 HTTP 状态码，重点关注 `401`、`403`、`404`、`408`、`429` 和 `5xx`。
2. 同时检查 API 响应中的 `code` 与 `message`。部分常见的请求校验失败会复用同一个数字错误码。
3. 若失败与具体端点相关，请查看该端点参考页的 **Errorcode** 章节。
4. 若失败与授权相关，请把端点要求的权限范围（scope）与合作伙伴中心中应用已开通的范围、以及令牌的 `granted_scopes` 字段逐一比对。

# `36009004` 的消息关键字索引
错误码 `36009004` 被多种不同的请求校验失败复用。请勿仅凭数字错误码做程序化分支判断，需结合响应 `message` 中的关键字，并记录包含 `request_id` 的完整响应。
| **消息关键字** | **可能含义** | **排查建议** |
| --- | --- | --- |
| `Missing credentials`, `signature` | 缺少必填的 `sign` 查询参数。 | 参考「为 API 请求签名」生成有效签名。 |
| `access_token header is invalid` | `access_token` 请求头无效。 | 传入通过 Get Access Token 获取的访问令牌。 |
| `x-tts-access-token header is invalid` | `x-tts-access-token` 请求头无效。 | 传入通过 Get Access Token 获取的访问令牌，并确认该令牌属于正确的授权主体。 |
| `Invalid app_key` | `app_key` 查询参数无效、已停用、已删除或无法解析。 | 在 **合作伙伴中心** 的 **App details** 页面核对应用密钥。 |
| `timestamp`, `lesser than 0` | `timestamp` 查询参数为负数。 | 使用落在允许时间窗口内的 Unix 时间戳。 |
| `timestamp`, `earlier than 5 minutes` | 时间戳过早。 | 时间戳不得早于当前时间 5 分钟以上。 |
| `timestamp`, `more than 30 seconds` | 时间戳过于超前。 | 时间戳最多比当前时间超前 30 秒。 |
| `shop_cipher`, `not required` | 请求中携带了多余的 `shop_cipher`。 | 移除 `shop_cipher`，并核对该端点实际要求的标识符。 |
| `category_asset_cipher`, `not required` | 请求中携带了多余的 `category_asset_cipher`。 | 移除 `category_asset_cipher`，并核对该端点实际要求的标识符。 |
| `shop_id`, `invalid` | `shop_id` 查询参数无效。 | 通过 Get Authorized Shops 获取正确的店铺标识符。 |
| `Invalid API version` | API 版本无效或不受支持。 | 参见 **参数错误** 中的版本说明。API 版本管理指南可能使用 `36009014`，而旧版或通用网关响应仍可能返回 `36009004`；请以所调用端点与版本的实际响应为准。 |
# 通用错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与处理建议** |
| --- | --- | --- |
| 36009002 | Too many requests. You've made too many requests in a short period of time. | 按限流处理。HTTP 响应需与业务错误码结合判断：`HTTP 429` 与 `36009002` 都表示触发限流。请加入重试/退避逻辑，若存在 `Retry-After` 响应头则遵循该值，并参考 Rate limits 说明。 |
| 36009007 | Request timeout. The request to the endpoint timed out. | 请重试，或考虑拆分为更小的请求。 |
| 36009009 | Invalid path. The specified path does not match any available endpoint. | 详见 API 文档。 |
| 36009010 | Invalid method. The HTTP method used is not supported by this endpoint. | 详见 API 文档。 |
| 36009021 | Invalid file size. The uploaded file size exceeds the maximum limit. | 详见 API 文档。 |
| 36009022 | Invalid request format. The request body format must be `application/json` for structured data or `multipart/form-data` for binary files. | 详见 API 文档。 |
| 36009023 | Invalid request format. The value of the `content-type` header must be `multipart/form-data`. | 详见 API 文档。 |
# 授权错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与处理建议** |
| --- | --- | --- |
| **105005** | **Access denied. The app is not authorized to access the endpoint because the access scopes granted for the app or the access token do not contain the required access scope for the endpoint.** | **最常见的权限范围失败。当 API 调用返回「Access denied」，或在应用配置完成后 Developer Tool / API Testing Tool 调用失败时，应优先排查此项。** <br/>  <br/>  建议检查：  <br/>  1. 在 **合作伙伴中心** > **App & Service** > **Manage API** 中查看应用已开通的权限范围；若缺少所需范围，请在合作伙伴中心申请或启用。  <br/>  2. 查看 Get Access Token 响应中的 `granted_scopes` 字段，确认令牌已获得的权限范围；若缺少所需范围，请让用户重新授权该范围，再重新生成令牌。 |
| 101000 | Invalid query or header. The `category_asset_cipher` query parameter or `x-tts-access-token` header is invalid. | 对于 `category_asset_cipher`，请确认取值来自 Get Authorized Category Assets 端点。  <br/>  <br/>  对于 `x-tts-access-token`，可能原因包括：  <br/>  - 该令牌的 `user_type` 不适用于此端点。参见 Generate a test access token 中的 `user_type` 取值定义，并通过 API entity tags 中该端点的实体标签确认其要求的是卖家、达人、合作伙伴、店铺还是资产级令牌。  <br/>  - 令牌未关联店铺，或所关联店铺与传入的 `shop_cipher` 查询参数不匹配。  <br/>  <br/>  详见授权指南。 |
| 36009033 | Access denied. Your IP address is not in the IP allow list configured for this app. | 在 **合作伙伴中心** > **App & Service** 中添加你的 IP 地址。 |
# 认证错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与处理建议** |
| --- | --- | --- |
| 105002 | Expired credentials. The `access_token` or `x-tts-access-token` header has expired. | 通过 Get Refresh Token 端点刷新令牌。 |
| 106001 | Invalid credentials. The `sign` query parameter is invalid. | 请参照请求签名指南生成有效签名。 |
| 36009004 | Missing credentials. The request does not include a required signature in the query. | 请参照请求签名指南生成签名。 |
| 36009004 | Invalid credentials. The `access_token` header is invalid. | 请传入通过 Get Access Token 端点获取的 `access_token`。 |
| 36009004 | Invalid credentials. The `x-tts-access-token` header is invalid. | 请传入通过 Get Access Token 端点获取的 `access_token`。 |
| 36009004 | Invalid credentials. Invalid `app_key` query parameter. | 可能原因包括：密钥格式无效、应用不存在、应用已停用或已删除，或获取所需授权时出错。请确认取值来自 **合作伙伴中心** 的 **App details** 页面。 |
| 36009004 | Invalid timestamp. The value of the `timestamp` query parameter must not be lesser than 0. | 时间戳必须在「当前时间前 5 分钟」到「当前时间后 30 秒」的范围内。 |
| 36009004 | Invalid timestamp. The value of the `timestamp` query parameter must not be earlier than 5 minutes before the current time. | 时间戳必须在「当前时间前 5 分钟」到「当前时间后 30 秒」的范围内。 |
| 36009004 | Invalid timestamp. The value of the `timestamp` query parameter must not exceed the current time by more than 30 seconds. | 时间戳必须在「当前时间前 5 分钟」到「当前时间后 30 秒」的范围内。 |
# 参数错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与处理建议** |
| --- | --- | --- |
| 106013 | Missing identifier. The `shop_cipher` query parameter is required to identify the target shop. | 通过 Get Authorized Shops 端点获取该值。 |
| 36009004 | Unexpected identifier. The `shop_cipher` query parameter is not required for this request. | 移除该参数后重试。所需的标识符请参见 API 文档。 |
| 36009004 | Unexpected identifier. The `category_asset_cipher` query parameter is not required for this request. | 移除该参数后重试。所需的标识符请参见 API 文档。 |
| 36009004 | Invalid identifier. The `shop_id` query parameter is invalid. | 通过 Get Authorized Shops 端点获取正确取值。 |
| 36009014 / 36009004 | Invalid API version. The `version` value is invalid or unsupported. | API 版本管理专题使用 `36009014` 标识无效版本，而较旧的文档或通用网关示例可能返回 `36009004` 并附带相同的 `Invalid API version` 消息。在文档与线上响应完全统一之前，请同时校验错误码与 `Invalid API version` 消息关键字，并以所调用端点与版本的实际响应为准。有效版本参见 TTS API versioning 及对应端点参考页。 |
| 36004004 | Invalid auth code. | `auth_code` 已被使用、已过期或无效。 |
