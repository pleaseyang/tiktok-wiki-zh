# 获取视频表现

# Path: /analytics/202403/videos/performances
# Method: [GET]
# 功能描述
使用此仅限美国创作者的 API 检索 TikTok 电商视频指标，包括 anchor_display_rate、click_through_rate、orders、items_sold 和 GMV，用于请求的视频。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| video_ids | string | Y | 7341286689295469829,7271486684427046149 | 要检索电商 metrics 的视频 ID，以逗号分隔。所有视频 ID 必须属于同一作者。每次请求最多 100 个视频 ID。 |
| start_time_ge | int | Y | 1704091445 | metrics 的开始日期，由于数据管道的延迟，设置为从今天起延迟一天。start_time 参数必须在距当前日期 180 天以内。仅处理日期值，小时/分钟/秒值将被忽略。 |
| 例如，如果 start_time 值为：1703507696（"26-12-2023 04:34:56"），后端服务在处理查询时将仅考虑"26-12-2023"部分，因为默认情况下，在离线数据分析中没有小时/分钟/秒级别的数据。 |  |  |  |  |
| end_time_le | int | Y | 1711356201 | metrics 的结束日期，由于数据管道的延迟，设置为从今天起延迟一天。仅处理日期值，小时/分钟/秒值将被忽略。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202403/videos/performances?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&video_ids=7341286689295469829,7271486684427046149&start_time_ge=1704091445&end_time_le=1711356201
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^videos | []object |  | 包含视频对象列表。内部对象列表将按 video_id 字段升序排列。 |
| ^^id | string | 7271486684427046149 | 视频 ID。performances 数组包含该视频的每日 metrics。 |
| ^^performances | []object |  | 内部对象列表将按 start_time 字段升序排列。 |
| ^^^time_range | object |  | 时间范围对象 |
| ^^^^start_time | int | 1704067200 | metrics 的日期。 |
| ^^^^end_time | int | 1704067200 | metrics 的日期。 |
| ^^^metrics | object |  | 该视频的 performance metrics。 |
| ^^^^anchor_display_rate | string | 0.64 | 锚点展示率，以两位小数表示。 |
| ^^^^click_through_rate | string | 0.08 | 点击率，以两位小数表示。 |
| ^^^^order_count | int | 3 | 该日期的订单数。 |
| ^^^^item_sold_count | int | 3 | 该日期的售出商品数。 |
| ^^^^gmv | object |  | 该视频的 GMV（商品交易总额）。 |
| ^^^^^amount | string | 27.85 | 该日期的 GMV 值，以两位小数表示。 |
| ^^^^^currency | string | USD | GMV 金额的货币。此 API 返回 `USD`，即美元的 ISO 4217 代码。 |
# 响应示例
```json
{"code":0,"data":{"videos":[{"id":"7271486684427046149","performances":[{"time_range":{"start_time":1704067200,"end_time":1704067200},"metrics":{"anchor_display_rate":"0.64","click_through_rate":"0.08","order_count":3,"item_sold_count":3,"gmv":{"amount":"27.85","currency":"USD"}}}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

