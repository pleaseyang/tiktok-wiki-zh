# 获取 SPS 指标 Top 项目

# Path: /analytics/202606/shop_performances/metrics/{metric_code}/top_items
# Method: [GET]
# 功能描述
返回 NRR、NBFR 或 AHT 的 Top 商品，或 OTDR 的 Top 物流服务商。
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
| metric_code | string | Y | NRR | 指标代码，选择返回的 top 项目列表： |

* NRR: 差评商品（`nrr_top_product_items`）。
* NBFR: 退货退款商品（`nbfr_top_product_items`）。
* OTDR: 物流服务商及其准时送达表现（`otdr_logistics_items`）。
* AHT: 商品及其售后处理详情（`aht_aftersales_type_items`）。 |

# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | BCP 47 区域代码，用于本地化响应文本。如果省略，则从请求上下文中解析默认区域设置。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics/NRR/top_items?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^aht_aftersales_type_items | []object |  | AHT 的 top 商品项，包含平均处理时长和 top 售后类型的字段。 |
| ^^handle_duration_hours | string | 18.5 | 平均处理时长（小时）。 |
| ^^product_id | string | 1729592969712207011 | 商品 ID。 |
| ^^product_name | string | Smart Watch | 商品名称。 |
| ^^return_order_count | int | 30 | 退货订单总数。 |
| ^^top_aftersales_type_name | string | Only Refund | TikTok Shop 售后分类返回的 top 售后类型。 |
| ^^top_type_order_count | int | 20 | 与 top 售后类型相关的订单数。 |
| ^^image_url | string | https://example.com/product.jpg | 商品图片 URL。 |
| ^metric_code | string | NRR | 请求中选择的稳定指标代码。可选值：NRR、NBFR、OTDR 或 AHT。 |
| ^nbfr_top_product_items | []object |  | NBFR top 商品项。 |
| ^^product_id | string | 1729592969712207010 | 商品 ID。 |
| ^^product_name | string | Cotton T-Shirt | 商品名称。 |
| ^^return_order_count | int | 8 | 退货或退款订单数。 |
| ^^top_reason_order_count | int | 5 | 与 top 退货或退款原因相关的订单数。 |
| ^^top_return_reasons | []string | ["Item doesn't match description"] | top 退货或退款原因。 |
| ^^image_url | string | https://example.com/product.jpg | 商品图片 URL。 |
| ^nrr_top_product_items | []object |  | NRR top 商品项。 |
| ^^delivered_order_count | int | 300 | 已送达订单总数。 |
| ^^image_url | string | https://example.com/product.jpg | 商品图片 URL。 |
| ^^negative_order_count | int | 12 | 差评订单数。 |
| ^^product_id | string | 1729592969712207008 | 商品 ID。 |
| ^^product_name | string | Wireless Headphones | 商品名称。 |
| ^^top_review_reasons | []string | ["Item doesn't match description"] | top 差评原因。 |
| ^otdr_logistics_items | []object |  | OTDR 物流服务商项。 |
| ^^delivered_order_count | int | 1000 | 已送达订单总数。 |
| ^^logistics_provider | string | TikTok Shipping | 物流服务商名称。 |
| ^^on_time_deliver_order_count | int | 947 | 准时送达的订单数。 |
| ^^on_time_deliver_rate | string | 0.947 | 准时送达率，为 0 到 1 的比率值。 |
| ^total_count | int | 120 | 此响应返回的指标特定列表中的项目数。 |
# 响应示例
```json
{"code":0,"data":{"aht_aftersales_type_items":[{"handle_duration_hours":"18.5","product_id":"1729592969712207011","product_name":"Smart Watch","return_order_count":30,"top_aftersales_type_name":"Only Refund","top_type_order_count":20,"image_url":"https://example.com/product.jpg"}],"metric_code":"NRR","nbfr_top_product_items":[{"product_id":"1729592969712207010","product_name":"Cotton T-Shirt","return_order_count":8,"top_reason_order_count":5,"top_return_reasons":["Item doesn't match description"],"image_url":"https://example.com/product.jpg"}],"nrr_top_product_items":[{"delivered_order_count":300,"image_url":"https://example.com/product.jpg","negative_order_count":12,"product_id":"1729592969712207008","product_name":"Wireless Headphones","top_review_reasons":["Item doesn't match description"]}],"otdr_logistics_items":[{"delivered_order_count":1000,"logistics_provider":"TikTok Shipping","on_time_deliver_order_count":947,"on_time_deliver_rate":"0.947"}],"total_count":120},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

