# 更新库存操作设置

# Path: /product/202608/inventory/operation/settings
# Method: [POST]
# 功能描述
Configure auto-restock behavior for 1 to 500 SKUs in one request. For seller-fulfilled orders, this setting controls whether inventory reserved for a canceled order is returned to the SKU's available inventory.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| seller_id | string | Y | 124129082343241 | Identifies the seller whose settings are being modified. |
| sku_ids | []string | N | ["124148921741214"] | List of specific SKU IDs. Up to 500 SKUs in a batch. |
| stock_operation_setting | object | N |  | The canceled-order auto-restock configuration to apply to the specified SKUs. |
| ^enable_auto_restock | bool | N | false | Controls automatic inventory replenishment after a seller-fulfilled (FBM) order is canceled. When at least one SKU is supplied, omitting `stock_operation_setting` or `enable_auto_restock` uses `false`. |

* `true`: Enable automatic replenishment for the specified SKUs.
* `false`: Disable automatic replenishment for the specified SKUs. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202608/inventory/operation/settings?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"seller_id":"124129082343241","sku_ids":["124148921741214"],"stock_operation_setting":{"enable_auto_restock":false}}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^stock_operation | object |  | The update result of stock operation |
| ^^failed_sku_ids | []string | ["124148921741214"] | Update inventory rule failed SkuID list |
| ^^success_sku_ids | []string | ["124148921741214"] | List of SkuIDs that successfully updated inventory rules |
# 响应示例
```json
{"code":0,"data":{"stock_operation":{"failed_sku_ids":["124148921741214"],"success_sku_ids":["124148921741214"]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12001017 | sku id is invalid |
| 12019017 | The stock of SKU exceed the limit |
| 12019112 | seller id is invalid |
| 12019114 | Seller has no permission |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

