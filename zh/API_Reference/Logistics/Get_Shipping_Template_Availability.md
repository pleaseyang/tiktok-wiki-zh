# 获取运费模板可用性

# 路径：/logistics/202510/seller_templates
# 方法：[GET]
# 功能描述
获取卖家可用的运费模板，并返回模板不可用的原因。此 API 目前仅适用于 JP 和 UK 市场。

---


# 公共参数
公共参数详情请参考 [如何调用 TikTok Shop APIs - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 参数 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
# 请求体参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_attribute | object | N |  | 用于评估运费模板可用性的商品尺寸和重量。 |
| ^weight | object | N |  | 商品重量 |
| ^^weight | string | N | 10 | 商品重量 |
| ^^unit | int | N | 1 | 1:克 |
| 2:磅 |  |  |  |  |
| 3:盎司 |  |  |  |  |
| 4:千克 |  |  |  |  |
| ^dimension | object | N |  | 商品尺寸 |
| ^^length | string | N | 10 | 商品长度 |
| ^^width | string | N | 10 | 商品宽度 |
| ^^height | string | N | 10 | 商品高度 |
| ^^unit | int | N | 1 | 1: 厘米 |
| 2:英寸 |  |  |  |  |
| 3:英尺 |  |  |  |  |
| 4:毫米 |  |  |  |  |
| 5:米 |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/logistics/202510/seller_templates?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 参数描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^templates | []object |  | 为卖家店铺评估的运费模板可用性列表。 |
| ^^template_is_available | bool | false | 模板是否可用 |
| ^^template | object |  | 运费模板详情，包括模板 ID、名称、履约方以及是否为默认模板。 |
| ^^^template_name | string | test template | 模板名称 |
| ^^^template_id | string | 1234566 | 模板 ID |
| ^^^is_default | bool | false | 是否为默认模板 |
| ^^^template_party | int | 1 | 1 表示由平台模板配送 |
| 2 表示由卖家模板配送 |  |  |  |
| ^^service_unreachable_reason | []object |  | 运费模板不可用的原因，按物流服务分组。当模板可用时，此字段将被省略。 |
| ^^^service_id | string | 23241 | 物流服务 ID |
| ^^^filter_reason | []object |  | 此物流服务对模板不可用的原因。 |
| ^^^^filter_type | string | 9 | 1 表示长度过滤 |
| 2 表示宽度过滤 |  |  |  |
| 3 表示高度过滤 |  |  |  |
| 4 表示重量过滤 |  |  |  |
| 9 表示服务模式过滤 |  |  |  |
| 11 表示服务过滤 |  |  |  |
| ^^^^reason | string | Ship by seller is banned | 不可用的详细原因 |
|  |  |  |  |
# 响应示例
```json
{"code":0,"data":{"templates":[{"template_is_available":false,"template":{"template_name":"test template","template_id":"1234566","is_default":false,"template_party":1},"service_unreachable_reason":[{"service_id":"23241","filter_reason":[{"filter_type":"9","reason":"Ship by seller is banned"}]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码详情请参考 [如何调用 TikTok Shop APIs - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
