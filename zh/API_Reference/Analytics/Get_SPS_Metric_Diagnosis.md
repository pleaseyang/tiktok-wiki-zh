# 获取 SPS 指标诊断

# Path: /analytics/202606/shop_performances/metrics/{metric_code}/diagnosis
# Method: [GET]
# 功能描述
返回单个 SPS 指标的诊断详情，包括基准阈值、趋势、计算详情和分布详情。
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
# 请求路径参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| metric_code | string | Y | OTDR | 指标代码。可选值：NRR、NBFR、SFCR、OTDR、AHT 和 IM_DSAT。 |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | BCP 47 区域代码，用于本地化响应文本。如果省略，则从请求上下文中解析默认区域设置。 |
| trend_duration_days | int | N | 30 | 回溯指标趋势数据的天数。值必须为 1 到 90。默认值：30。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics/OTDR/diagnosis?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&trend_duration_days=30
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^benchmarks | object |  | 该指标的基准阈值。 |
| ^^excellent_threshold | string | 0.98 | 优秀等级阈值。 |
| ^^poor_threshold | string | 0.80 | 较差等级阈值。 |
| ^calculation_rule | object |  | 用于计算该指标的详情。 |
| ^^denominator_label | string | Delivered orders | 分母标签。 |
| ^^denominator_value | string | 1000 | 分母值。 |
| ^^numerator_label | string | On-time delivered orders | 分子标签。 |
| ^^numerator_value | string | 947 | 分子值。 |
| ^dimension | string | Product satisfaction | 该指标所属的 SPS 维度。 |
| ^distribution_details | []object |  | 该指标的附加分布详情。 |
| ^^count | int | 820 | 分布桶中的项目数。 |
| ^^name | string | Dispatch 24-48 Hours | 分布详情名称。 |
| ^^percent | string | 82.0 | 分布桶中项目的百分比，范围从 0 到 100。 |
| ^evaluate_duration_days | int | 30 | 指标评估周期包含的天数。 |
| ^end_evaluation_time | int | 1761264000 | 指标评估周期结束时间。Unix 时间戳（秒）。 |
| ^start_evaluation_time | int | 1758672000 | 指标评估周期开始时间。Unix 时间戳（秒）。 |
| ^metric_code | string | OTDR | 稳定的指标代码。可选值：NRR、NBFR、SFCR、OTDR、AHT 和 IM_DSAT。 |
| ^score | string | 4.3 | 指标分数，范围从 0 到 5。 |
| ^status | string | GOOD | 指标状态。可选值包括 EXCELLENT、GOOD、POOR、CRITICAL 和 NIL。 |
| ^status_text | string | Excellent | 指标状态文本。值如 Excellent、Good、Normal、Attention。 |
| ^trend | object |  | 所请求回溯范围内的指标趋势。 |
| ^^data_points | []object |  | 指标趋势数据点。 |
| ^^^record_date | string | 20260601 | 趋势日期，格式为 yyyyMMdd。 |
| ^^^value | string | 0.947 | 趋势日期的指标值，使用与 value_unit 相同的单位。 |
| ^value | string | 0.947 | 指标值。比率表示为 0 到 1 的值；百分比表示为 0 到 100 的值。 |
| ^value_unit | string | PERCENT | 指标值的单位。可选值包括 PERCENT 和 HOURS。 |
| ^analyses | []object |  | 所选指标的诊断洞察。 |
| ^^summaries | []string | ["Stable performance. Top 3 issues to address."] | 影响所选指标的汇总原因。 |
| ^^details | []string | Your 30-day on-time delivery rate is only higher than **% of peers, which is hurting your SPS. | 所选指标诊断的详细说明。 |
# 响应示例
```json
{"code":0,"data":{"benchmarks":{"excellent_threshold":"0.98","poor_threshold":"0.80"},"calculation_rule":{"denominator_label":"Delivered orders","denominator_value":"1000","numerator_label":"On-time delivered orders","numerator_value":"947"},"dimension":"Product satisfaction","distribution_details":[{"count":820,"name":"Dispatch 24-48 Hours","percent":"82.0"}],"evaluate_duration_days":30,"end_evaluation_time":1761264000,"start_evaluation_time":1758672000,"metric_code":"OTDR","score":"4.3","status":"GOOD","status_text":"Excellent","trend":{"data_points":[{"record_date":"20260601","value":"0.947"}]},"value":"0.947","value_unit":"PERCENT","analyses":[{"summaries":["Stable performance. Top 3 issues to address."],"details":"Your 30-day on-time delivery rate is only higher than **% of peers, which is hurting your SPS."}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

