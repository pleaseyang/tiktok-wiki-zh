# 发布全球产品

# Path: /product/202309/global_products/{global_product_id}/publish
# Method: [POST]
# 功能描述
Publish and convert a global product to local products in one or multiple shops in supported markets. After publishing, the product is sent for review by TikTok Shop in the respective markets. For sellers in the EU market, the provided information will also be automatically translated into all EU languages supported by TikTok Shop.
**Note**:

* You can only publish in each market once. To change product information, edit the global product by using the [Edit Global Product API](6509e1bcc16ffe02b8dc3cd7). The changes will be automatically synchronized to all markets where the product is published
* Use the [Get Product API](6509d85b4a0bb702c057fdda) to obtain the converted local product information in the target market's language.
* Use the [Edit Product API](6509da7d0fcef602bf1caddf) or [Partial Edit Product API](650a98d74a0bb702c06c3289) to edit the local product information, if necessary.


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_product_id | string | Y | 1729592969712207008 | The global product id. |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| publish_target | []object | Y |  | Target markets for publishing global products. |
|  |  |  |  |  |
| ^region | string | Y | MY | The new market where you want to publish the global product. |
| Possible values: |  |  |  |  |

* AT: Austria
* BE:Belgium
* CZ:Czech Republic
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU:Hungary
* ID: Indonesia
* IE: Ireland
* IT: Italy
* JP: Japan
* MY: Malaysia
* NL: Netherlands(NL)
* PH: Philippines
* PO: Poland
* PT:Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico |
   ^responsible_person_ids |[]string |N |["67726293bf1eb1e92401a"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1).
   Default: The IDs provided when the global product was created.
   **Note**: Applicable only for the EU market in certain categories. Use the [Get Global Category Rules API](650a056df1fd3102b91b5b8e) to check the requirements. |
   ^manufacturer_ids |[]string |N |["67726293bf1eb1e92401a"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9).
   Default: The IDs provided when the global product was created.
   **Note**: Applicable only for the EU market in certain categories. Use the [Get Global Category Rules API](650a056df1fd3102b91b5b8e) to check the requirements. |
   ^skus |[]object |Y | |The SKUs to be published in the specified market.
* Max SKUs for EU, JP, UK, US: 300
* Max SKUs for other regions: 100 |
   ^^related_global_sku_id |string |Y |1729592969712207400 |The global SKU ID to be published.
   After publishing, a corresponding local product SKU will be created and linked to the global SKU. |
   ^^price |object |N | |The SKU's local pricing information in the specified market.

**Note**:

* Provide this only if you want to manually override the default local prices, which are automatically calculated from the global uniform price.
* Specify either `amount` or `sale_price`, the other will be auto-filled. If both are provided, `sale_price` takes precedence.
* JP and US shops using China warehouses must provide `price.sale_price`. |
   ^^^amount |string |N |10.01 |The SKU's **local pre-tax price**. This excludes any applicable charges such as cross-border shipping costs, taxes, and other fees, and therefore does not appear on the product page.
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed price ranges in each market.

**Note**: Not applicable for JP and US shops using China warehouses, please use `price.sale_price` instead. |
^^^currency |string |Y |MYR |货币。
Possible values based on the region:

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
   ^^^sale_price |string |N |100.00 |The SKU's **local display price** shown on the product page before any discounts.
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed price ranges in each market.

**Note**:

* Required for JP and US shops using China warehouses, optional for others.
* This is the definitive final price shown on the product page, all other prices will be ignored. |
   ^^inventory |object |N | |SKU inventory information per warehouse.
   Required for sellers without multiple warehouses, optional for others.

**Note**: If inventory details are not provided, the global SKU quantity will be evenly split among all markets, and any surplus will be added to the last published product SKU. |
^^^warehouse_id |string |N |7068517275539719942 |The warehouse ID. Retrieve this value from the [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6).
Default:

* Sellers without multiple warehouses: The available warehouses will be used, prioritizing local warehouses in the specified market over warehouses in the seller's base country.
* Sellers with multiple warehouses: The global warehouse ID |
   ^^^quantity |int |N |999 |The SKU quantity available in the warehouse.
   Valid range: [1, 99,999]

**Note**: If the local SKU inventory quantity exceeds the global SKU quantity, the global SKU quantity will be updated to be the sum of all local inventories. |
^^fees |[]object |N | |The fees required for this product based on TikTok Shop policies. Fees are required only for certain product categories, retrieve the requirements from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). |
^^^type |string |N |PFAND |费用类型。
Possible values: PFAND |
^^^amount |string |N |1.01 |The fee amount.
Valid range:

* PFAND: [0.00 - 6300.00] |
   ^^^additional_attribute |string |N |SINGLE_USE |An optional attribute that provides additional context for the fee. The accepted values may vary by fee type and market.

Possible values for Pfand:

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_products/1729592969712207008/publish?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"publish_target":[{"region":"MY","responsible_person_ids":["67726293bf1eb1e92401a"],"manufacturer_ids":["67726293bf1eb1e92401a"],"skus":[{"related_global_sku_id":"1729592969712207400","price":{"amount":"10.01","currency":"MYR","sale_price":"100.00"},"inventory":{"warehouse_id":"7068517275539719942","quantity":999},"fees":[{"type":"PFAND","amount":"1.01","additional_attribute":"SINGLE_USE"}]}]}]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | The local products converted from the global product. Match each item to its publication result in `publish_result` by `region`. A region can have a `publish_result` item without a corresponding local product when its status is `FAILED`. |
| ^^region | string | MY | The market of this local product. |
| Possible values: |  |  |  |

* AT: Austria
* BE:Belgium
* CZ:Czech Republic
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU:Hungary
* ID: Indonesia
* IE: Ireland
* IT: Italy
* JP: Japan
* MY: Malaysia
* NL: Netherlands(NL)
* PH: Philippines
* PO: Poland
* PT:Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico |
   ^^shop_id |string |7494083603082020484 |The ID of the local shop in the specified market. One market can only have one local shop. |
   ^^skus |[]object | |The newly created local SKUs in the specified market. |
   ^^^related_global_sku_id |string |1729696746528737924 |The associated global SKU ID. |
   ^^^id |string |1729592969712207400 |The newly generated local SKU ID. |
   ^^^seller_sku |string |XL-COLOR-001 |用于管理 SKU 的内部代码/名称，对买家不可见。 |
   ^^^sale_attributes |[]object | |定义产品每个变体的属性列表（如尺寸、颜色、长度）。 |
   ^^^^id |string |100001 |The newly generated local sales attribute ID. |
   ^^^^value_id |string |7272008676829824800 |The newly generated local sales attribute value ID. |
   ^^id |string |1929592969712207410 |The newly generated local product ID. |
   ^publish_result |[]object | |Results of publishing the global product. |
   ^^region |string |MY |The market associated with this publication result.
   Possible values:
* AT: Austria
* BE:Belgium
* CZ:Czech Republic
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU:Hungary
* ID: Indonesia
* IE: Ireland
* IT: Italy
* JP: Japan
* MY: Malaysia
* NL: Netherlands(NL)
* PH: Philippines
* PO: Poland
* PT:Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico |
   ^^status |string |SUCCESS |The status of publishing the product to the market.
   Possible values:
* SUCCESS: The global product was successfully published to the local shop, submitted for listing, and is now under review.
* DRAFT: The global product was saved as a draft local product due to validation errors.
* FAILED: Synchronization of the global product to the local shop was unsuccessful. |
   ^^fail_reasons |[]object | |The list of errors that occurred. |
   ^^^message |string |The publish region is inactive. |The error message. |

# 响应示例
```json
{"code":0,"data":{"products":[{"region":"MY","shop_id":"7494083603082020484","skus":[{"related_global_sku_id":"1729696746528737924","id":"1729592969712207400","seller_sku":"XL-COLOR-001","sale_attributes":[{"id":"100001","value_id":"7272008676829824800"}]}],"id":"1929592969712207410"}],"publish_result":[{"region":"MY","status":"SUCCESS","fail_reasons":[{"message":"The publish region is inactive."}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019004 | Seller is inactive |
| 12019010 | product price is invalid |
| 12019016 | Unable to publish or sync products to target markets due to missing or invalid warehouse details. |
| 12019028 | Multiple warehouses detected. Include all warehouse IDs and the corresponding details and try again. |
| 12019113 | product status is invalid |
| 12019121 | calculate price error |
| 12019150 | The product ID does not exist. |
| 12019212 | region already published |
| 12052055 | The SKU inventory quantity for the warehouse must be within allowed limits. |
| 12052084 | The provided currency is not available for this shop/region. |
| 12052117 | seller publish global product over limit and save draft |
| 12052145 | activity warehouse not allowed to be deleted |
| 12052146 | The specified inventory quantity is too low. It must be greater than the locked quantity (e.g. for committed orders, campaigns, creators) to ensure a non-negative available stock. |
| 12052260 | The product ID does not exist |
| 12052379 | the cover region of share warehouse can not cover the the product region |
| 12052424 | Missing 'sale price' value |
| 12052531 | The warehouse is disabled. |
| 12052556 | The SKU id not exist. |
| 12052700 | The seller is inactive. |
| 12052701 | do not support cross-boarder seller create local product directly |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052901 | The product in its current status is not available for this operation. Change the product status and try again. |
| 12052903 | The publish region is inactive. |
| 12052910 | Invalid input parameters. Refer to the API documentation for details. |

