# 搜索达人 Affiliate 订单

# 路径：/affiliate_creator/202410/orders/search
# 方法：[POST]
# 功能描述
搜索归属于已认证达人的联盟订单。响应包含订单与 SKU 详情、订单状态、内容归因、佣金率以及预估或实际佣金金额，用于跟踪联盟转化。

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
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
| page_size | int | Y | 20 | 每页返回的结果数量。 Default: 20 |
| Valid Range: [1-100] |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| create_time_ge | int | N | 1719807456 | 筛选订单，仅显示创建时间为指定日期时间或之后的订单。Unix 时间戳。 |
| Note: |  |  |  |  |
| `create_time_ge` 与 `create_time_lt` 共同构成创建时间筛选条件。 |  |  |  |  |

* 如果填写了 `create_time_ge` 但 `create_time_lt` 为空，`create_time_lt` 将默认为当前时间。
* 如果填写了 `create_time_lt` 但 `create_time_ge` 为空，则 `create_time_ge` 默认取最早的店铺时间。 |
   create_time_lt |int |N |1728443155 |筛选订单，仅显示创建时间早于指定时间的订单，以秒为单位的 Unix 时间戳表示。更多用法信息请参阅 `create_time_ge` 中的说明。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202410/orders/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_token=b2Zmc2V0PTAK&page_size=20
```

**Body**
```json
{"create_time_ge":1719807456,"create_time_lt":1728443155}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^orders | []object |  | 订单资源。 |
| ^^id | string | 789078671231123124 | 订单标识符。 |
| ^^create_time | int | 1685548800 | 订单创建时间，以 Unix 时间戳（秒，UTC）表示。 |
| ^^delivery_time | int | 1685548800 | 订单交付时间，以 Unix 时间戳（秒，UTC）表示。 |
| ^^status | string | SETTLED | 订单的当前状态。可能的选项为： |

* UNSPECIFIED: 订单状态未定义. 之后可能会更新。
* AWAITING PAYMENT：订单尚未支付，仅可获取预估佣金
* To-SETTLE：订单正在等待结算，仅可获得预估佣金
* SETTLED: 订单的佣金已结算。
* REFUNDED: 订单已被买家退货/退款/取消，且不会结算佣金。
* FROZEN：检测到该订单可能存在欺诈。欺诈问题解决后，佣金将解除冻结。 |
   ^^skus |[]object | |与订单关联的 SKU 列表。 |
   ^^^id |string |1729793769377925388 |SKU 标识符。 |
   ^^^campaign_id |string |73661290629 |与订单关联的活动标识符。 |
   ^^^open_collaboration_id |string |73661290629 |与订单关联的 open collaboration 标识符。 |
   ^^^target_collaboration_id |string |73661290629 |与订单关联的 target collaboration 标识符。 |
   ^^^product_name |string |black_suit |TikTok Shop 中的商品名称。 |
   ^^^product_id |string |1729793769377859852 |商品标识符。 |
   ^^^price |object | |表示商品本地化价格的对象。 |
   ^^^^amount |string |Rp9.900 |与商品相关的价格值。 |
   ^^^^currency |string |IDR |与商品相关价格的货币代码。 |
   ^^^shop_name |string |TestCase idl2l |商品提供销售的 TikTok Shop 名称。 |
   ^^^content_type |string |LIVE |创建订单的达人内容格式。
   可能的值：
* SHOP
* VIDEO
* LIVE
* PRE_LIVE
* PROMOTION_PAGE
* LINKSHARE |
   ^^^content_id |string |7493990579714164574 |创建订单的达人内容标识符。 |
   ^^^quantity |int |2 |订单中此 SKU 的数量，包含已退款件数。 |
   ^^^commission_rate |int |1000 |该 SKU 的总佣金率，等于标准佣金率、店铺广告佣金率、加成率和奖励率之和。以万分之一为单位表示；不含百分号（`%`）。例如，`3000` 表示 30% 的佣金。 |
   ^^^commission_tier_setting |string |3.0 OR 5.0 |卖家与达人之间的佣金百分比。当应用阶梯佣金模型时，将返回卖家设置的每个阶梯的佣金费率。 |
   ^^^commission_model |string |Tiered 佣金 |订单使用的佣金模型。
   可能的值：
* Fixed commission
* Tiered commission |
   ^^^commission_bonus_rate |int |1000 |与协作关联的佣金加成率。以万分之一为单位表示；不含百分号（`%`）。例如，`3000` 表示 30% 的佣金。 |
   ^^^estimated_commission_base |object | |表示订单创建时预估基础佣金的对象。 |
   ^^^^amount |string |Rp9.900 |预估佣金基数金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^standard_commission_rate |int |5000 |与协作关联的标准联盟佣金率。以万分之一为单位表示；不含百分号（`%`）。例如，`3000` 表示 30% 的佣金。 |
   ^^^shop_ads_commission_rate |int |5000 |达人从与特定内容关联的销售中获得的佣金率。以万分之一为单位表示；不含百分号（`%`）。例如，`3000` 表示 30% 的佣金。 |
   ^^^estimated_bonus_commission |object | |表示预估奖励佣金的对象，通过将预估佣金基数乘以佣金奖励费率计算得出。 |
   ^^^^amount |string |Rp1.00 |预估奖励佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^estimated_standard_commission |object | |表示预估标准联盟佣金的对象，由预估佣金基数乘以 `standard_commission_rate` 计算得出。 |
   ^^^^amount |string |Rp8.000 |预估标准佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^estimated_shop_ads_commission |object | |表示预估 Shop Ads 佣金的对象，通过将预估佣金基数乘以 shop_ads_commission_rate 计算得出 |
   ^^^^amount |string |Rp8.000 |预估 Shop Ads 佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^estimated_commission |object | |达人此 SKU 在适用加法和扣除后的总预估佣金收入。 |
   ^^^^amount |string |Rp1.980 |预估佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^actual_commission |object | |表示此 SKU 的最终收入，通过将实际佣金基数乘以总佣金费率，然后扣除税费或与机构分成的金额计算得出。 |
   ^^^^amount |string |Rp1.900 |实际佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^actual_bonus_commission |object | |表示实际奖励佣金的对象，通过将实际佣金基数乘以佣金奖励费率计算得出。 |
   ^^^^amount |string |Rp2.000 |实际奖励佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^actual_commission_base |object | |表示实际佣金基数的对象，通过将商品销售价格乘以已售商品数量，减去退货和退款订单计算得出。 |
   ^^^^amount |string |Rp9.900 |实际佣金基数的值。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^actual_standard_commission |object | |表示实际标准 affiliate 佣金的对象，通过将佣金基数乘以 standard_commission_rate 计算得出。 |
   ^^^^amount |string |Rp5.000 |实际标准佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^actual_shop_ads_commission |object | |表示实际 Shop Ads 佣金的对象，通过将佣金基数乘以 shop_ads_commission_rate 计算得出。 |
   ^^^^amount |string |Rp5.000 |实际 Shop Ads 佣金金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^returned_quantity |int |1 |此 SKU 在订单中的退货数量。 |
   ^^^refunded_quantity |int |0 |此 SKU 在订单中的退款数量。 |
   ^^^tag |string |test-01 |用于存储用户自定义元数据以进行追踪的字段。 |
   ^^^creator_commission_reward_rate |int |1000 |合作伙伴分配给达人的佣金奖励率。以万分之一为单位表示；不含百分号（`%`）。例如，`1000` 表示 10%。 |
   ^^^estimated_creator_commission_reward_fee |object | |预估达人佣金奖励费用。 |
   ^^^^amount |string |250 |达人通过佣金奖励从 affiliate 合作伙伴获得的预估费用 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^actual_creator_commission_reward_fee |object | |实际达人佣金奖励费用。 |
   ^^^^amount |string |100 |达人通过佣金奖励从 affiliate 合作伙伴获得的实际费用 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^isr |object | |仅适用于墨西哥达人，平台根据法规代政府收取相关收入税。 |
   ^^^^amount |string |100 |实际 ISR 金额。 |
   ^^^^currency |string |MXN |货币代码。 |
   ^^^iva |object | |仅适用于墨西哥达人，平台根据法规代政府收取相关收入税。 |
   ^^^^amount |string |100 |实际 IVA 金额。 |
   ^^^^currency |string |MXN |货币代码。 |
   ^^^pit |object | |仅适用于越南/泰国/菲律宾/印尼达人，卖家根据法规收取相关预扣税。 |
   ^^^^amount |string |100 |实际 PIT 金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^shared_with_partner |object | |根据适用的费用协议，达人税后收入与关联机构分享的金额。 |
   ^^^^amount |string |100 |实际与合作伙伴分享的金额。 |
   ^^^^currency |string |IDR |货币代码。 |
   ^^^trace_info |object | |用于追踪目的的额外信息。 |
   ^^^^id |string |15678763 |当 `trace_info.type` 为 `GENERAL` 时，此为 `{eid}`（在 `sharing_link` 中提供）；当 `trace_info.type` 为 `SPECIFIC` 时，此为 `publisher_id`。 |
   ^^^^type |string |SPECIFIC |对于来自特定发布者分享链接的订单，取值为 `SPECIFIC`；对于来自通用分享链接的订单，取值为 `GENERAL`。 |
   ^^^last_update_time |int |1685548800 |记录最后更新时间，以 Unix 时间戳（秒，UTC）表示。 |
   ^^^is_carousel |bool |false |轮播内容可能涉及佣金费率折扣。当订单归因于轮播内容时返回 true。 |
   ^next_page_token |string |b2Zmc2V0PTEw |用于获取下一页结果的不透明令牌。在首次请求中指定 `create_time_ge` 和 `create_time_lt`，并在每一页复用相同的值。在下一次请求中将返回的非空令牌作为 `page_token` 传入。空值表示最后一页；请停止请求更多页面。 |
   ^total_count |int |10 |匹配搜索条件的 SKU 订单总数。`page_size` 在 SKU 订单行分组为 `orders` 之前限制其行数；由于一个订单可包含多个 SKU，返回的订单对象数量可能小于 `page_size`。使用 `next_page_token` 继续分页。 |

# 响应示例
```json
{"code":0,"data":{"orders":[{"id":"789078671231123124","create_time":1685548800,"delivery_time":1685548800,"status":"SETTLED","skus":[{"id":"1729793769377925388","campaign_id":"73661290629","open_collaboration_id":"73661290629","target_collaboration_id":"73661290629","product_name":"black_suit","product_id":"1729793769377859852","price":{"amount":"Rp9.900","currency":"IDR"},"shop_name":"TestCase idl2l","content_type":"LIVE","content_id":"7493990579714164574","quantity":2,"commission_rate":1000,"commission_tier_setting":"3.0 OR 5.0","commission_model":"Tiered commission","commission_bonus_rate":1000,"estimated_commission_base":{"amount":"Rp9.900","currency":"IDR"},"standard_commission_rate":5000,"shop_ads_commission_rate":5000,"estimated_bonus_commission":{"amount":"Rp1.00","currency":"IDR"},"estimated_standard_commission":{"amount":"Rp8.000","currency":"IDR"},"estimated_shop_ads_commission":{"amount":"Rp8.000","currency":"IDR"},"estimated_commission":{"amount":"Rp1.980","currency":"IDR"},"actual_commission":{"amount":"Rp1.900","currency":"IDR"},"actual_bonus_commission":{"amount":"Rp2.000","currency":"IDR"},"actual_commission_base":{"amount":"Rp9.900","currency":"IDR"},"actual_standard_commission":{"amount":"Rp5.000","currency":"IDR"},"actual_shop_ads_commission":{"amount":"Rp5.000","currency":"IDR"},"returned_quantity":1,"refunded_quantity":0,"tag":"test-01","creator_commission_reward_rate":1000,"estimated_creator_commission_reward_fee":{"amount":"250","currency":"IDR"},"actual_creator_commission_reward_fee":{"amount":"100","currency":"IDR"},"isr":{"amount":"100","currency":"MXN"},"iva":{"amount":"100","currency":"MXN"},"pit":{"amount":"100","currency":"IDR"},"shared_with_partner":{"amount":"100","currency":"IDR"},"trace_info":{"id":"15678763","type":"SPECIFIC"},"last_update_time":1685548800,"is_carousel":false}]}],"next_page_token":"b2Zmc2V0PTEw","total_count":10},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

