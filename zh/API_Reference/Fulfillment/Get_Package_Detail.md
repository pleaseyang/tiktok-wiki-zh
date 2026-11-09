# 获取 Package 详情

# 路径：/fulfillment/202309/packages/{package_id}
# 方法：[GET]
# 功能描述
返回 package 的信息，包括交接时间段、 tracking 号码和物流服务商信息。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| package_id | string | Y | 5433567853345 | TikTok Shop package ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/5433567853345?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^package_id | string | 5433567853345 | TikTok Shop package ID。 |
|  |  |  |  |
| ^orders | []object |  | TikTok Shop 订单的响应列表。 |
| ^^id | string | 54335448533296 | TikTok Shop 订单 ID。 |
| ^^skus | []object |  | [已弃用] SKU 信息。 |
| ^^^id | string | 2729382476852921560 | [已弃用] SKU ID。 |
| ^^^name | string | white,128g | [已弃用] SKU 名称。 |
| ^^^image_url | string | https://p19-oec-sg.ibyteimg.com/tos-maliva-i-o3syd03w52-us/12345670c | [已弃用] 订单快照中的 SKU 图片。 |
| ^^^quantity | int | 5 | [已弃用] SKU 数量。 |
| ^package_status | string | PROCESSING | 可能的值： |

* `TO_FULFILL`：等待卖家或仓库发货。
* `PROCESSING`：卖家已安排 package。等待承运商揽收包裹。
* `FULFILLING`：承运商已揽收 package 并在运输中。
* `COMPLETED`：package 已送达。
* `CANCELLED`：package 已取消。通常，package 因丢失或损坏而被取消。 |
   ^package_sub_status |string |CREATED |Package 子状态。
   可能的值：
* `CREATED`：package 已创建。
* `ISSUE`：package 分配失败，请联系平台支持。
* `STOCKING`：平台验证完成，等待卖家发货。
* `RTSING`：正在购买 shipping label，承运商结果待处理。
* `HBW`：仅限 FBT 订单；package 已在仓库中创建。
* `HBWING`：仅限 FBT 订单；package 正在仓库中创建。
* `TSP_PENDING`：第三方服务商 fulfillment 授权待处理。
* `RTS`：shipping label 已购买，卖家可以打印。
* `TTS`：承运商已揽收 package。
* `DELIVERED`：package 已送达买家。
* `SHIP_EXCEPTION`：package 无法送达，例如因损坏或丢失。详见 `ship_exception_reason` 获取详细原因。
* `PART_DELIVERED_AND_EXCEPTION`：部分 package 配送完成，另一部分遇到 shipping 异常。
* `CANCELLED`：package 已取消。 |
   ^ship_exception_reason |string |PACKAGE_LOST |-PACKAGE_DAMAGED
   -PACKAGE_LOST
   -RETURNED_TO_SHIPPER
   -PACKAGE_SCRAP |
   ^split_and_combine_tag |string |SPLIT |可能的值：
* `DEFAULT`：package 未经过任何合并或拆分操作。
* `COMBINE`：package 已与其他订单合并。
* `SPLIT`：订单已拆分为多个订单。 |
   ^has_multi_skus |bool |true |package 中是否有多个 SKU ID。 |
   ^note_tag |string |BUYER_UNNOTED |可能的值：
* `BUYER_UNNOTED`：买家未备注订单。
* `BUYER_NOTED`：买家已备注订单。
   |
   ^shipping_provider_name |string |TT Virtual express |Package 物流服务商名称。 |
   ^shipping_provider_id |string |6617675021119438849 |Package 物流服务商 ID。 |
   ^shipping_type |string |TIKTOK |指示谁提供 shipping 服务。可能的值：
* `TIKTOK`：TikTok 提供的 shipping 服务。卖家应从 TikTok 获取 shipping label。
* `SELLER`：卖家提供 shipping，包括代表卖家行事的第三方 fulfillment 服务商。 |
   ^delivery_option_name |string |Shipped from seller
   |配送选项名称。仅供展示使用。 |
   ^delivery_option_id |string |7091146663229654785 |订单配送选项 ID。配送选项 ID 映射到卖家配置的物流模板 ID。 |
   ^tracking_number |string |6617675021119438849 |Package tracking 号码。 |
   ^last_mile_tracking_number |string |6617675021119438849 |仅限跨境订单。跨境订单末端 tracking 号码。
   |
   ^pickup_slot |object | |为 package 安排的承运商揽收时间段。 |
   ^^start_time |int |1635338186 |承运商计划揽收 package 时间段的开始时间，Unix 时间戳，单位为秒。 |
   ^^end_time |int |1635338186 |承运商计划揽收 package 时间段的结束时间，Unix 时间戳，单位为秒。 |
   ^create_time |int |1635338186 |Package 创建时间。Unix 时间戳，单位为秒。 |
   ^handover_method |string |PICKUP |package 是通过揽收还是 drop-off 交付。可能的值：
* `PICKUP`：物流承运商将从卖家的揽收地址揽收 package。
* `DROP_OFF`：卖家需要将 package 送到指定地点。 |
   ^order_line_item_ids |[]string |["1729382476852921560"] |package 中包含的订单行项目 ID。 |
   ^recipient_address |object | |收件人地址和联系信息。返回的个人信息可能经过脱敏处理以保护收件人隐私。 |
   ^^full_address |string |1*** Coleman Ave San Jose, CA 95110
   |收件人的完整地址，包括地理和详细街道地址信息。 |
   ^^phone_number |string |(+1)213-***-1234***
   ***|买家的电话号码。请注意，如果此订单使用平台物流，电话号码将被脱敏。 |***
   ***^^name |string |Zay |收件人姓名。请注意，如果此订单使用平台物流，收件人姓名将被脱敏。 |***
   ***^^postal_code |string |95110***
   ***|卖家可用于发货的邮政编码（在美国，指 ZIP code）。 |***
   ***^^address_detail |string |Unit one building 8***
   ***|收件人地址的详细街道地址部分。 |***
   ***^^region_code |string |US |收件人地址的国家或地区代码。 |***
   ***^^address_line1 |string |TikTok 5800 bristol Pkwy***
   ***|街道地址第一行。 |***
   ***^^address_line2 |string |Suite 100***
   ***|街道地址第二行。 |***
   ***^^address_line3 |string |Suite 100***
   ***|街道地址第三行。通常仅用于巴西市场。 |***
   ***^^address_line4 |string |Suite 100***
   ***|街道地址第四行。通常仅用于巴西市场。 |***
   ***^sender_address |object | |发件人地址和联系信息。敏感字段可能经过脱敏处理。 |***
   ***^^full_address |string |1*** Coleman Ave San Jose, CA 95110 |发件人的完整地址，包括地理地址组件和地址详情。 |
   ^^phone_number |string |(+1)213-***-1234
   |发件人的电话号码。 |
   ^^name |string |Zay |发件人姓名。 |
   ^^postal_code |string |95110 |发件人的邮政编码。 |
   ^^address_detail |string |Unit one building 8 |发件人地址的详细街道地址部分。 |
   ^^region_code |string |US |发件人的地区代码。 |
   ^^address_line1 |string |TikTok 5800 bristol Pkwy |发件人街道地址第一行。 |
   ^^address_line2 |string |Suite 100 |发件人街道地址第二行。 |
   ^^address_line3 |string |Suite 100 |发件人街道地址第三行。通常仅用于巴西市场。 |
   ^^address_line4 |string |Suite 100 |发件人街道地址第四行。通常仅用于巴西市场。 |
   ^weight |object | |计划 package 的重量。 |
   ^^value |string |1.2 |计划 package 的重量值。 |
   ^^unit |string |GRAM |用于测量重量的计量单位。可能的值：
* `GRAM`
* `POUND` |
   ^dimension |object | |计划 package 的尺寸。 |
   ^^length |string |1.2 |计划 package 的长度。 |
   ^^width |string |0.2 |计划 package 的宽度。 |
   ^^height |string |0.03 |计划 package 的高度。 |
   ^^unit |string |CM |package 尺寸的计量单位。可能的值：
* `CM`
* `INCH` |
   ^update_time |int |1635338186 |package 最后更新的时间，Unix 时间戳，单位为秒。 |
   ^insurance |object | |仅限美国。提供在 label 购买期间自动注册的 shipping 保险详情。 |
   ^^is_purchased |bool |true |是否为 package 购买了保险。 |
   ^^coverage_amount |string |200 |package 的保险覆盖金额。单位：USD。 |
   ^^is_claim_eligible |bool |true |package 是否有资格申请保险理赔，基于符合条件的退款原因。 |
   ^^claim_status |string |CLAIM_PENDING |保险理赔状态。
   可用值：
* `NOT_STARTED`：此 package 尚未启动理赔。
* `CLAIM_PENDING`：理赔正在审核中。
* `APPROVED`：理赔已批准。
* `DECLINED`：理赔被拒绝。 |
   ^biz_extension_tags |[]string |["NON_MCF"] |当前 package 的特殊标签（如有）。
* `NON_MCF`：此 package 是否作为 MCF 订单发货但实际不是。 |
   ^warehouse_id |string |7317467398322308906 |此 package 的卖家仓库 ID |

# 响应示例
```json
{"code":0,"data":{"package_id":"5433567853345","orders":[{"id":"54335448533296","skus":[{"id":"2729382476852921560","name":"white,128g","image_url":"https://p19-oec-sg.ibyteimg.com/tos-maliva-i-o3syd03w52-us/12345670c","quantity":5}]}],"package_status":"PROCESSING","package_sub_status":"CREATED","ship_exception_reason":"PACKAGE_LOST","split_and_combine_tag":"SPLIT","has_multi_skus":true,"note_tag":"BUYER_UNNOTED","shipping_provider_name":"TT Virtual express","shipping_provider_id":"6617675021119438849","shipping_type":"TIKTOK","delivery_option_name":"Shipped from seller\n","delivery_option_id":"7091146663229654785","tracking_number":"6617675021119438849","last_mile_tracking_number":"6617675021119438849","pickup_slot":{"start_time":1635338186,"end_time":1635338186},"create_time":1635338186,"handover_method":"PICKUP","order_line_item_ids":["1729382476852921560"],"recipient_address":{"full_address":"1*** Coleman Ave San Jose, CA 95110\n","phone_number":"(+1)213-***-1234\n","name":"Zay","postal_code":"95110\n","address_detail":"Unit one building 8\n","region_code":"US","address_line1":"TikTok 5800 bristol Pkwy\n","address_line2":"Suite 100\n","address_line3":"Suite 100\n","address_line4":"Suite 100\n"},"sender_address":{"full_address":"1*** Coleman Ave San Jose, CA 95110","phone_number":"(+1)213-***-1234\n","name":"Zay","postal_code":"95110","address_detail":"Unit one building 8","region_code":"US","address_line1":"TikTok 5800 bristol Pkwy","address_line2":"Suite 100","address_line3":"Suite 100","address_line4":"Suite 100"},"weight":{"value":"1.2","unit":"GRAM"},"dimension":{"length":"1.2","width":"0.2","height":"0.03","unit":"CM"},"update_time":1635338186,"insurance":{"is_purchased":true,"coverage_amount":"200","is_claim_eligible":true,"claim_status":"CLAIM_PENDING"},"biz_extension_tags":["NON_MCF"],"warehouse_id":"7317467398322308906"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10006402 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

