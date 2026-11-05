# 获取售后资格

# Path: /return_refund/202602/orders/{order_id}/aftersale_eligibility
# Method: [GET]
# 功能描述
使用此 API 检查 seller 或 buyer 是否可以为订单发起仅退款、退货退款或取消请求。响应按 SKU、订单行项目和售后请求类型分组显示资格。

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
| order_id | string | Y | 577087614418520388 | TikTok Shop 订单的唯一标识符。 |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| initiate_aftersale_user | string | N | BUYER | 您想要检查售后选项的用户类型。 |
| 默认值：SELLER |  |  |  |  |
| 可能的值： |  |  |  |  |

* SELLER
* BUYER |
   request_types |[]string |N |REFUND |**可选。** 指定要查询的请求类型。如果省略，API 将返回指定发起方当前可用的所有请求类型。可能的值：
   -`CANCEL`
   -`REFUND`
   -`RETURN_AND_REFUND` |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202602/orders/577087614418520388/aftersale_eligibility?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&initiate_aftersale_user=BUYER&request_types=REFUND
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sku_eligibility | []object |  | 给定 SKU 的可用售后选项。 |
| ^^sku_id | string | 1729385144994206632 | SKU ID。 |
| ^^line_item_eligibility | []object |  | 此 SKU 中订单行项目的资格结果，按售后请求类型分组。一个请求类型可以包含有资格和无资格的订单行项目的单独条目。有资格的条目可以包含 available_reason_names，而无资格的条目包含 ineligible_code 和 ineligible_reason。 |
| ^^^request_type | string | REFUND | 售后请求类型。 |
| 可能的值： |  |  |  |

* `CANCEL`
* `REFUND`
* `RETURN_AND_REFUND` |
   ^^^order_line_items_ids |[]string |["576469648086306000"] |指定订单行 ID。**注意：** 这是一个遗留字段，新集成请使用 `order_line_list` 代替。 |
   ^^^eligible |bool |true |指示此条目中的订单行是否有资格使用该条目的售后请求类型：
* `true`：订单行有资格使用该请求类型。
* `false`：订单行无资格使用该请求类型。 |
   ^^^ineligible_code |int |25001001 |无资格售后请求的原因码。 |
   ^^^ineligible_reason |string |invalid order status |无资格售后请求的原因。 |
   ^^^available_reason_names |[]string |available reason names |创建后续售后请求时可使用的原因名称列表。 |
   ^^^order_line_list |[]object | |指定订单行项目。**注意：** 此字段与之前的 `order_line_items_ids` 字段完全向后兼容。 |
   ^^^^order_line_item_id |string |576469648086306986 |对应的订单行 ID |
   ^^^^sub_order_line_item_id |string |576469648086306987 |捆绑商品内的子订单行 ID
* 捆绑商品必填
* 非捆绑商品无需填写 |

# 响应示例
```json
{"code":0,"data":{"sku_eligibility":[{"sku_id":"1729385144994206632","line_item_eligibility":[{"request_type":"REFUND","order_line_items_ids":["576469648086306000"],"eligible":true,"ineligible_code":25001001,"ineligible_reason":"invalid order status","available_reason_names":"available reason names","order_line_list":[{"order_line_item_id":"576469648086306986","sub_order_line_item_id":"576469648086306987"}]}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

