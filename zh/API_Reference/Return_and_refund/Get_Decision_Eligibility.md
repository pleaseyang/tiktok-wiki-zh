# 获取决策资格

# Path: /return_refund/202601/decision_eligibility
# Method: [GET]
# 功能描述
使用此 API 评估当前对指定售后请求允许哪些 seller 决策。API 为每个请求的决策返回一个结果，包括该决策当前是否有资格以及适用于有资格的拒绝决策的任何拒绝原因。

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
| return_or_cancel_id | string | Y | 4035319218955782461 | 待评估的 TikTok Shop 退货或取消请求 ID。传递目标取消、退款、退货或其他支持的售后流程的请求标识符。请勿在此字段中传递订单 ID 或订单行 ID。 |
| check_decisions | []string | N | APPROVE_REFUND,REJECT_RETURN | 为指定售后请求评估的 seller 决策。可能的值： |

* `APPROVE_REQUEST_CANCEL`
* `APPROVE_REFUND`
* `APPROVE_RETURN`
* `APPROVE_RECEIVED_PACKAGE`
* `APPROVE_REPLACEMENT`
* `ISSUE_REPLACEMENT_REFUND`
* `DIRECT_REFUND`
* `REJECT_REQUEST_CANCEL`
* `REJECT_REFUND`
* `REJECT_RETURN`
* `REJECT_RECEIVED_PACKAGE`
* `REJECT_REPLACEMENT`
   -`ISSUE_EXCHANGE_REFUND`
   **注意：** 省略时，API 将评估请求的所有支持的 seller 决策并为每个决策返回一个结果。 |
   locale |string |N |en-US |用于显示退货原因的 BCP-47 locale 代码，以逗号分隔。默认值：en-US
   支持的 locale 代码列表请参考 [Locale codes](678e3a47bae28f030a8c7523)。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202601/decision_eligibility?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&return_or_cancel_id=4035319218955782461&check_decisions=APPROVE_REFUND,REJECT_RETURN&locale=en-US
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^decisions | []object |  | 指定售后请求的 seller 决策资格结果。 |
| ^^decision | string | APPROVE_REFUND | 一个评估的 seller 决策的资格结果。可能的值： |

* `APPROVE_REQUEST_CANCEL`
* `APPROVE_REFUND`
* `APPROVE_RETURN`
* `APPROVE_RECEIVED_PACKAGE`
* `APPROVE_REPLACEMENT`
* `ISSUE_REPLACEMENT_REFUND`
* `DIRECT_REFUND`
* `REJECT_REQUEST_CANCEL`
* `REJECT_REFUND`
* `REJECT_RETURN`
* `REJECT_RECEIVED_PACKAGE`
* `REJECT_REPLACEMENT`
   -`ISSUE_EXCHANGE_REFUND` |
   ^^eligible |bool |true |此 seller 决策当前是否对指定售后请求有资格。`true` 表示有资格；`false` 表示无资格。 |
   ^^ineligible_code |int |25001001 |无资格决策的原因码。当 eligible 为 false 时返回此字段。 |
   ^^ineligible_reason |string |the return is already completed, you can't approve again. |无资格决策的原因。当 eligible 为 false 时返回此字段。 |
   ^^available_reject_reasons |[]object | |适用于有资格的拒绝决策的拒绝原因列表。每个原因包含 name 和本地化显示文本。 |
   ^^^name |string |seller_reject_apply_product_has_been_packed |拒绝原因的机器可读名称。 |
   ^^^text |string |Product shipped. Tracking updates will be available soon. |拒绝原因的显示文本。 |

# 响应示例
```json
{"code":0,"data":{"decisions":[{"decision":"APPROVE_REFUND","eligible":true,"ineligible_code":25001001,"ineligible_reason":"the return is already completed, you can't approve again.","available_reject_reasons":[{"name":"seller_reject_apply_product_has_been_packed","text":"Product shipped. Tracking updates will be available soon."}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

