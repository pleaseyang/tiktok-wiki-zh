# 审核售后请求

# Path: /return_refund/202609/aftersales/review
# Method: [POST]
# 功能描述
用于审核（批准、拒绝或提供替代方案）buyer 退货请求的 API。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| aftersales_request_decisions | []object | N |  | 应用于售后请求的决策。 |
| ^request_id | string | Y | 4035319218955782461 | 标识此决策所应用的对象。 |
| ^request_id_type | string | N | AFTERSALES | request_id 中提供的标识符类型。 |
| 可能的值： |  |  |  |  |

* `AFTERSALES`
* `RMA` |
   ^line_item_decisions |[]object |Y | |在行项目级别应用的决策。
   一个 SKU 只能有一个决策，因此所有行项目（对应于同一 SKU）应归属于同一决策对象。
   同一 SKU 的不同行项目决策将在未来得到支持。
   |
   ^^line_items |[]object |Y | |此决策适用的行项目。决策详情逐个应用于每个行项目（例如，3 个行项目各 1.00 美元的部分退款金额将导致总部分退款金额为 3.00 美元）。 |
   ^^^return_line_item_id |string |Y |4035227657962164811 |此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于原始父商品捆绑的 id。 |
   ^^^sub_return_line_item_id |string |N |4035227657962164815 |此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于当前被退货的子商品的 id。 |
   ^^action |string |Y |APPROVE_REQUEST |要应用的行动/决策。
   可能的值：
* `APPROVE_REQUEST`
* `APPROVE_RETURN_PACKAGE`
* `REJECT_REQUEST`
* `REJECT_RETURN_PACKAGE`
* `REFUND_INSTEAD`
* `OFFER_PARTIAL_REFUND`
* `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` |
   ^^alternative_solution_details |object |N | |替代解决方案的详情（如适用）。 |
   ^^^partial_refund_amount |string |N |12.34 |提议的退款金额。 |
   ^^^currency |string |N |USD |退款金额的币种（ISO 4217）。必须与正向订单的币种一致。 |
   ^^reason |object |N | |用于证明行动/决策的合理性（拒绝时通常需要）。 |
   ^^^reason_id |string |N |seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |Seller 拒绝售后请求的原因。使用 [Get Review Decision](https://partner.tiktokshop.com/docv2/page/get-review-decision-202606) endpoint 检索当前可用于同一请求的拒绝选项，并在此字段中提交返回的拒绝原因 name。
   **注意**：可用的决策和拒绝原因可能会根据当前请求状态而变化，因此在调用此 API 之前请重新获取资格。 |
   ^^^text |string |N |I have reached an agreement with the buyer |决策的附加说明。 |
   ^^^media |object |N | |支持性证据（如图片）。 |
   ^^^^uri |string |N |tos-maliva-i-o3syd03w52-us/57a1c8908fe74572861ea5e50887d8d1 |从 [Upload Product Image](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) API 获取的图片 URI。 |
   ^^^^mime_type |string |N |image/png |媒体的 MIME 类型（如 image/jpeg）。 |
   ^action_unix_time |int |N |1774486592 |做出决策/行动的时间戳（Unix 秒）。 |
   ^idempotency_key |string |N |40b456b1-78e7-412d-9fe6-82181496e1bd&app_key=38abcd |幂等性 key 是由客户端生成的唯一值，服务器用于识别相同请求。如何创建唯一 key 由您决定，但我们建议使用 UUID 或其他具有足够熵的随机字符串以避免冲突。幂等性 key 最长可达 255 个字符。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202609/aftersales/review?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"aftersales_request_decisions":[{"request_id":"4035319218955782461","request_id_type":"AFTERSALES","line_item_decisions":[{"line_items":[{"return_line_item_id":"4035227657962164811","sub_return_line_item_id":"4035227657962164815"}],"action":"APPROVE_REQUEST","alternative_solution_details":{"partial_refund_amount":"12.34","currency":"USD"},"reason":{"reason_id":"seller_reject_apply_package_has_not_exceeded_estimated_delivery_time","text":"I have reached an agreement with the buyer","media":{"uri":"tos-maliva-i-o3syd03w52-us/57a1c8908fe74572861ea5e50887d8d1","mime_type":"image/png"}}}],"action_unix_time":1774486592,"idempotency_key":"40b456b1-78e7-412d-9fe6-82181496e1bd\u0026app_key=38abcd"}]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 列出部分失败请求的错误。例如，如果请求审核了多个订单或商品且只有部分失败，则各个错误详情将在此处返回。 |
**重要**：部分失败仍返回顶级成功代码（0），因此客户端还必须检查此字段以检测部分错误。对于完全失败（如验证错误），顶级响应代码和消息将指示失败，但此字段将保持为空。 |
^^code |string |98001004 |错误码。 |
^^message |string |Invalid parameters. Please verify your input before retrying |错误描述。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":"98001004","message":"Invalid parameters. Please verify your input before retrying"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
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
| 25020005 | No permission to process this order |
| 25020008 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 25020009 | reverse already cancelled |

