# 获取店铺视频表现详情

# Path: /analytics/202509/shop_videos/{video_id}/performance
# Method: [GET]
# 功能描述
返回（请求的）视频的详细 performance metrics。

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
| video_id | string | Y | 7523456789012345678 | 请求 performance 详情的店铺视频 ID。 |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-09-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区。 |
| 在参数名称中，"ge"指"大于或等于"（包含） |  |  |  |  |
开始和结束之间的时间范围不得超过 60 天。 |
end_date_lt |string |Y |2024-09-08 |结束日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区。
在参数名称中，"lt"指"小于"（排除）
开始和结束之间的时间范围不得超过 60 天。 |
granularity |string |N |ALL |数据粒度。
可选值：ALL, 1D
默认值：ALL

* ALL：汇总
* 1D：每日 |
   currency |string |N |USD |目前响应中仅支持本地货币。

可选值：USD, LOCAL
默认值：LOCAL

* USD：美元
* LOCAL：店铺所在地的本地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202509/shop_videos/7523456789012345678/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-09-01&end_date_lt=2024-09-08&granularity=ALL&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^performance | object |  | 视频的总体 performance 数据。 |
| ^^intervals | []object |  | 请求时间范围内的时间间隔数据。每个时间间隔的时间范围由粒度决定。 |
| ^^^start_date | string | 2024-09-01 | 时间间隔的开始日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，包含。 |
| ^^^end_date | string | 2024-09-08 | 时间间隔的结束日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，排除。 |
| ^^^sales | object |  | 销售 performance 数据。 |
| ^^^^overall | object |  | 总体 performance |
| ^^^^^gmv | object |  | 直接从可购物视频下单的订单支付总金额，包括退货和退款。 |
| ^^^^^^amount | string | 230.02 | 对应货币的 GMV 金额。 |
| ^^^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^^gpm | object |  | 平均视频 GPM 是从 1,000 次视频曝光中产生的平均 GMV。 |
| ^^^^^^amount | string | 1.02 | 对应货币的 GPM 金额。 |
| ^^^^^^currency | string | USD | GPM 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^^customers | int | 12 | 直接从可购物视频下单的客户总数。 |
| ^^^^^items_sold | int | 22 | 直接从可购物视频售出的商品总数。 |
| ^^^^^ctr | string | 0.029 | 视频中的商品点击量与视频中所有商品曝光量的比率，以小数表示。 |
| ^^^^^product_impressions | int | 32092 | 所有视频商品的曝光次数 |
| ^^^^^product_clicks | int | 21232 | 视频中的商品点击次数 |
| ^^^^breakdowns | []object |  | 每个时间间隔内商品级别销售 performance 的明细数据。 |
| ^^^^^product_id | string | 19332235 | 链接到此视频的商品 ID |
| ^^^^^gmv | object |  | 该时间间隔内此商品的 GMV（商品交易总额）。 |
| ^^^^^^amount | string | 230.02 | 对应货币的 GMV 金额。 |
| ^^^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^^gpm | object |  | 该时间间隔内每 1,000 次视频曝光为此商品产生的平均 GMV。 |
| ^^^^^^amount | string | 1.02 | 对应货币的 GPM 金额。 |
| ^^^^^^currency | string | USD | GPM 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^^customers | int | 12 | 直接从可购物视频下单的客户总数。 |
| ^^^^^items_sold | int | 22 | 直接从可购物视频售出的商品总数。 |
| ^^^^^ctr | string | 0.029 | 视频中的商品点击次数 / 视频中所有商品的曝光次数 |
| ^^^^^product_impressions | int | 32092 | 所有视频商品的曝光次数 |
| ^^^^^product_clicks | int | 21232 | 视频中的商品点击次数 |
| ^^^traffic | object |  | 视频的流量 performance。 |
| ^^^^views | int | 76649 | 时间间隔内请求视频的观看次数。同一用户的重复观看分别计数。 |
| ^^^^new_followers | int | 11 | 观看视频后新关注您的用户数 |
| ^^^^shares | int | 23 | 用户分享视频的累计次数 |
| ^^^^comments | int | 8 | 用户在视频上留言的累计次数 |
| ^^^^likes | int | 2 | 用户点赞视频的累计次数 |
| ^^viewer_profile | []object |  | 视频的观众画像 |
| ^^^type | string | VIEWERS | 观众画像类型。可选值： |

* NEW_FOLLOWER：观看视频后新关注的观众
* VIEWERS：视频的观众 |
   ^^^gender_distribution |[]object | |观众性别分布 |
   ^^^^gender |string |MALE |观众性别。可选值：
* MALE：男性观众
* FEMALE：女性观众 |
   ^^^^percentage |string |0.349 |此观众画像中对应性别的占比，以小数表示。 |
   ^^^age_distribution |[]object | |观众年龄分布 |
   ^^^^age |string |25-34 |可选值：
* 18-24
* 25-34
* 35-44
* 45-54
* 55+ |
   ^^^^percentage |string |0.293 |此观众画像中对应年龄段的占比，以小数表示。 |
   ^^^country_distribution |[]object | |观众国家/地区分布。 |
   ^^^^country_code |string |MY |观众 TikTok 账号所在的地区。 |
   ^^^^percentage |string |0.993 |此观众画像中对应国家/地区的占比，以小数表示。 |
   ^latest_available_date |string |2024-09-07 |数据就绪的最新日期，本地时区（ISO 8601 格式）。 |

# 响应示例
```json
{"code":0,"data":{"performance":{"intervals":[{"start_date":"2024-09-01","end_date":"2024-09-08","sales":{"overall":{"gmv":{"amount":"230.02","currency":"USD"},"gpm":{"amount":"1.02","currency":"USD"},"customers":12,"items_sold":22,"ctr":"0.029","product_impressions":32092,"product_clicks":21232},"breakdowns":[{"product_id":"19332235","gmv":{"amount":"230.02","currency":"USD"},"gpm":{"amount":"1.02","currency":"USD"},"customers":12,"items_sold":22,"ctr":"0.029","product_impressions":32092,"product_clicks":21232}]},"traffic":{"views":76649,"new_followers":11,"shares":23,"comments":8,"likes":2}}],"viewer_profile":[{"type":"VIEWERS","gender_distribution":[{"gender":"MALE","percentage":"0.349"}],"age_distribution":[{"age":"25-34","percentage":"0.293"}],"country_distribution":[{"country_code":"MY","percentage":"0.993"}]}]},"latest_available_date":"2024-09-07"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 28001022 | 请求参数无效；详情：开始时间或结束时间无效。 |

