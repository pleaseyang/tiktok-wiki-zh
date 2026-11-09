# 更新促销活动

# 路径：/promotion/202309/activities/{activity_id}
# 方法：[PUT]
# 功能描述
更新现有的促销活动。存储的活动类型决定哪些请求字段会被处理：

* 对于固定价格、直接折扣和限时抢购活动，更新 title、begin_time 和 end_time；其他类型特定字段在此更新路径中不会被处理。
* 对于运费折扣活动，提供 discount.shipping_discount；使用 duration_type 选择定时或无限期活动。
* 对于买更多省更多 (BMSM) 或买XGetY (BXGY) 活动，将 duration_type 设置为 NORMAL，将 product_level 设置为 PRODUCT 或 SHOP，提供一个 participation_limit 条目，并提供匹配的 discount 对象。
* 对于满赠 (GWP) 活动，将 duration_type 设置为 NORMAL，将 product_level 设置为 PRODUCT，提供一个 participation_limit 条目，并提供 discount.gift_discount。
   固定价格、直接折扣、限时抢购、BMSM、BXGY 和 GWP 活动在停用或过期后无法更新。对于这些活动类型，即将开始的定时活动需要未来的 begin_time，而正在进行的活动必须保持其现有的 begin_time。正在进行中的 BMSM 或 BXGY 活动还必须保持其现有的第一层级阈值、阈值类型、折扣类型、商品范围、参与限制和目标用户设置。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| activity_id | string | Y | 7402881377634567979 | 促销活动的唯一标识符。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| title | string | Y | BlackFridayDiscount | 活动名称。名称必须唯一。最大长度：限时抢购活动为 50 个 Unicode 字符；运费折扣活动为 50 个字符；固定价格、直接折扣、BMSM、BXGY 或 GWP 活动为 100 个 Unicode 字符。 |
| duration_type | string | N | NORMAL | 活动调度模式。 |

* 对于 BMSM、BXGY 和 GWP 活动，将此字段设置为 `NORMAL`，并提供定时的 `begin_time` 和 `end_time`。
* 对于运费折扣活动，使用 `NORMAL` 表示定时活动，或使用 `INDEFINITE` 表示没有预定结束时间的活动。当在运费折扣更新中省略此字段时，默认为 `NORMAL`。对于 `INDEFINITE`，将 `begin_time` 和 `end_time` 都设置为 `0`。
* 更新固定价格、直接折扣或限时抢购活动时不会处理此字段。 |
   begin_time |int |Y |1661756811 |活动开始时间，以秒为单位的 Unix 时间戳。对于无限期运费折扣活动，将此字段设置为 0。对于具有正常调度的固定价格、直接折扣、限时抢购、BMSM、BXGY 或 GWP 活动，如果活动即将开始，请使用未来时间；如果活动正在进行中，请使用其现有的开始时间，因为该值无法更改。 |
   end_time |int |Y |1661856811 |活动结束时间，以秒为单位的 Unix 时间戳。对于无限期运费折扣活动，将此字段设置为 0。对于正常调度的固定价格、直接折扣、限时抢购、BMSM、BXGY 或 GWP 更新，end_time 必须比 begin_time 至少晚 600 秒。 |
   product_level |string |N |PRODUCT |promotion 的商品范围。更新 BMSM、BXGY、GWP 或运费折扣活动时必须提供此字段。
* PRODUCT：适用于商品及其所有 SKU。对于 GWP 使用此值；BMSM、BXGY 和运费折扣也支持此值。
* VARIATION：仅适用于指定的 SKU。不支持 BMSM、BXGY、GWP 或运费折扣更新。
* SHOP：适用于店铺中的所有商品。支持 BMSM、BXGY 和运费折扣，但不支持 GWP。
   更新固定价格、直接折扣或限时抢购活动时不会处理此字段。对于正在进行中的 BMSM 或 BXGY 活动，保持其现有的 PRODUCT 或 SHOP 范围。 |
   participation_limit |[]object |N | |买家参与限制。对于 BMSM、BXGY 和 GWP 更新，提供一个条目。如果 BMSM 或 BXGY 活动正在进行中，保持其现有的参与限制不变。 |
   ^type |string |Y |BUYER_NO_LIMIT |决定 promotion 是否限制每个买家可以享受优惠的订单数量。
* `BUYER_NO_LIMIT`：买家可以在多个订单中享受优惠。
* `BUYER_LIMIT_ONLY_ONE`：每个买家只能在一个订单中享受优惠。 |
   discount |object |N | |折扣信息。 |
   ^shipping_discount |object |N | |运费折扣的配置，包括购买条件、折扣值、配送方式、库存类型和区域范围。 |
   ^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |购买条件类型。可能的枚举值：
* `NO_THRESHOLD`：无最低购买条件。
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家的订单金额必须达到或超过最低消费条件。
   `MINIMAL_ITEM_QUANTITY` 和 `MINIMAL_ORDER_AMOUNT` 仅在 `product_level==SHOP` 时可以设置。 |
   ^^threshold_value |string |N |3 |运费折扣的购买阈值，根据 `threshold_type` 解释。
* 当 `threshold_type` 为 `NO_THRESHOLD` 时，不需要此字段。
* 当 `threshold_type` 为 `MINIMAL_ITEM_QUANTITY` 时，输入买家必须购买的符合条件的商品的最低数量。该值必须为整数。
* 当 `threshold_type` 为 `MINIMAL_ORDER_AMOUNT` 时，输入店铺本地货币中符合条件的商品的最低小计金额，例如 3 单位本地货币。该值最多保留两位小数。 |
   ^^type |string |Y |DISCOUNT_SHIPPING_FEE |运费优惠类型。
* `FREE_SHIPPING`：将买家的运费降至零。
* `DISCOUNT_SHIPPING_FEE`：将买家的运费减免最多 `shipping_discount.value` 中指定的金额。 |
   ^^value |string |N |10.5 |运费折扣金额。
* 当 `type` 为 `FREE_SHIPPING` 时，省略此字段。
* 当 `type` 为 `DISCOUNT_SHIPPING_FEE` 时，输入从买家运费中扣除的最大金额（以店铺本地货币计）。该值最多保留两位小数。 |
   ^^shipping_method |string |N |STANDARD_SHIPPING |此 promotion 适用的配送方式。
* 当 `STANDARD_SHIPPING`：仅适用于标准配送方式，包括经济配送。
* `EXPRESS_SHIPPING`：仅适用于快速配送方式。
* `ALL_SHIPPING_METHOD`：适用于店铺提供的所有配送方式。
   默认值：`STANDARD_SHIPPING` |
   ^^inventory_type |string |N |SELF_FULFILLED |促销活动适用的库存类型：
* `SELF_FULFILLED`：仅适用于从卖家仓库发货的库存。
* `FULFILLED_BY_TIKTOK`：仅适用于由 TikTok 从 FBT（Fulfilled by TikTok）仓库发货的库存。
* `ALL`：适用于符合条件商品的所有库存。
   对于美国全店免运费活动（`product_level` == `SHOP`），默认为 `ALL`，且 `inventory_type` 不能仅设置为 `SELF_FULFILLED` 或仅设置为 `FULFILLED_BY_TIKTOK`。
   对于其他地区，默认为 `SELF_FULFILLED`。`FULFILLED_BY_TIKTOK` 和 `ALL` 仅在 `product_level` == `SHOP` 且 `threshold_type` = `NO_THRESHOLD` 时可以设置。 |
   ^^area_scope |object |Y | |促销活动适用的（买家）地理区域。 |
   ^^^type |string |Y |WHOLE |促销活动适用的买家地理区域。
* `WHOLE`：促销活动适用于卖家提供配送的所有区域。
* `SPECIFIC_AREAS`：促销活动仅适用于 `area_scope.specific_areas` 中列出的配送区域。 |
   ^^^specific_areas |[]string |N |["Washington", "New York"] |促销活动适用的区域列表。可包含在此列表中的有效值取决于店铺所在区域。每个店铺区域的有效值列表可在此处获取：[链接](https://partner.tiktokshop.com/docv2/page/67e3b059e7dc4f04a4ff9e09) |
   ^bmsm_discount |object |N | |买更多省更多 (BMSM) 活动的相关配置。 |
   ^^details |[]object |N | |BMSM 活动的配置。最多允许两个层级。所有层级的 `threshold_type` 和 `type` 必须相同。更新活动时，每个值还必须与活动现有的阈值类型和折扣类型匹配。 |
   ^^^tier |int |Y |1 |从 1 开始的层级编号。第一层使用 `1`，第二层使用 `2`。对于第一层之后的每个层级，`threshold_value` 和 `value` 都必须大于前一层级的对应值。 |
   ^^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |购买条件类型。可能的枚举值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家的订单金额必须达到或超过最低消费条件。 |
   ^^^threshold_value |string |Y |5 |基于 `threshold_type` 的折扣购买阈值。
* 当 `threshold_type` 为 `MINIMAL_ITEM_QUANTITY` 时，输入买家必须购买的符合条件的商品的最低数量。该值必须为正整数。
* 当 `threshold_type` 为 `MINIMAL_ORDER_AMOUNT` 时，输入店铺本地货币中符合条件的商品的最低小计金额。该值必须为正数且最多保留两位小数。 |
   ^^^type |string |Y |PERCENTAGE_OFF |作为优惠的折扣类型。折扣值由 `value` 决定。
   可能的枚举值：
* `PERCENTAGE_OFF`：买家将获得符合条件的商品价格的 X% 折扣。
* `AMOUNT_OFF`：买家将获得符合条件的商品价格减免 X 单位本地货币。 |
   ^^^value |string |Y |10 |正数折扣值，根据 `type` 解释。
* 当 `type` 为 `PERCENTAGE_OFF` 时，输入符合条件的商品的折扣百分比，为正整数。
* 当 `type` 为 `AMOUNT_OFF` 时，输入从符合条件的商品价格中扣除的正数金额（以店铺本地货币计），最多保留两位小数。 |
   ^gift_discount |object |N | |满赠 (GWP) 活动的相关配置。仅需为 GWP 活动配置。 |
   ^^gift_receiving_type |string |Y |ALL_RECEIVE |礼品领取类型。目前仅支持一种类型：
* `ALL_RECEIVE`：可以领取活动中配置的所有礼品。 |
   ^^gift_infos |[]object |Y | |满赠 (GWP) 层级配置。至少提供一个层级。东南亚和英国最多允许两个层级；美国仅允许一个层级。所有层级的 `threshold_type` 必须相同。 |
   ^^^tier |int |Y |1 |`tier` 使用从 1 开始的索引，即第一层和第二层计为"1、2"，而不是"0、1"。
   给定层级的 `threshold_value` 必须大于前一层级的值。
   例如：如果 `tier`<span style="background-color: #ff0">1 的 </span><span style="background-color: #ff0"><code>threshold_value</code></span>`2`，则 `tier`==2 的 `threshold_value` 必须 > `2`。 |
   ^^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |折扣的购买阈值类型。每个层级的阈值类型必须一致。可能的枚举值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买达到或超过最低消费条件的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家的订单金额必须达到或超过最低消费条件。 |
   ^^^threshold_value |string |Y |3 |获得礼品的正数购买阈值，根据 `threshold_type` 解释。
* 当 `threshold_type` 为 `MINIMAL_ITEM_QUANTITY` 时，输入买家必须购买的符合条件的商品的最低数量。该值必须为正整数。
* 当 `threshold_type` 为 `MINIMAL_ORDER_AMOUNT` 时，输入店铺本地货币中符合条件的商品的最低小计金额，例如 3 单位本地货币。该值必须为正数且最多保留两位小数。 |
   ^^^gift_details |[]object |Y | |此层级的礼品 SKU。在所有层级中，至少提供一个礼品 SKU，且不要在整个活动中重复相同的 sku_id。对于 MINIMAL_ITEM_QUANTITY 层级，此列表不能为空。 |
   ^^^^product_id |string |Y |1732239744891062847 |礼品的 TikTok Shop 商品 id。 |
   ^^^^sku_id |string |Y |1732239787859544639 |礼品的 TikTok Shop sku id。 |
   ^^^^total_claim_limit |string |Y |100 |活动中涉及的礼品 sku 的数量限制。范围为 [1, 99999]。如果更新现有 sku 的值，则该值不能降低。 |
   ^bxgy_discount |object |N | |买XGetY (BXGY) 活动的配置。仅为 BXGY 活动配置此对象。更新活动时，`threshold_type` 和 `discount_type` 必须与活动的现有值匹配。 |
   ^^threshold_type |string |Y |MINIMAL_ITEM_QUANTITY |购买阈值类型。可能的值：
* `MINIMAL_ITEM_QUANTITY`：买家必须购买至少指定数量的符合条件的商品。
* `MINIMAL_ORDER_AMOUNT`：买家订单中符合条件的商品小计必须达到或超过店铺本地货币中指定的金额。 |
   ^^threshold_value |string |Y |5 |根据 `threshold_type` 解释的折扣购买阈值。
* 当 `threshold_type` 为 `MINIMAL_ITEM_QUANTITY` 时，输入买家必须购买的符合条件的商品的最低数量。该值必须为 1 到 10 之间的整数。
* 当 `threshold_type` 为 `MINIMAL_ORDER_AMOUNT` 时，输入店铺本地货币中符合条件的商品的最低小计金额。该值必须为正数且最多保留两位小数。 |
   ^^discount_type |string |Y |AMOUNT_OFF_EACH |作为优惠的折扣类型。折扣金额或百分比由 `discount_value` 决定。
   可能的值：
* `PERCENTAGE_OFF`：买家将获得 `discount_value` 指定的符合条件的商品的百分比折扣。
* `FREE`：买家将免费获得符合条件的商品。
* `AMOUNT_OFF_EACH`：买家将获得每个符合条件的商品价格减免 `discount_value` 指定的店铺本地货币金额。 |
   ^^discount_value |string |Y |5 |折扣值。
* 当 `type`==`PERCENTAGE_OFF` 时，买家将获得符合条件的商品价格的 X% 折扣。如果该值表示百分比，则应为整数。
* 当 `type`==`AMOUNT_OFF_EACH` 时，买家将获得每个符合条件的商品价格减免 X 单位本地货币。如果该值表示金额，则最多保留两位小数。
   |
   ^^benefit_max_applicable_quantity |string |Y |5 |每次应用 BXGY 优惠时商品 Y 可获得优惠的最大数量。输入 1 到 20 之间的正整数。 |
   ^^benefit_max_applicable_times |string |N |5 |可选。BXGY 优惠在单个订单中最多可应用的次数。输入 1 到 50 之间的正整数。 |
   target_user_info |object |N | |promotion 的目标用户配置。对于正在进行中的 BMSM 或 BXGY 活动，保持现有的目标用户设置不变，并在请求中包含该现有值。 |
   ^user_type |string |N |ALL_USER |可能的枚举值：
   `ALL_USER`
   `SHOP_NEW_CUSTOMER`
   `SHOP_EXISTING_CUSTOMER`
   `SHOP_REPEAT_CUSTOMER` |
   auction_support_type |string |N |ALL |决定运费折扣活动是否支持拍卖商品。此字段不适用于其他活动类型。
   可能的值：
* `ALL`：同时支持标准和拍卖商品。
* `EXCLUDE_AUCTION`：排除拍卖商品。
   当在运费折扣更新中省略时，默认为 `ALL`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202309/activities/7402881377634567979?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"title":"BlackFridayDiscount","duration_type":"NORMAL","begin_time":1661756811,"end_time":1661856811,"product_level":"PRODUCT","participation_limit":[{"type":"BUYER_NO_LIMIT"}],"discount":{"shipping_discount":{"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"3","type":"DISCOUNT_SHIPPING_FEE","value":"10.5","shipping_method":"STANDARD_SHIPPING","inventory_type":"SELF_FULFILLED","area_scope":{"type":"WHOLE","specific_areas":["Washington","New York"]}},"bmsm_discount":{"details":[{"tier":1,"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"5","type":"PERCENTAGE_OFF","value":"10"}]},"gift_discount":{"gift_receiving_type":"ALL_RECEIVE","gift_infos":[{"tier":1,"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"3","gift_details":[{"product_id":"1732239744891062847","sku_id":"1732239787859544639","total_claim_limit":"100"}]}]},"bxgy_discount":{"threshold_type":"MINIMAL_ITEM_QUANTITY","threshold_value":"5","discount_type":"AMOUNT_OFF_EACH","discount_value":"5","benefit_max_applicable_quantity":"5","benefit_max_applicable_times":"5"}},"target_user_info":{"user_type":"ALL_USER"},"auction_support_type":"ALL"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^activity_id | string | 7136104329798256386 | 标识不同活动的唯一 ID。 |
| ^title | string | BlackFridayDiscount | 卖家设置的活动名称。在固定价格、直接折扣、限时抢购、BMSM、GWP 和 BXGY 更新成功时返回。在运费折扣更新成功时不返回。 |
| ^update_time | int | 1661756811 | 最后更新时间，以秒为单位的 Unix 时间戳。 |
# 响应示例
```json
{"code":0,"data":{"activity_id":"7136104329798256386","title":"BlackFridayDiscount","update_time":1661756811},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 17003203 | 已存在一个全店免运费促销活动。一次只能创建一个。 |
| 17029001 | 参数无效 |
| 17029002 | 标题长度过长 |
| 17029003 | 活动标题为空。 |
| 17029004 | 活动标题重复。 |
| 17029005 | 开始时间早于当前时间 |
| 17029006 | 活动周期太短。 |
| 17029007 | 活动周期太长。 |
| 17029008 | 限时抢购周期太长 |
| 17029009 | 活动不存在 |
| 17029010 | 活动已停用 |
| 17029011 | 不允许更新活动的开始时间 |
| 17029012 | 不允许更新已过期的活动 |
| 17029022 | 商品或 SKU 不能同时处于两个 `ONGOING` 或 `NOT_START` 活动中。 |
| 17029026 | 卖家 ID 无效 |
| 17029028 | 您指定的活动不在您的店铺中。 |
| 17029052 | 不支持的 ProductType |
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
| 17029083 | 礼品的领取限制数量不能降低 |
| 17029084 | 礼品的阈值类型不能修改 |
| 17029085 | 礼品层级数量不能更改 |
| 17029102 | 商品级别和店铺级别不可互换 |
| 17029103 | 部分商品已在所选时间段内应用于另一个冲突的 promotion。 |
| 17029104 | 所选商品已在所选时间段内应用于另一个买更多省更多 promotion。要继续，请编辑商品列表或更改 promotion 时间段。 |
| 17029105 | 阈值类型和折扣类型不能修改。 |
| 17029106 | 参与限制信息不能更改或修改。 |
| 17029107 | 由于与其他活动重叠，卖家无法创建店铺范围的 BMSM 活动。 |
| 17029109 | promotion 超过阈值。 |
| 17029110 | 折扣值低于最低阈值。 |
| 17029111 | 阈值无效。 |
| 17029112 | 折扣值无效。 |
| 17029113 | 商品数量将超过 promotion 的最大数量。 |
| 17029114 | 不支持的 promotion 类型。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
