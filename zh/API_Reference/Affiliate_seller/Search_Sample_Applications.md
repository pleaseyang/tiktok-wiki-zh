# 搜索 Sample 申请

# 路径：/affiliate_seller/202508/sample_applications/search
# 方法：[POST]
# 功能描述
此 API 用于搜索达人提交的 sample 申请。您可以按申请状态、商品等条件筛选。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | b2Zmc2V0PTAK | 分页偏移量决定搜索的起始位置。首次请求时为空。 |
| page_size | int | N | 50 | "page_size" 的值必须大于 0 且小于或等于 50。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | N | 123456 | 商品的唯一标识符。用于指定要查询哪个商品的 sample 申请详情。 |
| title | string | N | product name | 商品名称，支持模糊搜索查询。允许卖家在管理 sample 申请时按名称搜索商品。 |
| creator_user_oepn_id | string | N | 123456 | 达人的 Open ID。请勿使用用户 ID、达人 ID 或卖家 ID。请严格按照 `creator_user_oepn_id` 的拼写发送此属性；不要将键名更改为 `creator_user_open_id`。 |
| username | string | N | test_tt_name | 达人的 TikTok 用户名，支持模糊搜索 |
| target_collabration_id | string | N | 123456 | 创建 target collaboration 后生成的唯一 ID。请严格按照 `target_collabration_id` 的拼写发送此属性；不要将键名更改为 `target_collaboration_id`。 |
| order_id | string | N | 123456 | 当 sample 申请被卖家批准时，与 sample 订单关联的主订单 ID。 |
| status | string | N | PENDING | Sample 申请的状态。 |
| 可能的枚举值为： |  |  |  |  |

* PENDING: Sample 申请正在等待卖家审核。
* AWAITING_SHIPMENT: 申请已批准，卖家需要发货 sample。
* SHIPPED: Sample 已由卖家发货，等待达人收件。
* CONTENT_PENDING: 达人已收到 sample 包裹，需要创建内容。
* REJECT_CANCELLED: Sample 申请已被卖家拒绝。
* OVERDUE_CANCELLED: Sample 申请因逾期已过期。
* UNFULFILL_CANCELLED: 达人未在约定期限内履行创建内容的承诺。
* DEL_OPEN_COLLAB: Open collaboration 已被删除。
* SELLER_NOT_SHIP_CANCELLED: 卖家未在规定期限内发货 sample。
* WITHDRAW_CANCELLED: 达人在卖家批准之前撤回了 sample 申请。
* UNFULFILLABLE_CANCELLED: 由于达人无法控制的原因，申请被取消，无法创建内容。
* OPS_CANCELLED: 申请已被运营人员手动取消。
* OPS_FAILED: 申请已被运营人员标记为失败。
* OPS_COMPLETED: 申请已被运营人员手动标记为已完成。
* COMPLETED: 申请已完成，达人已发布内容。
   此字段允许在整个生命周期中追踪 sample 申请的状态，为卖家和达人提供流程各阶段的可见性。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/sample_applications/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=b2Zmc2V0PTAK&page_size=50
```

**Body**
```json
{"product_id":"123456","title":"product name","creator_user_oepn_id":"123456","username":"test_tt_name","target_collabration_id":"123456","order_id":"123456","status":"PENDING"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTUw | 在下一次请求中作为 `page_token` 传入的分页 token。 Reuse the same `page_size` for each subsequent page. An empty string indicates that there are no more pages。 |
| ^total_count | int | 100 | 总数 |
| ^sample_applications | []object |  | 来自达人的 sample 申请 |
| ^^id | string | 123456 | Sample 申请的唯一 ID |
| ^^commission_rate | string | 0.20 | 卖家为此商品设定的达人佣金比率，以两位小数的十进制小数表示。例如，`0.20` 表示 20%。范围为 [0.01, 0.8]。 |
| ^^status | string | PENDING | Sample 申请的状态。 |
| 可能的枚举值为： |  |  |  |

* PENDING: Sample 申请正在等待卖家审核。
* AWAITING_SHIPMENT: 申请已批准，卖家需要发货 sample。
* SHIPPED: Sample 已由卖家发货，等待达人收件。
* CONTENT_PENDING: 达人已收到 sample 包裹，需要创建内容。
* REJECT_CANCELLED: Sample 申请已被卖家拒绝。
* OVERDUE_CANCELLED: Sample 申请因逾期已过期。
* UNFULFILL_CANCELLED: 达人未在约定期限内履行创建内容的承诺。
* DEL_OPEN_COLLAB: Open collaboration 计划已被删除。
* SELLER_NOT_SHIP_CANCELLED: 卖家未在规定期限内发货 sample。
* WITHDRAW_CANCELLED: 达人在卖家批准之前撤回了 sample 申请。
* UNFULFILLABLE_CANCELLED: 由于达人无法控制的原因，申请被取消，无法创建内容。
* OPS_CANCELLED: 申请已被运营人员手动取消。
* OPS_FAILED: 申请已被运营人员标记为失败。
* OPS_COMPLETED: 申请已被运营人员手动标记为已完成。
* COMPLETED: 申请已完成，达人已完成内容创作。 |
   ^^order_id |string |123456 |Sample 订单在卖家批准 sample 申请后生成 |
   ^^available_quantity |int |50 |Sample 商品的剩余库存配额。 |
   ^^approve_expiration_time |int |1728674995 |卖家批准 sample 申请的截止时间，以秒为单位的 Unix 时间戳。 |
   ^^shipment_expiration_time |int |1728674995 |卖家为申请发货 sample 的截止时间，以秒为单位的 Unix 时间戳。 |
   ^^tracking_number |string |123456 |Sample 申请订单的物流追踪号 |
   ^^fulfillment_status |string |ONGOING |表示当前履约流程的状态。可能的值为：
* PENDING: 达人尚未履行内容创作义务。
* ONGOING: 履约进行中；内容已创建，正在根据标准进行评估。
* SUCCEED: 履约已成功完成；内容符合所需标准。
* FAILED: 履约失败；内容不符合所需标准。
* OVERDUE: 履约已逾期；达人未满足截止日期。
* SUSPEND: 履约已暂停。
* CANCELLED: 履约已被取消，由达人取消或由于运营原因。
* EXEMPTED: 达人已被免除履约义务。 |
   ^^is_approvable |bool |true |Sample 申请是否可以被批准。 |
   ^^disapprovable_reasons |[]string |["Product out of stock"] |Sample 申请无法批准的原因。 This list may be absent or empty even when `is_approvable` is `false`; always check `is_approvable` to determine whether approval is allowed。 |
   ^^partner_name |string |ABC |如果 sample 申请由代理机构代表达人提交，则为合作伙伴的名称。 It is only populated when an agency handles the application process instead of the 达人 directly。 |
   ^^达人 |object | |达人详情，包括达人的 TikTok 用户名、达人 Open ID、个人资料信息以及销售和履约率等电商表现指标。 |
   ^^^creator_open_id |string |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
   ^^^username |string |test.name |达人的 TikTok 用户名 |
   ^^^nickname |string |Test Name |达人的 TikTok 昵称 |
   ^^^follower_count |int |200 |达人的粉丝数量 |
   ^^^avatar_url |string |https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068xxxxx |达人头像图片的 URL |
   ^^^gmv |object | |达人的可购物内容在过去 30 天内产生的 GMV。 It is formatted as a floating-point number with a currency symbol (e.g., "$1234.56"). If the 达人 has not authorized the disclosure of this information, the field returns an empty string。 |
   ^^^^amount |string |500 |GMV 金额 |
   ^^^^currency |string |USD |The currency code for the GMV 金额。 |
   ^^^content_count |int |4 |达人在最近 30 天内发布的内容数量。 It is formatted as an integer. If the 达人 has not authorized the sharing of this information, the field returns an empty string。 |
   ^^^fulfillment_percentage |string |60.50 |达人在过去 90 天内的 sample 履约率，以不带百分号的百分比字符串返回（例如，`60.85`）。 If the 达人 has not authorized disclosure of this information, the field returns an empty string。 |
   ^^^ec_video_view |int |1200 |达人的可购物视频在过去 30 天内的中位播放量。 If the 达人 has not authorized the sharing of this information, the field returns an empty string。 |
   ^^product |object | |商品信息 |
   ^^^id |string |123456 |商品标识符。 |
   ^^^title |string |A women dress |商品的商品名称。 |
   ^^^sku_id |string |123456 |达人申请为 sample 的商品 SKU 的唯一 ID。 |
   ^^^sku_image_url |string |https://p16-oec-va.ibyteimg.com/tos-malivaxxxxx |SKU 图片的 URL。 |
   ^^^sku_name |string |Soft Cover |SKU 属性值名称，以逗号连接。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTUw","total_count":100,"sample_applications":[{"id":"123456","commission_rate":"0.20","status":"PENDING","order_id":"123456","available_quantity":50,"approve_expiration_time":1728674995,"shipment_expiration_time":1728674995,"tracking_number":"123456","fulfillment_status":"ONGOING","is_approvable":true,"disapprovable_reasons":["Product out of stock"],"partner_name":"ABC","creator":{"creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","username":"test.name","nickname":"Test Name","follower_count":200,"avatar_url":"https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068xxxxx","gmv":{"amount":"500","currency":"USD"},"content_count":4,"fulfillment_percentage":"60.50","ec_video_view":1200},"product":{"id":"123456","title":"A women dress","sku_id":"123456","sku_image_url":"https://p16-oec-va.ibyteimg.com/tos-malivaxxxxx","sku_name":"Soft Cover"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

