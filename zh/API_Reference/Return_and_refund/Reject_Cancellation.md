# 拒绝取消

# 路径：/return_refund/202309/cancellations/{cancel_id}/reject
# 方法：[POST]
# 功能描述
使用此 API 拒绝指定 cancel_id 的 buyer 取消请求。在调用此 API 之前，请确保请求仍处于当前允许卖家拒绝的状态。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| cancel_id | string | Y | 4035319218955782461 | 待拒绝的取消请求 ID。使用 Search Cancellations 返回的 `cancel_id`。请勿在此处传递订单 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| idempotency_key | string | N | 40b456b1-78e7-412d-9fe6-82181496e1bd | 幂等性 key 是由客户端生成的唯一值，服务器用于识别相同请求。每次重试该请求时请复用相同的 key。如果省略此参数，服务器将为该次请求生成一个 key。您可以选择自己的方法来创建唯一 key。我们建议使用 UUID 或其他具有足够熵的随机字符串以避免冲突。幂等性 key 最长可达 255 个字符。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| reject_reason | string | Y | seller_reject_apply_product_has_been_packed | 卖家拒绝 buyer 订单取消请求的原因。使用 [Get Decision Eligibility](https://partner.tiktokshop.com/docv2/page/69844a11eeba77049695c7f6) endpoint 检索当前可用于同一取消请求的拒绝原因，并在此字段中提交返回的拒绝原因 name。 |
| comment | string | N | 在取消请求前我已打包商品 | 卖家对拒绝决策的备注。这是卖家提供有关拒绝请求更多信息的地方。 |
| images | []object | N |  | 卖家提供的用于支持卖家拒绝订单取消请求决策的图片列表。 |
| ^image_id | string | Y | tos-maliva-i-o3syd03w52-us/57a1c8908fe74572861ea5e50887d8d1 | 图片 ID。 |
| ^mime_type | string | N | image/png | MIME 类型。 |
| ^height | int | N | 200 | 图片高度。 |
| 单位：px |  |  |  |  |
| ^width | int | N | 200 | 图片宽度。 |
| 单位：px |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202309/cancellations/4035319218955782461/reject?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&idempotency_key=40b456b1-78e7-412d-9fe6-82181496e1bd
```

**Body**
```json
{"reject_reason":"seller_reject_apply_product_has_been_packed","comment":"I have packed the products before cancellation request","images":[{"image_id":"tos-maliva-i-o3syd03w52-us/57a1c8908fe74572861ea5e50887d8d1","mime_type":"image/png","height":200,"width":200}]}
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
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 11050001 | invalid param |
| 25001001 | 传递了无效的请求参数。请检查您是否具有正确的参数类型和格式。 |
| 25001003 | 无效的订单状态。 |
| 25001014 | 未知的退货原因。请确保您传递的是有效的退货原因。 |
| 25001016 | reverse reason not match action type |
| 25001020 | 提供的退货原因当前已下线。请选择其他退货原因。 |
| 25001028 | reverse lock failed |
| 25001057 | reverse reason not match reason type |
| 25001058 | reverse downstream data load error |
| 25007006 | Order not found. |
| 25011011 | reverse status cannot reject application |
| 25020003 | decision not match reverse status |
| 25020004 | decision not match reverse type |
| 25020005 | 无权处理此订单 |
| 25020010 | Aftersales has been approved and cannot be rejected. |

