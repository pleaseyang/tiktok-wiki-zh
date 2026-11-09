# 诊断和优化商品

# 路径：/product/202411/products/diagnose_optimize
# 方法：[POST]
# 功能描述
诊断商品以获取有助于改进商品内容的信息，从而提升商品可见度和买家信任。返回的信息包括:

* 上架质量信息（仅适用于 US 市场）。
* 当前商品详情存在的问题及总体建议
* 针对特定商品字段自动生成的优化建议，包括标题、描述和图片。
   此接口可诊断在售商品（状态: `ACTIVATE`）以及尚未在 TikTok Shop 上架的全新商品。
* 要诊断**在售商品**，请提供 `product_id` 和 `category_id`，并将其他所有商品详情留空。
* 要诊断尚未在 TikTok Shop 上架的**全新商品**，请省略 `product_id` 并按需提供商品详情。
* 要诊断**与现有商品相似的商品**，请提供 `product_id` 和 `category_id` 以及任何新详情。诊断将结合现有商品的信息与您提供的新详情。例如，如果提供新的 `title`，诊断将使用新标题代替现有标题，同时保留该商品 ID 的其他值。
   **注意**：
* 要诊断多个在售商品，请使用 [Product Information Issue Diagnosis API](665048f380b6b302e73917d9)。
* 此接口仅专注于优化商品可见度，不评估商品是否满足上架要求。此接口识别出的质量问题不会阻止商品上架。要核验上架要求，请使用 [Check Product Listing API](650a0ee8f1fd3102b91c6493)。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | N | 1729592969712203232 | TikTok Shop 中已有商品的商品 ID。 |

* 如果要诊断尚未在 TikTok Shop 上架的全新商品，请省略此项。
* 如果商品与现有商品相似，且希望诊断同时考虑现有商品详情和本次请求中的新信息，请提供此 ID。 |
   category_id |string |Y |600001 |此商品的分类 ID。必须是叶子分类。 Use the [Get Categories API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) to find a leaf category。
   **注意**：
* 对于美国市场，商品类目限制信息请参阅 [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy)。
* 对于印度尼西亚市场，要在 TikTok Shop 和 Tokopedia 上架商品，您必须仅使用两个平台上都可用的分类。 |
   description |string |N |
   请在购买前检查尺寸。
* M-Size
* XL-Size

![Image](https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627)
 |HTML 格式的商品描述。 **注意**： - The content must conform to the [HTML syntax](https://html.spec.whatwg.org/). 所有 HTML 标签都被接受，但为了优化在 TikTok Shop 商品详情页上的展示，系统会自动将某些标签转换为替代格式，例如将 `` 标签渲染为图片。 - 最大长度：10,000 个字符。 - Images must use TikTok Shop image URLs, not exceed 4000px, and include `src`, `width`, and `height` attributes. **建议**： - If you are syncing a pre-existing description from another platform, include the full HTML source description here. - Provide a detailed description, ideally over 300 characters. - Include 3-5 key selling points, each under 250 characters, with supporting images. - Use 1600x1600 px for the image dimensions。 | brand_id |string |N |7082427311584347905 |此商品的品牌 ID。 Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) 获取店铺可用品牌列表。 **注意**： 未经授权的品牌不会在 TikTok Shop 上显示。 | main_images |[]object |N | | 要在商品图片库中展示的图片列表。请先使用 [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) 上传图片并获取对应的图片 URI。**说明**：- 图片 URI 数量上限：9 - 按应在 TikTok Shop 上出现的顺序排列图片 URI。- 图片尺寸：[300x300 px, 4000x4000 px] **建议**：- 至少使用 5 张图片。- 首张图片应使用白色背景。可使用 [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) 将背景改为白色。 | ^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。从 [Upload Product Image API] 获取 URI(https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) or the [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97)。 | title |string |N |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks |商品标题。 标题长度： - DE, ES, FR, IE, IT, JP, UK, US: [1, 255] - BR, MX: [1, 300] - Other regions: [25, 255] | product_attributes |[]object |N | |描述商品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。 **注意**： The attributes available for use are determined by the system based on the product's assigned category, with some being mandatory. Retrieve the product attributes by using the [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 | ^id |string |N |100392 |商品属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 | ^values |[]object |N | |商品属性的可选值列表。 **注意**： 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。 | ^^id |string |N |1001533 |内置商品属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 | ^^name |string |N |Birthday |如果内置值不满足需求，可自定义商品属性值。系统将在上架后自动生成 ID。 **注意**： - 同一属性下不允许重复。 - 最大长度：500 个字符 | size_chart |object |N | |商品的测量详情，帮助买家找到合适的尺码。 **注意**： - For certain product categories, size charts may be required or not supported. Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 检查要求。 - Provide either a TikTok Shop size chart template ID or a size chart image; if both are provided, the ID takes priority。 | ^template |object |N | |由卖家中心 > 管理商品 > 批量操作 > 批量管理尺码表中的尺码表工具生成的 TikTok Shop 尺码表模板。 | ^^id |string |N |7267563252536723205 |尺码表模板 ID。 | ^image |object |N | |尺码表的图片。 | ^^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |尺码表图片的 URI。 Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload the image first 并获取相应的图片 URI。 | optimization_fields |[]string |N |["ALL"] |要为其生成具体优化建议的字段。可选值：- TITLE：商品标题 - DESCRIPTION：商品描述（生成此项建议可能需要 10 秒以上）- IMAGE：图片库中展示的商品图片 - ALL：为上述所有字段生成建议 - NONE：不提供任何建议。默认值：NONE |
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

| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^listing_quality | object |  | 商品上架质量信息。 |
| ^^current_tier | string | POOR | 此商品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc。 |
可能的值：

* POOR
* FAIR
* GOOD

**注意**: 仅适用于美国市场。 |
^^remaining_recommendations |int |3 |为使商品晋级到最高层级仍需落实的建议数量（见 `diagnosis_results`）。
**注意**：

* 要晋级到最高层级，必须落实 `diagnosis_results` 中列出的所有建议。
* 仅适用于美国市场。 |
   ^diagnoses |[]object | |商品诊断与优化信息。 |
   ^^field |string |TITLE |被诊断的商品字段。
   可能的值：
* TITLE：商品标题
* DESCRIPTION：商品描述
* IMAGE：图片库中展示的商品图片
* ATTRIBUTE：商品属性
* SIZE_CHART：商品尺码表 |
   ^^diagnosis_results |[]object | |对指定字段进行诊断的结果。 |
   ^^^code |string |TITLE_LESS_THAN_40_CHARACTERS |代表已识别问题的机器可读代码。
   有关已识别问题的完整列表及相应建议，请参阅 [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd)。 |
   ^^^how_to_solve |string |Names must be at least 40 characters long and contain product-identifying information, such as "hiking boots" or "lipstick". |解决已识别问题的建议，以店铺的默认语言返回。
   有关建议的完整列表，请参阅 [Listing quality diagnosis]((https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd))。 |
   ^^^quality_tier |string |FAIR |通过实施建议可以达到的上架质量等级。
   可能的值：
* FAIR
* GOOD
   **注意**：
* 要达到更高层级，必须落实目标层级及之前所有层级的全部建议。例如，当所有 "FAIR" 和 "GOOD" 建议都得到处理或落实后，商品就会达到 "GOOD" 层级。
* 仅适用于美国市场。 |
   ^^suggestion |object | |由系统自动生成、用于提升指定字段效果的优化建议。

**注意**: 如果 `optimization_fields` 的值为空或 `NONE`，则不会返回此项。 |
^^^seo_words |[]object | |当 `diagnoses.field` 为 "TITLE" 时的 SEO 关键词建议。
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

