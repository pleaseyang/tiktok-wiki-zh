# 取消 FBT MCF 订单

# Path: /fbt/202601/mcf_outbound_orders/cancel
# Method: [POST]
# 功能描述
一个 FBT 多渠道履约（MCF）订单可能会被拆分为一个或多个 consign 订单进行履约。使用此 API 通过提供 `mcf_order_id` 来取消 MCF 订单或选定的 consign 订单。如需取消选定的 consign 订单，请提供其 consign 订单 ID。您可以通过调用 **Get FBT MCF Order Status** API 获取已分配的 ID；在目标 consign 订单仍处于可取消的发货前状态时使用返回的 ID。
对于已达到 `SHIPPED`、`HANDOVER`、`COMPLETED` 或运输异常状态（如 `LOST`、`DAMAGE`、`RETURNED` 或 `SCRAP`）的目标 consign 订单，取消请求将被拒绝。
请求提交后，请将目标 consign 订单 ID 与此 API 的响应进行匹配。返回状态为 `CLOSED` 表示该 consign 订单已被取消。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| mcf_order_id | string | Y | 7136104329798256386 | MCF 订单 ID，以数字字符串形式表示。 |
| consign_orders | []object | N |  | 需要取消的 consign 订单。省略此字段将取消指定 MCF 订单中的所有 consign 订单。 |
| ^id | string | N | 7136104329798256386 | consign 订单 ID，以不带 `OBF` 前缀的数字字符串形式表示。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202601/mcf_outbound_orders/cancel?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"mcf_order_id":"7136104329798256386","consign_orders":[{"id":"7136104329798256386"}]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^mcf_order | object |  | MCF 订单信息及关联的 consign 订单状态。 |
| ^^external_order_id | string | shopify7136104329798256386 | 您 OMS 中对应的订单 ID。 |
| ^^mcf_order_id | string | 7136104329798256386 | 用于标识不同 MCF 订单的唯一 ID |
| ^^consign_orders | []object |  | MCF 订单中的所有 consign 订单及其在取消请求后的当前状态。请将请求的 consign 订单 ID 与返回的条目进行匹配；状态为 `CLOSED` 表示该 consign 订单已被取消。 |
| ^^^id | string | 1234 | consign 订单 ID，以不带 `OBF` 前缀的数字字符串形式返回。 |
| ^^^status | string | CLOSED | 该 consign 订单的当前状态。在取消响应中，`CLOSED` 表示该 consign 订单已被取消。 |
可能的状态枚举值

1. **PENDING** - 订单正在等待 warehouse 处理
2. **HANDLE_BY_WAREHOUSE** - 订单正在由 warehouse 处理
3. **SHIPPED** - 订单已从 warehouse 发出
4. **HANDOVER** - 订单已由物流承运商接收，正在运输中
5. **CLOSED** - 订单已取消
6. **LOST** - 订单丢失
7. **DAMAGE** - 订单损坏
8. **COMPLETED** - 订单已完成
9. **ABNORMAL** - 该订单存在问题，无法履约
10. **RETURNED** - 订单已退回
11. **SCRAP** - 订单已报废
12. **UNKNOWN** - 订单状态未知 |

# 响应示例
```json
{"code":0,"data":{"mcf_order":{"external_order_id":"shopify7136104329798256386","mcf_order_id":"7136104329798256386","consign_orders":[{"id":"1234","status":"CLOSED"}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 177001009 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

