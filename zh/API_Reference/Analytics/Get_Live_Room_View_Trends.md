# 获取直播间观看趋势

# 路径：/analytics/202502/live_rooms/{live_room_id}/view_trend_performances
# 方法：[GET]
# 功能描述
返回指定直播间的观众数趋势数据点，按在线观众、进入观众和离开观众分组。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| live_room_id | string | Y | 7274599999999999999 | 请求观众趋势数据的直播间 ID。直播间必须与已授权的达人关联。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202502/live_rooms/7274599999999999999/view_trend_performances?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^view_trend_performances | []object |  | 直播间的观众数趋势 |
| ^^stats_type | string | TREND_ONLINE_VIEWER | 观众趋势类别。 |
| TREND_ONLINE_VIEWER：正在观看直播间的观众。 |  |  |  |
| TREND_ENTER_VIEWER：进入直播间的观众。 |  |  |  |
| TREND_LEFT_VIEWER：离开直播间的观众。 |  |  |  |
| ^^data_points | []object |  | 对应趋势类别的观众数数据点。 |
| ^^^value | string | 123 | 此数据点对应趋势类别的观众数。 |
| ^^^timestamp | int | 1623812664 | 观众数数据点的 Unix 时间戳（秒，UTC）。 |
# 响应示例
```json
{"code":0,"data":{"view_trend_performances":[{"stats_type":"TREND_ONLINE_VIEWER","data_points":[{"value":"123","timestamp":1623812664}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 66009302 | 参数无效。请检查直播间 ID。 |
| 66009315 | 无操作权限。 |

