# 获取 Inbound 方式详情

# 路径：/fbt/202602/inbound_method_detail
# 方法：[POST]
# 功能描述
检索 inbound plan 的入库详情。首先调用该 plan 的 List Available Inbound Methods API，然后使用同一返回选项中的 `inbound_method` 和预计到达时间窗口。响应报告入库任务状态，以及在可用时带有货件分配的入库选项；`ONE_HUB` 选项还可以包含估算入库费用。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| plan_id | string | Y | 5766071177167344427 | Inbound plan 标识符 |
| inbound_method | string | Y | D2FC | **可能的值：** |

* `D2FC`（直接发送到 fulfillment center，可能拆分为多个货件）
* `ONE_HUB`（单一目的地；可包含估算入库费用） |
   estimate_arrival_time |object |Y | |所选 `inbound_method` 的预计到达时间窗口。使用此 plan 的 List Available Inbound Methods API 返回的 `available_time_window_list` 中同一条目的 `start_timestamp` 和 `end_timestamp`。 |
   ^start_timestamp |string |Y |1774162800 |预计到达窗口开始的 Unix 时间戳（秒），为 PDT 周日 00:00。例如，`1774162800` 对应 `2026-03-22T07:00:00Z`。

**此值必须与** **所选 List Available Inbound Methods 时间窗口的 `start_timestamp` 完全匹配。** |
^end_timestamp |string |Y |1774767600 |预计到达窗口结束的 Unix 时间戳（秒），为 PDT 周日 00:00。例如，`1774767600` 对应 `2026-03-29T07:00:00Z`。
**此值必须与** **所选 List Available Inbound Methods 时间窗口的 `end_timestamp` 完全匹配。** |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202602/inbound_method_detail?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"plan_id":"5766071177167344427","inbound_method":"D2FC","estimate_arrival_time":{"start_timestamp":"1774162800","end_timestamp":"1774767600"}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^info | []object |  | 当前入库任务的入库选项。如果 `placement_task_status` 为 `Executing`，请使用相同的 `plan_id`、`inbound_method` 和预计到达时间窗口重复此请求以获取最新状态。当状态为 `Succeed` 时，从 `info` 中选择一个选项并将其 `placement_option_id` 传递给 Confirm Inbound Method API。当状态为 `Failed` 时不要确认选项。在 `expiration_timestamp` 之后，使用相同的选择输入再次调用此 API 以获取新的入库选项或任务。 |
| ^^allocation_shipments | []object |  | 此入库选项的货件列表。 |
| ^^^warehouse_id | string | 7542187927317874487 | Warehouse 标识符。 |
| ^^^goods_items | []object |  | 商品列表。 |
| ^^^^goods_id | string | 2134566 | 商品标识符。 |
| ^^^^quantity | int | 400 | 此商品的数量。 |
| ^^^cartons | []object |  | 箱列表。 |
| ^^^^carton_type | string | SINGLE_SKU | 表示此箱是单 SKU 箱还是多 SKU 箱。 |
| **可能的值：** |  |  |  |

* `SINGLE_SKU`
* `MULTI_SKU` |
   ^^^^items |[]object | |箱中的商品列表。 |
   ^^^^^goods_id |string |12345 |商品标识符。 |
   ^^^^^quantity |int |20 |此商品的数量。 |
   ^^^^^lot_code |string |sfsfnjkfvv |此商品的批次码。 |
   ^^^^^expiration_timestamp |string |1623812664 |此商品的过期日期，以秒为单位的 Unix 时间戳。 |
   ^^^^quantity |int |2 |箱数量。 |
   ^^^^carton_nums |[]string |["C0001","C0002"] |箱号。 |
   ^^^^box_measurements |object | |箱尺寸信息。 |
   ^^^^^weight |string |3.5 |箱重量。 |
   ^^^^^weight_unit |string |POUNDS |箱 `weight` 值使用的单位。

**可能的值：**

* `KILOGRAM` (kg)
* `GRAM` (g)
* `MILLIGRAM` (mg)
* `POUNDS` (lbs)
* `OUNCE` (oz) |
   ^^^^^width |string |1.2 |箱宽度。 |
   ^^^^^height |string |2 |箱高度。 |
   ^^^^^length |string |5 |箱长度。 |
   ^^^^^length_unit |string |INCH |箱 `length`、`width` 和 `height` 值使用的单位。

**可能的值：**

* `METER` (m)
* `CENTIMETER` (cm)
* `MILLIMETER` (mm)
* `FOOT` (ft)
* `MICRON` (μm)
* `INCH` (in) |
   ^^^shipment_options |[]object | |货件选项。 |
   ^^^^shipping_method |string |SMALL_PARCEL |此货件选项的运输方式。可能的值：SMALL_PARCEL（小包裹运输方式）；FREIGHT（货运运输方式）。 |
   ^^placement_option_id |string |5766071177167344420 |入库选项 ID。入库选项代表货件拆分和目的地。 |
   ^^placement_fee_estimate |object | |`ONE_HUB` 入库选项的估算入库费用。 |
   ^^^amount |string |13.50 |入库费用金额。 |
   ^^^currency |string |USD |入库费用金额的货币。

**可能的值：**

* `USD`
* `CNY`
* `EUR`
* `GBP`
* `SAR` |
   ^placement_task_status |string |Executing |**可能的值：**
* `Executing`
* `Succeed`
* `Failed` |
   ^expiration_timestamp |string |1774767600 |入库结果过期的 Unix 时间戳（秒）。对于 `ONE_HUB`，过期时间设为此 API 处理请求后 24 小时。对于其他方式，为入库任务触发时间后 24 小时。过期后，再次调用此 API 以生成新的入库任务。 |

# 响应示例
```json
{"code":0,"data":{"info":[{"allocation_shipments":[{"warehouse_id":"7542187927317874487","goods_items":[{"goods_id":"2134566","quantity":400}],"cartons":[{"carton_type":"SINGLE_SKU","items":[{"goods_id":"12345","quantity":20,"lot_code":"sfsfnjkfvv","expiration_timestamp":"1623812664"}],"quantity":2,"carton_nums":["C0001","C0002"],"box_measurements":{"weight":"3.5","weight_unit":"POUNDS","width":"1.2","height":"2","length":"5","length_unit":"INCH"}}],"shipment_options":[{"shipping_method":"SMALL_PARCEL"}]}],"placement_option_id":"5766071177167344420","placement_fee_estimate":{"amount":"13.50","currency":"USD"}}],"placement_task_status":"Executing","expiration_timestamp":"1774767600"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |

