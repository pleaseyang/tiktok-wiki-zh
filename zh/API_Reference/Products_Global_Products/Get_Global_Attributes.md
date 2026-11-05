# 获取全球属性

# Path: /product/202309/categories/{category_id}/global_attributes
# Method: [GET]
# 功能描述
Retrieve the standard built-in product and sales attributes for listing a global product in a particular category across the seller's markets.
TikTok Shop 上的产品被分组到 TikTok Shop 预定义的分类中，每个分类都关联一组标准的产品属性和销售属性。

* **Sales attributes** (e.g. size, color, length) define product variants and are optional if your product is straightforward and has no variants.
* **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
   Use this API to determine the mandatory and optional attributes, including market-specific requirements, before listing a global product.
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
| locale | string | N | en-GB |  |
| 用于显示分类信息的 BCP-47 语言环境代码。 |  |  |  |  |
| Default: 您店铺的默认语言环境。 |  |  |  |  |
| Possible values: |  |  |  |  |

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
   category_version |string |N |v1 |按分类树版本过滤分类。Possible values based on region:
* US, EU and SEA: v2, represents the 7-level category tree.
   Important: For US, EU and SEA shops, you must pass v2 when using this API.
* Other regions: v1, represents the 3-level category tree.Default: v1 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/global_attributes?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&locale=en-GB
&category_version=v1
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^attributes | []object |  | The list of standard built-in product and sales attributes that are bound to the specified category. |
| ^^id | string | 100392 | 内置属性的 ID。 |
| ^^name | string | Occasion | 内置属性的名称。 |
| ^^type | string | PRODUCT_PROPERTY | 属性类型。 |
| Possible values: |  |  |  |

* SALES_PROPERTY: Indicates sales attributes that define product variants.
* PRODUCT_PROPERTY: Indicates product attributes that describe the product as a whole. |
   ^^is_requried |bool |false |A flag indicating whether the product attribute is required across all of the seller's markets when creating or editing a product.
* true: The attribute is required in all of the seller's markets.
* false: The attribute is not required in all of the seller's markets; it may be required in some markets, required only under certain conditions, or optional. Refer to `required_regions`, `optional_regions`, and `requirement_conditions` for the specific requirements.

Applicable only if `type=PRODUCT_PROPERTY`. |
^^values |[]object | |属性的可选值列表。 |
^^^id |string |1001533 |内置属性值的 ID。 |
^^^name |string |Birthday |内置属性值的名称。 |
^^is_multiple_selection |bool |false |A flag to indicate if multiple values can be provided for the attribute when creating or editing a product. |
^^is_customizable |bool |false |A flag to indicate if the attribute value can be customized by sellers when creating or editing a product. |
^^requirement_conditions |[]object | |A list of market-specific conditions that determine whether the product attribute is required based on the seller's inputs for other attributes. If any condition for a market is met, the attribute is required in that market; otherwise, it is optional in that market. This field is omitted when no conditions apply.
For example, a condition can state that the "Battery type" attribute is required if the seller selects the value "Batteries" for the attribute "Contains Batteries or Cells?". For more scenario-based guidance on using this parameter, refer to the [Solution Guide](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).
Applicable only if `type=PRODUCT_PROPERTY` and `optional_regions` is not empty. |
^^^region |string |IE |The market where the attribute is required when the conditions are met.
Possible values:

* AT: Austria
* BE: Belgium
* CZ: Czech Republic
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU: Hungary
* ID: Indonesia
* IT: Italy
* IE: Ireland
* JP: Japan
* MY: Malaysia
* NL: Netherlands
* PH: Philippines
* PL: Poland
* PT: Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico |
   ^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
   Possible values:
* VALUE_ID_MATCH: The condition is true when the seller selects a value whose ID matches the one specified in this condition. |
   ^^^attribute_id |string |101610 |被条件评估的产品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的产品属性值的 ID。 |
   ^^optional_regions |[]string |["US"] |The markets where the attribute is purely optional, or required only under certain conditions. Refer to `requirement_conditions` for details on markets with conditional requirements. This field is omitted when there are no optional markets.

Possible values:

* AT: Austria
* BE: Belgium
* CZ: Czech Republic
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU: Hungary
* ID: Indonesia
* IT: Italy
* IE: Ireland
* JP: Japan
* MY: Malaysia
* NL: Netherlands
* PH: Philippines
* PL: Poland
* PT: Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico
   Applicable only if `is_requried=false`. |
   ^^required_regions |[]string |["GB","MY","PH","SG","TH","VN"] |The markets where the attribute is required without conditions. When `is_requried=true`, this list contains all of the seller's markets. When `is_requried=false`, it contains only the markets where the attribute is unconditionally required. This field is omitted when there are no unconditionally required markets.

Possible values:

* AT: Austria
* BE: Belgium
* CZ: Czech Republic
* DE: Germany
* ES: Spain
* FR: France
* GB: United Kingdom
* GR: Greece
* HU: Hungary
* ID: Indonesia
* IT: Italy
* IE: Ireland
* JP: Japan
* MY: Malaysia
* NL: Netherlands
* PH: Philippines
* PL: Poland
* PT: Portugal
* SG: Singapore
* TH: Thailand
* US: United States
* VN: Vietnam
* MX: Mexico |

# 响应示例
```json
{"code":0,"data":{"attributes":[{"id":"100392","name":"Occasion","type":"PRODUCT_PROPERTY","is_requried":false,"values":[{"id":"1001533","name":"Birthday"}],"is_multiple_selection":false,"is_customizable":false,"requirement_conditions":[{"region":"IE","condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}],"optional_regions":["US"],"required_regions":["GB","MY","PH","SG","TH","VN"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类 does not exist |
| 12052024 | 分类 is not final category |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052700 | The seller is inactive. |
| 12052704 | seller id not exist |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

