# 获取最新未读消息

# 路径：/affiliate_seller/202412/conversations/messages/list/newest
# 方法：[GET]
# 功能描述
此 API 用于获取每个对话中最新的未读消息。

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
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202412/conversations/messages/list/newest?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^newest_message_list | []object |  | 最近一分钟内的未读消息列表。 |
| ^^conversation_id | string | 12345 | 消息所属的对话 ID |
| ^^content | string | {"content": "simple text message"} | 消息内容，为 JSON 序列化字符串。将该字符串解析为 JSON 对象；其结构取决于 `type`: |

* `TEXT`: `{"content": "simple text"}`
* `PRODUCT_CARD`: `{"product_id": "12345"}`
* `TARGET_COLLABORATION_CARD`: `{"invitation_group_id": "1234"}`
* `FREE_SAMPLE_CARD`: `{"apply_id": "1234"}`
* `IMAGE`: `{"height": "290", "url": "<image URL>", "width": "304"}`
* `CRM_TEXT_WITH_IMAGE_CARD`: `{"title": "abc", "content": "efg", "url": "<image URL>"}`
* `CRM_TEXT_WITH_PRODUCTS_CARD`: `{"title": "abc", "content": "efg", "product_ids": [123, 456, 789, 222]}`
* `NOTIFICATION` or `SYSTEM`: `{"content": "notification or system message"}`
* `EMOTICONS`: `{"height": "110", "url": "<image URL>", "width": "110"}` |
   ^^type |string |TEXT |消息类型。可能的值：
* TEXT
* PRODUCT_CARD
* TARGET_COLLABORATION_CARD
* FREE_SAMPLE_CARD
* IMAGE
* CRM_TEXT_WITH_IMAGE_CARD
* CRM_TEXT_WITH_PRODUCTS_CARD
* NOTIFICATION
* EMOTICONS
* SYSTEM |
   ^^sender_id |string |12345678 |发送者的 IM id |
   ^^unread_message_count |int |1 |会话中发送方的未读消息数。 |

# 响应示例
```json
{"code":0,"data":{"newest_message_list":[{"conversation_id":"12345","content":"{\"content\": \"simple text message\"}","type":"TEXT","sender_id":"12345678","unread_message_count":1}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

