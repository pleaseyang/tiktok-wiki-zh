# 获取订单列表

# Path: /order/202309/orders/search
# Method: [POST]
# 功能描述
返回在指定参数所示时间范围内创建或更新的订单列表。您还可以应用一系列筛选条件来缩小返回的订单列表范围，例如订单状态、配送选项类型和买家用户 ID。


---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 在请求 API 时使用该属性传递店铺信息。若为跨境店铺请求 API 时未传递正确的值，将返回不正确的响应。 |
| 通过 API 获取：[获取授权店铺](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许的类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都会有一个唯一的密钥。请使用分配给您应用的专属密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由生成算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。该时间戳在所有 API 请求中通用。开发者可使用它转换为本地时间。 |
| page_size | int | Y | 20 | 每页返回的结果数量。默认值：20。有效范围：[1-100]。 |
| sort_order | string | N | ASC | 用于 `sort_field` 参数的排序顺序。默认值：DESC |
| 可能的取值： |  |  |  |  |

* ASC：升序
* DESC：降序 |
   page_token |string |N |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT |用于获取分页结果集下一页的不透明令牌。该值需从上一次响应的 `next_page_token` 结果中获取。第一页无需提供。 |
   sort_field |string |N |create_time |返回的结果将按指定字段排序。
   默认值：`create_time`
   可能的取值：
* `create_time`
* `update_time`

使用 `sort_order` 参数指定返回结果的排序顺序。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_status | string | N | UNPAID | 具体的订单状态。 |
| 可用取值： |  |  |  |  |

* `UNPAID`：订单已下单，但尚未完成支付。
* `ON_HOLD`：订单已受理，等待履约。买家仍可取消而无需卖家批准。若 `order_type=PRE_ORDER`，商品仍在等待发售，因此只会在发售前 1 天授权支付，但卖家应开始为发售做准备。
* `AWAITING_SHIPMENT`：订单已可发货，但尚未发出任何商品。
* `PARTIALLY_SHIPPING`：订单中的部分商品已发出，但尚未全部发出。
* `AWAITING_COLLECTION`：运输已安排妥当，但包裹正在等待承运商揽收。
* `IN_TRANSIT`：包裹已被承运商揽收，正在配送途中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不再允许任何退货或退款。
* `CANCELLED`：订单已取消。 |
   create_time_ge |int |N |1623812664 |筛选订单，仅显示在指定日期和时间当天或之后创建的订单。Unix 时间戳。

注意：
`create_time_ge` 和 `create_time_lt` 共同构成创建时间筛选条件。

* 若填写了 `create_time_ge` 而 `create_time_lt` 为空，则 `create_time_lt` 默认为当前时间。
* 若填写了 `create_time_lt` 而 `create_time_ge` 为空，则 `create_time_ge` 默认为店铺最早时间。 |
   create_time_lt |int |N |1623812664 |筛选订单，仅显示在指定日期和时间之前创建的订单。Unix 时间戳。
   更多用法信息请参阅 `create_time_ge` 中的注意事项。
   |
   update_time_ge |int |N |1623812664 |筛选订单，仅显示在指定日期和时间当天或之后更新的订单。Unix 时间戳。

注意：
`update_time_ge` 和 `update_time_lt` 共同定义更新时间筛选条件。

* 若填写了 `update_time_ge` 而 `update_time_lt` 为空，则 `update_time_lt` 默认为当前时间。
* 若填写了 `update_time_lt` 而 `update_time_ge` 为空，则 `update_time_ge` 默认为店铺最早时间。

由于搜索过程中数据持续刷新，更新时间可能会超出所选的搜索范围。 |
update_time_lt |int |N |1623812664 |筛选订单，仅显示在指定日期和时间之前更新的订单。Unix 时间戳。
更多用法信息请参阅 `update_time_ge` 中的注意事项。
由于搜索过程中数据持续刷新，更新时间可能会超出所选的搜索范围。 |
shipping_type |string |N |TIKTOK |发货方式。

* `TIKTOK`：由 TikTok 提供的物流服务。卖家应从 TikTok 获取面单。
* `SELLER`：由卖家提供发货服务，包括代表卖家发货的第三方履约服务商。
* `TIKTOK_DIGITAL`：Tiktok 将虚拟商品直接交付给买家。无需进行任何操作。
* `IN-STORE PICKUP` ：买家直接在卖家门店地点自提商品。仅东南亚市场可用。 |
   buyer_user_id |string |N |7213489962827123654 |买家用户 ID。 |
   is_buyer_request_cancel |bool |N |false |买家是否已发起订单取消请求。 |
   warehouse_ids |[]string |N |["7000714532876273888","7000714532876273666"] |按揽收/销售仓库 ID 筛选订单。
   仅在启用多仓功能时适用。
   最大数量：100 |

# 请求示例
**查询参数**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202309/orders/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=20&sort_order=ASC&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT&sort_field=create_time
```

**请求体**
```json
{"order_status":"UNPAID","create_time_ge":1623812664,"create_time_lt":1623812664,"update_time_ge":1623812664,"update_time_lt":1623812664,"shipping_type":"TIKTOK","buyer_user_id":"7213489962827123654","is_buyer_request_cancel":false,"warehouse_ids":["7000714532876273888","7000714532876273666"]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT | 用于获取分页结果集下一页的不透明令牌。若当前响应未返回全部结果，请在请求的 `page_token` 参数中提供该值。 |
| ^total_count | int | 22113 | 搜索结果中的订单总数。 |
| ^orders | []object |  | 订单信息。 |
| ^^id | string | 576461413038785752 | TikTok Shop 订单 ID。 |
| ^^buyer_message | string | Please ship asap! | 买家的备注。 |
| ^^cancellation_initiator | string | SELLER | 取消请求发起方。 |
| 可用取值： |  |  |  |

* `SELLER`
* `BUYER`
* `SYSTEM`
   |
   ^^shipping_provider_id |string |6617675021119438849 |当前物流服务商的 ID。 |
   ^^create_time |int |1619611561 |订单创建的日期和时间。Unix 时间戳。 |
   ^^shipping_provider |string |TT Virtual express |当前物流服务商的名称。 |
   ^^packages |[]object | |该订单所包含的包裹列表。 |
   ^^^id |string |1152321127278713123 |包裹 ID。 |
   ^^payment |object | |该订单的支付信息。 |
   ^^^currency |string |IDR |支付货币。 |
   ^^^sub_total |string |5000 |买家支付的订单内所有 SKU 小计金额。

`sub_total = original_total_product_price - seller_discount - platform_discount`
对于美国市场，此为税前总金额。 |
^^^shipping_fee |string |5000 |买家支付的运费。
`shipping_fee = original_shipping_fee - shipping_fee_seller_discount - shipping_fee_platform_discount`
对于美国市场，此为税前总金额。 |
^^^seller_discount |string |5000 |卖家提供的商品折扣。 |
^^^platform_discount |string |5000 |平台提供的商品折扣。 |
^^^payment_platform_discount |string |10 |由支付平台出资、应用于该订单的折扣 |
^^^payment_discount_service_fee |string |10 |买家为享受支付平台折扣而支付的服务费 |
^^^total_amount |string |5000 |买家支付的总付款金额。
`total_amount = sub_total + shipping_fee + taxes + retail_delivery_fee` |
^^^original_total_product_price |string |5000 |商品原始价格总额（跨境店铺含增值税）。
对于美国市场，此为税前总金额。 |
^^^original_shipping_fee |string |5000 |折扣前的运费。 |
^^^shipping_fee_seller_discount |string |5000 |由卖家提供、且不符合联合资助报销条件的订单运费折扣。**注意**：若订单符合联合资助报销的最低订单金额要求，该值为 0。此时请参阅 `shipping_fee_cofunded_discount` 以了解买家所享受的运费折扣。 |
^^^shipping_fee_platform_discount |string |5000 |由平台提供的运费折扣。 |
^^^shipping_fee_cofunded_discount |string |5000 |由卖家提供、依据联合资助免运费计划条款在订单送达时符合联合资助报销条件的运费折扣。**注意**：对于不符合联合资助报销最低订单金额要求的订单，该值为 0。此时请参阅 `shipping_fee_seller_discount` 以了解买家所享受的运费折扣。 |
^^^tax |string |5000 |买家就该订单支付的税费总额。适用于跨境店铺和美国市场。 |
^^^small_order_fee |string |3000 |泰国（**仅泰国市场**）的小额订单费。
小额订单费是指平台会设定最低订单消费金额。当订单金额低于最低订单消费金额时，用户需要支付小额订单费以达到平台最低消费金额。
例如：最低订单消费金额为 100，订单金额为 80，则小额订单费为 20。 |
^^^shipping_fee_tax |string |11 |运费的税费。 |
^^^product_tax |string |21.3 |商品总价的税费。 |
^^^retail_delivery_fee |string |1.28 |零售配送费（RDF）。
**注意**：仅美国市场可用。 |
^^^buyer_service_fee |string |1000 |每笔成交的交易都会收取服务费。该费用从第 5 笔订单开始收取，并在结账时直接向客户收取。仅印度尼西亚市场可用。 |
^^^handling_fee |string |1000 |向买家收取的费用，用于覆盖与所选支付方式相关的额外处理、搬运和/或分期成本。 |
^^^shipping_insurance_fee |string |1000 |买家为货物在运输途中丢失或损坏的保险所承担的费用。
**注意**：仅印度尼西亚市场可用。 |
^^^item_insurance_fee |string |1000 |买家为商品购买后出现缺陷或损坏的保险所承担的费用。
**注意**：仅美国和印度尼西亚市场可用。 |
^^^item_insurance_tax |string |10 |买家购买保险所需缴纳的税费。
注意：仅适用于美国市场。 |
^^^distance_shipping_fee |string |1000 |距离运费是由我们的物流合作伙伴收取的费用，用于覆盖爪哇岛以外地区配送所产生的独立基于距离的成本，属于 Horizon+ 计划的一部分。
仅适用于印度尼西亚（ID）市场。 |
^^^distance_fee |string |2000 |Horizon+ 计划的距离费用总额。仅适用于印度尼西亚（ID）市场 |
^^recipient_address |object | |在 `UNPAID` 和 `ON_HOLD` 状态下，`recipient_address` 不可用。 |
^^^full_address |string |1199 Coleman Ave San Jose, CA 95110 |完整的收货地址信息。 |
^^^phone_number |string |(+1)213-***-1234 |收货人电话号码。
**注意**：若该订单使用平台物流，电话号码将被脱敏处理。 |
^^^name |string |David Kong |收货人姓名。
**注意**：若该订单使用平台物流，收货人姓名将被脱敏处理。 |
^^^first_name |string |David |收货人名字。
若未分别提供收货人的名字和姓氏，则该参数的取值将与 `name` 参数相同。 |
^^^last_name |string |Kong |收货人姓氏。
若未分别提供收货人的名字和姓氏，则该参数为空。 |
^^^first_name_local_script |string |ジョン |收货人名字的片假名写法。
**注意**：仅适用于日本（JP）市场。 |
^^^last_name_local_script |string |ドゥ |收货人姓氏的片假名写法。
**注意**：仅适用于日本（JP）市场。 |
^^^address_detail |string |Unit one building 8 |完整的收货详细地址。 |
^^^address_line1 |string |TikTok 5800 bristol Pkwy |街道地址的第一行。 |
^^^address_line2 |string |Suite 100 |街道地址的第二行。 |
^^^address_line3 |string | |街道地址的第三行。 |
^^^address_line4 |string | |街道地址的第四行。 |
^^^district_info |[]object | |在 `UNPAID` 和 `ON_HOLD` 状态下，`district_info` 不可用。 |
^^^^address_level_name |string |Country |卖家在发货时可使用的行政区划名称，例如州/县/市/区/镇等。 |
^^^^address_name |string |United Kingdom |行政区域名称，例如：London。 |
^^^^address_level |string |L0 |行政区划级别代码。取值可为 L0/L1/L2/L3/L4。例如 US 为 L0。 |
^^^^iso_code |string |VAN |行政区划级别的 ISO 代码 |
^^^delivery_preferences |object | |包含收件人为该收货地址提供的所有配送说明。目前仅美国市场可用。 |
^^^^drop_off_location |string |Front Door |收件人选择的投递地点。 |
^^^postal_code |string |95110 |卖家在发货时可使用的邮政编码。对于美国市场，此处指 ZIP Code（邮编）。 |
^^^region_code |string |US |地区代码。 |
^^^post_town |string |Ribbleton |地址的邮政镇（post town）
注意：仅英国市场可用 |
^^status |string |UNPAID |具体的订单状态。
可用取值：

* `UNPAID`：订单已下单，但尚未完成支付。
* `ON_HOLD`：订单已受理，等待履约。买家仍可取消而无需卖家批准。若 `order_type=PRE_ORDER`，商品仍在等待发售，因此只会在发售前 1 天授权支付，但卖家应开始为发售做准备。
* `AWAITING_SHIPMENT`：订单已可发货，但尚未发出任何商品。
* `PARTIALLY_SHIPPING`：订单中的部分商品已发出，但尚未全部发出。
* `AWAITING_COLLECTION`：运输已安排妥当，但包裹正在等待承运商揽收。
* `IN_TRANSIT`：包裹已被承运商揽收，正在配送途中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不再允许任何退货或退款。
* `CANCELLED`：订单已取消。 |
   ^^fulfillment_type |string |FULFILLMENT_BY_SELLER |履约方式。仅具有履约方式的订单可由卖家发货。
   可用取值：
* `FULFILLMENT_BY_SELLER`：一种由卖家直接从自有库存履约订单、而不使用 TikTok 履约中心的方式。在该模式下，卖家负责存储、包装商品并将其运送给客户。
* `FULFILLMENT_BY_TIKTOK`：由 TikTok 提供的一项服务，卖家可将商品发送至 TikTok 的履约中心，随后由 TikTok 负责将商品存储、拣货、打包并配送给客户。
* `FULFILLMENT_BY_DILAYANI_TOKOPEDIA`：由 Tokopedia GoTo Logistics 为卖家提供仓储和物流服务并对该服务收取费用的方式。 |
   ^^delivery_type |string |HOME_DELIVERY |指示是否为自提点（PUDO）。该自提点由买家在下单时选择。
   可用取值：
* `HOME_DELIVERY`：不是自提点
* `COLLECTION_POINT`：是自提点 |
   ^^paid_time |int |1619611563 |订单完成支付的日期和时间。Unix 时间戳。 |
   ^^rts_sla_time |int |1619611688 |平台指定的最晚发货时间。Unix 时间戳。 |
   ^^tts_sla_time |int |1619611761 |平台指定的最晚揽收时间。Unix 时间戳。 |
   ^^cancel_reason |string |Pricing error |取消原因。请访问[我们的取消原因列表](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d)以了解更多信息。 |
   ^^update_time |int |1619621355 |订单状态发生变更的时间。Unix 时间戳。 |
   ^^payment_method_name |string |CCDC |支付方式名称，仅用于展示。 |
   ^^rts_time |int |1619611563 |卖家发货订单（成功调用[发货包裹 API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1)）的时间。Unix 时间戳。 |
   ^^tracking_number |string |JX12345 |物流单号。在包裹发出后可用。 |
   ^^split_or_combine_tag |string |COMBINED |指示订单是被合并还是被拆分：
* `COMBINED`
* `SPLIT`

该字段将用于未来的履约 API。 |
^^has_updated_recipient_address |bool |false |收货地址是否已被更新或更改。 |
^^cancel_order_sla_time |int |1619621355 |平台指定的订单自动取消时间。
Unix 时间戳。 |
^^warehouse_id |string |6955005333819123123 |卖家仓库 ID。 |
^^request_cancel_time |int |1678389618 |买家请求取消的时间。Unix 时间戳。 |
^^shipping_type |string |TIKTOK |发货方式。
可用取值：

* `TIKTOK`：由 TikTok 提供的物流服务。卖家应从 TikTok 获取面单。
* `SELLER`：由卖家提供发货服务，包括代表卖家发货的第三方履约服务商。
* `TIKTOK_DIGITAL`：Tiktok 将虚拟商品直接交付给买家。无需进行任何操作。 |
   ^^user_id |string |7021436810468230477 |买家用户 ID。 |
   ^^seller_note |string |seller note |来自 TikTok Shop 卖家中心的卖家备注。 |
   ^^delivery_sla_time |int |1678389618 |订单应在此日期前送达，才被视为准时送达，以避免延迟配送处罚。 |
   ^^is_cod |bool |false |该选项适用于支持货到付款（COD）的卖家。买家将在收到包裹时以现金支付。

默认值：FALSE
仅适用于支持货到付款（COD）的国家。 |
^^delivery_option_id |string |7091146663229654785 |配送选项 ID，与卖家配置的物流模板 ID 相对应。 |
^^cancel_time |int |1678389618 |订单状态被更新为 `CANCELLED` 的时间。Unix 时间戳。 |
^^need_upload_invoice |string |NEED_INVOICE |是否需要上传发票以及上传状态（仅巴西市场）。

* UNKNOWN：当前无法确认是否需要发票
* NEED_INVOICE：该订单需要发票，且发票尚未上传
* NO_NEED：该订单不需要发票
* INVOICE_UPLOADED：该订单的发票已上传并通过核验。若订单被拆分，则任一子订单的发票上传后该订单即被标记为"已上传"。
* INVOICE_PROCESSING：该订单的发票当前正在上传/取消中。请等待最终结果，勿重复操作 |
   ^^delivery_option_name |string |Standard Shipping |配送选项名称，仅用于展示。
   可用取值：
* `Economy Shipping`
* `Standard Shipping`
* `Express Shipping` |
   ^^cpf |string |3213-31231412 |CPF（发票编号），用于开具发票。

**注意**：仅巴西市场可用。 |
^^line_items |[]object | |行项目信息列表。 |
^^^id |string |577086512123755123 |行项目 ID。 |
^^^sku_id |string |2729382476852921560 |SKU ID。 |
^^^combined_listing_skus |[]object | |对于虚拟捆绑 SKU，返回组成该虚拟捆绑的相关商品 SKU 数组。 |
^^^^sku_id |string |2729382476852921123 |与虚拟捆绑 SKU 相关联的原始 SKU ID。 |
^^^^sku_count |int |1 |组成该虚拟捆绑的原始 SKU 数量。 |
^^^^product_id |string |1729582718312380456 |与虚拟捆绑 SKU 相关联的原始商品 ID。 |
^^^^seller_sku |string |yellow-24-XL |与虚拟捆绑 SKU 相关联的原始卖家 SKU（由卖家自定义）。 |
^^^display_status |string |UNPAID |可用取值：

* `UNPAID`：订单已下单，但尚未完成支付。
* `AWAITING_SHIPMENT`：订单已可发货，但尚未发出任何商品。
* `AWAITING_COLLECTION`：运输已安排妥当，但包裹正在等待承运商揽收。
* `IN_TRANSIT`：包裹已被承运商揽收，正在配送途中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不再允许任何退货或退款。
* `CANCELLED`：订单已取消。 |
   ^^^product_name |string |Women's Winter Crochet Clothes |商品名称。 |
   ^^^seller_sku |string |red_iphone_256 |该商品的卖家库存单位（SKU）。 |
   ^^^sku_image |string |https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839 |SKU 图片。 |
   ^^^sku_name |string |Iphone |SKU 名称，由商品 SKU 属性（如尺寸或颜色）组合而成，例如 "Black, 26"

|
^^^product_id |string |1729582718312380123 |商品 ID。 |
^^^sale_price |string |0.01 |商品售价。请以 `payment_info` 的货币为准。 |
^^^pfand_fee |string |1.50 |适用于某些商品的押金费用，通常针对瓶、罐等饮料容器。
**注意** 仅德国市场可用 |
^^^platform_discount |string |0 |平台折扣金额。请以 `payment_info` 的货币为准。 |
^^^seller_discount |string |0 |卖家折扣金额。请以 `payment_info` 的货币为准。 |
^^^sku_type |string |PRE_ORDER |[**已弃用**：该字段已弃用，并将在未来的 API 版本中移除。请改用 `order_type`。]
订单行类型。
按地区划分的可能的取值：
**所有地区**

* `NORMAL`：有库存、可立即购买并履约的商品。
* `ZERO_LOTTERY`：在 TikTok LIVE 抽奖活动中购买的商品。
* `SHOP_PARTNER`：从 TikTok Shop 合作店铺购买的商品。

**美国**

* `PRE_ORDER`：尚未有货或发售的商品。履约将在未来的某个指定日期开始。
* `MADE_TO_ORDER`：仅在收到订单后才进行生产的商品。履约将在商品生产完成后开始。
   |
   ^^^cancel_reason |string |Discount not as expected |取消原因。请访问[我们的取消原因列表](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d)以了解更多信息。 |
   ^^^original_price |string |0.01 |商品原价。请以 `payment_info` 的货币为准。 |
   ^^^rts_time |int |1678389618 |卖家发货订单（成功调用[发货包裹 API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1)）的时间。Unix 时间戳。 |
   ^^^package_status |string |TO_FULFILL |该商品的包裹状态。
   可用取值：
* `TO_FULFILL`：包裹等待卖家安排发货。
* `PROCESSING`：卖家已安排发货，等待承运商揽收。
* `FULFILLING`：包裹已被承运商揽收，正在运输途中。
* `COMPLETED`：包裹已送达。
* `CANCELLED`：包裹已被取消。通常，包裹因丢失或损坏而被取消。 |
   ^^^currency |string |IDR |支付货币。 |
   ^^^shipping_provider_name |string |TT Virtual express |物流服务商名称。 |
   ^^^cancel_user |string |BUYER |取消请求发起方。
   可用取值：
* `BUYER`
* `SELLER`
* `OPERATOR`
* `SYSTEM` |
   ^^^shipping_provider_id |string |6617675021119438849 |该商品的物流服务商 ID。 |
   ^^^is_gift |bool |false |指示当前订单行项目是否为赠品。 |
   ^^^item_tax |[]object | |商品税费明细。 |
   ^^^^tax_type |string |SALES_TAX |税费类型。
   可用取值：
* `SALES_TAX`（美国市场销售税）

**注意**：目前仅有销售税可用。 |
^^^^tax_amount |string |21.2 |税费金额。 |
^^^^tax_rate |string |0.35 |税率。 |
^^^tracking_number |string |JX12345 |物流单号。在包裹发出后可用。 |
^^^package_id |string |1153132168123859123 |根据卖家选择的发货方式，一个订单可包含一个或多个包裹。每个包裹都有唯一的 `package_id` 和 `tracking_id`。 |
^^^retail_delivery_fee |string |1.28 |零售配送费（RDF）。
**注意**：仅美国市场可用。 |
^^^buyer_service_fee |string |1000 |每笔成交的交易都会收取服务费。该费用从第 5 笔订单开始收取，并在结账时直接向客户收取。
**注意**：仅印度尼西亚市场可用。 |
^^^small_order_fee |string |5000 |泰国（TH）的小额订单费。 |
^^^handling_duration_days |string |7 |[**已弃用**：该字段已弃用，并将在未来的 API 版本中移除。请改用 `handling_duration`。]
下单后，卖家处理订单并将其移交给承运商所需的营业日天数。
仅当 `sku_type` 的取值为 `MADE_TO_ORDER` 时适用。 |
^^^is_dangerous_good |bool |false |该 SKU 是否为危险品。为危险品创建面单时，您必须遵循平台规则将某些商品放入同一包裹。请参考 `sku_id` 与 `package_id` 之间的关系，以确定如何遵循平台规则。 |
^^^needs_prescription |bool |false |用于指示所涉商品是否需要处方的标志。 |
^^^gift_retail_price |string |20 |直播赠品、免费样品以及购品赠礼订单中免费商品的零售价。对于其他订单，该字段始终返回 0。
该金额可用于巴西市场免费样品和直播赠品订单的发票 |
^^^is_unboxing_item |bool |false |若为 `true`，表示该 SKU 是盲盒商品，需要开箱后才能向买家展示实际商品。开箱完成后，实际商品的 SKU 名称和图片也可以更新并同步至 TikTok。
注意：目前仅美国市场可用。 |
^^^unboxing_sku_code |string |14531134 |卖家为开箱后的实际商品设置的第三方 SKU 编码，仓库履约操作可参考该编码以识别需要发货的准确商品。
注意：目前仅美国市场可用。 |
^^^unboxing_case_list |[]object | |卖家为整箱开箱商品设置的第三方 SKU 编码，仓库履约操作可参考该编码以识别需要发货的准确商品。
注意：目前仅美国市场可用。 |
^^^^unbox_sku |string |14531134 |与开箱后实际商品相关联的开箱 SKU 编码。 |
^^^^unbox_sku_type |string |GIFT |指示开箱后的 SKU 是否为赠品
枚举值：NORMAL 或 GIFT |
^^^room_id |string |7652884452049160991 |创建该订单行项目所在直播场次的唯一 ID。若该订单行项目并非由直播场次创建，则该字段返回空字符串。 |
^^^sub_item_info |[]object | |子商品表示属于卖家所定义"虚拟捆绑"的 SKU。sub_item_info 将包含作为虚拟捆绑一部分进行履约所需的每个商品的相关信息。
注意：任一 SKU 的每个数量都有一个唯一的子商品信息"id"，这使得商品被拆分到不同仓库位置时，卖家仍可执行行级履约。 |
^^^^id |string |577086512123755123 |子商品（sub_item）的行项目 id。在执行拆分/行级履约操作时，可使用该唯一标识符。 |
^^^^sku_id |string |2729382476852921560 |SKU ID。 |
^^^^display_status |string |UNPAID |可用取值：

* `UNPAID`：订单已下单，但尚未完成支付。
* `AWAITING_SHIPMENT`：订单已可发货，但尚未发出任何商品。
* `AWAITING_COLLECTION`：运输已安排妥当，但包裹正在等待承运商揽收。
* `IN_TRANSIT`：包裹已被承运商揽收，正在配送途中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不再允许任何退货或退款。
* `CANCELLED`：订单已取消。 |
   ^^^^product_name |string |Women's Winter Crochet Clothes |商品名称。 |
   ^^^^seller_sku |string |red_iphone_256 |该商品的卖家库存单位（SKU）。 |
   ^^^^sku_image |string |https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839 |SKU 图片。 |
   ^^^^sku_name |string |Iphone |SKU 名称，由商品 SKU 属性（如尺寸或颜色）组合而成，例如 "Black, 26" |
   ^^^^product_id |string |1729582718312380123 |商品 ID。 |
   ^^^^sale_price |string |0.01 |商品售价。请以 `payment_info` 的货币为准。 |
   ^^^^platform_discount |string |0 |平台折扣金额。请以 `payment_info` 的货币为准。 |
   ^^^^seller_discount |string |0 |卖家折扣金额。请以 `payment_info` 的货币为准。 |
   ^^^^cancel_reason |string |Discount not as expected |取消原因。请访问[我们的取消原因列表](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d)以了解更多信息。 |
   ^^^^original_price |string |0.01 |商品原价。请以 `payment_info` 的货币为准。 |
   ^^^^rts_time |int |1678389618 |卖家发货订单（成功调用[发货包裹 API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1)）的时间。Unix 时间戳。 |
   ^^^^package_status |string |TO_FULFILL |该商品的包裹状态。
   可用取值：
* `TO_FULFILL`：包裹等待卖家安排发货。
* `PROCESSING`：卖家已安排发货，等待承运商揽收。
* `FULFILLING`：包裹已被承运商揽收，正在运输途中。
* `COMPLETED`：包裹已送达。
* `CANCELLED`：包裹已被取消。通常，包裹因丢失或损坏而被取消。 |
   ^^^^currency |string |USD |支付货币。 |
   ^^^^shipping_provider_name |string |TT Virtual express |物流服务商名称。 |
   ^^^^cancel_user |string |BUYER |取消请求发起方。
   可用取值：
* `BUYER`
* `SELLER`
* `OPERATOR`
* `SYSTEM` |
   ^^^^shipping_provider_id |string |6617675021119438849 |该商品的物流服务商 ID。 |
   ^^^^item_tax |[]object | |商品税费明细。 |
   ^^^^^tax_type |string |SALES_TAX |税费类型。
   可用取值：
* `SALES_TAX`（美国市场销售税）

**注意**：目前仅有销售税可用。 |
^^^^^tax_amount |string |21.2 |税费金额。 |
^^^^^tax_rate |string |0.35 |税率。 |
^^^^tracking_number |string |JX12345 |物流单号。在包裹发出后可用。 |
^^^^package_id |string |1153132168123859123 |根据卖家选择的发货方式，一个订单可包含一个或多个包裹。每个包裹都有唯一的 `package_id` 和 `tracking_id`。 |
^^^^retail_delivery_fee |string |1.28 |零售配送费（RDF）。
**注意**：仅美国市场可用。 |
^^^^is_dangerous_good |bool |false |该 SKU 是否为危险品。为危险品创建面单时，您必须遵循平台规则将某些商品放入同一包裹。请参考 `sku_id` 与 `package_id` 之间的关系，以确定如何遵循平台规则。 |
^^^^warehouse_id |string |6955005333819123123 |卖家仓库 ID。 |
^^^distance_shipping_fee |string |1000 |距离运费是由我们的物流合作伙伴收取的费用，用于覆盖爪哇岛以外地区配送所产生的独立基于距离的成本，属于 Horizon+ 计划的一部分。
仅适用于印度尼西亚（ID）市场。 |
^^^distance_fee |string |2000 |Horizon+ 计划的距离费用总额。仅适用于印度尼西亚（ID）市场 |
^^^shipping_vat_amount |string |3.5 |运费增值税金额
欧盟市场可用 |
^^^shipping_vat_rate |string |0.25 |运费增值税税率
欧盟市场可用 |
^^^is_pod_customized |bool |false |标识该 SKU 是否包含按需定制（print on demand）定制内容 |
^^^pod_info_id |string |789821378123 |按需定制详情信息的 ID。可使用该 ID 查询定制的确切详情 |
^^^product_listing_type |string |TEMPORARY_LISTING |描述该 SKU 的商品挂牌类型。
可能的取值：

* `TEMPORARY LISTING` |
   ^^buyer_email |string |v2b2V5@chat.seller.tiktok.com |买家的匿名化电子邮箱地址。不建议直接向该邮箱地址发送消息。如需联系买家，请前往 TikTok Shop 卖家中心 - 买家消息页面。 |
   ^^delivery_due_time |int |1678389618 |若订单未在此时间前将状态更新为 `DELIVERED`，该订单将被 TikTok Shop 自动取消。Unix 时间戳。 |
   ^^is_sample_order |bool |false |使用该字段判断订单是否为样品订单。 |
   ^^shipping_due_time |int |1678389618 |若订单未在此时间前将状态更新为 `AWAITING_COLLECTION`，该订单将被 TikTok Shop 自动取消。Unix 时间戳。 |
   ^^collection_due_time |int |1678389618 |若订单未在此时间前将状态更新为 `IN_TRANSIT`，该订单将被 TikTok Shop 取消。Unix 时间戳。 |
   ^^delivery_option_required_delivery_time |int |1678389618 |订单应在此时间前送达。Unix 时间戳。 |
   ^^is_on_hold_order |bool |false |指示订单已被更改或将被更新为 `ON_HOLD` 状态。 |
   ^^delivery_time |int |1678389618 |订单状态变更为 `DELIVERED` 的时间。Unix 时间戳。 |
   ^^is_replacement_order |bool |false |是否为补发订单。 |
   ^^is_subscription_order |bool |true |订阅订单是由客户设置的周期性重复订单。若为 TRUE，则该订单由订阅订单生成 |
   ^^is_refundable_sample |bool |false |该字段指示订单是否为可退款样品。可退款样品让卖家与达人展开合作，仅当达人达到销售门槛时才退还商品成本。 |
   ^^authentication_required |bool |false |若为 true，则订单需要鉴定。下单后需使用经批准的自有鉴定服务进行核验。此项必须在发货前完成。 |
   ^^collection_time |int |1678389618 |订单状态被更新为 `IN_TRANSIT` 的时间。Unix 时间戳。 |
   ^^replaced_order_id |string |576461416728782174 |被替换订单的订单 ID。

仅当 `is_replacement_order = true` 时返回。 |
^^is_buyer_request_cancel |bool |false |买家是否有待处理的取消请求。 |
^^pick_up_cut_off_time |int |1678389618 |为避免延迟配送（LDR），您必须确保包裹在此时间前被揽收。仅适用于东南亚地区。
|
^^fast_dispatch_sla_time |int |1678389618 |为获得 NDD（次日达）项目激励的最晚揽收时间。Unix 时间戳。
**注意**：仅泰国和菲律宾可用。 |
^^commerce_platform |string |TIKTOK_SHOP |下单所在平台。
可能的取值：

* `TIKTOK_SHOP`
* `TOKOPEDIA`
* `TIKTOK_SHOP_APP`
   **注意**：`Tokopedia` 和 `Tiktok Shop App` 仅在东南亚市场可用。 |
   ^^order_type |string |ZERO_LOTTERY |订单类型。
   按地区划分的可能取值：

**所有地区**

* `NORMAL`：有库存、可立即购买并履约的商品。
* `ZERO_LOTTERY`：在 TikTok LIVE 抽奖活动中下的订单。
* `AUCTION`：在拍卖中下的订单，商品价格不固定。
   **美国**
* `PRE_ORDER`：针对尚未有货或发售商品的预售订单。履约将在未来的某个指定日期开始。
* `MADE_TO_ORDER`：针对仅在收到订单后才进行生产商品的订单。履约将在商品生产完成后开始。
* `BACK_ORDER`：针对缺货但预计会补货商品的订单。履约将在商品补货后开始。
* `VIRTUAL_ORDER`：针对数字商品、无需实物配送的订单。履约在支付确认后即时或自动完成。

对于标准订单或不属于上述类别的其他类型，返回空值。 |
^^release_date |int |1619611762 |订单开始处理、且订单状态变更为 [AWAITING_SHIPMENT](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011) 的日期。
仅当 `order_type` 为 `PRE_ORDER` 时适用。 |
^^handling_duration |object | |下单后，卖家处理订单并将其移交给承运商所需的时长。
仅当 `order_type` 为 `MADE_TO_ORDER` 或 `BACK_ORDER` 时适用。 |
^^^days |string |7 |天数。 |
^^^type |string |BUSINESS_DAY |指示该时长按自然日还是营业日计算。
可能的取值：

* `CALENDAR_DAY`：表示连续的自然日，包含周末和节假日。
* `BUSINESS_DAY`：表示营业日，不包含周末和法定节假日。
   默认值：`BUSINESS_DAY` |
   ^^auto_combine_group_id |string |12345677 |在直播场次中分配给同一客户订单的标识符，用于在卖家中心开启"自动合单"时便于合并发货。 |
   ^^cpf_name |string |John Smith |巴西市场中归属于该 CPF 号码的姓名。
   |
   ^^is_exchange_order |bool |false |当为 TRUE 时，表示该订单为换货订单。

注意：仅美国和英国市场可用。 |
^^exchange_source_order_id |string |576461413038785752 |若订单为换货订单，该字段返回生成该换货订单的原始订单的订单 ID。
仅当 is_exchange_order = true 时返回。
注意：仅美国和英国市场可用。 |
^^consultation_id |string |123456 |用于标识相应电子药房问诊（ePharmacy consultation）的 ID。
仅当已发起电子药房问诊时适用。若处方由客户通过上传图片提供，则不适用。 |
^^fast_delivery_program |string |3_DAY_DELIVERY |在商品上展示的标识，用于告知买家卖家参与快速配送计划，因此订单应在承诺的时间范围内送达。
可能的取值：

* `3_DAY_DELIVERY`
* `3_DAY_POTENTIAL_SHIPPING`
* `3_DAY_POTENTIAL_TRANSIT`
   若订单不满足快速配送计划的要求，则不返回该字段。
   注意：仅适用于美国市场。 |
   ^^fulfillment_priority_level |int |100 |可用于优先发货的履约优先级取值（仅东南亚可用）
   100 = 即时达
   200 = 当日 8 小时达
   300 = 当日达
   400 = 次日达
   500 = 特快
   600 = 标准
   700 = 经济
   800 = 货运 |
   ^^recommended_shipping_time |int |1619611561 |根据各物流服务商（LSP）服务类型建议的发货时间（仅东南亚可用） |
   ^^buyer_nickname |string |user213123 |由 TikTok 用户定义的 TikTok 买家昵称。在 TikTok 直播场次内展示开箱结果时，可使用 buyer_nickname 来标识买家。 |
   ^^buyer_avatar |string |https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839 |由 TikTok 用户定义的 TikTok 买家头像。在 TikTok 直播场次内展示开箱结果时，可将 buyer_avatar 与 buyer_nickname 结合使用。 |
   ^^order_rights |[]int |[1] |订单标签标识，指示基于卖家所订阅计划该订单内是否具有某些权益。
   1 = 运费报销计划
   2 = Horizon+ 计划
   仅适用于东南亚市场 |
   ^^instore_pickup_sla_time |int |1784090976 |平台指定的到店自提方式下买家最晚自提时间。目前适用于东南亚市场。Unix 时间戳。 |
   ^^fast_rts_sla_time |int |1784090976 |指示发货动作的快速履约 SLA。仅适用于东南亚市场。Unix 时间戳 |
   ^^fast_collection_sla_time |int |1784090976 |指示揽收动作的快速履约 SLA。仅适用于东南亚市场。Unix 时间戳 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA+7D1ud64MPNz5OaT","total_count":22113,"orders":[{"id":"576461413038785752","buyer_message":"Please ship asap!","cancellation_initiator":"SELLER","shipping_provider_id":"6617675021119438849","create_time":1619611561,"shipping_provider":"TT Virtual express","packages":[{"id":"1152321127278713123"}],"payment":{"currency":"IDR","sub_total":"5000","shipping_fee":"5000","seller_discount":"5000","platform_discount":"5000","payment_platform_discount":"10","payment_discount_service_fee":"10","total_amount":"5000","original_total_product_price":"5000","original_shipping_fee":"5000","shipping_fee_seller_discount":"5000","shipping_fee_platform_discount":"5000","shipping_fee_cofunded_discount":"5000","tax":"5000","small_order_fee":"3000","shipping_fee_tax":"11","product_tax":"21.3","retail_delivery_fee":"1.28","buyer_service_fee":"1000","handling_fee":"1000","shipping_insurance_fee":"1000","item_insurance_fee":"1000","item_insurance_tax":"10","distance_shipping_fee":"1000","distance_fee":"2000"},"recipient_address":{"full_address":"1199 Coleman Ave San Jose, CA 95110","phone_number":"(+1)213-***-1234","name":"David Kong","first_name":"David","last_name":"Kong","first_name_local_script":"ジョン","last_name_local_script":"ドゥ","address_detail":"Unit one building 8","address_line1":"TikTok 5800 bristol Pkwy","address_line2":"Suite 100","address_line3":" ","address_line4":" ","district_info":[{"address_level_name":"Country","address_name":"United Kingdom","address_level":"L0","iso_code":"VAN"}],"delivery_preferences":{"drop_off_location":"Front Door"},"postal_code":"95110","region_code":"US","post_town":"Ribbleton"},"status":"UNPAID","fulfillment_type":"FULFILLMENT_BY_SELLER","delivery_type":"HOME_DELIVERY","paid_time":1619611563,"rts_sla_time":1619611688,"tts_sla_time":1619611761,"cancel_reason":"Pricing error","update_time":1619621355,"payment_method_name":"CCDC","rts_time":1619611563,"tracking_number":"JX12345","split_or_combine_tag":"COMBINED","has_updated_recipient_address":false,"cancel_order_sla_time":1619621355,"warehouse_id":"6955005333819123123","request_cancel_time":1678389618,"shipping_type":"TIKTOK","user_id":"7021436810468230477","seller_note":"seller note","delivery_sla_time":1678389618,"is_cod":false,"delivery_option_id":"7091146663229654785","cancel_time":1678389618,"need_upload_invoice":"NEED_INVOICE","delivery_option_name":"Standard Shipping","cpf":"3213-31231412","line_items":[{"id":"577086512123755123","sku_id":"2729382476852921560","combined_listing_skus":[{"sku_id":"2729382476852921123","sku_count":1,"product_id":"1729582718312380456","seller_sku":"yellow-24-XL "}],"display_status":"UNPAID","product_name":"Women's Winter Crochet Clothes","seller_sku":"red_iphone_256","sku_image":"https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839","sku_name":"Iphone","product_id":"1729582718312380123","sale_price":"0.01","pfand_fee":"1.50","platform_discount":"0","seller_discount":"0","sku_type":"PRE_ORDER","cancel_reason":"Discount not as expected","original_price":"0.01","rts_time":1678389618,"package_status":"TO_FULFILL","currency":"IDR","shipping_provider_name":"TT Virtual express","cancel_user":"BUYER","shipping_provider_id":"6617675021119438849","is_gift":false,"item_tax":[{"tax_type":"SALES_TAX","tax_amount":"21.2","tax_rate":"0.35"}],"tracking_number":"JX12345","package_id":"1153132168123859123","retail_delivery_fee":"1.28","buyer_service_fee":"1000","small_order_fee":"5000","handling_duration_days":"7","is_dangerous_good":false,"needs_prescription":false,"gift_retail_price":"20","is_unboxing_item":false,"unboxing_sku_code":"14531134","unboxing_case_list":[{"unbox_sku":"14531134","unbox_sku_type":"GIFT"}],"room_id":"7652884452049160991","sub_item_info":[{"id":"577086512123755123","sku_id":"2729382476852921560","display_status":"UNPAID","product_name":"Women's Winter Crochet Clothes","seller_sku":"red_iphone_256","sku_image":"https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839","sku_name":"Iphone","product_id":"1729582718312380123","sale_price":"0.01","platform_discount":"0","seller_discount":"0","cancel_reason":"Discount not as expected","original_price":"0.01","rts_time":1678389618,"package_status":"TO_FULFILL","currency":"USD","shipping_provider_name":"TT Virtual express","cancel_user":"BUYER","shipping_provider_id":"6617675021119438849","item_tax":[{"tax_type":"SALES_TAX","tax_amount":"21.2","tax_rate":"0.35"}],"tracking_number":"JX12345","package_id":"1153132168123859123","retail_delivery_fee":"1.28","is_dangerous_good":false,"warehouse_id":"6955005333819123123"}],"distance_shipping_fee":"1000","distance_fee":"2000","shipping_vat_amount":"3.5","shipping_vat_rate":"0.25","is_pod_customized":false,"pod_info_id":"789821378123","product_listing_type":"TEMPORARY_LISTING"}],"buyer_email":"v2b2V5@chat.seller.tiktok.com","delivery_due_time":1678389618,"is_sample_order":false,"shipping_due_time":1678389618,"collection_due_time":1678389618,"delivery_option_required_delivery_time":1678389618,"is_on_hold_order":false,"delivery_time":1678389618,"is_replacement_order":false,"is_subscription_order":true,"is_refundable_sample":false,"authentication_required":false,"collection_time":1678389618,"replaced_order_id":"576461416728782174","is_buyer_request_cancel":false,"pick_up_cut_off_time":1678389618,"fast_dispatch_sla_time":1678389618,"commerce_platform":"TIKTOK_SHOP","order_type":"ZERO_LOTTERY","release_date":1619611762,"handling_duration":{"days":"7","type":"BUSINESS_DAY"},"auto_combine_group_id":"12345677","cpf_name":"John Smith","is_exchange_order":false,"exchange_source_order_id":"576461413038785752","consultation_id":"123456","fast_delivery_program":"3_DAY_DELIVERY","fulfillment_priority_level":100,"recommended_shipping_time":1619611561,"buyer_nickname":"user213123","buyer_avatar":"https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839","order_rights":[1],"instore_pickup_sla_time":1784090976,"fast_rts_sla_time":1784090976,"fast_collection_sla_time":1784090976}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关通用错误码，请参阅 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 状态码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。若多次尝试后问题仍然存在，请联系平台支持。 |

