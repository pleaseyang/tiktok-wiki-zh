# 获取可用审核决策

# 路径：/return_refund/202606/review_decision
# 方法：[GET]
# 功能描述
[GET]/return_refund/:version/Get_Review_Decision 的描述

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
| seller_id | int | Y | 7494781899660428507 | 卖家/店铺的唯一标识符 |
| return_or_cancel_id | string | Y | 4035319218955782461 | 待评估的售后请求的标识符。传递逆向主订单 ID、售后请求 ID 或 return merchandise authorization（RMA）ID；API 会检测提供了哪种类型。请勿传递订单 ID 或订单行 ID。 |
| locale | string | N | en-US | 用于显示退货原因的 BCP-47 locale 代码，以逗号分隔。默认值：en-US |
| 支持的 locale 代码列表请参考 [Locale codes](678e3a47bae28f030a8c7523)。 |  |  |  |  |
| check_decisions | []string | N | APPROVE_REFUND,REJECT_RETURN | 为指定售后请求评估的卖家决策。可能的值： |

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
* `ISSUE_EXCHANGE_REFUND`
* `OFFER_PARTIAL_REFUND`
* `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`
   **注意：** 省略时，API 将评估请求的所有支持的卖家决策并为每个决策返回一个结果。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202606/review_decision?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&seller_id=7494781899660428507&return_or_cancel_id=4035319218955782461&locale=en-US&check_decisions=APPROVE_REFUND,REJECT_RETURN
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^line_items | []object |  | 返回的决策所适用的行项目。决策详情逐个应用于每个行项目。例如，三个行项目各 1.00 的部分退款金额总计为 3.00；请使用随金额范围返回的 `currency` 而不是假设某种币种。 |
| ^^return_line_item_id | string | 4035319218955782461 | 此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于原始父商品捆绑的 id。 |
| ^^sub_return_line_item_id | string | 4035227657962164815 | 此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于当前被退货的子商品的 id。 |
| ^^decisions | []object |  | 此行项目的候选审核决策列表。 |
| ^^^decision | string | OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG | 为此行项目评估的卖家审核决策。 |
| 可能的值： |  |  |  |

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
* `ISSUE_EXCHANGE_REFUND`
* `OFFER_PARTIAL_REFUND`
* `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` |
   ^^^eligible |bool |false |此决策当前是否对行项目有资格。当为 `false` 时，`ineligible_code` 和 `ineligible_reason` 解释决策无资格的原因；当为 `true` 时这些字段将被省略。 |
   ^^^ineligible_code |int |25005020 |无资格决策的原因码。 |
   ^^^ineligible_reason |string |the return is already completed, you can't approve again. |无资格决策的原因。 |
   ^^^available_reject_reasons |[]object | |此有资格决策的拒绝原因列表（如有）。每项包含机器可读名称和显示文本。 |
   ^^^^name |string |seller_reject_apply_product_has_been_packed |拒绝原因的机器可读名称，用作适用的审核或拒绝请求中的拒绝原因标识符。 |
   ^^^^text |string |The display text for the reject reason. |拒绝原因的显示文本。 |
   ^^^partial_refund_amount_range |object | |允许的部分退款金额范围。当 `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` 决策有资格时返回；所有其他决策省略。 |
   ^^^^min_amount |string |2.34 |卖家可以提供的最低部分退款金额。 |
   ^^^^max_amount |string |3.33 |卖家可以提供的最高部分退款金额。 |
   ^^^^currency |string |USD |部分退款金额范围的币种，与当前退货请求的币种一致。 |
   ^request_log_id |string |20260713225708FB… |此请求的日志 id，用于与 TikTok Shop 支持团队排查问题。 |
   ^errors |[]object | |列出部分失败请求的错误。例如，如果请求审核了多个订单或商品且只有部分失败，则各个错误详情将在此处返回。
   **重要**：部分失败仍返回顶级成功代码（0），因此客户端还必须检查此字段以检测部分错误。对于完全失败（如验证错误），顶级响应代码和消息将指示失败，但此字段将保持为空。 |
   ^^code |string |98001004 |错误码 |
   ^^message |string |Invalid parameters. Please verify your input before retrying |错误描述 |

# 响应示例
```json
{"code":0,"data":{"line_items":[{"return_line_item_id":"4035319218955782461","sub_return_line_item_id":"4035227657962164815","decisions":[{"decision":"OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG","eligible":false,"ineligible_code":25005020,"ineligible_reason":"the return is already completed, you can't approve again.","available_reject_reasons":[{"name":"seller_reject_apply_product_has_been_packed","text":"The display text for the reject reason."}],"partial_refund_amount_range":{"min_amount":"2.34","max_amount":"3.33","currency":"USD"}}]}],"request_log_id":"20260713225708FB…","errors":[{"code":"98001004","message":"Invalid parameters. Please verify your input before retrying"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001003 | 无效的订单状态。 |
| 25005020 | reverse amount not support partial refund |
| 25005021 | partial refund only support single sku |
| 25011010 | request has been transferred to platform operator |
| 25011011 | reverse status cannot reject application |
| 25011012 | reverse status cannot approve application |

