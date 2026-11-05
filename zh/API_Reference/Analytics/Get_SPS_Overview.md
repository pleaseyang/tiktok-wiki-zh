# 获取 SPS 概览

# Path: /analytics/202606/shop_performances/overview
# Method: [GET]
# 功能描述
返回授权店铺的 SPS 概览，包括分数、等级、维度、权益和 top 问题。
店铺绩效分（SPS）反映店铺在 TikTok Shop 上关键运营和服务指标方面的表现。通过集成只读的 SPS API，ISV 可以获取店铺的分数、等级、权益和指标基准，诊断绩效差距，并深入查看与特定问题相关的商品、物流服务商、售后类型、订单或聊天。这使 ISV 能够在其解决方案中嵌入可操作的 performance 洞察，帮助商家更快地识别问题区域并采取针对性措施来提升店铺表现。仅适用于美国地区店铺。
使用场景指南：[点击此处](https://partner.tiktokshop.com/docv2/page/ph0ccose)

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | BCP 47 区域代码，用于本地化响应文本。如果省略，则从请求上下文中解析默认区域设置。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/overview?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^benefits | []object |  | 与店铺 SPS 分数相关的固定完整权益集。 |
| ^^benefit_name | string | LIVE giveaway | 按请求区域本地化的权益显示名称。 |
| ^^is_unlocked | bool | true | 店铺是否已解锁此权益。 |
| ^^unlock_score | string | 4.5 | 解锁该权益所需的分数，范围 0 到 5。 |
| ^dimensions | []object |  | 按 SPS 维度的分数详情。 |
| ^^name | string | Product satisfaction | 维度名称。 |
| ^^score | string | 4.8 | 维度分数，范围 0 到 5。 |
| ^^status | string | EXCELLENT | 维度状态枚举。可选值包括 EXCELLENT、GOOD、POOR、CRITICAL 和 NIL。 |
| ^^status_text | string | Excellent | 维度状态文本。值如 Excellent、Good、Normal、Attention。 |
| ^^weight | string | 70 | 维度权重，为 0 到 100 的百分比。 |
| ^evaluate_duration_days | int | 90 | 分数评估周期包含的天数。 |
| ^end_evaluation_time | int | 1782518400 | 评估周期结束时间。Unix 时间戳（秒）。 |
| ^start_evaluation_time | int | 1774828800 | 评估周期开始时间。Unix 时间戳（秒）。 |
| ^peer_percentile | string | 86.5 | 店铺在同行中的百分位排名，范围 0 到 100。 |
| ^primary_category | object |  | 店铺的主营类目。 |
| ^^category_id | string | 601450 | 主营类目 ID。 |
| ^^category_name | string | Home Supplies | 主营类目名称。 |
| ^sps_score | string | 4.6 | 店铺 SPS 分数，范围 0 到 5，保留一位小数。 |
| ^sps_tier | string | GOOD | SPS 等级。可选值包括 EXCELLENT、GOOD、POOR、CRITICAL 和 NIL。 |
| ^sps_tier_text | string | Excellent | SPS 等级文本。值如 Excellent、Good、Normal、Attention。 |
| ^top_issues | object |  | 影响当前分数的 top SPS 问题。 |
| ^^issues | []object |  | 排名的问题列表。 |
| ^^^description | string | Your on-time delivery performance is lower than peer shops. | 本地化的问题描述。 |
| ^^^evaluate_duration_days | int | 31 | 该问题评估周期包含的天数。 |
| ^^^end_evaluation_time | int | 1761264000 | 问题评估周期结束时间。Unix 时间戳（秒）。 |
| ^^^start_evaluation_time | int | 1758672000 | 问题评估周期开始时间。Unix 时间戳（秒）。 |
| ^^^metric_code | string | OTDR | 相关指标代码。可选值包括 NRR、NBFR、SFCR、OTDR、AHT 和 IM_DSAT。 |
| ^^^metric_name | string | On-time delivery rate | 本地化的指标显示名称。 |
| ^^^percentile | string | 72.4 | 指标在同行店铺中的百分位排名，范围 0 到 100。 |
| ^^^rank | int | 1 | 问题排名，1 为最首要的问题。 |
| ^^summary | string | Improve late dispatch and negative reviews to increase your SPS score. | top 问题的本地化摘要。 |
| ^update_time | int | 1761264000 | 最新分数刷新时间。Unix 时间戳（秒）。 |
# 响应示例
```json
{"code":0,"data":{"benefits":[{"benefit_name":"LIVE giveaway","is_unlocked":true,"unlock_score":"4.5"}],"dimensions":[{"name":"Product satisfaction","score":"4.8","status":"EXCELLENT","status_text":"Excellent","weight":"70"}],"evaluate_duration_days":90,"end_evaluation_time":1782518400,"start_evaluation_time":1774828800,"peer_percentile":"86.5","primary_category":{"category_id":"601450","category_name":"Home Supplies"},"sps_score":"4.6","sps_tier":"GOOD","sps_tier_text":"Excellent","top_issues":{"issues":[{"description":"Your on-time delivery performance is lower than peer shops.","evaluate_duration_days":31,"end_evaluation_time":1761264000,"start_evaluation_time":1758672000,"metric_code":"OTDR","metric_name":"On-time delivery rate","percentile":"72.4","rank":1}],"summary":"Improve late dispatch and negative reviews to increase your SPS score."},"update_time":1761264000},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

