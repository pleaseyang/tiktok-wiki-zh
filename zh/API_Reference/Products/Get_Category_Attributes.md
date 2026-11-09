# 获取分类属性

# 路径：/product/202309/categories/{category_id}/attributes
# 方法：[GET]
# 功能描述
根据您店铺的位置，获取在特定分类中上架商品的标准内置商品属性和销售属性。
TikTok Shop 上的商品被分组到 TikTok Shop 预定义的分类中，每个分类都关联一组标准的商品属性和销售属性。

* **销售属性** (例如尺码、颜色、长度) 定义商品变体，如果您的商品较为简单且没有变体，则这些属性为可选。
* **商品属性**（例如制造商、原产国、所用材料）描述商品整体，与变体无关。部分商品属性根据上架政策为必填。
   使用此 API 确定在上架商品之前的必填和可选属性。
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
| category_id | string | Y | 600001 | 此商品的分类 ID。必须是叶子分类。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| locale | string | N | en-US | 用于显示分类信息的 BCP-47 语言环境代码。 |
| Default: 您店铺的默认语言环境。 |  |  |  |  |
| 可能的值： |  |  |  |  |

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
   category_version |string |N |v1 |按分类树版本过滤分类。基于地区的可能值：
* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |
   is_live_quick |bool |N |false |false — 常规商品
   true — LIVE_QUICK 商品。只有具有所需权限的卖家才能创建 LIVE_QUICK 商品。
   默认值：false |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/attributes?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&category_version=v1&is_live_quick=false
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^attributes | []object |  | 根据您店铺的位置，绑定到指定分类的标准内置商品属性和销售属性列表。 |
| ^^id | string | 100392 | 内置属性的 ID。 |
| ^^name | string | Occasion | 内置属性的名称。 |
| ^^type | string | PRODUCT_PROPERTY | 属性类型。 |
| 可能的值： |  |  |  |

* SALES_PROPERTY: 表示定义商品变体的销售属性。
* PRODUCT_PROPERTY: 表示从整体上描述商品的商品属性。 |
   ^^is_requried |bool |false |标识在创建或编辑商品时是否始终需要该商品属性的标志。
* true: 该属性始终必填。
* false: 该属性非必填，或仅在满足特定条件时才必填。具体要求请参阅 `requirement_conditions`。

仅当 `type=PRODUCT_PROPERTY` 时适用。 |
^^values |[]object | |属性的可选值列表。 |
^^^id |string |1001533 |内置属性值的 ID。 |
^^^name |string |Birthday |内置属性值的名称。 |
^^^icon_url |string |https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/37a9d5d39c27480d9870f73a2ad7cc95~tplv-aphluv4xwc-origin-jpeg.jpeg?dr=11254&from=3455097676&height=956&idc=no1a&ps=933b5bde&shcp=9b759fb9&shp=cdf09b4c&t=555f072d&width=1000 |内置属性值的图标 URL。 |
^^value_data_format |string |POSITIVE_INT_OR_DECIMAL |自由格式属性值的数据格式。
针对可自定义的数值属性返回。
可能的值：

* POSITIVE_INT_OR_DECIMAL: 正整数或小数。 |
   ^^is_customizable |bool |true |标识卖家在创建或编辑商品时是否可以为属性输入自定义值的标志。 |
   ^^requirement_conditions |[]object | |一组条件，根据卖家为其他属性输入的值来确定该商品属性是否必填。如果满足任一条件，则该属性必填；否则为可选。

例如，存在这样一个条件，即如果卖家为属性 "Contains Batteries or Cells?" 选择值 "Batteries"，则 "Battery type" 属性必填。有关使用此参数的更多场景指导，请参阅 [Solution Guide - CAT-PRE-HAZMAT](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985)。
仅在 `type=PRODUCT_PROPERTY` 且 `is_requried=false` 时适用。 |
^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
可能的值：

* VALUE_ID_MATCH：当卖家选择的取值 ID 与该条件中指定的 ID 匹配时，条件成立。 |
   ^^^attribute_id |string |101610 |被条件评估的商品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的商品属性值的 ID。 |
   ^^is_multiple_selection |bool |true |标识卖家在创建或编辑商品时是否可以为属性选择多个值的标志。 |
   ^^metric_standards |[]object | |定义用于描述为商品配置的度量标准和指标值的度量模板信息。 |
   ^^^id |string |7678592839487784712 |度量模板的唯一 ID。使用此 ID 确定哪个度量标准模板适用于该商品。 |
   ^^^name |string |prefix+num+units+suffix |度量模板的名称。 |
   ^^^metric_value_modules |[]object | |指标值模块。 |
   ^^^^id |string |7678592839487735560 |度量模板内指标项的唯一 ID。此 ID 标识提交的值属于哪个指标。 |
   ^^^^name |string |prefix+num |卖家为度量模板中指定指标项提供的值。 |
   ^^^^input_type |string |CUSTOMIZED |指标值模块的输入类型。 |
   ^^^^data_types |[]string |POSITIVE_INTEGER |指标值模块的数据类型。 |
   ^^^^default_values |[]object | |指标值模块的默认值。 |
   ^^^^^id |string |7678592839487735560 |指标值模块默认值的 ID。 |
   ^^^^^name |string |2026 |指标值模块默认值的名称。 |
   ^^^^units |[]object | |指标值模块的单位。 |
   ^^^^^id |string |7678592839484720903 |单位 ID。 |
   ^^^^^name |string |piece |单位名称。 |
   ^^^^value_limit |object | |指标值的取值限制。 |
   ^^^^^num_limit |object | |指标值的数值限制。 |
   ^^^^^^min_value |int |1000 |指标值数值限制的最小值。 |
   ^^^^^^max_value |int |1 |指标值数值限制的最大值。 |
   ^^^^^length_limit |object | |指标值的长度限制。 |
   ^^^^^^min_length |int |10 |指标值的最小长度。 |
   ^^^^^^max_length |int |1 |指标值的最大长度。 |
   ^^^^prefix |string |daily |指标值前缀。 |
   ^^^^suffix |string |and |指标值后缀。 |
   ^^^^shading_word |string |number2 |指标值遮蔽词。 |

# 响应示例
```json
{"code":0,"data":{"attributes":[{"id":"100392","name":"Occasion","type":"PRODUCT_PROPERTY","is_requried":false,"values":[{"id":"1001533","name":"Birthday","icon_url":"https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/37a9d5d39c27480d9870f73a2ad7cc95~tplv-aphluv4xwc-origin-jpeg.jpeg?dr=11254\u0026from=3455097676\u0026height=956\u0026idc=no1a\u0026ps=933b5bde\u0026shcp=9b759fb9\u0026shp=cdf09b4c\u0026t=555f072d\u0026width=1000"}],"value_data_format":"POSITIVE_INT_OR_DECIMAL","is_customizable":true,"requirement_conditions":[{"condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}],"is_multiple_selection":true,"metric_standards":[{"id":"7678592839487784712","name":"prefix+num+units+suffix","metric_value_modules":[{"id":"7678592839487735560","name":"prefix+num","input_type":"CUSTOMIZED","data_types":"POSITIVE_INTEGER","default_values":[{"id":"7678592839487735560","name":"2026"}],"units":[{"id":"7678592839484720903","name":"piece"}],"value_limit":{"num_limit":{"min_value":1000,"max_value":1},"length_limit":{"min_length":10,"max_length":1}},"prefix":"daily","suffix":"and","shading_word":"number2"}]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052025 | The category is invalid |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052704 | 卖家 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

