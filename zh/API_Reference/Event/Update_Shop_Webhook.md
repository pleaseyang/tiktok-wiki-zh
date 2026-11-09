# 更新店铺 Webhook

# 路径：/event/202309/webhooks
# 方法：[PUT]
# 功能描述
更新店铺特定事件主题的 webhook URL。

---


# 公共参数
有关公共参数，请参阅[如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [获取授权店铺](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| address | string | 是 | https://partner.tiktokshop.com | 用于接收事件数据的 HTTP 或 HTTPS webhook URL。 |
| 最大长度：255 个字符 |  |  |  |  |
| event_type | string | 是 | ORDER_STATUS_CHANGE | webhook 事件的主题。 |
| 可能的值： |  |  |  |  |

* `ORDER_STATUS_CHANGE`：每次订单状态更新时触发，从新订单下达到所有后续状态变更。参见[订单状态变更](650300b8a57708028b430b4a)。
* `RECIPIENT_ADDRESS_UPDATE`：收件人地址更新时触发。参见[收件人地址更新](650301af5a12ff0294ea3bf9)。
* `PACKAGE_UPDATE`：包裹更新时触发（例如，合并、拆分或地址变更）。参见[包裹更新](650955cabace3e02b73cc886)。
* `PRODUCT_STATUS_CHANGE`：商品审核结果更新时触发。参见[商品状态变更](650956aff1fd3102b90b6261)。
* `SELLER_DEAUTHORIZATION`：卖家取消授权时触发，以通知开发者并避免对平台授权问题的误解。参见[卖家取消授权](65095746defece02be4d749d)。
* `UPCOMING_AUTHORIZATION_EXPIRATION`：在授权到期前 30 天触发，每天 0:00 发送通知，直到完成重新授权。参见[即将到期的授权](6509579c0fcef602bf11312c)。
* `CANCELLATION_STATUS_CHANGE`：订单取消状态变更时触发。参见[取消状态变更](65030150746462028285f657)。
* `RETURN_STATUS_CHANGE`：订单退货状态变更时触发。参见[退货状态变更](65030162bb2a4d028d50cc51)。
* `NEW_CONVERSATION`：客服坐席加入或离开对话时触发。参见[新对话](6614330bfe9fdc02e002abfd)。
* `NEW_MESSAGE`：客服对话中发送新消息时触发。参见[新消息](66143486ef8a1202dc323258)。
* `PRODUCT_INFORMATION_CHANGE`：商品的标题、描述、主图或属性变更上线时触发。参见[商品信息变更](65d6f41411a60f02dc1cf8bf)。
* `PRODUCT_CREATION`：新商品创建时触发。参见[商品创建](663c98b566828e02e4515580)。
* `PRODUCT_CATEGORY_CHANGE`：商品类目变更时触发。参见[商品类目变更](668764a371f16d02eef1f393)。
* `NEW_MESSAGE_LISTENER`：达人向卖家发送消息时触发。参见[新消息监听](6790b76eb59cf9030997b783)。
* `INVOICE_STATUS_CHANGE`：使用 [POST 上传发票](67b542559a140004b343984f) endpoint 后，发票上传状态变更时触发。参见[发票状态变更](67b68ca185619104a6772e5d)。
* `PRODUCT_AUDIT_STATUS_CHANGE`：商品审核状态变更时触发。参见[商品审核状态变更](67b5c6cba42623049abe5062)。
* `REVERSE_STATUS_UPDATE`：买家发起取消、仅退款或退货退款请求且需要卖家接受或拒绝时触发。参见[逆向状态更新](https://partner.tiktokshop.com/doc/page/63fd7459715d622a338c5437)。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/event/202309/webhooks?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"address":"https://partner.tiktokshop.com","event_type":"ORDER_STATUS_CHANGE"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅[如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |


