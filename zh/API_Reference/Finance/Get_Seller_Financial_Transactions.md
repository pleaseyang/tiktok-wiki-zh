# 获取卖家财务交易

# Path: /finance/202309/withdrawals
# Method: [GET]
# 功能描述
检索卖家财务交易记录，支持可选的创建时间范围筛选，并按必需的交易类型过滤。

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
| create_time_lt | int | N | 1672416002 | Unix 时间戳，表示要请求的交易时间范围的结束时间 |
| types | []string | Y | WITHDRAW,SETTLE | 要返回的交易类型。 |
| 可选值： |  |  |  |  |

* WITHDRAW：卖家将结算金额提现到银行卡。
* SETTLE：平台将金额结算给卖家。
* TRANSFER：因平台政策产生的平台补贴或扣款。
* REVERSE：因银行卡信息错误导致的提现失败。
* PAYMENT：付款交易。
* REFUND：退款交易。 |
   page_size |int |N |20 |默认值为 20，必须为正整数，范围为 1-100 |
   page_token |string |N |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT |上一次响应返回的 `next_page_token`。请求第一页时省略此参数。分页时，在第一次请求中指定 `create_time_ge` 和 `create_time_lt`，然后在每一页中复用相同的 `types`、`create_time_ge` 和 `create_time_lt` 值。 |
   create_time_ge |int |N |1623812664 |Unix 时间戳，表示要请求的交易时间范围的起始时间 |
   sign |string |Y |5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c |由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
   timestamp |int |Y |1623812664 |Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/finance/202309/withdrawals?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&create_time_lt=1672416002&types=WITHDRAW,SETTLE&page_size=20&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT&create_time_ge=1623812664
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT | 用于搜索更多信息的游标 |
|  |  |  |  |
| ^total_count | int | 1 | 提现总数 |
| ^withdrawals | []object |  | 与请求过滤条件匹配的交易记录列表。 |
| ^^id | string | EFASDFSAFDA23432DFAFDSA | TikTok Shop 生成的唯一交易 ID。 |
| ^^type | string | WITHDRAW | 交易类型。 |
| 可选值： |  |  |  |

* WITHDRAW：卖家将结算金额提现到银行卡。
* SETTLE：平台将金额结算给卖家。
* TRANSFER：因平台政策产生的平台补贴或扣款。
* REVERSE：因银行卡信息错误导致的提现失败。
* POLICY_VIOLATION_DEDUCTION：因违反政策的扣款。
* REWARD：奖励交易。
* PAYMENT：付款交易。
* REFUND：退款交易。
* UNKNOWN：无法识别的交易类型。 |
   ^^amount |string |100 |交易金额，使用 currency 指定的货币。 |
   ^^currency |string |IDR |交易金额的三字母 ISO 4217 货币代码。 |
   ^^status |string |PROCESSING |交易的处理状态。
   可选值：
* SUCCESS：交易成功完成。对于 WITHDRAW 交易，这意味着提现已转入卖家账户。
* INIT：提现已初始化。此状态仅适用于 WITHDRAW 交易。
* ORDERED：交易订单已创建。
* PROCESSING：提现正在处理中。
* RECEIVED：提现已收到。
* PROCESSED：付款成功完成。
* FAILED：付款失败。
* REVERSED：交易已退款。
* EXCEPTION：交易已部分退款。
* CLOSED：交易已关闭。
* UNKNOWN：状态无法映射。 |
   ^^create_time |int |1623812664 |交易创建时间，以 Unix 时间戳（秒）表示。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT","total_count":1,"withdrawals":[{"id":"EFASDFSAFDA23432DFAFDSA","type":"WITHDRAW","amount":"100","currency":"IDR","status":"PROCESSING","create_time":1623812664}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 22005007 | 指定的商户不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

