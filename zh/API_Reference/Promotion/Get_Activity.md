# 获取活动详情

# Path: /promotion/202309/activities/{activity_id}
# Method: [GET]
# 功能描述
获取促销活动的详细信息。已结束超过 180 天的 `FIXED_PRICE`、`DIRECT_DISCOUNT` 和 `FLASHSALE` 活动的商品信息将不会返回。对于 coupon 活动，请使用[获取优惠券](6699dce0de15e502ed219e37)。

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
| activity_id | string | 是 | 7402881377634567979 | 活动 ID |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202309/activities/7402881377634567979?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^activity_id | string | 7136104329798256386 | 标识不同活动的唯一 ID。 |
| ^title | string | FlashSale 20230707 | 活动名称（最多 50 个字符）。名称必须唯一。 |
| ^activity_type | string | FIXED_PRICE | 活动类型。 |
| 可能的值： |  |  |  |

* `FIXED_PRICE`：固定价格的商品折扣活动。
* `DIRECT_DISCOUNT`：百分比折扣的商品折扣活动。
* `FLASHSALE`：限时抢购活动。
* `SHIPPING_DISCOUNT`：运费折扣活动。
* `BUY_MORE_SAVE_MORE`：多买多省促销活动。
* `GIFT_WITH_PURCHASE`：买赠活动。
* `BUY_X_GET_Y`：买 X 得 Y 活动。 |
   ^duration_type |string |NORMAL |当前活动的生效时间类型
* NORMAL：必须填写 `begin_time` 和 `end_time`
* INDEFINITE：不需要填写 `begin_time` 和 `end_time`，促销将作为长期活动无限期运行。
1. `INDEFINITE` 仅在 `activity_type` 为 `SHIPPING_DISCOUNT` 时有效，
2. 如果 `duration_type` 为 `INDEFINITE`，`start_time` 和 `end_time` 应为 0
   默认值：NORMAL |
   ^begin_time |int |1661756811 |活动开始时间，UNIX 时间戳（秒）。 |
   ^end_time |int |1661856811 |活动结束时间，UNIX 时间戳（秒）。 |
   ^participation_limit |[]object | |买家可以参与促销的次数。 |
   ^^type |string |BUYER_NO_LIMIT |决定促销活动是否限制每个买家享受优惠的次数。例如：
* `BUYER_NO_LIMIT`：不限制买家。买家可以在多个订单中享受此促销优惠。
* `BUYER_LIMIT_ONLY_ONE`：买家最多只能在一个订单中享受此促销活动优惠。
   默认值：`BUYER_NO_LIMIT` |
   ^products |[]object | |商品列表。
   注意：如果 `FIXED_PRICE`、`DIRECT_DISCOUNT` 和 `FLASHSALE` 活动已结束超过 180 天，此字段为空。 |
   ^^id |string |7136011254174631686 |TikTok Shop 商品 ID。 |
   ^^activity_price |object | |活动价格。 |
   ^^^amount |string |70500 |活动价格金额。 |
   ^^^currency |string |IDR |活动价格的货币单位。 |
   ^^quantity_limit |int |-1 |活动涉及商品的数量限制。范围为 `[1, 99]`，或 `-1` 表示不限。 |
   ^^quantity_per_user |int |-1 |每个买家的商品购买限制。范围为 `[1, 99]`，或 `-1` 表示不限。 |
   ^^discount |string |10 |折扣值。如果商品打 9 折（即 10% off），则值为 `10`。仅在 `activity_type==DIRECT_DISCOUNT` 且 `product_level==PRODUCT` 时可用。 |
   ^^skus |[]object | |仅在 `product_level==VARIATION` 时可用。 |
   ^^^id |string |7136382541418366725 |TikTok Shop SKU ID。 |
   ^^^discount |string |10 |折扣值。如果 SKU 打 9 折（即 10% off），则值为 `10`。仅在 `activity_type==DIRECT_DISCOUNT` 时可用。 |
   ^^^quantity_limit |int |-1 |活动涉及 SKU 的数量限制。范围为 `[1, 99]`，或 `-1` 表示不限。 |
   ^^^quantity_per_user |int |-1 |每个买家的 SKU 购买限制。范围为 `[1, 99]`，或 `-1` 表示不限。 |
   ^^^activity_price |object | |活动价格。仅在 `activity_type==FIXED_PRICE/FLASHSALE` 时可用。 |
   ^^^^amount |string |70500 |活动价格金额。 |
   ^^^^currency |string |IDR |活动价格的货币单位。 |
   ^^^used_quantity |int |3 |已在活动中生效的 SKU 数量。 |
   ^^used_quantity |int |3 |已在活动中生效的商品数量。 |
   ^status |string |ONGOING |活动状态。
   可能的值：
* DRAFT：此状态的促销活动对 TikTok 用户不可见。
* NOT_START：此状态的促销活动在设定的活动开始时间之前对 TikTok 用户不可见。
* ONGOING：此状态的促销活动对 TikTok 用户可见。
* EXPIRED：此状态的促销活动因已过期而对 TikTok 用户不可见。
* DEACTIVATED：活动已被卖家停用，对 TikTok 用户不可见。
* NOT_EFFECTIVE：活动已被平台终止，对 TikTok 用户不可见。 |
   ^create_time |int |1789355787347 |活动创建时间，UNIX 时间戳（毫秒）。 |
   ^update_time |int |1789355865063 |活动更新时间，UNIX 时间戳（毫秒）。 |
   ^product_level |string |PRODUCT |活动商品维度，值为：
* PRODUCT：商品级别的促销活动。
* VARIATION：SKU 级别的促销活动。
* SHOP：店铺级别的促销活动。 |
   ^activity_commands |[]string |["IMMUTABLE"] |适用于活动的命令：
* IMMUTABLE：活动不可编辑或停用 |
   ^discount |object | |特定类型的折扣信息。对于 `FIXED_PRICE`、`DIRECT_DISCOUNT` 和 `FLASHSALE` 活动，此字段会被省略。对于其他支持的活动类型，请使用对应的嵌套折扣对象（在返回时）。 |
   ^^shipping_discount |object | |运费折扣 |
   ^^^threshold_type |string |MINIMAL_ITEM_QUANTITY |购买条件的类型。可能的枚举值：
* `NO_THRESHOLD`：无最低购买条件。
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家必须购买达到或超过最低消费条件的符合条件的订单。
   `MINIMAL_ITEM_QUANTITY` 和 `MINIMAL_ORDER_AMOUNT` 仅在 `product_level==SHOP` 时可设置。 |
   ^^^threshold_value |string |3 |基于 `threshold_type` 返回的运费折扣购买门槛。
* 当 `threshold_type==NO_THRESHOLD` 时，不需要此值。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，这是买家必须购买的符合条件的商品数量，必须为整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，这是买家必须达到的符合条件的商品小计金额（以当地货币计，例如 3 单位当地货币），最多保留两位小数。 |
   ^^^type |string |DISCOUNT_SHIPPING_FEE |促销活动返回的运费折扣类型。
* FREE_SHIPPING：买家的运费由平台全额承担。
* DISCOUNT_SHIPPING_FEE：买家的运费最高减免 value 中的金额。 |
   ^^^value |string |10.5 |折扣值。
* 当 `type==FREE_SHIPPING` 时，不需要此值。
* `type==DISCOUNT_SHIPPING_FEE` 时，此值为从买家运费价格中扣除的最高金额（以当地货币计）。
   该值应限制为最多两位小数。 |
   ^^^shipping_method |string |STANDARD_SHIPPING |此促销适用的配送方式。
* 当 `STANDARD_SHIPPING` 时：仅适用于标准配送方式，包括经济配送。
* `EXPRESS_SHIPPING`：仅适用于快速配送方式。
* `ALL_SHIPPING_METHOD`：适用于店铺提供的所有配送方式。
   默认值：`STANDARD_SHIPPING` |
   ^^^inventory_type |string |SELF_FULFILLED |促销活动适用的库存类型：
* `SELF_FULFILLED`：仅适用于从卖家仓库发货的库存。
* `FULFILLED_BY_TIKTOK`：仅适用于由 TikTok 从 FBT（Fulfilled by TikTok）仓库发货的库存。
* `ALL`：适用于符合条件商品的所有库存。
   默认值：`SELF_FULFILLED`
   `FULFILLED_BY_TIKTOK` 和 `ALL` 仅在 `product_level`==`SHOP` 且 `threshold_type=NO_THRESHOLD` 时可设置。 |
   ^^^area_scope |object | |促销活动适用的（买家）地理区域。 |
   ^^^^type |string |WHOLE |促销活动适用的（买家）地理区域。
   - `WHOLE`：促销活动适用于卖家提供配送的所有区域。
* `SPECIFIC_AREAS`：仅适用于 `area_scope.specific_areas` 中定义的特定配送区域。 |
   ^^^^specific_areas |[]string |["Washington","New York"] |促销活动适用的区域列表。此列表中可包含的有效值取决于店铺所在地区。每个店铺地区的有效值列表可在此处查看：[链接](https://partner.tiktokshop.com/docv2/page/67e3b059e7dc4f04a4ff9e09) |
   ^^bmsm_discount |object | |与多买多省（BMSM）促销活动相关的配置。 |
   ^^^details |[]object | |多买多省（BMSM）促销活动的配置。
   最多允许两个 `tier`。所有 `tier` 中的 `details.threshold_type` 和 `details.type` 必须相同。 |
   ^^^^tier |int |1 |`tier` 使用从 1 开始的索引，即第一档和第二档计为"1、2"，而不是"0、1"。
   给定档位的 `threshold_value` 和 `value` 必须大于前一档位。
   例如：如果 `tier`<span style="background-color: #ff0">1 的 </span><span style="background-color: #ff0"><code>threshold_value</code></span>`20` 且 `value`== `15`，则 `tier`==2 必须有 `threshold_value` > `20` 且 `value`>`15`。 |
   ^^^^threshold_type |string |MINIMAL_ITEM_QUANTITY |购买条件的类型。可能的枚举值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家必须购买达到或超过最低消费条件的符合条件的订单。 |
   ^^^^threshold_value |string |5 |基于 `threshold_type` 的折扣购买门槛，例如"3"。由用户确定。
* 当 `threshold_type==NO_THRESHOLD` 时，不需要此值。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，买家必须至少购买指定数量的符合条件的商品（例如必须购买 3 件或更多符合条件的商品才能享受优惠）。如果表示数量，则必须为整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，买家订单的符合条件的商品小计必须达到或超过指定的当地货币订单金额（例如买家订单小计必须至少 $3 才能享受优惠）。如果表示订单金额，则必须限制为最多两位小数。 |
   ^^^^type |string |PERCENTAGE_OFF |作为优惠的折扣类型。折扣值由 `value` 确定。
   可能的枚举值：
* `PERCENTAGE_OFF`：买家将获得符合条件的商品价格 X% 的折扣。
* `AMOUNT_OFF`：买家将获得符合条件的商品价格 X 单位当地货币的折扣。 |
   ^^^^value |string |10 |折扣值。
* 当 `type`==`PERCENTAGE_OFF` 时，买家将获得符合条件的商品价格 X% 的折扣。如果值表示百分比，则应为整数。
* `type`==`AMOUNT_OFF` 时，买家将获得符合条件的商品价格 X 单位当地货币的折扣。如果值表示金额，则应限制为最多两位小数。
   |
   ^^gift_discount |object | |与买赠（GWP）促销活动相关的配置。仅需为 GWP 促销活动配置。 |
   ^^^gift_receiving_type |string |ALL_RECEIVE |赠品领取类型。目前仅支持一种类型：`ALL_RECEIVE` |
   ^^^gift_infos |[]object | |关于买赠（GWP）促销活动的配置。
   东南亚和英国最多允许两个 `tier`。美国仅允许一个 `tier`。所有 `tier` 中的 `threshold_type` 必须相同。 |
   ^^^^tier |int |1 |`tier` 使用从 1 开始的索引，即第一档和第二档计为"1、2"，而不是"0、1"。
   给定档位的 `threshold_value` 必须大于前一档位。
   例如：如果 `tier`<span style="background-color: #ff0">1 的 </span><span style="background-color: #ff0"><code>threshold_value</code></span>`2`，则 `tier`==2 必须有 `threshold_value` > `2`。 |
   ^^^^threshold_type |string |MINIMAL_ITEM_QUANTITY |折扣的购买门槛类型。可能的枚举值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家必须购买达到或超过最低消费条件的符合条件的订单。 |
   ^^^^threshold_value |string |3 |基于 `threshold_type` 的赠品购买门槛值。由用户确定。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，买家必须至少购买指定数量的符合条件的商品（例如 3 件符合条件的商品）。如果表示数量，则必须为整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，符合条件的商品小计必须达到或超过指定的当地货币金额（例如 3 单位当地货币）。如果表示订单金额，则必须限制为最多两位小数。 |
   ^^^^gift_details |[]object | |与买赠（GWP）促销活动相关的赠品配置。 |
   ^^^^^product_id |string |1732239744891062847 |赠品的 TikTok Shop 商品 ID。 |
   ^^^^^sku_id |string |1732239787859544639 |赠品的 TikTok Shop SKU ID。 |
   ^^^^^total_claim_limit |string |100 |活动涉及的赠品 SKU 的数量限制。范围为 [1, 99999]。如果更新现有 SKU 的值，则不能减小该值。 |
   ^^bxgy_discount |object | |与买 X 得 Y（BXGY）促销活动相关的配置。仅需为 BXGY 促销活动配置。 |
   ^^^threshold_type |string |MINIMAL_ITEM_QUANTITY |活动返回的购买条件。
   可能的值：
* `MINIMAL_ITEM_QUANTITY`：买家必须至少购买指定数量的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：符合条件的商品小计必须达到指定金额。 |
   ^^^threshold_value |string |5 |基于 `threshold_type` 返回的活动购买门槛。
* 当 `threshold_type==MINIMAL_ITEM_QUANTITY` 时，这是买家必须购买的符合条件的商品数量，必须为整数。
* 当 `threshold_type==MINIMAL_ORDER_AMOUNT` 时，这是买家必须达到的符合条件的商品小计金额（以当地货币计）。 |
   ^^^discount_type |string |AMOUNT_OFF_EACH |作为优惠的折扣类型。对于 PERCENTAGE_OFF 和 AMOUNT_OFF_EACH，折扣金额由 `discount_value` 确定。
   可能的枚举值：
* `PERCENTAGE_OFF`：买家将获得符合条件的商品价格 X% 的折扣。
* `FREE`：买家将免费获得 X 件符合条件的商品。
* `AMOUNT_OFF_EACH`：买家将获得每件符合条件的商品价格 X 单位当地货币的折扣。 |
   ^^^discount_value |string |10 |折扣值。
* 当 `type`==`PERCENTAGE_OFF` 时，买家将获得符合条件的商品价格 X% 的折扣。如果值表示百分比，则应为整数。
* `type`==`AMOUNT_OFF_EACH` 时，买家将获得每件符合条件的商品价格 X 单位当地货币的折扣。如果值表示金额，则应限制为最多两位小数。
   |
   ^^^benefit_max_applicable_quantity |string |5 |BXGY 促销中商品 Y 的数量。此值必须为正整数。 |
   ^^^benefit_max_applicable_times |string |5 |可选。单个订单中 BXGY 优惠最多可应用的次数。此值必须为正整数。 |
   ^target_user_info |object | |促销的目标用户类型。 |
   ^^user_type |string |ALL_USER |目标用户类型。
   可能的值：
* `ALL_USER`
* `SHOP_NEW_CUSTOMER`
* `SHOP_EXISTING_CUSTOMER`
* `SHOP_REPEAT_CUSTOMER`
* `SHOP_ABANDONED_CHECKOUTS_CUSTOMER` |
   ^benefit_products |[]object | |BXGY 促销中的优惠商品 |
   ^^id |string |1732239744891062847 |TikTokShop 商品 ID |
   ^auction_support_type |string |ALL |`SHIPPING_DISCOUNT` 活动是否支持拍卖商品。其他活动类型会省略此字段，当拍卖支持数据不可用时，运费折扣活动也可以省略此字段。
   可能的值：
* `ALL`：活动同时支持普通商品和拍卖商品。
* `EXCLUDE_AUCTION`：活动不支持拍卖商品。 |

# 响应示例
```json
{"code":0,"data":{"activity_id":"7136104329798256386","title":"FlashSale 20230707","activity_type":"FIXED_PRICE","duration_type":"NORMAL","begin_time":1661756811,"end_time":1661856811,"participation_limit":[{"type":"BUYER_NO_LIMIT"}],"products":[{"id":"7136011254174631686","activity_price":{"amount":"70500","currency":"IDR"},"quantity_limit":-1,"quantity_per_user":-1,"discount":"10","skus":[{"id":"7136382541418366725","discount":"10","quantity_limit":-1,"quantity_per_user":-1,"activity_price":{"amount":"70500","currency":"IDR"},"used_quantity":3}],"used_quantity":3}],"status":"ONGOING","create_time":1789355787347,"update_time":1789355865063,"product_level":"PRODUCT","activity_commands":["IMMUTABLE"],"discount":{"shipping_discount":{"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"3","type":"DISCOUNT_SHIPPING_FEE","value":"10.5","shipping_method":"STANDARD_SHIPPING","inventory_type":"SELF_FULFILLED","area_scope":{"type":"WHOLE","specific_areas":["Washington","New York"]}},"bmsm_discount":{"details":[{"tier":1,"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"5","type":"PERCENTAGE_OFF","value":"10"}]},"gift_discount":{"gift_receiving_type":"ALL_RECEIVE","gift_infos":[{"tier":1,"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"3","gift_details":[{"product_id":"1732239744891062847","sku_id":"1732239787859544639","total_claim_limit":"100"}]}]},"bxgy_discount":{"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"5","discount_type":"AMOUNT_OFF_EACH","discount_value":"10","benefit_max_applicable_quantity":"5","benefit_max_applicable_times":"5"}},"target_user_info":{"user_type":"ALL_USER"},"benefit_products":[{"id":"1732239744891062847"}],"auction_support_type":"ALL"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 17029001 | 参数无效 |
| 17029009 | 活动不存在 |
| 17029028 | 您指定的活动不在您的店铺中。 |
| 17029036 | 不支持的 ActivityType。 |
| 17029052 | 不支持的 ProductType |
| 17029055 | 请求超时 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

