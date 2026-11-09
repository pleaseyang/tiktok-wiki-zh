# 获取店铺 SKPP 摘要

# 路径：/product/202606/skpps/sum
# 方法：[GET]
# 功能描述
返回店铺级的 SKPP 汇总，包括合格与符合条件的商品数量、已获得的广告积分以及最近 30 天的增量曝光。此接口仅对已注册为符合条件的 SKPP 卖家的店铺开放。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^shop_summary | object |  | 店铺级别的 SKPP 汇总，涵盖过去 30 天内合格及符合资格的商品数量，已获得的广告金以及增量曝光。 |
| ^^qualified_products_count | int | 1 | 已是 SKPP 的商品数量。 |
| ^^eligible_products_count | int | 5 | 已是 SKPP 的商品数量，加上尚未达到标准但可承接 SKPP 任务的商品数量。 |
| ^^earned_ad_credit | string | $500 | 店铺获得的总广告金，带货币前缀。 |
| ^^increased_visibility_l30d | string | 12345 | 过去 30 天从 SKPP 奖励中获得的增量曝光。 |
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

