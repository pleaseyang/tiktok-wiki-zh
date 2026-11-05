# 获取产品诊断结果

# Path: /product/202405/products/diagnoses
# Method: [GET]
# 功能描述
Diagnose multiple existing live (status: `ACTIVATE`) products to obtain information that helps you to improve the product content, enhancing product visibility and customer trust. The returned information includes:

* Listing quality information (available only for the US market).
* Issues with the current product details and the overall recommendations
* Auto-generated optimization suggestions targeted for specific product fields, including the title, description, and image.
   **Note**: This API focuses solely on optimizing product visibility and does not evaluate whether your product meets listing requirements. Quality issues identified by this API do not block your product from being listed. To verify listing requirements, use the [Check Product Listing API](650a0ee8f1fd3102b91c6493).


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
| product_ids | []string | Y | 12345678,123456 | The list of product IDs that you want to diagnose. |
**Note**:

* 最大 ID 数量：200
* The product must be live (status: `ACTIVATE`) |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202405/products/diagnoses?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&product_ids=12345678,123456
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | The list of requested products and the corresponding diagnosis results. |
| ^^id | string | 123456 | 产品 ID。 |
| ^^listing_quality | object |  | 产品上架质量信息。 |
| ^^^current_tier | string | POOR | 此产品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc. |
Possible values:

* POOR
* FAIR
* GOOD

**Note**: Available only for the US market. |
^^^remaining_recommendations |int |3 |The remaining number of recommendations (see `diagnosis_results`) that must be implemented for the product to reach the highest tier.
**Note**:

* To reach the highest tier, you must implement all recommendations listed in `diagnosis_results`.
* Available only for the US market. |
   ^^diagnoses |[]object | |Product diagnosis and optimization information. |
   ^^^field |string |TITLE |被诊断的产品字段。
   Possible values:
* TITLE: Product title
* DESCRIPTION: Product description
* IMAGE: Product image (`main_images` in the product entity)
* ATTRIBUTE: Product attribute
* SIZE_CHART: Product size chart |
   ^^^diagnosis_results |[]object | |The results of diagnosing the specified field. |
   ^^^^code |string |TITLE_LESS_THAN_40_CHARACTERS |代表已识别问题的机器可读代码。
   Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the full list of diagnosed issues and the corresponding recommendations. |
   ^^^^how_to_solve |string |Names must be at least 40 characters long and contain product-identifying information, such as "hiking boots" or "lipstick". |解决已识别问题的建议，以店铺的默认语言返回。
   Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the full list of recommendations. |
   ^^^^quality_tier |string |GOOD |通过实施建议可以达到的上架质量等级。
   Possible values:
* FAIR
* GOOD

**Note**:

* To reach a higher tier, you must implement all recommendations from the destination tier and all preceding tiers. For example, a product will reach the "GOOD" tier once all "FAIR" and "GOOD" recommendations are addressed or implemented.
* Available only for the US market. |
   ^^^suggestion |object | |Optimization suggestions that are auto-generated by the system to improve the effectiveness of the specified field. |
   ^^^^seo_words |[]object | |The SEO keyword suggestions for product titles. |
   ^^^^^text |string |dress |The suggested SEO keyword. |
   ^^^^smart_texts |[]object | |The list of optimized product title or description. |
   ^^^^^text |string |this is a good title |The optimized text. |
   ^^^^images |[]object | |Optimized image alternatives generated from the first image in the product's `main_images` set. |
   ^^^^^height |int |600 |优化后的图片高度。 |
   ^^^^^width |int |600 |优化后的图片宽度。 |
   ^^^^^uri |string |tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d |图片的原始 URI。 |
   ^^^^^url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp |图片的原始 URL。 |
   ^^^^^optimized_uri |string |tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6 |优化后图片的 URI。 |
   ^^^^^optimized_url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp |优化后图片的 URL。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"id":"123456","listing_quality":{"current_tier":"POOR","remaining_recommendations":3},"diagnoses":[{"field":"TITLE","diagnosis_results":[{"code":"TITLE_LESS_THAN_40_CHARACTERS","how_to_solve":"Names must be at least 40 characters long and contain product-identifying information, such as \"hiking boots\" or \"lipstick\".","quality_tier":"GOOD"}],"suggestion":{"seo_words":[{"text":"dress"}],"smart_texts":[{"text":"this is a good title"}],"images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp","optimized_uri":"tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6","optimized_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp"}]}}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12009014 | seller no permission for product error |
| 12019114 | Seller has no permission |
| 12019120 | The number of provided product IDs exceeds the limit. |
| 12052260 | The product ID does not exist |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

