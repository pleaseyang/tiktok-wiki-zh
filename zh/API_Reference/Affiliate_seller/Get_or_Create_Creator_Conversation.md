# 获取或创建达人对话

# 路径：/affiliate_seller/202508/conversations
# 方法：[POST]
# 功能描述
此 API 用于获取与指定达人的对话。如果对话不存在，则创建新对话。

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
| creator_open_id | string | Y | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | 达人的 Open ID。请使用相关 API 返回的 Open ID，而非用户 ID、达人 ID 或卖家 ID。 [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
| only_need_conversation_id | bool | N | true | - 如果为 `true`, 仅返回 `data.conversation` 中的 `conversation_id`。 |

* 若为 `false`, 则返回 `data.conversation` 中的所有字段。
   `true` by default. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/conversations?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","only_need_conversation_id":true}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^conversation_id | string | 1234567890 | 对话的唯一 ID。 |
| ^is_new | bool | true | 是否为新对话。 |
| ^username | string | test_creator_name | TikTok 达人的用户名。 |
| ^avatar | string | https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp | TikTok 达人头像图片文件的 URL。 |
| ^unread_count | int | 2 | 店铺未读消息数量。 |
| ^creator_im_id | string | 12345678 | 达人的 IM 用户 ID。 |
# 响应示例
```json
{"code":0,"data":{"conversation_id":"1234567890","is_new":true,"username":"test_creator_name","avatar":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp","unread_count":2,"creator_im_id":"12345678"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16030001 | 达人已被清除 |
| 16030002 | 店铺已达到 IM 配额。 More information please check [https://seller.tiktokglobalshop.com/university/essay?identity=1&role=1&knowledge_id=2766765165102865&from=feature_guide] |
| 16030003 | 此店铺暂时无法向达人发送消息，因为未达到 Affiliate GMV 要求。 |
| 16030007 | 店铺状态无效 |
| 16030009 | test account isolate. please don't use the test account to send message. |
| 16032001 | 无效参数达人和卖家，请确保地区匹配。 |
| 45101021 | unauthorized operation on users who hit privacy control |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

