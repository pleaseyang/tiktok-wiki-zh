# 获取店铺 video 商品表现列表

# 路径：/analytics/202509/shop_videos/{video_id}/products/performance
# 方法：[GET]
# 功能描述
返回给定视频中推广的商品列表的 performance metrics。

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
| video_id | string | Y | 752xxxxxxxxxxxxxxx42 | 请求推广商品 performance 列表的店铺视频 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| end_date_lt | string | Y | 2024-09-08 | 结束日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区。必须晚于 start_date_ge。 |
| 在参数名称中，"lt"指"小于"（排除） |  |  |  |  |
| page_size | int | N | 10 | 每页商品数。 |
| 最小值：1 |  |  |  |  |
| 最大值：100 |  |  |  |  |
| 默认值：10 |  |  |  |  |
| sort_field | string | N | gmv | 排序字段。 |
| 可选值：gmv, units_sold, daily_avg_buyers |  |  |  |  |
| 默认值：gmv |  |  |  |  |
| sort_order | string | N | DESC | 排序方向。 |
| 可选值：ASC, DESC |  |  |  |  |
| 默认值：DESC |  |  |  |  |

* ASC：升序
* DESC：降序 |
   currency |string |N |USD |货币。
   可选值：USD, LOCAL
   默认值：LOCAL
* USD：美元
* LOCAL：店铺所在地的本地货币 |
   page_token |string |N |cGFnZV9udW1iZXI9MQ== |分页 token，表示当前位置。用于请求下一页数据。
   首次查询时留空。 |
   start_date_ge |string |Y |2024-09-01 |开始日期（ISO 8601 YYYY-MM-DD 格式），店铺注册时区。
   在参数名称中，"ge"指"大于或等于"（包含） |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202509/shop_videos/752xxxxxxxxxxxxxxx42/products/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&end_date_lt=2024-09-08&page_size=10&sort_field=gmv&sort_order=DESC&currency=USD&page_token=cGFnZV9udW1iZXI9MQ==&start_date_ge=2024-09-01
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-07 | 数据就绪的最新日期，本地时区（ISO 8601 格式）。 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 下一页请求的分页 token。如果此值非空，请将其作为 `page_token` 传入下次请求，并复用相同的 `video_id`、`start_date_ge`、`end_date_lt`、`sort_field`、`sort_order`、`currency` 和 `page_size` 值。空值表示没有更多页面。 |
| ^products | []object |  | 商品 performance metrics 列表。 |
| ^^ctr | string | 0 | 商品点击量与商品曝光量的比率，以原始小数格式表示。 |
| ^^customers | int | 0 | 购买该商品的客户数。 |
| ^^daily_avg_buyers | string | 0 | 当前商品的每日平均买家数。 |
| ^^gmv | object |  | 商品的总体 GMV（商品交易总额）。 |
| ^^^amount | string | 0 | 对应货币的 GMV 金额。 |
| ^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^gpm | object |  | 每 1,000 次商品曝光产生的平均 GMV。 |
| ^^^amount | string | 0 | 对应货币的 GPM 金额。 |
| ^^^currency | string | USD | GPM 货币代码（ISO 4217 标准）。 |
| ^^id | string | 105xxxxxxxxxxxxx247 | 视频中推广的商品 ID。 |
| ^^name | string | Product Name | 视频中推广的商品名称。 |
| ^^product_clicks | int | 0 | 商品点击次数。 |
| ^^product_impressions | int | 0 | 商品曝光次数。 |
| ^^units_sold | int | 0 | 当前商品的售出数量。 |
| ^total_count | int | 10 | 所有页面中符合请求的商品总数。 |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-07","next_page_token":"cGFnZV9udW1iZXI9MQ==","products":[{"ctr":"0","customers":0,"daily_avg_buyers":"0","gmv":{"amount":"0","currency":"USD"},"gpm":{"amount":"0","currency":"USD"},"id":"105xxxxxxxxxxxxx247","name":"Product Name","product_clicks":0,"product_impressions":0,"units_sold":0}],"total_count":10},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 28001022 | 请求参数无效；详情：开始时间或结束时间无效。 |

