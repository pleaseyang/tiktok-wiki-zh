# 获取 TradeIn 账户交易

# Path: /finance/202609/account_transactions
# Method: [GET]
# 功能描述
检索当前授权的 TradeIn 供应商的账户交易记录。
供应商身份和关联的卖家身份从授权上下文中解析。调用方不能指定 seller_id。
仅返回由 TradeIn 业务产生的账户交易。

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
| start_time | string | N | 2026-09-01T00:00:00Z | 筛选在此时间或之后创建的账户交易。使用带时区的 RFC 3339 格式。 |
| end_time | string | N | 2026-10-01T00:00:00Z | 筛选在此时间之前创建的账户交易。使用带时区的 RFC 3339 格式。 |
| flow_type | string | N | RECHARGE | 按业务交易类型筛选账户交易。允许值：RECHARGE、WITHDRAW、REVERSE。如果省略，则返回所有支持的交易类型。 |
| page_size | int | Y | 20 | 每页返回的账户交易数量。 |
| page_token | string | N | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmqN5M1kHYcZmtRyv9aVrNv65W7Q6tFA | 上一次请求返回的不透明 token。请求第一页时省略此参数。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/finance/202609/account_transactions?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_time=2026-09-01T00:00:00Z&end_time=2026-10-01T00:00:00Z&flow_type=RECHARGE&page_size=20&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmqN5M1kHYcZmtRyv9aVrNv65W7Q6tFA
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^flows | []object |  | 符合查询条件的 TradeIn 账户交易。没有匹配的交易时返回空数组。 |
| ^^amount | object |  | 交易金额和货币。使用 direction 判断交易是入账还是出账。 |
| ^^^amount | string | 125.50 | 以十进制字符串表示的交易金额。 |
| ^^^currency | string | USD | ISO 4217 格式的货币代码。 |
| ^^create_time | string | 2026-09-01T10:15:30Z | 账户交易的创建时间，RFC 3339 格式。 |
| ^^direction | string | IN | 账户交易的方向。 |

* IN：资金记入供应商账户。
* OUT：资金从供应商账户扣除。 |
   ^^origin_transaction_id |string |7894561230123456001 |与冲正交易关联的原始账户交易 ID。此字段仅在 REVERSE 交易可用时返回。 |
   ^^reference_id |string |TI202609010001 |与账户交易关联的 TradeIn 业务订单 ID。 |
   ^^transaction_id |string |7894561230123456789 |账户交易的唯一 ID。 |
   ^^type |string |RECHARGE |TradeIn 业务交易类型。
* RECHARGE：通过充值入账的资金。
* WITHDRAW：通过付款出账的资金。
* REVERSE：付款冲正后退回的资金。 |
   ^has_more |bool |true |是否有更多账户交易可用。 |
   ^next_page_token |string |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmqN5M1kHYcZmtRyv9aVrNv65W7Q6tFA |用于获取下一页的不透明 token。没有更多账户交易可用时，该值为空。 |
   ^total_count |int |100 |符合查询条件的账户交易总数。 |

# 响应示例
```json
{"code":0,"data":{"flows":[{"amount":{"amount":"125.50","currency":"USD"},"create_time":"2026-09-01T10:15:30Z","direction":"IN","origin_transaction_id":"7894561230123456001","reference_id":"TI202609010001","transaction_id":"7894561230123456789","type":"RECHARGE"}],"has_more":true,"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmqN5M1kHYcZmtRyv9aVrNv65W7Q6tFA","total_count":100},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

