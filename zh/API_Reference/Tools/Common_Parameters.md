# 公共参数

调用 TikTok Shop API 时，除非 endpoint 文档另有说明，否则请包含以下公共参数。
# Query 参数
| **参数** | **位置** | **类型** | **描述** | **示例** |
| --- | --- | --- | --- | --- |
| `app_key` | Query | string | 分配给您的应用的唯一密钥。请参阅"创建您的应用"以了解在哪里获取 **`app_key`**。 | 29a39d |
| `sign` | Query | string | 基于请求参数值的 HMAC-SHA256 哈希值，服务端使用该值以及 access token 来验证请求的发送者。<br/>请参阅"签署您的 API 请求"以了解如何生成此签名。 | bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290 |
| `timestamp` | Query | Unix timestamp | 10 位 Unix 秒级时间戳，用于确保请求的时效性并防止重放攻击。请勿发送毫秒级时间戳。该值还用于生成 **`sign`** 参数的数字签名。<br/>有效范围：[当前时间 - 5 分钟，当前时间 + 30 秒]。发送无效时间戳可能导致错误 `36009004 Invalid timestamp`。 | 1623812664 |
# 请求头参数
| **参数** | **类型** | **描述** | **示例** |
| --- | --- | --- | --- |
| `x-tts-access-token` | string | 用于验证请求的店铺或卖家授权的 access token。对于 `202309` 及更高版本的 API，access token 必须通过此请求头发送，而不是 query 字符串。 | act.example_access_token |
| `content-type` | string | 请求内容类型。发送 JSON 请求体时使用 `application/json`。 | application/json |

> **版本说明：** 对于 `202309` 版本之前的旧版 API，一些较早的文档可能将 `access_token` 显示为 query 参数。对于 `202309` 及更高版本的 API，请使用 `x-tts-access-token` 请求头。

# Endpoint 特定的公共标识符
部分 endpoint 除上述参数外，还需要公共业务标识符。这些字段是否为必填取决于具体的 endpoint。请始终遵循 endpoint 文档以确认确切的位置、要求和允许的值。
| **参数** | **位置** | **类型** | **描述** | **示例** |
| --- | --- | --- | --- | --- |
| `shop_cipher` | 取决于 endpoint | string | 加密的店铺标识符。当 endpoint 需要店铺级标识符时包含此字段。如果该字段是 endpoint 签名请求参数的一部分，则在生成 `sign` 时需包含它。 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMtA |
| `category_asset_cipher` | 取决于 endpoint | string | 加密的品类资产标识符。当 endpoint 需要品类资产标识符时包含此字段。如果该字段是 endpoint 签名请求参数的一部分，则在生成 `sign` 时需包含它。 | CAT_ASSET_XF90igAAAABh00qsWgtvOiGFNqyubMtA |
