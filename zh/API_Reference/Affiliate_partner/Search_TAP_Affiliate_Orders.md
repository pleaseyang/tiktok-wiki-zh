# 搜索 TAP Affiliate 订单

# Path: /affiliate_partner/202603/orders/search
# Method: [POST]
# 功能描述
TAP 可以使用此 API 获取 affiliate 订单列表并跟踪 affiliate 转化。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_token | string | N | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT | 上一次响应中 `next_page_token` 返回的分页 token。分页时，请在第一次请求中提供 `create_time_ge` 和 `create_time_lt`，然后在后续每次请求中传入此 token 并复用相同的 `campaign_id`（如果指定）、`create_time_ge` 和 `create_time_lt` 值。 |
| page_size | int | Y | 20 | 默认为 20，必须为正整数，范围为 1-100 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Body Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| create_time_ge | int | N | 1623812664 | 筛选在此时间或之后创建的订单，指定为 Unix 时间戳（秒）(UTC)。 |
`create_time_ge` 和 `create_time_lt` 必须同时提供，间隔不得超过三个月。如果两个字段都省略，API 将查询最近三个月的订单。 |
create_time_lt |int |N |1623899064 |筛选在此时间之前创建的订单，指定为 Unix 时间戳（秒）(UTC)。配对、间隔和默认行为请参见 `create_time_ge`。 |
campaign_id |string |N |7324371012170024705 |使用其标识符按 TAP campaign 筛选订单。 |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202603/orders/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT&page_size=20
```

**Body**
```json
{"create_time_ge":1623812664,"create_time_lt":1623899064,"campaign_id":"7324371012170024705"}
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sku_orders | []object |  | SKU 级别的 affiliate 订单记录。当对应的预估组件可用时，预估 commission 金额字段会被填充。实际 commission 金额字段仅在 `SETTLED` 或 `INELIGIBLE` 订单时填充，在这些状态之前会被省略；当底层组件不可用时，单个实际金额字段仍可能被省略。 |
| ^^id | string | 576962796354307765 | 交易主订单 ID |
| ^^create_time | int | 1685548800 | 订单创建时间，为 Unix 时间戳（秒）(UTC)。 |
| ^^delivery_time | int | 1685548800 | 订单配送时间，为 Unix 时间戳（秒）(UTC)。 |
| ^^settle_status | string | SETTLED | 订单的结算状态。 |
| 可能的值： |  |  |  |

1. "CUSTOMER UNPAID"，客户尚未付款。
2. "PENDING"，客户仍可退货或申请退款。显示的收益为预估值，等待结算。
3. "SETTLED"，您的收益已结算到您的账户。
4. "INELIGIBLE"，订单已被买家退货/退款/取消，不会结算 commission。
5. "FROZEN"，检测到与该订单相关的可能欺诈行为。commission 将在欺诈问题解决后解冻。 |
   ^^sku_id |string |1729793769377925388 |sku ID |
   ^^campaign_id |string |7324371012170024705 |与订单关联的 TAP campaign 标识符。 |
   ^^creator_username |string |liuyi_id_creator1jigo |Creator 用户名 |
   ^^product_name |string |Black Hoodie |产品名称。 |
   ^^product_id |string |1729435310697057093 |产品的唯一标识符 |
   ^^price |object | |价格 |
   ^^^amount |string |99 |价格金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^quantity |int |1 |订单中 SKU 项目的数量，包括已退款项目。 |
   ^^content_type |string |VIDEO |创建订单的 creator 内容格式。
   可能的值：
* SHOP
* VIDEO
* LIVE
* PRE_LIVE
* PROMOTION_PAGE
* LINKSHARE |
   ^^content_id |string |7494337156519332665 |内容的唯一标识符 |
   ^^creator_standard_commission_rate |int |3000 |Creator 标准 commission 率，按 10,000 缩放。例如，`3000` 表示 30%。 |
   ^^partner_standard_commission_rate |int |4000 |Affiliate partner 的标准 commission 率，按 10,000 缩放。例如，`4000` 表示 40%。 |
   ^^creator_shop_ads_commission_rate |int |3000 |Creator Shop Ads commission 率，按 10,000 缩放。例如，`3000` 表示 30%。 |
   ^^partner_shop_ads_commission_rate |int |4000 |Affiliate partner 的 Shop Ads commission 率，按 10,000 缩放。例如，`4000` 表示 40%。 |
   ^^partner_tap_bonus_commission_rate |int |1000 |TikTok Shop 为在特定 campaign 中推动产品销售而向 affiliate partner 提供的额外 commission 率，按 10,000 缩放。例如，`1000` 表示 10%。 |
   ^^creator_tap_bonus_commission_rate |int |2000 |affiliate partner 分配给 creator 的 commission 奖励率，按 10,000 缩放。例如，`2000` 表示 20%。 |
   ^^estimated_commission_base |object | |预估 commission 基数是商品单价乘以订单创建时的订购数量。 |
   ^^^amount |string |99 |预估 commission 基数金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_creator_standard_commission |object | |预估 TAP commission x creator commission 率 |
   ^^^amount |string |100 |预估 creator 标准 commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_partner_standard_commission |object | |预估 commission 基数 x TAP commission 率 |
   ^^^amount |string |100 |预估 affiliate partner 标准 commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_creator_shop_ads_commission |object | |预估 commission 基数 x creator shop ads commission 率 |
   ^^^amount |string |99 |预估 creator Shop Ads commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_partner_shop_ads_commission |object | |预估 commission 基数 x partner shop ads commission 率 |
   ^^^amount |string |99 |预估 affiliate partner Shop Ads commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_partner_tap_bonus_commission |object | |预估 partner commission 奖励费用 |
   ^^^amount |string |100 |预估 affiliate partner commission 奖励金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_creator_tap_bonus_commission |object | |预估 creator commission 奖励费用 |
   ^^^amount |string |100 |预估 creator commission 奖励金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_partner_isr |object | |墨西哥 partner 的预估 ISR 税额 |
   ^^^amount |string |99 |预估 ISR 税额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_partner_iva |object | |墨西哥 partner 的预估 IVA 税额 |
   ^^^amount |string |99 |预估 IVA 税额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_commission_base |object | |实际 commission 基数是商品单价乘以订购数量减去订单完成时的退货。 |
   ^^^amount |string |200 |实际 commission 基数金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_creator_standard_commission |object | |实际 TAP commission x creator commission 率 |
   ^^^amount |string |100 |实际 creator 标准 commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_partner_standard_commission |object | |实际 commission 基数 x TAP commission 率 |
   ^^^amount |string |99 |实际 affiliate partner 标准 commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_creator_shop_ads_commission |object | |实际 commission 基数 x creator shop ads commission 率 |
   ^^^amount |string |99 |实际 creator Shop Ads commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_partner_shop_ads_commission |object | |实际 commission 基数 x partner shop ads commission 率 |
   ^^^amount |string |99 |实际 affiliate partner Shop Ads commission 金额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_partner_isr |object | |墨西哥 partner 的实际 ISR 税额 |
   ^^^amount |string |99 |实际 ISR 税额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_partner_iva |object | |墨西哥 partner 的实际 IVA 税额 |
   ^^^amount |string |99 |实际 IVA 税额，不含货币符号。使用 `currency` 来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_partner_tap_bonus_commission |object | |实际 partner commission 奖励费用 |
   ^^^amount |string |200 |affiliate partner 从 commission 奖励中获得的实际费用 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_creator_tap_bonus_commission |object | |实际 creator commission 奖励费用 |
   ^^^amount |string |100 |creator 通过 affiliate partner 的 commission 奖励获得的实际费用 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^fully_return |string |Yes |SKU 是否已全额退货或退款。
   可能的值：
* `Yes`：该 SKU 已全额退货或退款，不支付 commission。
* `No`：该 SKU 未被全额退货或退款。 |
   ^^settlement_time |int |1685548800 |订单 commission 结算时间，为 Unix 时间戳（秒）(UTC)。 |
   ^^last_update_time |int |1685548800 |记录最后更新时间，为 Unix 时间戳（秒）(UTC)。 |
   ^^is_carousel |bool |false |轮播内容可能涉及 commission 率优惠。当订单归因于轮播内容时返回 true。 |
   ^next_page_token |string |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT |将此分页 token 作为下一次请求中的 `page_token` 传入。对每一页复用相同的 `campaign_id`（如果指定）、`create_time_ge` 和 `create_time_lt` 值；在第一次请求中指定两个时间边界以保持搜索窗口固定。当此字段被省略时停止分页。 |
   ^total_count |int |100 |跨所有页面匹配请求筛选条件的 SKU 订单总数。 |

# Response Sample
```json
{"code":0,"data":{"sku_orders":[{"id":"576962796354307765","create_time":1685548800,"delivery_time":1685548800,"settle_status":"SETTLED","sku_id":"1729793769377925388","campaign_id":"7324371012170024705","creator_username":"liuyi_id_creator1jigo","product_name":"Black Hoodie","product_id":"1729435310697057093","price":{"amount":"99","currency":"USD"},"quantity":1,"content_type":"VIDEO","content_id":"7494337156519332665","creator_standard_commission_rate":3000,"partner_standard_commission_rate":4000,"creator_shop_ads_commission_rate":3000,"partner_shop_ads_commission_rate":4000,"partner_tap_bonus_commission_rate":1000,"creator_tap_bonus_commission_rate":2000,"estimated_commission_base":{"amount":"99","currency":"USD"},"estimated_creator_standard_commission":{"amount":"100","currency":"USD"},"estimated_partner_standard_commission":{"amount":"100","currency":"USD"},"estimated_creator_shop_ads_commission":{"amount":"99","currency":"USD"},"estimated_partner_shop_ads_commission":{"amount":"99","currency":"USD"},"estimated_partner_tap_bonus_commission":{"amount":"100","currency":"USD"},"estimated_creator_tap_bonus_commission":{"amount":"100","currency":"USD"},"estimated_partner_isr":{"amount":"99","currency":"USD"},"estimated_partner_iva":{"amount":"99","currency":"USD"},"actual_commission_base":{"amount":"200","currency":"USD"},"actual_creator_standard_commission":{"amount":"100","currency":"USD"},"actual_partner_standard_commission":{"amount":"99","currency":"USD"},"actual_creator_shop_ads_commission":{"amount":"99","currency":"USD"},"actual_partner_shop_ads_commission":{"amount":"99","currency":"USD"},"actual_partner_isr":{"amount":"99","currency":"USD"},"actual_partner_iva":{"amount":"99","currency":"USD"},"actual_partner_tap_bonus_commission":{"amount":"200","currency":"USD"},"actual_creator_tap_bonus_commission":{"amount":"100","currency":"USD"},"fully_return":"Yes","settlement_time":1685548800,"last_update_time":1685548800,"is_carousel":false}],"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT","total_count":100},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

