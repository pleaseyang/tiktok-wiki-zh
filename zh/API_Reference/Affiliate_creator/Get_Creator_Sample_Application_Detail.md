# 获取达人样品申请详情

# 路径：/affiliate_creator/202412/sample_applications/single_query
# 方法：[POST]
# 功能描述
获取指定样品申请的样品详情。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 1729480364147774364 | 商品标识符。 |
| application_id | string | N | 8070590921506065183 | 免费样品申请 ID。当 `application_type` 为 `FREE_SAMPLE` 时，提供 `application_id`；若省略，则还需提供 `main_order_id`，以及必填的 `product_id`。 |
| application_type | string | Y | FREE_SAMPLE | 达人样品申请的类型。 |

* FREE_SAMPLE : 卖家提供的免费样品，达人可自行从商品详情页申请。
* SAMPLE_COUPON: 达人领取了样品券(一种优惠券)并使用它以折扣价下单。
* SAMPLE_CAMPAIGN: 由平台组织的活动。达人可参与此活动，免费获取平台提供的样品商品。
   |
   main_order_id |string |N |579622078763731743 |真实的主订单标识符，当 application 为 "SAMPLE_COUPON"、"SAMPLE_CAMPAIGN" 或 "REFUNDABLE_SAMPLE" 时必填。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202412/sample_applications/single_query?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"product_id":"1729480364147774364","application_id":"8070590921506065183","application_type":"FREE_SAMPLE","main_order_id":"579622078763731743"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sample_application | object |  | sample application 信息。 |
| ^^id | string | 8070590921506065183 | sample application 标识符。 |
| ^^create_time | int | 1731298837 | sample application 创建时间（秒）。 |
| ^^sample_product | object |  | 样品商品信息。 |
| ^^^id | string | 1729863469568985219 | 商品标识符。 |
| ^^^sku_id | string | 1729480364147774364 | SKU 标识符。 |
| ^^^sku_sale_property_value_names | []string | ["red","large size"] | 此 SKU ID 的 SKU 属性名称列表。 |
| ^^main_order_id | string | 57871819384716917 | 样品订单在卖家批准 sample application 后生成。 |
| ^^activity_id | string | 74378918272345199 | 样品活动标识符 ID（仅用于样品活动）。 |
| ^^type | string | FREE_SAMPLE | 达人样品申请的类型。 |

* FREE_SAMPLE : 卖家提供的免费样品，达人可自行从 pdp 页面申请。
* SAMPLE_COUPON: 达人领取了样品券(一种优惠券)并使用它以折扣价购买订单。
* SAMPLE_CAMPAIGN: 由平台组织的活动。达人可参与此活动，免费获取平台提供的样品商品。 |
   ^^status |string |PENDING |sample application 的状态。
   可能的枚举值为：
* PENDING：样品申请正等待卖家审核。
* AWAITING_SHIPMENT：申请已批准，卖家需要寄送样品。
* SHIPPED：卖家已寄出样品，等待达人接收包裹。
* CONTENT_PENDING：达人已收到样品包裹，预计将创作内容。
* REJECT_CANCELLED：样品申请已被卖家拒绝。
* OVERDUE_CANCELLED：样品申请因逾期已失效。
* UNFULFILL_CANCELLED：达人未在约定时间内履行创作内容的承诺。
* SELLER_NOT_SHIP_CANCELLED：卖家未在要求时间内寄出样品。
* WITHDRAW_CANCELLED：达人在卖家批准前撤回了样品申请。
* UNFULFILLABLE_CANCELLED：因达人无法控制的原因，申请被取消，导致无法创作内容。
* OPS_CANCELLED：申请已被运营人员手动取消。
* OPS_FAILED：申请已被运营人员标记为失败。
* OPS_ COMPLETED：申请已被运营人员手动标记为完成。
* COMPLETED：申请已完成，达人已发布内容。
   该字段用于跟踪样品申请在整个生命周期中的状态，让卖家和达人可查看流程各阶段。 |
   ^^creator_fulfillment |object | |此 sample application 的履约信息。 |
   ^^^id |string |87147319238415178 |履约标识符。 |
   ^^^expiration_time |int |1726301400 |履约截止时间戳（秒）。 |
   ^^^total_suspend_duration |int |7641234 |履约总暂停时长（秒）。 |
   ^^^status |string |PENDING |履约状态，表示履约流程的当前状态。可能的取值有：
* PENDING：达人尚未履行内容创作义务。
* ONGOING：履约进行中；内容已创建并正在按标准评估。
* SUCCEED：履约已成功完成；内容符合要求的标准。
* FAILED：履约失败；内容未达到要求的标准。
* OVERDUE：履约已逾期；达人未在截止时间内完成。
* SUSPEND：履约已暂停。
* CANCELLED：履约已取消，由达人取消或因运营原因取消。
* EXEMPTED: 该达人已被免除履约义务。
* REPEATED：达人在首次完成履约后再次执行了履约；重复履约不视为失败。 |

# 响应示例
```json
{"code":0,"data":{"sample_application":{"id":"8070590921506065183","create_time":1731298837,"sample_product":{"id":"1729863469568985219","sku_id":"1729480364147774364","sku_sale_property_value_names":["red","large size"]},"main_order_id":"57871819384716917","activity_id":"74378918272345199","type":"FREE_SAMPLE","status":"PENDING","creator_fulfillment":{"id":"87147319238415178","expiration_time":1726301400,"total_suspend_duration":7641234,"status":"PENDING"}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

