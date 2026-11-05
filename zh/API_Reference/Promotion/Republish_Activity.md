# 重新发布活动

# Path: /promotion/202607/activities/{activity_id}/republish
# Method: [POST]
# 功能描述
使用此 API 重新发布在过去 7 天内过期或被停用的商品折扣活动或限时抢购活动。此 API 仅支持 FIXED_PRICE、FLASHSALE 和 DIRECT_DISCOUNT 活动。您必须通过传递新的 begin_time 和 end_time 来提供新的生效时间段。已与活动关联的商品和 SKU 无需重新添加。活动重新发布后，您可以像往常一样编辑活动并修改其商品或 SKU。我们建议使用此 API 而不是重新创建活动，以减少添加商品 API 的请求次数。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| activity_id | string | Y | 7657162458772768530 | 标识不同活动的唯一 ID。 |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| end_time | int | N | 1782895064 | 活动结束时间，以秒为单位的 Unix 时间戳。必须晚于 begin_time，且生效周期至少为 10 分钟。最大周期取决于活动类型和店铺区域；对于 FLASHSALE 活动，不得超过 3 天。 |
| begin_time | int | N | 1782875064 | 活动开始时间，以秒为单位的 Unix 时间戳。该值必须晚于当前时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/promotion/202607/activities/7657162458772768530/republish?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"end_time":1782895064,"begin_time":1782875064}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^activity_id | string | 7136104329798256386 | 成功时，重新发布的活动的 ID。这与请求路径中提供的 activity_id 相同；重新发布不会创建新活动。使用此 ID 进行后续的活动、商品或 SKU 编辑。 |
# 响应示例
```json
{"code":0,"data":{"activity_id":"7136104329798256386"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 17003243 | 此活动不允许重新发布 |
