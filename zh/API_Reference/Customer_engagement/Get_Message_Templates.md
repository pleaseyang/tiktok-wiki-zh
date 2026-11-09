# 获取消息模板

# 路径：/customer_engagement/202412/message_templates
# 方法：[GET]
# 功能描述
获取 TikTok Shop 预定义的 customer engagement 消息模板库，您可以直接在 customer engagement 通信中使用。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| shop_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | Shop_cipher 对于跨境店铺是必填的，对于本地店铺是可选的。每个店铺的 shop_cipher 是唯一的。从 Get Authorized Shop API 动态获取此参数。使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| locale | string | Y | en | 用于显示消息内容的 BCP-47 locale 代码，以逗号分隔。 |
支持的 locale 代码列表请参考 [Locale codes](678e3a47bae28f030a8c7523)。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_engagement/202412/message_templates?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^message_templates | []object |  | TikTok Shop 预定义的 customer engagement 消息模板。 |
| ^^id | string | 123456789_987654321 | 模板 ID。 |
| ^^message_title | string | 遇见你的下一个心头好! | 消息标题。 |
| ^^message_body | string | 我们力求以您为本打造商品。查看我们的最新上新，找到专为提升自信打造的完美之选。 | 消息正文。 |
| ^^product_card_rules | object |  | 消息中可包含的交互式商品卡片的数量和类型规则。 |
| ^^^min_count | int | 0 | 必须包含的最少商品卡片数量。 |
| ^^^max_count | int | 4 | 可以包含的最多商品卡片数量。 |
| ^^coupon_card_rules | object |  | 消息中可包含的交互式优惠券卡片的数量和类型规则。 |
| ^^^min_count | int | 1 | 必须包含的最少优惠券卡片数量。 |
| ^^^max_count | int | 1 | 可以包含的最多优惠券卡片数量。 |
| ^^^coupon_type | []string | ["REGULAR_ALL","REGULAR_REPEAT"] | 消息中可包含的优惠券类型。 |
| 可能的值： |  |  |  |

* REGULAR_ALL：面向所有买家的常规优惠券。
   所需优惠券属性：[Search Coupons API](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd) 中的 `coupons.display_type=REGULAR` 和 `coupons.target_buyer_segment=ALL`。
* REGULAR_REPEAT：仅面向回头客的常规优惠券。
   所需优惠券属性：[Search Coupons API](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd) 中的 `coupons.display_type=REGULAR` 和 `coupons.target_buyer_segment=REPEAT_CUSTOMERS`。 |

# 响应示例
```json
{"code":0,"data":{"message_templates":[{"id":"123456789_987654321","message_title":"Meet your next favorite thing!","message_body":"We strive to create products with you in mind. Check out our newest drop to find your perfect fit that's built for a confidence boost.","product_card_rules":{"min_count":0,"max_count":4},"coupon_card_rules":{"min_count":1,"max_count":1,"coupon_type":["REGULAR_ALL","REGULAR_REPEAT"]}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 68009001 | 访问被拒绝。此店铺无法使用此 endpoint，因为卖家不满足 CRM 功能的访问条件。详情请参见 TikTok Shop Academy。 |
