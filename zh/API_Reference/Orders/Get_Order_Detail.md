# 获取订单详情

# 路径：/order/202507/orders
# 方法：[GET]
# 功能描述
获取订单的详细信息，包括订单状态、收货地址、支付明细、价格与税费信息以及包裹信息等重要属性。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时，如果未传递正确的值，将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| ids | []string | Y | 57668123555,57668123555 | TikTok Shop 订单 ID 取值列表。 |
| Max count: 50 |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202507/orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&ids=57668123555,57668123555
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^orders | []object |  | Order information. |
| ^^id | string | 576461413038785752 | TikTok Shop 订单的唯一标识符。 |
| ^^cancellation_initiator | string | SELLER | 取消请求的发起方。 |
| 可能的值： |  |  |  |

* `SELLER`
* `BUYER`
* `SYSTEM` |
   ^^shipping_provider |string |TT Virtual express |当前物流服务商的名称。 |
   ^^shipping_provider_id |string |6617675021119438849 |当前物流服务商的 ID。 |
   ^^user_id |string |7021436810468230477 |买家的用户 ID。 |
   ^^status |string |UNPAID |订单状态。
   可能的值：
* `UNPAID`：订单已下单，但尚未完成支付。
* `ON_HOLD`：订单已接收并等待履约，因此买家仍可无需卖家批准取消订单。如果 `order_type=PRE_ORDER`，还表示商品仍在等待发售，因此仅在发售前 1 天授权扣款，但卖家应开始为发售做准备。
* `AWAITING_SHIPMENT`：订单已准备好发货，但尚未发出任何商品。
* `PARTIALLY_SHIPPING`：订单中部分商品已发货，但并非全部。
* `AWAITING_COLLECTION`：已安排发货，但包裹正等待承运商揽收。
* `IN_TRANSIT`：承运商已揽收包裹，正在配送中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不再允许退货或退款。
* `CANCELLED`：订单已取消。 |
   ^^rts_time |int |1619611563 |卖家发货订单的时间（成功调用 Ship Order 端点）。
   Unix timestamp. |
   ^^payment |object | |TikTok Shop 订单的支付信息。 |
   ^^^currency |string |IDR |支付货币。 |
   ^^^sub_total |string |5000 |买家支付的订单中所有 SKU 的小计。对于 US 市场，此为税前总金额。
   `sub_total` = `original_total_product_price` - `seller_discount` - `platform_discount` |
   ^^^shipping_fee |string |5000 |买家支付的运费。
   `shipping_fee` = `original_shipping_fee` - `shipping_fee_seller_discount` - `shipping_fee_platform_discount`
   对于 US 市场，此为税前总金额。 |
   ^^^seller_discount |string |5000 |卖家提供的商品折扣。 |
   ^^^platform_discount |string |5000 |平台提供的商品折扣。 |
   ^^^payment_platform_discount |string |10 |由支付平台出资的订单折扣 |
   ^^^payment_discount_service_fee |string |10 |买家为使用支付平台折扣而支付的服务费 |
   ^^^total_amount |string |5000 |买家支付的总金额。
   `total_amount` = `sub_total` + `shipping_fee` + `taxes` + `retail_delivery_fee` |
   ^^^original_total_product_price |string |5000 |商品的原始总价（跨境店铺含 VAT）。
   对于 US 市场，此为税前总金额。 |
   ^^^original_shipping_fee |string |5000 |折扣前的运费 |
   ^^^shipping_fee_seller_discount |string |5000 |卖家为不符合共同出资报销条件的订单提供的运费折扣。**说明**：如果订单达到共同出资报销的最低订单金额，此值为 0。此时，买家获得的运费折扣请参阅 `shipping_fee_cofunded_discount`。 |
   ^^^shipping_fee_platform_discount |string |5000 |平台提供的运费折扣。 |
   ^^^shipping_fee_cofunded_discount |string |7 |卖家提供的运费折扣，根据 Co-Funded Free Shipping 计划条款，订单送达后有资格获得共同出资报销。**说明**：对于未达到共同出资报销最低订单金额的订单，此值为 0。此时，买家获得的运费折扣请参阅 `shipping_fee_seller_discount`。 |
   ^^^tax |string |5000 |买家支付的订单总税费。适用于跨境店铺和 US 市场。 |
   ^^^small_order_fee |string |3000 |TH 的小额订单费。
   小额订单费仅适用于泰国。小额订单费是指平台会设定最低订单消费金额，当订单金额低于最低订单消费金额时，用户需支付小额订单费以达到平台最低消费金额。
   e.g. 最低订单消费金额为 100，订单金额为 80，因此小额订单费为 20。 |
   ^^^shipping_fee_tax |string |11 |运费的税费。 |
   ^^^product_tax |string |21.3 |商品总价的税费。 |
   ^^^retail_delivery_fee |string |1.28 |RDF（零售配送费）。仅适用于 US 市场。 |
   ^^^buyer_service_fee |string |1000 |每笔交易均收取服务费。自第五笔订单起收取，并在结账时直接向客户收取。仅适用于印度尼西亚市场。 |
   ^^^handling_fee |string |1000 |向买家收取的费用，用于支付与所选支付方式相关的额外处理、操作和/或分期成本。 |
   ^^^shipping_insurance_fee |string |1000 |买家为保障商品在运输途中丢失或损坏而产生的费用。
   **说明**：仅适用于印度尼西亚市场。 |
   ^^^item_insurance_fee |string |1000 |买家为保障商品购买后出现缺陷或损坏而产生的费用。
   **说明**：仅适用于 US 和印度尼西亚市场。 |
   ^^^item_insurance_tax |string |10 |买家购买的保险所支付的税费。

说明：仅适用于 US 市场。 |
^^^distance_shipping_fee |string |1000 |距离配送费由我们的物流合作伙伴收取，用于覆盖 Horizon+ Program 中爪哇岛以外配送产生的按距离计费的独立成本。
仅适用于 ID 市场。 |
^^^distance_fee |string |2000 |Horizon+ Program 的总距离费用。仅适用于 ID 市场 |
^^recipient_address |object | |`recipient_address` 在 `UNPAID` 和 `ON_HOLD` 状态下不可用。 |
^^^full_address |string |1199 Coleman Ave San Jose, CA 95110 |完整的收件地址信息。 |
^^^phone_number |string |(+1)213-***-1234 |买家的电话号码。请注意，如果此订单使用平台物流，电话号码将脱敏。 |
^^^name |string |David Kong |收件人姓名。请注意，如果此订单使用平台物流，收件人姓名将脱敏 |
^^^first_name |string |David |收件人的名字。如果买家未分别提供名字和姓氏，此参数的取值将与 "name" 参数相同。 |
^^^last_name |string |Kong |收件人的姓氏。如果买家未分别提供名字和姓氏，此参数将为空。 |
^^^first_name_local_script |string |ジョン |片假名形式的收件人名字。
**注意**：仅适用于 JP 市场。 |
^^^last_name_local_script |string |ドゥ |片假名形式的收件人姓氏。
**注意**：仅适用于 JP 市场。 |
^^^region_code |string |US |地区代码。 |
^^^postal_code |string |95110 |卖家可用于配送的邮政编码（在 U.S 中为 ZIP code）。 |
^^^post_town |string |Ribbleton |地址的邮政城镇
说明：仅适用于 UK 市场 |
^^^address_line1 |string |TikTok 5800 bristol Pkwy |街道地址第一行。 |
^^^address_line2 |string |Suite 100 |街道地址第二行 |
^^^address_line3 |string |Vila Olímpia |街道地址第三行。 |
^^^address_line4 |string |Avenida Presidente Juscelino Kubitschek |街道地址第四行。 |
^^^district_info |[]object | |行政区信息列表。 |
^^^^address_level_name |string |Country |卖家可用于配送的行政区划名称。e.g. state/county/city/district/town etc。 |
^^^^address_name |string |United Kingdom |行政区域名称。eg: London |
^^^^address_level |string |L0 |行政区划层级代码。取值可为 L0/L1/L2/L3/L4。eg. US is L0 |
^^^^iso_code |string |VAN |行政区划层级的 ISO 代码 |
^^^delivery_preferences |object | |包含买家为收货地址提供的所有配送说明。目前仅适用于 US 市场。 |
^^^^drop_off_location |string |Front Door |买家选择的投放位置。 |
^^^address_detail |string |Unit one building 8 |买家的完整详细地址。 |
^^buyer_message |string |Please ship asap! |买家留言。 |
^^create_time |int |1619611561 |订单创建的日期和时间。Unix 时间戳。 |
^^tracking_number |string |JX12345 |运单号。包裹发货后可用。 |
^^cancel_reason |string |Pricing error |订单级别的取消原因。
**说明**：多行订单的多个商品可能具有不同的 `cancel_reason`。
发生此情况时，订单级别的 `cancel_reason` 将显示首个行商品的 `cancel_reason`。
[参见此处](https://partner.tiktokshop.com/docv2/page/cancel-reasons) 了解更多取消原因的详情。 |
^^rts_sla_time |int |1619611688 |平台指定的最晚发货时间。Unix 时间戳。 |
^^paid_time |int |1619611563 |订单支付的日期和时间。Unix 时间戳。 |
^^fulfillment_type |string |FULFILLMENT_BY_SELLER |履约类型。
只有具有履约类型的订单才能由卖家发货。
可能的值：

* `FULFILLMENT_BY_SELLER`：卖家直接从自有库存履约订单、不使用 TikTok 履约中心的方式。在此模式下，卖家负责存储、包装商品并将其配送给客户。
* `FULFILLMENT_BY_TIKTOK`：TikTok 提供的服务，使卖家可将商品送至 TikTok 履约中心。随后由 TikTok 负责存储、拣货、包装并将商品配送给客户。
* `FULFILLMENT_BY_DILAYANI_TOKOPEDIA`：Tokopedia GoTo Logistics 向卖家提供仓储和物流服务并就此收费的方式。 |
   ^^seller_note |string |卖家 note |此字段返回卖家在 TikTok Seller Center 中填写的备注。 |
   ^^tts_sla_time |int |1619611761 |平台指定的最晚揽收时间。
   Unix timestamp. |
   ^^cancel_order_sla_time |int |1619621355 |平台指定的订单自动取消时间。
   Unix timestamp. |
   ^^update_time |int |1619621355 |订单状态变更的时间。
   Unix timestamp. |
   ^^packages |[]object | |此订单包含的包裹列表 |
   ^^^id |string |1152321127278713123 |包裹 ID |
   ^^delivery_type |string |HOME_DELIVERY |指示是否为 PickUp DropOff (PUDO) 地点。PUDO 地点由买家下单时选择。
* `HOME_DELIVERY`：非 PUDO 地点
* `COLLECTION_POINT`：PUDO 地点 |
   ^^is_sample_order |bool |false |使用此字段判断订单是否为样品订单。 |
   ^^warehouse_id |string |6955005333819123123 |卖家仓库 ID。 |
   ^^split_or_combine_tag |string |COMBINED |指示订单是合并还是拆分。
* `COMBINED`
* `SPLIT`
   此字段将在未来的履约接口中使用。 |
   ^^has_updated_recipient_address |bool |false |收件地址是否已更新。
* `false`: no update
* `true`: updated |
   ^^cpf |string |3213-31231412 |CPF（发票号码），用于开具发票。仅适用于巴西市场。 |
   ^^delivery_option_id |string |7091146663229654785 |订单配送选项 ID。 |
   ^^delivery_sla_time |int |1678389618 |订单应在此日期前送达，方视为准时并避免延迟配送处罚。 |
   ^^payment_method_name |string |CCDC |支付方式名称，仅用于展示 |
   ^^payment_card_type |string |Debit
   |用于区分不同支付方式的代码。仅当支付方式使用银行卡时赋值。可取值为: Debit, Credit, Prepaid |
   ^^channel_entity_national_registry_id |string |26.545.167/0001-21 |支付机构/债权人的国家渠道实体注册 ID。在巴西，为支付机构的 CNPJ。 |
   ^^payment_method_code |string |pm_pi_ccdc_visa_c_d |标识当前交易的支付方式代码。若为卡交易，将包含支付方式和卡品牌。 |
   ^^payment_auth_code |string |AUTH123457 |当前交易的授权码（仅适用于巴西市场）。
   对于卡交易（信用卡/借记卡），此字段为交易授权码。对于 PIX 交易，此字段为 E2E ID。 |
   ^^shipping_due_time |int |1678389618 |如果订单在此时间之前未将状态更新为 `AWAITING_COLLECTION`，订单将被 TikTok Shop 自动取消。 |
   ^^line_items |[]object | |行商品信息列表。 |
   ^^^id |string |577086512123755123 |行商品 ID。 |
   ^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^combined_listing_skus |[]object | |对于虚拟捆绑 SKU，返回组成该虚拟捆绑 SKU 的相关商品 SKU 数组。 |
   ^^^^sku_id |string |2729382476852921123 |与虚拟捆绑 SKU 关联的原始 `sku_id`。 |
   ^^^^sku_count |int |1 |组成虚拟捆绑 SKU 的原始 SKU 数量。 |
   ^^^^product_id |string |1729582718312380456 |与虚拟捆绑 SKU 关联的原始 `product_id`。 |
   ^^^^seller_sku |string |yellow-24-XL |与虚拟捆绑 SKU 关联的原始 `seller_sku`（由卖家定义）。 |
   ^^^product_id |string |1729582718312380123 |商品 ID。 |
   ^^^product_name |string |Women's Winter Crochet Clothes |商品名称。 |
   ^^^sku_name |string |Iphone |SKU 名称，由商品 SKU 属性（如尺码或颜色）组合而成。例如，"Black, 26." |
   ^^^sku_image |string |https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839 |SKU 图片。 |
   ^^^original_price |string |0.01 |商品原价，请参阅 `payment_info` 的货币。 |
   ^^^sale_price |string |0.01 |商品售价，请参阅 `payment_info` 的货币。 |
   ^^^pfand_fee |string |1.5 |适用于某些商品的押金费，通常为瓶罐等饮料容器。
   **说明** 仅适用于德国市场 |
   ^^^platform_discount |string |0 |平台折扣金额，请参阅 `payment_info` 的货币。 |
   ^^^display_status |string |TO_SHIP |- `UNPAID`：订单已下单，但尚未完成支付。
* `AWAITING_SHIPMENT`：订单已准备好发货，但尚未发出任何商品。
* `AWAITING_COLLECTION`：已安排发货，但包裹正等待承运商揽收。
* `IN_TRANSIT`：承运商已揽收包裹，正在配送中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不再允许退货或退款。
* `CANCELLED`：订单已取消。 |
   ^^^cancel_user |string |BUYER |取消请求的发起方:
* `BUYER`
* `SELLER`
* `OPERATOR`
* `SYSTEM` |
   ^^^sku_type |string |PRE_ORDER |[**已弃用**：此字段已弃用，将在未来的 API 版本中移除。请改用 `order_type`。]
   订单行类型：
   基于地区的可能值：
   **All regions**
* `NORMAL`：有库存且可立即购买和履约的商品。
* `ZERO_LOTTERY:` TikTok LIVE 抽奖活动中购买的商品。
* `SHOP_PARTNER`：从 TikTok Shop 合作伙伴店铺购买的商品。
   **US**
* `PRE_ORDER`：尚未上架或发售的商品。履约在未来特定日期开始。
* `MADE_TO_ORDER`：仅在收到订单后才生产的商品。履约在商品生产完成后开始。 |
   ^^^seller_sku |string |red_iphone_256 |商品的卖家库存单位（SKU）。 |
   ^^^shipping_provider_id |string |6617675021119438849 |商品的物流服务商 ID。 |
   ^^^seller_discount |string |0 |卖家折扣金额。请参阅 `payment_info` 的货币。 |
   ^^^currency |string |IDR |支付货币。 |
   ^^^package_id |string |1153132168123859123 |一个订单可根据卖家选择的配送方式包含一个或多个包裹。每个包裹都有唯一的 `package_id`（以及 `tracking_id`，用于跟踪包裹的配送进度）。对于 US 和 UK 市场的本地卖家，在包裹发货前不会返回 `package_id` 和 `package_status` 属性 |
   ^^^rts_time |int |1678389618 |卖家发货行订单的时间（成功调用 Ship Order 端点）。
   Unix timestamp. |
   ^^^item_tax |[]object | |商品税费明细。 |
   ^^^^tax_type |string |SALES_TAX |税费类型。
* `SALES_TAX`（US 市场销售税）
   目前仅支持销售税。 |
   ^^^^tax_amount |string |21.2 |税费金额。 |
   ^^^^tax_rate |string |0.35 |税率。 |
   ^^^package_status |string |TO_FULFILL |商品的包裹状态:
* `TO_FULFILL`：包裹等待卖家安排发货。
* `PROCESSING`：卖家已安排包裹发货。等待承运商揽收包裹。
* `FULFILLING`：包裹已被承运商揽收，正在运输中。
* `COMPLETED`：包裹已送达。
* `CANCELLED`：包裹已取消。通常，包裹因丢失或损坏而被取消。 |
   ^^^shipping_provider_name |string |TT Virtual express |商品的物流服务商名称。 |
   ^^^is_gift |bool |false |指示当前订单行是否为赠品。 |
   ^^^cancel_reason |string |Discount not as expected |商品取消原因。 |
   ^^^small_order_fee |string |5000 |TH 的小额订单费。 |
   ^^^retail_delivery_fee |string |1.28 |RDF（零售配送费）。仅适用于 US 市场。 |
   ^^^tracking_number |string |JX12345 |运单号。包裹发货后可用。 |
   ^^^buyer_service_fee |string |1000 |每笔交易均收取服务费。自第五笔订单起收取，并在结账时直接向客户收取。仅适用于印度尼西亚市场。 |
   ^^^handling_duration_days |string |7 |[**已弃用**：此字段已弃用，将在未来的 API 版本中移除。请改用 `handling_duration`。]
   订单下达后，卖家处理订单并将其交给配送承运商所需的工作日数。
   仅当 `sku_type` 的取值为 `MADE_TO_ORDER` 时适用。 |
   ^^^is_dangerous_good |bool |true |SKU 是否为危险品。为危险品创建面单时，必须遵循平台规则将某些商品放入同一包裹。请参阅 `sku_id` 与 `package_id` 的关系以确定如何遵循平台规则。 |
   ^^^needs_prescription |bool |true |指示所含商品是否需要处方的标志。 |
   ^^^gift_retail_price |string |20 |直播赠品、免费样品和满赠赠品订单中免费商品的零售价。对于其他订单，此字段始终返回 0。
   此金额可用于巴西的免费样品和直播赠品订单发票 |
   ^^^is_unboxing_item |bool |false |如果为 `true`，表示 SKU 是盲盒商品，需要开盒才能向买家展示实际商品。开盒完成后，也可将实际商品的 SKU 名称和图片更新至 TikTok。

注意：目前仅适用于 US 市场。 |
^^^unboxing_sku_code |string |14531134 |卖家为开盒后实际商品设置的第三方 sku 代码，仓库履约操作可据此识别所配送的准确商品。
注意：目前仅在美国市场可用。
|
^^^unboxing_case_list |[]object | |卖家为整箱开盒商品设置的第三方 sku 代码，仓库履约操作可据此识别所配送的准确商品。
注意：目前仅适用于 US 市场。 |
^^^^unbox_sku |string |14531134 |与开盒后实际商品关联的开盒 sku 代码。 |
^^^^unbox_sku_type |string |GIFT |指示开盒 sku 是否为赠品
枚举值: NORMAL 或 GIFT |
^^^sub_item_info |[]object | |子商品表示属于卖家定义的"虚拟捆绑"的 SKU。sub_item_info 将包含作为虚拟捆绑一部分需履约的每个商品的所有相关信息。
说明：任何 SKU 的每个数量都有唯一的 sub_item_info "id"，使卖家能够在商品分散于不同仓库位置时执行行级履约。 |
^^^^id |string |577086512123755123 |sub_item 的行商品 ID。执行拆分/行级履约事件时可使用此唯一标识符。 |
^^^^sku_id |string |2729382476852921560 |SKU ID. |
^^^^display_status |string |UNPAID |可用取值:

* `UNPAID`：订单已下单，但支付尚未完成。
* `AWAITING_SHIPMENT`：订单已可发货，但尚无任何商品发货。
* `AWAITING_COLLECTION`：已安排发货，但包裹等待承运商揽收。
* `IN_TRANSIT`：包裹已被承运商揽收，正在配送中。
* `DELIVERED`：包裹已送达买家。
* `COMPLETED`：订单已完成，不允许再退货或退款。
* `CANCELLED`：订单已取消。 |
   ^^^^product_name |string |Women's Winter Crochet Clothes |商品名称。 |
   ^^^^seller_sku |string |red_iphone_256 |商品的卖家库存单位（SKU）。 |
   ^^^^sku_image |string |https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839 |SKU 图片。 |
   ^^^^sku_name |string |Iphone |SKU 名称，由商品 SKU 属性（如尺码或颜色）组合而成。e.g. "Black, 26" |
   ^^^^product_id |string |1729582718312380123 |商品 ID。 |
   ^^^^sale_price |string |0.01 |商品售价。请参阅 `payment_info` 的货币。 |
   ^^^^platform_discount |string |0 |平台折扣金额。请参阅 `payment_info` 的货币。 |
   ^^^^seller_discount |string |0 |卖家折扣金额。请参阅 `payment_info` 的货币。 |
   ^^^^cancel_reason |string |Discount not as expected |取消原因。请访问 [取消原因列表](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d) 了解更多信息。 |
   ^^^^original_price |string |0.01 |商品原价。请参阅 `payment_info` 的货币。 |
   ^^^^rts_time |int |1678389618 |卖家发货订单的时间（成功调用 [Ship Package API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1)）。Unix 时间戳。 |
   ^^^^package_status |string |TO_FULFILL |商品的包裹状态。
   Available values:
* `TO_FULFILL`：包裹等待卖家安排发货。
* `PROCESSING`：卖家已安排发货。等待承运商揽收。
* `FULFILLING`：包裹已被承运商揽收，正在运输中。
* `COMPLETED`：包裹已送达。
* `CANCELLED`：包裹已取消。通常，包裹因丢失或损坏而被取消。 |
   ^^^^currency |string |USD |支付货币。 |
   ^^^^shipping_provider_name |string |TT Virtual express |物流服务商名称。 |
   ^^^^cancel_user |string |BUYER |取消请求的发起方。
   Available values:
* `BUYER`
* `SELLER`
* `OPERATOR`
* `SYSTEM` |
   ^^^^shipping_provider_id |string |6617675021119438849 |商品的物流服务商 ID。 |
   ^^^^item_tax |[]object | |商品税费明细。 |
   ^^^^^tax_type |string |SALES_TAX |税费类型。
   Available values:
* `SALES_TAX`（US 市场销售税）

**说明**：目前仅支持销售税。 |
^^^^^tax_amount |string |21.2 |税费金额。 |
^^^^^tax_rate |string |0.35 |税率。 |
^^^^tracking_number |string |JX12345 |运单号。包裹发货后可用。 |
^^^^package_id |string |1153132168123859123 |一个订单可根据卖家选择的配送方式包含一个或多个包裹。每个包裹都有唯一的 `package_id` 和 `tracking_id`。 |
^^^^retail_delivery_fee |string |1.28 |零售配送费（RDF）。
**说明**：仅适用于 US 市场。 |
^^^^is_dangerous_good |bool |false |SKU 是否为危险品。为危险品创建面单时，必须遵循平台规则将某些商品放入同一包裹。请参阅 `sku_id` 与 `package_id` 的关系以确定如何遵循平台规则。 |
^^^^warehouse_id |string |6955005333819123123 |卖家仓库 ID。 |
^^^distance_shipping_fee |string |1000 |距离配送费由我们的物流合作伙伴收取，用于覆盖 Horizon+ Program 中爪哇岛以外配送产生的按距离计费的独立成本。
仅适用于 ID 市场。 |
^^^distance_fee |string |2000 |Horizon+ Program 的总距离费用。仅适用于 ID 市场 |
^^^shipping_vat_amount |string |3.5 |运费 VAT 金额
适用于 EU 市场 |
^^^shipping_vat_rate |string |0.25 |运费 VAT 税率
适用于 EU 市场 |
^^^is_pod_customized |bool |false |标识此 SKU 是否包含按需打印定制 |
^^^pod_info_id |string |789123812334 |按需打印定制详情的 ID。此 ID 可用于查询定制的确切详情 |
^^^room_id |string |7652884452049160991 |创建该订单行商品的 LIVE 会话的唯一 ID。如果订单行商品并非从 LIVE 会话创建，此字段返回空字符串。 |
^^^product_listing_type |string |TEMPORARY_LISTING |描述 SKU 的商品上架类型。
可能的值：

* `TEMPORARY_LISTING` |
   ^^shipping_type |string |TIKTOK |配送方式。
* `TIKTOK`：TikTok 提供的配送服务。卖家应从 TikTok 获取面单。
* `SELLER`：由卖家提供配送，包括通过代表卖家的第三方履约服务商。
* `TIKTOK_DIGITAL`：Tiktok 直接向买家交付虚拟商品。无需任何操作。 |
   ^^buyer_email |string |v2b2V5@chat.卖家.tiktok.com |买家的匿名化邮箱地址。不建议直接向此邮箱地址发送消息。如需联系买家，请前往 Seller Center - Buyer Messages 页面。 |
   ^^delivery_time |int |1678389618 |订单状态更新为 `DELIVERED` 的时间戳。 |
   ^^need_upload_invoice |string |NEED_INVOICE |是否需要上传发票及上传状态（仅适用于巴西市场）。
* UNKNOWN: 目前无法确认是否需要发票
* NEED_INVOICE: 此订单需要发票且尚未上传发票
* NO_NEED：此订单不需要发票
* INVOICE_UPLOADED: 此订单的发票已上传并核验。如果订单被拆分，一旦任意子订单的发票上传，即标记为 "uploaded"。
* INVOICE_PROCESSING: 此订单的发票正在上传/取消中。请等待最终结果，不要重复操作 |
   ^^is_cod |bool |false |此选项适用于接受货到付款的卖家（较少见）。买家将在收到包裹时以现金支付。默认值为 `FALSE`。仅适用于支持货到付款（COD）的国家。 |
   ^^request_cancel_time |int |1678389618 |买家请求取消的时间。 |
   ^^delivery_option_required_delivery_time |int |1678389618 |订单应在此时间之前送达。 |
   ^^delivery_option_name |string |Express shipping |配送选项名称。仅用于展示。 |
   ^^is_buyer_request_cancel |bool |false |当买家有待处理的取消请求时为 True |
   ^^delivery_due_time |int |1678389618 |如果订单在此时间之前未将状态更新为 `DELIVERED`，订单将被 TikTok Shop 自动取消。 |
   ^^collection_time |int |1678389618 |订单状态更新为 `IN_TRANSIT` 的时间戳。 |
   ^^is_on_hold_order |bool |false |指示订单是否经历过或将经历 `ON_HOLD` 状态。 |
   ^^cancel_time |int |1678389618 |订单状态更新为 `CANCELLED` 的时间戳。 |
   ^^is_replacement_order |bool |false |为 true 时，表示这是换货订单。 |
   ^^replaced_order_id |string |576461416728782174 |被替换订单的订单 ID。仅当 `is_replacement_order` = `true` 时返回 |
   ^^collection_due_time |int |1678389618 |如果订单在此时间之前未将状态更新为 `IN_TRANSIT`，订单将被 TikTok Shop 自动取消 |
   ^^pick_up_cut_off_time |int |1678389618 |为避免 LDR，必须确保包裹在此时间之前被揽收。仅适用于东南亚地区。 |
   ^^fast_dispatch_sla_time |int |1678389618 |获得 NDD（Next Day Delivery）项目激励的最晚揽收时间。Unix 时间戳
   仅适用于泰国和菲律宾。 |
   ^^commerce_platform |string |TIKTOK_SHOP |下单所在的平台。
   可能的值：
* `TIKTOK_SHOP`
* `TOKOPEDIA`
* `TIKTOK_SHOP_APP`
   **说明**：`Tokopedia` 和 `Tiktok Shop App` 仅适用于 SEA 市场。 |
   ^^order_type |string |ZERO_LOTTERY |订单类型。
   基于地区的可能值：
   **All regions**
* `NORMAL`：有库存且可立即购买和履约的商品。
* `ZERO_LOTTERY`：TikTok LIVE 抽奖活动中下达的订单。
* `AUCTION`：拍卖期间下达的订单，商品价格不固定。
   **US**
* `PRE_ORDER`：尚未上架或发售商品的预订订单。履约在未来特定日期开始。
* `MADE_TO_ORDER`：仅在收到订单后才生产商品的订单。履约在商品生产完成后开始。
* `BACK_ORDER`：缺货但预计将补货商品的订单。履约在商品补货后开始。
* `VIRTUAL_ORDER`：数字商品订单，无需实物配送。支付确认后立即或自动履约。
   对于标准订单或不属于上述类别的其他类型，返回空值。 |
   ^^release_date |int |1619611762 |订单处理开始且订单状态变更为 [AWAITING_SHIPMENT](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011) 的日期。
   仅当 `order_type` 为 `PRE_ORDER` 时适用。 |
   ^^handling_duration |object | |下单后卖家处理订单并将其交付给物流承运商的时长。
   仅当 `order_type` 为 `MADE_TO_ORDER` 或 `BACK_ORDER` 时适用。 |
   ^^^days |string |7 |天数。 |
   ^^^type |string |BUSINESS_DAY |指示时长按自然日还是工作日计算。
   可能的值：
* `CALENDAR_DAY`：表示连续天数，包括周末和节假日。
* `BUSINESS_DAY`：表示工作日，不包括周末和公共假日。
   Default: `BUSINESS_DAY` |
   ^^auto_combine_group_id |string |12345677 |在 Seller Center 中激活 "auto-combination" 时，为 LIVE 会话中同一客户的订单分配的标识符，以便合并订单发货。 |
   ^^cpf_name |string |John Smith |巴西市场 CPF 号码对应的姓名。 |
   ^^is_exchange_order |bool |false |为 TRUE 时，表示这是换货订单。
   注意：仅适用于 US 和 UK。 |
   ^^exchange_source_order_id |string |576461413038785752 |如果订单是换货订单，此字段返回生成该换货订单的原始订单的订单 ID。
   仅当 is_exchange_order = true 时返回。
   注意：仅适用于 US 和 UK。 |
   ^^is_subscription_order |bool |true |订阅订单是客户设置的周期性订单。如果为 TRUE，此订单由订阅订单生成 |
   ^^is_refundable_sample |bool |false |指示订单是否为可退款样品。可退款样品让卖家与达人协作，仅当达人达到销售门槛时才退还商品成本。 |
   ^^authentication_required |bool |false |如果为 true，订单需要鉴定。下单后使用经批准的自有鉴定服务进行验证。此操作必须在发货前完成。 |
   ^^consultation_id |string |123241 |用于标识相应 ePharmacy 问诊的 ID。
   仅当发起过 ePharmacy 问诊时适用。如果处方由客户通过上传图片提供，则不适用。 |
   ^^fast_delivery_program |string |3_DAY_DELIVERY |展示在商品上的标识，用于告知买家卖家参与了快速配送计划，订单应在承诺的时间段内送达。
   可能的值：
* `3_DAY_DELIVERY`
* `3_DAY_POTENTIAL_SHIPPING`
* `3_DAY_POTENTIAL_TRANSIT`
   订单未满足快速配送时不返回
   program requirements.
   说明：仅适用于 US 市场。 |
   ^^buyer_nickname |string |user213123 |TikTok 买家的昵称，由 TikTok 用户定义。在 TikTok Live Session 中展示开盒结果时，可使用 buyer_nickname 识别买家。 |
   ^^buyer_avatar |string |https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839 |TikTok 买家的头像，由 TikTok 用户定义。在 TikTok Live Session 中展示开盒结果时，可结合 buyer_nickname 使用 buyer_avatar。 |
   ^^order_rights |[]int |[1] |根据卖家订阅的计划，订单在订单内具有特定权益时的订单标签标识。
   1 = 运费报销计划
   2 = Horizon+ Program
   仅适用于 SEA 市场 |
   ^^fulfillment_priority_level |int |100 |可用于优先发货的履约优先级值（仅适用于 SEA）
   100 = Instant
   200 = Sameday 8 Hours
   300 = Sameday
   400 = 次日达
   500 = Express
   600 = Standard
   700 = Economy
   800 = Cargo |
   ^^recommended_shipping_time |int |1619611561 |基于各 LSP 服务类型的建议发货时间（仅适用于 SEA） |
   ^^instore_pickup_sla_time |int |1784090976 |平台指定的到店自提方式的最晚买家提货时间。目前适用于 SEA 市场。Unix 时间戳。 |
   ^^fast_rts_sla_time |int |1784090976 |指示发货操作的快速履约 SLA。仅适用于 SEA 市场。Unix 时间戳 |
   ^^fast_collection_sla_time |int |1784090976 |指示揽收操作的快速履约 SLA。仅适用于 SEA 市场。Unix 时间戳 |

# 响应示例
```json
{"code":0,"data":{"orders":[{"id":"576461413038785752","cancellation_initiator":"SELLER","shipping_provider":"TT Virtual express","shipping_provider_id":"6617675021119438849","user_id":"7021436810468230477","status":"UNPAID","rts_time":1619611563,"payment":{"currency":"IDR","sub_total":"5000","shipping_fee":"5000","seller_discount":"5000","platform_discount":"5000","payment_platform_discount":"10","payment_discount_service_fee":"10","total_amount":"5000","original_total_product_price":"5000","original_shipping_fee":"5000","shipping_fee_seller_discount":"5000","shipping_fee_platform_discount":"5000","shipping_fee_cofunded_discount":"7","tax":"5000","small_order_fee":"3000","shipping_fee_tax":"11","product_tax":"21.3","retail_delivery_fee":"1.28","buyer_service_fee":"1000","handling_fee":"1000","shipping_insurance_fee":"1000","item_insurance_fee":"1000","item_insurance_tax":"10","distance_shipping_fee":"1000","distance_fee":"2000"},"recipient_address":{"full_address":"1199 Coleman Ave San Jose, CA 95110","phone_number":"(+1)213-***-1234","name":"David Kong","first_name":"David","last_name":"Kong","first_name_local_script":"ジョン","last_name_local_script":"ドゥ","region_code":"US","postal_code":"95110","post_town":"Ribbleton","address_line1":"TikTok 5800 bristol Pkwy","address_line2":"Suite 100","address_line3":"Vila Olímpia","address_line4":"Avenida Presidente Juscelino Kubitschek","district_info":[{"address_level_name":"Country","address_name":"United Kingdom","address_level":"L0","iso_code":"VAN"}],"delivery_preferences":{"drop_off_location":"Front Door"},"address_detail":"Unit one building 8"},"buyer_message":"Please ship asap!","create_time":1619611561,"tracking_number":"JX12345","cancel_reason":"Pricing error","rts_sla_time":1619611688,"paid_time":1619611563,"fulfillment_type":"FULFILLMENT_BY_SELLER","seller_note":"seller note","tts_sla_time":1619611761,"cancel_order_sla_time":1619621355,"update_time":1619621355,"packages":[{"id":"1152321127278713123"}],"delivery_type":"HOME_DELIVERY","is_sample_order":false,"warehouse_id":"6955005333819123123","split_or_combine_tag":"COMBINED","has_updated_recipient_address":false,"cpf":"3213-31231412","delivery_option_id":"7091146663229654785","delivery_sla_time":1678389618,"payment_method_name":"CCDC","payment_card_type":"Debit\n","channel_entity_national_registry_id":"26.545.167/0001-21","payment_method_code":"pm_pi_ccdc_visa_c_d","payment_auth_code":"AUTH123457","shipping_due_time":1678389618,"line_items":[{"id":"577086512123755123","sku_id":"2729382476852921560","combined_listing_skus":[{"sku_id":"2729382476852921123","sku_count":1,"product_id":"1729582718312380456","seller_sku":"yellow-24-XL"}],"product_id":"1729582718312380123","product_name":"Women's Winter Crochet Clothes","sku_name":"Iphone","sku_image":"https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839","original_price":"0.01","sale_price":"0.01","pfand_fee":"1.5","platform_discount":"0","display_status":"TO_SHIP","cancel_user":"BUYER","sku_type":"PRE_ORDER","seller_sku":"red_iphone_256","shipping_provider_id":"6617675021119438849","seller_discount":"0","currency":"IDR","package_id":"1153132168123859123","rts_time":1678389618,"item_tax":[{"tax_type":"SALES_TAX","tax_amount":"21.2","tax_rate":"0.35"}],"package_status":"TO_FULFILL","shipping_provider_name":"TT Virtual express","is_gift":false,"cancel_reason":"Discount not as expected","small_order_fee":"5000","retail_delivery_fee":"1.28","tracking_number":"JX12345","buyer_service_fee":"1000","handling_duration_days":"7","is_dangerous_good":true,"needs_prescription":true,"gift_retail_price":"20","is_unboxing_item":false,"unboxing_sku_code":"14531134","unboxing_case_list":[{"unbox_sku":"14531134","unbox_sku_type":"GIFT"}],"sub_item_info":[{"id":"577086512123755123","sku_id":"2729382476852921560","display_status":"UNPAID","product_name":"Women's Winter Crochet Clothes","seller_sku":"red_iphone_256","sku_image":"https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839","sku_name":"Iphone","product_id":"1729582718312380123","sale_price":"0.01","platform_discount":"0","seller_discount":"0","cancel_reason":"Discount not as expected","original_price":"0.01","rts_time":1678389618,"package_status":"TO_FULFILL","currency":"USD","shipping_provider_name":"TT Virtual express","cancel_user":"BUYER","shipping_provider_id":"6617675021119438849","item_tax":[{"tax_type":"SALES_TAX","tax_amount":"21.2","tax_rate":"0.35"}],"tracking_number":"JX12345","package_id":"1153132168123859123","retail_delivery_fee":"1.28","is_dangerous_good":false,"warehouse_id":"6955005333819123123"}],"distance_shipping_fee":"1000","distance_fee":"2000","shipping_vat_amount":"3.5","shipping_vat_rate":"0.25","is_pod_customized":false,"pod_info_id":"789123812334","room_id":"7652884452049160991","product_listing_type":"TEMPORARY_LISTING"}],"shipping_type":"TIKTOK","buyer_email":"v2b2V5@chat.seller.tiktok.com","delivery_time":1678389618,"need_upload_invoice":"NEED_INVOICE","is_cod":false,"request_cancel_time":1678389618,"delivery_option_required_delivery_time":1678389618,"delivery_option_name":"Express shipping","is_buyer_request_cancel":false,"delivery_due_time":1678389618,"collection_time":1678389618,"is_on_hold_order":false,"cancel_time":1678389618,"is_replacement_order":false,"replaced_order_id":"576461416728782174","collection_due_time":1678389618,"pick_up_cut_off_time":1678389618,"fast_dispatch_sla_time":1678389618,"commerce_platform":"TIKTOK_SHOP","order_type":"ZERO_LOTTERY","release_date":1619611762,"handling_duration":{"days":"7","type":"BUSINESS_DAY"},"auto_combine_group_id":"12345677","cpf_name":"John Smith","is_exchange_order":false,"exchange_source_order_id":"576461413038785752","is_subscription_order":true,"is_refundable_sample":false,"authentication_required":false,"consultation_id":"123241","fast_delivery_program":"3_DAY_DELIVERY","buyer_nickname":"user213123","buyer_avatar":"https://p16-oec-va.itexeitg.com/tos-maliva-d-o5syd03w52-us/46123e87d14f40b69b839","order_rights":[1],"fulfillment_priority_level":100,"recommended_shipping_time":1619611561,"instore_pickup_sla_time":1784090976,"fast_rts_sla_time":1784090976,"fast_collection_sla_time":1784090976}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10002014 | 获取订单失败，如果多次重试仍失败，请联系平台寻求帮助 |
| 10002015 | 获取订单失败，如果多次重试仍失败，请联系平台寻求帮助 |
| 10006402 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 10037002 | 获取订单失败，如果多次重试仍失败，请联系平台寻求帮助 |
| 10037003 | 获取订单失败，如果多次重试仍失败，请联系平台寻求帮助 |
| 10037004 | 获取订单失败，如果多次重试仍失败，请联系平台寻求帮助 |
| 21008111 | The order or package does not belong to the current seller. |

