# 获取达人对话消息

# 路径：/affiliate_seller/202412/conversation/{conversation_id}/messages
# 方法：[GET]
# 功能描述
此 API 用于获取指定对话中的消息列表。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| conversation_id | string | Y | 1234567890 | 属于当前卖家的对话标识符。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_size | int | Y | 20 | 返回的最大消息数量。必须在 1 到 20 之间。 |
| page_token | string | N | 1735032460678899 | 分页游标。首次请求时省略此参数。当 `has_more` 为 `true` 时，传入上一次响应的 `next_page_token` 以获取下一页。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202412/conversation/1234567890/messages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=20&page_token=1735032460678899
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^has_more | bool | true | 是否还有更多消息。 |
| ^next_page_token | string | 1735032460678899 | 当 `has_more` 为 `true` 时，在下次请求中将此游标作为 `page_token` 传入。当 `has_more` 为 `false` 时，该值为空。 |
| ^messages | []object |  |  |
| ^^conversation_index | string | 1735032460678899 | 消息在会话中的索引。索引越大，消息越新。 |
| ^^message_body | object |  | 消息内容 |
| ^^^id | string | 7451907556216407553 | Message ID. |
| ^^^conversation_id | string | 7451873679308620048 | 消息所属的会话 ID。 |
| ^^^type | string | TEXT | Message type. 可能的值： |

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
   ^^^content |string |{"content": "simple text message"} |序列化为 JSON 字符串的消息内容. JSON 对象取决于 `type`:
* `TEXT`: `{"content": "simple text"}`
* `PRODUCT_CARD`: `{"product_id": "12345"}`
* `TARGET_COLLABORATION_CARD`: `{"invitation_group_id": "1234"}`
* `FREE_SAMPLE_CARD`: `{"apply_id": "1234"}`
* `IMAGE`: `{"height": "290", "url": "<image_url>", "width": "304"}`
* `CRM_TEXT_WITH_IMAGE_CARD`: `{"title": "abc", "content": "efg", "url": "<image_url>"}`
* `CRM_TEXT_WITH_PRODUCTS_CARD`: `{"title": "abc", "content": "efg", "product_ids": [123, 456, 789, 222]}`
* `NOTIFICATION` or `SYSTEM`: `{"content": "notification/system message"}`
* `EMOTICONS`: `{"height": "110", "url": "<image_url>", "width": "110"}` |
   ^^^create_time |int |1691411573 |消息创建时间，以 Unix 时间戳 (秒) 表示。 |
   ^^^sender_id |string |2368694990397660924 |消息发送者的 im id |

# 响应示例
```json
{"code":0,"data":{"has_more":true,"next_page_token":"1735032460678899","messages":[{"conversation_index":"1735032460678899","message_body":{"id":"7451907556216407553","conversation_id":"7451873679308620048","type":"TEXT","content":"{\"content\": \"simple text message\"}","create_time":1691411573,"sender_id":"2368694990397660924"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16032001 | 无效参数达人和卖家，请确保地区匹配。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

