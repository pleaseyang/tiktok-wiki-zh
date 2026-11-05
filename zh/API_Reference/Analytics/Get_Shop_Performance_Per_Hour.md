# 获取店铺每小时表现

# Path: /analytics/202510/shop/performance/{date}/performance_per_hour
# Method: [GET]
# 功能描述
返回请求日期的每小时店铺 performance 详情。日期可以是最近 30 天内的任意日期，包括今天。

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
| date | string | Y | 2025-09-18 | （ISO 8601 YYYY-MM-DD 格式）店铺注册时区。 |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| currency | string | N | USD | 货币。 |
| 可选值：USD, LOCAL |  |  |  |  |
| 默认值：LOCAL |  |  |  |  |

* USD：美元
* LOCAL：店铺所在地的本地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202510/shop/performance/2025-09-18/performance_per_hour?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^performance | object |  | 请求日期的店铺 performance 数据，包括每小时的时间间隔、总体汇总和最新可用时间戳。 |
| ^^intervals | []object |  | 请求日期的每小时时间间隔数据，包括小时索引、GMV、客户数、售出商品数和访客数。 |
| ^^^avg_order_value | object |  | 该小时的平均订单价值。 |
| ^^^^amount | string | 2.29 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^avg_sku_order_value | object |  | 该小时的平均 SKU 订单价值。 |
| ^^^^amount | string | 2.29 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^customers | int | 223 | 进行购买的独立客户数。此指标将每位客户计算一次，即使他们进行了多次购买。 |
| ^^^customers_count | int | 7 | 该小时内支付订单的独立用户数。 |
| ^^^gmv | object |  | 该小时时间间隔的 GMV。 |
| ^^^^amount | string | 2332.22 | 对应货币的 GMV 金额。 |
| ^^^^currency | string | SGD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^index | int | 2 | 小时索引，0-23。 |
| 0 表示 00:00 - 00:59。 |  |  |  |
| ^^^items_sold | int | 23 | 售出的独立商品总数。示例：如果一位客户购买了 3 件 SKU A 和 2 件 SKU B，则售出商品数为 5。 |
| ^^^live_attributed_gmv | object |  | 该小时内归因于直播的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^orders_count | int | 13 | 该小时内支付的订单数。 |
| ^^^product_card_attributed_gmv | object |  | 该小时内归因于商品卡的 GMV。 |
| ^^^^amount | string | 29.71 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^product_clicks | int | 12654 | 该小时内的商品点击总数。 |
| ^^^product_impressions | int | 86234 | 该小时内的商品曝光总数。 |
| ^^^sku_orders_count | int | 13 | 该小时内售出的不同 SKU 数量。 |
| ^^^unique_clicks | int | 8342 | 该小时内的独立商品点击总数。 |
| ^^^unique_product_impressions | int | 52314 | 该小时内的独立商品曝光总数。 |
| ^^^video_attributed_gmv | object |  | 该小时内归因于视频的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^visitors | int | 2332 | 在最近更新时间之前访问过商品详情页的独立用户数。 |
| ^^latest_available_timestamp | int | 1623812664 | 数据就绪的最新时间，以 UNIX 时间戳表示。 |
| ^^overall | object |  | 请求日期的汇总店铺 performance 指标。 |
| ^^^avg_order_value | object |  | 请求日期的平均订单价值。 |
| ^^^^amount | string | 2.29 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^avg_sku_order_value | object |  | 请求日期的平均 SKU 订单价值。 |
| ^^^^amount | string | 2.29 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^customers | int | 2332 | 进行购买的独立客户数。此指标将每位客户计算一次，即使他们进行了多次购买。 |
| ^^^customers_count | int | 7 | 请求日期内支付订单的独立用户数。 |
| ^^^gmv | object |  | 客户支付的总金额，包括运费，但扣除平台联合出资和卖家促销。GMV 不扣除取消或退款。 |
| ^^^^amount | string | 2344.00 | 对应货币的 GMV 金额。 |
| ^^^^currency | string | SGD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^items_sold | int | 543 | 售出的独立商品总数。示例：如果一位客户购买了 3 件 SKU A 和 2 件 SKU B，则售出商品数为 5。 |
| ^^^live_attributed_gmv | object |  | 请求日期内归因于直播的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^orders_count | int | 13 | 请求日期内支付的订单数。 |
| ^^^product_card_attributed_gmv | object |  | 请求日期内归因于商品卡的 GMV。 |
| ^^^^amount | string | 29.71 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^product_clicks | int | 12654 | 请求日期内的商品点击总数。 |
| ^^^product_impressions | int | 86234 | 请求日期内的商品曝光总数。 |
| ^^^sku_orders_count | int | 13 | 请求日期内售出的不同 SKU 数量。 |
| ^^^unique_clicks | int | 8342 | 请求日期内的独立商品点击总数。 |
| ^^^unique_product_impressions | int | 52314 | 请求日期内的独立商品曝光总数。 |
| ^^^video_attributed_gmv | object |  | 请求日期内归因于视频的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^visitors | int | 234324 | 在最近更新时间之前访问过商品详情页的独立用户数。 |
# 响应示例
```json
{"code":0,"data":{"performance":{"intervals":[{"avg_order_value":{"amount":"2.29","currency":"USD"},"avg_sku_order_value":{"amount":"2.29","currency":"USD"},"customers":223,"customers_count":7,"gmv":{"amount":"2332.22","currency":"SGD"},"index":2,"items_sold":23,"live_attributed_gmv":{"amount":"0.00","currency":"USD"},"orders_count":13,"product_card_attributed_gmv":{"amount":"29.71","currency":"USD"},"product_clicks":12654,"product_impressions":86234,"sku_orders_count":13,"unique_clicks":8342,"unique_product_impressions":52314,"video_attributed_gmv":{"amount":"0.00","currency":"USD"},"visitors":2332}],"latest_available_timestamp":1623812664,"overall":{"avg_order_value":{"amount":"2.29","currency":"USD"},"avg_sku_order_value":{"amount":"2.29","currency":"USD"},"customers":2332,"customers_count":7,"gmv":{"amount":"2344.00","currency":"SGD"},"items_sold":543,"live_attributed_gmv":{"amount":"0.00","currency":"USD"},"orders_count":13,"product_card_attributed_gmv":{"amount":"29.71","currency":"USD"},"product_clicks":12654,"product_impressions":86234,"sku_orders_count":13,"unique_clicks":8342,"unique_product_impressions":52314,"video_attributed_gmv":{"amount":"0.00","currency":"USD"},"visitors":234324}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

