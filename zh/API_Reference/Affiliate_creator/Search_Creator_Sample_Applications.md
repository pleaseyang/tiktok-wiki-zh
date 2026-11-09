# 搜索达人样品申请

# 路径：/affiliate_creator/202412/sample_applications/search
# 方法：[POST]
# 功能描述
为已认证的达人搜索样品申请。

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
| page_token | string | N | 87712341234 | 上一次响应在 `next_page_token` 中返回的页面令牌。首次请求时省略此参数。后续页面请传入返回的令牌，并复用相同的 `application_statuses` 取值。 |
| page_size | int | N | 50 | "page_size" 的值必须大于 0 且小于或等于 50。 |
| Default 20 |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| application_statuses | []string | N | ["PENDING","AWAITING_SHIPMENT"] | 按状态筛选样品申请。 |
| 可能的枚举值为： |  |  |  |  |

* PENDING：样品申请正等待卖家审核。
* AWAITING_SHIPMENT：申请已批准，卖家需要寄送样品。
* SHIPPED：卖家已寄出样品，等待达人接收包裹。
* CONTENT_PENDING：达人已收到样品包裹，预计将创作内容。
* REJECT_CANCELLED：样品申请已被卖家拒绝。
* OVERDUE_CANCELLED：样品申请因逾期已失效。
* UNFULFILL_CANCELLED：达人未在约定时间内履行创作内容的承诺。
* FULFILLMENT_SUSPEND: 由于商品无法推广，申请履约已暂停。
* DEL_OPEN_COLLAB：开放协作已删除。
* SELLER_NOT_SHIP_CANCELLED：卖家未在要求时间内寄出样品。
* WITHDRAW_CANCELLED：达人在卖家批准前撤回了样品申请。
* UNFULFILLABLE_CANCELLED：因达人无法控制的原因，申请被取消，导致无法创作内容。
* OPS_CANCELLED：申请已被运营人员手动取消。
* OPS_FAILED：申请已被运营人员标记为失败。
* OPS_ COMPLETED：申请已被运营人员手动标记为完成。
* COMPLETED：申请已完成，达人已发布内容。
* TO_BE_POST: 达人尚未为该样品发布视频或 LIVE。
* POST_IN_REVIEW: 达人已发布尚未满足履约要求的视频或直播。
* POST_FAILED: 达人已发布视频或 LIVE，但在完成样品履约前将其删除。
* CANCELED: 样品申请已取消。
   该字段用于跟踪样品申请在整个生命周期中的状态，让卖家和达人可查看流程各阶段。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202412/sample_applications/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_token=87712341234&page_size=50
```

**Body**
```json
{"application_statuses":["PENDING","AWAITING_SHIPMENT"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 20 | 用于查询下一页订单的分页令牌，最后一页为空字符串。 |
| ^sample_applications | []object |  | sample application 信息。 |
| ^^id | string | 8070590921506065183 | sample application 的唯一 ID。 |
| ^^sample_product | object |  | 样品商品信息。 |
| ^^^id | string | 1729432087292775344 | 商品标识符。 |
| ^^^sku_id | string | 1729480364147774364 | SKU 标识符。 |
| ^^^sku_sale_property_value_names | []string | ["red","large size"] | SKU 销售属性值的名称。 |
| ^^main_order_id | string | 13444222 | 样品订单在卖家批准 sample application 后生成。 |
| ^^activity_id | string | 13456677 | 样品活动标识符 ID（仅用于样品活动）。 |
| ^^status | string | PENDING | sample application 的状态。 |
| 可能的枚举值为： |  |  |  |

* PENDING：样品申请正等待卖家审核。
* AWAITING_SHIPMENT：申请已批准，卖家需要寄送样品。
* SHIPPED：卖家已寄出样品，等待达人接收包裹。
* REJECT_CANCELLED：样品申请已被卖家拒绝。
* OVERDUE_CANCELLED：样品申请因逾期已失效。
* UNFULFILL_CANCELLED：达人未在约定时间内履行创作内容的承诺。
* FULFILLMENT_SUSPEND: 由于商品状态不可推广，申请履约已暂停。
* DEL_OPEN_COLLAB：开放协作已删除。
* SELLER_NOT_SHIP_CANCELLED：卖家未在要求时间内寄出样品。
* WITHDRAW_CANCELLED：达人在卖家批准前撤回了样品申请。
* UNFULFILLABLE_CANCELLED：因达人无法控制的原因，申请被取消，导致无法创作内容。
* OPS_CANCELLED：申请已被运营人员手动取消。
* OPS_FAILED：申请已被运营人员标记为失败。
* OPS_ COMPLETED：申请已被运营人员手动标记为完成。
* COMPLETED：申请已完成，达人已发布内容。
* TO_BE_POST: 达人尚未为该样品发布视频/直播
* POST_IN_REVIEW: 达人已发布视频/直播，但未满足履约规则。
* POST_FAILED: 达人在完成样品履约前已发布视频/直播并将其删除。
* CANCELED: 此申请(订单)已取消。
   此字段可用于跟踪样品申请在其整个生命周期中的状态，让卖家和达人能够了解流程的每个阶段。 |
   ^^creator_fulfillment |object | | 此 sample application 的履约信息。 |
   ^^^id |string |123456 |履约 ID。 |
   ^^^expiration_time |int |1726301400 |履约截止时间戳（秒）。 |
   ^^^total_suspend_duration |int |123 |履约总暂停时长（秒）。 |
   ^^^status |string |PENDING |履约状态，表示履约流程的当前状态。可能的取值有：
* PENDING：达人尚未履行内容创作义务。
* ONGOING：履约进行中；内容已创建并正在按标准评估。
* SUCCEED：履约已成功完成；内容符合要求的标准。
* FAILED：履约失败；内容未达到要求的标准。
* OVERDUE：履约已逾期；达人未在截止时间内完成。
* SUSPEND：履约已暂停。
* CANCELLED：履约已取消，由达人取消或因运营原因取消。
* EXEMPTED: 该达人已被免除履约义务。 |
   ^^^bound_product_status |string |LIVE |表示与履约订单关联的商品的营销状态。它指示该商品是否可用于营销和履约。可能取值为：
* UNKNOWN: 商品的营销状态未知。
* LIVE: 商品可用且可用于履约。
* OUT_OF_STOCK: 商品缺货，无法履约。
* SELLER_DEACTIVATE：商品已被卖家停用。
* PLATFORM_DEACTIVATE：商品已被平台停用。
* NO_PLAN: 没有可供达人推广该商品的有效计划。
* PERMANENT_DELETED: 商品已被永久删除，不再可用。
   此字段帮助卖家和达人了解与履约订单关联的商品的当前状态，确保所有相关方都知晓样品申请和协作中所涉及商品的可用性与营销状态。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"20","sample_applications":[{"id":"8070590921506065183","sample_product":{"id":"1729432087292775344","sku_id":"1729480364147774364","sku_sale_property_value_names":["red","large size"]},"main_order_id":"13444222","activity_id":"13456677","status":"PENDING","creator_fulfillment":{"id":"123456","expiration_time":1726301400,"total_suspend_duration":123,"status":"PENDING","bound_product_status":"LIVE"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

