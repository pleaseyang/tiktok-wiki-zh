# 复制产品

# Path: /product/202507/products/{product_id}/global_replicate
# Method: [POST]
# 功能描述
Description of [POST]/product/:version/Replicate_Product

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 1729592969712207008 | The product ID in TikTok Shop. |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| inventory_mode | string | N | SHARED | The inventory mode for the source product in the source shop. This field is applicable only to EU markets. Possible values: |

* SHARED: Inventory for interconnected products must remain consistent; otherwise, an error is returned.
* EXCLUSIVE: Inventory for each product can be set independently without affecting the others.

If omitted, the inventory mode defaults to EXCLUSIVE. |
replicate_target |[]object |N | |Target markets for replicating the local product. |
^certifications |[]object |N | |您的产品的认证列表。
Max count: 10
As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Retrieve the certification requirements for your product from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). Refer to [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on product category restrictions. |
^^expiration_date |int |N |1741234626 |此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。
This field may be required for certain certifications. Use the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to find out the requirements. |
^^files |[]object |N | |认证相关文件列表。 |
^^^format |string |N |PDF |认证文件的格式。仅支持 PDF。 |
^^^id |string |Y |v09ea0g40000cj91373c77u3mid3g1s0 |认证文件的 ID。
Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload the files first and obtain the corresponding file ID. |
^^^name |string |Y |brand_cert.PDF |认证文件的名称，包括文件扩展名。 |
^^id |string |Y |7182427311584347905 |用于标识产品分类所需认证类型的 ID。
Retrieve this value from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). |
^^images |[]object |N | |认证相关图片列表。 |
^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22) with `use_case=CERTIFICATION_IMAGE`. |
^inventory_mode |string |N |SHARED |The inventory mode for the replicated product in this target market. This field is applicable only to EU markets. Possible values:

* SHARED: Inventory for interconnected products must remain consistent; otherwise, an error is returned.
* EXCLUSIVE: Inventory for each product can be set independently without affecting the others.

If omitted, the inventory mode defaults to EXCLUSIVE. |
^manufacturer_ids |[]string |N |["172959296971220002"] |A comma-delimited list of manufacturer IDs. 获取 ID，从 [Search Manufacturers API](67066a580dcee902fa03ccf9).
**Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules API](6509c0febace3e02b74594a9) to check the requirements. |
^product_attributes |[]object |N | |描述产品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。
**Important**: The attributes available for use are determined by the system based on the product's assigned category, with some being mandatory. You must provide the product attributes marked as `is_required` in the response of the [Get Attributes API](6509c5784a0bb702c0561cc8) to avoid listing failure. |
^^id |string |Y |100392 |产品属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). |
^^values |[]object |Y | |产品属性的可选值列表。
**Note**: Provide either a built-in ID or a custom name; if both are provided, the ID takes priority. |
^^^id |string |N |1001533 |内置产品属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8). |
^^^name |string |N |Birthday |如果内置值不满足需求，可自定义产品属性值。系统将在上架后自动生成 ID。
**Note**:

* 同一属性下不允许重复。
* Max length: 2000 characters |
   ^region |string |N |US |The new market where you want to replicate the product. |
   ^responsible_person_ids |[]string |N |["172959296971220003"] |A comma-delimited list of responsible person IDs. 获取 ID，从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1).

**Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules API](6509c0febace3e02b74594a9) to check the requirements. |
^skus |[]object |N | |The SKUs to be published in the specified market.

* Max SKUs for EU, JP, UK, US: 300
* Max SKUs for other regions: 100
   Note: SKUs of all source country must be included. |
   ^^inventory |[]object |N | |SKU inventory information per warehouse.
   This field is only required if the inventory allocation mode for the warehouse is MANUAL. Otherwise, it is optional. |
   ^^^quantity |int |N |100 |The SKU quantity available in the warehouse.
   Valid range: [1, 999,999] |
   ^^^warehouse_id |string |N |1732057700058170433 |The warehouse ID. Retrieve this value from the [Get Warehouse List API](650aa418defece02be6e66b6) or Get Inventory Rules API. |
   ^^price |object |N | |The SKU's **local display price** shown on the product page before any discounts. |
   ^^^currency |string |N |EUR |货币。 You must specify the local currency in the target market. |
   ^^^sale_price |string |Y |100 |The SKU's local display price shown on the product page before any discounts.
   Refer to Product Pricing for the allowed price ranges in each market. |
   ^^source_sku_id |string |N |1732057700058170433 |The ID of the SKU being replicated |
   ^^seller_sku |string |N |Color-Red-XM01 |用于管理 SKU 的内部代码/名称，对买家不可见。
   Valid length:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 characters
* Other regions: 1-50 characters
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: Use alphabets, numbers, hyphens (-), or underscores (_) only
* Other regions: Text without spaces |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202507/products/1729592969712207008/global_replicate?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"inventory_mode":"SHARED","replicate_target":[{"certifications":[{"expiration_date":1741234626,"files":[{"format":"PDF","id":"v09ea0g40000cj91373c77u3mid3g1s0","name":"brand_cert.PDF"}],"id":"7182427311584347905","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe"}]}],"inventory_mode":"SHARED","manufacturer_ids":["172959296971220002"],"product_attributes":[{"id":"100392","values":[{"id":"1001533","name":"Birthday"}]}],"region":"US","responsible_person_ids":["172959296971220003"],"skus":[{"inventory":[{"quantity":100,"warehouse_id":"1732057700058170433"}],"price":{"currency":"EUR","sale_price":"100"},"source_sku_id":"1732057700058170433","seller_sku":"Color-Red-XM01"}]}]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | The pre-submission validation errors for target markets. When this list is non-empty, asynchronous replication is not submitted. Use each item's `detail.region` to identify the affected target market. |
| ^^code | int | 12052223 | The error code. |
| ^^detail | object |  | The details of the error. |
| ^^^region | string | US | The target region where the error occurred. |
| ^^message | string | the category is unauthorized. | The error message. |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":12052223,"detail":{"region":"US"},"message":"the category is unauthorized."}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052500 | A replica already exists for this product in the stated region. Only one replica is allowed per region. |
| 12052501 | This operation is only available for shops using the LOCAL_REPLICATION listing method. Your shop is currently using the GLOBAL_PUBLISHING method. |
| 12052503 | If the inventory allocation mode is SHARED, the inventory quantity must be the same across all SKUs. |
| 12052518 | The number of SKUs provided do not match that of the source product. Please ensure that you provide complete SKU data. |
| 12052930 | Seller SKU is required |
| 12052936 | Seller SKU format invalid. SKU name must contain 6 - 50 characters and use alphabets, numbers, hyphens (-), or underscores (_) only. |

