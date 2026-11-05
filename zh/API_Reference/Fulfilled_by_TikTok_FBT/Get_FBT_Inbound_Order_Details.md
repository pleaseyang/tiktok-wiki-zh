# 获取 FBT Inbound 订单详情

# Path: /fbt/202602/inbound_orders
# Method: [GET]
# 功能描述
检索指定 FBT inbound 订单的详情，包括计划和实际收货信息及状态历史。将 `include_carton_details` 设为 `true` 以请求箱尺寸和商品数量。

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
| order_ids | []string | Y | 5766071177167344427,5766071177167344428 | 要获取信息的 inbound 订单数字标识符列表。 |
| **注意：** 仅提供数字序列；不要包含"IBR"前缀（例如，使用 `123456` 而非 `IBR123456`）。每次请求最多获取 **10 个订单**。 |  |  |  |  |
仅返回当前卖家可找到和可访问的订单。缺失或不可访问的订单 ID 将从响应中省略；如果无法返回任何请求的订单，则请求失败。
您可以在 [Inbound FBT 订单状态变更](6708f866a88d1103246fed6a) webhook 中的 `data.inbound_order_id` 或 [Search FBT Inventory Record](670d584ba83c5f030f3071e4) 响应中的 `data.inventory_records.order.id` 获取该值。 |
include_carton_details |bool |N |true |一个布尔标志，决定响应是否应包含货件中每个箱的详细信息。
**Note**: When set to `true`, the response will include the `carton_details` field. If set to `false` or omitted, this field will be excluded from the response payload to optimize performance. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202602/inbound_orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&order_ids=5766071177167344427,5766071177167344428&include_carton_details=true
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^inbound_orders | []object |  | inbound 订单详情信息列表。 |
| ^^order_id | string | 5766071177167344427 | Fulfilled by TikTok 系统中 inbound 订单的数字标识符。 |
| ^^order_id_string | string | IBR5766071177167344427 | Fulfilled by TikTok 系统中 inbound 订单的字符串标识符。 |
| ^^order_plan_id | string | 5766071177167345050 | Inbound 订单的 plan 标识符。 |
| ^^merchant | object |  | 拥有该订单的商家信息。 |
| ^^^id | string | 493493403043 | Fulfilled by TikTok 系统中商家的标识符。 |
| ^^^name | string | ExampleCompany | Fulfilled by TikTok 商家名称。 |
| ^^create_time | int | 1773778751 | inbound 订单创建时的 Unix 秒级时间戳。 |
| ^^ship_time | int | 1773778751 | inbound 订单发货时的 Unix 秒级时间戳。 |
| ^^expected_arrival_time | int | 1773778751 | 商家提供的预计到达时间的 Unix 秒级时间戳。 |
| ^^actual_arrival_time | int | 1773778751 | inbound 订单实际到达时间的 Unix 秒级时间戳。 |
| ^^warehouse | object |  | Warehouse 信息。 |
| ^^^fbt_warehouse_id | string | 121219993203023 | Fulfilled by TikTok 系统生成的 warehouse 标识符。 |
| ^^^business_warehouse_ids | []string | ["121219993209983"] | TikTok Shop 系统生成的 warehouse 业务标识符，与 `fbt_warehouse_id` 关联。 |
| ^^^name | string | TikTok Warehouse | Fulfilled by TikTok warehouse 名称。 |
| ^^^type | string | FC | 与 inbound 订单关联的 warehouse 类型。 |
Possible values:

* `HUB`
* `FC` (Fulfillment Center) |
   ^^status_logs |[]object | |Inbound 订单操作历史条目，源自最多 200 条源状态记录。此列表可能不完整，且此操作不提供用于检索额外状态记录的游标。 |
   ^^^operate_time |int |1715398048 |商家或 warehouse 处理 inbound 订单的时间，以秒为单位的 Unix 时间戳表示。 |
   ^^^new_status |string |RECEIVED |此操作后 **Fulfilled by TikTok (FBT)** warehouse 中的订单状态。

**Possible values:**

* `WORKING`
* `READY_TO_SHIP`
* `TO_BE_RECEIVED`
* `ARRIVED_HUB`
* `INTERNAL_TRANSFER`
* `RECEIVING`
* `PARTIALLY_RECEIVED`
* `RECEIVED`
* `CANCELLED`
* `DELIVERED` |
   ^^^previous_status |string |PARTIALLY_RECEIVED |此操作前 **Fulfilled by TikTok (FBT)** warehouse 中的订单状态。

**Possible values:**

* `WORKING`
* `READY_TO_SHIP`
* `TO_BE_RECEIVED`
* `ARRIVED_HUB`
* `INTERNAL_TRANSFER`
* `RECEIVING`
* `PARTIALLY_RECEIVED`
* `RECEIVED`
* `CANCELLED`
* `DELIVERED` |
   ^^^operator |string |Warehouse |执行状态更改的用户或系统实体的唯一标识符或名称。 |
   ^^logistic_info_list |[]object | |与订单关联的物流信息列表。仅对小包裹 inbound 订单填充。 |
   ^^^provider_name |string |UPS |物流服务提供商名称

Possible values:

* `FEDEX` (Federal Express)
* `UPS` (United Parcel Service)
* `DHL` (DHL Express)
* `USPS` (United States Postal Service)
* `OTHER` (All other logistics providers) |
   ^^^waybill_number |string |889042812410 |当前与承运商的 inbound 货件的追踪号。 |
   ^^^related_number |string |C0001 |与物流信息关联的箱号。 |
   ^^carton_details |[]object | |inbound 订单的详细箱信息。仅在请求中 `include_carton_details` 传递为 true 时填充。 |
   ^^^carton_no |string |C0001 |箱号。 |
   ^^^carton_type |string |SINGLE_SKU |此箱是单 SKU 还是多 SKU。

**Possible values:**

* `SINGLE_SKU`
* `MULTI_SKU` |
   ^^^box_measurements |object | |箱尺寸信息。 |
   ^^^^weight |string |5 |箱重量。 |
   ^^^^weight_unit |string |KILOGRAM |箱 `weight` 值使用的单位。

**Possible values:**

* `KILOGRAM` (kg)
* `GRAM` (g)
* `MILLIGRAM` (mg)
* `POUNDS` (lbs)
* `OUNCE` (oz) |
   ^^^^width |string |6 |箱宽度。 |
   ^^^^height |string |7 |箱高度。 |
   ^^^^length |string |8 |箱长度。 |
   ^^^^length_unit |string |METER |箱 `length`、`width` 和 `height` 值使用的单位。

**Possible values:**

* `METER` (m)
* `CENTIMETER` (cm)
* `MILLIMETER` (mm)
* `FOOT` (ft)
* `MICRON` (μm)
* `INCH` (in) |
   ^^^items |[]object | |此箱中的商品列表。 |
   ^^^^goods_id |string |7603596185 |Fulfilled by TikTok 系统中商品的标识符。 |
   ^^^^quantity |int |10 |此箱中商品的单位数量。 |
   ^^inbound_goods_lot_receive_item_details |[]object | |按计划与实际收货信息的详细细分，按商品、批次号和过期日期分段。 |
   ^^^goods_id |string |7603596185 |Fulfilled by TikTok 内商品的唯一数字标识符。 |
   ^^^lot_code |string |LOT-2024-XP9 |制造商为此组商品分配的批次号。此字段仅对启用批次码管理的商品非空。 |
   ^^^expiration_time |int |1735689600 |此批次中商品的过期日期，以秒为单位的 Unix 时间戳表示。此值仅对启用保质期管理的商品非零。 |
   ^^^planned_count |int |100 |作为 inbound 订单一部分预期收到的此特定批次的总数量。 |
   ^^^normal_received_count |int |98 |此批次在 **fulfillment centers** 以可售（良好）状态收到的商品数量。如果 inbound 订单发送至 hub，此值仅在商品随后转移到 fulfillment center 时更新。 |
   ^^^defective_received_count |int |2 |以损坏或不可售状态收到的商品数量。 |
   ^^^total_received_count |int |100 |`normal_received_count` 和 `defective_received_count` 之和。 |

# 响应示例
```json
{"code":0,"data":{"inbound_orders":[{"order_id":"5766071177167344427","order_id_string":"IBR5766071177167344427","order_plan_id":"5766071177167345050","merchant":{"id":"493493403043","name":"ExampleCompany"},"create_time":1773778751,"ship_time":1773778751,"expected_arrival_time":1773778751,"actual_arrival_time":1773778751,"warehouse":{"fbt_warehouse_id":"121219993203023","business_warehouse_ids":["121219993209983"],"name":"TikTok Warehouse","type":"FC"},"status_logs":[{"operate_time":1715398048,"new_status":"RECEIVED","previous_status":"PARTIALLY_RECEIVED","operator":"Warehouse"}],"logistic_info_list":[{"provider_name":"UPS","waybill_number":"889042812410","related_number":"C0001"}],"carton_details":[{"carton_no":"C0001","carton_type":"SINGLE_SKU","box_measurements":{"weight":"5","weight_unit":"KILOGRAM","width":"6","height":"7","length":"8","length_unit":"METER"},"items":[{"goods_id":"7603596185","quantity":10}]}],"inbound_goods_lot_receive_item_details":[{"goods_id":"7603596185","lot_code":"LOT-2024-XP9","expiration_time":1735689600,"planned_count":100,"normal_received_count":98,"defective_received_count":2,"total_received_count":100}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |
| 39015009 | SellerId 输入无效 |
| 39015010 | 未找到该 merchant 的 inbound 订单。 |
| 39015020 | 请求中的订单数量超过配置的限制。 |

