# 获取订单拆包属性

# Path: /fulfillment/202309/orders/split_attributes
# Method: [GET]
# 功能描述
检查一个或多个 TikTok Shop 订单是否可以拆分为多个 package。对于每个评估的订单，响应会指示是否可以拆分，并且在不允许拆分时可能包含原因，以及在适用时的强制 package 拆分限制。

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
| order_ids | []string | Y | 556643423443,556643423444 | 以逗号分隔的 TikTok Shop 订单 ID 列表，用于检查 package 拆分资格。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/orders/split_attributes?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&order_ids=556643423443,556643423444
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^split_attributes | []object |  | 已评估的 TikTok Shop 订单的拆分资格结果。每个结果标识一个订单并指示是否可以拆分；在不允许拆分时可能包含原因，以及在适用时的强制 package 拆分限制。 |
| ^^order_id | string | 556643423444 | TikTok Shop 订单 ID。 |
| ^^can_split | bool | false | 订单是否可以拆分： |

* `true`：订单可以拆分为多个 package。
* `false`：订单不能拆分为多个 package。 |
   ^^reason |string |Order has been canceled |订单不能拆分的原因。仅在 `can_split = false` 时返回此字段。 |
   ^^must_split |bool |false |订单是否必须拆分：
* true：订单必须拆分为多个 package。
* false：订单不必拆分为多个 package。 |
   ^^must_split_reasons |[]object | |订单必须拆分的原因。仅在 must_split = true 时返回此字段。 |
   ^^^type |string |CATEGORY_ITEM_LIMITATION |返回命中的验证类型。有两种验证类型：CATEGORY_ITEM_LIMITATION 表示品类验证，TOTAL_COUNT_LIMITATION 表示商品总数量验证。 |
   ^^^category_id |string |601990 |与此拆分限制关联的品类 ID。当 `type` 为 `CATEGORY_ITEM_LIMITATION` 时返回值；当 `type` 为 `TOTAL_COUNT_LIMITATION` 时不返回值。 |
   ^^^max_count |string |2 |对于品类验证，返回单个 package 中该品类允许的最大商品数量；对于 package 内商品总数量验证，返回单个 package 中商品的总数量限制。 |

# 响应示例
```json
{"code":0,"data":{"split_attributes":[{"order_id":"556643423444","can_split":false,"reason":"Order has been canceled","must_split":false,"must_split_reasons":[{"type":"CATEGORY_ITEM_LIMITATION","category_id":"601990","max_count":"2"}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

