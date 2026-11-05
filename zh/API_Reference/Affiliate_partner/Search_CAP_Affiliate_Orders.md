# 搜索 CAP Affiliate 订单

# Path: /affiliate_partner/202603/cap_order/search
# Method: [POST]
# 功能描述
在指定或默认的创建时间范围内搜索 MCN（Creator Agency Partner）的 affiliate 订单。当提供多个请求体筛选条件时，`order_id`、`product_id`、`settle_status` 和创建时间范围使用 AND 语义组合，因此订单必须匹配每个提供的筛选条件。

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
| page_token | string | N | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT | 上一次响应中 `next_page_token` 返回的分页 token。该 token 仅包含 search-after 排序位置；不保留搜索筛选条件或 `page_size`。第一页请省略此参数。对于后续每一页，传入返回的 token，提供有效的 `page_size`，并重新发送与第一页相同的 partner 授权上下文和请求体筛选条件。`page_size` 值可以在每页独立设置。为了稳定的分页，请在每次请求中显式提供相同的固定 `create_time_ge` 和 `create_time_lt` 值，而不是依赖滚动的默认时间范围。 |
| page_size | int | Y | 20 | 默认为 20，必须为正整数，范围为 1-100 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Body Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | N | 576962796354307765 | 交易主订单 ID |
| product_id | string | N | 1729435310697057093 | 产品的唯一标识符 |
| settle_status | int | N | 1 | 按结算状态筛选订单。发送以下整数值之一；响应中的 `settle_status` 字段使用对应的标签： |

* `1` → `CUSTOMER UNPAID`：客户尚未付款。
* `2` → `PENDING`：客户仍可退货或申请退款，因此收益为预估值并等待结算。
* `3` → `SETTLED`：收益已结算到您的账户。
* `4` → `INELIGIBLE`：订单已退货、退款或取消，因此不会结算 commission。
* `5` → `FROZEN`：检测到可能的欺诈行为；commission 将在欺诈问题解决后解冻。 |
   create_time_ge |int |N |1791222188 |筛选在此时间或之后创建的订单。Unix 时间戳（秒）。`create_time_ge` 和 `create_time_lt` 必须同时提供。显式提供的时间范围最多可跨越 92 天。如果两个字段都未提供，API 将从请求时间前三个月开始搜索到请求时间。 |
   create_time_lt |int |N |1791229388 |筛选在此时间之前创建的订单。Unix 时间戳（秒）。`create_time_ge` 和 `create_time_lt` 必须同时提供。 |

# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202603/cap_order/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT&page_size=20
```

**Body**
```json
{"order_id":"576962796354307765","product_id":"1729435310697057093","settle_status":1,"create_time_ge":1791222188,"create_time_lt":1791229388}
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sku_orders | []object |  | 当前页返回的 SKU 订单。 |
对于名称以 `actual_` 开头的金额字段，嵌套的 `amount` 仅在 `settle_status` 为 `SETTLED` 或 `INELIGIBLE` 时才会存在。对于所有其他状态，`amount` 属性将被省略。即使是 `SETTLED` 或 `INELIGIBLE` 订单，单个 `actual_*` 字段仍可能省略 `amount`。 |
^^id |string |576962796354307765 |交易主订单 ID |
^^tags |string |test-01 |每个订单的可自定义 ID，用于跟踪不同前端模块的 performance。 |
^^create_time |int |1685548800 |订单创建时的 Unix 时间戳（秒）(UTC)。 |
^^delivery_time |int |1685548800 |订单配送时的 Unix 时间戳（秒）(UTC)。当没有配送时间戳时，此字段将被省略。 |
^^settle_status |string |SETTLED |订单的结算状态。
可能的值：

1. "CUSTOMER UNPAID"，客户尚未付款。
2. "PENDING"，客户仍可退货或申请退款。显示的收益为预估值，等待结算。
3. "SETTLED"，您的收益已结算到您的账户。
4. "INELIGIBLE"，订单已被买家退货/退款/取消，不会结算 commission。
5. "FROZEN"，检测到与该订单相关的可能欺诈行为。commission 将在欺诈问题解决后解冻。 |
   ^^sku_id |string |1729478689395213981 |SKU 标识符。 |
   ^^open_collaboration_id |string |7324371012170024705 |与订单关联的开放合作标识符。 |
   ^^target_collaboration_id |string |7324371012170024705 |与订单关联的定向合作标识符。 |
   ^^creator_username |string |liuyi_id_creator1jigo |Creator 用户名 |
   ^^product_name |string |Black Hoodie |产品名称。 |
   ^^product_id |string |1729435310697057093 |产品的唯一标识符 |
   ^^price |object | |SKU 售价信息 |
   ^^^amount |string |99 |SKU 售价金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^quantity |int |1 |订单中 SKU 项目的数量，包括已退款项目。 |
   ^^shop_name |string |xuyann aaaaa |Shop / Seller 名称 |
   ^^content_type |string |VIDEO |创建订单的 creator 内容格式。
   可能的值：
* SHOP
* VIDEO
* LIVE
* PRE_LIVE
* PROMOTION_PAGE
* LINKSHARE |
   ^^content_id |string |7494337156519332665 |内容的唯一标识符 |
   ^^attribution_type |string |Direct |`LINKSHARE` 内容的归因类型。
   可能的值：
* `Direct`：同店归因。
* `Indirect`：非同一店归因。结算 commission 率通常低于 Marketplace 或定向合作中约定的费率。

对于其他内容类型，此字段为空字符串。 |
^^commission_model |string |Tiered commission |commission 计算模型。
可能的值：

* `Fixed commission`
* `Tiered commission` |
   ^^commission_tier_setting |string |3 OR 5 |seller 为阶梯 commission 模型配置的 commission 率，以百分比表示，用 `OR` 分隔。对于固定 commission 模型返回 `-`。 |
   ^^standard_commission_rate |int |3000 |seller 到 creator 的标准 commission 率。以百分之一的百分比为单位的整数返回，不含百分号；例如，3000 表示 30%。 |
   ^^commission_bonus_rate |int |3000 |TTS 到 creator 的 commission 奖励率。以百分之一的百分比为单位的整数返回，不含百分号；例如，3000 表示 30%。 |
   ^^shop_ads_commission_rate |int |3000 |支付给 creator 的 Shop Ads commission 率。以百分之一的百分比为单位的整数返回，不含百分号；例如，3000 表示 30%。 |
   ^^tap_bonus_commission_rate |int |3000 |affiliate partner 分配给 creator 的 commission 奖励率。以百分之一的百分比为单位的整数返回，不含百分号；例如，3000 表示 30%。 |
   ^^revenue_sharing_portion_rate |int |3000 |creator 和机构之间的收入分成比例。以百分之一的百分比为单位的整数返回，不含百分号；例如，3000 表示 30%。 |
   ^^estimated_commission_base |object | |预估 commission 基数是订单创建时的产品售价乘以销售数量。 |
   ^^^amount |string |99 |commission 基数金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_standard_commission |object | |creator 将获得的预估标准销售 commission。 |
   ^^^amount |string |99 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_bonus_commission |object | |TTS 支付给表现优秀的 creator 的预估 commission |
   ^^^amount |string |99 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_shop_ads_commission |object | |creator 将从购买特定创意的 seller/广告主获得的预估 Shop Ads commission |
   ^^^amount |string |99 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_tap_bonus_commission |object | |TAP 提供给 creator 的预估 commission 奖励 |
   ^^^amount |string |99 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_creator_tax_isr |object | |仅适用于墨西哥 creator，平台根据法规代政府收取的相关收入税。 |
   ^^^amount |string |99 |预估的 creator ISR 金额。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_creator_tax_iva |object | |仅适用于墨西哥 creator，平台根据法规代政府收取的相关收入税。 |
   ^^^amount |string |99 |预估的 creator IVA 金额。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_creator_tax_pit |object | |仅适用于 VN/TH/PH/ID creator，seller 根据法规代扣的相关所得税。 |
   ^^^amount |string |99 |预估的 creator PIT 金额。 |
   ^^^currency |string |USD |货币代码。 |
   ^^estimated_creator_total_earnings_after_tax |object | |creator 在与机构分成收入前的税后总收入 |
   ^^^amount |string |99 |预估的 creator 收益金额 |
   ^^^currency |string |USD |货币代码。 |
   ^^estimated_total_agency_earnings |object | |机构的税后总收入 |
   ^^^amount |string |1 |预估的机构收益金额 |
   ^^^currency |string |USD |货币代码。 |
   ^^estimated_agency_isr |object | |墨西哥机构的预估 ISR 税额 |
   ^^^amount |string |99 |税额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^estimated_agency_iva |object | |墨西哥机构的预估 IVA 税额 |
   ^^^amount |string |99 |税额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_commission_base |object | |实际 commission 基数是产品售价乘以销售数量，减去退货和退款订单。 |
   ^^^amount |string |100 |commission 基数金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_standard_commission |object | |creator 在收入分成前将获得的实际标准销售 commission |
   ^^^amount |string |100 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_bonus_commission |object | |Creator 的实际 TikTok Shop 奖励 commission。 |
   ^^^amount |string |100 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_shop_ads_commission |object | |creator 将从购买特定创意的 seller/广告主获得的实际 Shop Ads commission |
   ^^^amount |string |100 |commission 金额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_tap_bonus_commission |object | |TAP 提供给 creator 的实际 commission 奖励 |
   ^^^amount |string |100 |实际 TAP 奖励 commission 金额 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_creator_tax_isr |object | |仅适用于墨西哥 creator，平台根据法规代政府收取的相关收入税。 |
   ^^^amount |string |1 |实际 creator ISR 金额。 |
   ^^^currency |string |USD |货币代码。 |
   ^^actual_creator_tax_iva |object | |仅适用于墨西哥 creator，平台根据法规代政府收取的相关收入税。 |
   ^^^amount |string |1 |实际 creator IVA 金额。 |
   ^^^currency |string |USD |货币代码。 |
   ^^actual_creator_tax_pit |object | |仅适用于 VN/TH/PH/ID creator，seller 根据法规代扣的相关所得税。 |
   ^^^amount |string |1 |实际 creator PIT 金额。 |
   ^^^currency |string |USD |货币代码。 |
   ^^actual_creator_total_earnings_after_tax |object | |creator 在与机构分成收入前的实际税后总收入 |
   ^^^amount |string |1 |实际 creator 收益金额 |
   ^^^currency |string |USD |货币代码。 |
   ^^actual_total_agency_commission |object | |机构的实际税后总收入 |
   ^^^amount |string |1 |实际机构收益金额 |
   ^^^currency |string |USD |货币代码。 |
   ^^actual_agency_isr |object | |墨西哥机构的实际 ISR 税额 |
   ^^^amount |string |99 |税额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^actual_agency_iva |object | |墨西哥机构的实际 IVA 税额 |
   ^^^amount |string |99 |税额，不含货币符号。使用同级的 `currency` 字段来识别货币。 |
   ^^^currency |string |USD |使用的货币类型 |
   ^^fully_return |string |Yes |该 SKU 订单是否已全额退货或退款。
   可能的值：
* `Yes`：该 SKU 订单已全额退货或退款，不支付 commission。
* `No`：该 SKU 订单未被全额退货或退款。 |
   ^^settlement_time |int |1775548800 |订单 commission 结算时的 Unix 时间戳（秒）(UTC)。当没有结算时间戳时，此字段将被省略。 |
   ^^last_update_time |int |1685548800 |记录最后更新时的 Unix 时间戳（秒）(UTC)。 |
   ^^is_carousel |bool |false |轮播内容可能涉及 commission 率优惠。当 SKU 订单归因于轮播内容时返回 true。 |
   ^next_page_token |string |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT |下一页的分页 token。该 token 仅包含 search-after 排序位置；不保留搜索筛选条件或 `page_size`。如果返回此字段，请将其作为下一次请求中的 `page_token` 传入，提供有效的 `page_size`，并重新发送与第一页相同的 partner 授权上下文和请求体筛选条件。`page_size` 值可以在每页独立设置。为了稳定的分页，请在每次请求中显式提供相同的固定 `create_time_ge` 和 `create_time_lt` 值，而不是依赖滚动的默认时间范围。当此字段被省略时停止分页。当返回页面的记录数少于 `page_size` 时，此字段将被省略。 |
   ^total_count |int |100 |跨所有页面匹配当前搜索条件的 SKU 订单总数。 |

# Response Sample
```json
{"code":0,"data":{"sku_orders":[{"id":"576962796354307765","tags":"test-01","create_time":1685548800,"delivery_time":1685548800,"settle_status":"SETTLED","sku_id":"1729478689395213981","open_collaboration_id":"7324371012170024705","target_collaboration_id":"7324371012170024705","creator_username":"liuyi_id_creator1jigo","product_name":"Black Hoodie","product_id":"1729435310697057093","price":{"amount":"99","currency":"USD"},"quantity":1,"shop_name":"xuyann aaaaa","content_type":"VIDEO","content_id":"7494337156519332665","attribution_type":"Direct","commission_model":"Tiered commission","commission_tier_setting":"3 OR 5","standard_commission_rate":3000,"commission_bonus_rate":3000,"shop_ads_commission_rate":3000,"tap_bonus_commission_rate":3000,"revenue_sharing_portion_rate":3000,"estimated_commission_base":{"amount":"99","currency":"USD"},"estimated_standard_commission":{"amount":"99","currency":"USD"},"estimated_bonus_commission":{"amount":"99","currency":"USD"},"estimated_shop_ads_commission":{"amount":"99","currency":"USD"},"estimated_tap_bonus_commission":{"amount":"99","currency":"USD"},"estimated_creator_tax_isr":{"amount":"99","currency":"USD"},"estimated_creator_tax_iva":{"amount":"99","currency":"USD"},"estimated_creator_tax_pit":{"amount":"99","currency":"USD"},"estimated_creator_total_earnings_after_tax":{"amount":"99","currency":"USD"},"estimated_total_agency_earnings":{"amount":"1","currency":"USD"},"estimated_agency_isr":{"amount":"99","currency":"USD"},"estimated_agency_iva":{"amount":"99","currency":"USD"},"actual_commission_base":{"amount":"100","currency":"USD"},"actual_standard_commission":{"amount":"100","currency":"USD"},"actual_bonus_commission":{"amount":"100","currency":"USD"},"actual_shop_ads_commission":{"amount":"100","currency":"USD"},"actual_tap_bonus_commission":{"amount":"100","currency":"USD"},"actual_creator_tax_isr":{"amount":"1","currency":"USD"},"actual_creator_tax_iva":{"amount":"1","currency":"USD"},"actual_creator_tax_pit":{"amount":"1","currency":"USD"},"actual_creator_total_earnings_after_tax":{"amount":"1","currency":"USD"},"actual_total_agency_commission":{"amount":"1","currency":"USD"},"actual_agency_isr":{"amount":"99","currency":"USD"},"actual_agency_iva":{"amount":"99","currency":"USD"},"fully_return":"Yes","settlement_time":1775548800,"last_update_time":1685548800,"is_carousel":false}],"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT","total_count":100},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

