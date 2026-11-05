# 拒绝退货

# Path: /return_refund/202606/returns/{return_id}/reject
# Method: [POST]
# 功能描述
使用此 API 拒绝 buyer 的仅退款、退货退款或换货请求，或在收到包裹后提供部分退款。有效的决策取决于当前的请求类型和状态。在调用此 API 之前，请确保请求仍处于等待 seller 执行与您发送的决策相匹配的操作状态。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| return_id | string | Y | 4035319218955782461 | 待 seller 拒绝的退货请求的唯一标识符。 |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| idempotency_key | string | N | 40b456b1-78e7-412d-9fe6-82181496e1bd | 由客户端生成的唯一值，服务器用于识别重复请求。生成一个抗冲突的值（如 UUID），并在重试相同请求时复用相同的值。如果省略，服务器将为该请求生成一个 key；需要幂等重试的调用方应提供并复用自己的 key。最大长度：255 个字符。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| decision | string | Y | REJECT_RECEIVED_PACKAGE | Seller 对该请求的决策，可用值： |

* `REJECT_REFUND`：seller 拒绝仅退款请求
* `REJECT_RETURN`：seller 拒绝初始退货退款请求
* `REJECT_RECEIVED_PACKAGE`：seller 在 buyer 已发货或交出商品后拒绝退货退款请求
* `REJECT_REPLACEMENT`：seller 拒绝换货请求
* `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`：seller 就包裹商品质检提供部分退款 |
   reject_reason |string |Y |seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |Seller 拒绝售后请求的原因。对于 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`，请先对同一售后请求调用 Get Review Decision（`GET /return_refund/202606/review_decision`）：将此请求的 `return_id` 作为 `return_or_cancel_id` 传递，并将 `check_decisions` 设置为 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`。在响应中，选择受影响退货行项目的 `data.line_items[]` 条目，然后选择其 `decisions[]` 中 `decision` 为 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` 的条目，并提交该决策的 `available_reject_reasons[].name` 值之一。对于其他决策，使用 [Get Decision Eligibility](https://partner.tiktokshop.com/docv2/page/69844a11eeba77049695c7f6) endpoint 检索当前可用于同一请求的拒绝选项并提交返回的拒绝原因 name。**注意**：可用的决策和拒绝原因取决于当前请求状态，因此在调用此 API 之前请重新获取资格。 |
   comment |string |N |I have reached an agreement with the buyer |Seller 关于拒绝决策的备注。对于 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`，备注不得超过 500 个字符。 |
   images |[]object |N | |Seller 提供的用于支持决策的图片。对于 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`，最多允许 6 张图片。 |
   ^image_id |string |Y |tos-maliva-i-o3syd03w52-us/57a1c8908fe74572861ea5e50887d8d1 |从 [Upload Product Image](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) API 获取的图片 URI。 |
   ^mime_type |string |N |image/png |MIME 类型。 |
   ^height |int |N |200 |图片高度
   单位：px |
   ^width |int |N |200 |图片宽度
   单位：px |
   partial_refund_amount |object |N | |部分退款金额和币种。当 `decision` 为 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` 时必填。 |
   ^partial_refund_total |string |N |4.66 |部分退款金额。当 `decision` 为 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` 时，此字段必填且必须是表示大于 0 的金额的数值字符串。 |
   ^currency |string |N |USD |部分退款金额的币种。当 `decision` 为 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` 时，此字段必填且必须与退货订单的币种一致。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202606/returns/4035319218955782461/reject?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&idempotency_key=40b456b1-78e7-412d-9fe6-82181496e1bd
```

**Body**
```json
{"decision":"REJECT_RECEIVED_PACKAGE","reject_reason":"seller_reject_apply_package_has_not_exceeded_estimated_delivery_time","comment":"I have reached an agreement with the buyer","images":[{"image_id":"tos-maliva-i-o3syd03w52-us/57a1c8908fe74572861ea5e50887d8d1","mime_type":"image/png","height":200,"width":200}],"partial_refund_amount":{"partial_refund_total":"4.66","currency":"USD"}}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
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
| 25001014 | 未知的退货原因。请确保您传递的是有效的退货原因。 |
| 25001016 | reverse reason not match action type |
| 25001020 | 提供的退货原因当前已下线。请选择其他退货原因。 |
| 25001028 | reverse lock failed |
| 25001057 | reverse reason not match reason type |
| 25001058 | reverse downstream data load error |
| 25007002 | db access error |
| 25007006 | Order not found. |
| 25011010 | request has been transferred to platform operator |
| 25011023 | forbid process authentic guarantee order |
| 25011025 | Quick refund forbid reject receive. |
| 25011026 | forbid process receive for FBT order |
| 25011035 | could not reject parcel now |
| 25020004 | decision not match reverse type |
| 25020005 | No permission to process this order |
| 25020008 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 25020010 | Aftersales has been approved and cannot be rejected. |
| 25020011 | return already received |
| 25020012 | status can't reject receive |

