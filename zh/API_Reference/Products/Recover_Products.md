# 恢复产品

# Path: /product/202309/products/recover
# Method: [POST]
# 功能描述
Recover products that are in the `Deleted` status. The status changes to `Seller_deactivated` after recovery.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_ids | []string | Y | ["1729592969712207008"] | The product IDs to recover. |
| 最大 ID 数量：20. |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/recover?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":["1729592969712207008"]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | The errors for individual products that could not be recovered. Check this list even when the top-level `code` is `0`. |
| ^^code | int | 12052048 | 主要错误代码。 |
| ^^message | string | You can't edit other sellers' products | 主要错误消息。 |
| ^^detail | object |  | 主要错误的详细信息。 |
| ^^^product_id | string | 1729382588639839583 | The ID of the product that could not be recovered. |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":12052048,"message":"You can't edit other sellers' products","detail":{"product_id":"1729382588639839583"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019120 | The number of provided product IDs exceeds the limit. |
| 12052032 | The product does not exist |
| 12052048 | You cannot edit the specified product(s) as it isn't listed in your account or shop. |
| 12052332 | The seller center is locked during shop integration, only editing stock and price is allowed |
| 12052700 | The seller is inactive. |
| 12052703 | Invalid seller tax number |
| 12052705 | seller can not manage local product. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052901 | The product in its current status is not available for this operation. Change the product status and try again. |

