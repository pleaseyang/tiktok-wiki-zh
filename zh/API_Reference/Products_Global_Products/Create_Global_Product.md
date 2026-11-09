# 创建全球商品

# 路径：/product/202309/global_products
# 方法：[POST]
# 功能描述
创建全球商品，在卖家所在国家/地区以外的一个或多个店铺中销售。
你只能在 `AVAILABLE` 商品类目中创建全球商品。对于其它类目，请联系你的客户经理寻求帮助。创建商品后，使用 [Publish Global Product API](https://partner.tiktokshop.com/docv2/page/650a64d6defece02be678fd6) 在所需市场发布并翻译该商品。
**关键概念**：全球商品是跨境卖家创建的、用于在其所属国家以外的店铺销售的商品。借助全球商品，在多个市场运营的跨境卖家无需为每个店铺单独创建相同商品。相反，他们只需创建一个全球商品，即可将其发布并同步到所有店铺，从而简化跨市场的商品管理。
**注意**：

* 此 API 仅适用于欧盟境内卖家和全球卖家。若要创建并上架仅在本地店铺销售的本地商品，请改用 [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a)。
* 每天可上架的商品数量可能有限制。建议优先创建关键商品，以确保其得以发布。您可在 Seller Center 首页查看上架额度。
* 商品内容中使用的语言必须与目标市场的语言一致（例如，不要使用中文），否则上架将失败或被拒绝。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
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
| title | string | Y | Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks |  |
| 商品标题。 |  |  |  |  |
| 标题长度： |  |  |  |  |

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* MX:[1,300]
* 其他地区: [25, 255] |
   description |string |Y | |HTML 格式的商品描述。

**注意**：

* 内容必须符合 [HTML 语法](https://html.spec.whatwg.org/)。系统接受所有 HTML 标签，但为优化在 TikTok Shop 商品详情页上的展示，会自动将某些标签转换为其他格式，例如将 `<table>` 标签渲染为图片。
* 最大长度：10,000 个字符。
* 图片规范：必须使用 [TikTok Shop image URLs](6509df95defece02be598a22)。最多 30 个 `<img>` 标签，每个小于 4000px，并带 `src`、`width` 和 `height` 属性。

**建议**：

* 如果您正在从其他平台同步预先存在的描述，请在此处包含完整的 HTML 源代码描述。
* 提供详细描述，最好超过 300 个字符。
* 包含 3-5 个关键卖点，每个不超过 250 个字符，并附带支持图片。
* 图片尺寸使用 1600x1600 像素。 |
   category_id |string |Y |600001 |该商品所属类目的 ID。
* 必须是与 `category_version` 属性中指定的类目树类型相对应的叶子类目。
* 必须是主类目（在 [Get Global Categories API](650a03f8f1fd3102b91b338a) 中 `categories.permission_statuses=AVAILABLE`）。
   **注意**： 有关商品分类限制的信息，请参考 TikTok Shop Academy。 |
   brand_id |string |N |7082427311584347905 |此商品的品牌 ID。

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
   skus |[]object |Y | |用于标识商品不同变体的全球库存单位 (SKUs) 列表。

**注意**：

* EU、JP、UK、US 的最大 SKU 数：300
* 其他地区的最大 SKU 数量：100

**建议**：将最重要的变体放在数组开头。 |
^global_quantity |int |N |999 |全球所有店铺的 SKU 库存总量。
商品首次发布时，各本地店铺的库存会自动计算。发布后，此全局数量无法手动更改。您只能修改各本地店铺的库存数量。 |
^sales_attributes |[]object |N | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。
**注意**：

* 如果只有 1 个 SKU，则可以省略此对象。否则为**必填**。
* 每个商品最多只能有 3 种销售属性类型。
* 每个 SKU 必须包含相同数量和类型的销售属性。 例如，不能一个 SKU 只有颜色属性，而另一个 SKU 同时有颜色和尺码属性。
* 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。
* `id/name` 与 `value_id/value_name` 组合在每个 SKU 中必须唯一。例如，不能在不同 SKU 中重复 `"name": "Color"`、`"value_name": "Red"`。 |
   ^^id |string |N |100089 |内置销售属性的 ID，从 [Get Global Attributes API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a)。 |
   ^^name |string |N |Color |当内置属性无法满足你的需求时，可自定义销售属性名称。TikTok Shop 在创建全球商品时生成 ID，并在 `data.global_skus[].sales_attributes[].id` 中返回。

**注意**：

* 不要包含敏感字符。
* 最大长度：20 个字符 |
   ^^value_id |string |N |1729592969712207000
   |内置销售属性值的 ID，从 [Get Global Attributes API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a)。 |
   ^^value_name |string |N |Red |当内置值无法满足你的需求时，可自定义销售属性值。TikTok Shop 在创建全球商品时生成 ID，并在 `data.global_skus[].sales_attributes[].value_id` 中返回。

**注意**：

* 同一属性下不允许重复。
* 最大长度：50 个字符。
* 仅支持字母和数字。 |
   ^^sku_img |object |N | |为 SKU 展示的图片。

您只能为 1 种销售属性附加图片，并且必须为所选属性的每个取值附加一张图片。例如，如果商品有 2 种颜色和 3 种尺码，您可以选择为颜色销售属性或尺码销售属性附加图片。如果选择为颜色附加图片，则必须附加 2 张图片，每种颜色一张。 |
^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe
|图片的 URI。
通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=ATTRIBUTE_IMAGE` 获取此 URI。 |
^seller_sku |string |N |XL-COLOR-RED-001 |用于管理 SKU 的内部代码/名称，对买家不可见。

* 有效长度： 1-50 characters
* 格式：不含空格的文本 |
   ^price |object |Y | |该 SKU 的**全球统一税前**价格，作为计算不同市场本地价格的基准。

**注意**：

* 发布后，此价格将根据各市场汇率以及配送费用、税费等适用费用，自动换算为本地税前价格和本地展示价格。
* 自动转换将排除使用中国仓库的 JP 和 US 店铺。 |
   ^^amount |string |Y |999 |价格金额。
   Max: 99,999,999.99 |
   ^^currency |string |Y |USD |货币。
   可能的值：
* `USD`：适用于全球卖家
* `EUR`：适用于欧盟境内卖家 |
   ^identifier_code |object |N | |根据国际标准化法规（如 GTIN）分配给商品的受管标识码，以确保商品在各种平台和系统中可普遍识别。

**重要**：该对象及其取值仅可在商品处于 DRAFT 状态时修改。一旦提交审核，则不允许更改。请谨慎设置取值。 |
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
   ^inventory |[]object |N | |各仓库的 SKU 库存信息。
   如果在 Seller Center 启用了多仓库，则必须提供每个仓库的库存明细。
   Max count: 50

**注意**: 如果为每个仓库提供了库存明细，`global_quantity` 将不生效。
|
^^global_warehouse_id |string |Y |7068517275539719942 |存放该 SKU 的全球仓库 ID。
从 [Get Global Seller Warehouse API](https://partner.tiktokshop.com/docv2/page/650aa3f0defece02be6e5ffb) 获取卖家可用的全球仓库列表。 |
^^quantity |int |Y |999 |仓库中可用的 SKU 数量。
有效范围：[1, 99,999] |
^sku_unit_count |string |N |1 |SKU 代表的商品总量/体积。
例如，如果 SKU 代表 500 毫升水，则当单位类型定义为 ml 时，此值将为 500。
有效范围：[0.01, 99,999.9999]
仅适用于欧盟市场。
**注意**：

* 这主要用于计算 SKU 的单价，仅当您希望展示单价以便于跨不同商品和包装尺寸进行价格比较时才需要。
* 单价 = 售价/(SKU 单位数量/基本单位数量)。因此，如需获取单价，还需要定义 "base unit count" 和 "unit type" 商品属性。可通过 [Get Global Attributes API](650a0483c16ffe02b8dfc80a) 获取这些商品属性的相关信息。单价随后会在 [Get Global Product API](6509e2b0bace3e02b7490c96) 中返回。 |
   ^extra_identifier_codes |[]string |N |["10000000000000"] |如果 SKU 属于虚拟组合装（包含多个独立 SKU），可在此为组合装中包含的 SKU 添加最多 10 个附加标识符代码。

**Format**:
GTIN: 14 位数字
EAN: 8、13 或 14 位数字
UPC: 12 位数字
ISBN：13 位数字，或以大写 `X` 结尾的 9 位数字
**注意**：

* 仅适用于欧盟市场。
* 标识码必须在每个 SKU 中唯一，不允许重复。 |
   ^external_global_sku_id |string |N |1234567890 |在外部电商平台中使用的外部标识符。 This is used to associate the global SKU between TikTok Shop and the external ecommerce platform。
   最大长度：999 个字符 |
   package_weight |object |Y | |商品包装的重量。

**注意**：

* 提供包装商品后测量的重量。
* 该值会影响配送费用，因此务必确保尺寸测量准确。任何差异都可能导致额外的配送费用。
* 如果基于重量的费用更高，则包装重量将在费用计算中优先于包装尺寸。 |
   ^value |string |Y |1.31 |包裹重量，必须为正数且最多保留 3 位小数。 |
   ^unit |string |Y |KILOGRAM |包装重量的单位。 Only `KILOGRAM` is supported。 |
   certifications |[]object |N | |您的商品的认证列表。
   最大数量：10

根据 TikTok Shop 指南，某些受限商品类目需要提供认证。请通过 [Get Global Category Rules API](https://partner.tiktokshop.com/docv2/page/650a056df1fd3102b91b5b8e) 获取您商品的认证要求。有关商品类目限制的信息，请参阅 [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy)。 |
^id |string |Y |7182427311584347905 |用于标识商品分类所需认证类型的 ID。
从 [Get Global Category Rules API](https://partner.tiktokshop.com/docv2/page/650a056df1fd3102b91b5b8e) 获取该值。 |
^images |[]object |N | |认证相关图片列表。 |
^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CERTIFICATION_IMAGE` 获取此 URI。 |
^files |[]object |N | |认证相关文件列表。 |
^^id |string |Y |v09ea0g40000cj91373c77u3mid3g1s0 |认证文件的 ID。
先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传文件并获取对应的文件 ID。 |
^^name |string |Y |SNI.PDF |认证文件的名称，包括文件扩展名。 |
^^format |string |Y |PDF |认证文件的格式。仅支持 PDF。 |
package_dimensions |object |N | |商品包装的尺寸。
**注意**：

* 提供包装商品后测量的尺寸。
* 这些值会影响配送费用，因此务必确保尺寸准确。任何差异都可能导致额外的配送费用。 |
   ^length |string |Y |10 |包装长度。正整数。 |
   ^width |string |Y |10 |包装宽度。正整数。 |
   ^height |string |Y |10 |包装高度。正整数。 |
   ^unit |string |Y |CENTIMETER |包裹尺寸的单位。仅支持 `CENTIMETER`。 |
   product_attributes |[]object |N | |描述商品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。

**重要**：可用属性由系统根据商品所属类目确定，其中部分为必填。您必须提供 [Get Global Attributes API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a) 响应中标记为 `is_required` 的商品属性。 |
^id |string |Y |100392 |商品属性的 ID，从 [Get Global Attributes API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a)。 |
^values |[]object |Y | |商品属性的可选值列表。
最大数量：US 为 300；其他地区为 100。
**注意**： 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。 |
^^id |string |N |1001533 |内置商品属性值的 ID，从 [Get Global Attributes API](https://partner.tiktokshop.com/docv2/page/650a0483c16ffe02b8dfc80a)。 |
^^name |string |N |Steel |如果内置值不满足需求，可自定义商品属性值。系统将在上架后自动生成 ID。
**注意**：

* 同一属性下不允许重复。
* 最大长度：2000 个字符
* 仅支持字母和数字。 |
   size_chart |object |N | |商品的测量详情，帮助买家找到合适的尺码。

**注意**：

* 对于某些商品分类，可能需要或不支持尺码表。 Use the [Get Global Category Rules API](https://partner.tiktokshop.com/docv2/page/650a056df1fd3102b91b5b8e) 检查要求。
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
      video |object |N | |用于展示商品的商品介绍或推广视频。

**建议**：

* Aspect ratio: 1:1
* 分辨率：HD 720p 或更高
* Duration: 20 - 60 seconds |
   ^id |string |Y |v09e40f40000cfu0ovhc77ub7fl97k4w |商品视频的 ID。
   先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传视频并获取对应的文件 ID。 |
   manufacturer |object |N | |(**已弃用**：该字段已弃用，将在未来的 API 版本中移除。请改用 `manufacturer_ids`。)

商品制造商的详细信息。
**注意**: 必须填写所有嵌套属性，制造商信息才会有效。 |
^name |string |N |Sample Manufacturer Name |制造商名称。 |
^address |string |N |123W 106th St, New York, NY, USA, 10025 |制造商地址。 |
^phone_number |string |N |+1-2124108036 |制造商的电话号码，以加号 `+` 符号为前缀。
国家代码与本地电话号码之间必须有空格或连字符。 |
^email |string |N |samplemanufacturer101@outlook.com |制造商的邮箱地址。 |
category_version |string |N |v1 |按分类树版本过滤分类。基于地区的可能值：

* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |
   responsible_person_ids |[]string |N |["67726293bf1eb1e92401a"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1)。
   **注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Global Category Rules API](650a056df1fd3102b91b5b8e) 检查要求。 |
   manufacturer_ids |[]string |N |["67726293bf1eb1e92401a"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9)。
   **注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Global Category Rules API](650a056df1fd3102b91b5b8e) 检查要求。 |
   source_locale |string |N |de-DE |用于显示分类信息的 BCP-47 语言环境代码。
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
   external_global_product_id |string |N |123456789 |在外部电商平台中使用的外部标识符。 This is used to associate the global product between TikTok Shop and the external ecommerce platform。
   最大长度：999 个字符 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks\n","description":" ","category_id":"600001","brand_id":"7082427311584347905","main_images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"skus":[{"global_quantity":999,"sales_attributes":[{"id":"100089","name":"Color","value_id":"1729592969712207000\n","value_name":"Red","sku_img":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe\n"&rbrace;&rbrace;],"seller_sku":"XL-COLOR-RED-001","price":{"amount":"999","currency":"USD"},"identifier_code":{"code":"10000000000000","type":"GTIN"},"inventory":[{"global_warehouse_id":"7068517275539719942","quantity":999}],"sku_unit_count":"1","extra_identifier_codes":["10000000000000"],"external_global_sku_id":"1234567890"}],"package_weight":{"value":"1.31","unit":"KILOGRAM"},"certifications":[{"id":"7182427311584347905","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"files":[{"id":"v09ea0g40000cj91373c77u3mid3g1s0","name":"SNI.PDF","format":"PDF"}]}],"package_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"product_attributes":[{"id":"100392","values":[{"id":"1001533","name":"Steel"}]}],"size_chart":{"image":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"template":{"id":"7267563252536723205"&rbrace;&rbrace;,"video":{"id":"v09e40f40000cfu0ovhc77ub7fl97k4w"},"manufacturer":{"name":"Sample Manufacturer Name","address":"123W 106th St, New York, NY, USA, 10025","phone_number":"+1-2124108036","email":"samplemanufacturer101@outlook.com"},"category_version":"v1","responsible_person_ids":["67726293bf1eb1e92401a"],"manufacturer_ids":["67726293bf1eb1e92401a"],"source_locale":"de-DE","external_global_product_id":"123456789"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^global_product_id | string | 1729592969712207008 | TikTok Shop 生成的全球商品 ID。 |
| ^global_skus | []object |  | 用于标识商品不同款式的全球库存单位（SKU）列表。 |
| ^^id | string | 1729592969712207012 | TikTok Shop 生成的全球 SKU ID。一个商品可包含多个 SKU ID。 |
| ^^seller_sku | string | Color-Red-XM001 | 用于管理 SKU 的内部代码/名称，对买家不可见。 |
| ^^sales_attributes | []object |  | 定义商品每个变体的属性列表（如尺寸、颜色、长度）。 |
| ^^^id | string | 100000 | 销售属性 ID。 |
| 如果请求中包含自定义销售属性名称，则此为新生成的 ID。 |  |  |  |
| ^^^value_id | string | 1729592969712207123 | 销售属性值 ID。 |
| 如果请求中包含自定义销售属性值名称，则此为新生成的 ID。 |  |  |  |
| ^^external_global_sku_id | string | 1234567890 | 在外部电商平台中使用的外部标识符。 This is used to associate the global SKU between TikTok Shop and the external ecommerce platform。 |
| 最大长度：999 个字符 |  |  |  |
# 响应示例
```json
{"code":0,"data":{"global_product_id":"1729592969712207008","global_skus":[{"id":"1729592969712207012","seller_sku":"Color-Red-XM001","sales_attributes":[{"id":"100000","value_id":"1729592969712207123"}],"external_global_sku_id":"1234567890"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12019006 | product description is invalid |
| 12019011 | product package weight is invalid |
| 12019013 | brand id is invalid |
| 12019030 | property is invalid |
| 12019064 | No matching categories. Provide the full name of your product, edit its product properties, and try again. |
| 12019117 | Missing variations (sales attributes). When there are multiple SKUs in a product, each SKU must include variation (sales attribute) details that explain how it is different from other SKUs in the product. |
| 12052012 | Incorrect price format |
| 12052013 | The product description cannot exceed maximum characters |
| 12052015 | The product description is required |
| 12052016 | The parcel weight is required |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052026 | Brand does not exist |
| 12052028 | Main product image is required |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052050 | A single product cannot have more than 100 different SKUs |
| 12052051 | The product name exceed max limit characters |
| 12052054 | The seller SKU text length cannot exceed max limit characters |
| 12052055 | The SKU inventory quantity for the warehouse must be within allowed limits. |
| 12052056 | The num of image in description cannot exceed max limit |
| 12052073 | The product price is invalid |
| 12052084 | 所提供的货币不适用于该店铺/地区。 |
| 12052096 | Unable to update the price for SKUs with no warehouse. Assign a warehouse and try again. |
| 12052104 | property is required |
| 12052105 | required qualification miss |
| 12052116 | product package size is invalid |
| 12052128 | Size chart not found |
| 12052142 | no permission of multi global warehouse |
| 12052143 | sku warehouse must equal |
| 12052200 | brand is expired |
| 12052201 | 您无权在该类目下销售此品牌。如需销售，请通过 Seller Center 中的资质中心申请。 |
| 12052208 | 发布此商品信息需要品牌授权。 |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052220 | 该类目在 TikTok Shop 上被禁止或不受支持。请选择其他类目。 |
| 12052221 | 仅白名单卖家可在当前类目下交易 |
| 12052222 | category do not support cod |
| 12052225 | 您无权在该类目下销售，因为该类目不属于您店铺的主营类目。请联系您的客户经理寻求帮助或选择其他类目。 |
| 12052226 | 该类目受限。如需在该类目下销售，请通过 Seller Center 中的资质中心申请。 |
| 12052227 | the category is unauthorized or unavailable |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052240 | Do not support custom property. |
| 12052241 | attribute name or attribute id is empty. |
| 12052242 | The attribute name characters cannot exceed max_limit |
| 12052243 | The product attribute or sale attribute name characters contain Chinese. |
| 12052244 | The attribute name duplicate. |
| 12052245 | The product attributes contained invalid characters. Please modify and re-submit. |
| 12052246 | The &lbrace;&lbrace;property_type&rbrace;&rbrace; not support multi selected, attribute id is :&lbrace;&lbrace;property_id&rbrace;&rbrace;. |
| 12052247 | Do not support custom product attribute. |
| 12052248 | The &lbrace;&lbrace;property_type&rbrace;&rbrace; value name or attribute value id is empty. |
| 12052249 | The &lbrace;&lbrace;property_type&rbrace;&rbrace; value name characters cannot exceed &lbrace;&lbrace;max_limit&rbrace;&rbrace;, attribute value name is :&lbrace;&lbrace;property_value_name&rbrace;&rbrace;. |
| 12052250 | The &lbrace;&lbrace;property_type&rbrace;&rbrace; value name characters contain Chinese. |
| 12052251 | Duplicated attribute values found for an attribute. Remove or modify the duplicated value. |
| 12052254 | Duplicate attribute id |
| 12052260 | 商品 ID 不存在 |
| 12052261 | product name is empty |
| 12052262 | Chinese characters are not supported in product name |
| 12052266 | The product name contains non-English characters. |
| 12052282 | Product manufacturer is required. |
| 12052285 | Manufacturer ID &lbrace;&lbrace;manufacturer_id&rbrace;&rbrace; is not associated with the seller |
| 12052287 | Product responsible person is required |
| 12052288 | The number of responsible person ids cannot exceed &lbrace;&lbrace;max_limit&rbrace;&rbrace;, and cannot less &lbrace;&lbrace;min_limit&rbrace;&rbrace;. |
| 12052290 | Responsible person ID &lbrace;&lbrace;rp_id&rbrace;&rbrace; is not associated with the seller |
| 12052293 | When identifier code is not filled in, extra identification code is not allowed to be filled in. |
| 12052295 | Duplicate manufacturer IDs associated with the same product |
| 12052296 | Duplicate responsible person IDs associated with the same product |
| 12052300 | product main image uri illegal |
| 12052301 | Width and length of main image must be at least &lbrace;&lbrace;min_limit&rbrace;&rbrace;, check uri &lbrace;&lbrace;uri&rbrace;&rbrace; |
| 12052302 | The main images size exceed limit. |
| 12052304 | Main product image format not support. |
| 12052305 | The main images aspect ratio cannot exceed max limit. |
| 12052306 | main product images count exceed limit |
| 12052324 | Product description image file format is not supported |
| 12052340 | product description image uri illegal |
| 12052341 | The description images size cannot exceed limit. |
| 12052342 | The description images space cannot exceed limit. |
| 12052343 | Product description image format not support. |
| 12052344 | The product description html syntax with error |
| 12052345 | The product description html tag not support. |
| 12052346 | The product description has Chinese characters |
| 12052348 | The product description html tag required attribute is miss. |
| 12052349 | The product description html tag not support nest. |
| 12052350 | The product description html tag contain illegal attribute. |
| 12052351 | The product description contains non-English characters. |
| 12052352 | The product description nest exceeding limit |
| 12052360 | The video id is not exist. |
| 12052401 | package weight exceed limit. |
| 12052520 | product sale property image uri illegal |
| 12052521 | The sale property images size over limit. |
| 12052522 | Product sale property image is required |
| 12052523 | Product sale property image format not support. |
| 12052524 | The sale property image aspect ratio invalid |
| 12052525 | The attribute max num cannot exceed 3. |
| 12052526 | The attribute value max num over limit. |
| 12052527 | The sale attribute id not exist. |
| 12052528 | 您只能为 1 个商品款式添加图片，该款式将作为主款式展示在商品选项图库中。 |
| 12052529 | The property value id not exist. |
| 12052530 | The warehouse ' &lbrace;&lbrace;warehouse ID&rbrace;&rbrace; ' does not belong to this shop/seller. |
| 12052531 | The warehouse is disabled. |
| 12052550 | SKU property must contain all properties |
| 12052554 | sku name contain Chinese characters |
| 12052570 | product price exceed limit |
| 12052574 | unit price config is invalid |
| 12052591 | Invalid number of digits of identifier code |
| 12052592 | Identifier code already entered, cannot enter the same code twice |
| 12052598 | Only the last digit supports input X |
| 12052600 | The identifier code type must be selected |
| 12052650 | product qualification image uri illegal |
| 12052656 | qualification id duplicate |
| 12052657 | qualification image and pdf file is out of limit. |
| 12052670 | 尺码表图片 URI 无效。注意：API 用户必须使用 Upload Product Image API 生成的 URI。 |
| 12052671 | The sizechart images size over limit. |
| 12052673 | Product sizechart image is required |
| 12052700 | 卖家不活跃。 |
| 12052701 | do not support cross-boarder seller create local product directly |
| 12052702 | seller does not support pre-order |
| 12052703 | 卖家税号无效 |
| 12052704 | 卖家 ID 不存在 |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |

