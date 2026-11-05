# 检查运费模板是否存在

# Path: /logistics/202606/seller_template/template_exist
# Method: [GET]
# 功能描述
检查已认证的店铺是否为指定的业务仓库拥有运费模板。

---


# 公共参数
公共参数详情请参考 [如何调用 TikTok Shop APIs - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 参数 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您 app 的特定 key。 |
| access_token | string | Y | ROW_lueRwg4DEVhW7y9az74MgYA8y24seCBcjItc6CY8PGpsdgKZ4aOMGHKejG566H2mPj-jemiTXWkkZdnM5eTo11xqCRIZFihUe6VhBKKYzYsdjZDxg46ER8EffWnbeLBEjUUatmM4zpBIzyy_MPmJOdQh-Z54DX-A | 授权 Token，为所有符合条件的 TikTok Shop Partner 开发者提供。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| shop_id | int | N | 123 | 店铺 ID |
| biz_warehouse_id | int | Y | 456 | 业务仓库 ID |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/logistics/202606/seller_template/template_exist?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&shop_id=123&biz_warehouse_id=456
```

# 响应参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 参数描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^template_exist | bool | false | 如果模板存在，返回 true |
# 响应示例
```json
{"code":0,"data":{"template_exist":false},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码详情请参考 [如何调用 TikTok Shop APIs - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
