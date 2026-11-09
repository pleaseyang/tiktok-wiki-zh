# 取消订单

# 路径：/return_refund/202602/cancellations
# 方法：[POST]
# 功能描述
使用此接口代表卖家取消订单。在 US 和 UK 市场，当商品缺货时，此接口支持在单个商品层面进行部分取消。

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
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 577087614418520388 | TikTok Shop 订单 ID |
| skus | []object | N |  | 要取消的 SKU 列表 |
| ^sku_id | string | Y | 1729386416015578024 | 要取消的 SKU ID |
| ^quantity | int | Y | 1 | 要取消的 SKU 数量 |
| order_line_item_ids | []string | N | ["577087614418716996"] | 要取消的订单行项目 ID 列表。在美国和英国市场，当商品缺货时，支持在单个商品级别进行部分取消。要发起部分取消，请指定该商品的订单行 ID。**说明：**这是旧版字段。对于新集成，请改用 `order_line_list`。请勿在同一请求中同时为 `order_line_item_ids` 和 `order_line_list` 提供非空值。 |
| cancel_reason | string | Y | ecom_order_delivered_refund_and_return_reason_wrong_product_seller | 取消订单的原因。要获取此订单的原因，请使用相同的 `order_id`、`initiate_aftersale_user=SELLER` 和 `request_types=CANCEL` 调用 `GET /return_refund/202602/orders/{order_id}/aftersale_eligibility`。从相应的 `data.sku_eligibility[].line_item_eligibility[]` 结果中，取 `available_reason_names` 中的一个精确值作为 `cancel_reason` 传入。有关卖家取消原因的更多指导，请参见 "Return API Overview"。 |
| order_line_list | []object | N |  | 要取消的订单行或子订单行列表。在美国和英国市场，当商品缺货时，支持在单个商品级别进行部分取消。**说明：**此字段与之前的 `order_line_item_ids` 字段完全向后兼容。请勿在同一请求中同时为 `order_line_list` 和 `order_line_item_ids` 提供非空值。 |
| ^order_line_item_id | string | N | 576469648086306986 | 对应的订单行 ID |
| ^sub_order_line_item_id | string | N | 576469648086306987 | 组合商品内的子订单行 ID |

* 组合商品必填
* 非组合商品非必填 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202602/cancellations?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_id":"577087614418520388","skus":[{"sku_id":"1729386416015578024","quantity":1}],"order_line_item_ids":["577087614418716996"],"cancel_reason":"ecom_order_delivered_refund_and_return_reason_wrong_product_seller","order_line_list":[{"order_line_item_id":"576469648086306986","sub_order_line_item_id":"576469648086306987"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^cancel_id | string | 4035319218955782461 | 特定订单取消的标识符。 |
| ^cancel_status | string | CANCELLATION_REQUEST_SUCCESS | 订单取消请求的状态。 |
| Available values: |  |  |  |

* `CANCELLATION_REQUEST_PENDING`
* `CANCELLATION_REQUEST_SUCCESS`
* `CANCELLATION_REQUEST_CANCEL`
* `CANCELLATION_REQUEST_COMPLETE` |

# 响应示例
```json
{"code":0,"data":{"cancel_id":"4035319218955782461","cancel_status":"CANCELLATION_REQUEST_SUCCESS"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查参数类型和格式是否正确。 |
| 25001011 | 退货请求已在处理中，或订单已被取消。 |
| 25001014 | Unknown return reason. Please ensure you are passing a valid return reason. |
| 25001015 | The provided return reason cannot be used by the seller. Please select a valid return reason and try again. |
| 25001020 | The provided return reason is currently offline. Please select a different return reason. |
| 25001021 | Reason not match order status |
| 25001028 | reverse lock failed |
| 25001045 | 订单已发货，我们无法向承运商取消配送。 |
| 25001046 | Return request has failed due to an interception by TikTok risk control. |
| 25001051 | Not allowed to return or cancel since order is completed or cancelled |
| 25005010 | Unable to cancel individual line items within this request. |
| 25005011 | 请求的退货或退款订单行超出允许的上限。 |
| 25020005 | 无权处理此订单 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

