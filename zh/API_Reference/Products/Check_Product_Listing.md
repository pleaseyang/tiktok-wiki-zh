# 检查产品上架

# Path: /product/202309/products/listing_check
# Method: [POST]
# 功能描述
提前识别产品属性的任何问题，确保您的产品准备好上架。
每个产品在上架前必须满足 TikTok Shop 的要求。在上架之前，您可以将所有相关产品信息提交到此 API，以检查上架是否满足这些要求。您将收到一个需要在上架前解决的问题列表。此过程有助于降低创建产品时失败的风险。
**Note**:

* 产品内容中使用的语言必须与目标市场的语言一致（例如，不要使用中文），否则上架将失败或被拒绝。


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
| is_diagnosis_required | bool | N | true | (**Deprecated**: This field is deprecated and will be removed in a future API version. Use [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API instead to get listing quality related information.) |
| A flag to indicate whether to return the listing quality information (US only) and optimization diagnosis results for the product. If this is set to `false`, the response body will exclude the `listing_quality` and `diagnoses` objects. |  |  |  |  |
| Default: true |  |  |  |  |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| description | string | N | Please compare above detailed size with your measurement before purchase. |  |

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
   category_id |string |Y |600001 |The ID of a leaf category for this product. Use the [Get Categories API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) to obtain the available categories.

**Note**:

* Refer to TikTok Shop Academy for information on product category restrictions.
* For the US market, if you are creating products in `INVITE_ONLY` categories, you must submit a separate application through the Qualification Center on TikTok Shop Seller Center to gain access. Otherwise, even if the product audit is passed, the product will not be listed and made available to buyers. (The product status will be `PENDING` and the audit status will be `PRE_APPROVED`)
* For the Indonesia market, to list a product on both TikTok Shop and Tokopedia, you must use only categories that are available on both platforms. |
   brand_id |string |N |7082427311584347905 |此产品的品牌 ID。
   Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) to get the list of available brands for a shop.
   **Note**: Unauthorized brands won't be displayed on TikTok Shop. |
   main_images |[]object |Y | |A list of images to display in the product image gallery.
* Max count: 9
* Arrange your image URIs in the sequence that they should appear on TikTok Shop.
* Image dimensions: [300x300 px, 4000x4000 px]

**Recommendations**:

* Use a minimum of 5 images.
* The first image should have a white background. Use the [Optimize Images API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) to change the background to white. |
   ^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
   Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22) with `use_case=MAIN_IMAGE`. You can use the returned URI directly, or process it through the [Optimize Images API](665692b35d39dc02deb49a97) first and use the resulting URI. |
   skus |[]object |Y | |用于标识产品不同变体的 SKU（库存单位）列表。

**Note**:

* Max SKUs for BR, EU, JP, MX, UK, US: 300
* Max SKUs for other regions: 100

**Recommendations**: Place the most important variant at the beginning of the array. |
^sales_attributes |[]object |N | |定义产品每个变体的属性列表（如尺寸、颜色、长度）。
**Note**:

* You can omit this object if there is only 1 SKU. Otherwise, this is **required**.
* You can only have up to 3 types of sales attributes per product.
* Each SKU must include the same number and type of sales attributes. For example, you cannot have one SKU that has only a Color attribute, while another SKU has both Color and Size attributes.
* Provide either a built-in ID or a custom name; if both are provided, the ID takes priority.
* The `id/name` and `value_id/value_name` pairs must be unique in each SKU. For example, you cannot repeat `"name": "Color"`, `"value_name": "Red"` in different SKUs. |
   ^^id |string |N |100089 |内置销售属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8).
   |
   ^^name |string |N |Specification |当内置属性不满足需求时，用于验证的自定义销售属性名称。

**Note**:

* Do not include sensitive characters.
* Max length: 20 characters |
   ^^value_id |string |N |1729592969712207000 |内置销售属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). |
   ^^value_name |string |N |XL |当内置值不满足需求时，用于验证的自定义销售属性值。

**Note**:

* 同一属性下不允许重复。
* Max length: 50 characters. |
   ^^sku_img |object |N | |The default/main image for each value (e.g. red) of the primary sales attribute (e.g. color). This appears in the product options gallery on TikTok Shop.

You can attach images to only 1 type of sales attribute, which will serve as the primary attribute for display. An image must be provided for each value of the primary attribute. For example, if a product has 2 colors and 3 sizes, you can choose to attach images for either the color sales attribute or the size sales attribute. If you choose to attach images for color, you must attach 2 images, one for each color. If you want to add more images, use `supplementary_sku_images`. |
^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22) with `use_case=ATTRIBUTE_IMAGE`. |
^^supplementary_sku_images |[]object |N | |A list of supplementary images for each value (e.g. red) of the primary sales attribute (e.g. color) to provide multiple views or details of the product for that attribute value. These appear in the product options gallery on TikTok Shop.
**Note**:

* Max number of image URIs: 8.
* Arrange your image URIs in the sequence that they should appear on TikTok Shop.
* Applicable only for the US market. |
   ^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
   Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22) with `use_case=ATTRIBUTE_IMAGE`. |
   ^seller_sku |string |N |Color-Red-XM01 |用于管理 SKU 的内部代码/名称，对买家不可见。
   Valid length:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 characters
* Other regions: 1-50 characters
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: Use alphabets, numbers, hyphens (-), or underscores (_) only
* Other regions: Text without spaces |
   ^price |object |Y | |SKU 定价信息。 |
   ^^amount |string |N |1.23 |**Local sellers/Intra-EU sellers**
   The SKU's **local display price** shown on the product page before any discounts. Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed price ranges in each market. |
   ^^currency |string |Y |USD |货币。基于地区的可能值：
* BRL: Brazil
* CZK: Czech Republic
* EUR: France, Germany, Ireland, Italy, Spain, Netherlands, Belgium, Austria, Greece, Portugal
* GBP: United Kingdom
* HUF: Hungary
* IDR: Indonesia
* JPY: Japan
* MXN: Mexico
* MYR: Malaysia
* PHP: Philippines
* PLN: Poland
* SGD: Singapore
* THB: Thailand
* USD: United States
* VND: Vietnam |
   ^^sale_price |string |N |1.21 |**Global sellers**
   The SKU's **local display price** shown on the product page before any discounts.
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed price ranges in each market.

**Note**:

* Applicable only for global sellers.
* Required for JP and US shops using China warehouses, optional for others.
* This is the definitive final price shown on the product page, all other prices will be ignored. |
   ^^starting_bid_price |string |N |2.3 |starting bid price for auction product |
   ^external_sku_id |string |N |1729592969712207012 |在外部电商平台中使用的外部标识符。 This is used to associate the SKU between TikTok Shop and the external ecommerce platform.
   最大长度：999 个字符 |
   ^identifier_code |object |N | |A regulated identifier code assigned to a product based on international standardized regulations (e.g. GTIN) to ensure the product is universally identifiable across various platforms and systems. |
   ^^code |string |N |10000000000000 |The identifier code.

**Format**:

* GTIN: 14 digits
* EAN: 8, 13, or 14 digits
* UPC: 12 digits
* ISBN: 13 digits, or 9 digits ending in capital `X`
* JAN: 8 or 13 digits
   **Note**: The identifier code must be unique for each SKU, with no repetition allowed. |
   ^^type |string |N |GTIN |The type of identifier code.
   Possible values:
* GTIN
* EAN
* UPC
* ISBN
* JAN |
   ^inventory |[]object |Y | |SKU 库存信息。
   |
   ^^warehouse_id |string |Y |7068517275539719942 |SKU 存放仓库的 ID。
   从以下位置获取您的店铺可用仓库列表 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6). |
   ^^quantity |int |N |999 |仓库中可用的 SKU 总数量。
   Valid range: [1, 99,999]

Note: This quantity specifically refers to the in-stock inventory that can be shipped immediately. |
^^backorder_quantity |int |N |888 |The `backorder_quantity` will automatically be converted to `quantity` once in-stock inventory is sold out. The fulfillment of this inventory follows the `handling_time` specified below.
**Note**:

* For non-virtual product categories, provide `backorder_quantity` and `handling_time` together.
* Made-to-order (MTO), pre-order, and custom products cannot be backordered and are incompatible with `backorder_quantity`. |
   ^^handling_time |int |N |5 |The estimated number of working days needed for a backorder to be shipped. For non-virtual product categories, provide `handling_time` and `backorder_quantity` together. All warehouses for the same SKU must use the same `handling_time`. |
   ^combined_skus |[]object |N | |If this SKU belongs to a virtual bundle, this object contains the list of individual SKUs that form the bundle (e.g. gift basket, starter pack). |
   ^^product_id |string |Y |1729582718312380123 |The ID of the source product included in the virtual bundle. |
   ^^sku_id |string |Y |1729582718312380123 |The ID of the source SKU included in the virtual bundle. |
   ^^sku_count |int |Y |11 |The quantity of the source SKU included in the virtual bundle. |
   ^sku_unit_count |string |N |100.00 |The total quantity/volume of the product represented by the SKU.
   For example, if the SKU represents 500ml of water, this value would be 500 if the unit type is defined as ml.
   Valid range: [0.01, 99,999.9999]
   Applicable only for the EU market.

**Note**:

* This is mainly used to calculate the unit price of the SKU, and is required only if you wish to display the unit price to facilitate easier price comparisons across different products and packaging sizes.
* Unit price = Selling price/(SKU unit count/base unit count). Therefore if you want to obtain the unit price, you would also need to define the "base unit count" and the "unit type" product attributes. Retrieve the relevant information for these product attributes by using the [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). The unit price would then be returned in the [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda). |
   ^external_urls |[]string |N |["https://example.com/path1", "https://example.com/path2"] |消费者可以下单的第三方产品上架页面 URL 列表。 Add this property if you have products listed on third-party sites other than TikTok Shop and would like to map them.
   Provide this field as a JSON array of URL strings.
   Max string length: 500 |
   ^extra_identifier_codes |[]string |N |["00012345678905","9780596520687"] |If the SKU belongs to a virtual bundle (containing multiple individual SKUs), you can add up to 10 additional identifier codes here for the SKUs included in the bundle.

**Format**:
GTIN: 14 digits
EAN: 8, 13, or 14 digits
UPC: 12 digits
ISBN: 13 digits, or 9 digits ending in capital `X`
**Note**:

* Applicable only for the EU market.
* The identifier code must be unique for each SKU, with no repetition allowed. |
   ^pre_sale |object |N | |SKU presale information, used to tag a product as a presale product based on its presale type. Omit this object if the product is a regular item.

Applicable only if `allowed_special_product_types` from [Get Category Rules](6509c0febace3e02b74594a9) is not empty.
**Rules for the US market**:

* Regular / Preorder product: Once the product goes live, you cannot change the product type.
* Made-to-order product: You can change it to a regular product at any time. |
   ^^type |string |N |PRE_ORDER |The type of pre-sale.
   Possible values based on the region:
   **US**
* `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a release date.
* `MADE_TO_ORDER`: The product is produced only after the order is received. Fulfillment can be extended by specifying a duration.
* `CUSTOM`: The product requires a fulfillment timeline that exceeds the standard due to other factors. Fulfillment can be extended by specifying a duration.

**UK, EU, SEA, JP, and LATAM**

* `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a duration. |
   ^^fulfillment_type |object |N | |Information about the type of pre-sale order fulfillment and the corresponding timeframe.
* `handling_duration_days` is for fulfillment with an extended duration.
* `release_date` is for starting fulfillment on a fixed date.

**Note**: Provide either the `handling_duration_days` or the `release_date`, depending on the value of `pre_sale.type` and your shop's region. |
^^^handling_duration_days |int |N |24 |The desired duration for handling a pre-sale order and handing it over to a shipping carrier.
Applicable only for the following regions and pre-sale type:
**US**

* `MADE_TO_ORDER`: Business days, from 3 to 14 days.
* `CUSTOM`: Business days, from 3 to 30 days.

**UK, EU, SEA, JP, and LATAM**

* `PRE_ORDER`: Calendar days, from 3 to 30 days. |
   ^^^release_date |int |N |1619611761 |The date on which the product gets converted into a regular product and becomes available for general purchase. On this date, order handling will also start, changing the status of the order to [AWAITING_SHIPMENT](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011).

Applicable only for `PRE_ORDER` in the US.
**Note**:

* Valid range: The date must fall within 3 - 60 days from the current date.
* This date is a unix timestamp (seconds) based on the seller-selected timezone in Seller Center.
* This date cannot be modified once the product goes live.
   |
   ^list_price |object |N | |The SKU's list price information. This is equivalent to the manufacturer's suggested retail price (MSRP), or the recommended retail price (RRP).
   Applicable only for US local sellers.

**Note**: This value may appear as the strikethrough price on the product page. However, whether the strikethrough price is shown and the amount shown are subject to the audit team's review and decision based on various pricing information. |
^^amount |string |Y |1 |The price amount.
Valid range: [0.01, 7600]
**Note**: The value must be equal to or greater than `skus.price.amount`. Otherwise, it will be discarded. |
^^currency |string |Y |USD |货币。
Possible values: USD |
^external_list_prices |[]object |N | |The SKU list price (e.g. MSRP, RRP) or original price information on external ecommerce platforms.
Applicable only for selected local sellers in the US market.
**Note**: This value may appear as the strikethrough price on the product page. However, whether the strikethrough price is shown and the amount shown are subject to the audit team's review and decision based on various pricing information. |
^^source |string |Y |SHOPIFY_COMPARE_AT_PRICE |The external ecommerce platform from which the price is sourced.
Possible values:

* SHOPIFY_COMPARE_AT_PRICE: The compare_at_price in Shopify. |
   ^^amount |string |Y |1 |The price amount.
   Valid range: [0.01, 7600] |
   ^^currency |string |Y |USD |货币。
   Possible values: USD |
   ^fees |[]object |N | |The fees required for this product based on TikTok Shop policies. Fees are required only for certain product categories, retrieve the requirements from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). |
   ^^type |string |N |PFAND |费用类型。
   Possible values: PFAND |
   ^^amount |string |N |1.01 |The fee amount.
   Valid range:
* PFAND: [0.00 - 6300.00] |
   ^^additional_attribute |string |N |SINGLE_USE |An optional attribute that provides additional context for the fee. The accepted values may vary by fee type and market.

Possible values for Pfand:

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |
   ^sku_dimensions |object |N | |SKU 的尺寸。

Note:

* Provide the dimensions measured after packing the product.
* These values impact the shipping cost, so it is important to ensure that dimensions are accurate. Any discrepancies in measurements may lead to additional shipping fees.
* Optional for ID, TH, VN regions. |
   ^^length |string |Y |10 |包装长度。正整数。
   Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the nearest whole number. |
   ^^width |string |Y |10 |包装宽度。正整数。
   Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the nearest whole number. |
   ^^height |string |Y |10 |包装高度。正整数。
   Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the nearest whole number. |
   ^^unit |string |Y |CENTIMETER |SKU 尺寸的单位。
   Possible values based on region:
* US: CENTIMETER, INCH
* Other regions: CENTIMETER

Note: Use the same measurement system (metric or imperial) for `sku_weight` and `sku_dimensions`. For example, use `KILOGRAM` with `CENTIMETER`. |
^sku_weight |object |N | |SKU 的包装重量。
Note:

* Provide the weight measured after packing the SKU.
* Use the same measurement system for `sku_weight` and `sku_dimensions`; for example, use `KILOGRAM` with `CENTIMETER`.
* Weight and dimensions can affect shipping costs, so ensure both are accurate. Shipping fees may use the higher of the actual weight and the volumetric weight calculated from the dimensions. |
   ^^value |string |Y |1.32 |包装重量，必须是正数。
   The number format varies based on the unit:
* GRAM: integer
* KILOGRAM: up to 3 decimal places
* POUND: up to 2 decimal places |
   ^^unit |string |Y |KILOGRAM |SKU 重量的单位。
   Possible values based on region:
* US: KILOGRAM, POUND
* BR, JP, MX: KILOGRAM, GRAM
* Other countries: KILOGRAM

Note: Use the same measurement system (metric or imperial) for `sku_weight` and `sku_dimensions`. For example, use `KILOGRAM` with `CENTIMETER`. |
title |string |Y |Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks |产品标题。
标题长度：

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* Other regions: [25, 255] |
   is_cod_allowed |bool |N |false |标识是否在结账时显示货到付款（COD）付款选项的标志。 Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to check if COD is supported for your product category.

Applicable only for the following markets:

* Global sellers: MY, PH, SA, TH, VN
* Local sellers: ID, MY, PH, SA, TH, VN

**Note**: If COD is not supported, the listing will fail if you set this to `true`. |
certifications |[]object |N | |您的产品的认证列表。
Max count: 10
As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Retrieve the certification requirements for your product from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). Refer to [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on product category restrictions. |
^id |string |Y |7182427311584347905 |用于标识产品分类所需认证类型的 ID。
Retrieve this value from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). |
^images |[]object |N | |认证相关图片列表。 |
^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe
|图片的 URI。
Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22) with `use_case=CERTIFICATION_IMAGE`. |
^files |[]object |N | |认证相关文件列表。 |
^^id |string |Y |v09ea0g40000cj91373c77u3mid3g1s0 |认证文件的 ID。
Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload the files first and obtain the corresponding file ID. |
^^name |string |Y |SNI.PDF |认证文件的名称，包括文件扩展名。 |
^^format |string |Y |PDF |认证文件的格式。仅支持 PDF。 |
^expiration_date |int |N |1741234626 |此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。
This field may be required for certain certifications. Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to find out the requirements. |
package_weight |object |N | |产品包装的重量。
**Note**:

* All the products package weight is **mandatory by default**, except for products under **Virtual Products** categories. [Get Categories API](https://partner.tiktokshop.com/docv2/page/get-categories-202309) e.g **Digital Games**.
* Provide the weight measured after packing the product.
* This value impacts the shipping cost, so it is important to ensure that the weight is accurate. Any discrepancies in measurements may lead to additional shipping fees.
* The package weight will take precedence over package dimensions in fee calculation if the fee based on weight is higher. |
   ^value |string |Y |1.32 |包装重量，必须是正数。
   The number format varies based on the `unit`:
* `GRAM`: integer
* `KILOGRAM`: up to 3 decimal places
* `POUND`: up to 2 decimal places |
   ^unit |string |Y |KILOGRAM |包装重量的单位。
   Possible values based on region:
* US: `KILOGRAM`, `POUND`
* BR, JP, MX: `KILOGRAM`, `GRAM`
* Other countries: `KILOGRAM`

**Note**: You must use the same system of measurement (metric system or imperial system) for `package_weight` and `package_dimensions`. In other words, if you are using `KILOGRAM` for the weight, you must use `CENTIMETER` for the dimensions. |
product_attributes |[]object |N | |描述产品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。
**Important**: The attributes available for use are determined by the system based on the product's assigned category, with some being mandatory. You must provide the product attributes marked as `is_required` in the response of the [Get Attributes API](6509c5784a0bb702c0561cc8) to avoid listing failure. |
^id |string |Y |100392 |产品属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). |
^values |[]object |Y | |产品属性的可选值列表。
**Note**: Provide either a built-in ID or a custom name; if both are provided, the ID takes priority. |
^^id |string |N |1001533 |内置产品属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). |
^^name |string |N |Birthday |如果内置值不满足需求，可自定义产品属性值。系统将在上架后自动生成 ID。
**Note**:

* 同一属性下不允许重复。
* Max length: 2000 characters |
   size_chart |object |N | |产品的测量详情，帮助买家找到合适的尺码。

**Note**:

* For certain product categories, size charts may be required or not supported. Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to check the requirements.
* If size charts are not supported, even if you provide a size chart here, the size chart will not be saved.
* Provide either a TikTok Shop size chart template ID or a size chart image; if both are provided, the ID takes priority. |
   ^image |object |N | |尺码表的图片。

**Recommendations**:

* Resolution: Minimum 1024px on the shorter side
* Content: Include key measurement dimensions (e.g., bust, waist, hips, inseam), the more the better.
* Format: Use a table with distinct columns and row.
   * Use only one table per product and image.
   * Display each dimension in a separate row.
   * Display units in column headers. |
      ^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |尺码表图片的 URI。
      Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22) with `use_case=SIZE_CHART_IMAGE`. |
      ^template |object |N | |A TikTok Shop size chart template generated by the size chart tool in Seller Center > Manage Products > Bulk action > Batch manage size charts. |
      ^^id |string |Y |7267563252536723205 |尺码表模板 ID。 |
      package_dimensions |object |N | |产品包装的尺寸。

**Note**:

* Provide the dimensions measured after packing the product.
* These values impact the shipping cost, so it is important to ensure that dimensions are accurate. Any discrepancies in measurements may lead to additional shipping fees.
* Optional for ID, TH, VN regions. |
   ^length |string |Y |10 |包装长度。正整数。
   **Note**: For the BR market, decimal values using `.` or `,` as separators are also accepted but will be rounded to the nearest whole number. |
   ^width |string |Y |10 |包装宽度。正整数。
   **Note**: For the BR market, decimal values using `.` or `,` as separators are also accepted but will be rounded to the nearest whole number. |
   ^height |string |Y |10 |包装高度。正整数。
   **Note**: For the BR market, decimal values using `.` or `,` as separators are also accepted but will be rounded to the nearest whole number. |
   ^unit |string |Y |CENTIMETER |The unit for the package dimensions.
   Possible values based on region:
* US: CENTIMETER, INCH
* Other regions: CENTIMETER

**Note**: You must use the same system of measurement (metric system or imperial system) for `package_weight` and `package_dimensions`. In other words, if you are using KILOGRAM for the weight, you must use CENTIMETER for the dimensions. |
external_product_id |string |N |172959296971220002 |在外部电商平台中使用的外部标识符。 This is used to associate the product between TikTok Shop and the external ecommerce platform.
最大长度：999 个字符 |
delivery_option_ids |[]string |N |["1729592969712203232"] |This field is supported for seller accounts in the following regions only:

* ID
* MX
* MY
* PH
* SG
* TH
* VN

The custom delivery option IDs to apply to this product if you want to override the default warehouse delivery options. To retrieve the available option IDs, call [Get Warehouse Delivery Options](650aa46ebace3e02b75d9afa) with `scope=PRODUCT`.
**Note**: Leave this field blank to inherit the default delivery options configured for the warehouse. |
video |object |N | |用于展示产品的产品介绍或推广视频。
**Recommendations**:

* Aspect ratio: 1:1
* Resolution: HD 720p or higher
* Duration: 20 - 60 seconds |
   ^id |string |Y |v09e40f40000cfu0ovhc77ub7fl97k4w |产品视频的 ID。
   Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload the video first and obtain the corresponding file ID. |
   primary_combined_product_id |string |N |1729582718312380123 |If this product is associated with a virtual bundle, this value is the ID of the primary product in the bundle.

**Note**: Required only for virtual bundle products. |
manufacturer_ids |[]string |N |["172959296971220002"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9).
**Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules API](6509c0febace3e02b74594a9) to check the requirements. |
responsible_person_ids |[]string |N |["172959296971220003"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1).
**Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules API](6509c0febace3e02b74594a9) to check the requirements. |
listing_platforms |[]string |N |["TIKTOK_SHOP"] |产品上架的平台。
Possible values:

* TOKOPEDIA
* TIKTOK_SHOP
   Default: TIKTOK_SHOP

Applicable only for sellers that migrated from Tokopedia. |
shipping_insurance_requirement |string |N |NOT_SUPPORTED |对买家施加的产品运输保险购买要求。
Possible values:

* REQUIRED: Shipping insurance is mandatory and buyers can't opt out.
* OPTIONAL: Buyers can choose to purchase shipping insurance through the platform.
* NOT_SUPPORTED: Shipping insurance is not supported for the product.
   Default: OPTIONAL

Applicable only if the listing platforms include TOKOPEDIA. |
is_pre_owned |bool |N |false |标识产品是否为二手产品的标志。
Applicable only if TOKOPEDIA is the sole listing platform.
**Note**: To list pre-owned products on the TikTok Shop platform, please specify the ID of one of the designated pre-owned product categories (e.g. pre-owned luxury bags, luggage, and accessories) in `category_id`. |
minimum_order_quantity |int |N |4 |产品的最低订购量。
Valid range: [1, 20]
Applicable only for the Indonesia market and selected sellers in other SEA markets. Contact your account manager for more information about gaining access to this field. |
shipping_template_id |string |N |7552764259994699538 |将绑定到产品的运费模板的标识符 |
option |object |N | |异步产品信息验证的选项。 |
^need_trigger_gne_async_check |bool |N |false |Whether to trigger asynchronous product information verification. This asynchronous workflow is available only to enabled sellers in the US.
Set this field to `true` together with a nonempty `gne_async_check_session_id` to start new asynchronous checks.
To retry retrieval with the same session ID without creating new asynchronous tasks, set this field to `false`; any completed findings are returned in `pre_check_results`. |
^gne_async_check_session_id |string |N |20260122085233268 |A caller-provided session ID for asynchronous product information verification. This asynchronous workflow is available only to enabled sellers in the US.
Provide a nonempty session ID when you trigger asynchronous verification, then reuse the same session ID on later calls to this API with the same product information to retrieve any completed findings in `pre_check_results`.
This API does not generate or return a new session ID for you. |
scheduled_sale |object |N | |Scheduled listing configuration for the product, including whether scheduled listing is enabled and the scheduled listing time. |
^is_enabled_scheduled_sale |bool |Y |false |Whether scheduled listing is enabled for this product. If `true`, `schedule_sale_time` must be provided. |
^schedule_sale_time |int |Y |1768899145000 |Scheduled listing time, expressed as a Unix timestamp in milliseconds; must be later than the current time and within 90 days, and is required when is_enabled_scheduled_sale is true. |
search_terms |[]string |N |["sneakers","running shoes","athletic"] |搜索词（ST 词）。 ST words will not be displayed to consumers; they are only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words are consistent with the product description, with a maximum of 15 terms and a total of no more than 250 characters. |
key_product_features |[]string |N |["Breathable mesh upper", "Cushioned foam midsole"] |关键产品特性。 They will be displayed in the Product highlight module on the product detail page and will be used by search engines to increase your search weight for more traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500. |
product_tag_operations |[]object |N | |Legacy operations for enabling or disabling the `AUCTION` product tag. If `selling_format` is provided, it takes precedence over this field. |
^product_tag |string |Y |AUCTION |Possible values: AUCTION |
^enable |bool |Y |true |Whether to enable the specified product tag. Set to `true` to enable the `AUCTION` tag or `false` to disable it. |
locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。
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
   selling_format |string |N |FIXED_PRICE_AND_LIVE_AUCTION |Choose either Fixed price or Fixed price and LIVE auction. Fixed price is selected by default. LIVE auction require a starting bid price. Possible values: FIXED_PRICE, FIXED_PRICE_AND_LIVE_AUCTION. |
   is_live_quick |bool |N |false |false — NORMAL products
   true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.
   Default: false |

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
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^check_result | string | FAILED | 产品诊断的结果（PASS, FAILED）。 |
| ^fail_reasons | []object |  | A list of failure reasons if `check_result` is FAILED. |
| ^^code | int | 12052700 | 代表失败原因的机器可读代码。 This is equivalent to the error codes shown when creating a product. For the full list of codes, refer to [Create Product > Error Code](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a?#Error_Code). |
| ^^message | string | Product title invalid | 详细的失败原因。 |
| ^warnings | object |  | API 调用者需要特别关注的警告信息。 |
| ^^message | string | Your product will not be sent for review. | 需要注意的警告信息。 Review and address it when applicable. Its presence alone does not mean `check_result` is `FAILED`. |
| ^listing_quality | object |  | (**Deprecated**: This field is deprecated and will be removed in a future API version. Use the [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API instead to get listing quality related information.） |
| 产品上架质量信息。 |  |  |  |
| ^^current_tier | string | POOR | 此产品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc. |
Possible values:

* POOR
* FAIR
* GOOD
* EXCELLENT

**Note**: Available only for the US market. |
^^remaining_recommendations |int |3 |The remaining number of recommendations (see `diagnosis_results`) that must be implemented for the product to reach the highest tier.
**Note**:

* To reach the highest tier, you must implement all recommendations listed in `diagnosis_results`.
* Available only for the US market. |
   ^diagnoses |[]object | |(**Deprecated**: This field is deprecated and will be removed in a future API version. Use [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API instead to get product diagnosis related information.)
   产品优化诊断信息。 |
   ^^field |string |TITLE |被诊断的产品字段。
   Possible values:
* TITLE: Product title
* DESCRIPTION: Product description
* IMAGE: Product image displayed in the image gallery
* ATTRIBUTE: Product attribute
* SIZE_CHART: Product size chart |
   ^^diagnosis_results |[]object | |诊断结果。
   |
   ^^^code |string |TITLE_LESS_THAN_40_CHARACTERS |代表已识别问题的机器可读代码。
   Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the full list of identified issues and the corresponding recommendations. |
   ^^^how_to_solve |string |Names must be at least 40 characters long and contain product-identifying information, such as "hiking boots" or "lipstick". |解决已识别问题的建议，以店铺的默认语言返回。
   Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the full list of recommendations. |
   ^^^quality_tier |string |FAIR |通过实施建议可以达到的上架质量等级。
   Possible values:
* FAIR
* GOOD

**Note**:

* To reach a higher tier, you must implement all recommendations from the destination tier and all preceding tiers. For example, a product will reach the "GOOD" tier once all "FAIR" and "GOOD" recommendations are addressed or implemented.
* Available only for the US market. |
   ^^suggestions |object | |改进建议。 |
   ^^^seo_words |[]object | |The SEO keyword suggestions if `diagnoses.field` is "TITLE". |
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
   ^pre_check_results |[]object | |Contains any completed product information verification findings available for the supplied `gne_async_check_session_id`. The response does not expose a separate pending or completed status. If this field is missing or empty, you cannot determine from the response whether the asynchronous checks have completed or passed. |
   ^^pre_check_item |string |INCOMPLETE_INFO |Product information verification type: The types of issues returned by product information verification. |
   ^^pre_check_details |[]object | |Information Verification Details. |
   ^^^short_reason |string |Insufficient or Incomplete Product Information |Reason for streamlining: Simple problem description of product verification results |
   ^^^long_reason |string |Ensure product title and description contain complete information that accurately describes the product |Detailed reason: Detailed problem description of product verification results |
   ^^^related_fields |[]string |["PRE_CHECK_FIELD_TITLE"] |Problem Module: From which module does the problem originate, e.g., PRE_CHECK_FIELD_TITLE, PRE_CHECK_FIELD_IMAGES |

# 响应示例
```json
{"code":0,"data":{"check_result":"FAILED","fail_reasons":[{"code":12052700,"message":"Product title invalid"}],"warnings":{"message":"Your product will not be sent for review. "},"listing_quality":{"current_tier":"POOR","remaining_recommendations":3},"diagnoses":[{"field":"TITLE","diagnosis_results":[{"code":"TITLE_LESS_THAN_40_CHARACTERS","how_to_solve":"Names must be at least 40 characters long and contain product-identifying information, such as \"hiking boots\" or \"lipstick\".","quality_tier":"FAIR"}],"suggestions":{"seo_words":[{"text":"dress"}],"smart_texts":[{"text":"this is a good title"}],"images":[{"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp","optimized_uri":"tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6","optimized_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp","height":600,"width":600}]}}],"pre_check_results":[{"pre_check_item":"INCOMPLETE_INFO","pre_check_details":[{"short_reason":"Insufficient or Incomplete Product Information","long_reason":"Ensure product title and description contain complete information that accurately describes the product","related_fields":["PRE_CHECK_FIELD_TITLE"]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12001000 | product api internal error |
| 12019006 | product description is invalid |
| 12019011 | product package weight is invalid |
| 12019095 | `pre_sale.fulfillment_type` is missing or empty. |
| 12019097 | `pre_sale.fulfillment_type.release_date` must be set to a non-zero value. |
| 12019098 | `pre_sale.fulfillment_type.handling_duration_days` must be set to a non-zero value. |
| 12019099 | The specified `pre_sale.type` is not supported in your region. Refer to the API documentation for details. |
| 12019121 | calculate price error |
| 12052003 | Incorrect parcel height format |
| 12052004 | Incorrect parcel width format |
| 12052005 | Incorrect parcel length format |
| 12052023 | 分类 does not exist |
| 12052024 | 分类 is not final category |
| 12052084 | The provided currency is not available for this shop/region. |
| 12052220 | This category is prohibited or unsupported on TikTok Shop. Select another category. |
| 12052223 | This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
| 12052226 | This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
| 12052300 | product main image uri illegal |
| 12052356 | The number of 'supplementary_sku_images' for the sales attribute value exceeds the maximum limit. |
| 12052357 | 'supplementary_sku_images' is only allowed when 'sku_img' is specified. Add an image to 'sku_img' and try again. |
| 12052446 | 分类 is not open in this market |
| 12052520 | product sale property image uri illegal |
| 12052650 | product qualification image uri illegal |
| 12052670 | The size chart image URI is invalid. Note: API users must use the URI generated by the Upload Product Image API. |
| 12052700 | The seller is inactive. |
| 12052722 | The image URI does not exist in TikTok Shop. |
| 12052881 | identity internal error |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052910 | Invalid input parameters. Refer to the API documentation for details. |
| 12052915 | package weight unit and dimension unit miss match. |
| 12052916 | The package unit is not supported in the current region. |
| 12052930 | Seller SKU is required |
| 12052931 | The title must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
| 12052932 | The description must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
| 12052933 | Sales attribute names must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
| 12052934 | Sales attribute value names must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
| 12052935 | Product attribute value names must follow these formatting rules: it cannot contain HTML escape characters (e.g.,  ), emojis, or ASCII control characters (e.g., \u007F). It also cannot consist solely of symbols (e.g., //// or !@#$$$&), nor can it have more than 9 consecutive repeated characters (e.g., aaaaaaaaa or 111111111). |
| 12052936 | Seller SKU format invalid. SKU name must contain 6 - 50 characters and use alphabets, numbers, hyphens (-), or underscores (_) only. |

