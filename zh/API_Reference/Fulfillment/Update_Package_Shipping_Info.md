# 更新包裹物流信息

# 路径：/fulfillment/202610/packages/{package_id}/shipping_info/update
# 方法：[POST]
# 功能描述
如果卖家输入了错误的运单号，此接口允许卖家更新已发货包裹的运单号和物流服务商。注意: 此接口仅适用于卖家自行发货的订单（或包裹）。仅用于更新已发货包裹的运单号和物流服务商。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时，如果未传递正确的值，将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| package_id | string | Y | 5433567853345 | TikTok Shop 包裹 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| shipping_info_list | []object | Y |  | "仅支持在 3PL 单品场景（非虚拟捆绑）的分拆发货中上传多个运单号（此功能仅支持白名单卖家；如果您不在允许名单中，建议联系 AM 申请） |
| 其他场景下，一次只能上传一个运单号。" |  |  |  |  |
| ^tracking_number | string | N | 6617675021119438849 | Tracking number. |
| ^shipping_provider_id | string | N | 12312312321323432 | 使用 Get Shipping Provider API 获取各配送服务商的 shipping_provider_id。 |
| ^note | string | N | 这是一个表格 | "仅对部分白名单卖家可用。这适用于大件单品需要分多个包裹发货的场景。不在白名单内的卖家上传该字段，平台将自动忽略。 |
| 例如，包裹 1 标记为 ""headboard""，包裹 2 标记为 ""bed frame""。 |  |  |  |  |
| 此字段将展示给买家，请谨慎填写。" |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202610/packages/5433567853345/shipping_info/update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"shipping_info_list":[{"tracking_number":"6617675021119438849","shipping_provider_id":"12312312321323432","note":"this is a table"}]}
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
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10007002 | Current order is not a merchant blind box order. |
| 21001028 | The order is being processed. Try again later. |
| 21011001 | Package not found. If the error persists, please contact the platform for assistance. |
| 21011004 | 此接口不能用于更新非卖家发货包裹的配送信息。 |
| 21011007 | Package item has after-sale request, please process the after-sale request first. |
| 21011022 | Invalid tracking number or provider ID. Please double check and try again. |
| 21011028 | The package does not belong to the current shop. Please ensure you are providing the correct package ID and/or shop cipher. |
| 21011030 | fulfillment not allow update tracking no |
| 21011042 | Cannot complete the operation when order is cancelled. |
| 21011043 | The package has not been shipped yet. |
| 21011049 | Due to platform rule limitations, you are unable to update the tracking number. |
| 21011050 | The tracking number can only be updated within a certain number of hours. |
| 21011051 | The tracking number can only be updated once. |
| 21011052 | The tracking number can only be updated a limited number of times. |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 25001010 | A return request has already been completed, or the order has already been cancelled. |

