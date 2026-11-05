# 获取 FBT MCF 订单状态

# Path: /fbt/202601/mcf_outbound_orders
# Method: [GET]
# 功能描述
使用此 API 检索 MCF 订单及其 consign 订单的当前状态和履约详情。如果订单因承运商限制或包裹尺寸限制需要多个包裹，FBT system 会将其拆分履约，并在 `consign_orders` 中为每个包裹返回一个条目。

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
| mcf_order_id | string | Y | 7136104329798256386 | 用于标识不同 MCF 订单的唯一 ID |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202601/mcf_outbound_orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&mcf_order_id=7136104329798256386
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^mcf_order | object |  | MCF 订单信息 |
| ^^external_order_id | string | shopify202208291503530001100220033 | 您 OMS 中对应的订单 ID。 |
| ^^mcf_order_id | string | 7136104329798256386 | 用于标识不同 MCF 订单的唯一 ID |
| ^^consign_orders | []object |  | 为 MCF 订单创建的 consign 订单。如果履约被拆分为多个包裹，此数组包含每个包裹的一个条目。 |
| ^^^id | string | 1234 | `consign order` 唯一 ID |
| ^^^goods | []object |  | 此 consign 订单中的商品 ID 和数量。 |
| ^^^^id | string | 123124124 | Fulfilled by TikTok 系统生成的商品标识符 |
| ^^^^quantity | int | 1 | 此 consign 订单中的商品数量 |
| ^^^tracking_number | string | TN87654321 | 此 consign 订单的追踪号。如果订单尚未交给物流承运商，此字段可能为空值。 |
| ^^^carrier | string | USPS | The shipping carrier of this consign order. If the order has not yet been handed over to the logistics carrier, this field may be a null value. |
| ^^^status | string | PENDING | consign 订单的状态。 |
Possible values:

* **PENDING** - 订单正在等待 warehouse 处理。
* **HANDLE_BY_WAREHOUSE** - 订单正在由 warehouse 处理。
* **SHIPPED** - 订单已从 warehouse 发出。
* **HANDOVER** - 物流承运商已接收订单，正在运输中。
* **CLOSED** - 订单已关闭。
* **LOST** - 订单丢失。
* **DAMAGE** - 订单损坏。
* **RETURNED** - 订单已退回。
* **SCRAP** - 订单已报废。
* **UNKNOWN** - consign 订单状态或运输异常子类型未知。
* **COMPLETED** - 订单已完成。
* **ABNORMAL** - 存在问题导致订单无法履约。 |
   ^^^is_platform_closed |bool |false |当 `status` 为 `CLOSED` 时表示谁取消了 consign 订单。`true` 表示 FBT 平台取消了订单；`false` 表示通过您的 OMS 取消。 |
   ^^^issue |string |Lack of inventory |此字段显示订单停滞的原因。当 `consign order` 处于异常状态（如 **ABNORMAL**、**LOST** 等）时，具体的问题原因将在此处显示。 |
   ^^^shipping_provider |object | |此 consign 订单的物流承运商详细信息。如果订单尚未交给物流承运商，此字段可能为空值。 |
   ^^^^id |string |7345645330412603141 |物流承运商唯一 ID。 |
   ^^^^name |string |UPS |物流承运商名称。 |
   ^^create_time |int |1661756811 |MCF 订单创建时的 Unix 时间戳（秒）。 |

# 响应示例
```json
{"code":0,"data":{"mcf_order":{"external_order_id":"shopify202208291503530001100220033","mcf_order_id":"7136104329798256386","consign_orders":[{"id":"1234","goods":[{"id":"123124124","quantity":1}],"tracking_number":"TN87654321","carrier":"USPS","status":"PENDING","is_platform_closed":false,"issue":"Lack of inventory","shipping_provider":{"id":"7345645330412603141","name":"UPS"}}],"create_time":1661756811}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 177001009 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 177001010 | 无法通过您提供的 mcf_order_id 检索订单信息；请检查您的 ID 是否正确。 |

