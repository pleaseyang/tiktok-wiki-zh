# 获取退货记录

# Path: /return_refund/202309/returns/{return_id}/records
# Method: [GET]
# 功能描述
使用此 API 检索特定退货请求的记录条目。data.records 中的每个条目代表指定 return_id 的一个操作或生命周期事件。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| return_id | string | Y | 4035318504086604100 | TikTok Shop 退货请求的唯一标识符。 |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| locale | string | N | en-US | 用于显示退货原因的 BCP-47 locale 代码，以逗号分隔。默认值：en-US |
| 支持的 locale 代码列表请参考 [Locale codes](678e3a47bae28f030a8c7523)。 |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202309/returns/4035318504086604100/records?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^records | []object |  | 退货记录列表。 |
| ^^event | string | ORDER_RETURN | 表示此记录描述哪个生命周期事件的事件类型。它可能因当前状态和请求的退货流程而异，包括初始请求、seller 操作、运输事件以及超时或系统事件。 |
| ^^role | string | BUYER | 发起此生命周期事件的操作方。可能的值： |

* `BUYER`
* `SELLER`
* `OPERATOR`：操作由客服人员手动触发。
* `SYSTEM`：操作因策略原因自动触发。 |
   ^^description |string |Customer submitted a return request |此生命周期事件的可读描述。 |
   ^^reason_text |string |Wrong product was sent |退货原因对应的文本，基于 locale 输入参数进行本地化。 |
   ^^note |string |Reach an agreement with the buyer |与退货记录关联的备注。使用 role 来识别事件的发起方。 |
   ^^images |[]object | |Seller 或 buyer 提供的图片。您可以使用 role 字段来区分图片是来自 seller 还是 buyer。 |
   ^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |图片 URL。 |
   ^^^width |int |200 |图片宽度。
   单位：px |
   ^^^height |int |200 |图片高度。
   单位：px |
   ^^videos |[]object | |Buyer 上传的视频。仅 buyer 允许上传视频。 |
   ^^^url |string |https://v16m-default.akamaized.net/1e26046c3df91cd008d2ababba9445e2/65005d33/video/tos/maliva/tos-maliva-v-d8ca36-us/oQVCbIQemDpQxI9lHsg9IXQAb7mwgBabababab |视频 URL。 |
   ^^^cover |string |https://p16-oec-va.ibyteimg.com/musically-maliva-obj/998d0381960bda1ef272f4a7724cf5ed~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405489 |视频缩略图。 |
   ^^^width |int |200 |视频图片宽度。
   单位：px |
   ^^^height |int |200 |视频图片高度。
   单位：px |
   ^^^duration_millis |int |3000 |视频时长。
   单位：毫秒 |
   ^^create_time |int |1690532213 |此记录条目创建时的 Unix 时间戳（秒）。 |

# 响应示例
```json
{"code":0,"data":{"records":[{"event":"ORDER_RETURN","role":"BUYER","description":"Customer submitted a return request","reason_text":"Wrong product was sent","note":"Reach an agreement with the buyer","images":[{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200}],"videos":[{"url":"https://v16m-default.akamaized.net/1e26046c3df91cd008d2ababba9445e2/65005d33/video/tos/maliva/tos-maliva-v-d8ca36-us/oQVCbIQemDpQxI9lHsg9IXQAb7mwgBabababab","cover":"https://p16-oec-va.ibyteimg.com/musically-maliva-obj/998d0381960bda1ef272f4a7724cf5ed~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405489","width":200,"height":200,"duration_millis":3000}],"create_time":1690532213}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

