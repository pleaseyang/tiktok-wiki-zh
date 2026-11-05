# 获取店铺表现

# Path: /analytics/202609/shop/performance
# Method: [GET]
# 功能描述
返回店铺/卖家级别的 performance 指标。
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
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-04-01 | Start date (ISO 8601 YYYY-MM-DD format) in shop registered timezone. |
| In the parameter name, "ge" refers to "greater than or equal to" (inclusive) |  |  |  |  |
| end_date_lt | string | Y | 2024-04-08 | End date (ISO 8601 YYYY-MM-DD format) in shop registered timezone. |
| In the parameter name, "lt" refers to "less than" (exclusive) |  |  |  |  |
| granularity | string | N | ALL | Granularity of the data. |
| Available values: ALL, 1D |  |  |  |  |
| Default value: ALL |  |  |  |  |

* ALL: aggregate
* 1D: daily |
   currency |string |N |LOCAL |Currently, only local currency is supported in the response.

Available values: USD, LOCAL
Default value: LOCAL

* USD: US dollars
* LOCAL: local currency where the shop is located |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-04-01&end_date_lt=2024-04-08&granularity=ALL&currency=LOCAL
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-04-07 | Latest date in local timezone where data is ready (ISO 8601 format). |
| ^performance | object |  | Overall performance data for the shop. |
| ^^intervals | []object |  | Interval data for the requested time range. The time range of each interval is determined by the granularity. |
| ^^^breakdowns | object |  | Breakdowns of performance data by content type, channel, and attribution. |
| ^^^^affiliate_product_card_attributed_gmv | object |  | GMV attributed to affiliate product cards. |
| ^^^^^amount | string | 2363.83 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^content_breakdown | []object |  | GMV breakdown by content type and channel. |
| ^^^^^channel | string | CREATOR | Channel type. |
| Possible values: CREATOR, SELLER |  |  |  |
| ^^^^^content_type | string | LIVE | Content type. |
| Possible values: LIVE, VIDEO |  |  |  |
| ^^^^^gmv | object |  | GMV for this content type and channel. |
| ^^^^^^amount | string | 0.00 | GMV amount in the corresponding currency. |
| ^^^^^^currency | string | USD | GMV currency code (ISO 4217 standard). If LOCAL currency is requested, the value will be the local currency code of where the shop is registered (e.g. GBP). |
| ^^^^^indirect_gmv | object |  | Indirect GMV for this content type and channel. |
| ^^^^^^amount | string | 0.00 | GMV amount in the corresponding currency. |
| ^^^^^^currency | string | USD | GMV currency code (ISO 4217 standard). If LOCAL currency is requested, the value will be the local currency code of where the shop is registered (e.g. GBP). |
| ^^^^seller_product_card_gmv | object |  | GMV from seller product cards. |
| ^^^^^amount | string | 2363.83 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^shop_tab_and_search | object |  | Attribution breakdown by shop tab and search. |
| ^^^^^others | object |  | GMV from other attribution sources. |
| ^^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^^search_attributed | object |  | GMV attributed to search. |
| ^^^^^^amount | string | 1484.40 | Amount in the corresponding currency. |
| ^^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^^shop_tab_attributed | object |  | GMV attributed to shop tab. |
| ^^^^^^amount | string | 879.43 | Amount in the corresponding currency. |
| ^^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^end_date | string | 2024-04-08 | End date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered timezone, exclusive. |
| ^^^sales | object |  | Sales performance within the interval. |
| ^^^^avg_order_value | object |  | Average order value during the selected period. |
| ^^^^^amount | string | 2.29 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^avg_sku_order_value | object |  | Average SKU order value during the selected period. |
| ^^^^^amount | string | 2.29 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^cancellations_and_returns | int | 0 | Total number of cancellations and returns during the selected period. |
| ^^^^creator_live_attributed_gmv | object |  | GMV attributed to creator live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^creator_live_gmv | object |  | GMV from creator live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^creator_live_indirect_gmv | object |  | Indirect GMV from creator live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^creator_video_attributed_gmv | object |  | GMV attributed to creator videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^creator_video_gmv | object |  | GMV from creator videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^creator_video_indirect_gmv | object |  | Indirect GMV from creator videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^customers_count | int | 7 | Number of unique users who paid for orders during the selected period. |
| ^^^^gmv | object |  | Gross merchandise value: Total amount paid for orders during the selected period, including canceled and refunded orders. |
| ^^^^^amount | string | 29.71 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^gmv_with_tax | object |  | GMV including tax. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^gmv_with_tiktok_co_funding | object |  | GMV including TikTok co-funding. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^items_sold | int | 13 | The total number of individual items sold. Example: If a customer buys 3 units of SKU A and 2 units of SKU B, the items sold would be 5. |
| ^^^^live_attributed_gmv | object |  | GMV attributed to live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^live_gmv | object |  | GMV from live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^live_indirect_gmv | object |  | Indirect GMV from live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^orders_count | int | 13 | The number of paid orders during the selected period. |
| ^^^^product_card_attributed_gmv | object |  | GMV attributed to product cards. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^refunds | object |  | The amount of order refunds generated. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^seller_live_attributed_gmv | object |  | GMV attributed to seller live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^seller_live_gmv | object |  | GMV from seller live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^seller_live_indirect_gmv | object |  | Indirect GMV from seller live streams. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^seller_video_attributed_gmv | object |  | GMV attributed to seller videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^seller_video_gmv | object |  | GMV from seller videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^seller_video_indirect_gmv | object |  | Indirect GMV from seller videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^shipping_fees | object |  | Total shipping fees during the selected period. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^sku_orders_count | int | 13 | A total count of distinct SKUs sold. |
| ^^^^tax | object |  | Tax amount during the selected period. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^video_attributed_gmv | object |  | GMV attributed to videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^video_gmv | object |  | GMV from videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^^video_indirect_gmv | object |  | Indirect GMV from videos. |
| ^^^^^amount | string | 0.00 | Amount in the corresponding currency. |
| ^^^^^currency | string | USD | Currency code (ISO 4217 standard). |
| ^^^start_date | string | 2024-04-01 | Start date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered timezone, inclusive. |
| ^^^traffic | object |  | Traffic data for the interval. |
| ^^^^avg_conversation_rate | string | 0.3342 | The daily average percentage of unique users who paid for orders after viewing product detail pages during the selected period. |
| ^^^^avg_page_views | int | 56234 | Daily average number of page views for all of your product detail pages during the selected period. |
| ^^^^avg_visitors | int | 3433 | Daily average number of unique users who visited your product detail pages during the selected period |
| ^^^^product_clicks | int | 12654 | Total number of product clicks during the selected period. |
| ^^^^product_impressions | int | 86234 | Total number of product impressions during the selected period. |
| ^^^^unique_clicks | int | 8342 | Total number of unique clicks during the selected period. |
| ^^^^unique_product_impressions | int | 52314 | Total number of unique product impressions during the selected period. |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-04-07","performance":{"intervals":[{"breakdowns":{"affiliate_product_card_attributed_gmv":{"amount":"2363.83","currency":"USD"},"content_breakdown":[{"channel":"CREATOR","content_type":"LIVE","gmv":{"amount":"0.00","currency":"USD"},"indirect_gmv":{"amount":"0.00","currency":"USD"}}],"seller_product_card_gmv":{"amount":"2363.83","currency":"USD"},"shop_tab_and_search":{"others":{"amount":"0.00","currency":"USD"},"search_attributed":{"amount":"1484.40","currency":"USD"},"shop_tab_attributed":{"amount":"879.43","currency":"USD"}}},"end_date":"2024-04-08","sales":{"avg_order_value":{"amount":"2.29","currency":"USD"},"avg_sku_order_value":{"amount":"2.29","currency":"USD"},"cancellations_and_returns":0,"creator_live_attributed_gmv":{"amount":"0.00","currency":"USD"},"creator_live_gmv":{"amount":"0.00","currency":"USD"},"creator_live_indirect_gmv":{"amount":"0.00","currency":"USD"},"creator_video_attributed_gmv":{"amount":"0.00","currency":"USD"},"creator_video_gmv":{"amount":"0.00","currency":"USD"},"creator_video_indirect_gmv":{"amount":"0.00","currency":"USD"},"customers_count":7,"gmv":{"amount":"29.71","currency":"USD"},"gmv_with_tax":{"amount":"0.00","currency":"USD"},"gmv_with_tiktok_co_funding":{"amount":"0.00","currency":"USD"},"items_sold":13,"live_attributed_gmv":{"amount":"0.00","currency":"USD"},"live_gmv":{"amount":"0.00","currency":"USD"},"live_indirect_gmv":{"amount":"0.00","currency":"USD"},"orders_count":13,"product_card_attributed_gmv":{"amount":"0.00","currency":"USD"},"refunds":{"amount":"0.00","currency":"USD"},"seller_live_attributed_gmv":{"amount":"0.00","currency":"USD"},"seller_live_gmv":{"amount":"0.00","currency":"USD"},"seller_live_indirect_gmv":{"amount":"0.00","currency":"USD"},"seller_video_attributed_gmv":{"amount":"0.00","currency":"USD"},"seller_video_gmv":{"amount":"0.00","currency":"USD"},"seller_video_indirect_gmv":{"amount":"0.00","currency":"USD"},"shipping_fees":{"amount":"0.00","currency":"USD"},"sku_orders_count":13,"tax":{"amount":"0.00","currency":"USD"},"video_attributed_gmv":{"amount":"0.00","currency":"USD"},"video_gmv":{"amount":"0.00","currency":"USD"},"video_indirect_gmv":{"amount":"0.00","currency":"USD"}},"start_date":"2024-04-01","traffic":{"avg_conversation_rate":"0.3342","avg_page_views":56234,"avg_visitors":3433,"product_clicks":12654,"product_impressions":86234,"unique_clicks":8342,"unique_product_impressions":52314}}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 28001022 | invalid request params; detail: start time or end time is invalid. |

