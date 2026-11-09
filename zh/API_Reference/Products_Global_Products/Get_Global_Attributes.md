# 获取全球属性

# 路径：/product/202309/categories/{category_id}/global_attributes
# 方法：[GET]
# 功能描述
获取在卖家各市场的特定类目下上架全球商品所需的标准内置商品属性与销售属性。
TikTok Shop 上的商品被分组到 TikTok Shop 预定义的分类中，每个分类都关联一组标准的商品属性和销售属性。

* **销售属性** (例如尺码、颜色、长度) 定义商品变体，如果您的商品较为简单且没有变体，则这些属性为可选。
* **商品属性**（例如制造商、原产国、所用材料）描述商品整体，与变体无关。部分商品属性根据上架政策为必填。
   在上架全球商品之前，使用此 API 确定必填和可选属性，包括特定市场的要求。
   **注意**： 它必须是与 `category_version` 属性中指定的类目树类型相对应的[叶子类目](650a03f8f1fd3102b91b338a)。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
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
| locale | string | N | en-GB |  |
| 用于显示分类信息的 BCP-47 语言环境代码。 |  |  |  |  |
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

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/global_attributes?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&locale=en-GB
&category_version=v1
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^attributes | []object |  | 绑定到指定类目的标准内置商品属性与销售属性列表。 |
| ^^id | string | 100392 | 内置属性的 ID。 |
| ^^name | string | Occasion | 内置属性的名称。 |
| ^^type | string | PRODUCT_PROPERTY | 属性类型。 |
| 可能的值： |  |  |  |

* SALES_PROPERTY: 表示定义商品变体的销售属性。
* PRODUCT_PROPERTY: 表示从整体上描述商品的商品属性。 |
   ^^is_requried |bool |false |用于指示在创建或编辑商品时，该商品属性在卖家的所有市场中是否为必填的标志。
* true: 该属性在卖家的所有市场中均为必填。
* false: 该属性并非在卖家的所有市场都为必填；它可能在某些市场必填、仅在特定条件下必填，或为可选。具体请参考 `required_regions`、`optional_regions` 和 `requirement_conditions`。

仅当 `type=PRODUCT_PROPERTY` 时适用。 |
^^values |[]object | |属性的可选值列表。 |
^^^id |string |1001533 |内置属性值的 ID。 |
^^^name |string |Birthday |内置属性值的名称。 |
^^is_multiple_selection |bool |false |用于指示在创建或编辑商品时是否可以为该属性提供多个值的标志。 |
^^is_customizable |bool |false |用于指示卖家在创建或编辑商品时是否可自定义该属性取值的标志。 |
^^requirement_conditions |[]object | |针对各市场的条件列表，根据卖家为其它属性输入的内容判定该商品属性是否必填。如果某市场满足任一条件，则该属性在该市场为必填；否则在该市场为可选。当没有适用条件时，此字段会省略。
例如，某个条件可以规定：如果卖家为属性 "Contains Batteries or Cells?" 选择取值 "Batteries"，则 "Battery type" 属性为必填。有关使用此参数的更多基于场景的指导，请参考 [Solution Guide](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985)。
仅当 `type=PRODUCT_PROPERTY` 且 `optional_regions` 不为空时适用。 |
^^^region |string |IE |满足条件时该属性为必填项的市场。
可能的值：

* AT: 奥地利
* BE: 比利时
* CZ: 捷克共和国
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU: 匈牙利
* ID: 印度尼西亚
* IT: Italy
* IE: 爱尔兰
* JP: Japan
* MY: 马来西亚
* NL: 荷兰
* PH: 菲律宾
* PL: 波兰
* PT: 葡萄牙
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥 |
   ^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
   可能的值：
* VALUE_ID_MATCH：当卖家选择的取值 ID 与该条件中指定的 ID 匹配时，条件成立。 |
   ^^^attribute_id |string |101610 |被条件评估的商品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的商品属性值的 ID。 |
   ^^optional_regions |[]string |["US"] |该属性完全可选或仅在特定条件下必填的市场。有关带条件要求的市场的详细信息，请参考 `requirement_conditions`。当没有可选市场时，此字段会省略。

可能的值：

* AT: 奥地利
* BE: 比利时
* CZ: 捷克共和国
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU: 匈牙利
* ID: 印度尼西亚
* IT: Italy
* IE: 爱尔兰
* JP: Japan
* MY: 马来西亚
* NL: 荷兰
* PH: 菲律宾
* PL: 波兰
* PT: 葡萄牙
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥
   仅当 `is_requried=false` 时适用。 |
   ^^required_regions |[]string |["GB","MY","PH","SG","TH","VN"] |该属性无条件必填的市场。当 `is_requried=true` 时，此列表包含卖家的所有市场。当 `is_requried=false` 时，它仅包含该属性无条件必填的市场。当没有无条件必填的市场时，此字段会省略。

可能的值：

* AT: 奥地利
* BE: 比利时
* CZ: 捷克共和国
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU: 匈牙利
* ID: 印度尼西亚
* IT: Italy
* IE: 爱尔兰
* JP: Japan
* MY: 马来西亚
* NL: 荷兰
* PH: 菲律宾
* PL: 波兰
* PT: 葡萄牙
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥 |

# 响应示例
```json
{"code":0,"data":{"attributes":[{"id":"100392","name":"Occasion","type":"PRODUCT_PROPERTY","is_requried":false,"values":[{"id":"1001533","name":"Birthday"}],"is_multiple_selection":false,"is_customizable":false,"requirement_conditions":[{"region":"IE","condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}],"optional_regions":["US"],"required_regions":["GB","MY","PH","SG","TH","VN"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052700 | 卖家不活跃。 |
| 12052704 | 卖家 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

