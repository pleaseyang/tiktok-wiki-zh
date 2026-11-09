# 获取订单海关要求

# 路径：/fulfillment/202607/orders/customs_info/query
# 方法：[POST]
# 功能描述
此 API 用于查询订单是否需要额外的清关信息、此类信息是否已提交以及已提交的清关信息列表。
如果需要额外的清关信息但尚未提供，卖家必须在发货前完成并提交。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_ids | []string | Y | ["584882846571464153","584881010662934016"] | 要查询的 TikTok Shop 订单 ID。提供请求 body 时，包含 1 到 50 个订单 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202607/orders/customs_info/query?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"order_ids":["584882846571464153","584881010662934016"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^order_clearance_list | []object |  | 此订单的清关信息 |
| ^^order_id | string | 584882846571463232 | TikTok Shop 订单 ID |
| ^^need_fill_clearance | bool | true | 订单是否需要填写海关信息： |

* true：订单需要填写海关信息。
* false：订单不需要填写海关信息。 |
   ^^already_filled_clearance |bool |false |当 `need_fill_clearance` 为 `true` 时，是否已为每个需要清关信息的订单行提交了清关信息。当 `need_fill_clearance` 为 `false` 时，此值为 `false`。 |
   ^^target_country |string |JP |国家 Alpha-2 代码 |
   ^^biz_type |int |1 |enum CustomsBusinessType {
   CustomsBusinessTypeFS = 1;
   CustomsBusinessTypePOP = 2;
   } |
   ^^shipment_type |int |1 |enum ShipmentType{
   CROSS_BORDER = 1,
   LOCAL = 2,
   } |
   ^^item_list |[]object | |订单的订单行详情。 |
   ^^^order_line_id |string |584882846571423334 |子订单 ID |
   ^^^product_id |string |1729476373250999503 |商品 ID。 |
   ^^^sku_id |string |1735885807280883357 |SKU ID。 |
   ^^^is_virtual_unboxing |bool |true |此子订单是否为 virtual_unboxing |
   ^^^is_temporary_listing |bool |false |此子订单是否为 temporary_listing |
   ^^^related_item_detail |[]object | |此订单行已提交的清关商品详情，按 SKU 汇总。 |
   ^^^^product_id |string |1729476373250999503 |商品 ID。 |
   ^^^^sku_id |string |1735885807280883357 |SKU ID。 |
   ^^^^qty |int |2 |此 SKU 的数量 |
   ^^^^price_percent |int |10 |单位：% ，price_percent=10 表示 10% |

# 响应示例
```json
{"code":0,"data":{"order_clearance_list":[{"order_id":"584882846571463232","need_fill_clearance":true,"already_filled_clearance":false,"target_country":"JP","biz_type":1,"shipment_type":1,"item_list":[{"order_line_id":"584882846571423334","product_id":"1729476373250999503","sku_id":"1735885807280883357","is_virtual_unboxing":true,"is_temporary_listing":false,"related_item_detail":[{"product_id":"1729476373250999503","sku_id":"1735885807280883357","qty":2,"price_percent":10}]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 11001002 | 参数无效。 |
| 11036004 | 系统错误，请重试 |

