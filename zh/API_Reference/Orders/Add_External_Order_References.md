# 添加外部订单引用

# Path: /order/202406/orders/external_orders
# Method: [POST]
# 功能描述
如果您使用外部订单管理系统（OMS），其订单和订单行 ID 可能与相应的 TikTok Shop ID 不同。使用此 endpoint 可将外部 OMS 引用附加到最多 100 个 TikTok Shop 订单。要更新现有引用，请使用相同的 TikTok Shop 订单和 OMS 再次调用此 endpoint。每个订单独立处理。在 API 成功响应时，未在 `data.errors` 中列出的订单的引用已保存；请使用该列表识别每个订单的错误。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| orders | []object | 是 |  | 要添加或更新外部 OMS 引用的订单。最小数量：1。最大数量：100。 |
| ^id | string | 是 | 576461413038785752 | TikTok Shop 订单的唯一标识符。 |
| ^external_order | object | 是 |  | 您的外部订单管理系统（OMS）中的订单信息。 |
| ^^id | string | 是 | 676461413038785752 | 您的 OMS 中对应的订单 ID。 |
| ^^platform | string | 是 | SHOPIFY | 您的 OMS 的别名。 |
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
* ERP_SYSTEM

说明：

* 要将多个 OMS 的信息附加到 TikTok Shop 中的同一订单，请多次调用此 API，每次使用相同的 TikTok Shop 订单和不同的 OMS。
* 要编辑 TikTok Shop 订单的已附加信息，请使用相同的 OMS 调用 API。 |
   ^^line_items |[]object |是 | |最大数量：100。 |
   ^^^id |string |是 |577086512123755123 |您的 OMS 中的订单行 ID。 |
   ^^^origin_id |string |是 |677086512123755123 |TikTok Shop 中的订单行 ID。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202406/orders/external_orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"orders":[{"id":"576461413038785752","external_order":{"id":"676461413038785752","platform":"SHOPIFY","line_items":[{"id":"577086512123755123","origin_id":"677086512123755123"}]}}]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 每个订单的错误。每个条目标识一个无法处理的 TikTok Shop 订单及其外部 OMS 引用。在 API 成功响应时，未在此处列出的订单的引用已保存，即使此列表非空。 |
| ^^code | string | 36020001 | 此订单级错误的机器可读代码。 |
| ^^message | string | Invalid order_id | 描述此订单级错误的人类可读消息。 |
| ^^detail | object |  | 与此订单级错误关联的 TikTok Shop 订单和外部 OMS 引用。 |
| ^^^order_id | string | 576461413038785752 | TikTok Shop 订单的唯一标识符。 |
| ^^^external_order | object |  | 您的 OMS 中的订单信息。 |
| ^^^^id | string | 676461413038785752 | 您的 OMS 中对应的订单 ID。 |
| ^^^^platform | string | SHOPIFY | 您的 OMS 的别名。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":"36020001","message":"Invalid order_id","detail":{"order_id":"576461413038785752","external_order":{"id":"676461413038785752","platform":"SHOPIFY"}}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

