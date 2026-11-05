# 获取店铺 SKU 表现列表

# Path: /analytics/202509/shop_skus/performance
# Method: [GET]
# 功能描述
返回店铺 SKU 在请求日期范围内的 performance metrics 分页列表。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2026-10-01 | 开始时间（ISO 8601 YYYY-MM-DD 格式），店铺注册时区，包含。 |
| end_date_lt | string | Y | 2026-10-08 | performance 期间的结束日期，排除，店铺注册时区。使用 YYYY-MM-DD 格式。必须晚于 start_date_ge。 |
| page_size | int | N | 10 | 每页记录数。如果省略，默认为 10。最大值：100。 |
| page_token | string | N | cGFnZV9udW1iZXI9MQ== | 标识要获取页码的 token。第一页时省略此参数。后续页传入上一次响应返回的 `next_page_token`，并复用相同的 `start_date_ge`、`end_date_lt`、`sort_field`、`sort_order`、`category_filter`、`product_status_filter`、`product_ids`、`currency` 和 `page_size` 值。 |
| sort_field | string | N | gmv | 排序字段，可选值： |

* gmv（默认）
* sku_orders
* units_sold |
   sort_order |string |N |DESC |排序方向，可选值：
* DESC（默认）
* ASC |
   category_filter |[]string |N |123123,321412 |用于筛选返回的 SKU performance 记录的商品分类 ID 列表。 |
   product_status_filter |string |N |LIVE |按商品状态筛选 SKU。可选值：
* LIVE
* INACTIVE
* ALL（默认） |
   product_ids |[]string |N |123456789,34909989 |按商品 ID 筛选 SKU。如果提供了 product_ids，API 将仅返回指定商品 ID 的 SKU，否则返回店铺的所有 SKU |
   currency |string |N |USD |用于报告 GMV 的货币：
* USD：美元
* LOCAL（默认）：店铺所在地的本地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202509/shop_skus/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2026-10-01&end_date_lt=2026-10-08&page_size=10&page_token=cGFnZV9udW1iZXI9MQ==&sort_field=gmv&sort_order=DESC&category_filter=123123,321412&product_status_filter=LIVE&product_ids=123456789,34909989&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^skus | []object |  | SKU performance metrics 列表。 |
| ^^id | int | 18354627263453 | 返回的 SKU performance 记录中的 SKU ID。 |
| ^^product_id | int | 123456789 | 返回的 SKU 所属的商品 ID。 |
| ^^gmv | object |  | SKU 的总体 GMV（商品交易总额）。 |
| ^^^amount | string | 135.42 | 对应货币的 GMV 金额。 |
| ^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^sku_orders | int | 10 | SKU 的（所有）订单总数 |
| ^^units_sold | int | 10 | SKU 的售出数量 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 如果非空，将此 token 原样作为 `page_token` 传入下次请求，并复用相同的 `start_date_ge`、`end_date_lt`、`page_size`、`sort_field`、`sort_order`、`currency`、`category_filter`、`product_status_filter` 和 `product_ids` 值。对于可选参数，保留每个参数的省略或存在状态。空字符串表示没有更多页面。 |
| ^total_count | int | 20 | 所有页面中符合请求过滤条件的 SKU 总数。 |
| ^latest_available_date | string | 2024-04-07 | 数据就绪的最新日期，本地时区（ISO 8601 格式）。 |
# 响应示例
```json
{"code":0,"data":{"skus":[{"id":18354627263453,"product_id":123456789,"gmv":{"amount":"135.42","currency":"USD"},"sku_orders":10,"units_sold":10}],"next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":20,"latest_available_date":"2024-04-07"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

