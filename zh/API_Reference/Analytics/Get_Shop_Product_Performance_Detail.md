# 获取店铺商品表现详情

# 路径：/analytics/202509/shop_products/{product_id}/performance
# 方法：[GET]
# 功能描述
返回指定商品的详细 performance metrics。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 1732xxxxxxxxxxxxx629 | 请求 performance metrics 的商品 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-04-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区。 |
| 在参数名称中，"ge"指"大于或等于"（包含） |  |  |  |  |
| end_date_lt | string | Y | 2024-04-08 | 请求范围的结束日期，店铺注册时区，ISO 8601 `YYYY-MM-DD` 格式。此日期为排除（exclusive），必须晚于 `start_date_ge`。 |
| granularity | string | N | ALL | 数据粒度。 |
| 可选值：ALL, 1D |  |  |  |  |
| 默认值：ALL |  |  |  |  |

* ALL：汇总
* 1D：每日 |
   currency |string |N |LOCAL |货币。
   可选值：USD, LOCAL
   默认值：LOCAL
* USD：美元
* LOCAL：店铺所在地的本地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202509/shop_products/1732xxxxxxxxxxxxx629/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-04-01&end_date_lt=2024-04-08&granularity=ALL&currency=LOCAL
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^performance | object |  | 商品的总体 performance 数据。 |
| ^^intervals | []object |  | 请求时间范围内的时间间隔数据。每个时间间隔的时间范围由粒度决定。 |
| ^^^start_date | string | 2024-04-01 | 时间间隔的开始日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，包含。 |
| ^^^end_date | string | 2024-04-08 | 时间间隔的结束日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，排除。 |
| ^^^sales | object |  | 时间间隔内的销售 performance。 |
| ^^^^gmv | object |  | GMV（商品交易总额）：选定期间内订单的支付总金额，包括已取消和已退款的订单。 |
| ^^^^^amount | string | 233 | 对应货币的 GMV 金额。 |
| ^^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^orders | int | 23 | 商品的（所有）订单总数。 |
| ^^^^items_sold | int | 23 | 商品的售出数量。 |
| ^^^^breakdowns | []object |  | 销售明细。 |
| ^^^^^content_type | string | LIVE | 销售明细内容类型。 |
| 可选值： |  |  |  |

* VIDEO：视频内容。
* LIVE：直播内容。
* PRODUCT_CARD：商品卡。 |
   ^^^^^sales |object | |对应内容类型的销售数据。 |
   ^^^^^^gmv |object | |GMV（商品交易总额）。 |
   ^^^^^^^amount |string |43 |对应货币的 GMV 金额。 |
   ^^^^^^^currency |string |USD |GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
   ^^^^^^items_sold |int |454 |对应内容类型的售出数量。 |
   ^^^^^^avg_customers |int |34 |每日平均客户数。 |
   ^^^traffic |object | |流量 performance。 |
   ^^^^breakdowns |[]object | |流量明细。 |
   ^^^^^traffic |object | |对应内容类型的流量 performance。 |
   ^^^^^^impressions |int |34 |每次在 Shop Tab 中显示您的商品链接时，计为一次曝光。用户可以点击链接直接访问您的商品详情页。 |
   ^^^^^^page_views |int |43 |选定期间内商品详情页的总浏览量，包括同一用户的多次浏览。 |
   ^^^^^^avg_unique_page_views |int |34 |商品详情页的每日平均独立浏览量。 |
   ^^^^^^ctr |string |0.034 |在 Shop Tab 中看到商品链接后点击的观众百分比。点击次数除以浏览次数。 |
   ^^^^^^avg_conversion_rate |string |0.033 |独立浏览量产生销售的平均百分比。 |
   ^^^^^content_type |string |LIVE |流量明细内容类型。
   可选值：
* VIDEO：视频内容。
* LIVE：直播内容。
* PRODUCT_CARD：商品卡。 |
   ^^^cancel_and_refunds |object | |取消和退款数据 |
   ^^^^returned |int |2 |退货指被退回和退款的商品数量。 |
   ^^^^canceled |int |23 |取消指包含在"未支付"或"待发货"订单中的商品数量。 |
   ^^^^refunded |int |3 |退款指已退款但未退货的商品数量。 |
   ^^^^replacements |int |3 |换货指被退回并更换的商品数量。 |
   ^^ratings |[]object | |所选 start_date_ge 和 end_date_ge 范围内的评分 |
   ^^^stars |string |1_STAR |评星级别。
   可选值：
* 1_STAR：一星评分。
* 2_STAR：二星评分。
* 3_STAR：三星评分。
* 4_STAR：四星评分。
* 5_STAR：五星评分。 |
   ^^^count |int |23 |对应评分的评论数。 |
   ^^^percentage |string |0.23 |对应评分区间内所有商品评论的占比。该值为该区间的评论数除以总评论数，以 0 到 1 的小数返回，保留四位小数。例如，`0.23` 表示 23%。 |
   ^^top_contents |[]object | |从 `start_date_ge`（包含）到 `end_date_lt`（排除）期间与商品相关的内容。
   按 GMV 排序；仅返回前 100 名。 |
   ^^^type |string |LIVE |热门内容类型。
   可选值：
* LIVE：直播内容。
* VIDEO：视频内容。 |
   ^^^contents |[]object | |内容详情 |
   ^^^^content_id |string |2304002883 |LIVE 场次 ID 或视频 ID |
   ^^^^items_sold |int |23 |对应内容中的售出数量。 |
   ^^^^gmv |object | |GMV（商品交易总额）。 |
   ^^^^^amount |string |323 |对应货币的 GMV 金额。 |
   ^^^^^currency |string |GBP |GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
   ^^top_creators |[]object | |从 `start_date_ge`（包含）到 `end_date_lt`（排除）期间与商品相关的达人。
   按 GMV 排序；仅返回前 100 名。 |
   ^^^creator_open_id |string |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |达人的 open id，使用此 open id 识别唯一达人。 |
   ^^^creator_name |string |nick.name |达人个人资料页上显示的名称。 |
   ^^^creator_profile |string |https://www.example.com/images/creator-profile.webp |达人头像的 URL。 |
   ^^^gmv | object | |此达人创造的 GMV。 |
   ^^^^amount |string |2365 |对应货币的 GMV 金额。 |
   ^^^^currency |string |GBP |GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
   ^^^items_sold |int |32 |此达人售出的商品数。 |
   ^latest_available_date |string |2024-04-07 |数据就绪的最新日期，本地时区（ISO 8601 格式）。 |

# 响应示例
```json
{"code":0,"data":{"performance":{"intervals":[{"start_date":"2024-04-01","end_date":"2024-04-08","sales":{"gmv":{"amount":"233","currency":"USD"},"orders":23,"items_sold":23,"breakdowns":[{"content_type":"LIVE","sales":{"gmv":{"amount":"43","currency":"USD"},"items_sold":454,"avg_customers":34}}]},"traffic":{"breakdowns":[{"traffic":{"impressions":34,"page_views":43,"avg_unique_page_views":34,"ctr":"0.034","avg_conversion_rate":"0.033"},"content_type":"LIVE"}]},"cancel_and_refunds":{"returned":2,"canceled":23,"refunded":3,"replacements":3}}],"ratings":[{"stars":"1_STAR","count":23,"percentage":"0.23"}],"top_contents":[{"type":"LIVE","contents":[{"content_id":"2304002883","items_sold":23,"gmv":{"amount":"323","currency":"GBP"}}]}],"top_creators":[{"creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","creator_name":"nick.name","creator_profile":"https://www.example.com/images/creator-profile.webp","gmv":{"amount":"2365","currency":"GBP"},"items_sold":32}]},"latest_available_date":"2024-04-07"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 28001007 | 找不到任何相关数据；详情：未找到商品。请确保您发送的 product_id 属于当前店铺下的有效商品。 |
| 28001022 | 请求参数无效；详情：开始时间或结束时间无效。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

