# 批准退货

# 路径：/return_refund/202309/returns/{return_id}/approve
# 方法：[POST]
# 功能描述
使用此 API 批准 buyer 的退货请求。具体效果取决于退货类型和退货状态。在调用此 API 之前，请确保退货仍处于等待卖家执行与您发送的决策相匹配的操作状态。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| return_id | string | Y | 4035319218955782461 | 待卖家批准的退货请求的唯一标识符。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| idempotency_key | string | N | 40b456b1-78e7-412d-9fe6-82181496e1bd | 由客户端生成的唯一值，服务器用于识别重复请求。重试相同请求时请复用相同的 key。如果省略，服务器将为该次调用生成一个 key。您可以使用 UUID 或其他具有足够熵的随机字符串以避免冲突。最大长度：255 个字符。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| decision | string | Y | APPROVE_REFUND | 卖家对退货请求的决策，可用值： |

* `APPROVE_REFUND`：卖家批准仅退款请求
* `APPROVE_RETURN`：卖家批准初始退货退款请求
* `APPROVE_RECEIVED_PACKAGE`：卖家在 buyer 已发货或交出商品后批准退货退款请求
* `APPROVE_REPLACEMENT`：卖家批准换货请求
* `ISSUE_REPLACEMENT_REFUND`：卖家拒绝换货请求并直接退款给 buyer
* `OFFER_PARTIAL_REFUND`：卖家向 buyer 提供部分退款金额，无需退回商品
* `DIRECT_REFUND`：卖家发放无退货退款，即 buyer 获得全额退款并保留商品 |
   buyer_keep_item |bool |N |true |**可选**。仅当 decision 设置为 `APPROVE_RETURN` 时使用此字段。如果设置为 `true`，卖家发放无退货退款，即 buyer 获得全额退款并保留商品。如果设置为 `false` 或省略，卖家批准退货退款流程，buyer 退回商品。 |
   partial_refund |object |N | |当 `decision` 设置为 `OFFER_PARTIAL_REFUND` 时**必填**。提供 `partial_refund` 时，`amount` 和 `currency` 均为必填。其他决策请省略此字段。 |
   ^currency |string |N |IDR |退款币种必须与当前退货请求的币种一致。 |
   ^amount |string |N |10 |卖家希望向 buyer 提供的部分退款金额 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202309/returns/4035319218955782461/approve?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&idempotency_key=40b456b1-78e7-412d-9fe6-82181496e1bd
```

**Body**
```json
{"decision":"APPROVE_REFUND","buyer_keep_item":true,"partial_refund":{"currency":"IDR","amount":"10"}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 11050001 | invalid param |
| 25001001 | 传递了无效的请求参数。请检查您是否具有正确的参数类型和格式。 |
| 25001003 | 无效的订单状态。 |
| 25001028 | reverse lock failed |
| 25001044 | ConfirmReceive fulfillment order failed |
| 25001058 | reverse downstream data load error |
| 25007006 | Order not found. |
| 25007007 | ReverseOrderExistNegotiate |
| 25011010 | request has been transferred to platform operator |
| 25011012 | reverse status cannot approve application |
| 25011013 | reverse status cannot approve receive |
| 25011023 | forbid process authentic guarantee order |
| 25011026 | forbid process receive for FBT order |
| 25011032 | ReverseInvalidStatusPartialRefund |
| 25020004 | decision not match reverse type |
| 25020005 | 无权处理此订单 |
| 25020008 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 25020009 | reverse already cancelled |

