# 获取直播间商品统计

# 路径：/analytics/202502/live_rooms/{live_room_id}/product_stats
# 方法：[GET]
# 功能描述
返回指定直播间的商品表现统计，包括商品 ID、名称、GMV、单价、库存数量和点击次数。直播间必须与 access token 关联的达人所属。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| live_room_id | string | Y | 7494534671928321024 | 直播间 ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202502/live_rooms/7494534671928321024/product_stats?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_stats | []object |  | 指定直播间中每个商品的统计数据。 |
| ^^main_image_url | string | https://example.com/images/products/1732333333333333629-main.jpg | 商品主图 URL |
| ^^product_id | string | 1732333333333333629 | 每个商品的唯一 ID |
| ^^is_live | bool | true | 该商品是否正在直播间中上架 |
| ^^click_through_rate | string | 0.11 | 商品点击量与商品曝光量的比率 |
| ^^sellable_region | string | ID | 商品销售所在地区 |
| ^^created_order_count | int | 123 | 用户从直播中为此商品创建的订单数 |
| ^^exposure_count | int | 123 | 此商品的曝光次数，包括商品列表和商品卡 |
| ^^total_click_count | int | 123 | 此商品从直播中被点击的总次数，包括从商品列表和商品卡 |
| ^^local_gmv | object |  | 使用本地货币的商品收入 |
| ^^^amount | string | 123.45 | GMV 金额 |
| ^^^currency | string | USD | GMV 金额的 ISO 4217 货币代码。 |
| ^^product_name | string | Wireless Charging Stand | 直播间商品统计列表中的商品显示名称。 |
| ^^local_unit_price | object |  | 使用本地货币的售出商品平均单价 |
| ^^^amount | string | 12.34 | 单价金额 |
| ^^^currency | string | USD | 单价金额的 ISO 4217 货币代码。 |
| ^^paid_order_count | int | 123 | 用户从直播间为此商品创建并支付的 SKU 订单数 |
| ^^inventory_left_count | int | 123 | 商品的剩余库存 |
| ^^inventory_consumption_count | int | 123 | 已售出的商品数量 |
| ^^created_order_user_count | int | 123 | 为此商品创建订单的唯一用户数 |
| ^^paid_user_count | int | 123 | 为此商品支付订单的唯一用户数 |
| ^^click_order_rate | string | 0.11 | 商品已支付 SKU 订单数 / 商品点击量 |
# 响应示例
```json
{"code":0,"data":{"product_stats":[{"main_image_url":"https://example.com/images/products/1732333333333333629-main.jpg","product_id":"1732333333333333629","is_live":true,"click_through_rate":"0.11","sellable_region":"ID","created_order_count":123,"exposure_count":123,"total_click_count":123,"local_gmv":{"amount":"123.45","currency":"USD"},"product_name":"Wireless Charging Stand","local_unit_price":{"amount":"12.34","currency":"USD"},"paid_order_count":123,"inventory_left_count":123,"inventory_consumption_count":123,"created_order_user_count":123,"paid_user_count":123,"click_order_rate":"0.11"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 66009302 | 参数无效。请检查直播间 ID。 |
| 66009315 | 无操作权限。 |
