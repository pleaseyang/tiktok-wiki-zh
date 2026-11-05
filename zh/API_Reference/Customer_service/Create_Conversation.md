# 创建 Conversation

# Path: /customer_service/202309/conversations
# Method: [POST]
# 功能描述
使用此 API 代表店铺与指定买家创建 conversation。当不存在历史 conversation 时，调用此 API 将创建一个新的 conversation；当存在历史 conversation 时，无论其状态是活跃、已结束还是已关闭，调用此 API 都将重新打开该 conversation，并返回与历史 conversation 相同的 conversation ID。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| buyer_user_id | string | Y | 7494560109732338459 | 买家的用户 ID |
| 该值与 [Get Order Detail](650aa8ccc16ffe02b8f167a0) 响应数据中的 `data.orders.user_id` 相同。 |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202309/conversations?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"buyer_user_id":"7494560109732338459"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^conversation_id | string | 7106888323922608389 | Conversation ID。 |
| 买家与店铺之间 conversation 的唯一标识符。 |  |  |  |
# 响应示例
```json
{"code":0,"data":{"conversation_id":"7106888323922608389"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 45109003 | 无法创建 conversation，因为您未满足发起 conversation 的条件。详情请参考 [Customer Service API 概览](659645f9a46cdd02bc8aeacf#Important%20Concepts)。 |
