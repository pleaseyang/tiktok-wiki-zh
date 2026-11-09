# 获取全球商品

# 路径：/product/202309/global_products/{global_product_id}
# 方法：[GET]
# 功能描述
检索处于 "DRAFT"、"UNPUBLISHED" 或 "PUBLISHED" 状态的全球商品的所有属性，以及其在已发布市场中对应的本地商品 ID。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_product_id | string | Y | 1729592969712207008 | 全球商品 ID |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_products/1729592969712207008?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^id | string | 1729592969712207008 | TikTok Shop 中的全球商品 ID。 |
| ^title | string | Short Boat Invisible Socks | 商品标题。 |
| ^main_images | []object |  | 在商品图片库中展示的图片列表。 |
| ^^height | int | 600 | 图片高度。 |
| Unit: px |  |  |  |
| ^^width | int | 600 | 图片宽度。 |
| Unit: px |  |  |  |
| ^^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | 图片的 URI。 |
| ^video | object |  | 商品视频信息。 |
| ^^id | string | v09ea0g40000cj91373c77u3mid3g1s0 | 视频 ID。 |
| ^description | string |  | HTML 格式的商品描述。 |
| ^package_dimensions | object |  | 商品包装的尺寸。 |
| ^^length | string | 10 | 包裹长度。 |
| ^^width | string | 10 | 包裹宽度。 |
| ^^height | string | 10 | 包裹高度。 |
| ^^unit | string | CENTIMETER | 包裹尺寸的单位。 |
| ^package_weight | object |  | 商品包装的重量。 |
| ^^value | string | 1.32 | 包裹重量。 |
| ^^unit | string | KILOGRAM | 包装重量的单位。 |
| ^certifications | []object |  | 您的商品的认证列表。 |
| ^^id | string | 7267563252536723205 | 用于标识商品分类所需认证类型的 ID。 |
| ^^title | string | SNI Certificate | 认证类型的标题。 |
| ^^files | []object |  | 认证相关文件列表。 |
| ^^^id | string | v09ea0g40000cj91373c77u3mid3g1s0 | 认证文件的 ID。 |
| ^^^urls | []string | ["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] | 查看认证文件的 URL。 |
|  |  |  |  |
| ^^^name | string | SNI.PDF | 认证文件的名称 |
| ^^^format | string | PDF | 认证文件的格式。 |
| ^^images | []object |  | 认证相关图片列表。 |
| ^^^height | int | 600 | 图片高度。 |
| Unit: px |  |  |  |
| ^^^width | int | 600 | 图片宽度。 |
| Unit: px |  |  |  |
| ^^^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | 图片的 URI。 |
| ^skus | []object |  | 用于标识商品不同款式的全球库存单位（SKU）列表。 |
| ^^id | string | 1729592969712207234 | TikTok Shop 中的全球 SKU ID。 |
| ^^seller_sku | string | Color-Red-XM001 | 用于管理 SKU 的内部代码/名称，对买家不可见。 |
| ^^price | object |  | SKU 的**全球统一税前**价格，作为计算不同市场本地价格的基准。 |
**注意**：

* 发布后，此价格将根据各市场汇率以及配送费用、税费等适用费用，自动换算为本地税前价格和本地展示价格。
* 自动转换将排除使用中国仓库的 JP 和 US 店铺。 |
   ^^^amount |string |1.01 |价格金额。 |
   ^^^currency |string |USD |货币。
   可能的值：
* `USD`：适用于全球卖家
* `EUR`：适用于欧盟境内卖家 |
   ^^^unit_price |string |1.00 |SKU 的单价。
   你可以展示单位价格，以便更便捷地比较不同商品与包装规格的价格。
   仅适用于欧盟市场。

**注意**：

* 仅当您在创建商品时定义了用于计算此价格的要素时，此取值才可用。
* 单价 = 售价/(SKU 单位数量/基本单位数量) |
   ^^global_quantity |int |100 |全球所有店铺的 SKU 库存总量。

商品首次发布时，各本地店铺的库存会自动计算。发布后，此全局数量无法手动更改。您只能修改各本地店铺的库存数量。 |
^^identifier_code |object | |根据国际标准化法规（如 GTIN）分配给商品的受管标识码，以确保商品在各种平台和系统中可普遍识别。 |
^^^code |string |10000000000010 |标识码。 |
^^^type |string |GTIN |标识码类型。
可能的值：

* GTIN
* EAN
* UPC
* ISBN
* JAN |
   ^^sales_attributes |[]object | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。 |
   ^^^id |string |100000 |销售属性 ID。 |
   ^^^name |string |Color |销售属性名称。 |
   ^^^value_id |string |7267563252536723205 |销售属性取值 ID。 |
   ^^^value_name |string |Red
   |销售属性值的名称。 |
   ^^^sku_img |object | |用于展示该 SKU 的图片。 |
   ^^^^height |int |600 |图像高度。
   Unit: px |
   ^^^^width |int |600 |图像宽度。
   Unit: px |
   ^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
   ^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
   ^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。 |
   ^^inventory |[]object | |各仓库的 SKU 库存信息。 |
   ^^^global_warehouse_id |string |6966568648651605766 |存放该 SKU 的全球仓库 ID。 |
   ^^^quantity |int |100 |仓库中可用的 SKU 数量。 |
   ^^sku_unit_count |string |100.00 |SKU 代表的商品总量/体积。
   例如，如果 SKU 代表 500 毫升水，则当单位类型定义为 ml 时，此值将为 500。
   仅适用于欧盟市场。

**注意**：

* 这主要用于计算 SKU 的单价，仅当您希望展示单价以便于跨不同商品和包装尺寸进行价格比较时才需要。
* 单价 = 售价/(SKU 单位数量/基本单位数量)。因此，如需获取单价，还需要定义 "base unit count" 和 "unit type" 商品属性。可通过 [Get Global Attributes API](650a0483c16ffe02b8dfc80a) 获取这些商品属性的相关信息。 |
   ^^extra_identifier_codes |[]string |["12345678901234"] |如果 SKU 属于虚拟组合装（包含多个独立 SKU），则为最多 10 个附加标识符代码的列表。

**注意**： 仅适用于欧盟市场。 |
^^external_global_sku_id |string |1234567890 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联 SKU。 |
^update_time |int |1694522875 |商品最后更新的时间。
以秒为单位的 Unix 时间戳。 |
^create_time |int |1694522875 |商品的创建时间。
以秒为单位的 Unix 时间戳。 |
^product_attributes |[]object | |描述商品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。 |
^^id |string |100392 |商品属性的 ID。 |
^^name |string |Occasion |商品属性名称。 |
^^values |[]object | |商品属性的可选值列表。 |
^^^id |string |1001533 |商品属性取值 ID。 |
^^^name |string |Birthday |商品属性取值名称。 |
^size_chart |object | |商品的测量详情，帮助买家找到合适的尺码。 |
^^image |object | |尺码表的图片。 |
^^^height |int |600 |图片高度。
Unit: px |
^^^width |int |600 |图片宽度。
Unit: px |
^^^uri |string |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。 |
^^template |object | |由卖家中心 > 管理商品 > 批量操作 > 批量管理尺码表中的尺码表工具生成的 TikTok Shop 尺码表模板。 |
^^^id |string |7267563252536723205 |尺码表模板 ID。 |
^products |[]object | |通过全球商品发布或手动绑定关联的本地商品。 |
^^region |string |GB |本地商品上架所在的市场。 |
^^id |string |1729592969712207922 |本地商品 ID。 |
^^sku_mappings |[]object | |全球商品与本地商品之间的 SKU 映射列表。 |
^^^global_sku_id |string |1729592969712207234 |TikTok Shop 中的全局 SKU ID。 |
^^^local_sku_id |string |1729592969712207230 |TikTok Shop 中的本地 SKU ID。 |
^^^sales_attribute_mappings |[]object | |全球 SKU 与本地 SKU 之间的销售属性映射列表。 |
^^^^global_attribute_id |string |100000 |全局销售属性 ID。 |
^^^^local_attribute_id |string |100000 |本地销售属性 ID。 |
^^^^global_value_id |string |1001064 |全局销售属性取值 ID。 |
^^^^local_value_id |string |1001064 |本地销售属性取值 ID。 |
^global_seller_id |string |7494083603082020484 |跨境卖家 ID。 |
^brand |object | |商品品牌信息。 |
^^id |string |7082427311584347905 |此商品的品牌 ID。 |
^category |object | |商品的类目。 |
^^id |string |600002 |分类 ID。 |
^manufacturer |object | |(**Deprecated**: 此字段已弃用，将在未来的接口版本中移除。请改用 `manufacturer_ids`。)
商品制造商的详细信息。
如果存在多条制造商信息，此字段仅返回最先添加的制造商。 |
^^name |string |Sample Manufacturer Name |The name of the manufacturer. |
^^address |string |123W 106th St, New York, NY, USA, 10025 |制造商的地址。 |
^^phone_number |string |+1-2124108036 |制造商的电话号码。 |
^^email |string |samplemanufacturer101@outlook.com
|制造商的电子邮箱地址。 |
^responsible_person_ids |[]string |["67726293bf1eb1e92401a"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1)。
**注意**： 仅适用于欧盟市场的特定分类。 |
^manufacturer_ids |[]string |["67726293bf1eb1e92401a"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9)。
**注意**： 仅适用于欧盟市场的特定分类。 |
^source_locale |string |fr-FR |用于显示分类信息的 BCP-47 语言环境代码。
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
   ^external_global_product_id |string |123456789 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联商品。 |

# 响应示例
```json
{"code":0,"data":{"id":"1729592969712207008","title":"Short Boat Invisible Socks","main_images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"video":{"id":"v09ea0g40000cj91373c77u3mid3g1s0"},"description":" ","package_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"package_weight":{"value":"1.32","unit":"KILOGRAM"},"certifications":[{"id":"7267563252536723205","title":"SNI Certificate","files":[{"id":"v09ea0g40000cj91373c77u3mid3g1s0","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"name":"SNI.PDF","format":"PDF"}],"images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}]}],"skus":[{"id":"1729592969712207234","seller_sku":"Color-Red-XM001","price":{"amount":"1.01","currency":"USD","unit_price":"1.00"},"global_quantity":100,"identifier_code":{"code":"10000000000010","type":"GTIN"},"sales_attributes":[{"id":"100000","name":"Color","value_id":"7267563252536723205","value_name":"Red\n","sku_img":{"height":600,"width":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"]}}],"inventory":[{"global_warehouse_id":"6966568648651605766","quantity":100}],"sku_unit_count":"100.00","extra_identifier_codes":["12345678901234"],"external_global_sku_id":"1234567890"}],"update_time":1694522875,"create_time":1694522875,"product_attributes":[{"id":"100392","name":"Occasion","values":[{"id":"1001533","name":"Birthday"}]}],"size_chart":{"image":{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"template":{"id":"7267563252536723205"}},"products":[{"region":"GB","id":"1729592969712207922","sku_mappings":[{"global_sku_id":"1729592969712207234","local_sku_id":"1729592969712207230","sales_attribute_mappings":[{"global_attribute_id":"100000","local_attribute_id":"100000","global_value_id":"1001064","local_value_id":"1001064"}]}]}],"global_seller_id":"7494083603082020484","brand":{"id":"7082427311584347905"},"category":{"id":"600002"},"manufacturer":{"name":"Sample Manufacturer Name","address":"123W 106th St, New York, NY, USA, 10025","phone_number":"+1-2124108036","email":"samplemanufacturer101@outlook.com\n"},"responsible_person_ids":["67726293bf1eb1e92401a"],"manufacturer_ids":["67726293bf1eb1e92401a"],"source_locale":"fr-FR","external_global_product_id":"123456789"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052032 | 商品不存在 |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052260 | 商品 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |

