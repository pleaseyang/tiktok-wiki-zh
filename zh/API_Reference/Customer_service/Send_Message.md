# 发送消息

# 路径：/customer_service/202606/conversations/{conversation_id}/messages
# 方法：[POST]
# 功能描述
使用此 API 在 conversation 中向买家发送消息。

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
| conversation_id | string | Y | 7494560109732334262 | Conversation ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| type | string | Y | TEXT | 消息类型。可能的枚举值： |

* `TEXT`
* `IMAGE`
* `VIDEO`
* `PRODUCT_CARD`
* `ORDER_CARD`
* `RETURN_REFUND_CARD`
* `COUPON_CARD`
* `LOGISTICS_CARD` |
   content |string |Y |{"content": "test"} |消息内容，JSON 序列化字符串格式。

各类型消息的 content 示例如下：

* TEXT：
   {
   "content": "hi, I want to get refunded."
   }
   （注意：最多 2000 个字符。请勿使用违反 TikTok Shop 条款和政策的敏感词。）
* VIDEO
   {
   "vid": "v10394g5000cd499vc7og65mqn3r3dg0"
   }
* LOGISTICS_CARD
   {
   "order_id": "580874485811283206",
   "package_id": "123456" // 可选（建议用于一个订单有多个包裹的情况；一个订单一个包裹时不需要）
   }
* PRODUCT_CARD
   {
   "product_id": "7494560109732334265"
   }
* ORDER_CARD：
   {
   "order_id": "7494560109732334267"
   }
* RETURN_REFUND_CARD：
   {
   "order_id": "7494560109732334267",
   "sku_id": "7494560109732363423"
   }
   注意：发送 RETURN_REFUND_CARD 的订单必须满足售后条件。要检查资格，请使用 [Get Aftersale Eligibility](650ab645c16ffe02b8f2e1c1)。
* IMAGE：
   {
   "url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476",
   "width": 1280,
   "height": 720
   }

注意：您可以通过调用 [Upload Buyer Messages Image](650a599d0fcef602bf2a1dc8) 获取 `url` 的值。

* COUPON_CARD：
   {
   "coupon_id": "7262992004278206762"
   }
   注意：可在消息中发送的优惠券必须满足以下所有条件：
1. `display_type==CHAT` 或 `display_type==REGULAR`
2. `status==ONGOING`
3. `creation_source==SELLER_CENTER`
4. `target_buyer_segment!=REPEAT_CUSTOMERS` |
   sender_role |string |N |CUSTOMER_SERVICE |消息发送角色。
* 'CUSTOMER_SERVICE'：由真实客服人员回复的消息
* 'SYSTEM'：由系统自动触发的回复，如欢迎消息和超时回复
* 'ROBOT'：由智能机器人回复的消息 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202606/conversations/7494560109732334262/messages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"type":"TEXT","content":"{\"content\": \"test\"}","sender_role":"CUSTOMER_SERVICE"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^message_id | string | 7494560109732334261 | 消息 ID |
# 响应示例
```json
{"code":0,"data":{"message_id":"7494560109732334261"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 45101002 | 参数无效。RETURN_REFUND_CARD 必须满足上述条件。 |
| 45101003 | 未找到记录。请检查参数。 |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 45101006 | 您不能发送包含敏感内容的消息。请检查消息内容。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 45102007 | 无权访问此 conversation。可能存在数据损坏。请稍后重试或联系技术支持团队寻求帮助。 |
| 45109001 | 由于 conversation 规则无法发送消息。详情请参考 [Customer Service API 概览](659645f9a46cdd02bc8aeacf#Important%20Concepts)。 |
| 45111001 | 不支持 |
| 45111007 | 买家已达到此优惠券的最大领取限制。 |
| 45111012 | 由于超出 QPS 限制，发送优惠券卡片消息失败。发送优惠券卡片消息的 QPS 限制为 0.5。 |
| 45111017 | 参数无效。COUPON_CARD 必须满足上述条件。 |
