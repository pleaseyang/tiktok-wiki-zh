# 获取商品包装建议

# 路径：/product/202602/packages/recommend
# 方法：[POST]
# 功能描述
获取商品包裹的推荐重量和尺寸范围。仅适用于 BR 和 MX。

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
| page_size | int | Y | 100 | 每页返回的结果数量。 |
| 有效范围： [1-100] |  |  |  |  |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_ids | []string | N | ["12345678", "12345679"] | 用于获取包裹推荐的商品 ID 的 JSON 数组。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202602/packages/recommend?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=100&page_token=b2Zmc2V0PTAK
```

**Body**
```json
{"product_ids":["12345678","12345679"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明令牌。如果当前响应未返回全部结果，请在请求的 `page_token` 参数中提供此值。 |
| ^total_count | int | 200 | 符合查询条件的商品总数。 |
| ^products | []object |  | 符合查询条件的商品包裹推荐。每一项标识一个商品，并提供检测到的异常类型以及可用的重量或尺寸修正范围。 |
| ^^product_id | string | 23423 | TikTok Shop 生成的商品 ID。 |
| ^^abnormality_types | []string | ["Dimension","Weight"] | 检测到的包裹异常类型。可选值： |

* `None`: 未检测到重量或尺寸异常。
* `Dimension`: 建议进行尺寸修正。
* `Weight`: 建议进行重量修正。 |
   ^^weight_recommendation |object | |重量校正建议 (仅当商品重量已被推荐时返回 )。 |
   ^^^unit |string |GRAM |重量单位，固定为 GRAM。 |
   ^^^weight |object | |重量的推荐取值。 |
   ^^^^min_value |string |550 |推荐范围最小值; 单位: g |
   ^^^^max_value |string |650 |推荐范围最大值; 单位: g |
   ^^dimension_recommendation |object | |尺寸修正建议（仅在已推荐商品尺寸时返回）。 |
   ^^^unit |string |CENTIMETER |尺寸单位，固定为厘米。 |
   ^^^length |object | |长度的推荐取值。 |
   ^^^^min_value |string |19 |推荐范围最小值；单位：cm |
   ^^^^max_value |string |22 |推荐范围最大值；单位：cm |
   ^^^height |object | |高度的推荐取值 (结构与长度相同)。 |
   ^^^^min_value |string |19 |推荐范围最小值；单位：cm |
   ^^^^max_value |string |22 |推荐范围最大值；单位：cm |
   ^^^width |object | |宽度的推荐取值 (结构与长度相同)。 |
   ^^^^min_value |string |19 |推荐范围最小值；单位：cm |
   ^^^^max_value |string |22 |推荐范围最大值；单位：cm |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTAK","total_count":200,"products":[{"product_id":"23423","abnormality_types":["Dimension","Weight"],"weight_recommendation":{"unit":"GRAM","weight":{"min_value":"550","max_value":"650"}},"dimension_recommendation":{"unit":"CENTIMETER","length":{"min_value":"19","max_value":"22"},"height":{"min_value":"19","max_value":"22"},"width":{"min_value":"19","max_value":"22"}}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

