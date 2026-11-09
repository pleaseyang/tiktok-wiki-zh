# 创建退货

# 路径：/return_refund/202602/returns
# 方法：[POST]
# 功能描述
使用此 API 代表买家为订单创建卖家发起的售后请求。支持的请求类型为 `REFUND` 和 `RETURN_AND_REFUND`。提交请求前，请确认该订单符合所选售后类型和退货方式。请求创建后，使用相应的搜索、状态或审核 API 继续售后流程。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时，如果未传递正确的值，将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | N | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | N | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | N | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| idempotency_key | string | N | 1623812664 | Idempotency Key |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 576473917261320779 | Tiktok Shop 订单 ID |
| skus | []object | N |  | Skus |
| ^sku_id | string | Y | 1729386416015578024 | 卖家要发起退货请求的 SKU ID |
| ^quantity | int | Y | 1 | 要纳入退货请求的该 SKU 数量。 |
| order_line_item_ids | []string | N | ["455764739172614518516"] | 指定退货请求中要包含的订单行 ID。当订单拆分为多个包裹时，使用此字段选择订单行。请勿在同一请求中同时为 `order_line_item_ids` 和 `order_line_list` 提供非空值。如果 `order_line_item_ids`、`order_line_list` 和 `skus` 都省略，则包含订单中的所有订单行。**说明：**这是旧版字段；新集成应改用 `order_line_list`。 |
| return_reason | string | Y | ecom_order_delivered_refund_reason_missing_product_seller | 卖家发起退货的原因 |
| return_type | string | Y | REFUND | 要创建的类型： |

* REFUND
* RETURN_AND_REFUND |
   refund_total |string |N |10.5 |向买家退款的总金额。
   总退款金额不能超过可退款金额 |
   currency |string |N |USD |退款金额的货币。应与 TikTok Shop 订单的货币一致。提供 `refund_total` 时必填。 |
   shipment_type |string |N |PLATFORM |指定买家在退货申请中将商品寄回给卖家时使用的退货配送方式。支持的取值:
* `PLATFORM`
* `BUYER_ARRANGE` |
   handover_method |string |N |DROP_OFF |**可选**。仅当 shipment_type 为 `PLATFORM` 时适用。指定买家通过平台支持的配送方式退货时使用的交接方式。支持的取值：
* `DROP_OFF`
* `PICKUP` |
   order_line_list |[]object |N | |指定退货请求中要包含的行项目，并支持组合订单拆分。每个条目都必须包含 `order_line_item_id`。对于组合子项目，还需包含 `sub_order_line_item_id`；普通订单行则省略 `sub_order_line_item_id`。请勿在同一请求中混用普通订单行和组合子项目。**说明：**此字段与旧版 `order_line_item_ids` 字段完全向后兼容。 |
   ^order_line_item_id |string |N |576469648086306986 |对应的订单行 ID |
   ^sub_order_line_item_id |string |N |576469648086306987 |组合商品内的子订单行 ID
* 组合商品必填
* 非组合商品非必填 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202602/returns?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&idempotency_key=1623812664
```

**Body**
```json
{"order_id":"576473917261320779","skus":[{"sku_id":"1729386416015578024","quantity":1}],"order_line_item_ids":["455764739172614518516"],"return_reason":"ecom_order_delivered_refund_reason_missing_product_seller","return_type":"REFUND","refund_total":"10.5","currency":"USD","shipment_type":"PLATFORM","handover_method":"DROP_OFF","order_line_list":[{"order_line_item_id":"576469648086306986","sub_order_line_item_id":"576469648086306987"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^return_id | string | 4035319218955782461 | 特定退货请求的标识符。 |
| ^return_status | string | RETURN_OR_REFUND_REQUEST_PENDING | 退货状态，可用取值: |

* RETURN_OR_REFUND_REQUEST_PENDING: 请求待处理，需由卖家或平台批准
* REFUND_OR_RETURN_REQUEST_REJECT: 卖家已拒绝该请求
* AWAITING_BUYER_SHIP：等待买家将商品寄送给卖家，若超过截止时间，请求将被平台关闭
* BUYER_SHIPPED_ITEM: 买家已将商品寄给卖家。
* REJECT_RECEIVE_PACKAGE: 卖家拒收退货包裹
* RETURN_OR_REFUND_REQUEST_SUCCESS: 退款/退货请求成功，将向买家退款。
* RETURN_OR_REFUND_REQUEST_CANCEL: 该请求已被买家或系统取消
* RETURN_OR_REFUND_REQUEST_COMPLETE: 请求成功，且金额已退款。 |

# 响应示例
```json
{"code":0,"data":{"return_id":"4035319218955782461","return_status":"RETURN_OR_REFUND_REQUEST_PENDING"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查参数类型和格式是否正确。 |
| 25001003 | Invalid order status. |
| 25001010 | A return request has already been completed, or the order has already been cancelled. |
| 25001011 | 退货请求已在处理中，或订单已被取消。 |
| 25001014 | Unknown return reason. Please ensure you are passing a valid return reason. |
| 25001015 | The provided return reason cannot be used by the seller. Please select a valid return reason and try again. |
| 25001020 | The provided return reason is currently offline. Please select a different return reason. |
| 25001021 | Reason not match order status |
| 25001028 | reverse lock failed |
| 25001042 | Return package creation has failed due to internal error. |
| 25001046 | Return request has failed due to an interception by TikTok risk control. |
| 25001051 | Not allowed to return or cancel since order is completed or cancelled |
| 25005005 | Refund total amount is larger than the refundable amount. |
| 25005010 | Unable to cancel individual line items within this request. |
| 25005011 | 请求的退货或退款订单行超出允许的上限。 |
| 25020005 | 无权处理此订单 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

