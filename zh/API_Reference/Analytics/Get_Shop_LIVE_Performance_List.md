# 获取店铺直播表现列表

# Path: /analytics/202609/shop_lives/performance
# Method: [GET]
# 功能描述
返回店铺的直播场次列表及相关指标。卖家只能查询自己官方达人账号的直播间 ID 数据。
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
| start_date_ge | string | Y | 2024-09-01 | Start date (ISO 8601 YYYY-MM-DD format) in shop registered timezone. |
| In the parameter name, "ge" refers to "greater than or equal to" (inclusive) |  |  |  |  |
| end_date_lt | string | Y | 2024-09-08 | End date (ISO 8601 YYYY-MM-DD format) in shop registered timezone. |
| In the parameter name, "lt" refers to "less than" (exclusive) |  |  |  |  |
| account_type | string | Y | OFFICIAL_ACCOUNTS | video 创建时的账号类型。 |
| Available values: |  |  |  |  |

* OFFICIAL_ACCOUNTS: Official accounts.
* MARKETING_ACCOUNTS: Marketing accounts.
* AFFILIATE_ACCOUNTS: Affiliate accounts. |
   page_size |int |N |30 |每页商品数量。
   Max value: 100
   Default value: 10 |
   sort_field |string |N |gmv |排序字段。
   Default: live_attributed_gmv
   Available values:
* live_attributed_gmv
* products_added
* products_sold
* live_attributed_sku_orders
* live_attributed_items_sold
* attributed_customers |
   sort_order |string |N |ASC |排序方向。
   Available values:
* ASC: Ascending order.
* DESC: Descending order.
   Default value: DESC |
   currency |string |N |USD |货币。
   Available values:
* USD: US dollars.
* LOCAL: Local currency where the shop is located.
   Default value: LOCAL |
   page_token |string |N |cGFnZV9udW1iZXI9MQ== |分页 token，表示当前位置。用于请求下一页数据。
   首次查询时请留空。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop_lives/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-09-01&end_date_lt=2024-09-08&account_type=OFFICIAL_ACCOUNTS&page_size=30&sort_field=gmv&sort_order=ASC&currency=USD&page_token=cGFnZV9udW1iZXI9MQ==
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-07 | Latest date in local timezone where data is ready (ISO 8601 format). |
| ^live_stream_sessions | []object |  | 直播 performance 指标列表。 |
| ^^creator | object |  | 直播场次的达人信息。 |
| ^^^author_type | string | OFFICIAL | 达人账号类型。 |
| ^^^creator_country | string | US | 达人所在国家或地区代码。 |
| ^^^nick_name | string | abc_bec | 达人昵称。 |
| ^^^open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | 达人的 Open ID。 |
| ^^^user_name | string | creator_shop_01 | 达人用户名。 |
| ^^end_time | string | 1623812864 | LIVE 结束时间，Unix 时间戳 GMT (UTC+00:00)。 |
| ^^id | string | 75xxxxxxxxxxxxxxx28 | LIVE 的 ID |
| ^^interaction_performance | object |  | This object will return only when the account type is: |

* OFFICIAL_ACCOUNTS:
* MARKETING_ACCOUNTS |
   ^^^comment_rate |string |0.0047 |Ratio of comments to views. Expressed as a raw decimal string. |
   ^^^comments |int |534 |Number of comments on the LIVE video posted during the selected period. |
   ^^^follow_rate |string |0.0007 |Ratio of new followers to viewers. Expressed as a raw decimal string. |
   ^^^like_rate |string |0.0216 |Ratio of likes to views. Expressed as a raw decimal string. |
   ^^^likes |int |2442 |The number of likes a LIVE video received during the selected time period. |
   ^^^new_followers |int |12 |The number of viewers who followed creators from the video during the selected period. |
   ^^^share_rate |string |0.0014 |Ratio of shares to views. Expressed as a raw decimal string. |
   ^^^shares |int |156 |Number of times the LIVE video posted during the selected period were shared. |
   ^^sales_performance |object | |Sale performance data of the LIVE related to the shop |
   ^^^aov |object | |Average order value for the LIVE session. |
   ^^^^amount |string |19.80 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^attributed_customers |int |50 |Number of customers attributed to the LIVE session. |
   ^^^avg_live_auction_price |object | |Average price per item sold for LIVE auction products. |
   ^^^^amount |string |0.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^avg_price |object | |The total price paid for all items divided by the number of items sold. |
   ^^^^amount |string |9 |The average price paid for all items divided by the number of items sold. |
   ^^^^currency |string |USD |GMV currency code (ISO 4217 standard). If LOCAL currency is requested, the value will be the local currency code of where the shop is registered (e.g. GBP). |
   ^^^created_sku_orders |int |100 |The total number of orders created during the selected period, including those with pending payment for cash-on-delivery or PayLater. Example: If a customer orders 3 units of SKU A and 2 units of SKU B, the SKU orders would be 2. |
   ^^^gmv_with_tiktok_coupons |object | |GMV including TikTok coupon funding. |
   ^^^^amount |string |105.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^live_attributed_gmv |object | |GMV attributed to the LIVE session. |
   ^^^^amount |string |99.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^live_attributed_items_sold |int |122 |Number of items sold attributed to the LIVE session. |
   ^^^live_attributed_orders |int |60 |Number of orders attributed to the LIVE session. |
   ^^^live_attributed_sku_orders |int |80 |Number of paid SKU orders attributed to the LIVE session. |
   ^^^live_auction_attributed_gmv |object | |GMV attributed to LIVE auction products. |
   ^^^^amount |string |0.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^live_auction_attributed_items_sold |int |0 |Number of items sold attributed to LIVE auction products. |
   ^^^live_auction_attributed_sku_orders |int |0 |Number of paid SKU orders attributed to LIVE auction products. |
   ^^^live_auction_gmv |object | |Direct GMV generated from LIVE auction products. |
   ^^^^amount |string |0.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^live_auction_indirect_gmv |object | |Indirect GMV generated from LIVE auction products. |
   ^^^^amount |string |0.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^live_gmv |object | |Direct GMV generated from the LIVE session. |
   ^^^^amount |string |99.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^live_indirect_gmv |object | |Indirect GMV generated from the LIVE session. |
   ^^^^amount |string |0.00 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^payment_rate |string |0.8000 |Ratio of paid orders to created orders. Expressed as a raw decimal string. |
   ^^^products_sold |int |5 |Number of distinct products sold from the LIVE session. |
   ^^start_time |string |1623812664 |LIVE 开始时间，Unix 时间戳 GMT (UTC+00:00)。 |
   ^^title |string |abxxxxx |LIVE 标题 |
   ^^traffic |object | |Traffic efficiency metrics for the LIVE session. |
   ^^^acu |int |123 |Average concurrent users. |
   ^^^avg_viewing_duration |int |46 |Average viewing duration in seconds. |
   ^^^avg_viewing_duration_per_viewer |int |284 |Average viewing duration per viewer in seconds. |
   ^^^ctor |string |0.0129 |Click-to-order rate. Expressed as a raw decimal string. |
   ^^^ctor_sku_order |string |0.0206 |Ratio of attributed SKU orders to product clicks. Expressed as a raw decimal string. |
   ^^^ctr |string |0.0290 |Click-through rate. Expressed as a raw decimal string. |
   ^^^gmv_per_hour |object | |LIVE-attributed GMV generated per hour. |
   ^^^^amount |string |49.50 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^impressions |int |130000 |Number of LIVE impressions. |
   ^^^impressions_per_hour |int |65000 |Average number of impressions per hour. |
   ^^^live_ctr |string |0.1399 |Ratio of product clicks to product impressions. Expressed as a raw decimal string. |
   ^^^order_rate_sku_orders |string |0.0044 |Ratio of attributed SKU orders to views. Expressed as a raw decimal string. |
   ^^^over_1m_live_viewing_rate |string |0.1774 |Ratio of views lasting longer than one minute. Expressed as a raw decimal string. |
   ^^^over_1m_views |int |3250 |Number of views lasting longer than one minute. |
   ^^^pcu |int |1332 |Peak concurrent users. |
   ^^^product_clicks |int |3882 |Number of product clicks. |
   ^^^product_impressions |int |27749 |Number of product impressions. |
   ^^^products_added |int |12 |Number of products added to the LIVE session. |
   ^^^show_gpm |object | |LIVE-attributed GMV generated per 1,000 impressions. |
   ^^^^amount |string |0.76 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^^^tap_through_rate |string |0.8692 |Ratio of LIVE views to LIVE impressions. Expressed as a raw decimal string. |
   ^^^viewers |int |18323 |Number of unique viewers. |
   ^^^views |int |112993 |Number of LIVE views. |
   ^^^watch_gpm |object | |LIVE-attributed GMV generated per 1,000 watch units. |
   ^^^^amount |string |0.88 |Amount in the corresponding currency. |
   ^^^^currency |string |USD |Currency code (ISO 4217 standard). |
   ^next_page_token |string |cGFnZV9udW1iZXI9MQ== |Page token for the next page request. |
   ^total_count |int |233 |Total number of LIVE stream sessions. |
   ^updated_at |string |2026-09-02 21:52:00 |Time when the data was last updated in shop registered timezone. |

# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-07","live_stream_sessions":[{"creator":{"author_type":"OFFICIAL","creator_country":"US","nick_name":"abc_bec","open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","user_name":"creator_shop_01"},"end_time":"1623812864","id":"75xxxxxxxxxxxxxxx28","interaction_performance":{"comment_rate":"0.0047","comments":534,"follow_rate":"0.0007","like_rate":"0.0216","likes":2442,"new_followers":12,"share_rate":"0.0014","shares":156},"sales_performance":{"aov":{"amount":"19.80","currency":"USD"},"attributed_customers":50,"avg_live_auction_price":{"amount":"0.00","currency":"USD"},"avg_price":{"amount":"9","currency":"USD"},"created_sku_orders":100,"gmv_with_tiktok_coupons":{"amount":"105.00","currency":"USD"},"live_attributed_gmv":{"amount":"99.00","currency":"USD"},"live_attributed_items_sold":122,"live_attributed_orders":60,"live_attributed_sku_orders":80,"live_auction_attributed_gmv":{"amount":"0.00","currency":"USD"},"live_auction_attributed_items_sold":0,"live_auction_attributed_sku_orders":0,"live_auction_gmv":{"amount":"0.00","currency":"USD"},"live_auction_indirect_gmv":{"amount":"0.00","currency":"USD"},"live_gmv":{"amount":"99.00","currency":"USD"},"live_indirect_gmv":{"amount":"0.00","currency":"USD"},"payment_rate":"0.8000","products_sold":5},"start_time":"1623812664","title":"abxxxxx","traffic":{"acu":123,"avg_viewing_duration":46,"avg_viewing_duration_per_viewer":284,"ctor":"0.0129","ctor_sku_order":"0.0206","ctr":"0.0290","gmv_per_hour":{"amount":"49.50","currency":"USD"},"impressions":130000,"impressions_per_hour":65000,"live_ctr":"0.1399","order_rate_sku_orders":"0.0044","over_1m_live_viewing_rate":"0.1774","over_1m_views":3250,"pcu":1332,"product_clicks":3882,"product_impressions":27749,"products_added":12,"show_gpm":{"amount":"0.76","currency":"USD"},"tap_through_rate":"0.8692","viewers":18323,"views":112993,"watch_gpm":{"amount":"0.88","currency":"USD"}}}],"next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":233,"updated_at":"2026-09-02 21:52:00"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

