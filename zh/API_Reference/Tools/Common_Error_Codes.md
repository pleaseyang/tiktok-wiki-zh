# 公共错误码

发送 API 请求时，确保正确的结构和格式是与 TikTok Shop 服务器顺畅通信的关键。本主题涵盖与**请求 query**、**请求头** 和 **body 格式**相关的常见网关及跨域错误。这些基础错误发生在业务逻辑处理之前，必须解决后才能成功处理请求。
**注意：** 响应码中的 `0` 表示请求已成功处理。
**业务错误码：** 本页面未详尽列出 endpoint 特定的业务错误。对于业务逻辑失败，请打开相应的 endpoint 参考页面，并查看该页面底部的 **Errorcode** 部分。完整 API 参考入口请参阅 [TTS API 参考文档](https://partner.tiktokshop.com/docv2/page/create-product)。
**推荐的排查路径：**

1. 首先确认 HTTP 状态码，尤其是 `401`、`403`、`404`、`408`、`429` 和 `5xx`。
2. 结合查看 API 响应的 `code` 和 `message`。一些常见的请求验证失败会复用相同的数字码。
3. 如果失败是 endpoint 特定的，请查看 endpoint 参考页面的 **Errorcode** 部分。
4. 如果失败与授权相关，请将 endpoint 所需的权限范围与 Partner Center 中应用的权限范围以及 token 的 `granted_scopes` 字段进行对比。

# `36009004` 的消息关键字索引
错误码 `36009004` 被用于多种不同的请求验证失败。请勿仅凭数字码进行程序化分支判断。应结合响应 `message` 关键字，并记录包含 `request_id` 的完整响应。
| **消息关键字** | **可能含义** | **检查内容** |
| --- | --- | --- |
| `Missing credentials`、`signature` | 缺少必需的 `sign` query 参数。 | 请参阅"签署您的 API 请求"生成有效签名。 |
| `access_token header is invalid` | `access_token` 请求头无效。 | 传递从 Get Access Token 获取的 access token。 |
| `x-tts-access-token header is invalid` | `x-tts-access-token` 请求头无效。 | 传递从 Get Access Token 获取的 access token，并确认该 token 属于正确的授权主体。 |
| `Invalid app_key` | `app_key` query 参数无效、已禁用、已删除或无法解析。 | 在 **Partner Center** 的 **App details** 页面检查 app key。 |
| `timestamp`、`lesser than 0` | `timestamp` query 参数为负数。 | 使用在可接受时间窗口内的 Unix timestamp。 |
| `timestamp`、`earlier than 5 minutes` | 时间戳过于陈旧。 | 保持时间戳在当前时间之前 5 分钟以内。 |
| `timestamp`、`more than 30 seconds` | 时间戳过于超前。 | 保持时间戳不超过当前时间之后 30 秒。 |
| `shop_cipher`、`not required` | 请求包含了不必要的 `shop_cipher`。 | 移除 `shop_cipher` 并检查 endpoint 所需的标识符。 |
| `category_asset_cipher`、`not required` | 请求包含了不必要的 `category_asset_cipher`。 | 移除 `category_asset_cipher` 并检查 endpoint 所需的标识符。 |
| `shop_id`、`invalid` | `shop_id` query 参数无效。 | 从 Get Authorized Shops 获取正确的店铺标识符。 |
| `Invalid API version` | API 版本无效或不受支持。 | 请参阅**参数错误**中的版本说明。API 版本指南可能使用 `36009014`，而旧版/通用网关响应可能仍然出现 `36009004`；请验证所调用的 endpoint/版本的实际响应。 |
# 通用错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与指导** |
| --- | --- | --- |
| 36009002 | 请求过多。您在短时间内发送了过多请求。 | 将此视为速率限制条件。HTTP 响应应与业务码一起处理：`HTTP 429` 和 `36009002` 均表示速率限制。应用重试/退避逻辑，如有 `Retry-After` 请遵循，并参阅速率限制了解详情。 |
| 36009007 | 请求超时。对 endpoint 的请求已超时。 | 请重试，或考虑将其拆分为更小的请求。 |
| 36009009 | 路径无效。指定的路径与任何可用 endpoint 不匹配。 | 请参阅 API 文档了解详情。 |
| 36009010 | 方法无效。所使用的 HTTP 方法不被此 endpoint 支持。 | 请参阅 API 文档了解详情。 |
| 36009021 | 文件大小无效。上传的文件大小超过最大限制。 | 请参阅 API 文档了解详情。 |
| 36009022 | 请求格式无效。对于结构化数据，请求体格式必须为 `application/json`；对于二进制文件，必须为 `multipart/form-data`。 | 请参阅 API 文档了解详情。 |
| 36009023 | 请求格式无效。`content-type` 请求头的值必须为 `multipart/form-data`。 | 请参阅 API 文档了解详情。 |
# 授权错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与指导** |
| --- | --- | --- |
| **105005** | **访问被拒绝。应用未被授权访问该 endpoint，因为应用或 access token 被授予的访问权限范围不包含该 endpoint 所需的访问权限范围。** | **最常见的访问权限范围失败。当 API 调用因"Access denied"失败，或在应用设置后从 Developer Tool / API Testing Tool 发起的调用失败时，请首先检查此项。** <br/>  <br/>  建议检查：  <br/>  1. 在 **Partner Center** > **App & Service** > **Manage API** 中检查应用已授予的权限范围。如果缺少所需权限范围，请在 Partner Center 中申请或启用它。  <br/>  2. 在 Get Access Token 响应的 `granted_scopes` 字段中检查 token 已授予的权限范围。如果缺少所需权限范围，请请求用户重新授权所需权限范围，然后相应地生成新 token。 |
| 101000 | 无效的 query 或请求头。`category_asset_cipher` query 参数或 `x-tts-access-token` 请求头无效。 | 对于 `category_asset_cipher`，请确保从 Get Authorized Category Assets endpoint 获取正确的值。  <br/>  <br/>  对于 `x-tts-access-token`，可能的原因包括：  <br/>  - token 的 `user_type` 对该 endpoint 无效。请参阅"生成测试 access token"中的 `user_type` 值定义，并查看 API entity tags 中的 endpoint 实体标签，以确认它期望的是卖家、达人、合作伙伴、店铺还是资产级别的 token。  <br/>  - token 未关联店铺，或关联的店铺与提供的 `shop_cipher` query 参数不匹配。  <br/>  <br/>  请参阅授权指南了解详情。 |
| 36009033 | 访问被拒绝。您的 IP 地址不在此应用配置的 IP 白名单中。 | 在 **Partner Center** > **App & Service** 中添加您的 IP 地址。 |
# 认证错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与指导** |
| --- | --- | --- |
| 105002 | 凭证已过期。`access_token` 或 `x-tts-access-token` 请求头已过期。 | 通过使用 Get Refresh Token endpoint 刷新您的 token。 |
| 106001 | 无效凭证。`sign` query 参数无效。 | 请参阅签署请求指南确保生成有效签名。 |
| 36009004 | 缺少凭证。请求未在 query 中包含必需的签名。 | 请参阅签署请求指南生成签名。 |
| 36009004 | 无效凭证。`access_token` 请求头无效。 | 请传入从 Get Access Token endpoint 获取的 `access_token`。 |
| 36009004 | 无效凭证。`x-tts-access-token` 请求头无效。 | 请传入从 Get Access Token endpoint 获取的 `access_token`。 |
| 36009004 | 无效凭证。`app_key` query 参数无效。 | 可能的原因包括密钥格式无效、应用未找到、应用已禁用或删除，或获取所需授权时出错。确保从 **Partner Center** 的 **App details** 页面获取正确的值。 |
| 36009004 | 无效时间戳。`timestamp` query 参数的值不得小于 0。 | 时间戳必须在当前时间之前 5 分钟到之后 30 秒的范围内。 |
| 36009004 | 无效时间戳。`timestamp` query 参数的值不得早于当前时间之前 5 分钟。 | 时间戳必须在当前时间之前 5 分钟到之后 30 秒的范围内。 |
| 36009004 | 无效时间戳。`timestamp` query 参数的值不得超过当前时间之后 30 秒。 | 时间戳必须在当前时间之前 5 分钟到之后 30 秒的范围内。 |
# 参数错误
| **错误码** <!-- width:90px --> | **错误消息** <!-- width:300px --> | **详情与指导** |
| --- | --- | --- |
| 106013 | 缺少标识符。需要 `shop_cipher` query 参数来标识目标店铺。 | 从 Get Authorized Shops endpoint 获取此值。 |
| 36009004 | 意外标识符。此请求不需要 `shop_cipher` query 参数。 | 移除它并重试。请参阅 API 文档了解所需标识符的详情。 |
| 36009004 | 意外标识符。此请求不需要 `category_asset_cipher` query 参数。 | 移除它并重试。请参阅 API 文档了解所需标识符的详情。 |
| 36009004 | 无效标识符。`shop_id` query 参数无效。 | 从 Get Authorized Shops endpoint 获取正确的值。 |
| 36009014 / 36009004 | 无效 API 版本。`version` 值无效或不受支持。 | API 版本主题使用 `36009014` 标识无效 API 版本，而旧版/通用网关示例可能显示 `36009004` 及相同的 `Invalid API version` 消息。在所有文档和运行时响应统一之前，请通过同时检查错误码和 `Invalid API version` 消息关键字来处理此情况，并验证您调用的 endpoint/版本的实际响应。请参阅 TTS API 版本控制和 endpoint 参考页面了解有效版本。 |
| 36004004 | 无效授权码。 | `auth_code` 已被使用、已过期或无效。 |
