# 发送 Engagement Message

# Path: /customer_engagement/202412/messages
# Method: [POST]
# 功能描述
为特定的 engagement task 向指定客户发送消息。

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
| buyer_emails | []string | Y | ["v43424bDOUSGKQQ7YLNEGXPED3CNCQO24@scs.tiktokw.us","v4b1232DOUSGKQQ7YLNEMPPEPBORFEQ2A@scs.tiktokw.us"] | 买家的匿名化 email 地址。从 [Get Order Details API](650aa8ccc16ffe02b8f167a0) 获取这些值。 |
每次请求提供 1 到 50 个地址。
**注意**：您只能向在过去 365 天内在店铺至少下过一笔订单的买家发送消息。 |
task_id |string |N |1381478460934 |关联的 customer engagement task 的 ID。使用调用 [Create Engagement Task API](67777e436b61b002f60f01da) 时返回的值。
**注意**：确保任务仍然活跃。您不能向已结束的任务发送消息。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_engagement/202412/messages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"buyer_emails":["v43424bDOUSGKQQ7YLNEGXPED3CNCQO24@scs.tiktokw.us","v4b1232DOUSGKQQ7YLNEMPPEPBORFEQ2A@scs.tiktokw.us"],"task_id":"1381478460934"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 每个买家的验证或资格错误列表。 |
| ^^code | int | 68009003 | 错误码。 |
| ^^message | string | The user adresss is invalid | 错误消息。 |
| ^^detail | object |  | 错误详情。 |
| ^^^buyer_email | string | v4b1232DOUSGKQQ7YLNEMPPEPBORFEQ2A@scs.tiktokw.us | 与错误关联的买家匿名化 email 地址。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":68009003,"message":"The user adresss is invalid","detail":{"buyer_email":"v4b1232DOUSGKQQ7YLNEMPPEPBORFEQ2A@scs.tiktokw.us"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 68009001 | 访问被拒绝。此店铺无法使用此 endpoint，因为卖家不满足 CRM 功能的访问条件。详情请参见 TikTok Shop Academy。 |
| 68009002 | 指定的任务已结束，不再允许发送消息。 |
| 68009003 | The user adresss is invalid |
| 68009004 | 无法向指定的买家 email 发送消息，因为该买家在过去 365 天内未在店铺下过订单。 |
