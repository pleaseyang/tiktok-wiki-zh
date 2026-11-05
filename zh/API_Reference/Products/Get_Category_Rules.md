# 获取分类规则

# Path: /product/202309/categories/{category_id}/rules
# Method: [GET]
# 功能描述
根据您店铺的位置，获取在特定分类中上架产品的额外要求（除必填产品属性外）。要求可能包括产品认证、尺码表、尺寸等。
使用此 API 确定在上架产品之前必须准备的辅助信息。
**Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category tree type specified in the `category_version` property.

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
| category_id | string | Y | 600001 | 分类 ID。必须是叶子分类。 |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_version | string | N | v1 | 按分类树版本过滤分类。Possible values based on region: |

* US, EU and SEA: v2, represents the 7-level category tree.
   Important: For US, EU and SEA shops, you must pass v2 when using this API.
* Other regions: v1, represents the 3-level category tree.Default: v1 |
   locale |string |N |es-MX |用于显示分类信息的 BCP-47 语言环境代码。
   Default: 您店铺的默认语言环境。
   Possible values:
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

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&category_version=v1&locale=es-MX
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_certifications | []object |  | 认证相关规则。 |
| As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Refer to [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on product category restrictions. |  |  |  |
If this is empty, it means certifications are not required for this category. |
^^id |string |602362 |The ID to identify the type of certification required. |
^^name |string |SNI Certificate |The name of the certification type. |
^^is_required |bool |true |A flag to indicate if the certification is always required when creating or editing a product.

* true: The certification is always required.
* false: The certification is not required, or required only if certain conditions are met. Refer to `requirement_conditions` for the specific requirements. |
   ^^document_details |string |Upload a user manual or instructions in the official local language.

Where there are multiple items sold as a part of a bundle, please clearly indicate which specific product the certification pertains to in the uploaded file or image. |您必须提交的认证文件的详细信息，包括内容、格式和任何其他指南。 |
^^sample_image_url |string |https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg |查看示例认证文件图片的 URL。 |
^^requirement_conditions |[]object | |A list of conditions that determine if the certification is required based on the seller's inputs for a product attribute. If any of the conditions is met, the certification is required; otherwise, it is optional.
For example, there's a condition that states that the "Safety Data Sheet (SDS) for flammable materials" certification is required if the seller selects the value "Yes" for the attribute "Flammable Liquid?". For more scenario-based guidance on using this parameter, refer to the [Solution Guide - CAT-PRE-HAZMAT](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).
Applicable only if `is_required=false`. |
^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
Possible values:

* VALUE_ID_MATCH: The condition is true when the seller selects a value whose ID matches the one specified in this condition. |
   ^^^attribute_id |string |101610 |被条件评估的产品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的产品属性值的 ID。
   |
   ^^expiration_date |object | |认证到期日期相关规则。 |
   ^^^is_required |bool |true |标识此认证是否需要到期日期的标志。 |
   ^size_chart |object | |尺码表相关规则。 |
   ^^is_supported |bool |true |标识是否支持尺码表的标志。

**Note**: If size charts are not supported, even if you provide a size chart when creating or editing a product, the size chart will not be saved. |
^^is_required |bool |true |标识是否需要尺码表的标志。 |
^^measurement_and_options |[]object | |Measurement rules grouped by measurement basis. |
^^^size_systems |[]string |["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"] |Size system IDs supported by the current shop, determined by the shop region and seller type. Use these IDs for size-system columns in size_chart_data.table.headers[].id when creating or editing a size chart. The available list is configuration-dependent and may change; do not hardcode it. This field is omitted when size charts are unsupported or no size systems are returned. |
^^^measurement_type |string |BODY_MEASUREMENTS |Possible values: GENERIC_MEASUREMENTS: generic measurements for categories that do not distinguish body and product measurements; BODY_MEASUREMENTS: shopper body measurements; PRODUCT_MEASUREMENTS: finished-product or garment measurements. |
^^^options |[]object | |Online measurement options for this group. |
^^^^name |string |Bust |Localized measurement name resolved using the request locale. |
^^^^id |string |size_chart_option_bust |Platform-defined standard measurement ID, for example size_chart_option_bust. Use this ID as table.headers[].id for the corresponding standard measurement. |
^^^^role |string |KEY |Possible values: KEY: a key category measurement; RECOMMEND: a useful recommended measurement. |
^^^^unit |string |LENGTH |Possible values: NONE: no unit conversion; LENGTH: length values such as cm or in; WEIGHT: weight values such as kg or lb; HEIGHT: person-height values such as cm or ft/in. |
^^^^metric_value_range |[]string |["70","160"] |Allowed metric range in [minimum, maximum] order. |
^^^^imperial_value_range |[]string |["27.5","63"] |Allowed imperial range in [minimum, maximum] order. |
^^size_types |[]string |["size_chart_size_type_regular","size_chart_size_type_petite"] |Available size types configured for this category. Use values returned in this list for size_chart_data.size_types when creating or editing a size chart. Possible values include: size_chart_size_type_regular: Regular; size_chart_size_type_juniors: Juniors; size_chart_size_type_plus: Plus; size_chart_size_type_big&tall: Big & Tall; size_chart_size_type_petite: Petite. This field is omitted when size types do not apply to the category. |
^^size_systems |[]string |["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"] |Size system IDs supported by the current shop, determined by the shop region and seller type. Use these IDs for size-system columns in size_chart_data.table.headers[].id when creating or editing a size chart. The available list is configuration-dependent and may change; do not hardcode it. This field is omitted when size charts are unsupported or no size systems are returned. |
^cod |object | |货到付款（COD）相关规则。
Applicable only for the following markets:

* Global sellers: MY, PH, SA, TH, VN
* Local sellers: ID, MY, PH, SA, TH, VN |
   ^^is_supported |bool |true |标识是否支持 COD 的标志。

**Note**: If COD is not supported, but you set `is_cod_allowed=true` when creating or editing a product, the listing will fail. |
^package_dimension |object | |包装尺寸相关规则。 |
^^is_required |bool |true |标识是否需要包装尺寸的标志。 |
^epr |object | |生产者延伸责任（EPR）相关规则。 |
^^is_required |bool |false |标识是否需要 EPR 的标志。 |
^responsible_person |object | |负责人（RP）相关规则。仅适用于欧盟市场。 |
^^is_required |bool |false |标识是否需要负责人信息的标志。 |
^manufacturer |object | |制造商相关规则。仅适用于欧盟市场。 |
^^is_required |bool |false |标识是否需要制造商信息的标志。 |
^allowed_special_product_types |[]string |["PRE_ORDER"] |您的店铺允许在此分类中上架的特殊产品类型列表（不包括常规产品）。
Possible values based on the region:
**US**

* `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a release date.
* `MADE_TO_ORDER`: The product is produced only after the order is received. Fulfillment can be extended by specifying a duration.
* `CUSTOM`: The product requires a fulfillment timeline that exceeds the standard due to other factors. Fulfillment can be extended by specifying a duration.

**UK and SEA**

* `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a duration.

**Note**: This field is omitted if you lack the permission to list special product types. Contact your account manager for assistance if you wish to list such products. |
^fees |[]object | |产品费用相关规则。 |
^^type |string |PFAND |费用类型。
Possible values: PFAND |
^^is_required |bool |true |标识是否需要费用信息的标志。 |
^seller_sku |object | |Seller SKU related rules. Applicable only for cross-border POP shops in EU markets. |
^^is_required |bool |true |A flag to indicate whether a Seller SKU is required when creating or editing a product in this category. When required, the Seller SKU must be 6 to 50 characters long and can contain only letters, digits, hyphens (-) and underscores (_). |
# 响应示例
```json
{"code":0,"data":{"product_certifications":[{"id":"602362","name":"SNI Certificate","is_required":true,"document_details":"Upload a user manual or instructions in the official local language.\n\nWhere there are multiple items sold as a part of a bundle, please clearly indicate which specific product the certification pertains to in the uploaded file or image.","sample_image_url":"https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg","requirement_conditions":[{"condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}],"expiration_date":{"is_required":true}}],"size_chart":{"is_supported":true,"is_required":true,"measurement_and_options":[{"size_systems":["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"],"measurement_type":"BODY_MEASUREMENTS","options":[{"name":"Bust","id":"size_chart_option_bust","role":"KEY","unit":"LENGTH","metric_value_range":["70","160"],"imperial_value_range":["27.5","63"]}]}],"size_types":["size_chart_size_type_regular","size_chart_size_type_petite"],"size_systems":["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"]},"cod":{"is_supported":true},"package_dimension":{"is_required":true},"epr":{"is_required":false},"responsible_person":{"is_required":false},"manufacturer":{"is_required":false},"allowed_special_product_types":["PRE_ORDER"],"fees":[{"type":"PFAND","is_required":true}],"seller_sku":{"is_required":true}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类 does not exist |
| 12052024 | 分类 is not final category |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052220 | This category is prohibited or unsupported on TikTok Shop. Select another category. |
| 12052223 | This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
| 12052226 | This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052446 | 分类 is not open in this market |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

