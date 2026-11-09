# 推荐分类

# 路径：/product/202309/categories/recommend
# 方法：[POST]
# 功能描述
根据候选商品的标题、描述和图片获取推荐的分类。
如果您正在将商品目录从外部系统同步到 TikTok Shop，请使用此 API 来促进商品分类。
**注意**： 描述和标题等文本字段中使用的语言必须与目标市场的语言一致（例如，不要使用中文）。

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
| category_version | string | N | v1 | 按分类树版本过滤分类。基于地区的可能值： |

* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |
   description |string |N |
   请在购买前检查尺寸。
* M-Size
* XL-Size

![Image](https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627)
 |HTML 格式的产品描述。
**注意**：

* 内容必须符合 [HTML 语法](https://html.spec.whatwg.org/)。系统接受所有 HTML 标签，但为优化在 TikTok Shop 商品详情页上的展示，会自动将某些标签转换为其他格式，例如将 `<table>` 标签渲染为图片。
* 最大长度：10,000 个字符。
* 图片规范：必须使用 [TikTok Shop image URLs](6509df95defece02be598a22)。最多 30 个 `<img>` 标签，每个小于 4000px，并带 `src`、`width` 和 `height` 属性。

**建议**：

* 如果您正在从其他平台同步预先存在的描述，请在此处包含完整的 HTML 源代码描述。
* 提供详细描述，最好超过 300 个字符。
* 包含 3-5 个关键卖点，每个不超过 250 个字符，并附带支持图片。
* 图片尺寸使用 1600x1600 像素。 |
   images |[]object |N | |商品图片，包括图库图片、描述中出现的图片、商品变体图片。 |
   ^uri |string |N |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。从 [Upload Product Image API] 获取 URI(https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22)。 |
   include_prohibited_categories |bool |N |false |用于指示是否包含在 TikTok Shop 上禁售的匹配类目的标志。将此设置为 `true` 可识别该商品是否属于在任何情况下都无法在 TikTok Shop 上架的类目。
   **注意**：
* 仅适用于 BR 和 MX 市场。
* Default: `false` |
   listing_platform |string |N |TIKTOK_SHOP |推荐属于指定平台的类目。
   可能的值：
* TIKTOK_SHOP
* TOKOPEDIA
   默认值：TIKTOK_SHOP

仅适用于从 Tokopedia 迁移的卖家。 |
locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。
Default: 您店铺的默认语言环境。
可能的值：

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
   origin_platform_product_type |string |N |Handbags |在源平台上定义的商品类型。 |
   origin_platform_vendor |string |N |Chanel |源平台上的商品供应商或品牌名称。 |
   origin_platform_tags |[]string |N |["blastcornhole","Shopify Collective"] |与源平台上商品关联的标签。 |
   origin_platform_category |object |N | |在源平台上分配给商品的分类信息。 |
   ^id |string |N |gid://shopify/TaxonomyCategory/na |源平台上的分类 ID。 |
   ^name |string |N |Uncategorized |源平台上的分类名称。 |
   ^full_name |string |N |Uncategorized |源平台上的完整分类路径或完整分类名称。 |
   ^is_leaf |bool |N |true |该分类是否为叶子分类。 |
   ^is_root |bool |N |true |该分类是否为根分类。 |
   origin_platform_product_meta_data |object |N | |源平台提供的额外商品元数据。 |
   ^attribute_value_list |[]object |N | |商品元数据属性及其值的列表。 |
   ^^name |string |N |mark_out_of_stock |元数据属性名称。 |
   ^^values |[]string |N |["true"] |与元数据属性关联的值。 |
   product_title |string |Y |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short |商品标题。
   标题长度：
* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* 其他地区: [25, 255] |
   is_live_quick |bool |N |false |false — 常规商品
   true — LIVE_QUICK 商品。只有具有所需权限的卖家才能创建 LIVE_QUICK 商品。
   默认值：false |

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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^categories | []object |  | 推荐叶子分类的分类层级，从顶级分类到叶子分类排序。 |
| ^^id | string | 605254 | 分类 ID。 |
| ^^is_leaf | bool | true | 标识该分类是否为叶子分类的标志。 |
**注意**： 您只能创建或编辑属于叶子分类的商品。 |
^^level |int |1 |分类级别。 |
^^name |string |Teas |分类名称。 |
^^permission_statuses |[]string |["INVITE_ONLY"] |该店铺的此分类权限状态。
可能的值：

* AVAILABLE: 您有权在该类目下创建商品。
* INVITE_ONLY: 这是一个受限类目，你没有使用权限。请通过 TikTok Shop Seller Center 上的 Qualification Center 提交申请以获得访问权限。在 Seller Center 中，`INVITE_ONLY` 也称为 "restricted"。
* NON_MAIN_CATEGORY: 该类目不在店铺的主类目中。
* PROHIBITED：该类目在 TikTok Shop 上被禁止。如果您的商品属于此类目，请勿尝试上架，因为它将在审核中被拒绝。仅适用于 BR 和 MX 市场。 |
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
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
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
| 12052700 | 卖家不活跃。 |
| 12052704 | 卖家 ID 不存在 |
| 12052722 | The image URI does not exist in TikTok Shop. |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052912 | No matching category found within your account's main category. Check your main category in the seller profile on Seller Center and ensure your product falls within its scope. |
| 12052931 | 标题必须遵循以下格式规则: 不能包含 HTML 转义字符 (e.g., )、表情符号或 ASCII 控制字符 (e.g., \u007F). 也不能仅由符号组成 (e.g., //// or !@#$$$&), 且连续重复字符不能超过 9 个 (e.g., aaaaaaaaa or 111111111)。 |

