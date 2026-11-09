# 获取全球复制商品

# 路径：/product/202507/products/{product_id}/replicated_products
# 方法：[GET]
# 功能描述
如果商品已通过本地复制完成复制，则获取其他市场中与之全局关联的副本。
仅适用于全球卖家。

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
| product_id | string | Y | 1732064081124754497 | 商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202507/products/1732064081124754497/replicated_products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^replicated_products | []object |  | 其他市场中与所请求商品关联的副本。不包含所请求的源商品。当未找到其他关联副本时返回空数组。 |
| ^^region | string | US | 与已复制商品关联的市场。 |
| 可能的值： |  |  |  |

* AT: 奥地利
* BE:Belgium
* CZ:捷克
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU:Hungary
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MY: 马来西亚
* NL: 荷兰(NL)
* PH: 菲律宾
* PO: Poland
* PT:Portugal
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥 |
   ^^shop_id |string |1732057700058170433 |The TikTok Shop ID. |
   ^^product_id |string |1732057700058170433 |商品的 ID。 |
   ^^product_status |string |ACTIVATE |复制商品的状态。
   可能的值：
* UNKNOWN
* DRAFT
* PENDING
* FAILED
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED |

# 响应示例
```json
{"code":0,"data":{"replicated_products":[{"region":"US","shop_id":"1732057700058170433","product_id":"1732057700058170433","product_status":"ACTIVATE"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

