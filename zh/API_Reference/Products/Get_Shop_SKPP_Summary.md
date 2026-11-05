# 获取店铺 SKPP 摘要

# Path: /product/202606/skpps/sum
# Method: [GET]
# 功能描述
Return the shop-level SKPP summary, including qualified and eligible product counts, earned ad credit, and incremental visibility in the last 30 days. This API is available only to shops enrolled as eligible SKPP sellers.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202606/skpps/sum?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^shop_summary | object |  | The shop-level SKPP summary of qualified and eligible product counts, earned ad credit, and incremental visibility in the last 30 days. |
| ^^qualified_products_count | int | 1 | Number of products that are already SKPP. |
| ^^eligible_products_count | int | 5 | Number of products that are already SKPP, plus those that have not yet met the standard but can take SKPP tasks. |
| ^^earned_ad_credit | string | $500 | Total ad credit earned by the shop, currency-prefixed. |
| ^^increased_visibility_l30d | string | 12345 | Incremental visibility gained from SKPP rewards in the last 30 days. |
# 响应示例
```json
{"code":0,"data":{"shop_summary":{"qualified_products_count":1,"eligible_products_count":5,"earned_ad_credit":"$500","increased_visibility_l30d":"12345"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12081001 | Invalid request parameters. |
| 12081003 | Internal server error. |
| 12081006 | Unauthorized for SKPP on this shop. |

