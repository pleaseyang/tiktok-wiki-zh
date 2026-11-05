# 获取全球产品

# Path: /product/202309/global_products/{global_product_id}
# Method: [GET]
# 功能描述
Retrieve all properties of a global product that is in the "DRAFT", "UNPUBLISHED", or "PUBLISHED" status, and the corresponding local product IDs in the published markets.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_product_id | string | Y | 1729592969712207008 | Global product ID |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
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
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^id | string | 1729592969712207008 | The global product ID in TikTok Shop. |
| ^title | string | Short Boat Invisible Socks | 产品标题。 |
| ^main_images | []object |  | A list of images to display in the product image gallery. |
| ^^height | int | 600 | The image height. |
| Unit: px |  |  |  |
| ^^width | int | 600 | The image width. |
| Unit: px |  |  |  |
| ^^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | 图片的 URI。 |
| ^video | object |  | Product video information. |
| ^^id | string | v09ea0g40000cj91373c77u3mid3g1s0 | The video ID. |
| ^description | string |  | HTML 格式的产品描述。 |
| ^package_dimensions | object |  | 产品包装的尺寸。 |
| ^^length | string | 10 | The package length. |
| ^^width | string | 10 | The package width. |
| ^^height | string | 10 | The package height. |
| ^^unit | string | CENTIMETER | The unit for the package dimensions. |
| ^package_weight | object |  | 产品包装的重量。 |
| ^^value | string | 1.32 | The package weight. |
| ^^unit | string | KILOGRAM | 包装重量的单位。 |
| ^certifications | []object |  | 您的产品的认证列表。 |
| ^^id | string | 7267563252536723205 | 用于标识产品分类所需认证类型的 ID。 |
| ^^title | string | SNI Certificate | The title of the certification type. |
| ^^files | []object |  | 认证相关文件列表。 |
| ^^^id | string | v09ea0g40000cj91373c77u3mid3g1s0 | 认证文件的 ID。 |
| ^^^urls | []string | ["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] | The URLs to view the certification files. |
|  |  |  |  |
| ^^^name | string | SNI.PDF | The name of the certification file |
| ^^^format | string | PDF | The format of the certification file. |
| ^^images | []object |  | 认证相关图片列表。 |
| ^^^height | int | 600 | The image height. |
| Unit: px |  |  |  |
| ^^^width | int | 600 | The image width. |
| Unit: px |  |  |  |
| ^^^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | 图片的 URI。 |
| ^skus | []object |  | A list of global Stock Keeping Units (SKUs) used to identify distinct variants of the product. |
| ^^id | string | 1729592969712207234 | The global SKU ID in TikTok Shop. |
| ^^seller_sku | string | Color-Red-XM001 | 用于管理 SKU 的内部代码/名称，对买家不可见。 |
| ^^price | object |  | The SKU's **global uniform pre-tax** price that serves as the baseline for calculating the local prices across different markets. |
**Note**:

* Upon publishing, this price will be automatically converted to the local pre-tax price and local display price based on market-specific exchange rates and applicable charges such as shipping costs, taxes, and other fees.
* The auto-conversion will exclude JP and US shops using China warehouses. |
   ^^^amount |string |1.01 |The price amount. |
   ^^^currency |string |USD |货币。
   Possible values:
* `USD`: Applicable for global sellers
* `EUR`: Applicable for intra-EU sellers |
   ^^^unit_price |string |1.00 |The unit price of the SKU.
   You can display the unit price to facilitate easier price comparisons across different products and packaging sizes.
   Applicable only for the EU market.

**Note**:

* This value is available only if you have defined the elements used to calculate this price when creating the product.
* Unit price = Selling price/(SKU unit count/base unit count) |
   ^^global_quantity |int |100 |The total SKU inventory quantity across all shops globally.

The inventory for each local shop is automatically calculated when a product is first published. After publishing, this global quantity cannot be manually changed. You can only modify the inventory quantity in each local shop. |
^^identifier_code |object | |A regulated identifier code assigned to a product based on international standardized regulations (e.g. GTIN) to ensure the product is universally identifiable across various platforms and systems. |
^^^code |string |10000000000010 |The identifier code. |
^^^type |string |GTIN |The type of identifier code.
Possible values:

* GTIN
* EAN
* UPC
* ISBN
* JAN |
   ^^sales_attributes |[]object | |定义产品每个变体的属性列表（如尺寸、颜色、长度）。 |
   ^^^id |string |100000 |The sales attribute ID. |
   ^^^name |string |Color |The sales attribute name. |
   ^^^value_id |string |7267563252536723205 |The sales attribute value ID. |
   ^^^value_name |string |Red
   |The sales attribute value name. |
   ^^^sku_img |object | |An image to display for the SKU. |
   ^^^^height |int |600 |The image height.
   Unit: px |
   ^^^^width |int |600 |The image width.
   Unit: px |
   ^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |The URLs to view the image thumbnails. |
   ^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
   ^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |The URLs to view the images. |
   ^^inventory |[]object | |SKU inventory information per warehouse. |
   ^^^global_warehouse_id |string |6966568648651605766 |The ID of the global warehouse where the SKU is stored. |
   ^^^quantity |int |100 |The SKU quantity available in the warehouse. |
   ^^sku_unit_count |string |100.00 |The total quantity/volume of the product represented by the SKU.
   For example, if the SKU represents 500ml of water, this value would be 500 if the unit type is defined as ml.
   Applicable only for the EU market.

**Note**:

* This is mainly used to calculate the unit price of the SKU, and is required only if you wish to display the unit price to facilitate easier price comparisons across different products and packaging sizes.
* Unit price = Selling price/(SKU unit count/base unit count). Therefore if you want to obtain the unit price, you would also need to define the "base unit count" and the "unit type" product attributes. Retrieve the relevant information for these product attributes by using the [Get Global Attributes API](650a0483c16ffe02b8dfc80a). |
   ^^extra_identifier_codes |[]string |["12345678901234"] |A list of up to 10 additional identifier codes if the SKU belongs to a virtual bundle (containing multiple individual SKUs).

**Note**: Applicable only for the EU market. |
^^external_global_sku_id |string |1234567890 |在外部电商平台中使用的外部标识符。 This is used to associate the SKU between TikTok Shop and the external ecommerce platform. |
^update_time |int |1694522875 |The time when the product is last updated.
Unix timestamp in seconds. |
^create_time |int |1694522875 |The time when the product is created.
Unix timestamp in seconds. |
^product_attributes |[]object | |描述产品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。 |
^^id |string |100392 |The ID of the product attribute. |
^^name |string |Occasion |The product attribute name. |
^^values |[]object | |产品属性的可选值列表。 |
^^^id |string |1001533 |The product attribute value ID. |
^^^name |string |Birthday |The product attribute value name. |
^size_chart |object | |产品的测量详情，帮助买家找到合适的尺码。 |
^^image |object | |尺码表的图片。 |
^^^height |int |600 |The image height.
Unit: px |
^^^width |int |600 |The image width.
Unit: px |
^^^uri |string |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。 |
^^template |object | |A TikTok Shop size chart template generated by the size chart tool in Seller Center > Manage Products > Bulk action > Batch manage size charts. |
^^^id |string |7267563252536723205 |尺码表模板 ID。 |
^products |[]object | |The local products associated through global product publishing or manual binding. |
^^region |string |GB |The market where the local product is listed. |
^^id |string |1729592969712207922 |The local product ID. |
^^sku_mappings |[]object | |The list of sku mappings between the global and local products. |
^^^global_sku_id |string |1729592969712207234 |The global SKU ID in TikTok Shop. |
^^^local_sku_id |string |1729592969712207230 |The local SKU ID in TikTok Shop. |
^^^sales_attribute_mappings |[]object | |The list of sales attribute mappings between the global and local SKUs. |
^^^^global_attribute_id |string |100000 |The global sales attribute ID. |
^^^^local_attribute_id |string |100000 |The local sales attribute ID. |
^^^^global_value_id |string |1001064 |The global sales attribute value ID. |
^^^^local_value_id |string |1001064 |The local sales attribute value ID. |
^global_seller_id |string |7494083603082020484 |The cross-border seller ID. |
^brand |object | |Product brand information. |
^^id |string |7082427311584347905 |此产品的品牌 ID。 |
^category |object | |The category of the product. |
^^id |string |600002 |分类 ID。 |
^manufacturer |object | |(**Deprecated**: This field is deprecated and will be removed in a future API version. Use `manufacturer_ids` instead.)
The product manufacturer's details.
If there are more than one manufacturer information, only the first-added manufacturer will be returned in this field. |
^^name |string |Sample Manufacturer Name |The name of the manufacturer. |
^^address |string |123W 106th St, New York, NY, USA, 10025 |The address of the manufacturer. |
^^phone_number |string |+1-2124108036 |The phone number of the manufacturer. |
^^email |string |samplemanufacturer101@outlook.com
|The email address of the manufacturer. |
^responsible_person_ids |[]string |["67726293bf1eb1e92401a"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1).
**Note**: Applicable only for the EU market in certain categories. |
^manufacturer_ids |[]string |["67726293bf1eb1e92401a"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9).
**Note**: Applicable only for the EU market in certain categories. |
^source_locale |string |fr-FR |用于显示分类信息的 BCP-47 语言环境代码。
Default: 您店铺的默认语言环境。
Possible values:

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
   ^external_global_product_id |string |123456789 |在外部电商平台中使用的外部标识符。 This is used to associate the product between TikTok Shop and the external ecommerce platform. |

# 响应示例
```json
{"code":0,"data":{"id":"1729592969712207008","title":"Short Boat Invisible Socks","main_images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}],"video":{"id":"v09ea0g40000cj91373c77u3mid3g1s0"},"description":" ","package_dimensions":{"length":"10","width":"10","height":"10","unit":"CENTIMETER"},"package_weight":{"value":"1.32","unit":"KILOGRAM"},"certifications":[{"id":"7267563252536723205","title":"SNI Certificate","files":[{"id":"v09ea0g40000cj91373c77u3mid3g1s0","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"name":"SNI.PDF","format":"PDF"}],"images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}]}],"skus":[{"id":"1729592969712207234","seller_sku":"Color-Red-XM001","price":{"amount":"1.01","currency":"USD","unit_price":"1.00"},"global_quantity":100,"identifier_code":{"code":"10000000000010","type":"GTIN"},"sales_attributes":[{"id":"100000","name":"Color","value_id":"7267563252536723205","value_name":"Red\n","sku_img":{"height":600,"width":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"]}}],"inventory":[{"global_warehouse_id":"6966568648651605766","quantity":100}],"sku_unit_count":"100.00","extra_identifier_codes":["12345678901234"],"external_global_sku_id":"1234567890"}],"update_time":1694522875,"create_time":1694522875,"product_attributes":[{"id":"100392","name":"Occasion","values":[{"id":"1001533","name":"Birthday"}]}],"size_chart":{"image":{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"},"template":{"id":"7267563252536723205"}},"products":[{"region":"GB","id":"1729592969712207922","sku_mappings":[{"global_sku_id":"1729592969712207234","local_sku_id":"1729592969712207230","sales_attribute_mappings":[{"global_attribute_id":"100000","local_attribute_id":"100000","global_value_id":"1001064","local_value_id":"1001064"}]}]}],"global_seller_id":"7494083603082020484","brand":{"id":"7082427311584347905"},"category":{"id":"600002"},"manufacturer":{"name":"Sample Manufacturer Name","address":"123W 106th St, New York, NY, USA, 10025","phone_number":"+1-2124108036","email":"samplemanufacturer101@outlook.com\n"},"responsible_person_ids":["67726293bf1eb1e92401a"],"manufacturer_ids":["67726293bf1eb1e92401a"],"source_locale":"fr-FR","external_global_product_id":"123456789"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052032 | The product does not exist |
| 12052048 | You cannot edit the specified product(s) as it isn't listed in your account or shop. |
| 12052260 | The product ID does not exist |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052901 | The product in its current status is not available for this operation. Change the product status and try again. |

