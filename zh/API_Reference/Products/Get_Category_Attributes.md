# 获取分类属性

# Path: /product/202309/categories/{category_id}/attributes
# Method: [GET]
# 功能描述
根据您店铺的位置，获取在特定分类中上架产品的标准内置产品属性和销售属性。
TikTok Shop 上的产品被分组到 TikTok Shop 预定义的分类中，每个分类都关联一组标准的产品属性和销售属性。

* **Sales attributes** (e.g. size, color, length) define product variants and are optional if your product is straightforward and has no variants.
* **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
   使用此 API 确定在上架产品之前的必填和可选属性。
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
| category_id | string | Y | 600001 | 此产品的分类 ID。必须是叶子分类。 |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| locale | string | N | en-US | 用于显示分类信息的 BCP-47 语言环境代码。 |
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
   is_live_quick |bool |N |false |false — NORMAL products
   true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.
   Default: false |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/attributes?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&category_version=v1&is_live_quick=false
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^attributes | []object |  | 根据您店铺的位置，绑定到指定分类的标准内置产品属性和销售属性列表。 |
| ^^id | string | 100392 | 内置属性的 ID。 |
| ^^name | string | Occasion | 内置属性的名称。 |
| ^^type | string | PRODUCT_PROPERTY | 属性类型。 |
| Possible values: |  |  |  |

* SALES_PROPERTY: Indicates sales attributes that define product variants.
* PRODUCT_PROPERTY: Indicates product attributes that describe the product as a whole. |
   ^^is_requried |bool |false |标识在创建或编辑产品时是否始终需要该产品属性的标志。
* true: The attribute is always required.
* false: The attribute is not required, or required only if certain conditions are met. Refer to `requirement_conditions` for the specific requirements.

Applicable only if `type=PRODUCT_PROPERTY`. |
^^values |[]object | |属性的可选值列表。 |
^^^id |string |1001533 |内置属性值的 ID。 |
^^^name |string |Birthday |内置属性值的名称。 |
^^^icon_url |string |https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/37a9d5d39c27480d9870f73a2ad7cc95~tplv-aphluv4xwc-origin-jpeg.jpeg?dr=11254&from=3455097676&height=956&idc=no1a&ps=933b5bde&shcp=9b759fb9&shp=cdf09b4c&t=555f072d&width=1000 |The icon url value of the built-in attribute value. |
^^value_data_format |string |POSITIVE_INT_OR_DECIMAL |自由格式属性值的数据格式。
Returned for customizable numeric attributes.
Possible values:

* POSITIVE_INT_OR_DECIMAL: Positive integers or decimal numbers. |
   ^^is_customizable |bool |true |标识卖家在创建或编辑产品时是否可以为属性输入自定义值的标志。 |
   ^^requirement_conditions |[]object | |A list of conditions that determine if the product attribute is required based on the seller's inputs for other attributes. If any of the conditions is met, the attribute is required; otherwise, it is optional.

For example, there's a condition that states that the "Battery type" attribute is required if the seller selects the value "Batteries" for the attribute "Contains Batteries or Cells?". For more scenario-based guidance on using this parameter, refer to the [Solution Guide - CAT-PRE-HAZMAT](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).
Applicable only if `type=PRODUCT_PROPERTY` and `is_requried=false`. |
^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
Possible values:

* VALUE_ID_MATCH: The condition is true when the seller selects a value whose ID matches the one specified in this condition. |
   ^^^attribute_id |string |101610 |被条件评估的产品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的产品属性值的 ID。 |
   ^^is_multiple_selection |bool |true |标识卖家在创建或编辑产品时是否可以为属性选择多个值的标志。 |
   ^^metric_standards |[]object | |Defines the measurement template information used to describe the measurement standards and metric values configured for the product. |
   ^^^id |string |7678592839487784712 |The unique ID of the measurement template. Use this ID to identify which measurement standard template applies to the product. |
   ^^^name |string |prefix+num+units+suffix |The name of the measurement template. |
   ^^^metric_value_modules |[]object | |Metric value modules. |
   ^^^^id |string |7678592839487735560 |The unique ID of a metric item within the measurement template. This ID identifies which metric the submitted value belongs to. |
   ^^^^name |string |prefix+num |The seller-provided value for the specified metric item in the measurement template. |
   ^^^^input_type |string |CUSTOMIZED |Metric value modules input type. |
   ^^^^data_types |[]string |POSITIVE_INTEGER |Metric value modules data type. |
   ^^^^default_values |[]object | |Metric value modules default values. |
   ^^^^^id |string |7678592839487735560 |Metric value modules default value id. |
   ^^^^^name |string |2026 |Metric value modules default value name. |
   ^^^^units |[]object | |Metric value modules units. |
   ^^^^^id |string |7678592839484720903 |Unit id. |
   ^^^^^name |string |piece |Unit name. |
   ^^^^value_limit |object | |Metric value value limit. |
   ^^^^^num_limit |object | |Metric value num limit. |
   ^^^^^^min_value |int |1000 |Metric value num limit min value. |
   ^^^^^^max_value |int |1 |Metric value num limit max value. |
   ^^^^^length_limit |object | |Metric value length limit. |
   ^^^^^^min_length |int |10 |Metric value min length. |
   ^^^^^^max_length |int |1 |Metric value max length. |
   ^^^^prefix |string |daily |Metric value prefix. |
   ^^^^suffix |string |and |Metric value suffix. |
   ^^^^shading_word |string |number2 |Metric value shading word. |

# 响应示例
```json
{"code":0,"data":{"attributes":[{"id":"100392","name":"Occasion","type":"PRODUCT_PROPERTY","is_requried":false,"values":[{"id":"1001533","name":"Birthday","icon_url":"https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/37a9d5d39c27480d9870f73a2ad7cc95~tplv-aphluv4xwc-origin-jpeg.jpeg?dr=11254\u0026from=3455097676\u0026height=956\u0026idc=no1a\u0026ps=933b5bde\u0026shcp=9b759fb9\u0026shp=cdf09b4c\u0026t=555f072d\u0026width=1000"}],"value_data_format":"POSITIVE_INT_OR_DECIMAL","is_customizable":true,"requirement_conditions":[{"condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}],"is_multiple_selection":true,"metric_standards":[{"id":"7678592839487784712","name":"prefix+num+units+suffix","metric_value_modules":[{"id":"7678592839487735560","name":"prefix+num","input_type":"CUSTOMIZED","data_types":"POSITIVE_INTEGER","default_values":[{"id":"7678592839487735560","name":"2026"}],"units":[{"id":"7678592839484720903","name":"piece"}],"value_limit":{"num_limit":{"min_value":1000,"max_value":1},"length_limit":{"min_length":10,"max_length":1}},"prefix":"daily","suffix":"and","shading_word":"number2"}]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类 does not exist |
| 12052024 | 分类 is not final category |
| 12052025 | The category is invalid |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052704 | seller id not exist |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

