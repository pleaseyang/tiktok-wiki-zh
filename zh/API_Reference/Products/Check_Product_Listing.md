# 检查商品上架

# 路径：/product/202309/products/listing_check
# 方法：[POST]
# 功能描述
提前识别商品属性的任何问题，确保您的商品准备好上架。
每个商品在上架前必须满足 TikTok Shop 的要求。在上架之前，您可以将所有相关商品信息提交到此 API，以检查上架是否满足这些要求。您将收到一个需要在上架前解决的问题列表。此过程有助于降低创建商品时失败的风险。
**注意**：

* 商品内容中使用的语言必须与目标市场的语言一致（例如，不要使用中文），否则上架将失败或被拒绝。


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
| is_diagnosis_required | bool | N | true | (**已废弃**：此字段已废弃，将在未来的 API 版本中移除。请改用 [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API 获取与上架质量相关的信息。) |
| 用于指示是否返回商品的上架质量信息（仅限美国）和优化诊断结果的标志。如果设置为 `false`，响应体将不包含 `listing_quality` 和 `diagnoses` 对象。 |  |  |  |  |
| 默认值：true |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| description | string | N | 购买前请将上述详细尺码与您的测量尺寸进行比较。 |  |

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
   category_id |string |Y |600001 |此商品的叶子分类 ID。 Use the [Get Categories API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) 获取可用分类。

**注意**：

* 有关商品分类限制的信息，请参考 TikTok Shop Academy。
* 对于 US 市场，如果您要在 `INVITE_ONLY` 类目下创建商品，必须通过 TikTok Shop Seller Center 上的 Qualification Center 单独提交申请以获得权限。否则，即使商品审核通过，商品也不会上架并对买家可见。（商品状态将为 `PENDING`，审核状态将为 `PRE_APPROVED`）
* 对于印度尼西亚市场，要在 TikTok Shop 和 Tokopedia 上架商品，您必须仅使用两个平台上都可用的分类。 |
   brand_id |string |N |7082427311584347905 |此商品的品牌 ID。
   Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) 获取店铺可用品牌列表。
   **注意**： 未经授权的品牌不会在 TikTok Shop 上显示。 |
   main_images |[]object |Y | |在商品图片库中展示的图片列表。
* 最大数量：9
* 按图片在 TikTok Shop 上的展示顺序排列图片 URI。
* 图片尺寸：[300x300 像素，4000x4000 像素]

**建议**：

* 至少使用 5 张图片。
* 第一张图片应有白色背景。 Use the [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) 将背景更改为白色。 |
   ^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
   通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=MAIN_IMAGE` 获取此 URI。您可以直接使用返回的 URI，或先通过 [Optimize Images API](665692b35d39dc02deb49a97) 处理后再使用生成的 URI。 |
   skus |[]object |Y | |用于标识商品不同变体的 SKU（库存单位）列表。

**注意**：

* BR、EU、JP、MX、UK、US 的最大 SKU 数量：300
* 其他地区的最大 SKU 数量：100

**建议**：将最重要的变体放在数组开头。 |
^sales_attributes |[]object |N | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。
**注意**：

* 如果只有 1 个 SKU，则可以省略此对象。否则为**必填**。
* 每个商品最多只能有 3 种销售属性类型。
* 每个 SKU 必须包含相同数量和类型的销售属性。 例如，不能一个 SKU 只有颜色属性，而另一个 SKU 同时有颜色和尺码属性。
* 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。
* `id/name` 与 `value_id/value_name` 组合在每个 SKU 中必须唯一。例如，不能在不同 SKU 中重复 `"name": "Color"`、`"value_name": "Red"`。 |
   ^^id |string |N |100089 |内置销售属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。
   |
   ^^name |string |N |Specification |当内置属性不满足需求时，用于验证的自定义销售属性名称。

**注意**：

* 不要包含敏感字符。
* 最大长度：20 个字符 |
   ^^value_id |string |N |1729592969712207000 |内置销售属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 |
   ^^value_name |string |N |XL |当内置值不满足需求时，用于验证的自定义销售属性值。

**注意**：

* 同一属性下不允许重复。
* 最大长度：50 个字符。 |
   ^^sku_img |object |N | |主要销售属性（如颜色）每个值（如红色）的默认/主图片。此图片显示在 TikTok Shop 的商品选项库中。

您只能为 1 种销售属性附加图片，该属性将作为展示的主属性。必须为主属性的每个取值提供图片。例如，如果某商品有 2 种颜色和 3 种尺码，您可以选择为颜色销售属性或尺码销售属性附加图片。如果选择为颜色附加图片，则必须附加 2 张图片，每种颜色各 1 张。如需添加更多图片，请使用 `supplementary_sku_images`。 |
^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=ATTRIBUTE_IMAGE` 获取此 URI。 |
^^supplementary_sku_images |[]object |N | |主要销售属性（如颜色）每个值（如红色）的补充图片列表，用于提供该商品属性值的多角度视图或详情。这些图片显示在 TikTok Shop 的商品选项库中。
**注意**：

* 最大图片 URI 数量：8。
* 按图片在 TikTok Shop 上的展示顺序排列图片 URI。
* 仅适用于美国市场。 |
   ^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
   通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=ATTRIBUTE_IMAGE` 获取此 URI。 |
   ^seller_sku |string |N |Color-Red-XM01 |用于管理 SKU 的内部代码/名称，对买家不可见。
   有效长度：
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 个字符
* 其他地区: 1-50 个字符
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 仅使用字母、数字、连字符 (-) 或下划线 (_)
* 其他地区: 不含空格的文本 |
   ^price |object |Y | |SKU 定价信息。 |
   ^^amount |string |N |1.23 |**本地卖家/欧盟内部卖家**
   SKU 在商品页面上折扣前显示的**本地展示价格**。 Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。 |
   ^^currency |string |Y |USD |货币。基于地区的可能值：
* BRL: 巴西
* CZK: 捷克共和国
* EUR: 法国、德国、爱尔兰、意大利、西班牙、荷兰、比利时、奥地利、希腊、葡萄牙
* GBP: 英国
* HUF: 匈牙利
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* PLN: 波兰
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^sale_price |string |N |1.21 |**全球卖家**
   SKU 在商品页面上折扣前显示的**本地展示价格**。
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

**注意**：

* 仅适用于全球卖家。
* 对于使用中国仓库的 JP 和 US 店铺为必填，其他为可选。
* 这是商品页面上显示的最终确定价格，所有其他价格将被忽略。 |
   ^^starting_bid_price |string |N |2.3 |拍卖商品的起始竞价 |
   ^external_sku_id |string |N |1729592969712207012 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联 SKU。
   最大长度：999 个字符 |
   ^identifier_code |object |N | |根据国际标准化法规（如 GTIN）分配给商品的受管标识码，以确保商品在各种平台和系统中可普遍识别。 |
   ^^code |string |N |10000000000000 |标识码。

**Format**:

* GTIN: 14 位数字
* EAN: 8、13 或 14 位数字
* UPC: 12 位数字
* ISBN：13 位数字，或以大写 `X` 结尾的 9 位数字
* JAN: 8 或 13 位数字
   **注意**：标识码必须在每个 SKU 中唯一，不允许重复。 |
   ^^type |string |N |GTIN |标识码类型。
   可能的值：
* GTIN
* EAN
* UPC
* ISBN
* JAN |
   ^inventory |[]object |Y | |SKU 库存信息。
   |
   ^^warehouse_id |string |Y |7068517275539719942 |SKU 存放仓库的 ID。
   从以下位置获取您的店铺可用仓库列表 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6)。 |
   ^^quantity |int |N |999 |仓库中可用的 SKU 总数量。
   有效范围：[1, 99,999]

注意：此数量特指可以立即发货的有库存的库存量。 |
^^backorder_quantity |int |N |888 |一旦现货库存售罄，`backorder_quantity` 将自动转换为 `quantity`。此库存的履约遵循下文指定的 `handling_time`。
**注意**：

* 对于非虚拟商品类目，请同时提供 `backorder_quantity` 和 `handling_time`。
* 按单生产（MTO）、预售和定制商品不能缺货订购，且与 `backorder_quantity` 不兼容。 |
   ^^handling_time |int |N |5 |The estimated number of working days needed for a backorder to be shipped. For non-virtual product categories, provide `handling_time` and `backorder_quantity` together. All warehouses for the same SKU must use the same `handling_time`. |
   ^combined_skus |[]object |N | |如果此 SKU 属于虚拟套装，此对象包含组成套装的单个 SKU 列表（如礼品篮、入门套装）。 |
   ^^product_id |string |Y |1729582718312380123 |虚拟套装中包含的源商品 ID。 |
   ^^sku_id |string |Y |1729582718312380123 |虚拟套装中包含的源 SKU ID。 |
   ^^sku_count |int |Y |11 |虚拟套装中包含的源 SKU 数量。 |
   ^sku_unit_count |string |N |100.00 |SKU 代表的商品总量/体积。
   例如，如果 SKU 代表 500 毫升水，则当单位类型定义为 ml 时，此值将为 500。
   有效范围：[0.01, 99,999.9999]
   仅适用于欧盟市场。

**注意**：

* 这主要用于计算 SKU 的单价，仅当您希望展示单价以便于跨不同商品和包装尺寸进行价格比较时才需要。
* 单价 = 售价/(SKU 单位数量/基本单位数量)。因此，如需获取单价，还需要定义 "base unit count" 和 "unit type" 商品属性。可通过 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) 获取这些商品属性的相关信息。单价随后会在 [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) 中返回。 |
   ^external_urls |[]string |N |["https://example.com/path1", "https://example.com/path2"] |消费者可以下单的第三方商品上架页面 URL 列表。 如果您在 TikTok Shop 以外的第三方网站上架了商品并希望进行映射，请添加此属性。
   将此字段作为 URL 字符串的 JSON 数组提供。
   最大字符串长度：500 |
   ^extra_identifier_codes |[]string |N |["00012345678905","9780596520687"] |如果 SKU 属于虚拟组合商品（包含多个独立 SKU），可在此为组合中包含的 SKU 最多添加 10 个附加识别码。

**Format**:
GTIN: 14 位数字
EAN: 8、13 或 14 位数字
UPC: 12 位数字
ISBN：13 位数字，或以大写 `X` 结尾的 9 位数字
**注意**：

* 仅适用于欧盟市场。
* 标识码必须在每个 SKU 中唯一，不允许重复。 |
   ^pre_sale |object |N | |SKU 预售信息，用于根据预售类型将商品标记为预售商品。如果商品是常规商品，请省略此对象。

仅当 [Get Category Rules](6509c0febace3e02b74594a9) 返回的 `allowed_special_product_types` 不为空时适用。
**美国市场规则**：

* 常规/预售商品：商品上架后，您无法更改商品类型。
* 按需生产商品：您可以随时将其更改为常规商品。 |
   ^^type |string |N |PRE_ORDER |预售类型。
   基于地区的可能值：
   **US**
* `PRE_ORDER`：商品尚未上架或发布。可通过指定发布日期延长履约。
* `MADE_TO_ORDER`：商品仅在收到订单后生产。可通过指定时长延长履约。
* `CUSTOM`：因其他因素，商品所需的履约时限超出标准。可通过指定时长延长履约。

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`：商品尚未上架或发布。可通过指定时长延长履约。 |
   ^^fulfillment_type |object |N | |关于预售订单履约类型及相应时间范围的信息。
* `handling_duration_days` 适用于延长时长的履约。
* `release_date` 用于在固定日期开始履约。

**注意**：根据 `pre_sale.type` 的值和店铺所在地区，提供 `handling_duration_days` 或 `release_date`。 |
^^^handling_duration_days |int |N |24 |处理预售订单并移交承运商所需的期望持续时间。
仅适用于以下地区和预售类型：
**US**

* `MADE_TO_ORDER`：工作日，3 至 14 天。
* `CUSTOM`：工作日，3 至 30 天。

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`：自然日，3 至 30 天。 |
   ^^^release_date |int |N |1619611761 |商品转为普通商品并可供一般购买的日期。在该日期，订单处理也将开始，订单状态将变为 [AWAITING_SHIPMENT](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011)。

仅适用于美国的 `PRE_ORDER`。
**注意**：

* 有效范围：日期必须在当前日期的 3 到 60 天内。
* 此日期是基于卖家中心中卖家选择的时区的 Unix 时间戳（秒）。
* 商品上架后无法修改此日期。
   |
   ^list_price |object |N | |SKU 的标价信息。这等同于制造商建议零售价（MSRP）或建议零售价（RRP）。
   仅适用于美国本地卖家。

**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^amount |string |Y |1 |价格金额。
有效范围：[0.01, 7600]
**说明**：取值必须大于或等于 `skus.price.amount`。否则将被丢弃。 |
^^currency |string |Y |USD |货币。
可能的值： USD |
^external_list_prices |[]object |N | |SKU 标价（如 MSRP、RRP）或外部电商平台上的原价信息。
仅适用于美国市场选定的本地卖家。
**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^source |string |Y |SHOPIFY_COMPARE_AT_PRICE |价格来源的外部电商平台。
可能的值：

* SHOPIFY_COMPARE_AT_PRICE: Shopify 中的 compare_at_price。 |
   ^^amount |string |Y |1 |价格金额。
   有效范围：[0.01, 7600] |
   ^^currency |string |Y |USD |货币。
   可能的值： USD |
   ^fees |[]object |N | |根据 TikTok Shop 政策该商品所需的费用。仅部分商品类目需要费用，请从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取相关要求。 |
   ^^type |string |N |PFAND |费用类型。
   可能的值：PFAND |
   ^^amount |string |N |1.01 |费用金额。
   有效范围：
* PFAND: [0.00 - 6300.00] |
   ^^additional_attribute |string |N |SINGLE_USE |提供费用附加上下文的可选属性。接受的值可能因费用类型和市场而异。

Pfand 的可能值：

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |
   ^sku_dimensions |object |N | |SKU 的尺寸。

Note:

* 提供包装商品后测量的尺寸。
* 这些值会影响运费，因此确保尺寸准确很重要。任何测量差异都可能导致额外运费。
* ID、TH、VN 地区为可选。 |
   ^^length |string |Y |10 |包装长度。正整数。
   注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。 |
   ^^width |string |Y |10 |包装宽度。正整数。
   注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。 |
   ^^height |string |Y |10 |包装高度。正整数。
   注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。 |
   ^^unit |string |Y |CENTIMETER |SKU 尺寸的单位。
   基于地区的可能值：
* US: CENTIMETER, INCH
* 其他地区: CENTIMETER

注意：对 `sku_weight` 和 `sku_dimensions` 使用相同的计量系统（公制或英制）。例如，将 `KILOGRAM` 与 `CENTIMETER` 搭配使用。 |
^sku_weight |object |N | |SKU 的包装重量。
Note:

* 提供包装 SKU 后测量的重量。
* `sku_weight` 和 `sku_dimensions` 使用同一计量体系；例如 `KILOGRAM` 搭配 `CENTIMETER`。
* 重量和尺寸会影响运费，因此请确保两者准确。运费可能使用实际重量和根据尺寸计算的体积重量中的较高者。 |
   ^^value |string |Y |1.32 |包装重量，必须是正数。
   数字格式因单位而异：
* GRAM: 整数
* KILOGRAM: 最多 3 位小数
* POUND: 最多 2 位小数 |
   ^^unit |string |Y |KILOGRAM |SKU 重量的单位。
   基于地区的可能值：
* US: KILOGRAM, POUND
* BR, JP, MX: KILOGRAM, GRAM
* 其他国家: KILOGRAM

注意：对 `sku_weight` 和 `sku_dimensions` 使用相同的计量系统（公制或英制）。例如，将 `KILOGRAM` 与 `CENTIMETER` 搭配使用。 |
title |string |Y |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks |商品标题。
标题长度：

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* 其他地区: [25, 255] |
   is_cod_allowed |bool |N |false |标识是否在结账时显示货到付款（COD）付款选项的标志。 Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 检查您的商品分类是否支持 COD。

仅适用于以下市场：

* 全球卖家: MY, PH, SA, TH, VN
* 本地卖家: ID, MY, PH, SA, TH, VN

**注意**：如果不支持 COD，将此值设为 `true` 会导致上架失败。 |
certifications |[]object |N | |您的商品的认证列表。
最大数量：10
根据 TikTok Shop 规范，某些受限商品类目需要提供资质认证。请通过 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取您商品的资质要求。有关商品类目限制的信息，请参阅 [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy)。 |
^id |string |Y |7182427311584347905 |用于标识商品分类所需认证类型的 ID。
从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取该值。 |
^images |[]object |N | |认证相关图片列表。 |
^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe
|图片的 URI。
通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CERTIFICATION_IMAGE` 获取此 URI。 |
^files |[]object |N | |认证相关文件列表。 |
^^id |string |Y |v09ea0g40000cj91373c77u3mid3g1s0 |认证文件的 ID。
先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传文件并获取对应的文件 ID。 |
^^name |string |Y |SNI.PDF |认证文件的名称，包括文件扩展名。 |
^^format |string |Y |PDF |认证文件的格式。仅支持 PDF。 |
^expiration_date |int |N |1741234626 |此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。
对于某些资质认证，此字段可能为必填。请使用 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 了解相关要求。 |
package_weight |object |N | |商品包装的重量。
**注意**：

* 所有商品包装重量**默认为必填**, （**虚拟商品**分类下的商品除外）。 [Get Categories API](https://partner.tiktokshop.com/docv2/page/get-categories-202309) 例如**数字游戏**。
* 提供包装商品后测量的重量。
* 此值会影响运费，因此确保重量准确很重要。任何测量差异都可能导致额外运费。
* 如果基于重量的费用更高，则包装重量将在费用计算中优先于包装尺寸。 |
   ^value |string |Y |1.32 |包装重量，必须是正数。
   数字格式因 `unit` 而异：
* `GRAM`: integer
* `KILOGRAM`：最多 3 位小数
* `POUND`：最多 2 位小数 |
   ^unit |string |Y |KILOGRAM |包装重量的单位。
   基于地区的可能值：
* US: `KILOGRAM`, `POUND`
* BR, JP, MX: `KILOGRAM`, `GRAM`
* Other countries: `KILOGRAM`

**注意**：必须对 `package_weight` 和 `package_dimensions` 使用相同的计量系统（公制或英制）。换言之，如果重量使用 `KILOGRAM`，则尺寸必须使用 `CENTIMETER`。 |
product_attributes |[]object |N | |描述商品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。
**重要**：可用属性由系统根据商品所属类目确定，其中部分为必填。您必须提供 [Get Attributes API](6509c5784a0bb702c0561cc8) 响应中标记为 `is_required` 的商品属性，以避免上架失败。 |
^id |string |Y |100392 |商品属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 |
^values |[]object |Y | |商品属性的可选值列表。
**注意**： 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。 |
^^id |string |N |1001533 |内置商品属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 |
^^name |string |N |Birthday |如果内置值不满足需求，可自定义商品属性值。系统将在上架后自动生成 ID。
**注意**：

* 同一属性下不允许重复。
* 最大长度：2000 个字符 |
   size_chart |object |N | |商品的测量详情，帮助买家找到合适的尺码。

**注意**：

* 对于某些商品分类，可能需要或不支持尺码表。 Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 检查要求。
* 如果不支持尺码表，即使您在此处提供尺码表，也不会保存。
* 提供 TikTok Shop 尺码表模板 ID 或尺码表图片；如果同时提供，则 ID 优先。 |
   ^image |object |N | |尺码表的图片。

**建议**：

* 分辨率：较短边最小 1024 像素
* 内容：包含关键测量尺寸（如胸围、腰围、臀围、内缝），越多越好。
* 格式：使用具有明显列和行的表格。
   * 每个商品和图片仅使用一个表格。
   * 在单独的行中显示每个尺寸。
   * 在列标题中显示单位。 |
      ^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |尺码表图片的 URI。
      通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=SIZE_CHART_IMAGE` 获取此 URI。 |
      ^template |object |N | |由卖家中心 > 管理商品 > 批量操作 > 批量管理尺码表中的尺码表工具生成的 TikTok Shop 尺码表模板。 |
      ^^id |string |Y |7267563252536723205 |尺码表模板 ID。 |
      package_dimensions |object |N | |商品包装的尺寸。

**注意**：

* 提供包装商品后测量的尺寸。
* 这些值会影响运费，因此确保尺寸准确很重要。任何测量差异都可能导致额外运费。
* ID、TH、VN 地区为可选。 |
   ^length |string |Y |10 |包装长度。正整数。
   **注意**：对于 BR 市场，使用 `.` 或 `,` 作为分隔符的小数值也可接受，但会四舍五入为最接近的整数。 |
   ^width |string |Y |10 |包装宽度。正整数。
   **注意**：对于 BR 市场，使用 `.` 或 `,` 作为分隔符的小数值也可接受，但会四舍五入为最接近的整数。 |
   ^height |string |Y |10 |包装高度。正整数。
   **注意**：对于 BR 市场，使用 `.` 或 `,` 作为分隔符的小数值也可接受，但会四舍五入为最接近的整数。 |
   ^unit |string |Y |CENTIMETER |包裹尺寸的单位。
   基于地区的可能值：
* US: CENTIMETER, INCH
* 其他地区: CENTIMETER

**注意**：必须对 `package_weight` 和 `package_dimensions` 使用相同的计量系统（公制或英制）。换言之，如果重量使用 KILOGRAM，则尺寸必须使用 CENTIMETER。 |
external_product_id |string |N |172959296971220002 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联商品。
最大长度：999 个字符 |
delivery_option_ids |[]string |N |["1729592969712203232"] |该字段仅支持以下地区的卖家账号：

* ID
* MX
* MY
* PH
* SG
* TH
* VN

如果要覆盖默认的仓库配送选项，应用于此商品的自定义配送选项 ID。要获取可用的选项 ID，请使用 `scope=PRODUCT` 调用 [Get Warehouse Delivery Options](650aa46ebace3e02b75d9afa)。
**注意**： 将此字段留空以继承为仓库配置的默认配送选项。 |
video |object |N | |用于展示商品的商品介绍或推广视频。
**建议**：

* Aspect ratio: 1:1
* 分辨率：HD 720p 或更高
* Duration: 20 - 60 seconds |
   ^id |string |Y |v09e40f40000cfu0ovhc77ub7fl97k4w |商品视频的 ID。
   先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传视频并获取对应的文件 ID。 |
   primary_combined_product_id |string |N |1729582718312380123 |如果此商品关联虚拟套装，此值是主要 套装中的商品 ID。

**注意**： 仅虚拟套装商品需要。 |
manufacturer_ids |[]string |N |["172959296971220002"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9)。
**注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Category Rules API](6509c0febace3e02b74594a9) 检查要求。 |
responsible_person_ids |[]string |N |["172959296971220003"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1)。
**注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Category Rules API](6509c0febace3e02b74594a9) 检查要求。 |
listing_platforms |[]string |N |["TIKTOK_SHOP"] |商品上架的平台。
可能的值：

* TOKOPEDIA
* TIKTOK_SHOP
   默认值：TIKTOK_SHOP

仅适用于从 Tokopedia 迁移的卖家。 |
shipping_insurance_requirement |string |N |NOT_SUPPORTED |对买家施加的商品运输保险购买要求。
可能的值：

* REQUIRED: 运输保险为强制购买，买家无法取消。
* OPTIONAL: 买家可以选择通过平台购买运输保险。
* NOT_SUPPORTED: 商品不支持运输保险。
   Default: OPTIONAL

仅当上架平台包含 TOKOPEDIA 时适用。 |
is_pre_owned |bool |N |false |标识商品是否为二手商品的标志。
仅当 TOKOPEDIA 是唯一上架平台时适用。
**注意**：要在 TikTok Shop 平台上架二手商品，请在 `category_id` 中填入指定二手商品类目之一的 ID（例如二手奢侈包袋、箱包和配饰）。 |
minimum_order_quantity |int |N |4 |商品的最低订购量。
有效范围： [1, 20]
仅适用于印尼市场及其他东南亚市场的部分卖家。如需了解如何获得此字段的访问权限，请联系您的客户经理。 |
shipping_template_id |string |N |7552764259994699538 |将绑定到商品的运费模板的标识符 |
option |object |N | |异步商品信息验证的选项。 |
^need_trigger_gne_async_check |bool |N |false |是否触发异步商品信息校验。此异步工作流仅对美国已启用的卖家可用。
将此字段设为 `true` 并同时提供非空的 `gne_async_check_session_id`，以启动新的异步检查。
若要使用同一会话 ID 重试获取而不创建新的异步任务，请将此字段设为 `false`；任何已完成的检查结论将在 `pre_check_results` 中返回。 |
^gne_async_check_session_id |string |N |20260122085233268 |调用方提供的会话 ID，用于异步商品信息校验。此异步工作流仅对 US 已启用的卖家可用。
触发异步校验时提供非空会话 ID，随后在携带相同商品信息再次调用此接口时复用同一会话 ID，以在 `pre_check_results` 中获取任何已完成的检查结论。
此接口不会为您生成或返回新的会话 ID。 |
scheduled_sale |object |N | |商品的定时上架配置，包括是否启用定时上架及定时上架时间。 |
^is_enabled_scheduled_sale |bool |Y |false |该商品是否启用定时上架。如果为 `true`，则必须提供 `schedule_sale_time`。 |
^schedule_sale_time |int |Y |1768899145000 |定时上架时间，以毫秒级 Unix 时间戳表示；必须晚于当前时间且在 90 天内，当 is_enabled_scheduled_sale 为 true 时必填。 |
search_terms |[]string |N |["sneakers","running shoes","athletic"] |搜索词（ST 词）。 ST words will not be displayed to consumers; they are only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words are consistent with the product description, with a maximum of 15 terms and a total of no more than 250 characters。 |
key_product_features |[]string |N |["Breathable mesh upper", "Cushioned foam midsole"] |关键商品特性。 They will be displayed in the Product highlight module on the product detail page and will be used by search engines to increase your search weight for more traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500。 |
product_tag_operations |[]object |N | |用于启用或停用 `AUCTION` 商品标签的旧版操作。如果提供了 `selling_format`，则优先于该字段。 |
^product_tag |string |Y |AUCTION |可能的值： AUCTION |
^enable |bool |Y |true |是否启用指定的商品标签。设为 `true` 以启用 `AUCTION` 标签，设为 `false` 以禁用。 |
locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。
Default: 您店铺的默认语言环境。
可能的值：

* cs-CZ
* de-AT
* de-BE
* de-DE
* el-GR
* en-GB
* en-IE
* en-US
* es-ES
* es-MX
* fr-FR
* fr-BE
* hu-HU
* id-ID
* it-IT
* ja-JP
* ms-MY
* nl-NL
* nl-BE
* pl-PL
* pt-BR
* pt-PT
* th-TH
* vi-VN
* zh-CN |
   selling_format |string |Y |FIXED_PRICE_AND_LIVE_AUCTION |选择固定价格或固定价格加 LIVE 拍卖。默认选择固定价格。LIVE 拍卖需要起拍价。可选值：FIXED_PRICE, FIXED_PRICE_AND_LIVE_AUCTION。 |
   is_live_quick |bool |N |false |false — 常规商品
   true — LIVE_QUICK 商品。只有具有所需权限的卖家才能创建 LIVE_QUICK 商品。
   默认值：false |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/listing_check?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&is_diagnosis_required=true
```

**Body**
```json
{"description":"\u003cp\u003ePlease compare above detailed size with your measurement before purchase.\u003c/p\u003e\n\u003cul\u003e \n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" /\u003e\n","category_id":"600001","brand_id":"7082427311584347905","main_images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"skus":[{"sales_attributes":[{"id":"100089","name":"Specification","value_id":"1729592969712207000","value_name":"XL","sku_img":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"supplementary_sku_images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}]}],"seller_sku":"Color-Red-XM01","price":{"amount":"1.23","currency":"USD","sale_price":"1.21","starting_bid_price":"2.3"},"external_sku_id":"1729592969712207012","identifier_code":{"code":"10000000000000","type":"GTIN"},"inventory":[{"warehouse_id":"7068517275539719942","quantity":999,"backorder_quantity":888,"handling_time":5}],"combined_skus":[{"product_id":"1729582718312380123","sku_id":"1729582718312380123","sku_count":11}],"sku_unit_count":"100.00","external_urls":["https://example.com/path1","https://example.com/path2"],"extra_identifier_codes":["00012345678905","9780596520687"],"pre_sale":{"type":"PRE_ORDER","fulfillment_type":{"handling_duration_days":24,"release_date":1619611761}},"list_price":{"amount":"1","currency":"USD"},"external_list_prices":[{"source":"SHOPIFY_COMPARE_AT_PRICE","amount":"1","currency":"USD"}],"fees":[{"type":"PFAND","amount":"1.01","additional_attribute":"SINGLE_USE"}],"sku_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"sku_weight":{"value":"1.32","unit":"KILOGRAM"}}],"title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks","is_cod_allowed":false,"certifications":[{"id":"7182427311584347905","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe\n"}],"files":[{"id":"v09ea0g40000cj91373c77u3mid3g1s0","name":"SNI.PDF","format":"PDF"}],"expiration_date":1741234626}],"package_weight":{"value":"1.32","unit":"KILOGRAM"},"product_attributes":[{"id":"100392","values":[{"id":"1001533","name":"Birthday"}]}],"size_chart":{"image":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"template":{"id":"7267563252536723205"}},"package_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"external_product_id":"172959296971220002","delivery_option_ids":["1729592969712203232"],"video":{"id":"v09e40f40000cfu0ovhc77ub7fl97k4w"},"primary_combined_product_id":"1729582718312380123","manufacturer_ids":["172959296971220002"],"responsible_person_ids":["172959296971220003"],"listing_platforms":["TIKTOK_SHOP"],"shipping_insurance_requirement":"NOT_SUPPORTED","is_pre_owned":false,"minimum_order_quantity":4,"shipping_template_id":"7552764259994699538","option":{"need_trigger_gne_async_check":false,"gne_async_check_session_id":"20260122085233268"},"scheduled_sale":{"is_enabled_scheduled_sale":false,"schedule_sale_time":1768899145000},"search_terms":["sneakers","running shoes","athletic"],"key_product_features":["Breathable mesh upper","Cushioned foam midsole"],"product_tag_operations":[{"product_tag":"AUCTION","enable":true}],"locale":"en-US","selling_format":"FIXED_PRICE_AND_LIVE_AUCTION","is_live_quick":false}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^check_result | string | FAILED | 商品诊断的结果（PASS, FAILED）。 |
| ^fail_reasons | []object |  | 当 `check_result` 为 FAILED 时的失败原因列表。 |
| ^^code | int | 12052700 | 代表失败原因的机器可读代码。 This is equivalent to the error codes shown when creating a product. For the full list of codes, refer to [Create Product > Error Code](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a?#Error_Code)。 |
| ^^message | string | Product title invalid | 详细的失败原因。 |
| ^warnings | object |  | API 调用者需要特别关注的警告信息。 |
| ^^message | string | 您的商品将不会被提交审核。 | 需要注意的警告信息。 Review and address it when applicable. Its presence alone does not mean `check_result` is `FAILED`。 |
| ^listing_quality | object |  | (**已弃用**：此字段已弃用，将在未来的 API 版本中移除。请改用 [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API 获取商品信息质量相关信息。） |
| 商品上架质量信息。 |  |  |  |
| ^^current_tier | string | POOR | 此商品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc。 |
可能的值：

* POOR
* FAIR
* GOOD
* EXCELLENT

**注意**：仅适用于美国市场。 |
^^remaining_recommendations |int |3 |商品达到最高层级仍需完成的建议数量（参见 `diagnosis_results`）。
**注意**：

* 要达到最高等级，必须落实 `diagnosis_results` 中列出的所有建议。
* 仅适用于美国市场。 |
   ^diagnoses |[]object | |(**已弃用**：此字段已弃用，将在未来的 API 版本中移除。请改用 [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API 获取商品诊断相关信息。)
   商品优化诊断信息。 |
   ^^field |string |TITLE |被诊断的商品字段。
   可能的值：
* TITLE：商品标题
* DESCRIPTION：商品描述
* IMAGE：图片库中展示的商品图片
* ATTRIBUTE：商品属性
* SIZE_CHART：商品尺码表 |
   ^^diagnosis_results |[]object | |诊断结果。
   |
   ^^^code |string |TITLE_LESS_THAN_40_CHARACTERS |代表已识别问题的机器可读代码。
   有关已识别问题的完整列表及相应建议，请参阅 [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd)。 |
   ^^^how_to_solve |string |Names must be at least 40 characters long and contain product-identifying information, such as "hiking boots" or "lipstick". |解决已识别问题的建议，以店铺的默认语言返回。
   有关建议的完整列表，请参阅 [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd)。 |
   ^^^quality_tier |string |FAIR |通过实施建议可以达到的上架质量等级。
   可能的值：
* FAIR
* GOOD

**注意**：

* 要达到更高层级，必须落实目标层级及之前所有层级的全部建议。例如，当所有 "FAIR" 和 "GOOD" 建议都得到处理或落实后，商品就会达到 "GOOD" 层级。
* 仅适用于美国市场。 |
   ^^suggestions |object | |改进建议。 |
   ^^^seo_words |[]object | |当 `diagnoses.field` 为 "TITLE" 时的 SEO 关键词建议。 |
   ^^^^text |string |dress |建议的 SEO 关键词文本。 |
   ^^^smart_texts |[]object | |标题和描述的智能文本建议。 |
   ^^^^text |string |this is a good title |建议的智能文本。 |
   ^^^images |[]object | |优化后的主图。仅优化主图组中的第一张图片。 |
   ^^^^uri |string |tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d |图片的原始 URI。
   |
   ^^^^url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp |图片的原始 URL。 |
   ^^^^optimized_uri |string |tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6 |优化后图片的 URI。 |
   ^^^^optimized_url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp |优化后图片的 URL。 |
   ^^^^height |int |600 |优化后的图片高度。 |
   ^^^^width |int |600 |优化后的图片宽度。 |
   ^pre_check_results |[]object | |包含所提供 `gne_async_check_session_id` 可用的任何已完成商品信息校验结论。响应不单独暴露待处理或已完成状态。如果此字段缺失或为空，则无法从响应判断异步检查是否已完成或通过。 |
   ^^pre_check_item |string |INCOMPLETE_INFO |商品信息校验类型：商品信息校验返回的问题类型。 |
   ^^pre_check_details |[]object | |信息校验详情。 |
   ^^^short_reason |string |Insufficient or Incomplete Product Information |精简原因：商品校验结果的简单问题描述 |
   ^^^long_reason |string |确保商品标题和描述包含能准确描述该商品的完整信息 |详细原因: 商品校验结果的详细问题描述 |
   ^^^related_fields |[]string |["PRE_CHECK_FIELD_TITLE"] |问题模块: 问题源自哪个模块，例如 PRE_CHECK_FIELD_TITLE、PRE_CHECK_FIELD_IMAGES |

# 响应示例
```json
{"code":0,"data":{"check_result":"FAILED","fail_reasons":[{"code":12052700,"message":"Product title invalid"}],"warnings":{"message":"Your product will not be sent for review. "},"listing_quality":{"current_tier":"POOR","remaining_recommendations":3},"diagnoses":[{"field":"TITLE","diagnosis_results":[{"code":"TITLE_LESS_THAN_40_CHARACTERS","how_to_solve":"Names must be at least 40 characters long and contain product-identifying information, such as \"hiking boots\" or \"lipstick\".","quality_tier":"FAIR"}],"suggestions":{"seo_words":[{"text":"dress"}],"smart_texts":[{"text":"this is a good title"}],"images":[{"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp","optimized_uri":"tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6","optimized_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp","height":600,"width":600}]}}],"pre_check_results":[{"pre_check_item":"INCOMPLETE_INFO","pre_check_details":[{"short_reason":"Insufficient or Incomplete Product Information","long_reason":"Ensure product title and description contain complete information that accurately describes the product","related_fields":["PRE_CHECK_FIELD_TITLE"]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12001000 | product api 内部错误 |
| 12019006 | product description is invalid |
| 12019011 | product package weight is invalid |
| 12019095 | `pre_sale.fulfillment_type` is missing or empty. |
| 12019097 | `pre_sale.fulfillment_type.release_date` 必须设置为非零值。 |
| 12019098 | `pre_sale.fulfillment_type.handling_duration_days` 必须设置为非零值。 |
| 12019099 | The specified `pre_sale.type` is not supported in your region. Refer to the API documentation for details. |
| 12019121 | calculate price error |
| 12052003 | Incorrect parcel height format |
| 12052004 | Incorrect parcel width format |
| 12052005 | Incorrect parcel length format |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052084 | 所提供的货币不适用于该店铺/地区。 |
| 12052220 | 该类目在 TikTok Shop 上被禁止或不受支持。请选择其他类目。 |
| 12052223 | 该类目受限。如需在该类目下销售，请通过 Seller Center 中的资质中心申请。 |
| 12052226 | 该类目受限。如需在该类目下销售，请通过 Seller Center 中的资质中心申请。 |
| 12052300 | product main image uri illegal |
| 12052356 | The number of 'supplementary_sku_images' for the sales attribute value exceeds the maximum limit. |
| 12052357 | 'supplementary_sku_images' is only allowed when 'sku_img' is specified. Add an image to 'sku_img' and try again. |
| 12052446 | 分类 is not open in this market |
| 12052520 | product sale property image uri illegal |
| 12052650 | product qualification image uri illegal |
| 12052670 | 尺码表图片 URI 无效。注意：API 用户必须使用 Upload Product Image API 生成的 URI。 |
| 12052700 | 卖家不活跃。 |
| 12052722 | The image URI does not exist in TikTok Shop. |
| 12052881 | identity 内部错误 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |
| 12052915 | package weight unit and dimension unit miss match. |
| 12052916 | The package unit is not supported in the current region. |
| 12052930 | Seller SKU is required |
| 12052931 | 标题必须遵循以下格式规则: 不能包含 HTML 转义字符 (e.g., )、表情符号或 ASCII 控制字符 (e.g., \u007F). 也不能仅由符号组成 (e.g., //// or !@#$$$&), 且连续重复字符不能超过 9 个 (e.g., aaaaaaaaa or 111111111)。 |
| 12052932 | 描述必须遵循以下格式规则: 不能包含 HTML 转义字符 (e.g., )、表情符号或 ASCII 控制字符 (e.g., \u007F). 也不能仅由符号组成 (e.g., //// or !@#$$$&), 且连续重复字符不能超过 9 个 (e.g., aaaaaaaaa or 111111111)。 |
| 12052933 | 销售属性名称必须遵循以下格式规则: 不能包含 HTML 转义字符 (e.g., )、表情符号或 ASCII 控制字符 (e.g., \u007F). 也不能仅由符号组成 (e.g., //// or !@#$$$&), 且连续重复字符不能超过 9 个 (e.g., aaaaaaaaa or 111111111)。 |
| 12052934 | 销售属性值名称必须遵循以下格式规则: 不能包含 HTML 转义字符 (e.g., )、表情符号或 ASCII 控制字符 (e.g., \u007F). 也不能仅由符号组成 (e.g., //// or !@#$$$&), 且连续重复字符不能超过 9 个 (e.g., aaaaaaaaa or 111111111)。 |
| 12052935 | 商品属性值名称必须遵循以下格式规则: 不能包含 HTML 转义字符 (e.g., )、表情符号或 ASCII 控制字符 (e.g., \u007F). 也不能仅由符号组成 (e.g., //// or !@#$$$&), 且连续重复字符不能超过 9 个 (e.g., aaaaaaaaa or 111111111)。 |
| 12052936 | Seller SKU format invalid. SKU name must contain 6 - 50 characters and use alphabets, numbers, hyphens (-), or underscores (_) only. |

