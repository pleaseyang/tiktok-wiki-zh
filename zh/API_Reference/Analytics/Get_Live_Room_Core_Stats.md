# 获取直播间核心统计

# 路径：/analytics/202502/live_rooms/{live_room_id}/core_stats
# 方法：[GET]
# 功能描述
返回指定直播间的核心统计数据，包括 GMV、订单数、买家数、商品点击数和观看次数。

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
https://open-api.tiktokglobalshop.com/analytics/202502/live_rooms/7494534671928321024/core_stats?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^stats | object |  | 直播间的统计数据 |
| ^^sales | int | 123 | 从直播中售出的商品数量 |
| ^^local_gmv | object |  | 从直播中产生的商品交易总额（GMV），以本地货币表示。 |
| ^^^amount | string | 123.45 | GMV 金额 |
| ^^^currency | string | USD | `amount` 的 ISO 4217 货币代码。 |
| ^^created_order_count | int | 123 | 用户从直播中创建的 SKU 订单数 |
| ^^current_visitor_count | int | 123 | 当前正在观看直播的观众数。 |
| ^^paid_order_count | int | 123 | 用户从直播中创建并支付的 SKU 订单数 |
| ^^local_unit_price | object |  | 售出商品的平均单价 |
| ^^^amount | string | 12.34 | 单价金额 |
| ^^^currency | string | USD | `amount` 的 ISO 4217 货币代码。 |
| ^^product_reach_count | int | 123 | 从直播中的商品点击数，包括商品列表和商品卡点击 |
| ^^watch_pv | int | 123 | 直播的观看次数 |
| ^^click_through_rate | string | 0.11 | 点击率，商品点击量 / 观看次数 |
| ^^accumulated_new_follower_count | int | 123 | 用户点击关注达人的次数 |
| ^^buyer_count | int | 123 | 从直播中支付订单的唯一用户数，包括已退货/退款的订单 |
| ^^accumulated_comment_count | int | 123 | 用户在直播中发表评论的累计次数 |
| ^^product_view_count | int | 123 | 所有直播商品的曝光次数，包括商品列表和商品卡曝光 |
| ^^click_order_rate | string | 0.11 | 点击转化率，已支付 SKU 订单数 / 商品点击量 |
| ^^avg_watching_duration | int | 123 | 每个唯一观众观看直播的平均时长。 |
| ^^accumulated_sharing_count | int | 123 | 用户分享直播的累计次数 |
| ^^peak_concurrent_user_count | int | 123 | 直播的同时在线观众峰值 |
# 响应示例
```json
{"code":0,"data":{"stats":{"sales":123,"local_gmv":{"amount":"123.45","currency":"USD"},"created_order_count":123,"current_visitor_count":123,"paid_order_count":123,"local_unit_price":{"amount":"12.34","currency":"USD"},"product_reach_count":123,"watch_pv":123,"click_through_rate":"0.11","accumulated_new_follower_count":123,"buyer_count":123,"accumulated_comment_count":123,"product_view_count":123,"click_order_rate":"0.11","avg_watching_duration":123,"accumulated_sharing_count":123,"peak_concurrent_user_count":123}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 66009302 | 参数无效。请检查直播间 ID。 |
| 66009315 | 无操作权限。 |
