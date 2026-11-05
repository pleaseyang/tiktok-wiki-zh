# 发送 IM 消息

# Path: /affiliate_seller/202412/conversations/{conversation_id}/messages
# Method: [POST]
# 功能描述
此 API 用于向指定对话发送 IM 消息。支持发送文本消息和图片消息。

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
| conversation_id | string | Y | 1234 | conversation_id |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| msg_type | string | Y | TEXT | 消息类型。该值决定 `content` 中需要的解码 JSON 对象。可能的值： |

* `TEXT`
* `PRODUCT_CARD`
* `TARGET_COLLABORATION_CARD`
* `FREE_SAMPLE_CARD`
* `IMAGE`
* `CRM_TEXT_WITH_IMAGE_CARD`
* `CRM_TEXT_WITH_PRODUCTS_CARD` |
   content |string |Y |{"content": "simple text message"} |消息内容，JSON 序列化字符串格式。解码后的 JSON 对象取决于 `msg_type`：
* `TEXT`: `{"content": "simple text"}`. `content` 为必填项，不能为空，最多支持 2,000 个 Unicode 字符。
* `PRODUCT_CARD`: `{"product_id": "12345"}`. `product_id` 为必填项。
* `TARGET_COLLABORATION_CARD`: `{"target_collaboration_id": "1234"}`. `target_collaboration_id` 为必填项，即邀请组 ID。
* `FREE_SAMPLE_CARD`: `{"apply_id": "1234"}`. `apply_id` 为必填项。
* `IMAGE`: `{"url": "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476", "width": 1280, "height": 720}`. `url`, `width`, 和 `height` 为必填项； `width` 和 `height` 必须为整数。您可以通过调用 `url` 获取 [Upload Messages Image](https://partner.tiktokshop.com/docv2/page/upload-message-image-v2-202608).
* `CRM_TEXT_WITH_PRODUCTS_CARD`: `{"product_ids": "12345,123456", "title": "abc", "content": "abc"}`. `product_ids` is required 和 包含一到五个以逗号分隔的正产品 ID。 `content` 为必填项，不能为空，最多支持 500 个 Unicode 字符。 `title` 最多支持 50 个 Unicode 字符。
* `CRM_TEXT_WITH_IMAGE_CARD`: `{"image_url": "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476", "title": "abc", "content": "abc"}`. `image_url` 和 `content` 为必填项。 `content` must not be empty 和 supports up to 500 Unicode characters. `title` 最多支持 50 个 Unicode 字符。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202412/conversations/1234/messages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"msg_type":"TEXT","content":"{\"content\": \"simple text message\"}"}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^message_id | string | 1234444 | 消息 ID。`message_id` 字段不一定在消息提交成功时返回。 |
# 响应示例
```json
{"code":0,"data":{"message_id":"1234444"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 16030100 | 店铺已达到与此 creator 的 ID 的 IM 发送消息配额 |
| 16030101 | 卖家账号异常或店铺等级未达到 GMV 要求，无法联系此 creator。 |
| 16032001 | nvalid parameter Creator 和 Seller, please ensure Region mismatch. |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

