# 按达人搜索 Affiliate 订单

# 路径：/affiliate_creator/202505/orders/trace/search
# 方法：[POST]
# 功能描述
获取当前访问令牌所代表达人归属的联盟订单。结果可提供订单状态与时间戳，以及 SKU 级别的商品、店铺、内容、trace、数量、价格和预估或实际佣金详情。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | asdasdaszz | 用于检索分页结果集下一页的不透明 token。从上一次响应的 next_page_token 结果中获取此值。第一页不需要此参数。 |
| page_size | int | Y | 50 | 每页返回的结果数。 |
| 有效范围： 1 to 100。 |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| time_ge | int | Y | 1719807456000 | 所选 `time_type` 时间范围的包含性起始时间，以毫秒为单位的 Unix 时间戳。包含时间戳大于或等于 `time_ge` 且小于 `time_lt` 的订单。 |
| time_lt | int | Y | 1728443155000 | 所选 `time_type` 时间范围的排他结束时间，以毫秒为单位的 Unix 时间戳。包含时间戳大于或等于 `time_ge` 且小于 `time_lt` 的订单。 |
| time_type | string | N | PAY_TIME | 指定用于筛选订单的时间戳类型. 查询时间范围 (time_ge 和 time_lt) 将应用于所选的时间类型。 |
| 可能的值： |  |  |  |  |

* PAY_TIME: 按订单支付时间筛选。
* DELIVERY_TIME: 按订单配送/发货时间筛选。
* SETTLE_TIME: 按订单结算时间筛选。
* CREATE_TIME (默认): 按订单创建时间筛选。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202505/orders/trace/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_token=asdasdaszz&page_size=50
```

**Body**
```json
{"time_ge":1719807456000,"time_lt":1728443155000,"time_type":"PAY_TIME"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^orders | []object |  | 订单资源。 |
| ^^id | int | 789078671231123124 | 订单标识符。 |
| ^^status | string | SETTLED | 订单的当前状态。可能的值： |

* UNSPECIFIED: 状态未定义，后续可能更新。
* ORDERED: 订单已下单，但佣金尚未结算. 预估佣金可用。
* SETTLED: 佣金已结算. 当对应的结算金额可用时才会填入实际的佣金取值。
* REFUNDED：订单被买家退货、退款或取消；实际佣金和实际佣金基数金额以本地化的零值返回。
* FROZEN: 检测到可能存在欺诈。在问题解决之前，佣金保持冻结。
* DEDUCTED: 余额账户发生额外扣款。

对于 SETTLED 或 REFUNDED 以外的状态，实际佣金值可能为空。加成、店铺广告和达人佣金奖励金额仅在存在相应佣金数据时才会填充；其可用性并非仅由订单状态决定。 |
^^skus |[]object | |与订单关联的 SKU 列表。 |
^^^id |string |1729793769377925388 |SKU 标识符。 |
^^^product_id |string |1729793769377859852 |商品标识符。 |
^^^price |object | |表示商品本地化价格的对象。 |
^^^^amount |string |Rp9.900 |商品价格，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |与商品相关价格的货币代码。 |
^^^quantity |int |2 |此 SKU 在订单中的数量。 |
^^^commission_rate |int |1000 |与协作关联的佣金率，以 0.01% 为单位。取值不含百分号。例如，`3000` 表示 30%。 |
^^^estimated_commission_base |object | |表示订单创建时预估基础佣金的对象。 |
^^^^amount |string |Rp9.900 |预估佣金基数，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |货币代码。 |
^^^actual_commission |object | |表示达人实际佣金的对象。其金额包含 `actual_bonus_commission` 和 `actual_creator_commission_reward_fee` 中也报告的分项。`actual_shop_ads_commission` 金额是单独的，不包含在内。 |
^^^^amount |string |Rp1.900 |实际佣金金额，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。空字符串表示没有可用的实际佣金值。 |
^^^^currency |string |IDR |货币代码。 |
^^^shop_ads_commission_rate |int |5000 |达人从与特定内容关联的销售中获得的佣金率，以万分之一为单位表示。该值不含百分号。例如，`3000` 表示 30%。 |
^^^commission_bonus_rate |int |1000 |与协作关联的佣金奖励率，以 0.01% 为单位。取值不含百分号。例如，`3000` 表示 30%。 |
^^^product_name |string |black suit |TikTok Shop 中的商品名称。 |
^^^shop_name |string |TestCase idl2l |商品提供销售的 TikTok Shop 名称。 |
^^^returned_quantity |int |1 |此 SKU 在订单中的退货数量。 |
^^^refunded_quantity |int |0 |此 SKU 在订单中的退款数量。 |
^^^campaign_id |string |73661290629 |与订单关联的活动标识符。 |
^^^actual_commission_base |object | |表示实际佣金基数的对象，通过将商品销售价格乘以已售商品数量，减去退货和退款订单计算得出。 |
^^^^amount |string |Rp9.900 |实际佣金基数，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。对于 `SETTLED` 订单，如有则包含实际基数；对于 `REFUNDED` 订单，为本地化的零值；对于其它状态，为空字符串。 |
^^^^currency |string |IDR |货币代码。 |
^^^actual_shop_ads_commission |object | |表示实际 Shop Ads 佣金的对象，通过将佣金基数乘以 shop_ads_commission_rate 计算得出。 |
^^^^amount |string |Rp5.000 |如有，实际店铺广告佣金金额，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |货币代码。 |
^^^estimated_shop_ads_commission |object | |表示预估 Shop Ads 佣金的对象，通过将预估佣金基数乘以 shop_ads_commission_rate 计算得出 |
^^^^amount |string |Rp8.000 |预估店铺广告佣金金额，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |货币代码。 |
^^^estimated_bonus_commission |object | |表示预估奖励佣金的对象，通过将预估佣金基数乘以佣金奖励费率计算得出。 |
^^^^amount |string |Rp1.00 |如有，预估加成佣金金额，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |货币代码。 |
^^^delivery_time |int |1685548800 |订单交付日期和时间，UTC+0 计时 |
^^^creator_commission_reward_rate |int |1000 |联盟合作伙伴分配给达人的佣金奖励率，以 0.01% 为单位。取值不含百分号。例如，`1000` 表示 10%。 |
^^^estimated_creator_commission_reward_fee |object | |预估达人佣金奖励费用。 |
^^^^amount |string |250 |如有，预估达人佣金奖励费用，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |货币代码。 |
^^^actual_creator_commission_reward_fee |object | |实际达人佣金奖励费用。 |
^^^^amount |string |100 |如有，实际达人佣金奖励费用，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
^^^^currency |string |IDR |货币代码。 |
^^^content_type |string |LIVE |创建订单的达人内容格式。
可能的值：

* SHOP
* VIDEO
* LIVE
* PRE_LIVE
* PROMOTION_PAGE
* LINKSHARE |
   ^^^content_id |string |7493990579714164574 |创建订单的达人内容标识符。 |
   ^^^trace |object | |用于追踪目的的额外信息。 |
   ^^^^id |string |15678763 |当 `trace.type` 为 `GENERAL` 时，这是通用分享链接中嵌入的 `event_id`。当 `trace.type` 为 `SPECIFIC` 时，这是生成特定发布者分享链接时提供的 `publisher_id`。 |
   ^^^^type |string |SPECIFIC |对于来自特定发布者分享链接的订单，取值为 `SPECIFIC`；对于来自通用分享链接的订单，取值为 `GENERAL`。 |
   ^^^estimated_commission |object | |表示达人预估佣金的对象。其金额包含 `estimated_bonus_commission` 和 `estimated_creator_commission_reward_fee` 中也报告的分项。`estimated_shop_ads_commission` 金额是单独的，不包含在内。 |
   ^^^^amount |string |1 |预估佣金金额，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
   ^^^^currency |string |USD |货币代码。 |
   ^^^actual_bonus_commission |object | |表示实际奖励佣金的对象，通过将实际佣金基数乘以佣金奖励费率计算得出。 |
   ^^^^amount |string |1 |实际加成佣金金额，以本地化展示字符串形式表示。它可能包含货币符号或货币代码以及地区特有的小数点与千位分隔符；货币代码请参见同级 `currency` 字段。 |
   ^^^^currency |string |USD |货币代码。 |
   ^^create_time |int |1685548800 |订单创建日期和时间，UTC+0 计时 |
   ^^delivery_time |int |1685548800 |订单交付日期和时间，UTC+0 计时 |
   ^next_page_token |string |b2Zmc2V0PTEw |用于获取分页结果集下一页的不透明 token。
   |
   ^total_count |int |10 |响应中的订单总数。
   |

# 响应示例
```json
{"code":0,"data":{"orders":[{"id":789078671231123124,"status":"SETTLED","skus":[{"id":"1729793769377925388","product_id":"1729793769377859852","price":{"amount":"Rp9.900","currency":"IDR"},"quantity":2,"commission_rate":1000,"estimated_commission_base":{"amount":"Rp9.900","currency":"IDR"},"actual_commission":{"amount":"Rp1.900","currency":"IDR"},"shop_ads_commission_rate":5000,"commission_bonus_rate":1000,"product_name":"black suit","shop_name":"TestCase idl2l","returned_quantity":1,"refunded_quantity":0,"campaign_id":"73661290629","actual_commission_base":{"amount":"Rp9.900","currency":"IDR"},"actual_shop_ads_commission":{"amount":"Rp5.000","currency":"IDR"},"estimated_shop_ads_commission":{"amount":"Rp8.000","currency":"IDR"},"estimated_bonus_commission":{"amount":"Rp1.00","currency":"IDR"},"delivery_time":1685548800,"creator_commission_reward_rate":1000,"estimated_creator_commission_reward_fee":{"amount":"250","currency":"IDR"},"actual_creator_commission_reward_fee":{"amount":"100","currency":"IDR"},"content_type":"LIVE","content_id":"7493990579714164574","trace":{"id":"15678763","type":"SPECIFIC"},"estimated_commission":{"amount":"1","currency":"USD"},"actual_bonus_commission":{"amount":"1","currency":"USD"}}],"create_time":1685548800,"delivery_time":1685548800}],"next_page_token":"b2Zmc2V0PTEw","total_count":10},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

