# 激活产品

# Path: /product/202309/products/activate
# Method: [POST]
# 功能描述
激活处于 `Seller_deactivated` 或 `Platform_deactivated` 状态的隐藏产品，并在 TikTok Shop 目录中展示它们。
提交激活请求后，产品将被发送到 TikTok Shop 进行审核，其状态将变为 `Pending`。如果产品通过审核，其状态将变回 `Activate`。您可以使用[产品状态变更 webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) 来监控审核状态。

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
| product_ids | []string | Y | ["1729592969712207008", "1729592969712207021"] | 要激活的产品 ID。 |
| 最大 ID 数量：20 |  |  |  |  |
| listing_platforms | []string | N | ["TIKTOK_SHOP"] | 产品将被激活的上架平台。 |
| Possible values: |  |  |  |  |

* TOKOPEDIA
* TIKTOK_SHOP
   Default: TIKTOK_SHOP

Applicable only for sellers that migrated from Tokopedia. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/activate?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":["1729592969712207008","1729592969712207021"],"listing_platforms":["TIKTOK_SHOP"]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 无法激活的单个产品的错误。即使顶级 `code` is `0`. |
| ^^code | int | 12052990 | 主要错误代码。 |
| ^^message | string | Batch activate business error. | 主要错误消息。 |
| ^^detail | object |  | 主要错误的详细信息。 |
| ^^^product_id | string | 1729382588639839583 | 无法激活的产品 ID。 |
| ^^^extra_errors | []object |  | 与主要错误相关的进一步嵌套错误或问题列表。 |
| ^^^^code | int | 12052048 | 次要错误代码。 |
| ^^^^message | string | You can't edit other sellers' products | 次要错误消息。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":12052990,"message":"Batch activate business error.","detail":{"product_id":"1729382588639839583","extra_errors":[{"code":12052048,"message":"You can't edit other sellers' products"}]}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019022 | SKU must contain a valid warehouse. |
| 12019120 | The number of provided product IDs exceeds the limit. |
| 12052048 | You cannot edit the specified product(s) as it isn't listed in your account or shop. |
| 12052093 | Exceeded the product listing limit for the seller. |
| 12052330 | product is not supported to list in designated sale platform |
| 12052332 | The seller center is locked during shop integration, only editing stock and price is allowed |
| 12052700 | The seller is inactive. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052901 | The product in its current status is not available for this operation. Change the product status and try again. |
| 12052910 | Invalid input parameters. Refer to the API documentation for details. |
| 12052990 | The check failed. |

