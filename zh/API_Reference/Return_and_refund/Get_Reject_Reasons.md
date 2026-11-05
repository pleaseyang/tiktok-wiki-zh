# 获取拒绝原因

# Path: /return_refund/202309/reject_reasons
# Method: [GET]
# 功能描述
使用此 API 检索当前适用于指定售后请求的 seller 拒绝原因选项。调用相应的 seller 拒绝 API 时，使用返回的 name 值作为拒绝原因 key。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| locale | string | N | en-US | 用于显示拒绝原因的 BCP-47 locale 代码，以逗号分隔。默认值：en-US |
| 支持的 locale 代码列表请参考 [Locale codes](678e3a47bae28f030a8c7523)。 |  |  |  |  |
| return_or_cancel_id | string | Y | 4035319218955782461 | 订单退货或取消的唯一标识符。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202309/reject_reasons?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&return_or_cancel_id=4035319218955782461
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^reasons | []object |  | seller 提供的拒绝原因列表。 |
| ^^name | string | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer | 拒绝原因 key。将此确切值传递给相应的 seller 拒绝 API 作为拒绝原因。注意：可用的拒绝原因可能会根据当前售后请求上下文而变化。为避免使用过时或不适用的原因 key，请在拒绝操作之前调用此 API 并使用最新返回的 name 值，而不是硬编码。 |
| ^^text | string | You have reached an agreement with the buyer | 与原因 name 对应的文本，基于 locale 输入参数进行本地化。 |
# 响应示例
```json
{"code":0,"data":{"reasons":[{"name":"seller_reject_apply_you_have_reached_an_agreement_with_the_buyer","text":"You have reached an agreement with the buyer"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

