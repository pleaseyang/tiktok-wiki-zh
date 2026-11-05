# 创建或更新 Inbound Plan

# Path: /fbt/202602/create_update_inbound_plan
# Method: [POST]
# 功能描述
创建新的 inbound plan 或通过使用商品列表或带有尺寸的箱 configurations 完全替换现有 inbound plan 的内容。省略 `plan_id` 表示创建 plan；提供 `plan_id` 表示更新 plan。请恰好提供一个非空数组：`goods_items` 或 `cartons`；不可同时提供两者。
对于更新操作，请提交完整的期望商品或箱内容；请求中未包含的先前存储的商品或箱不会被保留。使用 `goods_items` 将清除现有的箱和批次/保质期数据。使用 `cartons` 将重建箱和商品数据。

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
| plan_id | string | N | 5766071177167344427 | 不提供 plan id 则为创建，提供 plan id 则为更新。 |
| idempotent_key | string | N | 9ef6857095f84893 | 创建 inbound plan 的幂等 key。当未提供 `plan_id` 时必填。 |
| goods_items | []object | N |  | 商品列表。 |
| ^goods_id | string | Y | 231313 | 此 inbound plan 商品的 Fulfilled by TikTok 商品标识符。商品必须属于与已认证卖家关联的商家，已通过履约审批，并已匹配到 SKU。 |
| ^quantity | int | Y | 400 | 此商品在 inbound plan 中的数量。必须大于 0。 |
| cartons | []object | N |  | 箱列表。 |
| ^carton_type | string | Y | SINGLE_SKU | 表示箱是配置为单 SKU 还是多 SKU。 |
**Possible values:**

* `SINGLE_SKU`: `items` must contain exactly one item.
* `MULTI_SKU`: `items` must contain two or more items. |
   ^items |[]object |Y | |箱中的商品列表。 |
   ^^goods_id |string |Y |12345 |此箱商品的 Fulfilled by TikTok 商品标识符。商品必须属于与已认证卖家关联的商家，已通过履约审批，并已匹配到 SKU。 |
   ^^quantity |int |Y |20 |此商品在每个箱中的数量。必须大于 0。 |
   ^^lot_code |string |N |sfsfnjkfvv |此商品的批次码。当商品启用批次码管理时必填。`cartons` 中同一 `goods_id` 的每次出现必须使用相同的 `lot_code` 和 `expiration_timestamp` 值。 |
   ^^expiration_timestamp |string |N |1623812664 |此商品的过期日期，以秒为单位的 Unix 时间戳表示。当商品启用保质期管理时必填。它不得早于当前时间加上商品特定的 `inbound_cutoff_days`。请从 Search Goods Info（`POST /fbt/202607/goods/search`）的 `data.goods[].lot_expiration_info.inbound_cutoff_days` 中获取此值。 |
   ^quantity |int |Y |2 |使用此箱配置表示的箱数量。 |
   ^carton_nums |[]string |N |["C0001","C0002"] |分配给此配置所代表箱的标识符。请求中的每个箱配置要么都提供非空的 `carton_nums` 数组，要么都不提供任何箱标识符。提供时，标识符的数量必须等于此配置的 `quantity`；每个标识符必须使用 `C` 加四位数字的格式，且在请求中必须唯一。如果未提供，箱标识符将自动生成。 |
   ^box_measurements |object |Y | |箱尺寸信息。 |
   ^^weight |string |Y |3.50 |箱重量。 |
   ^^weight_unit |string |Y |POUNDS |箱 `weight` 值使用的单位。

**Possible values:**

* `KILOGRAM` (kg)
* `GRAM` (g)
* `MILLIGRAM` (mg)
* `POUNDS` (lbs)
* `OUNCE` (oz) |
   ^^width |string |Y |1.2 |箱宽度。 |
   ^^height |string |Y |2 |箱高度。 |
   ^^length |string |Y |5 |箱长度。 |
   ^^length_unit |string |Y |INCH |箱的 `length`、`width` 和 `height` 值使用的单位。

**Possible values:**

* `METER` (m)
* `CENTIMETER` (cm)
* `MILLIMETER` (mm)
* `FOOT` (ft)
* `MICRON` (μm)
* `INCH` (in) |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202602/create_update_inbound_plan?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"plan_id":"5766071177167344427","idempotent_key":"9ef6857095f84893","goods_items":[{"goods_id":"231313","quantity":400}],"cartons":[{"carton_type":"SINGLE_SKU","items":[{"goods_id":"12345","quantity":20,"lot_code":"sfsfnjkfvv","expiration_timestamp":"1623812664"}],"quantity":2,"carton_nums":["C0001","C0002"],"box_measurements":{"weight":"3.50","weight_unit":"POUNDS","width":"1.2","height":"2","length":"5","length_unit":"INCH"}}]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^inbound_plan | object |  | Inbound plan。 |
| ^^plan_id | string | 5766071177167344427 | Plan 标识符。 |
# 响应示例
```json
{"code":0,"data":{"inbound_plan":{"plan_id":"5766071177167344427"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |

