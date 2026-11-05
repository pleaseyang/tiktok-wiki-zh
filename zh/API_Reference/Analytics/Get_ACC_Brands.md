# 获取 ACC 品牌

# Path: /analytics/202610/acc/brands
# Method: [GET]
# 功能描述
获取当前店铺的授权 ACC 品牌及其关联行业。当记录包含两个 ID 时，将其 `brand_id` 和 `industry_id` 配对用于获取 ACC 受众概览。

---


# 公共参数
公共参数，请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/brands?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^brands | []object | [{"brand_id":"1000001","brand_logo_url":"https://example.com/images/demo-brand-logo.png","brand_name":"Demo Brand","industry_id":"9000001","industry_name":"Beauty \u0026 Personal Care","shop_id":"1000000000000000002","shop_name":"Demo Shop","ttms_id":"1000000000000000003"}] | 当前店铺的授权品牌和行业记录。返回所有记录，无分页，顺序不保证；空数组表示无授权记录。记录按品牌 ID 去重，并不枚举每个可能的品牌-行业关系。在其他 ACC 数据 API 中使用同一记录中的 brand_id 和 industry_id。 |
| ^^brand_id | string | 1000001 | 授权品牌的 ID。调用其他 ACC 数据 API 时，与同一记录中的 industry_id 一起使用。 |
| ^^brand_logo_url | string | https://example.com/images/demo-brand-logo.png | 授权品牌 logo 的 URL。 |
| ^^brand_name | string | Demo Brand | 授权品牌的名称。 |
| ^^industry_id | string | 9000001 | 与品牌关联的行业 ID。调用其他 ACC 数据 API 时，与同一记录中的 brand_id 一起使用。 |
| ^^industry_name | string | Beauty & Personal Care | 与品牌关联的行业名称。 |
| ^^shop_id | string | 1000000000000000002 | 此品牌授权应用的当前店铺 ID。这是一个只读的响应标识符；ACC 请求使用的店铺由授权店铺上下文确定。 |
| ^^shop_name | string | Demo Shop | 此品牌授权应用的当前店铺名称。 |
| ^^ttms_id | string | 1000000000000000003 | 与品牌关联的 TTMS 标识符。仅供参考返回；请勿将其作为业务参数传递给 ACC API。 |
# 响应示例
```json
{"code":0,"data":{"brands":[{"brand_id":"1000001","brand_logo_url":"https://example.com/images/demo-brand-logo.png","brand_name":"Demo Brand","industry_id":"9000001","industry_name":"Beauty \u0026 Personal Care","shop_id":"1000000000000000002","shop_name":"Demo Shop","ttms_id":"1000000000000000003"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

