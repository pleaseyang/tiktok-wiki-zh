# 复制商品

# 路径：/product/202507/products/{product_id}/global_replicate
# 方法：[POST]
# 功能描述
[POST]/product/:version/Replicate_Product 的描述

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
| product_id | string | Y | 1729592969712207008 | TikTok Shop 中的商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| inventory_mode | string | N | SHARED | 源店铺中源商品的库存模式。该字段仅适用于欧盟市场。可选值： |

* SHARED: 相互关联商品的库存必须保持一致；否则将返回错误。
* EXCLUSIVE: 可独立设置每个商品的库存，且不影响其他商品。

若省略，库存模式默认为 EXCLUSIVE。 |
replicate_target |[]object |N | |用于复制本地商品的目标市场。 |
^certifications |[]object |N | |您的商品的认证列表。
最大数量：10
根据 TikTok Shop 规范，某些受限商品类目需要提供资质认证。请通过 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取您商品的资质要求。有关商品类目限制的信息，请参阅 [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy)。 |
^^expiration_date |int |N |1741234626 |此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。
对于某些资质认证，此字段可能为必填。请使用 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 了解相关要求。 |
^^files |[]object |N | |认证相关文件列表。 |
^^^format |string |N |PDF |认证文件的格式。仅支持 PDF。 |
^^^id |string |Y |v09ea0g40000cj91373c77u3mid3g1s0 |认证文件的 ID。
先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传文件并获取对应的文件 ID。 |
^^^name |string |Y |brand_cert.PDF |认证文件的名称，包括文件扩展名。 |
^^id |string |Y |7182427311584347905 |用于标识商品分类所需认证类型的 ID。
从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取该值。 |
^^images |[]object |N | |认证相关图片列表。 |
^^^uri |string |Y |tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |图片的 URI。
通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CERTIFICATION_IMAGE` 获取此 URI。 |
^inventory_mode |string |N |SHARED |该目标市场中复制商品的库存模式。该字段仅适用于欧盟市场。可选值：

* SHARED: 相互关联商品的库存必须保持一致；否则将返回错误。
* EXCLUSIVE: 可独立设置每个商品的库存，且不影响其他商品。

若省略，库存模式默认为 EXCLUSIVE。 |
^manufacturer_ids |[]string |N |["172959296971220002"] |A comma-delimited list of manufacturer IDs. 获取 ID，从 [Search Manufacturers API](67066a580dcee902fa03ccf9)。
**注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Category Rules API](6509c0febace3e02b74594a9) 检查要求。 |
^product_attributes |[]object |N | |描述商品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。
**重要**：可用属性由系统根据商品所属类目确定，其中部分为必填。您必须提供 [Get Attributes API](6509c5784a0bb702c0561cc8) 响应中标记为 `is_required` 的商品属性，以避免上架失败。 |
^^id |string |Y |100392 |商品属性的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 |
^^values |[]object |Y | |商品属性的可选值列表。
**注意**： 提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。 |
^^^id |string |N |1001533 |内置商品属性值的 ID，从 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)。 |
^^^name |string |N |Birthday |如果内置值不满足需求，可自定义商品属性值。系统将在上架后自动生成 ID。
**注意**：

* 同一属性下不允许重复。
* 最大长度：2000 个字符 |
   ^region |string |N |US |要将商品复制到的新市场。 |
   ^responsible_person_ids |[]string |N |["172959296971220003"] |A comma-delimited list of responsible person IDs. 获取 ID，从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1)。

**注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Category Rules API](6509c0febace3e02b74594a9) 检查要求。 |
^skus |[]object |N | |要在指定市场上架的 SKU。

* EU、JP、UK、US 的最大 SKU 数：300
* 其他地区的最大 SKU 数量：100
   说明: 必须包含所有来源国家的 SKU。 |
   ^^inventory |[]object |N | |各仓库的 SKU 库存信息。
   仅当该仓库的库存分配模式为 MANUAL 时，此字段才为必填. 否则为可选。 |
   ^^^quantity |int |N |100 |仓库中可用的 SKU 数量。
   有效范围： [1, 999,999] |
   ^^^warehouse_id |string |N |1732057700058170433 |仓库 ID。可从 [Get Warehouse List API](650aa418defece02be6e66b6) 或 Get Inventory Rules API 获取此值。 |
   ^^price |object |N | |SKU 在商品页面上折扣前显示的**本地展示价格**。 |
   ^^^currency |string |N |EUR |货币。 You must specify the local currency in the target market。 |
   ^^^sale_price |string |Y |100 |折扣前商品页面上展示的 SKU 本地显示价格。
   各市场允许的价格范围请参阅 Product Pricing。 |
   ^^source_sku_id |string |N |1732057700058170433 |正在复制的 SKU 的 ID |
   ^^seller_sku |string |N |Color-Red-XM01 |用于管理 SKU 的内部代码/名称，对买家不可见。
   有效长度：
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 个字符
* 其他地区: 1-50 个字符
   Format:
* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 仅使用字母、数字、连字符 (-) 或下划线 (_)
* 其他地区: 不含空格的文本 |

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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 目标市场的提交前校验错误。当此列表非空时，不会提交异步复制。可使用各条目的 `detail.region` 识别受影响的目标市场。 |
| ^^code | int | 12052223 | 错误码。 |
| ^^detail | object |  | 错误详情。 |
| ^^^region | string | US | 发生错误的目标地区。 |
| ^^message | string | the category is unauthorized. | 错误消息。 |
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
| 12052503 | 如果库存分配模式为 SHARED，则所有 SKU 的库存数量必须相同。 |
| 12052518 | The number of SKUs provided do not match that of the source product. Please ensure that you provide complete SKU data. |
| 12052930 | Seller SKU is required |
| 12052936 | Seller SKU format invalid. SKU name must contain 6 - 50 characters and use alphabets, numbers, hyphens (-), or underscores (_) only. |

