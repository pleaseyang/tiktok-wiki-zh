# 发货 Inbound 订单

# Path: /fbt/202603/ship_inbound_order
# Method: [POST]
# 功能描述
为准备发货的 inbound 订单确定箱和运输详情。对于尚未发货的订单，成功响应表示详情已保存且订单已进入收货阶段。在订单已发货后重复请求将返回成功但不会再次应用提供的详情。

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
| inbound_order_id | string | Y | 5766071177167344427 | 要发货的 inbound 订单的标识符。 |
| cartons | []object | N |  | 箱详情。当 inbound plan 使用 `goods_items` 而非 `cartons` 创建或更新且订单尚未发货时必填。重试已发货的订单时不需要。 |
| ^carton_type | string | Y | SINGLE_SKU | 箱组成类型。 |
**Possible values:**

* `SINGLE_SKU` - `items` must contain exactly one goods item.
* `MULTI_SKU` - `items` must contain more than one goods item. |
   ^items |[]object |Y | |箱中的商品列表。 |
   ^^goods_id |string |Y |723456789012345678 |箱中商品的标识符。 |
   ^^quantity |int |Y |100 |父箱条目所代表的每个箱中此商品的单位数量。必须大于 0。 |
   ^^lot_code |string |N |sfsfnjkfvv |商品的批次码。当商品启用批次码管理时必填。如果同一 `goods_id` 出现在多个箱中，每次出现请使用相同的 `lot_code` 和 `expiration_timestamp`。 |
   ^^expiration_timestamp |string |N |1623812664 |商品的过期时间，以秒为单位的 Unix 时间戳表示。当商品启用保质期管理时必填。它不得早于当前时间加上商品特定的 `inbound_cutoff_days`。请从 Search Goods Info（`POST /fbt/202607/goods/search`）的 `data.goods[].lot_expiration_info.inbound_cutoff_days` 中获取此值。如果同一 `goods_id` 出现在多个箱中，每次出现请使用相同的 `expiration_timestamp` 和 `lot_code`。 |
   ^quantity |int |Y |2 |此箱条目代表的实际箱数量。 |
   ^carton_nums |[]string |N |["C0001","C0002"] |此箱条目代表的实际箱的箱号。要么从每个箱中省略 `carton_nums` 以自动生成箱号，要么为每个箱提供。提供时，每个值必须由 `C` 加四位数字组成，值在请求中必须唯一，且值的数量必须等于 `quantity`。 |
   ^box_measurements |object |Y | |箱尺寸信息。 |
   ^^weight |string |Y |10 |箱重量。 |
   ^^weight_unit |string |Y |POUNDS |箱重量使用的单位。

**Possible values:**

* `KILOGRAM` (kg)
* `GRAM` (g)
* `MILLIGRAM` (mg)
* `POUNDS` (lbs)
* `OUNCE` (oz) |
   ^^width |string |Y |20 |箱宽度。 |
   ^^height |string |Y |2 |箱高度。 |
   ^^length |string |Y |3 |箱长度。 |
   ^^length_unit |string |Y |INCH |箱的长度、宽度和高度使用的单位。

**Possible values:**

* `METER` (m)
* `CENTIMETER` (cm)
* `MILLIMETER` (mm)
* `FOOT` (ft)
* `MICRON` (μm)
* `INCH` (in) |
   shipment_option |object |Y | |包含货运类型和运输方式的货件选项。 |
   ^shipping_method |string |Y |SMALL_PARCEL |运输方式。可能的值：SMALL_PARCEL（小包裹运输）；FREIGHT（货运运输）。 |
   ^freight_type |string |N |FTL |货运装载类型。当 EU 和 UK 店铺的 `shipping_method` 为 `FREIGHT` 时必填。对于 US 店铺为可选，当 `shipping_method` 为 `SMALL_PARCEL` 时不需要。

**Possible values:**

* `FTL`
* `LTL` |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202603/ship_inbound_order?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"inbound_order_id":"5766071177167344427","cartons":[{"carton_type":"SINGLE_SKU","items":[{"goods_id":"723456789012345678","quantity":100,"lot_code":"sfsfnjkfvv","expiration_timestamp":"1623812664"}],"quantity":2,"carton_nums":["C0001","C0002"],"box_measurements":{"weight":"10","weight_unit":"POUNDS","width":"20","height":"2","length":"3","length_unit":"INCH"}}],"shipment_option":{"shipping_method":"SMALL_PARCEL","freight_type":"FTL"}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^inbound_order_id | string | 5766071177167344427 | 已发货 inbound 订单的标识符。 |
# 响应示例
```json
{"code":0,"data":{"inbound_order_id":"5766071177167344427"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |

