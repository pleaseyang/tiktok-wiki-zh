# 获取 SPS 指标

# 路径：/analytics/202606/shop_performances/metrics
# 方法：[GET]
# 功能描述
返回授权店铺的 SPS 指标详情和基准阈值。
店铺绩效分（SPS）反映店铺在 TikTok Shop 上关键运营和服务指标方面的表现。通过集成只读的 SPS API，ISV 可以获取店铺的分数、等级、权益和指标基准，诊断绩效差距，并深入查看与特定问题相关的商品、物流服务商、售后类型、订单或聊天。这使 ISV 能够在其解决方案中嵌入可操作的 performance 洞察，帮助卖家更快地识别问题区域并采取针对性措施来提升店铺表现。仅适用于美国地区店铺。
使用场景指南：[点击此处](https://partner.tiktokshop.com/docv2/page/ph0ccose)

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | BCP 47 区域代码，用于本地化响应文本。如果省略，则从请求上下文中解析默认区域设置。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^metrics | []object |  | 授权店铺的固定完整 SPS 指标集。 |
| ^^benchmarks | object |  | 指标的基准阈值，以 `value_unit` 指定的单位表示。 |
| ^^^excellent_threshold | string | 0.02 | 优秀等级阈值。 |
| ^^^poor_threshold | string | 0.08 | 较差等级阈值。 |
| ^^dimension | string | Product satisfaction | 该指标所属的 SPS 维度。 |
| ^^evaluate_duration_days | int | 30 | 该指标评估周期包含的天数。 |
| ^^end_evaluation_time | int | 1761264000 | 指标评估周期结束时间。Unix 时间戳（秒）。 |
| ^^start_evaluation_time | int | 1758672000 | 指标评估周期开始时间。Unix 时间戳（秒）。 |
| ^^metric_code | string | NRR | 稳定的指标代码。可选值包括 NRR、NBFR、SFCR、OTDR、AHT 和 IM_DSAT。 |
| ^^metric_name | string | 60 天差评率 | 本地化的指标显示名称。 |
| ^^score | string | 4.7 | 指标分数，范围 0 到 5。 |
| ^^status | string | EXCELLENT | 指标状态。可选值包括 EXCELLENT、GOOD、POOR、CRITICAL 和 NIL。 |
| ^^status_text | string | Excellent | 指标状态文本。值如 Excellent、Good、Normal、Attention。 |
| ^^value | string | 0.97 | 指标值。小时数以数值表示；百分比以 0 到 100 的数值表示。 |
| ^^value_unit | string | PERCENT | 指标值的单位。可选值包括 PERCENT 和 HOURS。 |
| ^^top_reason_text | string | Top opportunity | 表示该指标是 SPS 的关键影响因素。 |
# 响应示例
```json
{"code":0,"data":{"metrics":[{"benchmarks":{"excellent_threshold":"0.02","poor_threshold":"0.08"},"dimension":"Product satisfaction","evaluate_duration_days":30,"end_evaluation_time":1761264000,"start_evaluation_time":1758672000,"metric_code":"NRR","metric_name":"60-day negative review rate","score":"4.7","status":"EXCELLENT","status_text":"Excellent","value":"0.97","value_unit":"PERCENT","top_reason_text":"Top opportunity"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

