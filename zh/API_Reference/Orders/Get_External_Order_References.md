# 获取外部订单引用

# 路径：/order/202406/orders/{order_id}/external_orders
# 方法：[GET]
# 功能描述
如果您已使用 `Add External Order References` API，请使用此 API 检索与指定外部订单管理系统（OMS）平台的 TikTok Shop 订单关联的外部订单引用。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | 是 | 576461413038785752 | TikTok Shop 订单的唯一标识符。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| platform | string | 是 | SHOPIFY | 您的外部订单管理系统（OMS）的别名。 |
| 可能的值： |  |  |  |  |

* SHOPIFY
* WOOCOMMERCE
* BIGCOMMERCE
* MAGENTO
* SALESFORCE_COMMERCE_CLOUD
* CHANNEL_ADVISOR
* AMAZON
* ORDER_MANAGEMENT_SYSTEM
* WAREHOUSE_MANAGEMENT_SYSTEM
* ERP_SYSTEM |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202406/orders/576461413038785752/external_orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&platform=SHOPIFY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^external_orders | []object |  | 您的 OMS 和 TikTok Shop 之间已同步的订单列表。 |
注意：如果您已将多个 OMS 的订单信息同步到同一个 TikTok Shop 订单，您将检索到所有外部订单信息。 |
^^id |string |676461413038785752 |您的 OMS 中的订单 ID。 |
^^platform |string |SHOPIFY |您的 OMS 的别名。 |
^^line_items |[]object | |外部订单和 TikTok Shop 之间的订单行引用。 |
^^^id |string |577086512123755123 |您的 OMS 中的订单行 ID。 |
^^^origin_id |string |677086512123755123 |TikTok Shop 中的订单行 ID。
|
# 响应示例
```json
{"code":0,"data":{"external_orders":[{"id":"676461413038785752","platform":"SHOPIFY","line_items":[{"id":"577086512123755123","origin_id":"677086512123755123"}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

