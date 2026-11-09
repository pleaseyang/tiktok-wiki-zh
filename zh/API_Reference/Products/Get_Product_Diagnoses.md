# 获取商品诊断结果

# 路径：/product/202405/products/diagnoses
# 方法：[GET]
# 功能描述
诊断多个现有的在售（status: `ACTIVATE`）商品，获取有助于改进商品内容、提升商品可见度和客户信任度的信息。返回的信息包括：

* 上架质量信息（仅适用于 US 市场）。
* 当前商品详情存在的问题及总体建议
* 针对特定商品字段自动生成的优化建议，包括标题、描述和图片。
   **说明**：此 API 仅专注于优化商品可见性，不评估你的商品是否满足上架要求。此 API 识别出的质量问题不会阻止商品上架。要核验上架要求，请使用 [Check Product Listing API](650a0ee8f1fd3102b91c6493)。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| product_ids | []string | Y | 12345678,123456 | 要诊断的商品 ID 列表。 |
**注意**：

* 最大 ID 数量：200
* 商品必须已上架 (状态: `ACTIVATE`) |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202405/products/diagnoses?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&product_ids=12345678,123456
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 所请求商品及对应诊断结果的列表。 |
| ^^id | string | 123456 | 商品 ID。 |
| ^^listing_quality | object |  | 商品上架质量信息。 |
| ^^^current_tier | string | POOR | 此商品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc。 |
可能的值：

* POOR
* FAIR
* GOOD

**注意**：仅适用于美国市场。 |
^^^remaining_recommendations |int |3 |为使商品达到最高层级，仍需落实的建议数量（参见 `diagnosis_results`）。
**注意**：

* 要达到最高等级，必须落实 `diagnosis_results` 中列出的所有建议。
* 仅适用于美国市场。 |
   ^^diagnoses |[]object | |商品诊断与优化信息。 |
   ^^^field |string |TITLE |被诊断的商品字段。
   可能的值：
* TITLE：商品标题
* DESCRIPTION：商品描述
* IMAGE: 商品图片(商品实体中的 `main_images`)
* ATTRIBUTE：商品属性
* SIZE_CHART：商品尺码表 |
   ^^^diagnosis_results |[]object | |指定字段的诊断结果。 |
   ^^^^code |string |TITLE_LESS_THAN_40_CHARACTERS |代表已识别问题的机器可读代码。
   有关诊断问题的完整列表及相应建议，请参阅 [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd)。 |
   ^^^^how_to_solve |string |Names must be at least 40 characters long and contain product-identifying information, such as "hiking boots" or "lipstick". |解决已识别问题的建议，以店铺的默认语言返回。
   有关建议的完整列表，请参阅 [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd)。 |
   ^^^^quality_tier |string |GOOD |通过实施建议可以达到的上架质量等级。
   可能的值：
* FAIR
* GOOD

**注意**：

* 要达到更高层级，必须落实目标层级及之前所有层级的全部建议。例如，当所有 "FAIR" 和 "GOOD" 建议都得到处理或落实后，商品就会达到 "GOOD" 层级。
* 仅适用于美国市场。 |
   ^^^suggestion |object | |系统自动生成的优化建议，用于提升指定字段的效果。 |
   ^^^^seo_words |[]object | |商品标题的 SEO 关键词建议。 |
   ^^^^^text |string |dress |建议的 SEO 关键词。 |
   ^^^^smart_texts |[]object | |优化后的商品标题或描述列表。 |
   ^^^^^text |string |this is a good title |优化后的文本。 |
   ^^^^images |[]object | |根据商品 `main_images` 集合中的第一张图片生成的优化图片备选。 |
   ^^^^^height |int |600 |优化后的图片高度。 |
   ^^^^^width |int |600 |优化后的图片宽度。 |
   ^^^^^uri |string |tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d |图片的原始 URI。 |
   ^^^^^url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp |图片的原始 URL。 |
   ^^^^^optimized_uri |string |tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6 |优化后图片的 URI。 |
   ^^^^^optimized_url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp |优化后图片的 URL。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"id":"123456","listing_quality":{"current_tier":"POOR","remaining_recommendations":3},"diagnoses":[{"field":"TITLE","diagnosis_results":[{"code":"TITLE_LESS_THAN_40_CHARACTERS","how_to_solve":"Names must be at least 40 characters long and contain product-identifying information, such as \"hiking boots\" or \"lipstick\".","quality_tier":"GOOD"}],"suggestion":{"seo_words":[{"text":"dress"}],"smart_texts":[{"text":"this is a good title"}],"images":[{"height":600,"width":600,"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp","optimized_uri":"tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6","optimized_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp"}]}}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12009014 | seller no permission for product error |
| 12019114 | 卖家无权限 |
| 12019120 | 提供的商品 ID 数量超过限制。 |
| 12052260 | 商品 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

