# 诊断和优化产品

# Path: /product/202411/products/diagnose_optimize
# Method: [POST]
# 功能描述
Diagnose products to obtain information that helps you to improve the product content, enhancing product visibility and customer trust. The returned information includes:

* Listing quality information (available only for the US market).
* Issues with the current product details and the overall recommendations
* Auto-generated optimization suggestions targeted for specific product fields, including the title, description, and image.
   This API enables you to diagnose both live products (status: `ACTIVATE`) and brand-new products not yet listed in TikTok Shop.
* To diagnose a **live product**, provide the `product_id` and `category_id` and leave all other product details blank.
* To diagnose a **brand-new product** not yet listed in TikTok Shop, omit the `product_id` and provide the product details as necessary.
* To diagnose a **product similar to an existing one**, provide the `product_id` and `category_id`, along with any new details. The diagnosis will combine the existing product's information with the new details you provide. For example, if you provide a new `title`, the diagnosis will use the new title instead of the existing one while keeping the other values from the product ID.
   **Note**:
* To diagnose multiple live products, use the [Product Information Issue Diagnosis API](665048f380b6b302e73917d9).
* This API focuses solely on optimizing product visibility and does not evaluate whether your product meets listing requirements. Quality issues identified by this API do not block your product from being listed. To verify listing requirements, use the [Check Product Listing API](650a0ee8f1fd3102b91c6493).


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
| product_id | string | N | 1729592969712203232 | The product ID of an existing product in TikTok Shop. |

* Omit this if you are diagnosing a brand-new product not yet listed in TikTok Shop.
* Provide this ID if the product is similar to an existing one, and you want the diagnosis to consider both the existing product's details and the new information in this request. |
   category_id |string |Y |600001 |此产品的分类 ID。必须是叶子分类。 Use the [Get Categories API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) to find a leaf category.
   **Note**:
* For the US market, refer to [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on product category restrictions.
* For the Indonesia market, to list a product on both TikTok Shop and Tokopedia, you must use only categories that are available on both platforms. |
   description |string |N |
   Please check the measurements before purchase.
* M-Size
* XL-Size

![Image](https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627)
 |HTML 格式的产品描述。 **Note**: - The content must conform to the [HTML syntax](https://html.spec.whatwg.org/). All HTML tags are accepted but to optimize display on the TikTok Shop product detail page, the system will automatically convert certain tags into alternative formats, such as rendering `` tags as images. - Max length: 10,000 characters. - Images must use TikTok Shop image URLs, not exceed 4000px, and include `src`, `width`, and `height` attributes. **Recommendations**: - If you are syncing a pre-existing description from another platform, include the full HTML source description here. - Provide a detailed description, ideally over 300 characters. - Include 3-5 key selling points, each under 250 characters, with supporting images. - Use 1600x1600 px for the image dimensions. | brand_id |string |N |7082427311584347905 |此产品的品牌 ID。 Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) to get the list of available brands for a shop. **Note**: Unauthorized brands won't be displayed on TikTok Shop. | main_images |[]object |N | | A list of images to display in the product image gallery. Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload the images first and obtain the corresponding image URI. **Note**: - Max number of image URIs: 9 - Arrange your image URIs in the sequence that they should appear on TikTok Shop. - Image dimensions: [300x300 px, 4000x4000 px] **Recommendations**: - Use a minimum of 5 images. - The first image should have a white background. Use the [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) to change the background to white. | ^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。从 [Upload Product Image API] 获取 URI(https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) or the [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97). | title |string |N |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks |产品标题。 标题长度： - DE, ES, FR, IE, IT, JP, UK, US: [1, 255] - BR, MX: [1, 300] - Other regions: [25, 255] | product_attributes |[]object |N | |描述产品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。 **Note**: The attributes available for use are determined by the system based on the product's assigned category, with some being mandatory. Retrieve the product attributes by using the [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). | ^id |string |N |100392 |产品属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). | ^values |[]object |N | |产品属性的可选值列表。 **Note**: Provide either a built-in ID or a custom name; if both are provided, the ID takes priority. | ^^id |string |N |1001533 |内置产品属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). | ^^name |string |N |Birthday |如果内置值不满足需求，可自定义产品属性值。系统将在上架后自动生成 ID。 **Note**: - 同一属性下不允许重复。 - Max length: 500 characters | size_chart |object |N | |产品的测量详情，帮助买家找到合适的尺码。 **Note**: - For certain product categories, size charts may be required or not supported. Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to check the requirements. - Provide either a TikTok Shop size chart template ID or a size chart image; if both are provided, the ID takes priority. | ^template |object |N | |A TikTok Shop size chart template generated by the size chart tool in Seller Center > Manage Products > Bulk action > Batch manage size charts. | ^^id |string |N |7267563252536723205 |尺码表模板 ID。 | ^image |object |N | |尺码表的图片。 | ^^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |尺码表图片的 URI。 Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload the image first and obtain the corresponding image URI. | optimization_fields |[]string |N |["ALL"] |The fields for which you want to generate specific optimization suggestions. Possible values: - TITLE: Product title - DESCRIPTION: Product description (suggestions for this may take more than 10 seconds to generate) - IMAGE: Product image displayed in the image gallery - ALL: Suggestions are generated for all the above fields - NONE: No suggestions will be provided. Default: NONE |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202411/products/diagnose_optimize?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_id":"1729592969712203232","category_id":"600001","description":"\u003cp\u003ePlease check the measurements before purchase.\u003c/p\u003e\n\u003cul\u003e\n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" width='100' height='100' /\u003e ","brand_id":"7082427311584347905","main_images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks","product_attributes":[{"id":"100392","values":[{"id":"1001533","name":"Birthday"}]}],"size_chart":{"template":{"id":"7267563252536723205"},"image":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe\n"}},"optimization_fields":["ALL"]}
```

# 响应参数

| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^listing_quality | object |  | 产品上架质量信息。 |
| ^^current_tier | string | POOR | 此产品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc. |
Possible values:

* POOR
* FAIR
* GOOD

**NOTE**: Available only for the US market. |
^^remaining_recommendations |int |3 |The remaining number of recommendations (see `diagnosis_results`) that must be implemented for the product to advance to the highest tier.
**Note**:

* To advance to the highest tier, you must implement all recommendations listed in `diagnosis_results`.
* Available only for the US market. |
   ^diagnoses |[]object | |Product diagnosis and optimization information. |
   ^^field |string |TITLE |被诊断的产品字段。
   Possible values:
* TITLE: Product title
* DESCRIPTION: Product description
* IMAGE: Product image displayed in the image gallery
* ATTRIBUTE: Product attribute
* SIZE_CHART: Product size chart |
   ^^diagnosis_results |[]object | |The results of diagnosing the specified field. |
   ^^^code |string |TITLE_LESS_THAN_40_CHARACTERS |代表已识别问题的机器可读代码。
   Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the full list of identified issues and the corresponding recommendations. |
   ^^^how_to_solve |string |Names must be at least 40 characters long and contain product-identifying information, such as "hiking boots" or "lipstick". |解决已识别问题的建议，以店铺的默认语言返回。
   Refer to [Listing quality diagnosis]((https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd)) for the full list of recommendations. |
   ^^^quality_tier |string |FAIR |通过实施建议可以达到的上架质量等级。
   Possible values:
* FAIR
* GOOD
   **Note**:
* To reach a higher tier, you must implement all recommendations from the destination tier and all preceding tiers. For example, a product will reach the "GOOD" tier once all "FAIR" and "GOOD" recommendations are addressed or implemented.
* Available only for the US market. |
   ^^suggestion |object | |Optimization suggestions that are auto-generated by the system to improve the effectiveness of the specified field.

**Note**: This will not be returned if the value for `optimization_fields` is blank or `NONE`. |
^^^seo_words |[]object | |The SEO keyword suggestions if `diagnoses.field` is "TITLE".
|
^^^^text |string |dress |建议的 SEO 关键词文本。
|
^^^smart_texts |[]object | |标题和描述的智能文本建议。
|
^^^^text |string |this is a good title |建议的智能文本。
|
^^^images |[]object | |优化后的主图。仅优化主图组中的第一张图片。
|
^^^^height |int |600 |优化后的图片高度。
|
^^^^width |int |600 |优化后的图片宽度。
|
^^^^uri |string |tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d |图片的原始 URI。
|
^^^^url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp |图片的原始 URL。
|
^^^^optimized_uri |string |tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6 |优化后图片的 URI。
|
^^^^optimized_url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp |优化后图片的 URL。
|
# 响应示例
```json
{"code":0,"data":{"listing_quality":{"current_tier":"POOR","remaining_recommendations":3},"diagnoses":[{"field":"TITLE","diagnosis_results":[{"code":"TITLE_LESS_THAN_40_CHARACTERS","how_to_solve":"Names must be at least 40 characters long and contain product-identifying information, such as \"hiking boots\" or \"lipstick\".","quality_tier":"FAIR"}],"suggestion":{"seo_words":[{"text":"dress"}],"smart_texts":[{"text":"this is a good title"}],"images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp","optimized_uri":"tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6","optimized_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp"}]}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

