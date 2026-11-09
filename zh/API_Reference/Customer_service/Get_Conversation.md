# 获取 Conversation

# 路径：/customer_service/202601/conversations/{conversation_id}
# 方法：[GET]
# 功能描述
使用此 API 通过 ID 获取 conversation 的信息。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| conversation_id | string | Y | 7494560109732334261 | Conversation ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| need_session_id | bool | N | false | 设置为 `true` 以请求 `cur_session_id`。该字段在当前开放 session 信息可用时返回；当 `need_session_info` 为 `true` 时也可能返回。 |
| need_session_info | bool | N | false | 设置为 `true` 以请求 `cur_session` 和 `cur_session_id`。这些字段在当前开放 session 信息可用时返回。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202601/conversations/7494560109732334261?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&need_session_id=false&need_session_info=false
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^conversation | object |  | Conversation 信息。 |
| ^^id | string | 7494560109732334261 | Conversation ID |
| ^^participant_count | int | 3 | Conversation 中的参与者数量。 |

* 如果 conversation 中没有客服人员参与，则值为 `2`：店铺和买家；
* 否则，值为 `3`：店铺、买家和客服人员。 |
   ^^participants |[]object | |Conversation 参与者。 |
   ^^^im_user_id |string |7494560109732334261 |参与者在 IM 系统中的 ID。此 ID 用于 IM 系统，不能用于查询订单。要查询订单，请使用 `user_id`。 |
   ^^^role |string |BUYER |参与者的角色。
   可能的枚举值：
* `BUYER`
* `SHOP`
* `CUSTOMER_SERVICE` |
   ^^^nickname |string |Albert |参与者的昵称。 |
   ^^^avatar |string |https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image? |参与者的头像 URL。 |
   ^^^user_id |string |7494560109732334262 |参与者的 ID。 |
   ^^^platform |string |TIKTOK_SHOP |买家来自的平台。
   此字段仅在参与者角色为 `BUYER` 且店铺所在地区为印度尼西亚时返回。可能的值：
* `TIKTOK_SHOP`
* `TOKOPEDIA`
   您不能向来自不同平台的买家发送特定平台的内容。例如，向 Tokopedia 买家发送商品卡片时，请确保该商品已在 Tokopedia 上架。 |
   ^^create_time |int |1691411573 |Conversation 创建时的 Unix 时间戳。单位为秒。 |
   ^^unread_count |int |0 |客服人员未读消息数量。 |
   ^^cur_session_id |string |7494472109882334261 |当前开放 session 的 ID。当 `need_session_id` 或 `need_session_info` 为 `true` 且当前开放 session 信息可用时返回此字段。 |
   ^^cur_session |object | |当前开放 session 的信息。当 `need_session_info` 为 `true` 且当前开放 session 信息可用时返回此字段。 |
   ^^^id |string |7494472109882334261 |当前 session ID。 |
   ^^^phase |string |ASSIGNED |session 的当前阶段。
   可能的枚举值：
* `AUTO_REPLY` — session 正在由自动回复或聊天机器人处理。
* `QUEUED` — session 正在等待分配给客服人员。
* `ASSIGNED` — session 已分配给客服人员。 |

# 响应示例
```json
{"code":0,"data":{"conversation":{"id":"7494560109732334261","participant_count":3,"participants":[{"im_user_id":"7494560109732334261","role":"BUYER","nickname":"Albert","avatar":"https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image?","user_id":"7494560109732334262","platform":"TIKTOK_SHOP"}],"create_time":1691411573,"unread_count":0,"cur_session_id":"7494472109882334261","cur_session":{"id":"7494472109882334261","phase":"ASSIGNED"}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 45101003 | 未找到记录。请检查参数。 |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
