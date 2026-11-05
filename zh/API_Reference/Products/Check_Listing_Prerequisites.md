# 检查上架前提条件

# Path: /product/202312/prerequisites
# Method: [GET]
# 功能描述
检查 TikTok 店铺是否准备好上架产品。
每个店铺在开始上架产品之前需要满足一系列 TikTok Shop 要求。在上架产品之前，使用此 API 检查您的店铺是否已满足所有要求。
**Tip**: We recommend that you run this check before any bulk updates to avoid listing issues. For example, sellers may change the delivery option to "Shipped by seller" but fail to add a shipping template, thus blocking the shop from listing products. In this case, the API would return `is_failed=true` for the `SHIPPING_TEMPLATE` check item and you can prompt the seller to fix the problem.

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
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202312/prerequisites?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^check_results | []object |  | A list of results from checking whether a shop satisfies TikTok Shop requirements. |
| ^^check_item | string | RETURN_WAREHOUSE | 店铺需要满足的要求。 |
| Possible values: |  |  |  |

* SHOP_STATUS
* SHOP_TAX
* PICKUP_WAREHOUSE
* RETURN_WAREHOUSE
* DELIVERY_OPTION
* SHIPPING_TEMPLATE
* PRODUCT_QUANTITY_LIMIT
* EXTENDED_PRODUCER_RESPONSIBILITY
* BANk_ACCOUNT
* CONTACT_INFO
   |
   ^^is_failed |bool |true |标识店铺是否未通过 `check_item`. |
   ^^fail_reasons |[]string |["Couldn't publish this product as you haven't set the return warehouse for your shop. Add the return warehouse information on TikTok Shop Seller Center first and try again."] |未通过特定 `check_item`. |

# 响应示例
```json
{"code":0,"data":{"check_results":[{"check_item":"RETURN_WAREHOUSE","is_failed":true,"fail_reasons":["Couldn't publish this product as you haven't set the return warehouse for your shop. Add the return warehouse information on TikTok Shop Seller Center first and try again."]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 33001002 | internal error |

