# 更新促销活动商品

# 路径：/promotion/202309/activities/{activity_id}/products
# 方法：[PUT]
# 功能描述
此 API 的使用方式如下：

* 对于 PRODUCT 或 VARIATION 范围的 `FIXED_PRICE`、`DIRECT_DISCOUNT` 或 `FLASHSALE` 活动，提供非空的 `products` 数组。对于 VARIATION 范围，在每个商品的 `skus` 数组中添加或更新 SKU。
* 对于 PRODUCT 范围的 `SHIPPING_DISCOUNT` 或 `GIFT_WITH_PURCHASE` 活动，提供非空的 `products` 数组。SHOP 范围的运费折扣活动不支持此操作，此操作也不记录运费折扣或买赠的嵌套 SKU 更新。
* 对于 PRODUCT 范围的 `BUY_MORE_SAVE_MORE` 或 `BUY_X_GET_Y` 活动，当请求仅更新优惠商品关系时，`products` 可以省略或为空。
* 对于 SHOP 范围的 `BUY_MORE_SAVE_MORE` 或 `BUY_X_GET_Y` 活动，省略 `products` 或传递空数组；使用 `benefit_product_ids` 或 `exclude_product_ids` 进行适用的关系更新。
   对于进行中的限时抢购，您可以添加商品或 SKU，但不能更改活动中已有商品或 SKU 的价格或购买限制。要移除商品或 SKU，请使用[移除活动商品](https://partner.tiktokshop.com/docv2/page/650acfd84a0bb702c072b4eb)。


---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| activity_id | string | 是 | 7402881377634567979 | 促销活动的唯一标识符。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| products | []object | 否 |  | 要添加到列表中的商品或促销活动中已有的待编辑商品。长度不得超过 `300`。 |
| ^id | string | 是 | 7135427619356477189 | TikTok Shop 商品 ID |
| ^activity_price_amount | string | 否 | 4.5 | 商品货币的促销价格。当 `product_level==PRODUCT` 且 `activity_type` 为 `FIXED_PRICE` 或 `FLASHSALE` 时指定此字段。当 `activity_type==DIRECT_DISCOUNT` 或 `product_level==VARIATION` 时不要指定。 |
| ^discount | string | 否 | 10 | 折扣值。如果商品打 9 折（即 10% off），则值为 `10`。 |
| 当 `product_level==PRODUCT` 且 `activity_type==DIRECT_DISCOUNT` 时必须指定此值；其他情况下不得指定。 |  |  |  |  |
| ^quantity_limit | int | 是 | -1 | 活动涉及商品的数量限制。范围为 `[1, 99]`，或使用 `-1` 表示不限。如果更新已有商品的值，则不能小于当前值。 |
| 当 `product_level==VARIATION` 时，必须指定 `-1`。 |  |  |  |  |
| ^quantity_per_user | int | 是 | -1 | 每个买家的商品购买限制。范围为 `[1, 99]`，或使用 `-1` 表示不限。如果更新已有商品的值，则不能小于当前值。 |
| 当 `product_level==VARIATION` 时，必须指定 `-1`。 |  |  |  |  |
| ^skus | []object | 否 |  | 要添加到列表中的 SKU 或待编辑的已有 SKU。一次 API 调用中所有商品的 SKU 总数不得超过 300。 |
| 对于 `product_level==VARIATION` 的商品折扣或限时抢购活动，每个商品必须包含至少一个 SKU。对于这些活动类型且 `product_level==PRODUCT` 的情况，指定 `[]`。 |  |  |  |  |
| ^^id | string | 是 | 7125688837187176194 | SKU ID |
| ^^activity_price_amount | string | 否 | 6.5 | SKU 货币的促销价格。当 `product_level==VARIATION` 且 `activity_type` 为 `FIXED_PRICE` 或 `FLASHSALE` 时指定此字段。当 `activity_type==DIRECT_DISCOUNT` 时不要指定。 |
| ^^discount | string | 否 | 10 | 折扣值。如果 SKU 打 9 折（即 10% off），则值为 `10`。 |
| 当 `product_level==VARIATION` 且 `activity_type==DIRECT_DISCOUNT` 时必须指定此值。当 `activity_type` 为 `FIXED_PRICE` 或 `FLASHSALE` 时不要指定。 |  |  |  |  |
| ^^quantity_limit | int | 是 | -1 | 活动涉及 SKU 的数量限制。范围为 `[1, 99]`，或使用 `-1` 表示不限。如果更新已有 SKU 的值，则不能减小该值。 |
| ^^quantity_per_user | int | 是 | 10 | 每个买家的 SKU 购买限制。范围为 `[1, 99]`，或使用 `-1` 表示不限。如果更新已有 SKU 的值，则不能减小该值。 |
| activity_id | string | 是 | 7136104288010372865 | 标识活动的唯一 ID。 |
| 您不能更新 `DEACTIVATED` 或 `EXPIRED` 活动中的商品。 |  |  |  |  |
| benefit_product_ids | []string | 否 | ["7135427619356477189","7135427619356477190"] | 要添加到多买多省（BMSM）或买 X 得 Y（BXGY）活动中或更新其优惠商品 ID。省略此字段或传递空数组不会更改活动现有的优惠商品；不会移除它们。更新后，活动最多可包含 100 个优惠商品。 |
| exclude_product_ids | []string | 否 | ["7135427619356477189","7135427619356477190"] | 对于 SHOP 级别的多买多省（BMSM）或买 X 得 Y（BXGY）活动，这些是要添加到排除列表中或更新其的商品 ID。省略此字段或传递空数组不会更改现有的排除商品；不会移除它们。每次请求最多 100 个 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202309/activities/7402881377634567979/products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"products":[{"id":"7135427619356477189","activity_price_amount":"4.5","discount":"10","quantity_limit":-":-1,"quantity_per_user":-1,"skus":[{"id":"7125688837187176194","activity_price_amount":"6.5","discount":"10","quantity_limit":-1,"quantity_per_user":10}]}],"activity_id":"7136104288010372865","benefit_product_ids":["7135427619356477189","7135427619356477190"],"exclude_product_ids":["7135427619356477189","7135427619356477190"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^activity_id | string | 7136104329798256386 | 标识不同活动的唯一 ID。 |
| ^title | string | DiscountPromotion | 卖家设置的活动名称。 |
| ^update_time | int | 1661756811 | 响应生成时间，Unix 时间戳（秒）（UTC）。 |
| ^status | string | DRAFT | 活动状态。 |
| 可能的值： |  |  |  |

* DRAFT：此状态的促销活动对 TikTok 用户不可见。
* NOT_START：此状态的促销活动在设定的活动开始时间之前对 TikTok 用户不可见。
* ONGOING：此状态的促销活动对 TikTok 用户可见。
* EXPIRED：此状态的促销活动因已过期而对 TikTok 用户不可见。
* DEACTIVATED：活动已被卖家停用，对 TikTok 用户不可见。
* NOT_EFFECTIVE：活动已被平台终止，对 TikTok 用户不可见。 |
   ^total_count |int |1 |此请求中的商品数量。
   当 `product_level==PRODUCT` 时，为商品数量。当 `product_level==VARIATION` 时，为所有商品的 SKU 总数。当 `product_level==SHOP` 时，此值为 `0`。不包含 `benefit_product_ids` 和 `exclude_product_ids` 中的 ID。 |

# 响应示例
```json
{"code":0,"data":{"activity_id":"7136104329798256386","title":"DiscountPromotion","update_time":1661756811,"status":"DRAFT","total_count":1},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 17011102 | 促销标题不能重复。 |
| 17027107 | 内部系统错误，请稍后重试。 |
| 17029001 | 参数无效 |
| 17029009 | 活动不存在 |
| 17029010 | 活动已停用 |
| 17029012 | 不允许更新已过期的活动 |
| 17029013 | 当 `product_level==PRODUCT` 时，`sku` 必须为 `[]`。 |
| 17029014 | `quantity_per_user` 的值超出范围。 |
| 17029015 | 当 `product_level==VARIATION` 时，`quantity_limit` 的值必须为 `-1`。 |
| 17029016 | 无效的 SKU ID。 |
| 17029017 | 您指定的商品不在您的店铺中。 |
| 17029018 | 提供的 SKU 数量大于可用库存。 |
| 17029019 | 提供的商品数量大于可用库存。 |
| 17029020 | 商品折扣超出限制。限制因商品和地区而异。 |
| 17029021 | SKU 折扣超出限制。限制因商品和地区而异。 |
| 17029022 | 商品或 SKU 不能同时处于两个 `ONGOING` 或 `NOT_START` 活动中。 |
| 17029025 | 活动中包含的商品或 SKU 数量超过 `10000`。 |
| 17029026 | 无效的 SellerID |
| 17029028 | 您指定的活动不在您的店铺中。 |
| 17029029 | 当 `activity_type==DIRECT_DISCOUNT` 且 `product_level==PRODUCT` 时，您错误地指定了 `activity_price_amount` 而非 `discount`。 |
| 17029030 | 当 `activity_type==FIXED_PRICE / FLASHSALE` 且 `product_level==PRODUCT` 时，您错误地指定了 `discount` 而非 `activity_price_amount`。 |
| 17029031 | 当 `activity_type==DIRECT_DISCOUNT` 且 `product_level==VARIATION` 时，您错误地指定了 `activity_price_amount` 而非 `discount`。 |
| 17029032 | 当 `activity_type==FIXED_PRICE / FLASHSALE` 且 `product_level==VARIATION` 时，您错误地指定了 `discount` 而非 `activity_price_amount`。 |
| 17029033 | `products` 为空。 |
| 17029034 | `activity_price_amount` 无效。 |
| 17029037 | 当 `product_level==VARIATION` 时，`skus` 为空。 |
| 17029038 | 当 `product_level==VARIATION` 时，不得指定 `product.activity_price_amount` 和 `product.discount`。 |
| 17029039 | 商品 ID 重复。 |
| 17029040 | SKU ID 重复。 |
| 17029041 | 当 `activity_type==DIRECT_DISCOUNT` 且 `product_level==PRODUCT` 时，必须指定 `product.discount`。 |
| 17029042 | 当 `activity_type==FIXED_PRICE / FLASHSALE` 且 `product_level==PRODUCT` 时，必须指定 `product.activity_price_amount`。 |
| 17029043 | 当 `activity_type==DIRECT_DISCOUNT` 且 `product_level==VARIATION` 时，必须指定 `sku.discount`。 |
| 17029044 | 当 `activity_type==FIXED_PRICE / FLASHSALE` 且 `product_level==VARIATION` 时，必须指定 `sku.activity_price_amount`。 |
| 17029045 | RequestSerialNo 重复。 |
| 17029046 | 每次请求的商品数量超过限制。 |
| 17029047 | 进行中的限时抢购商品无法更新。 |
| 17029048 | 进行中的限时抢购 SKU 无法更新。 |
| 17029049 | 不支持的 ActivityVersion。 |
| 17029050 | `quantity_limit` 和 `quantity_per_user` 的值必须为 `-1` 或在 `[1, 99]` 范围内。 |
| 17029051 | 未找到商品 ID。 |
| 17029053 | SKU ID 与商品 ID 不匹配。 |
| 17029054 | 请限制请求频率。 |
| 17029055 | 请求超时 |
| 17029056 | 商品状态无效。 |
| 17029058 | 无法减少买家/数量购买限制。 |
| 17029060 | 商品的类别无效 |
| 17029062 | 折扣低于限制，请确认。 |
| 17029063 | SKU 折扣低于限制，请确认。 |
| 17029064 | 商品不可销售。 |
| 17029065 | 目标配额小于初始配额。 |
| 17029066 | 限制信息无法更改或修改。 |
| 17029067 | 拍卖商品不符合促销资格。 |
| 17029069 | 访问被拒绝。此活动不属于该店铺，因此无法修改。 |
| 17029074 | 符合条件的商品和赠品不能是同一商品。 |
| 17029079 | 商品已被分配到另一个冲突的促销活动中。 |
| 17029103 | 部分商品在所选时段内已被应用到另一个冲突的促销活动中。 |
| 17029104 | 所选商品在所选时段内已被应用到另一个多买多省促销活动中。如需继续，请编辑商品列表或更改促销时段。 |
| 17029113 | 商品数量将超过促销活动的最大数量。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

