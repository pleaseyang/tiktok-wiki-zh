# 获取付款

# Path: /finance/202605/payments
# Method: [GET]
# 功能描述
**此 API 目前不适用于东南亚市场。**
根据指定的日期范围检索店铺自动付款记录。
使用返回的列表来验证付款并与卖家银行账户中的交易进行对账。

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
| create_time_lt | int | N | 1687266376 | 筛选付款，仅显示在指定日期和时间之前发起的付款。Unix 时间戳（秒）。 |
| 有关更多使用信息，请参阅 `create_time_ge` 中的说明。 |  |  |  |  |
| page_size | int | N | 20 | 每页返回的结果数量。 |
| 默认值：20 |  |  |  |  |
| 有效范围：[1-100] |  |  |  |  |
| page_token | string | N | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5Oa | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此参数。 |
| sort_field | string | Y | create_time | 返回结果将按指定字段排序。仅支持 `create_time`。 |
| sort_order | string | N | ASC | `sort_field` 参数的排序顺序。 |
| 默认值：ASC |  |  |  |  |
| 可选值： |  |  |  |  |

* ASC：升序
* DESC：降序 |
   create_time_ge |int |N |1687266376 |筛选付款，仅显示在指定日期和时间或之后发生的付款。Unix 时间戳。

**注意：**
`create_time_ge` 和 `create_time_lt` 共同构成创建时间过滤条件。

* 如果填写了 `create_time_ge` 但 `create_time_lt` 为空，则 `create_time_lt` 默认为当前时间。
* 如果填写了 `create_time_lt` 但 `create_time_ge` 为空，则 `create_time_ge` 默认为最早的店铺时间。 |
   sign |string |Y |5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c |由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
   timestamp |int |Y |1623812664 |Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/finance/202605/payments?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&create_time_lt=1687266376&page_size=20&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5Oa&sort_field=create_time&sort_order=ASC&create_time_ge=1687266376
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT | 用于获取分页结果集下一页的不透明 token。如果当前响应未返回所有结果，请在请求的 `page_token` 参数中提供此值。空字符串表示没有下一页。 |
| ^payments | []object |  | 符合查询条件的付款列表。 |
| ^^create_time | int | 1636105796 | 在 TikTok Shop 中发起付款的时间，以 Unix 时间戳（秒）表示。 |
| ^^id | string | 3458767051733897992 | 付款 ID。 |
| ^^status | string | PAID | 付款状态，表示付款是否已转入卖家的银行账户。 |
| 可选值： |  |  |  |

* PAID：付款已转入卖家账户。
* FAILED：付款转账失败。
* PROCESSING：付款正在处理中。 |
   ^^amount |object | |货币兑换后的最终付款金额。 |
   ^^^value |string |100 |最终付款金额。 |
   ^^^currency |string |GBP |兑换货币的 ISO 4217 格式代码。 |
   ^^settlement_amount |object | |货币兑换前的结算金额。 |
   ^^^value |string |130 |结算金额。 |
   ^^^currency |string |GBP |原始货币的 ISO 4217 格式代码。 |
   ^^payment_amount_before_exchange |object | |货币兑换前的原始付款金额。 |
   ^^^value |string |100 |原始付款金额。
   |
   ^^^currency |string |GBP |原始货币的 ISO 4217 格式代码。 |
   ^^exchange_rate |string |1.000000 |汇率，显示六位小数。 |
   ^^paid_time |int |1685548800 |在 TikTok Shop 中完成付款处理的时间，以 Unix 时间戳（秒）表示。没有完成时间时返回 `0`。 |
   ^^bank_account |string |***********1234 |卖家银行账户号（已脱敏），仅显示最后 4 位以保护隐私。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT","payments":[{"create_time":1636105796,"id":"3458767051733897992","status":"PAID","amount":{"value":"100","currency":"GBP"},"settlement_amount":{"value":"130","currency":"GBP"},"payment_amount_before_exchange":{"value":"100","currency":"GBP"},"exchange_rate":"1.000000","paid_time":1685548800,"bank_account":"***********1234"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

