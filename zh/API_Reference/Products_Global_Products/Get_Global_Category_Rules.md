# 获取全球分类规则

# 路径：/product/202309/categories/{category_id}/global_rules
# 方法：[GET]
# 功能描述
获取在特定类目下上架全球商品的附加要求（必填商品属性之外），不受市场差异影响。要求可能包括商品认证、尺码表、尺寸等。
使用此接口确定上架全球商品前必须准备的辅助信息。
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
| category_version | string | N | v1 | 按分类树版本过滤分类。基于地区的可能值： |

* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |
   locale |string |N |en-GB |用于显示分类信息的 BCP-47 语言环境代码。
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
https://open-api.tiktokglobalshop.com/product/202309/categories/600001/global_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_version=v1&locale=en-GB
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
^^id |string |7267563252536723205 |用于标识所需认证类型的 ID。 |
^^name |string |product_cert_name |认证类型的名称。 |
^^is_required |bool |false |指示认证是否**全局**必填的标志。

* true: 所有地区均要求提供该认证。
* false：该认证仅在部分地区为必填，或仅在满足特定条件时必填。具体要求请参阅 `required_regions` 和 `requirement_conditions`。 |
   ^^sample_image_url |string |https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg |查看示例认证文件图片的 URL。 |
   ^^required_regions |[]string |["GB","MY","PH","SG","TH","VN"] |无条件要求提供该认证的市场。
   可能的值：
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* ID: 印度尼西亚
* IT: Italy
* IE: 爱尔兰
* JP: Japan
* MY: 马来西亚
* PH: 菲律宾
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥

仅当 `is_required=false` 时适用。 |
^^optional_regions |[]string |["US"] |认证纯属可选、或仅在特定条件下为必填的市场。有关附条件要求市场的详细信息，请参阅 `requirement_conditions`。
可能的值：

* AT: 奥地利
* BE: 比利时
* CZ: Czechia
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU: 匈牙利
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MX: 墨西哥
* MY: 马来西亚
* NL: 荷兰
* PH: 菲律宾
* PL: 波兰
* PT: 葡萄牙
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南

仅当 `is_required=false` 时适用。 |
^^requirement_conditions |[]object | |条件列表，根据卖家为商品属性输入的内容判定某市场是否需要该认证。如果满足任一条件，则该认证为必填；否则为可选。
例如，有一个条件规定：如果卖家为属性 "Flammable Liquid?" 选择取值 "Yes"，则需要 "Safety Data Sheet (SDS) for flammable materials" 认证。有关使用此参数的更多基于场景的指导，请参考 [Solution Guide](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985)。
仅当 `optional_regions` 不为空时适用。 |
^^^region |string |IE |满足条件时该认证为必填项的市场。
可能的值：

* AT: 奥地利
* BE: 比利时
* CZ: Czechia
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU: 匈牙利
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MX: 墨西哥
* MY: 马来西亚
* NL: 荷兰
* PH: 菲律宾
* PL: 波兰
* PT: 葡萄牙
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南 |
   ^^^condition_type |string |VALUE_ID_MATCH |条件的类型。
   可能的值：
* VALUE_ID_MATCH：当卖家选择的取值 ID 与该条件中指定的 ID 匹配时，条件成立。 |
   ^^^attribute_id |string |101610 |被条件评估的商品属性的 ID。 |
   ^^^attribute_value_id |string |1024358 |必须与卖家输入匹配才能使条件为真的商品属性值的 ID。 |
   ^size_chart |object | |尺码表相关规则。 |
   ^^is_supported |bool |true |标识是否支持尺码表的标志。

**注意**： 如果不支持尺码表，即使您在创建或编辑商品时提供了尺码表，该尺码表也不会被保存。 |
^^is_required |bool |true |标识是否需要尺码表的标志。 |
^responsible_person |object | |负责人规则。
如果此项为空，表示该类目不需要责任人。
仅适用于 EU 市场。 |
^^is_required |bool |false |用于指示**所有欧盟市场**是否要求责任人的标志。

* true: 所有欧盟市场均要求提供制造商。
* false：仅在部分欧盟市场中制造商信息为必填。详情请参阅 `required_regions` 和 `optional_regions`。 |
   ^^optional_regions |[]string |["IE"] |负责人为可选项的市场。
   可能的值：
* DE: 德国
* ES: Spain
* FR: 法国
* IT: Italy
* IE: 爱尔兰 |
   ^^required_regions |[]string |["DE","ES"] |负责人为必填项的市场。
   可能的值：
* AT: 奥地利
* BE: 比利时
* CZ: Czechia
* DE: 德国
* ES: Spain
* FR: 法国
* GR: 希腊
* HU: 匈牙利
* IE: 爱尔兰
* IT: Italy
* NL: 荷兰
* PL: 波兰
* PT: 葡萄牙 |
   ^manufacturer |object | |制造商规则。
   如果此项为空，表示该类目不需要制造商。

仅适用于 EU 市场。 |
^^is_required |bool |false |用于指示制造商是否对 **所有 EU 市场** 均为必填的标志。

* true: 所有欧盟市场均要求提供制造商。
* false：仅在部分欧盟市场中制造商信息为必填。详情请参阅 `required_regions` 和 `optional_regions`。 |
   ^^optional_regions |[]string |["IE"] |制造商为可选的市场。
   可能的值：
* DE: 德国
* ES: Spain
* FR: 法国
* IT: Italy
* IE: 爱尔兰 |
   ^^required_regions |[]string |["DE","ES"] |制造商为必填项的市场。
   可能的值：
* AT: 奥地利
* BE: 比利时
* CZ: Czechia
* DE: 德国
* ES: Spain
* FR: 法国
* GR: 希腊
* HU: 匈牙利
* IE: 爱尔兰
* IT: Italy
* NL: 荷兰
* PL: 波兰
* PT: 葡萄牙 |

# 响应示例
```json
{"code":0,"data":{"product_certifications":[{"id":"7267563252536723205","name":"product_cert_name","is_required":false,"sample_image_url":"https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg","required_regions":["GB","MY","PH","SG","TH","VN"],"optional_regions":["US"],"requirement_conditions":[{"region":"IE","condition_type":"VALUE_ID_MATCH","attribute_id":"101610","attribute_value_id":"1024358"}]}],"size_chart":{"is_supported":true,"is_required":true},"responsible_person":{"is_required":false,"optional_regions":["IE"],"required_regions":["DE","ES"]},"manufacturer":{"is_required":false,"optional_regions":["IE"],"required_regions":["DE","ES"]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019002 | category is invalid |
| 12052023 | 分类不存在 |
| 12052024 | 分类不是最终分类 |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052220 | 该类目在 TikTok Shop 上被禁止或不受支持。请选择其他类目。 |
| 12052223 | 该类目受限。如需在该类目下销售，请通过 Seller Center 中的资质中心申请。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052700 | 卖家不活跃。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

