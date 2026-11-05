# 更新 Target Collaboration

# Path: /affiliate_seller/202508/target_collaborations/{target_collaboration_id}
# Method: [PUT]
# 功能描述
使用此 API 更新 target collaboration。您可以修改 commission 比率、sample 设置等。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| target_collaboration_id | string | Y | 7890786712312312 | The unique id of specific target collaboration. |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | Y | openapi_test | Target collaboration 的名称。 |
| end_time | string | Y | 1715654330 | Target collaboration 的结束时间，以秒为单位的 Unix 时间戳。 |
| products | []object | Y |  | 卖家为 target collaboration 中 creator 合作提供的产品信息。 |
| 产品最大数量为 100。 |  |  |  |  |
| 当从产品列表中删除产品时，如果被删除的产品已被 creator 添加到 showcase，则将在次日 0:00 生效，否则立即生效。 |  |  |  |  |
| ^id | string | Y | 789078671231312312 | 产品标识符。 |
| ^commission_rate | int | Y | 1000 | Target collaboration 的目标 commission 比率。该值以万分之一为单位。例如，3587 表示 commission 等于原始价格的 35.87%。范围为 [100, 8000]。 |
| 提高产品 commission 将立即生效，而降低产品 commission 如果当前产品已被 creator 添加到 showcase，则将在次日 00:00 生效，否则立即生效。 |  |  |  |  |
| ^target_ad_commission_rate | int | N | 1000 | The commission rate applies only to orders generated from ads. If a creator’s video is used as an ad without this rate being set, the resulting orders will instead earn either: |

* The Shop Ads commission you configured in open collaboration, or
* The standard commission defined in this invitation.
   The commission rate is specified in increments of 1/10,000.
   For example, 1000 stands for 0.1 or 10%. |
   creator_user_open_ids |[]string |Y |["123123213213"] |Target collaboration 中邀请的 Creator 的 TikTok User Open ID 列表。Creator 最大数量为 50。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
   seller_contact_info |object |Y | |Target collaboration 中卖家的联系信息。 |
   ^email |string |Y |test@bytedance.com |卖家的电子邮件联系信息 |
   ^phone_number |string |N |1234567890 |卖家的电话号码。 |
   ^whatsapp |string |N |1234567890 |卖家注册 WhatsApp 使用的电话号码。 |
   ^telegram |string |N |1234567890 |卖家的 Telegram 用户名或电话号码。 |
   ^line |string |N |1234567890 |卖家注册 Line 应用使用的电话号码。 |
   free_sample_rule |object |Y | |卖家在 target collaboration 中设置的免费 sample 规则。 |
   ^has_free_sample |bool |Y |true |如果为 true，则向邀请到 target collaboration 的 creator 提供免费 sample。 |
   ^is_sample_approval_exempt |bool |Y |true |如果为 true，邀请到 target collaboration 的 creator 将免除卖家审核，并自动获得免费 sample。
   Note that if has_free_sample=false, this field will not take effect. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/target_collaborations/7890786712312312?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"name":"openapi_test","end_time":"1715654330","products":[{"id":"789078671231312312","commission_rate":1000,"target_ad_commission_rate":1000}],"creator_user_open_ids":["123123213213"],"seller_contact_info":{"email":"test@bytedance.com","phone_number":"1234567890","whatsapp":"1234567890","telegram":"1234567890","line":"1234567890"},"free_sample_rule":{"has_free_sample":true,"is_sample_approval_exempt":true}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^target_collaboration_conflicts | []object |  | 因 target collaboration 冲突导致 target collaboration 更新失败的 creator 和产品列表。 |
| ^^creator_user_open_id | string | 7494656937121841111 | Creator Open ID。更多详情：https://partner.tiktokshop.com/docv2/page/3obfokj6 |
| ^^product_id | string | 789078671231 | 产品标识符。 |
| ^update_failed | object |  | 描述哪些字段未成功更新。 |
| ^^remove_creator_open_ids | []string | ["12345"] | 未成功移除的 creator 的 TikTok User Open ID 列表。更多详情：https://partner.tiktokshop.com/docv2/page/3obfokj6 |
| ^^remove_product_ids | []string | ["12345"] | 未成功移除的产品 ID 列表。 |
| ^^add_creator_open_ids | []string | ["12345"] | 未成功添加的 creator 的 TikTok User Open ID 列表。更多详情：https://partner.tiktokshop.com/docv2/page/3obfokj6 |
| ^^add_products | object |  | 未成功添加的产品列表。 |
| ^^^id | string | 789078671231312312 | 产品标识符。 |
| ^^^commission_rate | int | 1000 | Target collaboration 的目标 commission 比率。目标 commission 比率以百分之一为单位。例如，3587 表示 35.87% 的 commission 比率。此值最小为 1000。 |
| ^^change_commissions | object |  | 未成功更改的 commission 信息列表。 |
| ^^^product_id | string | 789078671231312312 | 产品标识符。 |
| ^^^commission_rate | int | 1000 | Target collaboration 的目标 commission 比率。目标 commission 比率以百分之一为单位。例如，3587 表示 35.87% 的 commission 比率。此值最小为 1000。 |
| ^^end_time | int | 1715654330 | 未成功更新的 target collaboration 结束时间。 |
| ^^seller_contact_info | object |  | 未成功更新的 target collaboration 中卖家的联系信息。 |
| ^^^email | string | test@bytedance.com | 未成功更新的卖家电子邮件联系信息。 |
| ^^^phone_number | string | (+62) 1234567890 |  |
| 卖家的电话号码。 |  |  |  |
| ^^^whatsapp | string | (+62) 1234567890 |  |
| 卖家注册 WhatsApp 使用的电话号码。 |  |  |  |
| ^^^telegram | string | (+62) 1234567890 |  |
| 卖家的 Telegram 用户名或电话号码。 |  |  |  |
| ^^^line | string | (+62) 1234567890 |  |
| 卖家注册 Line 应用使用的电话号码。 |  |  |  |
| ^^name | string | openapi_test | Target collaboration 的名称。 |
| ^^invalid_product_id_list | []string | ["1234"] | 导致更新失败的产品 ID 列表。 |
| ^^invalid_open_id_list | []string | ["xxxxxx"] | 导致更新失败的 open ID 列表。 |
# 响应示例
```json
{"code":0,"data":{"target_collaboration_conflicts":[{"creator_user_open_id":"7494656937121841111","product_id":"789078671231"}],"update_failed":{"remove_creator_open_ids":["12345"],"remove_product_ids":["12345"],"add_creator_open_ids":["12345"],"add_products":{"id":"789078671231312312","commission_rate":1000},"change_commissions":{"product_id":"789078671231312312","commission_rate":1000},"end_time":1715654330,"seller_contact_info":{"email":"test@bytedance.com","phone_number":"(+62) 1234567890\n","whatsapp":"(+62) 1234567890\n","telegram":"(+62) 1234567890\n","line":"(+62) 1234567890\n"},"name":"openapi_test","invalid_product_id_list":["1234"],"invalid_open_id_list":["xxxxxx"]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 16024004 | 测试账号和非测试账号不能交叉邀请 |
| 16024006 | 卖家不能邀请其官方 creator。 |
| 16024008 | 存在不属于此商家的产品。 |
| 16024016 | 邀请失败，因为 creator 已关联店铺账号。 |
| 16024018 | 卖家不能邀请其拉黑的 creator |
| 16024019 | 配额不足，无法创建邀请 |
| 16024020 | 请移除被排除的 creator 以创建邀请 |
| 16024021 | 邀请包含超过粉丝限制的 creator |
| 36009007 | 请求超时 |
| 50001701 | target collaboration 已过期 |
| 50001702 | Your invitation target contains an unavailable creator or product. Please check your request params.Remove the unavailable creator or product id and try again. |
| 50001703 | 请求参数包含敏感词。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 98001004 | Parameter {param_name} is invalid. Reason: {reason}. Expected: {expected_value} |

