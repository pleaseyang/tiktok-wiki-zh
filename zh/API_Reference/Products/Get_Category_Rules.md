# 获取分类规则

# 路径：/product/202309/categories/{category_id}/rules
# 方法：[GET]
# 功能描述
根据您店铺的位置，获取在特定分类中上架商品的额外要求（除必填商品属性外）。要求可能包括商品认证、尺码表、尺寸等。
使用此 API 确定在上架商品之前必须准备的辅助信息。
**注意**： 它必须是与 `category_version` 属性中指定的类目树类型相对应的[叶子类目](6509c89d0fcef602bf1acd9b)。

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
| category_id | string | Y | 600001 | 分类 ID。必须是叶子分类。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_version | string | N | v1 | 按分类树版本过滤分类。基于地区的可能值： |

* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |
   locale |string |N |es-MX |用于显示分类信息的 BCP-47 语言环境代码。
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

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&category_version=v1&locale=es-MX
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_certifications | []object |  | 认证相关规则。 |
| 根据 TikTok Shop 规范，某些受限商品类目需要提供认证。有关商品类目限制的信息，请参阅 [TikTok Shop Restricted Products Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy)。 |  |  |  |
如果此项为空，表示该类目不需要认证。 |
^^id |string |602362 |用于标识所需认证类型的 ID。 |
^^name |string |SNI Certificate |认证类型的名称。 |
^^is_required |bool |true |指示在创建或编辑商品时是否始终需要该认证的标志。

* true: 该认证始终必填。
* false: 该认证非必填，或仅在满足特定条件时才必填。具体要求请参阅 `requirement_conditions`。 |
   ^^document_details |string |上传官方当地语言的用户手册或说明书。

Where there are multiple items sold as a part of a bundle, please clearly indicate which specific product the certification pertains to in the uploaded file or image. |您必须提交的认证文件的详细信息，包括内容、格式和任何其他指南。 |
^^sample_image_url |string |https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg |查看示例认证文件图片的 URL。 |
^^requirement_conditions |[]object | |一组条件，根据卖家为商品属性输入的值来确定该认证是否必填。如果满足任一条件，则该认证必填；否则为可选。
例如，存在这样一个条件，即如果卖家为属性 "Flammable Liquid?" 选择值 "Yes"，则需要 "Safety Data Sheet (SDS) for flammable materials" 认证。有关使用此参数的更多场景指导，请参阅 [Solution Guide - CAT-PRE-HAZMAT](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985)。
仅当 `is_required=false` 时适用。 |
^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
可能的值：

* VALUE_ID_MATCH：当卖家选择的取值 ID 与该条件中指定的 ID 匹配时，条件成立。 |
   ^^^attribute_id |string |101610 |被条件评估的商品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的商品属性值的 ID。
   |
   ^^expiration_date |object | |认证到期日期相关规则。 |
   ^^^is_required |bool |true |标识此认证是否需要到期日期的标志。 |
   ^size_chart |object | |尺码表相关规则。 |
   ^^is_supported |bool |true |标识是否支持尺码表的标志。

**注意**： 如果不支持尺码表，即使您在创建或编辑商品时提供了尺码表，该尺码表也不会被保存。 |
^^is_required |bool |true |标识是否需要尺码表的标志。 |
^^measurement_and_options |[]object | |按度量基准分组的度量规则。 |
^^^size_systems |[]string |["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"] |当前店铺支持的尺码体系 ID，由店铺所在地区和卖家类型决定。创建或编辑尺码表时，请将这些 ID 用于 size_chart_data.table.headers[].id 中的尺码体系列。可用列表取决于配置，可能会变化；请勿硬编码。当不支持尺码表或未返回尺码体系时，将省略此字段。 |
^^^measurement_type |string |BODY_MEASUREMENTS |Possible values: GENERIC_MEASUREMENTS: generic measurements for categories that do not distinguish body and product measurements; BODY_MEASUREMENTS: shopper body measurements; PRODUCT_MEASUREMENTS: finished-product or garment measurements. |
^^^options |[]object | |该分组的在线度量选项。 |
^^^^name |string |Bust |根据请求语言环境解析的本地化度量名称。 |
^^^^id |string |size_chart_option_bust |平台定义的标准度量 ID，例如 size_chart_option_bust。请将此 ID 用作对应标准度量的 table.headers[].id。 |
^^^^role |string |KEY |Possible values: KEY: a key category measurement; RECOMMEND: a useful recommended measurement. |
^^^^unit |string |LENGTH |Possible values: NONE: no unit conversion; LENGTH: length values such as cm or in; WEIGHT: weight values such as kg or lb; HEIGHT: person-height values such as cm or ft/in. |
^^^^metric_value_range |[]string |["70","160"] |允许的公制范围，按 [最小值，最大值] 顺序。 |
^^^^imperial_value_range |[]string |["27.5","63"] |允许的英制范围，按 [最小值，最大值] 顺序。 |
^^size_types |[]string |["size_chart_size_type_regular","size_chart_size_type_petite"] |为该类目配置的可用尺码类型。创建或编辑尺码表时，请使用此列表中返回的值作为 size_chart_data.size_types。可能的值包括: size_chart_size_type_regular: Regular; size_chart_size_type_juniors: Juniors; size_chart_size_type_plus: Plus; size_chart_size_type_big&tall: Big & Tall; size_chart_size_type_petite: Petite。当尺码类型不适用于该类目时，将省略此字段。 |
^^size_systems |[]string |["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"] |当前店铺支持的尺码体系 ID，由店铺所在地区和卖家类型决定。创建或编辑尺码表时，请将这些 ID 用于 size_chart_data.table.headers[].id 中的尺码体系列。可用列表取决于配置，可能会变化；请勿硬编码。当不支持尺码表或未返回尺码体系时，将省略此字段。 |
^cod |object | |货到付款（COD）相关规则。
仅适用于以下市场：

* 全球卖家: MY, PH, SA, TH, VN
* 本地卖家: ID, MY, PH, SA, TH, VN |
   ^^is_supported |bool |true |标识是否支持 COD 的标志。

**注意**: 如果不支持 COD，但在创建或编辑商品时设置 `is_cod_allowed=true`，上架将失败。 |
^package_dimension |object | |包装尺寸相关规则。 |
^^is_required |bool |true |标识是否需要包装尺寸的标志。 |
^epr |object | |生产者延伸责任（EPR）相关规则。 |
^^is_required |bool |false |标识是否需要 EPR 的标志。 |
^responsible_person |object | |负责人（RP）相关规则。仅适用于欧盟市场。 |
^^is_required |bool |false |标识是否需要负责人信息的标志。 |
^manufacturer |object | |制造商相关规则。仅适用于欧盟市场。 |
^^is_required |bool |false |标识是否需要制造商信息的标志。 |
^allowed_special_product_types |[]string |["PRE_ORDER"] |您的店铺允许在此分类中上架的特殊商品类型列表（不包括常规商品）。
基于地区的可能值：
**US**

* `PRE_ORDER`：商品尚未上架或发布。可通过指定发布日期延长履约。
* `MADE_TO_ORDER`：商品仅在收到订单后生产。可通过指定时长延长履约。
* `CUSTOM`：因其他因素，商品所需的履约时限超出标准。可通过指定时长延长履约。

**UK 和 SEA**

* `PRE_ORDER`: 商品尚未上架或发布。可通过指定时长延长履约。

**注意**: 如果您没有上架特殊商品类型的权限，将省略此字段。如需上架此类商品，请联系您的客户经理寻求帮助。 |
^fees |[]object | |商品费用相关规则。 |
^^type |string |PFAND |费用类型。
可能的值：PFAND |
^^is_required |bool |true |标识是否需要费用信息的标志。 |
^seller_sku |object | |卖家 SKU 相关规则。仅适用于欧盟市场的跨境 POP 店铺。 |
^^is_required |bool |true |指示在该类目中创建或编辑商品时是否需要卖家 SKU 的标志。当需要时，卖家 SKU 长度必须为 6 到 50 个字符，且只能包含字母、数字、连字符 (-) 和下划线 (_)。 |
# 响应示例
```json
{"code":0,"data":{"product_certifications":[{"id":"602362","name":"SNI Certificate","is_required":true,"document_details":"Upload a user manual or instructions in the official local language.\n\nWhere there are multiple items sold as a part of a bundle, please clearly indicate which specific product the certification pertains to in the uploaded file or image.","sample_image_url":"https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg","requirement_conditions":[{"condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}],"expiration_date":{"is_required":true}}],"size_chart":{"is_supported":true,"is_required":true,"measurement_and_options":[{"size_systems":["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"],"measurement_type":"BODY_MEASUREMENTS","options":[{"name":"Bust","id":"size_chart_option_bust","role":"KEY","unit":"LENGTH","metric_value_range":["70","160"],"imperial_value_range":["27.5","63"]}]}],"size_types":["size_chart_size_type_regular","size_chart_size_type_petite"],"size_systems":["size_chart_size_system_us","size_chart_size_system_uk","size_chart_size_system_eu"]},"cod":{"is_supported":true},"package_dimension":{"is_required":true},"epr":{"is_required":false},"responsible_person":{"is_required":false},"manufacturer":{"is_required":false},"allowed_special_product_types":["PRE_ORDER"],"fees":[{"type":"PFAND","is_required":true}],"seller_sku":{"is_required":true}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052220 | 该类目在 TikTok Shop 上被禁止或不受支持。请选择其他类目。 |
| 12052223 | 该类目受限。如需在该类目下销售，请通过 Seller Center 中的资质中心申请。 |
| 12052226 | 该类目受限。如需在该类目下销售，请通过 Seller Center 中的资质中心申请。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052446 | 分类 is not open in this market |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

