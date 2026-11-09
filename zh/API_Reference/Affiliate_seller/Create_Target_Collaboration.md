# 创建 Target Collaboration

# 路径：/affiliate_seller/202508/target_collaborations
# 方法：[POST]
# 功能描述
使用此 API 创建 target collaboration。您可以邀请达人推广您的商品，并为他们设置专属佣金。

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
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | Y | openapi_test | Target collaboration 的名称。 |
| message | string | N | this is a message | 与 target collaboration 关联的发送给达人的消息。 |
| end_time | string | Y | 1715654330 | Target collaboration 的结束日期，Unix 时间戳。 |
| products | []object | Y |  | 卖家为 target collaboration 提供的商品元数据和数据列表。列表最大长度为 `100` 个商品。 |
| ^id | string | Y | 789078671231312312 | 商品标识符。 |
| ^target_commission_rate | int | Y | 1000 | Target collaboration 的目标佣金比率。目标佣金比率以百分之一为单位。例如，`3587` 表示 `35.87%` 的佣金比率。此值最小为 `100`。 |
| ^shop_ads_commission_rate | int | N | 1000 | 该佣金率仅适用于广告产生的订单。如果达人的视频被用作广告而未设置此费率，产生的订单将改为按以下之一获得佣金： |

* 您在 open collaboration 中配置的 Shop Ads 佣金，或
* 此邀请中定义的标准佣金。
   佣金比率以万分之一为增量指定。
   例如，1000 代表 0.1 或 10%。 |
   creator_user_open_ids |[]string |Y |["uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"] | 列表最大长度为 `50` 个用户 open 标识符。达人 Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
   seller_contact_info |object |Y | |与卖家联系信息关联的元数据和数据。 |
   ^email |string |N |test@tiktokshop.com |卖家的电子邮件地址。 |
   ^phone_number |string |N |1234567890 |卖家的电话号码。 |
   ^whatsapp |string |N |1234567890 |卖家注册 WhatsApp 使用的电话号码。 |
   ^telegram |string |N |1234567890 |卖家的 Telegram 用户名或电话号码。 |
   ^line |string |N |1234567890 |卖家注册 Line 应用使用的电话号码。 |
   free_sample_rule |object |Y | |控制商品免费 sample 行为的一组属性。 |
   ^has_free_sample |bool |Y |true |如果设置为 `true`，则向邀请到 target collaboration 组的达人提供免费 sample。如果设置为 `false`，则不提供免费 sample。 |
   ^is_sample_approval_exempt |bool |Y |true |如果设置为 `true`，邀请到 target collaboration 的达人将免除卖家审核，并自动获得免费商品 sample。请注意，`has_free_sample` 属性会覆盖免费 sample 行为。 |
   preferred_content_type |string |N |LIVE |首选的达人内容类型，"LIVE" 或 "VIDEO" |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/target_collaborations?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"name":"openapi_test","message":"this is a message","end_time":"1715654330","products":[{"id":"789078671231312312","target_commission_rate":1000,"shop_ads_commission_rate":1000}],"creator_user_open_ids":["uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"],"seller_contact_info":{"email":"test@tiktokshop.com","phone_number":"1234567890","whatsapp":"1234567890","telegram":"1234567890","line":"1234567890"},"free_sample_rule":{"has_free_sample":true,"is_sample_approval_exempt":true},"preferred_content_type":"LIVE"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^target_collaboration | object |  | Target collaboration。 |
| ^^id | string | 7365861555575916210 | Target collaboration 标识符。 |
| ^target_collaboration_conflicts | []object |  | 因 target collaboration 冲突导致 target collaboration 失败的用户和商品标识符列表。 |
| ^^creator_user_open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
| ^^product_id | string | 789078671231 | 商品标识符。 |
| ^invalid_open_id_list | []string | ["xxxx"] | 导致创建失败的 open ID 列表。 |
| ^invalid_product_id_list | []string | ["1234"] | 导致创建失败的商品 ID 列表。 |
| ^create_time | int | 1715654330 | Target collaboration 的创建时间。 |
# 响应示例
```json
{"code":0,"data":{"target_collaboration":{"id":"7365861555575916210"},"target_collaboration_conflicts":[{"creator_user_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","product_id":"789078671231"}],"invalid_open_id_list":["xxxx"],"invalid_product_id_list":["1234"],"create_time":1715654330},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16024004 | 测试账号和非测试账号不能交叉邀请 |
| 16024006 | 卖家不能邀请其官方达人。 |
| 16024008 | 存在不属于此卖家的商品。 |
| 16024016 | 邀请失败，因为达人已关联店铺账号。 |
| 16024019 | 配额不足，无法创建邀请 |
| 16024020 | 请移除被排除的达人以创建邀请 |
| 16024021 | 邀请包含超过粉丝限制的达人 |
| 16024022 | 此邀请已存在达人和商品，请检查冲突对。 |
| 50001702 | Your invitation target contains an unavailable creator or product. Please check your request params.Remove the unavailable creator or product id and try again. |
| 50001703 | 请求参数包含敏感词。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 98001004 | 参数 {param_name} 无效。原因：{reason}。预期值：{expected_value} |

