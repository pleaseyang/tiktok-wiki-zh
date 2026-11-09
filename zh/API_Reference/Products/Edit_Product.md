# 编辑商品

# 路径：/product/202509/products/{product_id}
# 方法：[PUT]
# 功能描述
编辑未处于 `FREEZE` 或 `DELETED` 状态的现有商品的所有属性（例如描述、品牌、图片）。
编辑商品后，最新的商品内容（称为 v2）将重新送交审核。如果审核通过，v2 将发布到店铺；否则现有商品保持上架且不变（保留 v1）。但是，对 `price` 或 `inventory` 字段的编辑无需重新审核，将立即在平台发布。使用 [Product status change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook 跟踪审核状态。
**注意**：

* 此接口仅适用于已完成 KYC 入驻流程的**活跃卖家/店铺**。
* 每天可重新上架的商品数量可能有限制。建议优先处理重点商品以确保其发布。您可在 Seller Center 首页查看上架限额。
* 请求负载中的所有输入（包括空值）都将覆盖现有值。要保留现有值，请务必在请求中包含该值。此规则的例外是 `price` 和 `inventory` 字段，如果请求中省略它们，它们将保持不变。因此，**强烈建议使用** [Get Product](6509d85b4a0bb702c057fdda) **获取最新商品数据，并在编辑时提交完整数据**。这可确保准确性，并有助于避免因字段缺失导致的错误或意外数据丢失。
* 如果只想编辑某些属性，可以使用 [Partial Edit Product API](650a98d74a0bb702c06c3289)、[Update Inventory API](6503068fc20ad60284b38858) 或 [Update Price API](650307de5a12ff0294eac8b0)。
* 商品内容中使用的语言必须与目标市场的语言一致（例如，不要使用中文），否则上架将失败或被拒绝。
   **面向全球卖家**：
   如果您使用本地复制上架方式，请注意以下同步规则：
* 要将任何变更同步到其他市场，请提供 `seller_sku` 和完整的 `replicated_products` 数据。
* 请注意，**类目变更**和**销售属性变更**（销售属性 ID/名称）必须同步到其他市场。如果未提供这些详细信息，接口调用将失败。
   **面向 Tokopedia 卖家**：
   请注意，一个商品在任何时刻于所有平台上只能有**一个生效版本**。如果商品在两个平台上均在售，最新版本的审核结果按以下方式处理：
* **审核结果混合**：如果商品在一个平台通过审核但在另一个平台未通过，在通过审核的平台上，商品将保持在售并更新为最新版本（v2）的内容，而在未通过审核的平台上，商品将被停用并完全隐藏。
* **所有平台审核均失败**：如果商品在所有平台审核均未通过，现有商品将保持在售且保持不变（保留 v1）。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 1729409636071801988 | TikTok Shop 生成的商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| save_mode | string | N | AS_DRAFT | 指示商品应如何保存。 |
| 可能的值： |  |  |  |  |

* AS_DRAFT: 将商品保存为草稿以便将来编辑。
* LISTING: 提交编辑后的商品进行上架。需要审核的变更在批准后才发布；对价格或库存字段的变更立即发布。
   默认值：LISTING

**注意**：

* 当商品状态为 `DELETED`，或商品在任一上架平台处于 `PENDING` 或 `FREEZE` 时，不支持保存为草稿。
* 使用 `save_mode=AS_DRAFT` 保存上架后草稿时，不支持 `inventory` 和 `delivery_option_ids`，也不会保存它们。 |
   description |string |N |
   购买前请将上述详细尺码与您的测量尺寸进行比较。
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
   category_id |string |Y |600001 |此商品所属类目的 ID。必须是与 `category_version` 属性中指定的类目树类型相对应的叶子类目。请使用 [Get Categories API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) 获取可用类目。

**注意**：

* 有关商品分类限制的信息，请参考 TikTok Shop Academy。
* 针对美国市场，如果将商品类目更改为 `INVITE_ONLY` 类目，必须通过 TikTok Shop Seller Center 上的 Qualification Center 单独提交申请以获得相应权限。否则，即使商品审核通过，商品也不会上架并向买家开放。（商品状态将为 `PENDING`，审核状态将为 `PRE_APPROVED`）
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
* 第一张图片应有白色背景。 Use the [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) 将背景更改为白色 |
   ^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
   通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=MAIN_IMAGE` 获取此 URI。您可以直接使用返回的 URI，或先通过 [Optimize Images API](665692b35d39dc02deb49a97) 处理后再使用生成的 URI。 |
   skus |[]object |Y | |用于标识商品不同变体的 SKU（库存单位）列表。

**注意**：

* BR、EU、MX、JP、UK、US 的 SKU 上限: 300
* 其他地区的最大 SKU 数量：100

**建议**：将最重要的变体放在数组开头。 |
^id |string |N |1729592969712207000 |由 TikTok Shop 生成的 SKU ID。一个商品可包含多个 SKU ID。
**注意**：

* 要编辑现有 SKU，请包含其 SKU ID。
* 此处未列出的任何现有 SKU ID 都将导致对应 SKU 被删除。例如，如果该商品包含 5 个 SKU，而您只提供 2 个 SKU ID，则其余 3 个将被删除。
* 要创建新 SKU，请将 SKU ID 留空并填写其他字段。 |
   ^sales_attributes |[]object |N | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。

**注意**：

* 必须至少保留 1 个销售属性，不允许删除全部现有销售属性。
* 每个商品最多只能有 3 种销售属性类型。
* 每个 SKU 必须包含相同数量和类型的销售属性。 例如，不能一个 SKU 只有颜色属性，而另一个 SKU 同时有颜色和尺码属性。
* 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。
* `id/name` 与 `value_id/value_name` 组合在每个 SKU 中必须唯一。例如，不能在不同 SKU 中重复 `"name": "Color"`、`"value_name": "Red"`。 |
   ^^id |string |N |100089 |销售属性的 ID。
   该值可以是来自 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) 的内置销售属性 ID，也可以是调用 [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) 后返回的自定义属性 ID。 |
   ^^name |string |N |Specification |当现有属性不满足需求时，可自定义销售属性名称。系统将在编辑后自动生成 ID。

**注意**：

* 不要包含敏感字符。
* 最大长度：20 个字符
   |
   ^^value_id |string |N |1729592969712401100 |销售属性值的 ID。
   该值可以是来自 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) 的内置销售属性值 ID，也可以是调用 [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) 后返回的自定义销售属性值 ID。 |
   ^^value_name |string |N |XL |当现有取值不满足需求时，可自定义销售属性值。系统将在编辑后自动生成 ID。

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
   ^seller_sku |string |N |Color-Red-XM001 |用于管理 SKU 的内部代码/名称，对买家不可见。
   有效长度：
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 个字符
* 其他地区: 1-50 个字符
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 仅使用字母、数字、连字符 (-) 或下划线 (_)
* 其他地区: 不含空格的文本 |
   ^price |object |N | |SKU 定价信息。

**注意**: 如果在接口请求中省略此对象，现有信息将保持不变。 |
^^amount |string |N |1.21 |**本地卖家/欧盟内部卖家**
SKU 在商品页面上折扣前显示的**本地展示价格**。 Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。
**全球卖家**
SKU 的**本地税前价格**。不含跨境配送费用、税费及其他适用费用等，因此不会显示在商品页面上。
Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

* **注意**：不适用于使用中国仓库的 JP 和 US 店铺，请改用 `price.sale_price`。 |
   ^^currency |string |Y |USD |货币。
   基于地区的可能值：
* BRL: 巴西
* EUR：法国、德国、爱尔兰、意大利、西班牙
* GBP: 英国
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
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
   ^identifier_code |object |N | |根据国际标准化法规（如 GTIN）分配给商品的受管标识码，以确保商品在各种平台和系统中可普遍识别。

**注意**：仅当商品处于 DRAFT 状态时可编辑。否则不允许更改。 |
^^code |string |N |12345678901234 |标识码。
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
   ^inventory |[]object |N | |SKU 库存信息。

**注意**：

* 如果在接口请求中省略此对象数组，现有信息将保持不变。
* 如果使用 `save_mode=AS_DRAFT` 保存上架后草稿，则不支持该字段且不会保存。使用 Get Product 获取草稿时，取值将反映基础版本中的值。 |
   ^^warehouse_id |string |Y |7068517275539719942 |SKU 存放仓库的 ID。
   从以下位置获取您的店铺可用仓库列表 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6)。 |
   ^^quantity |int |N |999 |仓库中可用的 SKU 总数量。
   有效范围：[1, 99,999]

注意：此数量特指可以立即发货的有库存的库存量。 |
^^backorder_quantity |int |N |888 |一旦现货库存售罄，`backorder_quantity` 将自动转换为 `quantity`。其履约遵循指定的 `handling_time`。
**注意**：

* 请同时提供 `backorder_quantity` 和 `handling_time`。
* 按单生产（MTO）、预售和定制商品不支持缺货预订，因此不能使用 `backorder_quantity`。 |
   ^^handling_time |int |N |5 |The estimated number of working days needed for a backorder to be shipped. Provide `handling_time` and `backorder_quantity` together. Different warehouses for the same SKU cannot use different `handling_time` values. |
   ^combined_skus |[]object |N | |如果此 SKU 属于虚拟套装，此对象包含组成套装的单个 SKU 列表（如礼品篮、入门套装）。 |
   ^^product_id |string |Y |1729582718312380123 |虚拟套装中包含的源商品 ID。 |
   ^^sku_id |string |Y |2729382476852921560 |虚拟套装中包含的源 SKU ID。 |
   ^^sku_count |int |Y |2 |虚拟套装中包含的源 SKU 数量。 |
   ^sku_unit_count |string |N |100.00 |SKU 代表的商品总量/体积。
   例如，如果 SKU 代表 500 毫升水，则当单位类型定义为 ml 时，此值将为 500。
   有效范围：[0.01, 99,999.9999]
   仅适用于欧盟市场。

**注意**：

* 这主要用于计算 SKU 的单价，仅当您希望展示单价以便于跨不同商品和包装尺寸进行价格比较时才需要。
* 单价 = 售价/(SKU 单位数量/基本单位数量)。因此，如需获取单价，还需要定义 "base unit count" 和 "unit type" 商品属性。可通过 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) 获取这些商品属性的相关信息。单价随后会在 [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) 中返回。 |
   ^external_urls |[]string |N |["https://example.com/path1", "https://example.com/path2"] |消费者可以下单的第三方商品上架页面 URL 列表。 如果您在 TikTok Shop 以外的第三方网站上架了商品并希望进行映射，请添加此属性。
   最大字符串长度：500 |
   ^extra_identifier_codes |[]string |N | ["00012345678905","9780596520687"] |如果 SKU 属于虚拟组合商品（包含多个独立 SKU），可在此为组合中包含的 SKU 最多添加 10 个附加识别码。

**Format**:
GTIN: 14 位数字
EAN: 8、13 或 14 位数字
UPC: 12 位数字
ISBN：13 位数字，或以大写 `X` 结尾的 9 位数字
**注意**：

* 仅适用于欧盟市场。
* 标识码必须在每个 SKU 中唯一，不允许重复。 |
   ^pre_sale |object |N | |SKU 预售信息，用于根据预售类型将商品标记为预售商品。
   仅当 [Get Category Rules](6509c0febace3e02b74594a9) 返回的 `allowed_special_product_types` 不为空时适用。

**通用使用规则**:

* 省略此对象可保留当前的预售设置。

**美国市场规则**：

* 常规/预售商品：商品上架后，您无法更改商品类型。
* 按需生产商品：您可以随时将其更改为常规商品。 |
   ^^type |string |N |PRE_ORDER |预售类型。
   基于地区的可能值：
   **US**
* `PRE_ORDER`：商品尚未上架或发布。可通过指定**发布日期**延长履约。
* `MADE_TO_ORDER`：商品仅在收到订单后生产。可通过指定**时长**延长履约。
* `CUSTOM`：因其他因素，商品所需的履约时限超出标准。可通过指定**时长**延长履约。

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`: 商品尚未上架或发布。可通过指定**时长**延长履约。

**ALL**

* `NONE`: 将商品转换为普通（非预售）商品。 |
   ^^fulfillment_type |object |N | |关于预售订单履约类型及相应时间范围的信息。
* `handling_duration_days` 适用于延长时长的履约。
* `release_date` 用于在固定日期开始履约。

**注意**：根据 `pre_sale.type` 的值和店铺所在地区，提供 `handling_duration_days` 或 `release_date`。 |
^^^handling_duration_days |int |N |7 |处理预售订单并移交承运商所需的期望持续时间。
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
* 商品上架后无法修改此日期。 |
   ^list_price |object |N | |SKU 的标价信息。这等同于制造商建议零售价（MSRP）或建议零售价（RRP）。
   仅适用于美国本地卖家。

**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^amount |string |Y |1 |价格金额。
有效范围：[0.01, 7600]
**注意**：

* 该值必须等于或大于 `skus.price.amount`。否则将被丢弃。
* 如果该值经审核团队核实为合规，将被保存并在 [Get Product API](6509d85b4a0bb702c057fdda) 中返回。 |
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

注意: 你必须为 `sku_weight` 和 `sku_dimensions` 使用相同的计量单位制（公制或英制）。换言之，如果重量使用 KILOGRAM，则尺寸必须使用 CENTIMETER。 |
^sku_weight |object |N | |SKU 的包装重量。
**注意**：

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

注意: 你必须为 `sku_weight` 和 `sku_dimensions` 使用相同的计量单位制（公制或英制）。换言之，如果重量使用 KILOGRAM，则尺寸必须使用 CENTIMETER。 |
title |string |Y |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks
|产品标题。
标题长度：

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* 其他地区: [25, 255] |
   is_cod_allowed |bool |N |false |标识是否在结账时显示货到付款（COD）付款选项的标志。
   Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 检查您的商品分类是否支持 COD。

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
^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CERTIFICATION_IMAGE` 获取此 URI。 |
^files |[]object |N | |认证相关文件列表。 |
^^id |string |Y |v09e40f40000cfu0ovhc77ub7fl97k4w |认证文件的 ID。
先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传文件并获取对应的文件 ID。 |
^^name |string |Y |Certificate.pdf |认证文件的名称，包括文件扩展名。 |
^^format |string |Y |PDF |认证文件的格式。仅支持 PDF。 |
^expiration_date |int |N |1741235456 |此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。
对于某些资质认证，此字段可能为必填。请使用 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 了解相关要求。 |
package_weight |object |N | |商品包装的重量。
**注意**：

* 商品包裹重量默认为必填，但 **Virtual Products** 类目下的商品除外。参见 [Get Categories API](https://partner.tiktokshop.com/docv2/page/get-categories-202309)，例如 **Digital Games**。
* 提供包装商品后测量的重量。
* 此值会影响配送费用，请确保重量准确。测量差异可能导致额外的配送费用。
* 如果按重量计算的费用更高，则费用计算中包裹重量优先于包裹尺寸。 |
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
^^id |string |N |1001533 |商品属性值的 ID。
该值可以是来自 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) 的内置商品属性值 ID，也可以是调用 [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) 后返回的自定义商品属性值 ID。 |
^^name |string |N |Birthday |内置值无法满足需求时自定义的商品属性值。系统将在编辑后自动生成 ID。
**注意**：

* 同一属性下不允许重复。
* 最大长度：2000 个字符 |
   ^^metric_standard_info |object |N | |定义度量模板信息，用于描述为商品配置的度量标准和指标值。 |
   ^^^id |string |N |7678592839487784712 |度量模板的唯一 ID。使用此 ID 可确定商品适用哪个度量标准模板。 |
   ^^^metric_value_module_infos |[]object |N | |度量模板下的指标值条目列表。每个对象表示卖家为模板中某个指标提交的取值。 |
   ^^^^id |string |N |7678592839487735560 |度量模板内指标项的唯一 ID。此 ID 用于标识所提交的取值属于哪个指标。 |
   ^^^^value |string |N |2026 |卖家为度量模板中指定指标项提供的取值。 |
   ^^^^unit_id |string |N |7678592839484720903 |指标值模块单位 ID。 |
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

对于所有其他地区，该字段不使用；如果在创建、编辑或部分编辑操作中传入，也不会被处理。
如果要覆盖默认的仓库配送选项，需应用于此商品的自定义配送选项 ID。要获取可用的选项 ID，请调用 [Get Warehouse Delivery Options](https://partner.tiktokshop.com/docv2/page/650aa46ebace3e02b75d9afa) 并传入 `scope=PRODUCT`。
**注意**：

* 将此字段留空以继承为仓库配置的默认配送选项。
* 如果使用 `save_mode=AS_DRAFT` 保存上架后草稿，则不支持该字段且不会保存。使用 Get Product 获取草稿时，取值将反映基础版本中的值。 |
   video |object |N | |用于展示商品的商品介绍或推广视频。

**建议**：

* Aspect ratio: 1:1
* 分辨率：HD 720p 或更高
* Duration: 20 - 60 seconds |
   ^id |string |Y |v09e40f40000cfu0ovhc77ub7fl97k4w |商品视频的 ID。
   先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传视频并获取对应的文件 ID。 |
   category_version |string |N |v1 |为该商品指定的类目树版本。
   基于地区的可能值：
* US 和 SEA 地区：`v2`，表示 7 级类目树。
   **重要**：对于 US 和 SEA 店铺，使用此接口时必须传入 `v2`。
* 其他地区：`v1`，表示 3 级类目树。
   Default: `v1` |
   manufacturer_ids |[]string |N |["172959296971220002"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9)。

**注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Category Rules API](6509c0febace3e02b74594a9) 检查要求。 |
responsible_person_ids |[]string |N |["172959296971220003"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1)。
**注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Category Rules API](6509c0febace3e02b74594a9) 检查要求。 |
listing_platforms |[]string |N |["TIKTOK_SHOP"] |商品上架的平台。
可能的值：

* TOKOPEDIA
* TIKTOK_SHOP
   仅适用于从 Tokopedia 迁移的卖家。

**重要**：该字段控制商品在上架平台上的可见性。

* 如果商品在两个平台上均在售，但请求只包含 1 个平台，则商品将在被省略的平台上停用并隐藏。
* 如果商品仅在 1 个平台在售，但请求包含另一个平台，则商品将在被省略的平台上停用并隐藏。
* 如果省略此数组，商品将送交当前活跃平台或上次请求中指定平台的审核。
* 如果要在两个平台上停用商品，请使用 Deactivate Product API。 |
   shipping_insurance_requirement |string |N |REQUIRED |对买家施加的商品运输保险购买要求。

可能的值：

* REQUIRED: 运输保险为强制购买，买家无法取消。
* OPTIONAL: 买家可以选择通过平台购买运输保险。
* NOT_SUPPORTED: 商品不支持运输保险。
   Default: OPTIONAL

仅当上架平台包含 TOKOPEDIA 时适用。 |
is_pre_owned |bool |N |false |标识商品是否为二手商品的标志。
仅当 TOKOPEDIA 是唯一上架平台时适用。
**注意**：要在 TikTok Shop 平台上架二手商品，请在 `category_id` 中填入指定二手商品类目之一的 ID（例如二手奢侈包袋、箱包和配饰）。 |
minimum_order_quantity |int |N |1 |商品的最低订购量。
有效范围： [1, 20]
仅适用于印尼市场及其他东南亚市场的部分卖家。如需了解如何获得此字段的访问权限，请联系您的客户经理。 |
replicated_products |[]object |N | |更新应同步到的本地市场副本列表。这是一个全量编辑端点，因此所有字段都将被同步。
针对每个目标市场：

* 该市场必须已存在副本。使用 Get Global Replicated Products 查看可用市场。
* 提交完整的目标市场 SKU 列表。列表中省略的现有目标 SKU ID 将被删除。
* 为每个目标 SKU 提供价格。库存也是必填项，但从 US 同步到 MX 时，目标库存为可选。

类目变更以及销售属性 ID 或名称变更必须同步到其他市场。对于这些变更，请提供来源 `seller_sku` 并在此对象中填写相应的详细信息；否则接口调用将失败。 |
^region |string |Y |US |要同步变更到的市场。该市场必须已存在副本。使用 Get Global Replicated Products 查看包含副本的市场。
可能的值：

* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MY: 马来西亚
* PH: 菲律宾
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南 |
   ^skus |[]object |N | |要同步到指定市场的 SKU。

**注意**：

* 必须传入所有现有 SKU。此处未列出的任何现有 SKU ID 都将导致对应 SKU 被删除。例如，如果该商品包含 5 个 SKU，而您只提供 2 个 SKU ID，则其余 3 个将被删除。
* 要创建新 SKU，请将 SKU ID 留空并提供 seller_sku。 |
   ^^id |string |N |1729592969712207001 |由 TikTok Shop 生成的 SKU ID。对于现有 SKU 请提供此值。 |
   ^^seller_sku |string |N |Color-Red-XM002 |用于管理 SKU 的内部代码/名称，对买家不可见。
   有效长度：
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 个字符
* 其他地区: 1-50 个字符
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 仅使用字母、数字、连字符 (-) 或下划线 (_)
* 其他地区: 不含空格的文本 |
   ^^price |object |Y | |SKU 在商品页面上折扣前显示的**本地展示价格**。 |
   ^^^currency |string |Y |USD |货币。 You must specify the local currency in the target market。
   可能的值：
* EUR：法国、德国、爱尔兰、意大利、西班牙
* GBP: 英国
* IDR: 印度尼西亚
* JPY: 日本ese
* MYR: 马来西亚
* PHP: 菲律宾
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^sale_price |string |Y |1.21 |折扣前商品页面上显示的 SKU 本地展示价格。
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。 |
   ^^inventory |[]object |N | |各仓库的 SKU 库存信息。该字段在其他地区为必填。但从 US 向 MX 同步商品时，MX 商品库存字段为可选。 |
   ^^^warehouse_id |string |N |7068517275539719942 |仓库 ID。从 [Get Warehouse List API](650aa418defece02be6e66b6) 或 Get Inventory Rules API 获取该值。该字段在其他地区为必填。但从 US 向 MX 同步商品时，MX 商品库存字段为可选。 |
   ^^^quantity |int |N |999 |仓库中可用的 SKU 数量。
   有效范围: [1, 999,999]。此字段在其他地区为必填。但从 US 向 MX 同步商品时，MX 商品库存字段为可选。 |
   ^inventory_mode |string |N |SHARED |定义复制后目标商品的库存模式。该参数支持两种模式：SHARED 和 EXCLUSIVE。
* SHARED：在此模式下，所有相互关联（共享）商品的库存必须严格一致；否则将返回错误。
* EXCLUSIVE：在此模式下，每个商品的库存可独立设置，互不影响。

Applicability:
此功能仅适用于欧盟市场。
Default Value:
如果留空，系统默认使用 EXCLUSIVE 模式。 |
subscribe_info_edit |object |N | |与指定商品关联的所有可编辑的 Save and Subscribe 促销信息。 |
^subscribe_status |string |N |ENABLED |用于表示指定商品是否有生效中的 Subscribe and Save 促销活动的枚举：

* ENABLED
* NOT_ENABLED

创建或修改订阅时，该字段为必填。 |
^discount_details |[]object |N | |所有 Save and Subscribe 折扣明细。 |
^^discount_level |string |N |REGULAR |表示折扣类型的枚举：

* REGULAR
* FIRST_ORDER
* RETENTION |
   ^^discount_value |int |N |10 |折扣值。值为 10 表示 10% 的折扣。 |
   shipping_template_id |string |N |7552764259994699538 |将绑定到商品的运费模板的标识符 |
   scheduled_sale |object |N | |商品的定时上架配置，包括是否启用定时上架及定时上架时间。 |
   ^is_enabled_scheduled_sale |bool |Y |false |该商品是否启用定时上架。如果为 `true`，则必须提供 `schedule_sale_time`。 |
   ^schedule_sale_time |int |Y |1768899145000 |定时上架时间，以毫秒级 Unix 时间戳表示；必须晚于当前时间且在 90 天内，当 is_enabled_scheduled_sale 为 true 时必填。 |
   locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。 Default: 您店铺的默认语言环境。 可能的值：
* `de-DE`
* `en-GB`
* `en-IE`
* `en-US`
* `es-ES`
* `es-MX`
* `fr-FR`
* `id-ID`
* `it-IT`
* `ja-JP`
* `ms-MY`
* `pt-BR`
* `th-TH`
* `vi-VN`
* `zh-CN` |
   auto_translate_enabled |bool |N |false |在需要多种语言的市场上架商品时是否自动翻译商品内容。不需要自动翻译时请省略此字段。 |
   search_terms |[]string |N |["sneakers","running shoes","athletic"] |搜索词（ST 词）。 ST words will not be displayed to consumers; they are only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words are consistent with the product description, with a maximum of 15 terms and a total of no more than 250 characters。 |
   key_product_features |[]string |N |["Breathable mesh upper", "Cushioned foam midsole"] |关键商品特性。 They will be displayed in the Product highlight module on the product detail page and will be used by search engines to increase your search weight for more traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500。 |
   inventory_mode |string |N |SHARED |定义复制后源商品的库存模式。该参数支持两种模式：SHARED 和 EXCLUSIVE。
* SHARED：在此模式下，所有相互关联（共享）商品的库存必须严格一致；否则将返回错误。
* EXCLUSIVE：在此模式下，每个商品的库存可独立设置，互不影响。

Applicability:
此功能仅适用于欧盟市场。
Default Value:
如果留空，系统默认使用 EXCLUSIVE 模式。 |
product_tag_operations |[]object |N | |用于启用或停用 `AUCTION` 商品标签的旧版操作。如果提供了 `selling_format`，则优先于该字段。 |
^product_tag |string |Y |AUCTION |可能的值： AUCTION |
^enable |bool |Y |false |是否启用指定的商品标签。设为 `true` 启用 `AUCTION` 标签，设为 `false` 将其禁用。 |
purchase_order_quantity_limit |object |N | |应用于商品每个 SKU 的购买数量限制，包括每笔订单的最大数量和跨订单的累计数量。 |
^maximum_order_quantity |int |N |2 |每笔订单中每个
商品款式（SKU）。
例如: 如果为含 5 个变体（SKU）的商品设置最大限购 2 件，买家每个 SKU 最多可购买 2 件，每笔订单合计最多 10 件。
设置为 0 表示清除 |
^cumulative_order_quantity |int |N |20 |· 客户可购买某商品的
限购生效期间，跨所有订单的款式（SKU）数量。清除限购将重置其历史购买量，允许其按新限购再次购买；若未设置限购，则不受限制。
• 例如，如果为含 5 个款式（SKU）的商品设置总限购 2，则客户每个 SKU 最多可购买 2 件，多次购买合计最多 10 件。之后，除非清除限购，否则无法继续购买。总限购必须大于或等于最大值
limit.
设置为 0 表示清除 |
selling_format |string |Y |FIXED_PRICE_AND_LIVE_AUCTION |选择固定价格或固定价格加 LIVE 拍卖。默认选择固定价格。LIVE 拍卖需要起拍价。可选值：FIXED_PRICE, FIXED_PRICE_AND_LIVE_AUCTION。 |
is_live_quick |bool |N |false |false — 常规商品
true — LIVE_QUICK 商品。只有具有所需权限的卖家才能创建 LIVE_QUICK 商品。
默认值：false |
is_blind_box |bool |N |false |该商品是否为盲盒或福袋。例如：PopMart |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202509/products/1729409636071801988?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"save_mode":"AS_DRAFT","description":" \u003cp\u003ePlease compare above detailed size with your measurement before purchase.\u003c/p\u003e\n\u003cul\u003e \n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" width='100' height='100' /\u003e","category_id":"600001","brand_id":"7082427311584347905","main_images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"skus":[{"id":"1729592969712207000","sales_attributes":[{"id":"100089","name":"Specification","value_id":"1729592969712401100","value_name":"XL","sku_img":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"supplementary_sku_images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}]}],"seller_sku":"Color-Red-XM001","price":{"amount":"1.21","currency":"USD","sale_price":"1.21","starting_bid_price":"2.3"},"external_sku_id":"1729592969712207012","identifier_code":{"code":"12345678901234","type":"GTIN"},"inventory":[{"warehouse_id":"7068517275539719942","quantity":999,"backorder_quantity":888,"handling_time":5}],"combined_skus":[{"product_id":"1729582718312380123","sku_id":"2729382476852921560","sku_count":2}],"sku_unit_count":"100.00","external_urls":["https://example.com/path1","https://example.com/path2"],"extra_identifier_codes":["00012345678905","9780596520687"],"pre_sale":{"type":"PRE_ORDER","fulfillment_type":{"handling_duration_days":7,"release_date":1619611761&rbrace;&rbrace;,"list_price":{"amount":"1","currency":"USD"},"external_list_prices":[{"source":"SHOPIFY_COMPARE_AT_PRICE","amount":"1","currency":"USD"}],"fees":[{"type":"PFAND","amount":"1.01","additional_attribute":"SINGLE_USE"}],"sku_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"sku_weight":{"value":"1.32","unit":"KILOGRAM"&rbrace;&rbrace;],"title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks\n","is_cod_allowed":false,"certifications":[{"id":"7182427311584347905","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"files":[{"id":"v09e40f40000cfu0ovhc77ub7fl97k4w","name":"Certificate.pdf","format":"PDF"}],"expiration_date":1741235456}],"package_weight":{"value":"1.32","unit":"KILOGRAM"},"product_attributes":[{"id":"100392","values":[{"id":"1001533","name":"Birthday","metric_standard_info":{"id":"7678592839487784712","metric_value_module_infos":[{"id":"7678592839487735560","value":"2026","unit_id":"7678592839484720903"}]&rbrace;&rbrace;]}],"size_chart":{"image":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"template":{"id":"7267563252536723205"&rbrace;&rbrace;,"package_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"external_product_id":"172959296971220002","delivery_option_ids":["1729592969712203232"],"video":{"id":"v09e40f40000cfu0ovhc77ub7fl97k4w"},"category_version":"v1","manufacturer_ids":["172959296971220002"],"responsible_person_ids":["172959296971220003"],"listing_platforms":["TIKTOK_SHOP"],"shipping_insurance_requirement":"REQUIRED","is_pre_owned":false,"minimum_order_quantity":1,"replicated_products":[{"region":"US","skus":[{"id":"1729592969712207001","seller_sku":"Color-Red-XM002","price":{"currency":"USD","sale_price":"1.21"},"inventory":[{"warehouse_id":"7068517275539719942","quantity":999}]}],"inventory_mode":"SHARED"}],"subscribe_info_edit":{"subscribe_status":"ENABLED","discount_details":[{"discount_level":"REGULAR","discount_value":10}]},"shipping_template_id":"7552764259994699538","scheduled_sale":{"is_enabled_scheduled_sale":false,"schedule_sale_time":1768899145000},"locale":"en-US","auto_translate_enabled":false,"search_terms":["sneakers","running shoes","athletic"],"key_product_features":["Breathable mesh upper","Cushioned foam midsole"],"inventory_mode":"SHARED","product_tag_operations":[{"product_tag":"AUCTION","enable":false}],"purchase_order_quantity_limit":{"maximum_order_quantity":2,"cumulative_order_quantity":20},"selling_format":"FIXED_PRICE_AND_LIVE_AUCTION","is_live_quick":false,"is_blind_box":false}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_id | string | 1729592969712207008 | TikTok Shop 生成的商品 ID。 |
| ^skus | []object |  | 用于标识商品不同变体的 SKU（库存单位）列表。 |
| ^^id | string | 1729592969712207012 | TikTok Shop 生成的 SKU ID。一个商品可包含多个 SKU ID。 |
| ^^seller_sku | string | Color-Red-XM001 | 用于管理 SKU 的内部代码/名称，对买家不可见。 |
| 有效长度： |  |  |  |

* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 个字符
* 其他地区: 1-50 个字符
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 仅使用字母、数字、连字符 (-) 或下划线 (_)
* 其他地区: 不含空格的文本 |
   ^^sales_attributes |[]object | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。 |
   ^^^id |string |100000 |销售属性 ID。
   如果请求中包含自定义销售属性名称，则此为新生成的 ID。 |
   ^^^value_id |string |1729592969712207123 |销售属性值 ID。
   如果请求中包含自定义销售属性值名称，则此为新生成的 ID。 |
   ^^external_sku_id |string |1729592969712207234 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联 SKU。 |
   ^^fees |[]object | |根据 TikTok Shop 政策该商品所需的费用。仅部分商品类目需要费用，请从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取相关要求。 |
   ^^^type |string |PFAND |费用类型。
   可能的值：PFAND |
   ^^^amount |string |1.01 |费用金额。
   有效范围：
* PFAND: [0.00 - 6300.00] |
   ^^^additional_attribute |string |SINGLE_USE |提供费用附加上下文的可选属性。接受的值可能因费用类型和市场而异。

Pfand 的可能值：

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |
   ^warnings |[]object | |API 调用者需要特别关注的警告信息。 |
   ^^message |string |The [brand_id]:123 field is incorrect and has been automatically cleared by the system. Reason: [Brand does not exist]. You can edit it later. |API 调用方应查看并在适用时处理的警告消息。它的出现本身并不表示编辑商品操作失败。 |
   ^audit |object | |商品审核信息。
   **注意**: 仅适用于在 TikTok Shop 上架的商品。不适用于仅在 Tokopedia 上架的商品。 |
   ^^status |string |AUDITING |商品审核状态。
   可能的值：
* NONE：商品不适用审核，因为它尚未提交在本平台上架，或处于草稿、冻结或已停用状态。
* AUDITING：商品正在审核中。
* APPROVED: 如果只编辑了已批准商品的 `price` 或 `inventory` 字段，商品仍保持批准状态，新信息将立即在平台发布。 |

# 响应示例
```json
{"code":0,"data":{"product_id":"1729592969712207008","skus":[{"id":"1729592969712207012","seller_sku":"Color-Red-XM001","sales_attributes":[{"id":"100000","value_id":"1729592969712207123"}],"external_sku_id":"1729592969712207234","fees":[{"type":"PFAND","amount":"1.01","additional_attribute":"SINGLE_USE"}]}],"warnings":[{"message":"The [brand_id]:123 field is incorrect and has been automatically cleared by the system. Reason: [Brand does not exist]. You can edit it later."}],"audit":{"status":"AUDITING"&rbrace;&rbrace;,"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019006 | product description is invalid |
| 12019011 | product package weight is invalid |
| 12019012 | product package size is invalid |
| 12019013 | brand id is invalid |
| 12019019 | sale property is invalid |
| 12019022 | SKU 必须包含有效仓库。 |
| 12019056 | sku not allow add |
| 12019057 | sku not allow delete |
| 12019061 | Product weight or dimensions unit does not support the imperial units on non-US local products. |
| 12019095 | `pre_sale.fulfillment_type` is missing or empty. |
| 12019096 | The value for `pre_sale.type` is missing. |
| 12019097 | `pre_sale.fulfillment_type.release_date` 必须设置为非零值。 |
| 12019098 | `pre_sale.fulfillment_type.handling_duration_days` 必须设置为非零值。 |
| 12019100 | All SKUs of a product must have the same `pre_sale.type`. Do not assign different values. |
| 12019215 | deposit balance is not enough |
| 12052002 | Incorrect category format |
| 12052003 | Incorrect parcel height format |
| 12052004 | Incorrect parcel width format |
| 12052005 | Incorrect parcel length format |
| 12052013 | The product description cannot exceed maximum characters |
| 12052015 | The product description is required |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052025 | The category is invalid |
| 12052026 | Brand does not exist |
| 12052028 | Main product image is required |
| 12052032 | 商品不存在 |
| 12052034 | This product doesn't belong to this shop |
| 12052037 | 无法更新库存。可能原因: |

* 库存自动分配，无法手动修改
* 提供的仓库 ID 不正确
* 缺少仓库 ID（必须包含存放该商品的所有仓库） |
   12052038 |Product price locked due to ongoing promotion. |
   12052048 |您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
   12052050 |A single product cannot have more than 100 different SKUs |
   12052051 |The product name exceed max limit characters |
   12052054 |The seller SKU text length cannot exceed max limit characters |
   12052055 |The SKU inventory quantity for the warehouse must be within allowed limits. |
   12052056 |The num of image in description cannot exceed max limit |
   12052073 |The product price is invalid |
   12052084 |The provided currency is not available for this shop/region. |
   12052092 |product sale price is invalid |
   12052094 |No multiple warehouse permission |
   12052095 |Warehouse information parsing error |
   12052096 |Unable to update the price for SKUs with no warehouse. Assign a warehouse and try again. |
   12052097 |The warehouse does not exist |
   12052104 |property is required |
   12052105 |required qualification miss |
   12052115 |seller has no warehouse |
   12052116 |product package size is invalid |
   12052128 |Size chart not found |
   12052141 |please edit stock from global |
   12052144 |platform warehouse not support to edit |
   12052151 |product property value contain restricted words |
   12052152 |sale property name contains restricted words |
   12052153 |sale property value contains restricted words |
   12052158 |category unable to change |
   12052159 |unique item total quantity must be one |
   12052160 |sku count must be one and disable variables |
   12052162 |unique item sku count must be one and disable varialbes |
   12052163 |The gift product are not allowed to be edited |
   12052181 |The package weight of the product can not be zero. |
   12052182 |The '&lbrace;&lbrace;sub_property_name&rbrace;&rbrace;' field is required as you've selected '&lbrace;&lbrace;parent_property_value&rbrace;&rbrace;' for '&lbrace;&lbrace;parent_property_name&rbrace;&rbrace;'. |
   12052183 |The '&lbrace;&lbrace;sub_property_name&rbrace;&rbrace;' field should be left empty as you've selected '&lbrace;&lbrace;parent_property_value&rbrace;&rbrace;' for '&lbrace;&lbrace;parent_property_name&rbrace;&rbrace;'. |
   12052200 |brand is expired |
   12052201 |You are not authorized to sell this brand in this category. To do so, apply through the Qualification Center in Seller Center. |
   12052207 |receipt brand not support warehouse |
   12052208 |A brand authorization is required to publish this listing. |
   12052217 |所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
   12052220 |This category is prohibited or unsupported on TikTok Shop. Select another category. |
   12052221 |Only whitelisted sellers are permitted to trade under current category |
   12052222 |category do not support cod |
   12052223 |This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
   12052225 |You are not authorized to sell in this category because it does not fall under your shop's main category. Contact your account manager for help or select another category. |
   12052226 |This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
   12052227 |the category is unauthorized or unavailable |
   12052230 |Category version and categoryID are not matched. |
   12052235 |The format of url is invalid |
   12052238 |The length of the url is greater than 200 |
   12052240 |Do not support custom property. |
   12052241 |attribute name or attribute id is empty. |
   12052242 |The attribute name characters cannot exceed max_limit |
   12052243 |The product attribute or sale attribute name characters contain Chinese. |
   12052244 |The attribute name duplicate. |
   12052245 |The product attributes contained invalid characters. Please modify and re-submit. |
   12052246 |The &lbrace;&lbrace;property_type&rbrace;&rbrace; not support multi selected, attribute id is :&lbrace;&lbrace;property_id&rbrace;&rbrace;. |
   12052247 |Do not support custom product attribute. |
   12052248 |The &lbrace;&lbrace;property_type&rbrace;&rbrace; value name or attribute value id is empty. |
   12052249 |The &lbrace;&lbrace;property_type&rbrace;&rbrace; value name characters cannot exceed &lbrace;&lbrace;max_limit&rbrace;&rbrace;, attribute value name is :&lbrace;&lbrace;property_value_name&rbrace;&rbrace;. |
   12052250 |The &lbrace;&lbrace;property_type&rbrace;&rbrace; value name characters contain Chinese. |
   12052251 |Duplicated attribute values found for an attribute. Remove or modify the duplicated value. |
   12052253 |Duplicate attribute value id |
   12052254 |Duplicate attribute id |
   12052256 |The &lbrace;&lbrace;property_name&rbrace;&rbrace; value need to be positive integers or positive decimals . |
   12052260 |商品 ID 不存在 |
   12052261 |product name is empty |
   12052262 |Chinese characters are not supported in product name |
   12052263 |product name prefix illegal |
   12052273 |After the pre-sale product has been onlive product, the pre-sale info cannot be modified. |
   12052275 |sku's mto day is invalid |
   12052278 |seller does not support make to order |
   12052282 |Product manufacturer is required. |
   12052284 |Manufacturer ID &lbrace;&lbrace;manufacturer_id&rbrace;&rbrace; is not found |
   12052285 |Manufacturer ID &lbrace;&lbrace;manufacturer_id&rbrace;&rbrace; is not associated with the seller |
   12052287 |Product responsible person is required |
   12052289 |Responsible person ID &lbrace;&lbrace;rp_id&rbrace;&rbrace; is not found |
   12052294 |The format of the extra identification code is incorrect. |
   12052300 |product main image uri illegal |
   12052301 |Width and length of main image must be at least &lbrace;&lbrace;min_limit&rbrace;&rbrace;, check uri &lbrace;&lbrace;uri&rbrace;&rbrace; |
   12052302 |The main images size exceed limit. |
   12052304 |Main product image format not support. |
   12052305 |The main images aspect ratio cannot exceed max limit. |
   12052306 |main product images count exceed limit |
   12052307 |skus in the lottery cannot be deleted |
   12052308 |There's an ongoing appeal. If you wish to edit product details, please revoke the appeal first. |
   12052310 |The futures information filled in by the seller does not meet the requirements. |
   12052311 |The number of backorder product exceeds the limit max_num, or the proportion of backorder product exceeds the limit max_ratio |
   12052314 |Standard product cannot be converted to MTO product |
   12052315 |Standard product cannot be converted to preorder product |
   12052316 |product second hand not applicable in this sale platform |
   12052317 |purchase order quantity not support |
   12052319 |maximum order quantity smaller than minimum order quantity |
   12052324 |Product description image file format is not supported |
   12052329 |A pre-order product can't be changed to a regular product |
   12052330 |商品不支持在指定销售平台上架 |
   12052332 |店铺集成期间卖家中心被锁定，仅允许编辑库存和价格 |
   12052340 |product description image uri illegal |
   12052341 |The description images size cannot exceed limit. |
   12052342 |The description images space cannot exceed limit. |
   12052343 |Product description image format not support. |
   12052344 |The product description html syntax with error |
   12052345 |The product description html tag not support. |
   12052346 |The product description has Chinese characters |
   12052348 |The product description html tag required attribute is miss. |
   12052349 |The product description html tag not support nest. |
   12052350 |The product description html tag contain illegal attribute. |
   12052352 |The product description nest exceeding limit |
   12052357 |'supplementary_sku_images' is only allowed when 'sku_img' is specified. Add an image to 'sku_img' and try again. |
   12052359 |save subscribe not support |
   12052360 |The video id is not exist. |
   12052361 |This base unit value count is not supported. The supported base unit values can be obtained from the Get Attribute API. |
   12052362 |SKU unit count is required. |
   12052364 |The warehouse is unavailable because this product cannot be shipped to the target market from this warehouse. |
   12052365 |The manufacturer lacks language version information for this market. |
   12052371 |Auction product is bidding when it is not supported to change product info |
   12052372 |Generate EU energy label image failed |
   12052375 |product list price is invalid |
   12052376 |list price not support |
   12052382 |Can't edit Dilayani Tokopedia warehouse quantity |
   12052383 |product list price exceed limit |
   12052385 |Please enter valid certificate expiration date |
   12052393 |Product locked for Promotion and stock can't be updated below current stock |
   12052402 |seller shipping template is empty |
   12052403 |The warehouse does not support fulfillment for the current shop. |
   12052404 |multi-warehouse not support customize logistics service |
   12052405 |The warehouse has not opened the subscribed logistics service |
   12052420 |warehouse didn't set logistics service |
   12052424 |Missing 'sale price' value |
   12052446 |Category is not open in this market |
   12052465 |warehouse is unavailable for eu gpr product |
   12052490 |The handling time must be within the allowed limits. |
   12052503 |If the inventory allocation mode is SHARED, the inventory quantity must be the same across all SKUs. |
   12052508 |The SKU ID in `replicated_products` is invalid and cannot be found. |
   12052509 |Missing seller_sku in `replicated_products`. You must indicate the seller_sku for all new SKUs. |
   12052510 |No matching seller_sku found in the source product. Ensure you indicate the seller_sku in both `skus.seller_sku` and `replicated_products.skus.seller_sku`. |
   12052511 |Missing SKU details in `replicated_products`. You must complete the SKU details. |
   12052512 |No replicas exist for this product. You can replicate the product first by using the Replicate Product endpoint. |
   12052513 |No replicas exist for this product in the stated region. You can replicate the product first by using the Replicate Product endpoint. |
   12052514 |Missing regions in `replicated_products`. The category was changed, therefore you must sync the product to all other markets where replicas exist. |
   12052515 |Missing regions in `replicated_products`. The sales attributes were changed, therefore you must sync the product to all other markets where replicas exist. |
   12052516 |Missing inventory details. You must include all warehouse IDs assigned to the SKU, along with the respective quantity. Do not omit any or add unrelated warehouses. |
   12052520 |product sale property image uri illegal |
   12052521 |The sale property images size over limit. |
   12052522 |Product sale property image is required |
   12052523 |Product sale property image format not support. |
   12052524 |The sale property image aspect ratio invalid |
   12052525 |The attribute max num cannot exceed 3. |
   12052526 |The attribute value max num over limit. |
   12052527 |The sale attribute id not exist. |
   12052528 |You can add images to only 1 product variation, which will serve as the primary variation for display in the product options gallery. |
   12052529 |The property value id not exist. |
   12052530 |The warehouse ' &lbrace;&lbrace;warehouse ID&rbrace;&rbrace; ' does not belong to this shop/seller. |
   12052531 |The warehouse is disabled. |
   12052532 |该仓库非配送仓库 |
   12052533 |不允许移除、新增或更改仓库。请为 SKU 指定原始仓库。 |
   12052534 |warehouse unable to delete |
   12052535 |Couldn't publish this product as you haven't set the return warehouse for your shop. Add the return warehouse information on TikTok Shop Seller Center first and try again. |
   12052550 |SKU property must contain all properties |
   12052553 |Sku id duplicate |
   12052554 |sku name contain Chinese characters |
   12052557 |The SKU ID does not belong to the product. |
   12052558 |Number of product skus exceed limit. |
   12052559 |The product with duplicate default sku. |
   12052560 |The SKU contains duplicate sales attribute. |
   12052570 |product price exceed limit |
   12052571 |Missing price for SKU(s) |
   12052572 |the sale price is invalid |
   12052574 |unit price config is invalid |
   12052592 |Identifier code already entered, cannot enter the same code twice |
   12052593 |The identifier code cannot be changed once be submitted |
   12052650 |product qualification image uri illegal |
   12052651 |The qualification images size over limit. |
   12052655 |qualification id not exist |
   12052656 |qualification id duplicate |
   12052657 |qualification image and pdf file is out of limit. |
   12052658 |product qualification file uri illegal |
   12052670 |The size chart image URI is invalid. Note: API users must use the URI generated by the Upload Product Image API. |
   12052671 |The sizechart images size over limit. |
   12052673 |Product sizechart image is required |
   12052700 |卖家不活跃。 |
   12052701 |do not support cross-boarder seller create local product directly |
   12052702 |seller does not support pre-order |
   12052703 |Invalid seller tax number |
   12052704 |卖家 ID 不存在 |
   12052706 |The minimum sales quantity should not be exceed limit |
   12052707 |Setting minimum sales quantity is not supported |
   12052712 |sku's pre_order is invalid |
   12052805 |Bundle does not support adding this product type |
   12052815 |product in bundle deal cannot set minimum sale quantity |
   12052832 |The sub-SKU coefficient associated with each combo SKU cannot exceed &lbrace;&lbrace;max_limit&rbrace;&rbrace;, and cannot less &lbrace;&lbrace;min_limit&rbrace;&rbrace;. |
   12052834 |The number of combo sku associated with a sku cannot exceed limit. |
   12052835 |Sub product ID not exist |
   12052836 |The category of the combo is inconsistent with the category of the main sub-product. |
   12052838 |The first-level categories of the sub-products in the combo are inconsistent |
   12052841 |The sub-sku relationship corresponding to different combo sku cannot be duplicated. |
   12052843 |The main sub-product in the combo cannot be changed |
   12052844 |The sub-sku is not in the sub-product |
   12052846 |combo does not support adding this product type |
   12052847 |The combo sku relationship cannot be changed |
   12052850 |The stock of combo does not support being edited. |
   12052853 |The sale property of combo mismatch. |
   12052857 |Combined products and normal products cannot be converted to each other. |
   12052859 |When the combined SKU is only associated with one sub-SKU, the coefficient of this sub-SKU cannot be less than 2. |
   12052863 |All SKU of a combined product need to be the combined SKU. |
   12052864 |Unable to add deactivated SKUs to the combined product. |
   12052881 |identity 内部错误 |
   36009003 |内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
   12052901 |商品当前状态不支持此操作。请更改商品状态后重试。 |
   12052902 |The SKU list is empty. Either omit the list entirely, or provide all required details. |
   12052910 |输入参数无效。请参阅 API 文档了解详情。 |
   12052915 |package weight unit and dimension unit miss match. |
   12052921 |Couldn't edit the inventory quantity because this product shares the inventory with the source shop |
   12052922 |edit fields limit |
   12052930 |Seller SKU is required |
   12052931 |The title must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
   12052932 |The description must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
   12052933 |Sales attribute names must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
   12052934 |Sales attribute value names must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
   12052935 |Product attribute value names must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
   12052936 |Seller SKU format invalid. SKU name must contain 6 - 50 characters and use alphabets, numbers, hyphens (-), or underscores (_) only. |
   12052994 |seller is not toko seller |


