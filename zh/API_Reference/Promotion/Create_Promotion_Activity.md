# 创建 Promotion 活动

# Path: /promotion/202309/activities
# Method: [POST]
# 功能描述
创建固定价格、百分比折扣、限时抢购、运费折扣、买更多省更多、满赠或买XGetY促销活动。无法通过此 API 创建 coupon；请在卖家中心或卖家应用中创建。要更新活动中包含的商品或 SKU，请使用[更新活动商品](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c)。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| title | string | Y | DiscountEvent0829 | 所有活动中的唯一名称。最大长度：`FLASHSALE` 和 `SHIPPING_DISCOUNT` 为 50 个字符；`FIXED_PRICE`、`DIRECT_DISCOUNT`、`BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y` 和 `GIFT_WITH_PURCHASE` 为 100 个字符。 |
| activity_type | string | Y | FIXED_PRICE | promotion 活动类型。 |
| 可能的值： |  |  |  |  |

* `FIXED_PRICE`：固定价格的商品折扣活动。
* `DIRECT_DISCOUNT`：百分比折扣的商品折扣活动。
* `FLASHSALE`：限时抢购活动。
* `SHIPPING_DISCOUNT`：运费折扣活动。
* `BUY_MORE_SAVE_MORE`：买更多省更多活动。
* `GIFT_WITH_PURCHASE`：满赠活动。
* `BUY_X_GET_Y`：买XGetY活动。 |
   product_level |string |Y |PRODUCT |活动的商品范围。
   可能的值：
* `PRODUCT`：在商品 (SPU) 级别应用 promotion，涵盖所选商品的所有 SKU。
* `VARIATION`：仅将 promotion 应用于所选 SKU。
* `SHOP`：将 promotion 应用于店铺中的所有商品。

活动特定约束：

* `FIXED_PRICE`、`DIRECT_DISCOUNT` 和 `FLASHSALE` 支持 `PRODUCT` 或 `VARIATION`。
* `SHIPPING_DISCOUNT` 不支持 `VARIATION`。
* `BUY_MORE_SAVE_MORE` 和 `BUY_X_GET_Y` 支持 `PRODUCT` 或 `SHOP`。
* `GIFT_WITH_PURCHASE` 需要 `PRODUCT`。

要设置活动覆盖的商品或 SKU，请使用[更新活动商品](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c)。 |
duration_type |string |N |NORMAL |当前活动的生效时间类型

* NORMAL：必须填写 `begin_time` 和 `end_time`
* INDEFINITE：不需要填写 `begin_time` 和 `end_time`，promotion 将作为长期活动无限期运行。
1. `INDEFINITE` 仅在 `activity_type` 为 `SHIPPING_DISCOUNT` 时有效，
2. 如果 `duration_type` 为 `INDEFINITE`，`start_time` 和 `end_time` 应为 0
   默认值：NORMAL |
   begin_time |int |Y |1661756811 |活动开始时间。UNIX 时间戳。该值必须大于当前时间的值。 |
   end_time |int |Y |1661856811 |活动结束时间，以秒为单位的 Unix 时间戳。对于 `NORMAL` 类型的 `FIXED_PRICE`、`DIRECT_DISCOUNT`、`FLASHSALE`、`BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y` 和 `GIFT_WITH_PURCHASE` 活动，结束时间必须比开始时间至少晚 600 秒。对于 `NORMAL` 类型的运费折扣活动，请提供正值。 |
   participation_limit |[]object |N | |买家参与限制设置。对于 `BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y` 和 `GIFT_WITH_PURCHASE`，请提供一个条目。 |
   ^type |string |Y |BUYER_NO_LIMIT |决定每个买家是否可以多次享受活动优惠。
   可能的值：
* `BUYER_NO_LIMIT`：买家可以在多个订单中享受此活动的优惠。
* `BUYER_LIMIT_ONLY_ONE`：买家只能在一个订单中享受此活动的优惠。 |
   discount |object |N | |折扣配置。对于 `SHIPPING_DISCOUNT`，提供 `shipping_discount`；对于 `BUY_MORE_SAVE_MORE`，提供 `bmsm_discount`；对于 `GIFT_WITH_PURCHASE`，提供 `gift_discount`；对于 `BUY_X_GET_Y`，提供 `bxgy_discount`。此字段不用于 `FIXED_PRICE`、`DIRECT_DISCOUNT` 或 `FLASHSALE`。 |
   ^shipping_discount |object |N | |运费折扣的配置，包括购买条件、折扣值、配送方式、库存类型和区域范围。 |
   ^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |购买条件类型。可能的枚举值：
* `NO_THRESHOLD`：无最低购买条件。
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家的订单金额必须达到或超过最低消费条件。
   `MINIMAL_ITEM_QUANTITY` 和 `MINIMAL_ORDER_AMOUNT` 仅在 `product_level==SHOP` 时可以设置。 |
   ^^threshold_value |string |N |3 |折扣的购买阈值，基于 `threshold_type`，例如 `3`。由用户确定。
* 当 `threshold_type==NO_THRESHOLD` 时，不需要此值。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，买家必须购买至少指定数量的符合条件的商品（例如，3 件符合条件的商品）。如果表示数量，则必须为整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，符合条件的商品小计必须达到或超过以本地货币指定的值（例如，3 单位本地货币）。如果表示订单金额，则最多保留两位小数。 |
   ^^type |string |Y |DISCOUNT_SHIPPING_FEE |运费优惠类型。
* `FREE_SHIPPING`：将买家的运费降至零。
* `DISCOUNT_SHIPPING_FEE`：将买家的运费减免最多 `shipping_discount.value` 中指定的金额。 |
   ^^value |string |N |10.5 |由 `type` 决定的运费折扣值。
* 当 `type==FREE_SHIPPING` 时，省略此值。
* 当 `type==DISCOUNT_SHIPPING_FEE` 时，输入从买家运费中扣除的最大金额（以本地货币计），最多两位小数。 |
   ^^shipping_method |string |N |STANDARD_SHIPPING |此 promotion 适用的配送方式。
* 当 `STANDARD_SHIPPING`：仅适用于标准配送方式，包括经济配送。
* `EXPRESS_SHIPPING`：仅适用于快速配送方式。
* `ALL_SHIPPING_METHOD`：适用于店铺提供的所有配送方式。
   默认值：`STANDARD_SHIPPING` |
   ^^inventory_type |string |N |SELF_FULFILLED |promotion 活动适用的库存类型：
* `SELF_FULFILLED`：仅适用于从卖家仓库发货的库存。
* `FULFILLED_BY_TIKTOK`：仅适用于由 TikTok 从 FBT（Fulfilled by TikTok）仓库发货的库存。
* `ALL`：适用于符合条件商品的所有库存。
   对于美国全店免运费活动（`product_level` == `SHOP`），默认为 `ALL`，且 `inventory_type` 不能仅设置为 `SELF_FULFILLED` 或仅设置为 `FULFILLED_BY_TIKTOK`。
   对于其他地区，默认为 `SELF_FULFILLED`。`FULFILLED_BY_TIKTOK` 和 `ALL` 仅在 `product_level` == `SHOP` 且 `threshold_type` = `NO_THRESHOLD` 时可以设置。 |
   ^^area_scope |object |Y | |promotion 活动适用的（买家）地理区域。 |
   ^^^type |string |Y |WHOLE |promotion 活动适用的（买家）地理区域。
   - `WHOLE`：promotion 活动适用于卖家提供配送的所有区域。
* `SPECIFIC_AREAS`：仅适用于 `area_scope.specific_areas` 中定义的特定配送区域。 |
   ^^^specific_areas |[]string |N |["Washington", "New York"] |promotion 活动适用的区域列表。可包含在此列表中的有效值取决于店铺所在区域。每个店铺区域的有效值列表可在此处获取：[链接](https://partner.tiktokshop.com/docv2/page/67e3b059e7dc4f04a4ff9e09) |
   ^bmsm_discount |object |N | |买更多省更多 (BMSM) 活动的相关配置。 |
   ^^details |[]object |N | |买更多省更多层级配置。提供一个或两个层级。所有层级的 `threshold_type` 和 `type` 必须相同。 |
   ^^^tier |int |Y |1 |`tier` 使用从 1 开始的索引：第一层和第二层分别为 `1` 和 `2`，而不是 `0` 和 `1`。对于每个后续层级，`threshold_value` 和 `value` 都必须大于前一层级的对应值。例如，如果第 `1` 层的 `threshold_value` 为 `20`，`value` 为 `15`，则第 `2` 层的 `threshold_value` 必须大于 `20`，`value` 必须大于 `15`。 |
   ^^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |购买条件类型。可能的枚举值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家的订单金额必须达到或超过最低消费条件。 |
   ^^^threshold_value |string |Y |5 |此层级的购买阈值。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，输入正整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，输入以本地货币计的正数金额，最多两位小数。 |
   ^^^type |string |Y |PERCENTAGE_OFF |作为优惠的折扣类型。折扣值由 `value` 决定。
   可能的枚举值：
* `PERCENTAGE_OFF`：买家将获得符合条件的商品价格的 X% 折扣。
* `AMOUNT_OFF`：买家将获得符合条件的商品价格减免 X 单位本地货币。 |
   ^^^value |string |Y |10 |折扣值。
* 当 `type==PERCENTAGE_OFF` 时，输入正整数百分比。
* 当 `type==AMOUNT_OFF` 时，输入以本地货币计的正数金额，最多两位小数。 |
   ^gift_discount |object |N | |满赠 (GWP) 活动的相关配置。仅需为满赠活动配置。 |
   ^^gift_receiving_type |string |Y |ALL_RECEIVE |礼品领取类型。目前仅支持一种类型：
* `ALL_RECEIVE`：可以领取活动中配置的所有礼品。 |
   ^^gift_infos |[]object |Y | |满赠 (GWP) 层级配置。至少提供一个层级。东南亚和英国最多允许两个层级，而美国仅允许一个层级。所有层级的 `threshold_type` 必须相同。 |
   ^^^tier |int |Y |1 |`tier` 使用从 1 开始的索引，即第一层和第二层计为"1、2"，而不是"0、1"。
   给定层级的 `threshold_value` 必须大于前一层级的值。
   例如：如果 `tier`<span style="background-color: #ff0">1 的 </span><span style="background-color: #ff0"><code>threshold_value</code></span>`2`，则 `tier`==2 的 `threshold_value` 必须 > `2`。 |
   ^^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |折扣的购买阈值类型。可能的枚举值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家的订单金额必须达到或超过最低消费条件。 |
   ^^^threshold_value |string |Y |3 |获得礼品的购买阈值，由 `threshold_type` 决定。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，输入符合条件的商品的正整数数量。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，输入以本地货币计的符合条件的商品正数小计金额，最多两位小数。 |
   ^^^gift_details |[]object |Y | |此层级的礼品 SKU。在所有层级中，至少提供一个礼品 SKU，且不要在整个活动中重复相同的 sku_id。对于 MINIMAL_ITEM_QUANTITY 层级，此列表不能为空。 |
   ^^^^product_id |string |Y |1732239744891062847 |礼品的 TikTok Shop 商品 id。 |
   ^^^^sku_id |string |Y |1732239787859544639 |礼品的 TikTok Shop sku id。 |
   ^^^^total_claim_limit |string |Y |100 |此活动中礼品 SKU 的总领取限制。输入 `1` 到 `99999` 之间的整数。 |
   ^bxgy_discount |object |N | |买XGetY (BXGY) 活动的相关配置。仅需为 BXGY 活动配置。 |
   ^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |购买条件。
   可能的值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买至少配置数量的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：符合条件的商品小计必须达到配置的金额。 |
   ^^threshold_value |string |Y |5 |由 `threshold_type` 决定的购买阈值。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，输入不超过 `10` 的正整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，输入以本地货币计的符合条件的商品正数小计金额，最多两位小数。 |
   ^^discount_type |string |Y |AMOUNT_OFF_EACH |优惠类型。
   可能的值：
* PERCENTAGE_OFF：将 `discount_value` 指定的百分比应用于符合条件的商品。
* FREE：免费提供配置数量的符合条件的商品。
* AMOUNT_OFF_EACH：从每个符合条件的商品价格中扣除 `discount_value` 指定的本地货币金额。 |
   ^^discount_value |string |Y |5 |折扣值。
* 当 `type`==`PERCENTAGE_OFF` 时，买家将获得符合条件的商品价格的 X% 折扣。如果该值表示百分比，则应为整数。
* 当 `type`==`AMOUNT_OFF_EACH` 时，买家将获得每个符合条件的商品价格减免 X 单位本地货币。如果该值表示金额，则最多保留两位小数。
   |
   ^^benefit_max_applicable_quantity |string |Y |5 |每次应用买XGetY优惠时 awarded 的商品 Y 的数量。输入不超过 `20` 的正整数。 |
   ^^benefit_max_applicable_times |string |N |5 |可选。买XGetY优惠在单个订单中最多可应用的次数。输入不超过 `50` 的正整数。 |
   target_user_info |object |N | |`BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y` 和 `GIFT_WITH_PURCHASE` 活动的目标受众配置。如果省略，则活动面向 `ALL_USER`。 |
   ^user_type |string |N |ALL_USER |可能的枚举值：
   `ALL_USER`
   `SHOP_NEW_CUSTOMER`
   `SHOP_EXISTING_CUSTOMER`
   `SHOP_REPEAT_CUSTOMER` |
   auction_support_type |string |N |ALL |对于 `SHIPPING_DISCOUNT` 活动，决定是否支持拍卖商品。
   可能的值：
* `ALL`：同时支持普通商品和拍卖商品。
* `EXCLUDE_AUCTION`：排除拍卖商品。
   默认值：`ALL`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202309/activities?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"title":"DiscountEvent0829","activity_type":"FIXED_PRICE","product_level":"PRODUCT","duration_type":"NORMAL","begin_time":1661756811,"end_time":1661856811,"participation_limit":[{"type":"BUYER_NO_LIMIT"}],"discount":{"shipping_discount":{"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"3","type":"DISCOUNT_SHIPPING_FEE","value":"10.5","shipping_method":"STANDARD_SHIPPING","inventory_type":"SELF_FULFILLED","area_scope":{"type":"WHOLE","specific_areas":["Washington","New York"]}},"bmsm_discount":{"details":[{"tier":1,"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"5","type":"PERCENTAGE_OFF","value":"10"}]},"gift_discount":{"gift_receiving_type":"ALL_RECEIVE","gift_infos":[{"tier":1,"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"3","gift_details":[{"product_id":"1732239744891062847","sku_id":"1732239787859544639","total_claim_limit":"100"}]}]},"bxgy_discount":{"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"5","discount_type":"AMOUNT_OFF_EACH","discount_value":"5","benefit_max_applicable_quantity":"5","benefit_max_applicable_times":"5"}},"target_user_info":{"user_type":"ALL_USER"},"auction_support_type":"ALL"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^activity_id | string | 7136104329798256386 | 成功时，创建的活动的 ID。在使用[更新活动商品](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c)添加商品或 SKU 时用作 `activity_id`。 |
| ^create_time | int | 1661756811 | 活动创建时间。 |
| ^update_time | int | 1661756811 | 活动最后更新时间。 |
| ^status | string | ONGOING | 可能的值： |

* DRAFT：具有此状态的 promotion 活动不对 TikTok 用户开放。
* NOT_START：具有此状态的 promotion 活动在设定的活动开始时间之前不对 TikTok 用户开放。
* ONGOING：具有此状态的 promotion 活动对对 TikTok 用户开放。
* EXPIRED：具有此状态的 promotion 活动因已过期而不对 TikTok 用户开放。
* DEACTIVATED：活动已被卖家停用，不对 TikTok 用户开放。
* NOT_EFFECTIVE：活动已被平台终止，不对 TikTok 用户开放。 |

# 响应示例
```json
{"code":0,"data":{"activity_id":"7136104329798256386","create_time":1661756811,"update_time":1661756811,"status":"ONGOING"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 17003203 | 已存在一个全店免运费 promotion 活动。一次只能创建一个。 |
| 17029001 | 参数无效 |
| 17029002 | 标题长度过长 |
| 17029004 | 活动标题重复。 |
| 17029005 | 开始时间早于当前时间 |
| 17029006 | 活动周期太短。 |
| 17029007 | 活动周期太长。 |
| 17029008 | 限时抢购周期太长 |
| 17029026 | 卖家 ID 无效 |
| 17029027 | RequestSerialNo 为空 |
| 17029035 | 店铺风险检查失败 |
| 17029036 | 不支持的 ActivityType。 |
| 17029049 | 不支持的 ActivityVersion。 |
| 17029052 | 不支持的 ProductType |
| 17029068 | 您所在的地区不支持所选的 `inventory_type`。 |
| 17029070 | 礼品 sku 信息为空。 |
| 17029071 | 礼品 sku id 无效，不是整数。 |
| 17029072 | 礼品 sku 重复 |
| 17029073 | 礼品价格超过上限 |
| 17029074 | 符合条件的商品和礼品不能是同一商品。 |
| 17029075 | 每层级的礼品数量不符合限制 |
| 17029076 | 礼品 sku 库存不足。 |
| 17029077 | 不同层级的礼品重复 |
| 17029078 | 礼品层级数量不符合要求 |
| 17029082 | 指定的时间不在此活动的定义范围内。请检查活动的时间范围并重试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
