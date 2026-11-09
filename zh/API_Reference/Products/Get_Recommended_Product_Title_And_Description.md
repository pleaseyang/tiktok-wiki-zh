# 获取推荐商品标题和描述

# 路径：/product/202405/products/suggestions
# 方法：[GET]
# 功能描述
为直播商品 (状态: `ACTIVATE`) 获取经 AI 优化的商品标题和描述。

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
| product_ids | []string | Y | 12345678,123456 | 要优化其信息的商品 ID。 |

* Max IDs: 20
* 商品必须已上架 (状态: `ACTIVATE`) |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202405/products/suggestions?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&product_ids=12345678,123456
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 返回的商品及其标题与描述建议。所请求的商品可能不会出现在响应中。对于返回的商品，`TITLE` 或 `DESCRIPTION` 的空 `items` 列表表示该字段没有可用的优化文本。 |
| ^^id | string | 123456 | 商品 ID。 |
| ^^suggestions | []object |  | 针对每个商品字段的建议。 |
| ^^^field | string | TITLE | 适用的商品字段。 |
| 可能的值： |  |  |  |

* TITLE
* DESCRIPTION |
   ^^^items |[]object | |优化后文本列表。 |
   ^^^^text |string |this is a good title |优化后的文本。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"id":"123456","suggestions":[{"field":"TITLE","items":[{"text":"this is a good title"}]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
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

