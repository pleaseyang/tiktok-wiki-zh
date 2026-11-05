# 搜索尺码表

# Path: /product/202407/sizecharts/search
# Method: [POST]
# 功能描述
获取卖家已创建的尺码表。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | Y | 10 | 每页返回的结果数量。 |
| Valid range: [1-100] |  |  |  |  |
| page_token | string | N | cGFnZV9udW1iZXI9Mg== | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
| locales | []string | N | en-US,es-ES | 用于显示尺码表的 BCP-47 语言环境代码。 |
| Default: 您店铺的默认语言环境。 |  |  |  |  |
| Possible values: |  |  |  |  |

* de-DE
* en-GB
* en-IE
* en-US
* es-ES
* es-MX
* fr-FR
* id-ID
* it-IT
* ja-JP
* ms-MY
* pt-BR
* th-TH
* vi-VN
* zh-CN |

# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| ids | []string | N | ["7362027385890244398"] | 按尺码表模板 ID 过滤尺码表。 |
| Max: 50 IDs |  |  |  |  |
| keyword | string | N | size chart | 按尺码表模板名称或模板名称中的关键词过滤尺码表。 |
| Keyword searches do not return PRODUCT_SCOPED size charts because they do not have a template name. |  |  |  |  |
| If both ids and keyword are provided, ids takes priority. |  |  |  |  |
|  |  |  |  |  |
| size_chart_mode | string | N | REUSABLE_TEMPLATE | 按使用模式过滤尺码表。 Possible values: REUSABLE_TEMPLATE: A size chart template that can be reused across multiple products. PRODUCT_SCOPED: A size chart created for and used by a single product. If omitted, the existing search behavior is preserved. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202407/sizecharts/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_size=10&page_token=cGFnZV9udW1iZXI9Mg==&locales=en-US,es-ES
```

**Body**
```json
{"ids":["7362027385890244398"],"keyword":"size chart","size_chart_mode":"REUSABLE_TEMPLATE"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^size_chart | []object |  | 符合查询条件的尺码表列表。 |
| ^^template_id | string | 7362027385890244398 | 尺码表模板 ID。 |
| ^^template_name | string | size chart | 尺码表模板名称。 |
| ^^images | []object |  | 尺码表中包含的图片列表。 |
| ^^^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | The URI to identify the image in API requests and responses. |
| ^^^url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036 | 访问和查看图片的 URL。 |
| ^^^locale | string | en-US | 尺码表图片的语言。 |
| ^^related_category_ids | []string | ["601739","601740"] | 适用于此尺码表的叶子分类 ID。 |
| ^^size_chart_datas | []object |  | 本地化的结构化尺码表数据。 Each item contains a locale and the structured data for that locale. |
| ^^^locale | string | en-US | 尺码表表格的语言。 |
| ^^^size_chart_data | object |  | 指定语言环境的结构化尺码表数据。 |
| ^^^^table | object |  | 包含表头和行的结构化表格。 |
| ^^^^^headers | []object |  | 有序的表头定义。 |
| ^^^^^^name | string | Bust (cm) | 表头显示名称。 |
| ^^^^^^id | string | size_chart_size_system_size | 标准尺码体系 ID 或测量键。 |
| ^^^^^rows | []object |  | 尺码表的行。 |
| ^^^^^^cells | []object |  | 按索引与 table.headers 对齐的单元格。 |
| ^^^^^^^value | string | M | 单元格值。 |
| ^^^^description | string | Use body measurements. | 额外的尺码表描述。 |
| ^^^^is_one_size | bool | false | 是否为均码表。 |
| ^^^^measurement_type | string | BODY_MEASUREMENTS | Possible values: GENERIC_MEASUREMENTS: generic measurements; BODY_MEASUREMENTS: shopper body measurements; PRODUCT_MEASUREMENTS: finished-product measurements. |
| ^^^^unit_system | string | METRIC | Possible values: METRIC: metric units; IMPERIAL: imperial units. |
| ^^^^size_types | []string | ["size_chart_size_type_regular"] | Possible values include: size_chart_common_size_type: Common; size_chart_size_type_regular: Regular; size_chart_size_type_juniors: Juniors; size_chart_size_type_plus: Plus; size_chart_size_type_big&tall: Big & Tall; size_chart_size_type_petite: Petite. Available values depend on the category. |
| ^^size_chart_mode | string | REUSABLE_TEMPLATE | 按使用模式过滤尺码表。 Possible values: REUSABLE_TEMPLATE: A size chart template that can be reused across multiple products. PRODUCT_SCOPED: A size chart created for and used by a single product. If omitted, the existing search behavior is preserved. |
| ^^target_regions | []string | ["US","GB"] | Target country or market codes recorded for this size chart, used for localized content and images. The list may include historical targets. Omitted when no target regions are recorded; omission does not mean worldwide support. This field does not determine product publishing eligibility. |
| ^next_page_token | string | cGFnZV9udW1iZXI9Mg== | 用于获取分页结果集下一页的不透明 token。如果此值非空，请将其传递给下一个请求的 `page_token` 参数。空值表示没有更多结果。 |
| ^total_count | int | 100 | 符合查询条件的尺码表数量。 |
# 响应示例
```json
{"code":0,"data":{"size_chart":[{"template_id":"7362027385890244398","template_name":"size chart","images":[{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe","url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036","locale":"en-US"}],"related_category_ids":["601739","601740"],"size_chart_datas":[{"locale":"en-US","size_chart_data":{"table":{"headers":[{"name":"Bust (cm)","id":"size_chart_size_system_size"}],"rows":[{"cells":[{"value":"M"}]}]},"description":"Use body measurements.","is_one_size":false,"measurement_type":"BODY_MEASUREMENTS","unit_system":"METRIC","size_types":["size_chart_size_type_regular"]}}],"size_chart_mode":"REUSABLE_TEMPLATE","target_regions":["US","GB"]}],"next_page_token":"cGFnZV9udW1iZXI9Mg==","total_count":100},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019108 | page number is invalid |
| 12019109 | page size is invalid |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

