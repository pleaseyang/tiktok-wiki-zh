# 获取 SPS 指标问题详情

# 路径：/analytics/202606/shop_performances/metrics/{metric_code}/problem_details
# 方法：[GET]
# 功能描述
返回所选 SPS 指标的问题订单或聊天详情。
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
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| metric_code | string | Y | NRR | 指标代码。可选值：NRR、NBFR、SFCR、OTDR、AHT 和 IM_DSAT。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | BCP 47 区域代码，用于本地化响应文本。如果省略，则从请求上下文中解析默认区域设置。 |
| page_token | string | N | 2 | 首页请留空此参数。后续页面请将上一次响应返回的不透明 `next_page_token` 原样传入，并使用相同的 `page_size`。 |
| page_size | int | N | 10 | 每页返回的结果数。最小值为 1。默认值为 10。最大值为 50。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics/NRR/problem_details?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&page_token=2&page_size=10
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^aht_problem_order_items | []object |  | AHT 问题订单项。 |
| ^^aftersales_type_name | string | Only Return | TikTok Shop 售后分类返回的售后类型。 |
| ^^approve_duration_hours | string | 12.5 | 审批时长（小时）。 |
| ^^inspect_duration_hours | string | 30.0 | 检验时长（小时）。 |
| ^^order_id | string | 576461413038785752 | 订单 ID。 |
| ^^return_order_id | string | 576461413038785753 | 退货订单 ID。 |
| ^^review_count | int | 2 | 审核轮次。 |
| ^^total_handle_duration_hours | string | 42.5 | 售后处理总时长（小时）。 |
| ^im_dsat_chat_items | []object |  | IM_DSAT 聊天会话项。 |
| ^^chat_duration_hours | string | 1.5 | 聊天时长（小时）。 |
| ^^chat_record_id | string | 745961413038785752 | 聊天记录 ID。 |
| ^^customer_name | string | J*** D*** | 脱敏后的客户名称。 |
| ^^customer_rating | int | 2 | 客户评分，范围 1 到 5。 |
| ^^first_reply_time | int | 1761264060 | 首次回复时间。Unix 时间戳（秒）。 |
| ^^rating_reasons | []string | ["other"] | 客户评分原因。 |
| ^^service_agent | string | Agent A | 服务客服名称。 |
| ^metric_code | string | NRR | 稳定的指标代码。可选值：NRR、NBFR、SFCR、OTDR、AHT 和 IM_DSAT。 |
| ^nbfr_problem_order_items | []object |  | NBFR 问题订单项。 |
| ^^deliver_time | int | 1761523200 | 送达时间。Unix 时间戳（秒）。 |
| ^^order_create_time | int | 1761264000 | 订单创建时间。Unix 时间戳（秒）。 |
| ^^order_id | string | 576461413038785752 | 订单 ID。 |
| ^^product_id | string | 1729592969712207010 | 商品 ID（如有）。 |
| ^^product_name | string | Cotton T-Shirt | 商品名称。 |
| ^^return_refund_reason | string | Wrong size | 退货或退款原因。 |
| ^^sku_id | string | 1729592969712207013 | SKU ID。 |
| ^next_page_token | string | 2 | 用于获取分页结果集下一页的不透明 token。当没有更多结果时返回空字符串。 |
| ^nrr_problem_order_items | []object |  | NRR 问题订单项。 |
| ^^deliver_time | int | 1761523200 | 送达时间。Unix 时间戳（秒）。 |
| ^^order_create_time | int | 1761264000 | 订单创建时间。Unix 时间戳（秒）。 |
| ^^order_id | string | 576461413038785752 | 订单 ID。 |
| ^^product_id | string | 1729592969712207008 | 商品 ID（如有）。 |
| ^^product_name | string | Wireless Headphones | 商品名称。 |
| ^^sku_id | string | 1729592969712207012 | SKU ID。 |
| ^^user_review_rating | int | 2 | 用户评价评分，范围 1 到 5。 |
| ^otdr_problem_order_items | []object |  | OTDR 问题订单项。 |
| ^^actual_deliver_time | int | 1761609600 | 实际送达时间。Unix 时间戳（秒）。 |
| ^^expect_deliver_time | int | 1761523200 | 预计送达时间。Unix 时间戳（秒）。 |
| ^^order_id | string | 576461413038785752 | 订单 ID。 |
| ^^product_name | string | Wireless Headphones | 商品名称。 |
| ^^sku_id | string | 1729592969712207014 | SKU ID。 |
| ^sfcr_problem_order_items | []object |  | SFCR 问题订单项。 |
| ^^cancellation_reasons | []string | ["Defective item"] | 取消原因。 |
| ^^order_create_time | int | 1761264000 | 订单创建时间。Unix 时间戳（秒）。 |
| ^^order_id | string | 576461413038785752 | 订单 ID。 |
| ^^product_id | string | 1729592969712207011 | 商品 ID（如有）。 |
| ^^product_name | string | Smart Watch | 商品名称。 |
| ^^sku_id | string | 1729592969712207014 | SKU ID。 |
| ^total_count | int | 200 | 可用记录总数。 |
# 响应示例
```json
{"code":0,"data":{"aht_problem_order_items":[{"aftersales_type_name":"Only Return","approve_duration_hours":"12.5","inspect_duration_hours":"30.0","order_id":"576461413038785752","return_order_id":"576461413038785753","review_count":2,"total_handle_duration_hours":"42.5"}],"im_dsat_chat_items":[{"chat_duration_hours":"1.5","chat_record_id":"745961413038785752","customer_name":"J*** D***","customer_rating":2,"first_reply_time":1761264060,"rating_reasons":["other"],"service_agent":"Agent A"}],"metric_code":"NRR","nbfr_problem_order_items":[{"deliver_time":1761523200,"order_create_time":1761264000,"order_id":"576461413038785752","product_id":"1729592969712207010","product_name":"Cotton T-Shirt","return_refund_reason":"Wrong size","sku_id":"1729592969712207013"}],"next_page_token":"2","nrr_problem_order_items":[{"deliver_time":1761523200,"order_create_time":1761264000,"order_id":"576461413038785752","product_id":"1729592969712207008","product_name":"Wireless Headphones","sku_id":"1729592969712207012","user_review_rating":2}],"otdr_problem_order_items":[{"actual_deliver_time":1761609600,"expect_deliver_time":1761523200,"order_id":"576461413038785752","product_name":"Wireless Headphones","sku_id":"1729592969712207014"}],"sfcr_problem_order_items":[{"cancellation_reasons":["Defective item"],"order_create_time":1761264000,"order_id":"576461413038785752","product_id":"1729592969712207011","product_name":"Smart Watch","sku_id":"1729592969712207014"}],"total_count":200},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

