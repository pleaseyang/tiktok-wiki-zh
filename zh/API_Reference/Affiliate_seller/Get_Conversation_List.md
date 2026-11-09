# 获取对话列表

# 路径：/affiliate_seller/202412/conversations
# 方法：[GET]
# 功能描述
此 API 用于获取卖家 IM 对话列表。您可以按对话状态、创建时间等条件筛选对话。

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
| page_size | int | Y | 20 | 每页返回的对话数量。范围：1–50。 |
| page_token | string | N | 12345678 | 分页游标。首次请求时省略此参数。后续页面使用上一次响应返回的 `next_page_token`。 |
| only_need_conversation_id | bool | N | true | - 如果为 `true`，则仅返回 `conversation` 中的 `conversation_id`。 |

* 如果为 `false`，则返回 `conversation` 中的所有字段。默认为 `true`。 |
   conversation_status |string |N |UNREPLIED |按状态筛选返回的 IM 对话。如果省略，API 返回所有状态的对话。

可能的值：

* `ALL`: 无论状态如何，获取所有对话。
* `UNREAD`: 获取卖家有未读消息的对话。消息保持未读状态，直到通过调用 [Mark Conversation Read](6791db761882810314a991a8); 回复不会更改已读状态。
* `UNREPLIED`: 获取卖家不是最后一条消息发送者的对话。
* `STARRED`: 获取卖家置顶的对话。
* `ARCHIVED`: 获取卖家归档的对话。 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| only_need_conversation_id | bool | N | true | - 如果为 `true`，则仅返回 `data.conversation` 中的 `conversation_id`。 |

* 如果为 `false`，则返回 `data.conversation` 中的所有字段。
   默认为 `true`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202412/conversations?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=20&page_token=12345678&only_need_conversation_id=true&conversation_status=UNREPLIED
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^has_more | bool | true | 是否还有更多对话。 |
| ^next_page_token | string | 12345678 | 下一页的分页游标。当 `has_more` 为 `true` 时，将此值作为 `page_token` 传入下一次请求。 |
| ^conversations | []object |  | 对话列表。 |
| ^^id | string | 12345678 | 对话唯一 ID。 |
| ^^unread_count | int | 2 | 未读消息数量。 |
| ^^username | string | test_creator_name | TikTok 用户名。 |
| ^^avatar | string | https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp | TikTok 达人头像图片文件的 URL。 |
| ^^creator_im_id | string | 12345678 | 达人的 IM 用户 ID。 |
# 响应示例
```json
{"code":0,"data":{"has_more":true,"next_page_token":"12345678","conversations":[{"id":"12345678","unread_count":2,"username":"test_creator_name","avatar":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp","creator_im_id":"12345678"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

