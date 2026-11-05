# 推荐全球分类

# Path: /product/202309/global_categories/recommend
# Method: [POST]
# 功能描述
Retrieve a recommended leaf category and its category hierarchy for a candidate global product based on its title, description, and images.
If you are syncing product catalogs from an external system to TikTok Shop, use this API to facilitate product classification.
**Note**: Double-byte characters (e.g. Chinese characters) are not supported in text fields such as descriptions and titles. If you include them, the API request will fail.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
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
| product_title | string | Y | Men's Fashion Sports Low Cut Cotton Breathable Ankle Short | 产品标题。 |
| 标题长度： |  |  |  |  |

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* MX:[1,300]
* Other regions: [25, 255]
   |
   description |string |N |
   Please check the measurements before purchase.
* M-Size
* XL-Size

![Image](https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627)
 |HTML 格式的产品描述。
**Note**:

* The content must conform to the [HTML syntax](https://html.spec.whatwg.org/). All HTML tags are accepted but to optimize display on the TikTok Shop product detail page, the system will automatically convert certain tags into alternative formats, such as rendering `<table>` tags as images.
* Max length: 10,000 characters.
* Image guidelines: You must use [TikTok Shop image URLs](6509df95defece02be598a22). Max 30 `<img>` tags, each under 4000px with `src`, `width`, and `height` attributes.

**Recommendations**:

* If you are syncing a pre-existing description from another platform, include the full HTML source description here.
* Provide a detailed description, ideally over 300 characters.
* Include 3-5 key selling points, each under 250 characters, with supporting images.
* Use 1600x1600 px for the image dimensions. |
   images |[]object |N | |Product images, including gallery images, images that appear in the description, product variant images.
   |
   ^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。从 [Upload Product Image API] 获取 URI(https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). |
   category_version |string |N |v1 |The category tree version to use for this product.
   Possible values based on region:
* US: `v2`, represents the 7-level category tree.
   **Important**: If the seller account contains an active US shop, you must pass `v2` when using this API.
* Other regions: `v1`, represents the 3-level category tree.
   Default: `v1` |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_categories/recommend?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"product_title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short","description":"\u003cp\u003ePlease check the measurements before purchase.\u003c/p\u003e\n\u003cul\u003e\n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" width='100' height='100' /\u003e \n ","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"category_version":"v1"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^leaf_category_id | string | 605254 | 推荐的分类 ID。这始终是叶子分类。 |
| ^categories | []object |  | 推荐叶子分类的分类层级，从顶级分类到叶子分类排序。 |
| ^^id | string | 605254 | 分类 ID。 |
| ^^name | string | Christmas Gifts | 分类名称。 |
| ^^level | int | 3 | 分类级别。 |
| ^^is_leaf | bool | true | 标识该分类是否为叶子分类的标志。 |
| **Note**: 您只能创建或编辑属于叶子分类的产品。 |  |  |  |
# 响应示例
```json
{"code":0,"data":{"leaf_category_id":"605254","categories":[{"id":"605254","name":"Christmas Gifts","level":3,"is_leaf":true}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019006 | product description is invalid |
| 12019009 | product image list is invalid |
| 12019064 | No matching categories. Provide the full name of your product, edit its product properties, and try again. |
| 12052013 | The product description cannot exceed maximum characters |
| 12052051 | The product name exceed max limit characters |
| 12052056 | The num of image in description cannot exceed max limit |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052261 | product name is empty |
| 12052262 | Chinese characters are not supported in product name |
| 12052266 | The product name contains non-English characters. |
| 12052301 | Width and length of main image must be at least &lbrace;&lbrace;min_limit&rbrace;&rbrace;, check uri &lbrace;&lbrace;uri&rbrace;&rbrace; |
| 12052305 | The main images aspect ratio cannot exceed max limit. |
| 12052306 | main product images count exceed limit |
| 12052340 | product description image uri illegal |
| 12052345 | The product description html tag not support. |
| 12052346 | The product description has Chinese characters |
| 12052348 | The product description html tag required attribute is miss. |
| 12052349 | The product description html tag not support nest. |
| 12052350 | The product description html tag contain illegal attribute. |
| 12052351 | The product description contains non-English characters. |
| 12052700 | The seller is inactive. |
| 12052704 | seller id not exist |
| 12052722 | The image URI does not exist in TikTok Shop. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052912 | No matching category found within your account's main category. Check your main category in the seller profile on Seller Center and ensure your product falls within its scope. |
| 12052931 | The title must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
| 12056001 | System error, try again later |

