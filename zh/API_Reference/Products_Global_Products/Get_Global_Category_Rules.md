# 获取全球分类规则

# Path: /product/202309/categories/{category_id}/global_rules
# Method: [GET]
# 功能描述
Retrieve the additional requirements (beyond mandatory product attributes) for listing a global product in a particular category, regardless of market variations. Requirements may include product certifications, size charts, dimensions and more.
Use this API to determine the supporting information that you must prepare before listing a global product.
**Note**: It must be a [leaf category](650a03f8f1fd3102b91b338a) that corresponds to the category tree type specified in the `category_version` property.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
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
   locale |string |N |en-GB |用于显示分类信息的 BCP-47 语言环境代码。
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
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/global_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_version=v1&locale=en-GB
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
^^id |string |7267563252536723205 |The ID to identify the type of certification required. |
^^name |string |product_cert_name |The name of the certification type. |
^^is_required |bool |false |A flag to indicate if the certification is required **globally**.

* true: The certification is required in all regions.
* false: The certification is required only in some regions, or if certain conditions are met. Refer to `required_regions` and `requirement_conditions` for the specific requirements. |
   ^^sample_image_url |string |https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg |查看示例认证文件图片的 URL。 |
   ^^required_regions |[]string |["GB","MY","PH","SG","TH","VN"] |The markets where the certification is required, without conditions.
   Possible values:
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* ID: Indonesia
* IT: Italy
* IE: Ireland
* JP: Japan
* MY: Malaysia
* PH: Philippines
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico

Applicable only if `is_required=false`. |
^^optional_regions |[]string |["US"] |The markets where the certification is purely optional, or required only under certain conditions. Refer to `requirement_conditions` for details on markets with conditional requirements.
Possible values:

* AT: Austria
* BE: Belgium
* CZ: Czechia
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU: Hungary
* ID: Indonesia
* IE: Ireland
* IT: Italy
* JP: Japan
* MX: Mexico
* MY: Malaysia
* NL: Netherlands
* PH: Philippines
* PL: Poland
* PT: Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam

Applicable only if `is_required=false`. |
^^requirement_conditions |[]object | |A list of conditions that determine if the certification is required in a market based on the seller's inputs for a product attribute. If any of the conditions is met, the certification is required; otherwise, it is optional.
For example, there's a condition that states that the "Safety Data Sheet (SDS) for flammable materials" certification is required if the seller selects the value "Yes" for the attribute "Flammable Liquid?". For more scenario-based guidance on using this parameter, refer to the [Solution Guide](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).
Applicable only if `optional_regions` is not empty. |
^^^region |string |IE |The market where the certification is required when the conditions are met.
Possible values:

* AT: Austria
* BE: Belgium
* CZ: Czechia
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU: Hungary
* ID: Indonesia
* IE: Ireland
* IT: Italy
* JP: Japan
* MX: Mexico
* MY: Malaysia
* NL: Netherlands
* PH: Philippines
* PL: Poland
* PT: Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam |
   ^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
   Possible values:
* VALUE_ID_MATCH: The condition is true when the seller selects a value whose ID matches the one specified in this condition. |
   ^^^attribute_id |string |101610 |被条件评估的产品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的产品属性值的 ID。 |
   ^size_chart |object | |尺码表相关规则。 |
   ^^is_supported |bool |true |标识是否支持尺码表的标志。

**Note**: If size charts are not supported, even if you provide a size chart when creating or editing a product, the size chart will not be saved. |
^^is_required |bool |true |标识是否需要尺码表的标志。 |
^responsible_person |object | |Responsible person rules.
If this is empty, it means a responsible person is not required for this category.
Applicable only for EU markets. |
^^is_required |bool |false |A flag to indicate whether the responsible person is required for **all EU markets**.

* true: The manufacturer is required in all EU markets.
* false: The manufacturer is required only in some EU markets. Refer to `required_regions` and `optional_regions` for details. |
   ^^optional_regions |[]string |["IE"] |The markets where the responsible person is optional.
   Possible values:
* DE: Germany
* ES: Spain
* FR: France
* IT: Italy
* IE: Ireland |
   ^^required_regions |[]string |["DE","ES"] |The markets where the responsible person is required.
   Possible values:
* AT: Austria
* BE: Belgium
* CZ: Czechia
* DE: Germany
* ES: Spain
* FR: France
* GR: Greece
* HU: Hungary
* IE: Ireland
* IT: Italy
* NL: Netherlands
* PL: Poland
* PT: Portugal |
   ^manufacturer |object | |Manufacturer rules.
   If this is empty, it means a manufacturer is not required for this category.

Applicable only for EU markets. |
^^is_required |bool |false |A flag to indicate whether the manufacturer is required for **all EU markets**.

* true: The manufacturer is required in all EU markets.
* false: The manufacturer is required only in some EU markets. Refer to `required_regions` and `optional_regions` for details. |
   ^^optional_regions |[]string |["IE"] |The markets where the manufacturer is optional.
   Possible values:
* DE: Germany
* ES: Spain
* FR: France
* IT: Italy
* IE: Ireland |
   ^^required_regions |[]string |["DE","ES"] |The markets where the manufacturer is required.
   Possible values:
* AT: Austria
* BE: Belgium
* CZ: Czechia
* DE: Germany
* ES: Spain
* FR: France
* GR: Greece
* HU: Hungary
* IE: Ireland
* IT: Italy
* NL: Netherlands
* PL: Poland
* PT: Portugal |

# 响应示例
```json
{"code":0,"data":{"product_certifications":[{"id":"7267563252536723205","name":"product_cert_name","is_required":false,"sample_image_url":"https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg","required_regions":["GB","MY","PH","SG","TH","VN"],"optional_regions":["US"],"requirement_conditions":[{"region":"IE","condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}]}],"size_chart":{"is_supported":true,"is_required":true},"responsible_person":{"is_required":false,"optional_regions":["IE"],"required_regions":["DE","ES"]},"manufacturer":{"is_required":false,"optional_regions":["IE"],"required_regions":["DE","ES"]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019002 | category is invalid |
| 12052023 | 分类 does not exist |
| 12052024 | 分类 is not final category |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052220 | This category is prohibited or unsupported on TikTok Shop. Select another category. |
| 12052223 | This category is restricted. To sell in this category, apply through the Qualification Center in Seller Center. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052700 | The seller is inactive. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

