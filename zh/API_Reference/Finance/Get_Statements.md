# 获取对账单

# Path: /finance/202309/statements
# Method: [GET]
# 功能描述
根据指定的日期范围或付款状态，检索为店铺生成的账单及关键账单信息。使用此 API 获取一段时间内每日账单的概览，或查看哪些账单已付款、哪些未付款。有关详细交易信息，请参阅 [Get Statement Transactions](650a6749defece02be67da87) 或 [Get Order Statement Transactions](650a6734defece02be67d724)。
适用于所有地区的卖家。仅提供 2023-07-01 之后的数据。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| statement_time_lt | int | N | 1777507200 | 筛选账单，仅显示在指定日期和时间之前生成的账单。Unix 时间戳（秒）。 |
| 有关更多使用信息，请参阅 `statement_time_ge` 中的说明。 |  |  |  |  |
| payment_status | string | N | PAID | 根据付款状态筛选账单。 |
| 可选值： |  |  |  |  |

* PAID：付款已转入卖家账户。
* FAILED：付款转账失败。
* PROCESSING：付款正在处理中。
   默认值：返回所有状态。 |
   page_size |int |N |20 |每页返回的结果数量。
   默认值：20
   有效范围：[1-100] |
   page_token |string |N |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT |用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此参数。 |
   sort_field |string |Y |statement_time |返回结果将按指定字段排序。仅支持 `statement_time`。 |
   sort_order |string |N |ASC |`sort_field` 参数的排序顺序。
   默认值：ASC
   可选值：
* ASC：升序
* DESC：降序 |
   statement_time_ge |int |N |1777420800 |筛选账单，仅显示在指定日期和时间或之后生成的账单。Unix 时间戳（秒）。

**注意：**
`statement_time_ge` 和 `statement_time_lt` 共同定义一个半开的账单生成时间范围：`statement_time_ge` 为包含（inclusive），`statement_time_lt` 为排除（exclusive）。

* 如果提供了 `statement_time_ge` 但未提供 `statement_time_lt`，则 `statement_time_lt` 默认为当前时间。
* 如果提供了 `statement_time_lt` 但未提供 `statement_time_ge`，则 `statement_time_ge` 默认为最早的店铺时间。

**示例：**
账单每天 UTC 00:00 生成，涵盖前一天的交易。要查询 2026 年 4 月 28 日交易生成的账单，请使用精确的账单生成时间间隔 `[2026-04-29T00:00:00Z, 2026-04-30T00:00:00Z)`：

* 将 `statement_time_ge` 设置为 `1777420800`（包含）。
* 将 `statement_time_lt` 设置为 `1777507200`（排除）。 |
   sign |string |Y |5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c |由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
   timestamp |int |Y |1623812664 |Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/finance/202309/statements?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&statement_time_lt=1777507200&payment_status=PAID&page_size=20&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT&sort_field=statement_time&sort_order=ASC&statement_time_ge=1777420800
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT | 用于获取分页结果集下一页的不透明 token。如果此值非空，请在下次请求的 `page_token` 参数中提供。空的 `next_page_token` 表示没有更多结果。 |
| ^statements | []object |  | 符合查询条件的账单列表。 |
| ^^id | string | 7238804564097517339 | 账单 ID。 |
| ^^statement_time | int | 1685548800 | 账单生成时间，以 Unix 时间戳（秒）表示。 |
| 账单每天 UTC 00:00 生成，包含前一天的所有交易。 |  |  |  |
| ^^settlement_amount | string | 100 | 结算金额。 |
| ^^currency | string | GBP | ISO 4217 格式的货币代码。 |
| ^^revenue_amount | string | 200 | 订单结算时的最终收入金额。 |
| 适用于除英国和美国之外的所有地区。 |  |  |  |
| ^^fee_amount | string | -30 | TikTok Shop 在订单结算时收取的费用。订单在发货后一定天数（因地区而异）被视为已结算，前提是没有待处理的退货或退款。 |
**注意**：不含运费相关成本，但东南亚地区的本地卖家除外（含运费相关成本）。 |
^^adjustment_amount |string |-70 |调整金额。
有关调整原因的更多详情，请参阅 [Get Statement Transactions API](https://partner.tiktokshop.com/docv2/page/650a6749defece02be67da87)。 |
^^payment_status |string |PAID |付款状态，表示付款是否已转入卖家的银行账户或已结算到卖家账户。
可选值：

* PAID：付款已转入卖家账户。
* FAILED：付款转账失败。
* PROCESSING：付款正在处理中。
* SETTLED：资金已结算到卖家账户。 |
   ^^payment_id |string |3459275187040258849 |付款 ID。 |
   ^^net_sales_amount |string |-70 |扣除卖家折扣后的最终收入金额。
   仅适用于东南亚地区以外的本地卖家。
   |
   ^^shipping_cost_amount |string |-70 |运费。
   仅适用于东南亚地区以外的本地卖家。
   |
   ^^payment_time |int |1685548800 |付款的 Unix 时间戳
   |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT","statements":[{"id":"7238804564097517339","statement_time":1685548800,"settlement_amount":"100","currency":"GBP","revenue_amount":"200","fee_amount":"-30","adjustment_amount":"-70","payment_status":"PAID","payment_id":"3459275187040258849","net_sales_amount":"-70","shipping_cost_amount":"-70","payment_time":1685548800}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

