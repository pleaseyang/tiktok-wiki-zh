# 获取优惠券

# Path: /promotion/202406/coupons/{coupon_id}
# Method: [GET]
# 功能描述
使用此 API 获取与 {coupon_id} 匹配的优惠券的完整详细信息。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| coupon_id | string | 是 | 7136104329798256386 | 优惠券的唯一标识符。 |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202406/coupons/7136104329798256386?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^coupon | object |  | 优惠券详情对象，包括标识、展示设置、状态、领取和使用期限、折扣、门槛、商品范围、使用限制、使用统计和直播任务。 |
| ^^id | string | 7342461823095965461 | 标识不同优惠券的唯一 ID。 |
| ^^title | string | Coupon202407 | 卖家指定的优惠券标题。 |
| ^^display_type | string | CHAT |  |
|优惠券的展示类型。
值：

* `REGULAR`：常规优惠券，在 TTS 中所有可用的展示位置向 TikTok 用户展示，包括 PLP、PDP、TikTok 视频、直播间、创作者橱窗，并可通过 TTS 客服即时消息分享。包括针对特定客户群体的优惠券。
* `LIVE`：仅在直播间向 TikTok 用户展示的优惠券。
* `CREATOR_EXCLUSIVE`：可通过指定创作者的展示渠道（如其直播间和创作者橱窗）领取的优惠券。
* `CHAT`：可通过 TTS 客服聊天消息发送给客户的专属优惠券，但不在其他展示位置展示。
* `PROMO_CODE`：促销码在 TikTok 上没有专用的展示位置，但可以在直播、TikTok 视频或其他社交媒体平台上与客户分享。客户可以在结账时输入领取码或使用自定义促销码着陆页 URL 来领取。

|
^^status |string |NOT_START
|优惠券的促销状态。
值：

* `NOT_START`：在优惠券配置的开始时间之前对 TikTok 用户不可见。
* `ONGOING`：对 TikTok 用户可见。
* `EXPIRED`：因已过期而对 TikTok 用户不可见。
* `DEACTIVATED`：已被卖家停用，对 TikTok 用户不可见。

|
^^create_time |int |1661756811000 |优惠券创建时的 UNIX 时间戳（毫秒）。 |
^^update_time |int |1661756811000 |优惠券最后更新时的 UNIX 时间戳（毫秒）。 |
^^claim_duration |object | |优惠券的可领取期限。 |
^^^start_time |int |1709568000 |购物者可以开始领取优惠券的 UNIX 时间戳（秒）。 |
^^^end_time |int |1709654340 |购物者不能再领取优惠券的 UNIX 时间戳（秒）。 |
^^redemption_duration |object | |优惠券可以兑换（即应用于订单）的期限。 |
^^^type |string |ABSOLUTE |值：

* `ABSOLUTE`：兑换期限从 `start_time` 开始，到 `end_time` 结束。
* `RELATIVE`：兑换期限从优惠券领取时间开始，持续 `relative_time` 天。 |
   ^^^start_time |int |1709754340 |当 `type == 'ABSOLUTE'` 时，兑换期限开始的 UNIX 时间戳（秒）。 |
   ^^^end_time |int |1709768000 |当 `type == 'ABSOLUTE'` 时，兑换期限结束的 UNIX 时间戳（秒）。 |
   ^^^relative_time |int |4 |优惠券领取后可兑换的有效天数，`type = 'RELATIVE'`。 |
   ^^display_channels |[]string |["SHOPPING_CENTER"]

|优惠券可以展示或分发的渠道：

* `ALL`：所有渠道。
* `SHOPPING_CENTER`：仅在 TikTok Shop 购物中心。
* `CHAT`：仅在 TT 聊天中。
* `LIVE`：仅在 TT 直播中。
* `PRIVATE`：用于促销码。TikTok 用户在您展示之前不会知道码。
* `PRIVATE_WITH_ALLOW`：为常规优惠券返回的私有展示渠道值。
* `VIDEO`：仅在短视频中。
* `SHOWCASE`：仅在橱窗中。 |
   ^^promo_code |string |TTS12345 |促销码。仅在 `display_type == 'PROMO_CODE'` 时返回。该字符串仅包含 Unicode 字母或数字。字符串长度范围为 `[6, 12]`。 |
   ^^target_buyer_segment |string |NEW
   |优惠券的目标买家群体。可能的枚举值：
* `ALL`：所有 TTS 买家均可发现和领取。
* `NEW`：从未在您店铺购买过的客户。
* `REPEAT_CUSTOMERS`：之前在您店铺下过单并在一定天数内（非美国 30 天，美国 90 天）再次购买的人。
* `RECENT_CUSTOMERS`：在过去一定天数内（非美国 30 天，美国 90 天）首次在您店铺购买的人。
* `FREQUENT_CUSTOMERS`：在过去 90 天内购买超过 1 次的客户。
* `LAPSED_CUSTOMERS`：在过去 365 天内至少有 1 次购买但在最近一定天数内（非美国 90 天，美国 30 天）没有购买的客户。
* `NEW_FOLLOWERS`：在过去 30 天内开始关注您店铺 TikTok 账号的人。
* `EXISTING_ACTIVE_FOLLOWERS`：关注了您店铺的 TikTok 账号并在过去 30 天内通过直播、短视频或商品卡与您店铺互动的人。
   |
   ^^usage_limits |object | |优惠券使用限制。 |
   ^^^single_buyer_claim_limit |int |30 |单个买家可以领取优惠券的次数。 |
   ^^^total_claim_limit |int |1000 |所有买家可领取优惠券的总次数。 |
   ^^^redemption_limit |int |1000 |已领取优惠券可被所有买家兑换的总次数。（仅在 ID、MY、PH、TH、SG、VN 地区可用。） |
   ^^usage_stats |object | |使用统计 |
   ^^^claimed_count |int |5 |优惠券已被领取的次数。 |
   ^^^redeemed_count |int |0 |优惠券已被兑换（即应用于订单）的次数。 |
   ^^discount |object | |优惠券折扣配置，包括类型、reduction_amount、percentage 和 max_discount。 |
   ^^^type |string |AMOUNT_OFF |优惠券提供的折扣类型。可能的枚举值：
* `AMOUNT_OFF`：按指定的 `reduction_amount` 降低商品最终价格。
* `PERCENT_OFF`：按指定的 `percentage` 降低商品最终价格。 |
   ^^^reduction_amount |object | |当 `type == 'AMOUNT_OFF'` 时出现。 |
   ^^^^amount |string |30.5 |`AMOUNT_OFF` 折扣的货币价值。 |
   ^^^^currency |string |USD |折扣金额的货币。 |
   ^^^percentage |string |30 |优惠券提供的折扣百分比。当 `type == 'PERCENT_OFF'` 时出现。 |
   ^^^max_discount |object | |当 `type == "PERCENT_OFF"` 时，折扣总额可选的货币上限。 |
   ^^^^amount |string |40 |`max_discount` 的货币价值。 |
   ^^^^currency |string |USD |`max_discount` 的货币。 |
   ^^threshold |object | |可选的最低购买条件，必须满足才能获得优惠券折扣。 |
   ^^^type |string |MIN_SPEND |购买条件的类型。可能的枚举值：
* `NONE`：无最低购买条件。
* `MIN_SPEND`：买家必须购买达到或超过最低消费条件的符合条件的商品。 |
   ^^^min_spend |object |MIN_SPEND |当 `threshold.type == 'MIN_SPEND'` 时，客户必须从 `product_scope` 定义的范围内购买金额大于或等于此值的商品，否则客户无法使用该优惠券。 |
   ^^^^amount |string |30 |`min_spend` 的货币价值。 |
   ^^^^currency |string |USD |`min_spend` 门槛的货币。 |
   ^^product_scope |string |FULL_SHOP |优惠券适用的商品范围。可能的枚举值：
* `FULL_SHOP`：店铺中销售的所有商品均可使用优惠券。
* `SPECIFIC_PRODUCTS`：仅指定商品可使用优惠券。指定商品列表在 `get_coupon` API 的响应中返回。 |
   ^^product_ids |[]string |["1729581162206365900"] |当 `product_scope == 'SPECIFIC_PRODUCTS'` 时符合条件的商品 ID。 |
   ^^seller_tnc |string |terms & conditions: xxx |卖家在配置优惠券时可选上传的自定义条款和条件。 |
   ^^creation_source |string |SELLER_CENTER |优惠券创建的系统来源：
* `SELLER_CENTER`：通过 TikTok 卖家中心的促销部分创建。
* `SELLER_APP`：通过 TikTok 卖家移动应用创建。
* `TTS_CRM`：通过 TikTok Shop CRM 创建。 |
   ^^live_tasks |[]object | |购物者在领取 TikTok 直播分发的优惠券之前必须完成的任务。仅存在于美国和英国的 LIVE 优惠券中。 |
   ^^^type |string |FOLLOW_HOST |可能的枚举值：
* `NONE`：直播间中的任何购物者均可领取优惠券。
* `FOLLOW_HOST`：购物者必须先关注直播主持人才能领取优惠券。
* `WATCH_FOR_MIN_TIME`：购物者必须观看直播达到 `min_watch_time` 指定的时间才能领取优惠券。 |
   ^^^min_watch_time |string |60 |购物者必须观看直播以领取优惠券的秒数。 |

# 响应示例
```json
{"code":0,"data":{"coupon":{"id":"7342461823095965461","title":"Coupon202407","display_type":"CHAT\n\n\n","status":"NOT_START\n\n\n\n","create_time":1661756811000,"update_time":1661756811000,"claim_duration":{"start_time":1709568000,"end_time":1709654340},"redemption_duration":{"type":"ABSOLUTE","start_time":1709754340,"end_time":1709768000,"relative_time":4},"display_channels":["SHOPPING_CENTER"],"promo_code":"TTS12345","target_buyer_segment":"NEW\n","usage_limits":{"single_buyer_claim_limit":30,"total_claim_limit":1000,"redemption_limit":1000},"usage_stats":{"claimed_count":5,"redeemed_count":0},"discount":{"type":"AMOUNT_OFF","reduction_amount":{"amount":"30.5","currency":"USD"},"percentage":"30","max_discount":{"amount":"40","currency":"USD"}},"threshold":{"type":"MIN_SPEND","min_spend":{"amount":"30","currency":"USD"}},"product_scope":"FULL_SHOP","product_ids":["1729581162206365900"],"seller_tnc":"terms \u0026 conditions: xxx","creation_source":"SELLER_CENTER","live_tasks":[{"type":"FOLLOW_HOST","min_watch_time":"60"}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

