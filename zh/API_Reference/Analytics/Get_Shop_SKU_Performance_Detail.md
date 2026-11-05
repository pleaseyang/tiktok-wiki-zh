# 获取店铺 SKU 表现详情

# Path: /analytics/202509/shop_skus/{sku_id}/performance
# Method: [GET]
# 功能描述
返回指定 SKU 的 performance metrics。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| sku_id | string | Y | 1732xxxxxxxxxxxxx629 | 请求 performance metrics 的 SKU ID。 |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-04-01 | 开始时间（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，包含。 |
| end_date_lt | string | Y | 2024-04-08 | 结束日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，排除。必须晚于 start_date_ge。 |
| granularity | string | N | ALL | 数据粒度。 |
| 可选值：ALL, 1D |  |  |  |  |
| 默认值：ALL |  |  |  |  |

* ALL：汇总
* 1D：每日 |
   currency |string |N |USD |货币：
* USD：美元
* LOCAL（默认）：店铺所在地的本地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202509/shop_skus/1732xxxxxxxxxxxxx629/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-04-01&end_date_lt=2024-04-08&granularity=ALL&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-04-07 | 数据就绪的最新日期，本地时区（ISO 8601 格式）。 |
| ^performance | object |  | SKU 的总体 performance 数据。 |
| ^^product_id | int | 123456789 | SKU 所属的商品 ID。 |
| ^^sku_id | string | 123456789 | 此 performance 数据的 SKU ID。 |
| ^^intervals | []object |  | 请求时间范围内的时间间隔数据。每个时间间隔的时间范围由粒度决定。 |
| ^^^start_date | string | 2024-04-01 | 时间间隔的开始日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，包含。 |
| ^^^end_date | string | 2024-04-07 | 时间间隔的结束日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，排除。 |
| ^^^gmv | object |  | SKU 的总体 GMV（商品交易总额）。 |
| ^^^^amount | string | 135.42 | 对应货币的 GMV 金额。 |
| ^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^gmv_breakdown | []object |  | SKU 的 GMV 明细。 |
| ^^^^amount | string | 82.15 | 对应类型和货币的 GMV 金额。 |
| ^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^type | string | LIVE | GMV 明细类型。 |
| 可选值： |  |  |  |

* LIVE：直播内容。
* VIDEO：视频内容。
* PRODUCT_CARD：商品卡。 |
   ^^^items_sold |int |10 |SKU 的售出数量。 |
   ^^^items_sold_breakdown |[]object | |售出数量明细。 |
   ^^^^amount |int |10 |对应类型的售出数量。 |
   ^^^^type |string |LIVE |售出明细类型。
   可选值：
* LIVE：直播内容。
* VIDEO：视频内容。
* PRODUCT_CARD：商品卡。 |
   ^^^sku_orders |int |10 |SKU 的（所有）订单总数。 |

# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-04-07","performance":{"product_id":123456789,"sku_id":"123456789","intervals":[{"start_date":"2024-04-01","end_date":"2024-04-07","gmv":{"amount":"135.42","currency":"USD"},"gmv_breakdown":[{"amount":"82.15","currency":"USD","type":"LIVE"}],"items_sold":10,"items_sold_breakdown":[{"amount":10,"type":"LIVE"}],"sku_orders":10}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 28001007 | 找不到任何相关数据；详情：未找到商品。请确保您发送的 product_id 属于当前店铺下的有效商品。 |
| 28001022 | 请求参数无效；详情：开始时间或结束时间无效。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

