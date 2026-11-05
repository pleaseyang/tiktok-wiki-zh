# 推荐分类

# Path: /product/202309/categories/recommend
# Method: [POST]
# 功能描述
根据候选产品的标题、描述和图片获取推荐的分类。
如果您正在将产品目录从外部系统同步到 TikTok Shop，请使用此 API 来促进产品分类。
**Note**: 描述和标题等文本字段中使用的语言必须与目标市场的语言一致（例如，不要使用中文）。

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
| category_version | string | N | v1 | 按分类树版本过滤分类。Possible values based on region: |

* US, EU and SEA: v2, represents the 7-level category tree.
   Important: For US, EU and SEA shops, you must pass v2 when using this API.
* Other regions: v1, represents the 3-level category tree.Default: v1 |
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
   images |[]object |N | |Product images, including gallery images, images that appear in the description, product variant images. |
   ^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。从 [Upload Product Image API] 获取 URI(https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). |
   include_prohibited_categories |bool |N |false |A flag to indicate whether to include matching categories that are prohibited on TikTok Shop. Set this to `true` to identify if the product falls under a category that you can't list on TikTok Shop in any circumstances.
   **Note**:
* Applicable only for BR and MX markets.
* Default: `false` |
   listing_platform |string |N |TIKTOK_SHOP |Recommend categories that belong to the specified platform.
   Possible values:
* TIKTOK_SHOP
* TOKOPEDIA
   Default: TIKTOK_SHOP

Applicable only for sellers that migrated from Tokopedia. |
locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。
Default: 您店铺的默认语言环境。
Possible values:

* `cs-CZ`
* `de-AT`
* `de-BE`
* `de-DE`
* `el-GR`
* `en-GB`
* `en-IE`
* `en-US`
* `es-ES`
* `es-MX`
* `fr-FR`
* `fr-BE`
* `hu-HU`
* `id-ID`
* `it-IT`
* `ja-JP`
* `ms-MY`
* `nl-NL`
* `nl-BE`
* `pl-PL`
* `pt-BR`
* `pt-PT`
* `th-TH`
* `vi-VN`
* `zh-CN` |
   origin_platform_product_type |string |N |Handbags |在源平台上定义的产品类型。 |
   origin_platform_vendor |string |N |Chanel |源平台上的产品供应商或品牌名称。 |
   origin_platform_tags |[]string |N |["blastcornhole","Shopify Collective"] |与源平台上产品关联的标签。 |
   origin_platform_category |object |N | |在源平台上分配给产品的分类信息。 |
   ^id |string |N |gid://shopify/TaxonomyCategory/na |源平台上的分类 ID。 |
   ^name |string |N |Uncategorized |源平台上的分类名称。 |
   ^full_name |string |N |Uncategorized |源平台上的完整分类路径或完整分类名称。 |
   ^is_leaf |bool |N |true |该分类是否为叶子分类。 |
   ^is_root |bool |N |true |该分类是否为根分类。 |
   origin_platform_product_meta_data |object |N | |源平台提供的额外产品元数据。 |
   ^attribute_value_list |[]object |N | |产品元数据属性及其值的列表。 |
   ^^name |string |N |mark_out_of_stock |元数据属性名称。 |
   ^^values |[]string |N |["true"] |与元数据属性关联的值。 |
   product_title |string |Y |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short |产品标题。
   标题长度：
* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* Other regions: [25, 255] |
   is_live_quick |bool |N |false |false — NORMAL products
   true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.
   Default: false |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/recommend?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"category_version":"v1","description":"\u003cp\u003ePlease check the measurements before purchase.\u003c/p\u003e\n\u003cul\u003e\n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" width='100' height='100' /\u003e","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"include_prohibited_categories":false,"listing_platform":"TIKTOK_SHOP","locale":"en-US","origin_platform_product_type":"Handbags","origin_platform_vendor":"Chanel","origin_platform_tags":["blastcornhole","Shopify Collective"],"origin_platform_category":{"id":"gid://shopify/TaxonomyCategory/na","name":"Uncategorized","full_name":"Uncategorized","is_leaf":true,"is_root":true},"origin_platform_product_meta_data":{"attribute_value_list":[{"name":"mark_out_of_stock","values":["true"]}]},"product_title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short","is_live_quick":false}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^categories | []object |  | 推荐叶子分类的分类层级，从顶级分类到叶子分类排序。 |
| ^^id | string | 605254 | 分类 ID。 |
| ^^is_leaf | bool | true | 标识该分类是否为叶子分类的标志。 |
**Note**: 您只能创建或编辑属于叶子分类的产品。 |
^^level |int |1 |分类级别。 |
^^name |string |Teas |分类名称。 |
^^permission_statuses |[]string |["INVITE_ONLY"] |该店铺的此分类权限状态。
Possible values:

* AVAILABLE: You have the permission to create products in this category.
* INVITE_ONLY: This is a restricted category and you do not have permission to use it. Submit an application through the Qualification Center on TikTok Shop Seller Center to gain access. In Seller Center, `INVITE_ONLY` is also known as "restricted".
* NON_MAIN_CATEGORY: This category is not in the shop's main category.
* PROHIBITED: This category is prohibited on TikTok Shop. If your product falls under this category, do not attempt to list it, as it will be rejected during audit. Applicable only for BR and MX markets. |
   ^leaf_category_id |string |605254 |推荐的分类 ID。这始终是叶子分类。 |

# 响应示例
```json
{"code":0,"data":{"categories":[{"id":"605254","is_leaf":true,"level":1,"name":"Teas","permission_statuses":["INVITE_ONLY"]}],"leaf_category_id":"605254"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
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
| 12052300 | product main image uri illegal |
| 12052301 | Width and length of main image must be at least &lbrace;&lbrace;min_limit&rbrace;&rbrace;, check uri &lbrace;&lbrace;uri&rbrace;&rbrace; |
| 12052305 | The main images aspect ratio cannot exceed max limit. |
| 12052306 | main product images count exceed limit |
| 12052340 | product description image uri illegal |
| 12052341 | The description images size cannot exceed limit. |
| 12052343 | Product description image format not support. |
| 12052345 | The product description html tag not support. |
| 12052346 | The product description has Chinese characters |
| 12052348 | The product description html tag required attribute is miss. |
| 12052349 | The product description html tag not support nest. |
| 12052350 | The product description html tag contain illegal attribute. |
| 12052351 | The product description contains non-English characters. |
| 12052352 | The product description nest exceeding limit |
| 12052700 | The seller is inactive. |
| 12052704 | seller id not exist |
| 12052722 | The image URI does not exist in TikTok Shop. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052912 | No matching category found within your account's main category. Check your main category in the seller profile on Seller Center and ensure your product falls within its scope. |
| 12052931 | The title must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |

