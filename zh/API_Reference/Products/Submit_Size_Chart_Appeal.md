# 提交尺码表申诉

# Path: /product/202604/appeals/submit
# Method: [POST]
# 功能描述
#### Appeal Size Chart Verification
Initiates an appeal process for a product that was blocked during the listing phase due to a size chart verification failure.
This API is used when a seller believes their product was incorrectly blocked by our automated size chart validation system. The validation checks for three potential issues:

1. Whether the size chart contains all mandatory dimensions.
2. Whether the size chart covers all Stock-Keeping Units (SKUs) for sale.
3. Whether the numerical values within the size chart are valid.
   If the validation system detects an issue, the product listing will be blocked. By using this API, sellers can submit an appeal. If the appeal is approved, the block will be lifted, and the seller can re-list the product.
   Use the `[Appeal Status Webhook]` to monitor the appeal's progress, or pass the `appeal_id` to the `[Get Appeal Status API]` to retrieve the current status.
   Note:
* Please wait at least 5 minutes after submitting an appeal before checking its status via the API to ensure the data is synchronized.
* You can submit up to 50 appeals per day. Any requests exceeding this limit will be rejected.


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
| product_id | int | Y | 1729532326804361713 | product_id |
| appeal_message | object | Y |  | Details of the products submitted for appeal |
| ^field_name | string | Y | APPEAL_MESSAGE_FIELD_SIZE_CHART | The target fields to appeal. |
| Possible values: |  |  |  |  |

* APPEAL_MESSAGE_FIELD_SIZE_CHART |
   ^indicator_details |[]object |Y | |Indicator details of the products submitted for appeal |
   ^^indicator_type |string |Y |CONTAINS_ALL_SALE_PROPERTY |The target indicator_type to appeal of this field.
   Possible values:
* REQUIRED_DIMENSION：Does the size chart include all required dimensions?
* CONTAINS_ALL_SALE_PROPERTY：Does the size chart cover all sales attributes?""
* VALUE_RANGE_OUT_OF_RANGE：Are the value ranges in the size chart valid? |
   ^size_chart_id |string |N |7597302357391361806 |size_chart_id |
   ^size_chart_image_uri |string |N |tos-alisg-i-aphluv4xwc-sg/ebf6d1b2204a4aa883abb0befb6fee50 |uri of size_chart_image |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/appeals/submit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_id":1729532326804361713,"appeal_message":{"field_name":"APPEAL_MESSAGE_FIELD_SIZE_CHART","indicator_details":[{"indicator_type":"CONTAINS_ALL_SALE_PROPERTY"}],"size_chart_id":"7597302357391361806","size_chart_image_uri":"tos-alisg-i-aphluv4xwc-sg/ebf6d1b2204a4aa883abb0befb6fee50"}}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
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
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

