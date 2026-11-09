# 计算退款

# 路径：/return_refund/202602/refunds/calculate
# 方法：[POST]
# 功能描述
使用此 API 估算取消、退款或退货退款请求的可退款金额。估算结果取决于所选的 request_type、reason_name 和目标商品。如果 skus、order_line_item_ids 和 order_line_list 均被省略，则订单中的所有订单行将被选为退款计算的输入。对于退货退款场景，估算结果还可能取决于所选的退货物流方式。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 576469648086175911 | TikTok Shop 订单 ID。 |
| request_type | string | Y | REFUND | 请求类型 |

* CANCEL
* REFUND
* RETURN_AND_REFUND
   注意：不同的请求类型用于不同的售后场景。同时，不同的请求类型可能有不同的退款金额，因为退款金额计算策略不同。 |
   shipment_type |string |N |PLATFORM |在退货请求中 buyer 如何将商品寄回给卖家，可以是：
* `PLATFORM`
* `BUYER_ARRANGE` |
   handover_method |string |N |DROP_OFF |buyer 在使用平台退货时选择的交接方式
* `DROP_OFF`：buyer 将包裹送到物流服务收集点。
* `PICKUP`：物流服务上门取件。 |
   reason_name |string |Y |ecom_order_delivered_refund_reason_missing_product_seller |卖家对所选取消、退款或退货退款请求的原因。使用 [Get Aftersale Eligibility](https://partner.tiktokshop.com/docv2/page/69c3070c66dee40493fdfe2e) endpoint 检索当前可用的原因，并在此字段中提交返回的原因 name。 |
   order_line_item_ids |[]string |N |["576469648086306986"] |纳入退款计算的 TikTok Shop 订单行项目 ID。请勿在同一请求中同时为 `order_line_item_ids` 和 `order_line_list` 提供非空值。 |
   skus |[]object |N | |skus |
   ^sku_id |string |Y |1729386416015578024 |纳入退款计算的 TikTok Shop SKU ID。 |
   ^quantity |int |Y |1 |纳入退款计算的此 SKU 的数量。 |
   order_line_list |[]object |N | |纳入退款计算的订单行。当您需要识别捆绑商品中的各个子商品时使用此字段。**注意：** 此字段与之前的 `order_line_item_ids` 字段完全向后兼容。请勿在同一请求中同时为 `order_line_list` 和 `order_line_item_ids` 提供非空值。 |
   ^order_line_item_id |string |N |576469648086306986 |对应的订单行 ID |
   ^sub_order_line_item_id |string |N |576469648086306987 |捆绑商品内的子订单行 ID
* 捆绑商品必填
* 非捆绑商品无需填写 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202602/refunds/calculate?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_id":"576469648086175911","request_type":"REFUND","shipment_type":"PLATFORM","handover_method":"DROP_OFF","reason_name":"ecom_order_delivered_refund_reason_missing_product_seller","order_line_item_ids":["576469648086306986"],"skus":[{"sku_id":"1729386416015578024","quantity":1}],"order_line_list":[{"order_line_item_id":"576469648086306986","sub_order_line_item_id":"576469648086306987"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^order_refund_amount | object |  | 退还给 buyer 的退款金额。 |
| ^^currency | string | USD | 付款币种。 |
| ^^refund_total | string | 1.23 | 退还给 buyer 的总金额。 |
| ^^refund_subtotal | string | 1 | 计算退款中包含的小计金额。 |
| ^^refund_shipping_fee | string | 0.2 | 退还给 buyer 的运费。 |
| ^^refund_tax | string | 0.03 | 退还给 buyer 的税额。 |
| ^^retail_delivery_fee | string | 0.1 | 根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。 |
# 响应示例
```json
{"code":0,"data":{"order_refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查您是否具有正确的参数类型和格式。 |
| 25007006 | Order not found. |

