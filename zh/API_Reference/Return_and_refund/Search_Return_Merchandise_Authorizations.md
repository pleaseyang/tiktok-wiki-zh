# 搜索退货授权

# 路径：/return_refund/202604/rma/search
# 方法：[POST]
# 功能描述
搜索已授权店铺的退货授权（RMA）。可按标识符、RMA 状态以及创建或更新时间进行筛选。使用 `whitelisted_data_fields` 可在每个 RMA 中包含行项目或 SKU 退货请求。

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
| locale | string | N | en-US | 用于展示的 BCP-47 语言区域代码. 默认值: `en` |
| 有关支持的语言区域代码列表，请参阅 [Locale codes](https://partner.tiktokshop.com/docv2/page/678e3a47bae28f030a8c7523)。 |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| whitelisted_data_fields | []string | N | ["LINE_ITEMS","SKU_RETURN_REQUESTS"] | 控制每个 RMA 包含哪些附加字段。 |
| 可能的值： |  |  |  |  |

* `LINE_ITEMS`: Includes `line_items`.
* `SKU_RETURN_REQUESTS`: Includes `sku_return_requests`. |
   filters |object |N | |用于缩小结果集的筛选条件。 |
   ^rma_ids |[]string |N |["2894521704838895640"] |将结果限定为指定的 RMA 记录。每个 RMA ID 必须是可容纳于有符号 64 位整数内的十进制整数字符串。 |
   ^package_ids |[]string |N |["2894521704838895645"] |将结果限定为指定的包裹。每个包裹 ID 必须是可容纳于有符号 64 位整数内的十进制整数字符串。 |
   ^^^statuses |[]string |N |["PENDING_PACKAGE_REVIEW"] |将结果限定为指定的 RMA 数据状态。
   可能的值：
* `INIT`
* `AWAITING_BUYER_RETURN`
* `RETURN_IN_TRANSIT`
* `PENDING_PACKAGE_REVIEW`
* `PACKAGE_REVIEW_COMPLETED` |
   ^aftersales_request_ids |[]string |N |["4035319218955782461"] |将结果限定为指定的售后请求。每个 ID 必须是可容纳于有符号 64 位整数内的十进制整数字符串。 |
   ^main_order_ids |[]string |N |["577686530908261117"] |将结果限定为指定的主(正向)订单 ID。 |
   ^time |object |N | |基于时间的筛选条件。 |
   ^^create_time |object |N | |按创建时间筛选。 |
   ^^^min_unix_time_inclusive |int |N |1774486592 |含边界的下限 (Unix 秒)。 |
   ^^^max_unix_time_exclusive |int |N |1774572992 |不含边界的上限 (Unix 秒)。 |
   ^^update_time |object |N | |按最后更新时间筛选。 |
   ^^^min_unix_time_inclusive |int |N |1774486592 |含边界的下限 (Unix 秒)。 |
   ^^^max_unix_time_exclusive |int |N |1774572992 |不含边界的上限 (Unix 秒)。 |
   sort |object |N | |结果集的排序条件。 |
   ^sort_field |string |N |CREATE_TIME |用于排序结果的字段。
   可能的值：
* `CREATE_TIME`
* `UPDATE_TIME` |
   ^sort_order |string |N |ASC |排序方向。
   可能的值：
* `ASC`
* `DESC` |
   pagination |object |N | |分页配置。 |
   ^page_size |int |N |100 |每页返回的记录数。最小值: 1。最大值: 100。 |
   ^page_token |string |N |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |标识要获取的页面。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202604/rma/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

**Body**
```json
{"whitelisted_data_fields":["LINE_ITEMS","SKU_RETURN_REQUESTS"],"filters":{"rma_ids":["2894521704838895640"],"package_ids":["2894521704838895645"],"statuses":["PENDING_PACKAGE_REVIEW"],"aftersales_request_ids":["4035319218955782461"],"main_order_ids":["577686530908261117"],"time":{"create_time":{"min_unix_time_inclusive":1774486592,"max_unix_time_exclusive":1774572992},"update_time":{"min_unix_time_inclusive":1774486592,"max_unix_time_exclusive":1774572992}}},"sort":{"sort_field":"CREATE_TIME","sort_order":"ASC"},"pagination":{"page_size":100,"page_token":"aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA=="}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^return_merchandise_authorizations | []object |  | 符合筛选条件的退货授权（RMA）记录列表。当没有匹配的记录时，此字段会被省略。 |
| ^^id | string | 2894521704838895640 | 此 RMA 数据的唯一标识符。 |
| ^^package_id | string | 2894521704838895645 | 关联的实体退货包裹的标识符。 |
| ^^aftersales_request_id | string | 4035318504086604101 | 父售后请求的标识符。 |
| ^^status | string | AWAITING_BUYER_RETURN | 此 RMA 数据的当前状态。 |
| 可能的值： |  |  |  |

* `INIT`
* `AWAITING_BUYER_RETURN`
* `RETURN_IN_TRANSIT`
* `PENDING_PACKAGE_REVIEW`
* `PACKAGE_REVIEW_COMPLETED` |
   ^^line_items |[]object | |此退货包裹中预期的商品件数。仅当 `LINE_ITEMS` 包含在 `whitelisted_data_fields` 中且存在匹配的商品数据时，才返回此字段。 |
   ^^^return_line_item_id |string |4035227657962164811 |此商品在该退货中的唯一标识符。对于虚拟组合装，此值对应原始父商品组合装的 id。 |
   ^^^sub_return_line_item_id |string |4035227657962164815 |此商品在该退货中的唯一标识符。对于虚拟组合装，此值对应当前被退回的子商品的 id。 |
   ^^^sku_id |string |2729382476852921560 |与此商品关联的 SKU 标识符（用于商品详情）。 |
   ^^^main_order_id |string |577686530908261117 |关联的主 (正向) 订单的标识符。 |
   ^^^sku_return_request_id |string |4035318504086604100 |关联的 SKU 级别子退货请求的标识符。 |
   ^^sku_return_requests |[]object | |与此 RMA 关联的 SKU 级子退货请求。仅当 `SKU_RETURN_REQUESTS` 包含在 `whitelisted_data_fields` 中且存在匹配数据时，才返回此字段。 |
   ^^^order_id |string |577686530908261117 |与此 SKU 退货申请关联的 TikTok Shop 主订单 ID。 |
   ^^^return_id |string |4035318504086604100 |特定退货的标识符。 |
   ^^^return_type |string |REFUND |退货类型。
   Available values:
* `REFUND`: 卖家将不退货直接退款. 买家无需将商品寄回卖家。
* `RETURN_AND_REFUND`：买家需将商品寄回给卖家。卖家需先检查退回商品的状况，方可向买家退款。
* `REPLACEMENT`: 买家要求卖家更换商品。
* `EXCHANGE`: 买家要求卖家换货。 |
   ^^^return_status |string |RETURN_OR_REFUND_REQUEST_PENDING |退货状态。
   Available values:
* `RETURN_OR_REFUND_REQUEST_PENDING`: 买家已发起退货或退款请求. 该请求待卖家或平台审核。
* `REFUND_OR_RETURN_REQUEST_REJECT`：退货或退款申请被拒绝。
* `AWAITING_BUYER_SHIP`：退货申请已批准。卖家正等待买家将已批准的商品寄回。如果买家未在截止日期前将商品寄给卖家，平台将关闭该申请。
* `BUYER_SHIPPED_ITEM`：买家已将已批准的商品寄给卖家。
* `REJECT_RECEIVE_PACKAGE`: 卖家已检查退回商品并拒收退货包裹。
* `RETURN_OR_REFUND_REQUEST_SUCCESS`: 退货/退款申请已获批。买家将获得退款。
* `RETURN_OR_REFUND_REQUEST_CANCEL`：申请已被买家或系统取消。
* `RETURN_OR_REFUND_REQUEST_COMPLETE`：退货/退款已成功处理。买家已收到退款。
* `REPLACEMENT_REQUEST_PENDING`：买家已发起换货申请。该申请正等待卖家审核。
* `REPLACEMENT_REQUEST_REJECT`：卖家拒绝买家的换货申请。
* `REPLACEMENT_REQUEST_REFUND_SUCCESS`：因库存不足，买家的换货申请以退款方式处理。
* `REPLACEMENT_REQUEST_CANCEL`：买家取消了换货申请。
* `REPLACEMENT_REQUEST_COMPLETE`：卖家已批准买家的换货申请，平台将生成新订单供卖家履约。
* `AWAITING_BUYER_RESPONSE`：卖家向买家提供其他退货方式，等待买家响应。卖家提议的退货方式可查看 `seller_proposed_return_type`。
* `EXCHANGE_REQUEST_PENDING`：买家已发起换货申请。该申请正等待卖家审核。
* `EXCHANGE_REQUEST_REFUND_SUCCESS`：因库存不足，买家的换货申请以退款方式处理。
* `EXCHANGE_REQUEST_CANCEL`：买家取消了换货申请。
* `EXCHANGE_REQUEST_COMPLETE`: 卖家已批准买家的换货请求，平台将为卖家生成新订单以供履约。 |
   ^^^arbitration_status |string |IN_PROGRESS |仲裁状态。
   Available values:
* `IN_PROGRESS`: TikTok Shop 平台运营方正在处理仲裁并可能要求卖家提供额外信息。
* `SUPPORT_BUYER`: 平台运营方支持买家。
* `SUPPORT_SELLER`: 平台运营方支持卖家。
* `CLOSED`：仲裁已结束。 |
   ^^^role |string |BUYER |退货发起角色。
   Available values:
* `BUYER`
* `SELLER`
* `OPERATOR` : TikTok Shop 平台运营方。
* `SYSTEM`: TikTok Shop 系统。
   请参阅 "API 概览" 以了解更多关于角色的信息。 |
   ^^^return_reason |string |ecom_order_to_ship_canceled_reason_created_by_mistakes |退货的机器可读原因码。本地化展示文本请使用 `return_reason_text`。 |
   ^^^return_reason_text |string |Order created by mistake |退货原因，以本地化文本表示。
   可以使用 locale 请求参数更改语言。 |
   ^^^seller_next_action_response |[]object | |卖家的下一步操作和截止时间。 |
   ^^^^action |string |SELLER_RESPOND_REFUND |卖家的下一步操作。
   Available values:
* `SELLER_RESPOND_REFUND`
* `SELLER_RESPOND_RETURN`
* `SELLER_RESPOND_RECEIVE_PACKAGE`
* `SELLER_RESPOND_REPLACEMENT` |
   ^^^^deadline |int |1690554680 |卖家执行指定操作的截止时间，以秒为单位的 Unix 时间戳表示。 |
   ^^^shipment_type |string |PLATFORM |买家选择的将商品退回卖家的配送方式。
   Available values:
* `PLATFORM`: 买家使用 TikTok Shop 的配送服务. 关于买家使用 `DROP_OFF` 还是 `PICKUP`, 请参阅 `handover_method`。
* `BUYER_ARRANGE`: 买家安排退货配送。 |
   ^^^handover_method |string |DROP_OFF |买家使用平台的配送服务将商品退回给卖家时所选择使用的交接方式。
* `DROP_OFF`: 买家将把商品(s)送至快递点
* `PICKUP`: 买家正在预约承运商提供的上门取件服务。 |
   ^^^return_tracking_number |string |213456789098765433456 |买家退货时包裹的物流单号。 |
   ^^^return_provider_name |string |J&T Express |买家退货时包裹的承运商名称。 |
   ^^^return_provider_id |string |TH27014E9R5Q4G |买家退货时包裹的承运商 ID。 |
   ^^^pre_return_id |string |4035310341095393452 |当前退货订单编辑所依据的先前退货 ID。 |
   ^^^next_return_id |string |4035310341095393463 |当前退货单编辑后指向的下一个退货 ID。 |
   ^^^refund_amount |object | |退款金额详情。 |
   ^^^^currency |string |USD |支付货币。 |
   ^^^^refund_total |string |1.23 |向买家退款的总金额。 |
   ^^^^refund_subtotal |string |1 |向买家退款的小计金额。 |
   ^^^^refund_shipping_fee |string |0.2 |退还给买家的运费金额。 |
   ^^^^refund_tax |string |0.03 |退还给买家的退税金额。 |
   ^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费开始生效。 |
   ^^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^^^return_line_items |[]object | |退货订单行项目。 |
   ^^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^product_image |object | |商品图片信息。 |
   ^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^width |int |200 |商品图片宽度。单位：像素（px）。 |
   ^^^^^height |int |200 |商品图片高度。单位：像素（px）。 |
   ^^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^^seller_sku |string |PUTIH 1 TALI |卖家定义的 SKU 名称。 |
   ^^^^refund_amount |object | |退款金额明细。 |
   ^^^^^currency |string |USD |支付货币。 |
   ^^^^^refund_total |string |1.23 |退还买家的总金额。 |
   ^^^^^refund_subtotal |string |1 |退还买家的小计金额。 |
   ^^^^^refund_shipping_fee |string |0.2 |退还买家的配送费金额。 |
   ^^^^^refund_tax |string |0.03 |退还买家的税费金额。 |
   ^^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费开始生效。 |
   ^^^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^^^^return_sub_line_items |[]object | |退货子订单行项目。
   子项表示属于卖家定义的"虚拟组合装"的 SKU。sub_items 将包含虚拟组合装中每个商品的所有相关信息。 |
   ^^^^^return_sub_line_item_id |string |4035227657962164812 |退货子订单行 ID。 |
   ^^^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^^^sub_order_line_item_id |string |576473917261451852 |子订单行 ID。 |
   ^^^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^^product_image |object | |商品图片信息。 |
   ^^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^^width |int |200 |商品图片宽度. 单位: 像素 (px)。 |
   ^^^^^^height |int |200 |商品图片高度. 单位: 像素 (px)。 |
   ^^^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^^^seller_sku |string |PUTIH 1 TALI |卖家定义的 SKU 名称。 |
   ^^^^^refund_amount |object | |退款金额明细。 |
   ^^^^^^currency |string |USD |支付货币。 |
   ^^^^^^refund_total |string |1.23 |向买家退款的总金额。 |
   ^^^^^^refund_subtotal |string |1 |向买家退款的小计金额。 |
   ^^^^^^refund_shipping_fee |string |0.2 |退还给买家的运费金额。 |
   ^^^^^^refund_tax |string |0.03 |退还给买家的退税金额。 |
   ^^^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费开始生效。 |
   ^^^^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^^^create_time |int |1690451136 |退货创建时间，以秒为单位的 Unix 时间戳。 |
   ^^^update_time |int |1690453136 |退货最后一次更新的时间，以秒为单位的 Unix 时间戳。 |
   ^^^discount |object | |折扣退款金额，以 `refund_amount.currency` 指定的货币计价。 |
   ^^^^product_platform_discount |string |0.1 |平台折扣的退款金额。 |
   ^^^^product_seller_discount |string |0.1 |商品卖家优惠的退款金额。 |
   ^^^^shipping_fee_platform_discount |string |0.1 |运费平台优惠的退款金额。 |
   ^^^^shipping_fee_seller_discount |string |0.1 |运费卖家优惠的退款金额。 |
   ^^^shipping_fee |object | |退货配送费金额，以 `refund_amount.currency` 指定的货币计价。 |
   ^^^^seller_paid_return_shipping_fee_amount |string |0.1 |卖家支付的退货运费金额。 |
   ^^^^buyer_paid_return_shipping_fee_amount |string |0.1 |买家支付的退货运费金额。 |
   ^^^^platform_paid_return_shipping_fee_amount |string |0.1 |平台支付的退货运费金额。 |
   ^^^buyer_keep_item |bool |true |表示买家是否可保留商品。对于换货请求，此字段返回 `true`；对于其他退货类型，此字段被省略。 |
   ^^^return_shipping_document_type |string |SHIPPING_LABEL |买家选择的退货配送单据类型。
   Available values:
* `SHIPPING_LABEL`
* `QR_CODE` - 带框二维码
* `QR_CODE_NBNL` - 无盒无标签的二维码 |
   ^^^return_method |string |PLATFORM_SHIPPED |退货方式:
* `SELLER_SHIPPED`: 卖家提供退货配送服务。
* `BUYER_SHIPPED`: 买家提供退货配送服务。
* `PLATFORM_SHIPPED`: TikTok Shop 提供退货配送服务。 |
   ^^^is_combined_return |bool |false |如果买家要求将多个退货合并为一个退货包裹，此字段将返回 true。 |
   ^^^combined_return_id |string |4035309948547073951 |如果 `is_combined_return` 为 `true`，此字段将返回与合并退货关联的 `combined_return_id`。 |
   ^^^seller_proposed_return_type |string |PARTIAL_REFUND |卖家提出的退货方式:
* `PARTIAL_REFUND` |
   ^^^partial_refund_amount |object | |部分退款明细。 |
   ^^^^partial_refund_total |string |10 |卖家提供的部分退款金额。
   说明: 仅卖家提出的部分退款会返回此字段。 |
   ^^^^currency |string |IDR |部分退款货币 |
   ^^^buyer_rejected_partial_refund |bool |false |仅当卖家发起部分退款时才返回此字段。
   Available values:
* `TRUE`: 买家拒绝卖家的部分退款提议。
* `FALSE`: 买家接受卖家的部分退款提议，或等待买家响应。 |
   ^^^return_warehouse_address |object | |卖家提供的退货仓库地址详情。 |
   ^^^^full_address |string |1199 Coleman Ave San Jose, CA 95110 |完整的退货仓库地址。 |
   ^^^exchange_order_lines |[]object | |忽略此字段. 目前尚不支持。 |
   ^^^^order_line_id |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^sku_id |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^sku_name |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^product_name |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^seller_sku_name |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^product_image |object | |忽略此字段. 目前尚不支持。 |
   ^^^^^url |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^^width |int |0 |忽略此字段. 目前尚不支持。 |
   ^^^^^height |int |0 |忽略此字段. 目前尚不支持。 |
   ^^^^price_detail |object | |忽略此字段. 目前尚不支持。 |
   ^^^^^currency |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^^refund_total |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^^refund_subtotal |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^^refund_shipping_fee |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^^^refund_tax |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^reshipment_order_id |string |0 |忽略此字段. 目前尚不支持。 |
   ^^^is_quick_refund |bool |false |如果退货命中极速退款策略，卖家将无法拒收已收到的包裹 |
   ^^^return_sub_line_items |[]object | |已废弃. 请勿使用此字段。 |
   ^^^^return_sub_line_item_id |string |4035227657962164812 |退货子订单行 ID。 |
   ^^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^^sub_order_line_item_id |string |576473917261451852 |子订单行 ID。 |
   ^^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^product_image |object | |商品图片信息。 |
   ^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^width |int |200 |商品图片宽度。单位：像素（px）。 |
   ^^^^^height |int |200 |商品图片高度。单位：像素（px）。 |
   ^^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^^seller_sku |string |PUTIH 1 TALI |卖家定义的 SKU 名称。 |
   ^^^^refund_amount |object | |退款金额明细。 |
   ^^^^^currency |string |USD |支付货币。 |
   ^^^^^refund_total |string |1.23 |退还买家的总金额。 |
   ^^^^^refund_subtotal |string |1 |退还买家的小计金额。 |
   ^^^^^refund_shipping_fee |string |0.2 |退还买家的配送费金额。 |
   ^^^^^refund_tax |string |0.03 |退还买家的税费金额。 |
   ^^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费开始生效。 |
   ^^^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^total_count |int |12345 |结果集总数，与分页无关。 |
   ^next_page_token |string |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |用于获取下一页/下一组结果。 |

# 响应示例
```json
{"code":0,"data":{"return_merchandise_authorizations":[{"id":"2894521704838895640","package_id":"2894521704838895645","aftersales_request_id":"4035318504086604101","status":"AWAITING_BUYER_RETURN","line_items":[{"return_line_item_id":"4035227657962164811","sub_return_line_item_id":"4035227657962164815","sku_id":"2729382476852921560","main_order_id":"577686530908261117","sku_return_request_id":"4035318504086604100"}],"sku_return_requests":[{"order_id":"577686530908261117","return_id":"4035318504086604100","return_type":"REFUND","return_status":"RETURN_OR_REFUND_REQUEST_PENDING","arbitration_status":"IN_PROGRESS","role":"BUYER","return_reason":"ecom_order_to_ship_canceled_reason_created_by_mistakes","return_reason_text":"Order created by mistake","seller_next_action_response":[{"action":"SELLER_RESPOND_REFUND","deadline":1690554680}],"shipment_type":"PLATFORM","handover_method":"DROP_OFF","return_tracking_number":"213456789098765433456","return_provider_name":"J\u0026T Express","return_provider_id":"TH27014E9R5Q4G","pre_return_id":"4035310341095393452","next_return_id":"4035310341095393463","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"},"return_line_items":[{"return_line_item_id":"4035227657962164811","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"},"return_sub_line_items":[{"return_sub_line_item_id":"4035227657962164812","return_line_item_id":"4035227657962164811","sub_order_line_item_id":"576473917261451852","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"}}]}],"create_time":1690451136,"update_time":1690453136,"discount":{"product_platform_discount":"0.1","product_seller_discount":"0.1","shipping_fee_platform_discount":"0.1","shipping_fee_seller_discount":"0.1"},"shipping_fee":{"seller_paid_return_shipping_fee_amount":"0.1","buyer_paid_return_shipping_fee_amount":"0.1","platform_paid_return_shipping_fee_amount":"0.1"},"buyer_keep_item":true,"return_shipping_document_type":"SHIPPING_LABEL","return_method":"PLATFORM_SHIPPED","is_combined_return":false,"combined_return_id":"4035309948547073951","seller_proposed_return_type":"PARTIAL_REFUND","partial_refund_amount":{"partial_refund_total":"10","currency":"IDR"},"buyer_rejected_partial_refund":false,"return_warehouse_address":{"full_address":"1199 Coleman Ave San Jose, CA 95110"},"exchange_order_lines":[{"order_line_id":"0","sku_id":"0","sku_name":"0","product_name":"0","seller_sku_name":"0","product_image":{"url":"0","width":0,"height":0},"price_detail":{"currency":"0","refund_total":"0","refund_subtotal":"0","refund_shipping_fee":"0","refund_tax":"0"}}],"reshipment_order_id":"0","is_quick_refund":false,"return_sub_line_items":[{"return_sub_line_item_id":"4035227657962164812","return_line_item_id":"4035227657962164811","sub_order_line_item_id":"576473917261451852","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"}}]}]}],"total_count":12345,"next_page_token":"aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查参数类型和格式是否正确。 |
| 25020005 | 无权处理此订单 |
| 25020008 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

