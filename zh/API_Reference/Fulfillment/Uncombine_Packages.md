# 取消合并 Package

# 路径：/fulfillment/202309/packages/{package_id}/uncombine
# 方法：[POST]
# 功能描述
使用此 API 从已合并的 package 中取消合并一个或多个订单。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| package_id | string | Y | 123456 | 您希望从中取消合并订单的 package ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_ids | []string | N | ["11132131131"] | TikTok Shop 订单 ID。指定需要从 package 中移除的订单。请确保订单属于该 package。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/123456/uncombine?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_ids":["11132131131"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^packages | []object |  | 从原始合并 package 中移除指定订单后创建的 package。 |
| ^^id | string | 123456 | 取消合并后生成的新 package ID。 |
| ^^order_ids | []string | ["576462377512830168"] | 对应取消合并 package ID 的订单 ID 列表。 |
# 响应示例
```json
{"code":0,"data":{"packages":[{"id":"123456","order_ids":["576462377512830168"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10006402 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11001027 | 系统超时。如果此错误持续存在，请联系平台寻求帮助。 |
| 21001001 | 参数无效。请确保您传递了正确的请求参数。 |
| 21001008 | 未找到错误 |
| 21001028 | 订单正在处理中。请稍后重试。 |
| 21008042 | 卖家已打印 shipping label |
| 21011001 | 未找到 package。如果错误持续存在，请联系平台寻求帮助。 |
| 21011005 | 传递了无效的请求参数。请检查您是否具有正确的参数类型和格式。 |
| 21011006 | 这些订单已经发货。 |
| 21011007 | Package 商品有售后请求，请先处理售后请求。 |
| 21011017 | 单个订单无需合并 |
| 21011028 | 该 package 不属于当前店铺。请确保您提供了正确的 package ID 和/或 shop cipher。 |
| 21011029 | 订单不属于该 fulfill unit |

