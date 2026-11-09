# 获取店铺直播表现列表

# 路径：/analytics/202609/shop_lives/performance
# 方法：[GET]
# 功能描述
返回店铺的直播场次列表及相关指标。卖家只能查询自己官方达人账号的直播间 ID 数据。
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
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-09-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），采用店铺注册时区。 |
| 在参数名中，"ge" 表示"大于或等于"（含边界） |  |  |  |  |
| end_date_lt | string | Y | 2024-09-08 | 结束日期（ISO 8601 YYYY-MM-DD 格式），采用店铺注册时区。 |
| 在参数名中，"lt" 表示"小于"（不含边界） |  |  |  |  |
| account_type | string | Y | OFFICIAL_ACCOUNTS | video 创建时的账号类型。 |
| Available values: |  |  |  |  |

* OFFICIAL_ACCOUNTS：官方账号。
* MARKETING_ACCOUNTS：营销账号。
* AFFILIATE_ACCOUNTS: 联盟账户。 |
   page_size |int |N |30 |每页商品数量。
   Max value: 100
   Default value: 10 |
   sort_field |string |N |gmv |排序字段。
   默认值: live_attributed_gmv
   Available values:
* live_attributed_gmv
* products_added
* products_sold
* live_attributed_sku_orders
* live_attributed_items_sold
* attributed_customers |
   sort_order |string |N |ASC |排序方向。
   Available values:
* ASC: 升序。
* DESC: 降序。
   默认值: DESC |
   currency |string |N |USD |货币。
   Available values:
* USD: 美元。
* LOCAL: 店铺所在地的本地货币。
   默认值: LOCAL |
   page_token |string |N |cGFnZV9udW1iZXI9MQ== |分页 token，表示当前位置。用于请求下一页数据。
   首次查询时请留空。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop_lives/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-09-01&end_date_lt=2024-09-08&account_type=OFFICIAL_ACCOUNTS&page_size=30&sort_field=gmv&sort_order=ASC&currency=USD&page_token=cGFnZV9udW1iZXI9MQ==
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-07 | 本地时区下数据已就绪的最新日期（ISO 8601 格式）。 |
| ^live_stream_sessions | []object |  | 直播 performance 指标列表。 |
| ^^creator | object |  | 直播场次的达人信息。 |
| ^^^author_type | string | OFFICIAL | 达人账号类型。 |
| ^^^creator_country | string | US | 达人所在国家或地区代码。 |
| ^^^nick_name | string | abc_bec | 达人昵称。 |
| ^^^open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | 达人的 Open ID。 |
| ^^^user_name | string | creator_shop_01 | 达人用户名。 |
| ^^end_time | string | 1623812864 | LIVE 结束时间，Unix 时间戳 GMT (UTC+00:00)。 |
| ^^id | string | 75xxxxxxxxxxxxxxx28 | LIVE 的 ID |
| ^^interaction_performance | object |  | 仅当账户类型为以下值时返回此对象: |

* OFFICIAL_ACCOUNTS:
* MARKETING_ACCOUNTS |
   ^^^comment_rate |string |0.0047 |评论数与观看量的比率。以原始小数字符串表示。 |
   ^^^comments |int |534 |所选时间段内发布的 LIVE 视频的评论数。 |
   ^^^follow_rate |string |0.0007 |新增关注者与观众的比率。以原始小数字符串表示。 |
   ^^^like_rate |string |0.0216 |点赞数与观看量的比率。以原始小数字符串表示。 |
   ^^^likes |int |2442 |所选时间段内 LIVE 视频获得的点赞数。 |
   ^^^new_followers |int |12 |所选时间段内通过该视频关注达人的观众人数。 |
   ^^^share_rate |string |0.0014 |分享数与观看量的比率。以原始小数字符串表示。 |
   ^^^shares |int |156 |所选时间段内发布的 LIVE 视频被分享的次数。 |
   ^^sales_performance |object | |与店铺相关的 LIVE 销售表现数据 |
   ^^^aov |object | |LIVE 场次的平均订单金额。 |
   ^^^^amount |string |19.80 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^attributed_customers |int |50 |归因于该 LIVE 场次的客户数量。 |
   ^^^avg_live_auction_price |object | |LIVE 竞拍商品每件售出商品的平均价格。 |
   ^^^^amount |string |0.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^avg_price |object | |所有商品实付总价除以售出商品件数。 |
   ^^^^amount |string |9 |所有商品实付总价除以售出商品件数。 |
   ^^^^currency |string |USD |GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，取值将为店铺注册地的本地货币代码（例如 GBP）。 |
   ^^^created_sku_orders |int |100 |所选时间段内创建的订单总数，包括货到付款或 PayLater 待付款的订单。示例：如果客户订购 3 件 SKU A 和 2 件 SKU B，则 SKU 订单数为 2。 |
   ^^^gmv_with_tiktok_coupons |object | |包含 TikTok 优惠券补贴的 GMV。 |
   ^^^^amount |string |105.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^live_attributed_gmv |object | |归因于 LIVE 直播的 GMV。 |
   ^^^^amount |string |99.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^live_attributed_items_sold |int |122 |归因于该 LIVE 场次的售出商品件数。 |
   ^^^live_attributed_orders |int |60 |归因于 LIVE 场次的订单数量。 |
   ^^^live_attributed_sku_orders |int |80 |归因于该 LIVE 场次的已支付 SKU 订单数。 |
   ^^^live_auction_attributed_gmv |object | |归因于 LIVE 竞拍商品的 GMV。 |
   ^^^^amount |string |0.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^live_auction_attributed_items_sold |int |0 |归因于 LIVE 竞拍商品的售出商品数量。 |
   ^^^live_auction_attributed_sku_orders |int |0 |归因于 LIVE 竞拍商品的已支付 SKU 订单数量。 |
   ^^^live_auction_gmv |object | |来自 LIVE 竞拍商品的直接 GMV。 |
   ^^^^amount |string |0.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^live_auction_indirect_gmv |object | |LIVE 竞拍商品产生的间接 GMV。 |
   ^^^^amount |string |0.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^live_gmv |object | |LIVE 直播产生的直接 GMV。 |
   ^^^^amount |string |99.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^live_indirect_gmv |object | |来自 LIVE 场次的间接 GMV。 |
   ^^^^amount |string |0.00 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^payment_rate |string |0.8000 |已支付订单与已创建订单的比率。以原始十进制字符串表示。 |
   ^^^products_sold |int |5 |LIVE 场次中售出的不同商品数量。 |
   ^^start_time |string |1623812664 |LIVE 开始时间，Unix 时间戳 GMT (UTC+00:00)。 |
   ^^title |string |abxxxxx |LIVE 标题 |
   ^^traffic |object | |LIVE 直播的流量效率指标。 |
   ^^^acu |int |123 |平均并发用户数。 |
   ^^^avg_viewing_duration |int |46 |平均观看时长，单位为秒。 |
   ^^^avg_viewing_duration_per_viewer |int |284 |每位观众的平均观看时长，以秒为单位。 |
   ^^^ctor |string |0.0129 |点击下单率. 以原始小数字符串表示。 |
   ^^^ctor_sku_order |string |0.0206 |归因 SKU 订单数与商品点击数之比。以原始小数字符串表示。 |
   ^^^ctr |string |0.0290 |点击率. 以原始小数字符串表示。 |
   ^^^gmv_per_hour |object | |每小时产生的 LIVE 归因 GMV。 |
   ^^^^amount |string |49.50 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^impressions |int |130000 |LIVE 曝光次数。 |
   ^^^impressions_per_hour |int |65000 |每小时平均展示次数。 |
   ^^^live_ctr |string |0.1399 |商品点击量与商品曝光量的比率. 以原始小数字符串表示。 |
   ^^^order_rate_sku_orders |string |0.0044 |归因 SKU 订单与观看量的比率. 以原始小数字符串表示。 |
   ^^^over_1m_live_viewing_rate |string |0.1774 |时长超过一分钟的观看次数占比。以原始小数字符串表示。 |
   ^^^over_1m_views |int |3250 |观看时长超过一分钟的观看次数。 |
   ^^^pcu |int |1332 |峰值并发用户数。 |
   ^^^product_clicks |int |3882 |商品点击次数。 |
   ^^^product_impressions |int |27749 |商品曝光次数。 |
   ^^^products_added |int |12 |添加到 LIVE 场次的商品数量。 |
   ^^^show_gpm |object | |每 1,000 次展示产生的 LIVE 归因 GMV。 |
   ^^^^amount |string |0.76 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^^^tap_through_rate |string |0.8692 |直播观看量与直播曝光量的比率. 以原始小数字符串表示。 |
   ^^^viewers |int |18323 |独立观众数。 |
   ^^^views |int |112993 |LIVE 观看次数。 |
   ^^^watch_gpm |object | |每 1,000 个观看单位产生的 LIVE 归因 GMV。 |
   ^^^^amount |string |0.88 |对应货币的金额。 |
   ^^^^currency |string |USD |货币代码（ISO 4217 标准）。 |
   ^next_page_token |string |cGFnZV9udW1iZXI9MQ== |用于请求下一页的页面令牌。 |
   ^total_count |int |233 |LIVE 直播场次总数。 |
   ^updated_at |string |2026-09-02 21:52:00 |数据在店铺注册时区最后一次更新的时间。 |

# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-07","live_stream_sessions":[{"creator":{"author_type":"OFFICIAL","creator_country":"US","nick_name":"abc_bec","open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","user_name":"creator_shop_01"},"end_time":"1623812864","id":"75xxxxxxxxxxxxxxx28","interaction_performance":{"comment_rate":"0.0047","comments":534,"follow_rate":"0.0007","like_rate":"0.0216","likes":2442,"new_followers":12,"share_rate":"0.0014","shares":156},"sales_performance":{"aov":{"amount":"19.80","currency":"USD"},"attributed_customers":50,"avg_live_auction_price":{"amount":"0.00","currency":"USD"},"avg_price":{"amount":"9","currency":"USD"},"created_sku_orders":100,"gmv_with_tiktok_coupons":{"amount":"105.00","currency":"USD"},"live_attributed_gmv":{"amount":"99.00","currency":"USD"},"live_attributed_items_sold":122,"live_attributed_orders":60,"live_attributed_sku_orders":80,"live_auction_attributed_gmv":{"amount":"0.00","currency":"USD"},"live_auction_attributed_items_sold":0,"live_auction_attributed_sku_orders":0,"live_auction_gmv":{"amount":"0.00","currency":"USD"},"live_auction_indirect_gmv":{"amount":"0.00","currency":"USD"},"live_gmv":{"amount":"99.00","currency":"USD"},"live_indirect_gmv":{"amount":"0.00","currency":"USD"},"payment_rate":"0.8000","products_sold":5},"start_time":"1623812664","title":"abxxxxx","traffic":{"acu":123,"avg_viewing_duration":46,"avg_viewing_duration_per_viewer":284,"ctor":"0.0129","ctor_sku_order":"0.0206","ctr":"0.0290","gmv_per_hour":{"amount":"49.50","currency":"USD"},"impressions":130000,"impressions_per_hour":65000,"live_ctr":"0.1399","order_rate_sku_orders":"0.0044","over_1m_live_viewing_rate":"0.1774","over_1m_views":3250,"pcu":1332,"product_clicks":3882,"product_impressions":27749,"products_added":12,"show_gpm":{"amount":"0.76","currency":"USD"},"tap_through_rate":"0.8692","viewers":18323,"views":112993,"watch_gpm":{"amount":"0.88","currency":"USD"}}}],"next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":233,"updated_at":"2026-09-02 21:52:00"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

