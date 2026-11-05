# 获取物流服务商

# Path: /logistics/202309/delivery_options/{delivery_option_id}/shipping_providers
# Method: [GET]
# 功能描述
返回指定配送选项可用的物流服务商。如果配送选项由 TikTok 履约，则请求返回错误，不返回任何物流服务商。

---


# 公共参数
公共参数详情请参考 [如何调用 TikTok Shop APIs - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 参数 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| delivery_option_id | string | Y | 6955034615128000261 | 配送选项 ID，以十进制整数字符串表示。 |
# 请求 Query 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| warehouse_region | string | N | ES | 仓库所在国家，表示发货国家。 |
| buyer_region | string | N | DE | 买家所在国家，表示配送的目的国家。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/logistics/202309/delivery_options/6955034615128000261/shipping_providers?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&warehouse_region=ES&buyer_region=DE
```

# 响应参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 参数描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^shipping_providers | []object |  | 指定配送选项可用的物流服务商列表。 |
| ^^id | string | 7117858858072016686 | 物流服务商 ID |
| ^^name | string | USPS | 物流服务商名称 |
# 响应示例
```json
{"code":0,"data":{"shipping_providers":[{"id":"7117858858072016686","name":"USPS"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码详情请参考 [如何调用 TikTok Shop APIs - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 21008116 | 指定配送选项没有订阅。 |
| 21008117 | 指定 delivery_option_id 的配送由 TikTok 履约。将不返回物流服务商。 |
