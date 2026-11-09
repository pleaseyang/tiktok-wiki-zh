# 移除促销活动商品

# 路径：/promotion/202309/activities/{activity_id}/products
# 方法：[DELETE]
# 功能描述
将此 API 用于 `FIXED_PRICE`、`DIRECT_DISCOUNT`、`FLASHSALE`、`BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y`、`GIFT_WITH_PURCHASE` 和 `SHIPPING_DISCOUNT` 活动。至少提供一个非空的移除列表；省略 body、发送空对象或仅发送空列表不会请求移除项目。

* 从 PRODUCT 范围的活动中移除普通活动商品时，使用 `product_ids`，不要提供 `sku_ids`。
* 从 VARIATION 范围的活动中移除普通活动商品或 SKU 时，使用 `product_ids`、`sku_ids` 或两者都使用。
* 对于 `GIFT_WITH_PURCHASE`，提供非空的 `product_ids` 列表；其他移除列表不会被其分支处理。
* 对于 `BUY_MORE_SAVE_MORE` 或 `BUY_X_GET_Y`，`benefit_product_ids` 移除权益商品关系，不需要 `product_ids`。
* 对于 SHOP 范围的 `BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y` 或 `SHIPPING_DISCOUNT` 活动，`exclude_product_ids` 移除排除商品关系。
   您可以在一个普通的非 GWP 请求中提供多个适用的非空列表。您不能从 `DEACTIVATED` 或 `EXPIRED` 活动中移除项目。


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
| product_ids | []string | N | ["7493989962827597361"] | 要移除的商品 ID 列表。 |
| 最大数量：300。 |  |  |  |  |
| sku_ids | []string | N | ["7135657830438176513"] | 要移除的 SKU ID 列表。对于商品级别的活动，不要指定此字段。 |
| 最大数量：300。 |  |  |  |  |
| benefit_product_ids | []string | N | ["7493989962827597361"] | 要从 `BUY_MORE_SAVE_MORE` 或 `BUY_X_GET_Y` 活动中移除的权益商品关系 ID 列表。最多 100 个 ID。 |
| exclude_product_ids | []string | N | ["7493989962827597361"] | 要从 SHOP 范围的 `BUY_MORE_SAVE_MORE`、`BUY_X_GET_Y` 或 `SHIPPING_DISCOUNT` 活动中移除的排除商品关系 ID 列表。最多 100 个 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202309/activities/7402881377634567979/products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":["7493989962827597361"],"sku_ids":["7135657830438176513"],"benefit_product_ids":["7493989962827597361"],"exclude_product_ids":["7493989962827597361"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^activity_id | string | 7136104329798256386 | 标识活动的唯一 ID。 |
| ^status | string | ONGOING | 活动状态。 |
| 可能的值： |  |  |  |

* DRAFT：具有此状态的促销活动不对 TikTok 用户开放。
* NOT_START：具有此状态的促销活动在设定的活动开始时间之前不对 TikTok 用户开放。
* ONGOING：具有此状态的促销活动对 TikTok 用户开放。
* EXPIRED：具有此状态的促销活动因已过期而不对 TikTok 用户开放。
* DEACTIVATED：活动已被卖家停用，不对 TikTok 用户开放。
* NOT_EFFECTIVE：活动已被平台终止，不对 TikTok 用户开放。 |
   ^update_time |int |1661765135 |响应生成的时间，以秒为单位的 Unix 时间戳 (UTC)。 |

# 响应示例
```json
{"code":0,"data":{"activity_id":"7136104329798256386","status":"ONGOING","update_time":1661765135},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 17027802 | 内部错误，promotion 购买限制删除失败，请重试 |
| 17029001 | 参数无效 |
| 17029009 | 活动不存在 |
| 17029010 | 活动已停用 |
| 17029011 | 不允许更新活动的开始时间 |
| 17029012 | 不允许更新已过期的活动 |
| 17029016 | SKU ID 无效。 |
| 17029023 | 商品不在 promotion 中 |
| 17029024 | 在此 promotion 中未找到 SKU。 |
| 17029028 | 您指定的活动不在您的店铺中。 |
| 17029036 | 不支持的 ActivityType。 |
| 17029046 | 每次请求的项目数量超过限制。 |
| 17029047 | 无法更新 `ONGOING` 状态的限时抢购商品。 |
| 17029048 | 无法更新 `ONGOING` 状态的限时抢购 SKU。 |
| 17029052 | 不支持的 ProductType |
| 17029055 | 请求超时 |
| 17029069 | 访问被拒绝。此活动不属于该店铺，因此无法修改。 |
| 17029074 | 符合条件的商品和礼品不能是同一商品。 |
| 17029079 | 商品已分配到另一个冲突的 promotion 中。 |
| 17029102 | 商品级别和店铺级别不可互换 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
