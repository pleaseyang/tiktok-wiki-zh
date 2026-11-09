# 搜索卖家 Affiliate 订单

# 路径：/affiliate_seller/202410/orders/search
# 方法：[POST]
# 功能描述
此 API 允许合作伙伴检索卖家生成的 affiliate 订单（符合 affiliate 佣金资格的订单）列表，返回订单 ID 和商品 ID。通过此 API，合作伙伴可以使用订单 ID 追踪代表卖家的 affiliate 转化情况。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。请从上一次响应的 `next_page_token` 结果中获取此值。首页不需要此参数。 |
| page_size | int | Y | 20 | 每页返回的结果数量。默认值：20 |
| 有效范围：[1-100] |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| create_time_lt | int | N | 1722485856 | 筛选在指定日期和时间之前创建的订单。Unix 时间戳。更多使用信息请参阅 `create_time_ge` 中的说明。请注意，每次请求最多支持 3 个月的数据。 |
| create_time_ge | int | N | 1719807456 | 筛选在指定日期和时间或之后创建的订单。Unix 时间戳。 |
注意：
`create_time_ge` 和 `create_time_lt` 共同构成创建时间筛选条件。

* 如果填写了 `create_time_ge` 但 `create_time_lt` 为空，则 `create_time_lt` 将默认为当前时间。
* 如果填写了 `create_time_lt` 但 `create_time_ge` 为空，则 `create_time_ge` 将默认为店铺最早时间。
   如果两者都未指定，则默认查询最近三个月的数据。 |
   program_id |string |N |73661290629 |按关联的 affiliate 计划筛选订单，该计划对应您的代理机构合作伙伴的活动 ID。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202410/orders/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=b2Zmc2V0PTAK&page_size=20
```

**Body**
```json
{"create_time_lt":1722485856,"create_time_ge":1719807456,"program_id":"73661290629"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^orders | []object |  | 返回的订单列表。 |
| ^^id | string | 579125529499110202 | 订单 ID。 |
| ^^delivery_time | int | 1723748656 | 订单交付的日期和时间。Unix 时间戳。 |
| ^^create_time | int | 1722420186 | 订单创建的日期和时间。Unix 时间戳。 |
| ^^status | string | COMPLETED | 该字段已弃用，不会返回值。有关 SKU 的结算状态，请参阅下方的 settle_status。 |
| ^^skus | []object |  | 此订单中包含的 SKU 列表。 |
| ^^^sku_id | string | 1729791975232997145 | 您的 SKU ID |
| ^^^settlement_status | string | SETTLED | SKU 订单的当前结算状态。可能的选项包括： |

* Unknown：订单状态未定义，可能会在后续更新。
* AWAITING PAYMENT：客户尚未付款，仅提供预估佣金。
* To-SETTLE：订单等待结算，仅提供预估佣金。
* SETTLED：订单的佣金已结算。
* INELIGIBLE：订单已被买家退货/退款/取消，不会结算佣金。 |
   ^^^open_collaboration_id |string |73661290629 |商品注册的 open collaboration 的 ID。 |
   ^^^target_collaboration_id |string |73661290629 |商品注册的 target collaboration 的 ID。 |
   ^^^campaign_id |string |73661290629 |商品注册的 TAP 活动的 ID。 |
   ^^^creator_username |string |exampleTikTokCreatorUsername |参与指定 open collaboration 的达人的用户名。 |
   ^^^price |object | |SKU 售价信息。 |
   ^^^^amount |string |1000 |价格金额。 |
   ^^^^currency |string |VND |价格币种。 |
   ^^^quantity |int |1 |订单的 SKU 数量。 |
   ^^^content_type |string |LIVE |创建此订单的达人内容格式。
   可能的值：
* SHOP
* VIDEO
* LIVE
* PRE_LIVE
* PROMOTION_PAGE
* LINKSHARE |
   ^^^content_id |string |7493990579714164574 |内容标识符。 |
   ^^^product_id |string |1729503179457070324 |TikTok Shop 中的商品 ID。 |
   ^^^commission_model |string |Tiered 佣金 |确定订单佣金是基于固定佣金模型还是阶梯模型计算。 |
   ^^^commission_tier_setting |string |3.0 OR 5.0 |卖家与达人之间的佣金百分比。当应用阶梯佣金模型时，将返回卖家设置的每个阶梯的佣金比率。 |
   ^^^commission_rate |string |1000 |卖家设定的需支付给参与 collaboration 的达人的佣金比率，以百分之一为单位。例如，1550 表示 15.50% 的佣金比率。请注意，仅当此订单直接来自您的达人时才返回该值。如果您使用合作伙伴，请参阅 partner_commission_rate。 |
   ^^^partner_commission_rate |string |1000 |卖家设定的需支付给参与 collaboration 的 affiliate 合作伙伴的佣金比率，以百分之一为单位。例如，1550 表示 15.50% 的佣金比率。 |
   ^^^shop_ads_commission_rate |string |5000 |通过 Shop Ads 生成的订单的佣金比率。 |
   ^^^estimated_commission_base |object | |扣除任何退款前的预估总销售额，用作计算佣金的基础。
   公式：售价 * 订单数量 |
   ^^^^amount |string |1000 |佣金基础金额。 |
   ^^^^currency |string |VND |佣金基础币种。 |
   ^^^estimated_paid_shop_ads_commission |object | |卖家将为销售支付的预估 Shop Ads 佣金。
   公式：预估佣金基础 * Shop Ads 佣金比率 |
   ^^^^amount |string |1000 |佣金金额。 |
   ^^^^currency |string |VND |佣金币种。 |
   ^^^estimated_paid_commission |object | |卖家将为销售支付的预估佣金。
   公式：预估佣金基础 * 佣金比率。
   请注意，仅当此订单直接来自您的达人时才返回该值。如果您使用合作伙伴，请参阅 paid_partner_commission。 |
   ^^^^amount |string |20000 |佣金金额。 |
   ^^^^currency |string |VND |佣金币种。 |
   ^^^estimated_paid_partner_commission |object | |卖家将为销售支付给 affiliate 合作伙伴的预估佣金。
   公式：预估佣金基础 * 合作伙伴佣金比率 |
   ^^^^amount |string |100 |佣金金额。 |
   ^^^^currency |string |USD |佣金币种。 |
   ^^^actual_commission_base |object | |扣除任何退款后的实际总销售额，用作计算佣金的基础。
   公式：售价 *（订单数量 - 退货/退款数量） |
   ^^^^amount |string |50000 |佣金基础金额。 |
   ^^^^currency |string |VND |佣金基础币种。 |
   ^^^actual_paid_commission |object | |卖家将为销售支付的实际佣金。
   公式：实际佣金基础 * 佣金比率。
   请注意，仅当此订单直接来自您的达人时才返回该值。如果您使用合作伙伴，请参阅 actual_paid_partner_commission。
   |
   ^^^^amount |string |10000 |佣金金额。 |
   ^^^^currency |string |VND |佣金币种。 |
   ^^^actual_paid_partner_commission |object | |卖家将为销售支付给 affiliate 合作伙伴的实际佣金。
   公式：实际佣金基础 * 合作伙伴佣金比率 |
   ^^^^amount |string |20000 |佣金金额。 |
   ^^^^currency |string |VND |佣金币种。 |
   ^^^actual_paid_shop_ads_commission |object | |卖家将为销售支付的实际 Shop Ads 佣金。
   公式：实际佣金基础 * Shop Ads 佣金比率 |
   ^^^^amount |string |20000 |佣金金额。 |
   ^^^^currency |string |VND |佣金币种。 |
   ^^^estimated_cofunded_creator_bonus_amount |object | |您在佣金 boost 中共同资助的预估达人奖金部分。 |
   ^^^^amount |string |100 |佣金金额。 |
   ^^^^currency |string |USD |佣金币种。 |
   ^^^actual_cofunded_creator_bonus_amount |object | |您在佣金 boost 中共同资助的实际达人奖金部分。 |
   ^^^^amount |string |100 |佣金金额。 |
   ^^^^currency |string |USD |佣金币种。 |
   ^^^refunded_quantity |int |1 |该字段已弃用，不返回值。请参阅 fully_return。 |
   ^^^returned_quantity |int |1 |该字段已弃用，不返回值。请参阅 fully_return。 |
   ^^^fully_return |string |Yes |当此 SKU 完全退货/退款时返回 yes。全额退货/退款时不给予佣金。 |
   ^^^is_carousel |bool |false |轮播内容可能涉及佣金比率折扣。当订单归因于轮播内容时返回 [True]。 |
   ^^^sku_name |string |Silver PVD |此商品的官方显示名称和唯一标识符，由 TikTok Shop 定义和标准化。 |
   ^^^seller_sku |string |cs001-pvd-bag |此商品的唯一标识符，由卖家自行定义和使用。 |
   ^next_page_token |string |WzE2OTUxMTY2NTQ2OTMsNTc2NDczNDg5ODYxNDEyMDI1XQ== |用于获取分页结果集下一页的不透明 token。如果当前响应未返回所有结果，请在此请求的 `page_token` 参数中提供此值。 |
   ^total_count |int |10000 |符合查询条件的 SKU 订单总数。 |

# 响应示例
```json
{"code":0,"data":{"orders":[{"id":"579125529499110202","delivery_time":1723748656,"create_time":1722420186,"status":"COMPLETED","skus":[{"sku_id":"1729791975232997145","settlement_status":"SETTLED","open_collaboration_id":"73661290629","target_collaboration_id":"73661290629","campaign_id":"73661290629","creator_username":"exampleTikTokCreatorUsername","price":{"amount":"1000","currency":"VND"},"quantity":1,"content_type":"LIVE","content_id":"7493990579714164574","product_id":"1729503179457070324","commission_model":"Tiered commission","commission_tier_setting":"3.0 OR 5.0","commission_rate":"1000","partner_commission_rate":"1000","shop_ads_commission_rate":"5000","estimated_commission_base":{"amount":"1000","currency":"VND"},"estimated_paid_shop_ads_commission":{"amount":"1000","currency":"VND"},"estimated_paid_commission":{"amount":"20000","currency":"VND"},"estimated_paid_partner_commission":{"amount":"100","currency":"USD"},"actual_commission_base":{"amount":"50000","currency":"VND"},"actual_paid_commission":{"amount":"10000","currency":"VND"},"actual_paid_partner_commission":{"amount":"20000","currency":"VND"},"actual_paid_shop_ads_commission":{"amount":"20000","currency":"VND"},"estimated_cofunded_creator_bonus_amount":{"amount":"100","currency":"USD"},"actual_cofunded_creator_bonus_amount":{"amount":"100","currency":"USD"},"refunded_quantity":1,"returned_quantity":1,"fully_return":"Yes","is_carousel":false,"sku_name":"Silver PVD","seller_sku":"cs001-pvd-bag"}]}],"next_page_token":"WzE2OTUxMTY2NTQ2OTMsNTc2NDczNDg5ODYxNDEyMDI1XQ==","total_count":10000},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

