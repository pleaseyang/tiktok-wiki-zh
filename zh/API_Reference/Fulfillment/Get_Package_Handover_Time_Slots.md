# 获取 Package 交接时间段

# 路径：/fulfillment/202309/packages/{package_id}/handover_time_slots
# 方法：[GET]
# 功能描述
使用此 API 获取指定 package 的上门揽收时间段以及 pickup、drop-off 和（在英国）van collection 的交接可用性。当可用时，响应还会提供用于查找 drop-off 地点的 URL。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| package_id | string | Y | 5433567853345 | TikTok Shop package ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/5433567853345/handover_time_slots?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^can_pickup | bool | true | 此 package 是否支持上门揽收。 |
| ^can_drop_off | bool | true | 此 package 是否可以 drop-off 到指定地点 |
| ^can_van_collection | bool | true | 英国特有。使用此字段判断 van collection 是否可用。 |
| ^drop_off_point_url | string | https://jtexpress.my/location | 通过提供的 URL 查看 package drop-off 地点。 |
| ^pickup_slots | []object |  | 上门揽收时间段。检查 `avaliable` 以确定每个时间段是否可以预约。 |
| ^^start_time | int | 1623812664 | package 揽收时间段的开始时间，Unix 时间戳，单位为秒。 |
| ^^end_time | int | 1623812664 | package 揽收时间段的结束时间，Unix 时间戳，单位为秒。 |
| ^^avaliable | bool | true | 此时间段是否可以预约。 |
# 响应示例
```json
{"code":0,"data":{"can_pickup":true,"can_drop_off":true,"can_van_collection":true,"drop_off_point_url":"https://jtexpress.my/location","pickup_slots":[{"start_time":1623812664,"end_time":1623812664,"avaliable":true}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11001027 | 系统超时。如果此错误持续存在，请联系平台寻求帮助。 |
| 11021009 | 此请求没有可用的 shipping 服务。请修改 package 重量或检查收件人地址。如果错误持续存在，请联系平台寻求帮助。 |
| 21001001 | 参数无效。请确保您传递了正确的请求参数。 |

