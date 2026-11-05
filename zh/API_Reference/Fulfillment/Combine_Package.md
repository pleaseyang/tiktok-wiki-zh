# 合并 Package

# Path: /fulfillment/202309/packages/combine
# Method: [POST]
# 功能描述
使用此 API 将每个指定 package 中的订单合并到新的 fulfillment package 中。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| combinable_packages | []object | Y |  | 要合并的 package。至少提供一个 package。每个项目标识一个 package，并可以指定要包含的订单 ID。 |
| ^id | string | Y | 12321313133 | package ID。 |
| ^order_ids | []string | N | ["1233213123123","32132131231"] | 合并 `id` 标识的 package 时要包含的订单 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/combine?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"combinable_packages":[{"id":"12321313133","order_ids":["1233213123123","32132131231"]}]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^packages | []object |  | 成功合并的 package 返回列表。 |
| ^^id | string | 413234134123412 | package 成功合并后生成的新 package ID。 |
| ^^order_ids | []string | ["1233213123123","32132131231"] | 对应新合并 package ID 的订单 ID 列表。 |
| ^errors | []object |  | 无法合并的 package 返回的错误。 |
| ^^code | int | 10007014 | 失败原因代码。 |
| ^^message | string | fulfillment not allow combine package | package 合并操作不成功的原因。 |
| ^^detail | object |  | 错误详情。 |
| ^^^package_id | string | 1231231231231313123132 | Package ID。 |
# 响应示例
```json
{"code":0,"data":{"packages":[{"id":"413234134123412","order_ids":["1233213123123","32132131231"]}],"errors":[{"code":10007014,"message":"fulfillment not allow combine package","detail":{"package_id":"1231231231231313123132"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 21011028 | 该 package 不属于当前店铺。请确保您提供了正确的 package ID 和/或 shop cipher。 |
| 21011031 | 订单不属于 pre_pkg。请确保您提供了正确的订单 ID。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

