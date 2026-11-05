# 获取直播间 GMV 和订单趋势

# Path: /analytics/202502/live_rooms/{live_room_id}/gmv_trend_performances
# Method: [GET]
# 功能描述
返回指定直播间的 GMV 趋势表现数据点，包括 GMV 和创建订单的趋势值。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| live_room_id | string | Y | 7494534671928321024 | 已认证创作者拥有的直播间 ID。 |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202502/live_rooms/7494534671928321024/gmv_trend_performances?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^gmv_trend_performances | []object |  | 直播间的 GMV 和创建订单趋势序列。每项通过 `stats_type` 标识一个指标。 |
| ^^stats_type | string | TREND_GMV | stats_type 描述趋势值的类型。可选值：TREND_GMV（直播间的 GMV），TREND_CREATED_ORDER（直播间的创建订单数）。 |
| ^^data_points | []object |  | 由 `stats_type` 标识的指标的数据点。 |
| ^^^order_count | int | 123 | 此数据点的创建订单数。当 `stats_type` 为 `TREND_CREATED_ORDER` 时返回。 |
| ^^^timestamp | int | 1623812664 | 时间戳 |
| ^^^gmv | object |  | 此数据点的 GMV。当 `stats_type` 为 `TREND_GMV` 时返回。 |
| ^^^^currency | string | USD | GMV 金额的 ISO 4217 货币代码。 |
| ^^^^amount | string | 123.45 | GMV 金额 |
# 响应示例
```json
{"code":0,"data":{"gmv_trend_performances":[{"stats_type":"TREND_GMV","data_points":[{"order_count":123,"timestamp":1623812664,"gmv":{"currency":"USD","amount":"123.45"}}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 66009302 | 参数无效。请检查直播间 ID。 |
| 66009315 | 无操作权限。 |
