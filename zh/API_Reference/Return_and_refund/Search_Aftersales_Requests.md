# 搜索售后请求

# Path: /return_refund/202603/aftersales/search
# Method: [POST]
# 功能描述
搜索已授权店铺的售后请求。您可以通过售后请求、buyer 或主订单 ID、售后请求状态、退货类型以及创建或更新时间进行筛选。使用 `whitelisted_data_fields` 在每个结果中包含行项目、SKU 退货请求或 return merchandise authorization。

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
| locale | string | N | en-US | 用于显示目的的 BCP-47 locale 代码。默认值：`en` |
| 支持的 locale 代码列表请参考 [Locale codes](https://partner.tiktokshop.com/docv2/page/678e3a47bae28f030a8c7523)。 |  |  |  |  |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| whitelisted_data_fields | []string | N | ["LINE_ITEMS", "SKU_RETURN_REQUESTS", "RETURN_MERCHANDISE_AUTHORIZATIONS"] | 控制每个售后请求包含哪些附加字段。 |
| 可能的值： |  |  |  |  |

* `LINE_ITEMS`：包含 `line_items`。
* `SKU_RETURN_REQUESTS`：包含 `sku_return_requests`。
* `RETURN_MERCHANDISE_AUTHORIZATIONS`：包含 `return_merchandise_authorizations`。 |
   filters |object |N | |用于缩小结果集的筛选条件。 |
   ^aftersales_request_ids |[]string |N |["4035318504086604101"] |将结果限制为指定的售后请求。每个 ID 必须是适合有符号 64 位整数的十进制整数字符串。 |
   ^aftersales_request_statuses |[]string |N |["PENDING_REQUEST_REVIEW"] |将结果限制为指定的售后请求状态。
   可能的值：
* `INIT`
* `PENDING_REQUEST_REVIEW`
* `REQUEST_REVIEW_COMPLETED` |
   ^return_types |[]string |N |["REFUND", "RETURN_AND_REFUND"] |将结果限制为包含至少一个具有给定类型的 SKU 退货请求的售后请求数据。
   可能的值：
* `REFUND`
* `RETURN_AND_REFUND`
* `REPLACEMENT`
* `EXCHANGE` |
   ^main_order_ids |[]string |N |["577686530908261117"] |将结果限制为包含至少一个指定主（正向）订单的 SKU 退货请求的售后请求。每个主订单 ID 必须是适合有符号 64 位整数的十进制整数字符串。 |
   ^buyer_ids |[]string |N |["7493996903972308733"] |将结果限制为包含至少一个指定 buyer 的 SKU 退货请求的售后请求。每个 buyer ID 必须是适合有符号 64 位整数的十进制整数字符串。 |
   ^time |object |N | |基于时间的筛选条件。 |
   ^^create_time |object |N | |基于创建时间筛选。 |
   ^^^min_unix_time_inclusive |int |N |1774486592 |包含下界（Unix 秒）。 |
   ^^^max_unix_time_exclusive |int |N |1774572992 |排除上界（Unix 秒）。 |
   ^^update_time |object |N | |基于最后更新时间筛选。 |
   ^^^min_unix_time_inclusive |int |N |1774486592 |包含下界（Unix 秒）。 |
   ^^^max_unix_time_exclusive |int |N |1774572992 |排除上界（Unix 秒）。 |
   sort |object |N | |结果集的排序条件。 |
   ^sort_field |string |N |CREATE_TIME |用于排序的字段名称。
   可能的值：
* `CREATE_TIME`
* `UPDATE_TIME`
   |
   ^sort_order |string |N |ASC |排序方向。
   可能的值：
* `ASC`
* `DESC` |
   pagination |object |N | |分页配置。 |
   ^page_size |int |N |100 |每页返回的记录数。最小值：1。最大值：100。 |
   ^page_token |string |N |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |标识要获取的页面。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202603/aftersales/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

**Body**
```json
{"whitelisted_data_fields":["LINE_ITEMS","SKU_RETURN_REQUESTS","RETURN_MERCHANDISE_AUTHORIZATIONS"],"filters":{"aftersales_request_ids":["4035318504086604101"],"aftersales_request_statuses":["PENDING_REQUEST_REVIEW"],"return_types":["REFUND","RETURN_AND_REFUND"],"main_order_ids":["577686530908261117"],"buyer_ids":["7493996903972308733"],"time":{"create_time":{"min_unix_time_inclusive":1774486592,"max_unix_time_exclusive":1774572992},"update_time":{"min_unix_time_inclusive":1774486592,"max_unix_time_exclusive":1774572992}}},"sort":{"sort_field":"CREATE_TIME","sort_order":"ASC"},"pagination":{"page_size":100,"page_token":"aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA=="}}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^aftersales_requests | []object |  | 匹配筛选条件的售后请求列表。当没有匹配的售后请求时，此字段将被省略。 |
| ^^id | string | 4035318504086604101 | 此售后请求的唯一标识符。 |
| ^^line_items | []object |  | 与此售后请求关联的商品列表。仅当 `LINE_ITEMS` 包含在 `whitelisted_data_fields` 中且有匹配的商品数据可用时，才返回此字段。 |
| ^^^return_line_item_id | string | 4035227657962164811 | 此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于原始父商品捆绑的 id。 |
| ^^^sub_return_line_item_id | string | 4035227657962164815 | 此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于当前被退货的子商品的 id。 |
| ^^^sku_id | string | 2729382476852921560 | 与此商品关联的 SKU 标识符（用于商品详情）。 |
| ^^^main_order_id | string | 577686530908261117 | 关联的主（正向）订单的标识符。 |
| ^^^sku_return_request_id | string | 4035318504086604100 | 关联的 SKU 级子退货请求的标识符。 |
| ^^status | string | PENDING_REQUEST_REVIEW | 此售后请求的当前状态。 |
| 可能的值： |  |  |  |

* `INIT`
* `PENDING_REQUEST_REVIEW`
* `REQUEST_REVIEW_COMPLETED` |
   ^^sku_return_requests |[]object | |与此售后请求关联的 SKU 级子退货请求，也称为逆向订单或退货请求。仅当 `SKU_RETURN_REQUESTS` 包含在 `whitelisted_data_fields` 中且有匹配数据可用时，才返回此字段。 |
   ^^^order_id |string |577686530908261117 |与此 SKU 退货请求关联的 TikTok Shop 主订单 ID。 |
   ^^^return_id |string |4035318504086604100 |特定退货的标识符。 |
   ^^^return_type |string |REFUND |退货类型。
   可用值：
* `REFUND`：Seller 将发放仅退款。Buyer 无需将商品寄回给 seller。
* `RETURN_AND_REFUND`：Buyer 需要将商品寄回给 seller。Seller 需要审核退回商品的状况后才能向 buyer 发放退款。
* `REPLACEMENT`：Buyer 要求 seller 换货。
* `EXCHANGE`：Buyer 要求 seller 换货。 |
   ^^^return_status |string |RETURN_OR_REFUND_REQUEST_PENDING |退货状态。
   可用值：
* `RETURN_OR_REFUND_REQUEST_PENDING`：Buyer 已发起退货或退款请求。请求等待 seller 或平台审核。
* `REFUND_OR_RETURN_REQUEST_REJECT`：退货或退款请求被拒绝。
* `AWAITING_BUYER_SHIP`：退货请求已获批准。Seller 等待 buyer 将批准的商品寄回。如果 buyer 在截止日期前未寄出商品，平台将关闭请求。
* `BUYER_SHIPPED_ITEM`：Buyer 已将批准的商品寄回给 seller。
* `REJECT_RECEIVE_PACKAGE`：Seller 检查了退回商品并拒绝了退货包裹。
* `RETURN_OR_REFUND_REQUEST_SUCCESS`：退货/退款请求已获批准。Buyer 将获得退款。
* `RETURN_OR_REFUND_REQUEST_CANCEL`：请求已被 buyer 或系统取消。
* `RETURN_OR_REFUND_REQUEST_COMPLETE`：退货/退款已成功处理。Buyer 已收到退款。
* `REPLACEMENT_REQUEST_PENDING`：Buyer 已发起换货请求。请求等待 seller 审核。
* `REPLACEMENT_REQUEST_REJECT`：Seller 拒绝了 buyer 的换货请求。
* `REPLACEMENT_REQUEST_REFUND_SUCCESS`：由于库存不足，buyer 的换货请求已通过退款解决。
* `REPLACEMENT_REQUEST_CANCEL`：Buyer 取消了换货请求。
* `REPLACEMENT_REQUEST_COMPLETE`：Seller 已批准 buyer 的换货请求，平台将生成新订单供 seller 履行。
* `AWAITING_BUYER_RESPONSE`：Seller 向 buyer 提供另一种退货类型，等待 buyer 响应。Seller 提出的退货类型可检查 `seller_proposed_return_type`。
* `EXCHANGE_REQUEST_PENDING`：Buyer 已发起换货请求。请求等待 seller 审核。
* `EXCHANGE_REQUEST_REFUND_SUCCESS`：由于库存不足，buyer 的换货请求已通过退款解决。
* `EXCHANGE_REQUEST_CANCEL`：Buyer 取消了换货请求。
* `EXCHANGE_REQUEST_COMPLETE`：Seller 已批准 buyer 的换货请求，平台将生成新订单供 seller 履行。 |
   ^^^arbitration_status |string |IN_PROGRESS |仲裁状态。
   可用值：
* `IN_PROGRESS`：TikTok Shop 平台运营方正在处理仲裁，可能会要求 seller 提供更多信息。
* `SUPPORT_BUYER`：平台运营方支持 buyer。
* `SUPPORT_SELLER`：平台运营方支持 seller。
* `CLOSED`：仲裁已关闭。 |
   ^^^role |string |BUYER |退货发起方角色。
   可用值：
* `BUYER`
* `SELLER`
* `OPERATOR`：TikTok Shop 平台运营方。
* `SYSTEM`：TikTok Shop 系统。
   请参阅"API 概览"了解更多关于角色的信息。 |
   ^^^return_reason |string |ecom_order_to_ship_canceled_reason_created_by_mistakes |退货的机器可读原因代码。使用 `return_reason_text` 获取本地化显示文本。 |
   ^^^return_reason_text |string |Order created by mistake |退货原因，本地化文本。
   您可以使用 locale 请求参数更改语言。 |
   ^^^seller_next_action_response |[]object | |Seller 的下一步操作和截止日期。 |
   ^^^^action |string |SELLER_RESPOND_REFUND |Seller 的下一步操作。
   可用值：
* `SELLER_RESPOND_REFUND`
* `SELLER_RESPOND_RETURN`
* `SELLER_RESPOND_RECEIVE_PACKAGE`
* `SELLER_RESPOND_REPLACEMENT` |
   ^^^^deadline |int |1690554680 |Seller 执行指定操作的截止日期，为 Unix 时间戳（秒）。 |
   ^^^shipment_type |string |PLATFORM |Buyer 选择的将商品寄回给 seller 的物流方式。
   可用值：
* `PLATFORM`：Buyer 使用 TikTok Shop 的 shipping 服务。参见 `handover_method` 了解 buyer 使用 `DROP_OFF` 还是 `PICKUP`。
* `BUYER_ARRANGE`：Buyer 自行安排退货物流。 |
   ^^^handover_method |string |DROP_OFF |Buyer 在使用平台 shipping 服务退货时选择的交接方式。
* `DROP_OFF`：buyer 将商品送到快递收集点
* `PICKUP`：buyer 预约快递提供的上门取件服务。 |
   ^^^return_tracking_number |string |213456789098765433456 |Buyer 退货时包裹的 tracking number。 |
   ^^^return_provider_name |string |J&T Express |Buyer 退货时包裹的物流服务商名称。 |
   ^^^return_provider_id |string |TH27014E9R5Q4G |Buyer 退货时包裹的物流服务商 ID。 |
   ^^^pre_return_id |string |4035310341095393452 |当前退货订单编辑自的前一个退货 ID。 |
   ^^^next_return_id |string |4035310341095393463 |当前退货订单编辑至的下一个退货 ID。 |
   ^^^refund_amount |object | |退款金额详情。 |
   ^^^^currency |string |USD |付款币种。 |
   ^^^^refund_total |string |1.23 |退还给 buyer 的总退款金额。 |
   ^^^^refund_subtotal |string |1 |退还给 buyer 的小计退款金额。 |
   ^^^^refund_shipping_fee |string |0.2 |退还给 buyer 的运费退款金额。 |
   ^^^^refund_tax |string |0.03 |退还给 buyer 的税额退款金额。 |
   ^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。 |
   ^^^^buyer_service_fee |string |0.1 |Buyer 服务费。 |
   ^^^return_line_items |[]object | |退货订单行项目。 |
   ^^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^^sku_id |string |2729382476852921560 |SKU ID。 |
   ^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^product_image |object | |商品图片信息。 |
   ^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^width |int |200 |商品图片宽度。单位：像素（px）。 |
   ^^^^^height |int |200 |商品图片高度。单位：像素（px）。 |
   ^^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^^seller_sku |string |PUTIH 1 TALI |Seller 定义的 SKU 名称。 |
   ^^^^refund_amount |object | |退款金额详情。 |
   ^^^^^currency |string |USD |付款币种。 |
   ^^^^^refund_total |string |1.23 |退还给 buyer 的总退款金额。 |
   ^^^^^refund_subtotal |string |1 |退还给 buyer 的小计退款金额。 |
   ^^^^^refund_shipping_fee |string |0.2 |退还给 buyer 的运费退款金额。 |
   ^^^^^refund_tax |string |0.03 |退还给 buyer 的税额退款金额。 |
   ^^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。 |
   ^^^^^buyer_service_fee |string |0.1 |Buyer 服务费。 |
   ^^^^return_sub_line_items |[]object | |退货子订单行项目。
   子项目代表属于 seller 定义的"虚拟捆绑"的 SKU。sub_items 将包含虚拟捆绑中每个商品的所有相关信息。 |
   ^^^^^return_sub_line_item_id |string |4035227657962164812 |退货子订单行 ID。 |
   ^^^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^^^sub_order_line_item_id |string |576473917261451852 |子订单行 ID。 |
   ^^^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^^^sku_id |string |2729382476852921560 |SKU ID。 |
   ^^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^^product_image |object | |商品图片信息。 |
   ^^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^^width |int |200 |商品图片宽度。单位：像素（px）。 |
   ^^^^^^height |int |200 |商品图片高度。单位：像素（px）。 |
   ^^^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^^^seller_sku |string |PUTIH 1 TALI |Seller 定义的 SKU 名称。 |
   ^^^^^refund_amount |object | |退款金额详情。 |
   ^^^^^^currency |string |USD |付款币种。 |
   ^^^^^^refund_total |string |1.23 |退还给 buyer 的总退款金额。 |
   ^^^^^^refund_subtotal |string |1 |退还给 buyer 的小计退款金额。 |
   ^^^^^^refund_shipping_fee |string |0.2 |退还给 buyer 的运费退款金额。 |
   ^^^^^^refund_tax |string |0.03 |退还给 buyer 的税额退款金额。 |
   ^^^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。 |
   ^^^^^^buyer_service_fee |string |0.1 |Buyer 服务费。 |
   ^^^create_time |int |1690451136 |退货创建时间，Unix 时间戳（秒）。 |
   ^^^update_time |int |1690453136 |退货最后更新时间，Unix 时间戳（秒）。 |
   ^^^discount |object | |折扣退款金额，以 `refund_amount.currency` 指定的币种计价。 |
   ^^^^product_platform_discount |string |0.1 |平台折扣的退款金额。 |
   ^^^^product_seller_discount |string |0.1 |商品 seller 折扣的退款金额。 |
   ^^^^shipping_fee_platform_discount |string |0.1 |运费平台折扣的退款金额。 |
   ^^^^shipping_fee_seller_discount |string |0.1 |运费 seller 折扣的退款金额。 |
   ^^^shipping_fee |object | |退货物流费用金额，以 `refund_amount.currency` 指定的币种计价。 |
   ^^^^seller_paid_return_shipping_fee_amount |string |0.1 |Seller 承担的退货物流费用金额。 |
  3 ^^^^buyer_paid_return_shipping_fee_amount |string |0.1 |Buyer 承担的退货物流费用金额。 |
   ^^^^platform_paid_return_shipping_fee_amount |string |0.1 |平台承担的退货物流费用金额。 |
   ^^^buyer_keep_item |bool |true |指示 buyer 是否可以保留商品。对于换货请求，此字段返回 `true`，其他退货类型则省略此字段。 |
   ^^^return_shipping_document_type |string |SHIPPING_LABEL |Buyer 选择的退货物流单据类型。
   可用值：
* `SHIPPING_LABEL`
* `QR_CODE` - 带箱的二维码
* `QR_CODE_NBNL` - 无箱无标的二维码 |
   ^^^return_method |string |PLATFORM_SHIPPED |退货方式：
* `SELLER_SHIPPED`：Seller 提供退货物流服务。
* `BUYER_SHIPPED`：Buyer 自行安排退货物流。
* `PLATFORM_SHIPPED`：TikTok Shop 提供退货物流服务。 |
   ^^^is_combined_return |bool |false |如果 buyer 要求将多个退货合并为一个退货包裹，此字段返回 true。 |
   ^^^combined_return_id |string |4035309948547073951 |如果 `is_combined_return` 为 `true`，此字段返回与合并退货关联的 `combined_return_id`。 |
   ^^^seller_proposed_return_type |string |PARTIAL_REFUND |Seller 提出的退货类型：
* `PARTIAL_REFUND` |
   ^^^partial_refund_amount |object | |部分退款详情。 |
   ^^^^partial_refund_total |string |10 |Seller 提供的部分退款金额。
   注意：仅 seller 发起的部分退款才返回此字段。 |
   ^^^^currency |string |IDR |部分退款币种 |
   ^^^buyer_rejected_partial_refund |bool |true |仅在 seller 发起部分退款时返回此字段。
   可用值：
* `TRUE`：Buyer 拒绝了 seller 的部分退款提议。
* `FALSE`：Buyer 接受了 seller 的部分退款提议或等待 buyer 响应。 |
   ^^^return_warehouse_address |object | |Seller 提供的退货仓库地址详情。 |
   ^^^^full_address |string |1199 Coleman Ave San Jose, CA 95110 |完整的退货仓库地址。 |
   ^^^exchange_order_lines |[]object | |请忽略此字段。尚未支持。 |
   ^^^^order_line_id |string |0 |请忽略此字段。尚未支持。 |
   ^^^^sku_id |string |0 |请忽略此字段。尚未支持。 |
   ^^^^sku_name |string |0 |请忽略此字段。尚未支持。 |
   ^^^^product_name |string |0 |请忽略此字段。尚未支持。 |
   ^^^^seller_sku_name |string |0 |请忽略此字段。尚未支持。 |
   ^^^^product_image |object | |请忽略此字段。尚未支持。 |
   ^^^^^url |string |0 |请忽略此字段。尚未支持。 |
   ^^^^^width |int |0 |请忽略此字段。尚未支持。 |
   ^^^^^height |int |0 |请忽略此字段。尚未支持。 |
   ^^^^price_detail |object | |请忽略此字段。尚未支持。 |
   ^^^^^currency |string |0 |请忽略此字段。尚未支持。 |
   ^^^^^refund_total |string |0 |请忽略此字段。尚未支持。 |
   ^^^^^refund_subtotal |string |0 |请忽略此字段。尚未支持。 |
   ^^^^^refund_shipping_fee |string |0 |请忽略此字段。尚未支持。 |
   ^^^^^refund_tax |string |0 |请忽略此字段。尚未支持。 |
   ^^^reshipment_order_id |string |0 |请忽略此字段。尚未支持。 |
   ^^^is_quick_refund |bool |false |如果退货触发了快速退款策略，seller 无法拒绝收货包裹 |
   ^^^return_sub_line_items |[]object | |已弃用。请勿使用此字段。 |
   ^^^^return_sub_line_item_id |string |4035227657962164812 |退货子订单行 ID。 |
   ^^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^^sub_order_line_item_id |string |576473917261451852 |子订单行 ID。 |
   ^^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^^sku_id |string |2729382476852921560 |SKU ID。 |
   ^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^product_image |object | |商品图片信息。 |
   ^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^width |int |200 |商品图片宽度。单位：像素（px）。 |
   ^^^^^height |int |200 |商品图片高度。单位：像素（px）。 |
   ^^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^^seller_sku |string |PUTIH 1 TALI |Seller 定义的 SKU 名称。 |
   ^^^^refund_amount |object | |退款金额详情。 |
   ^^^^^currency |string |USD |付款币种。 |
   ^^^^^refund_total |string |1.23 |退还给 buyer 的总退款金额。 |
   ^^^^^refund_subtotal |string |1 |退还给 buyer 的小计退款金额。 |
   ^^^^^refund_shipping_fee |string |0.2 |退还给 buyer 的运费退款金额。 |
   ^^^^^refund_tax |string |0.03 |退还给 buyer 的税额退款金额。 |
   ^^^^^retail_delivery_fee |string |0.1 |根据美国科罗拉多州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。 |
   ^^^^^buyer_service_fee |string |0.1 |Buyer 服务费。 |
   ^^return_merchandise_authorizations |[]object | |与此售后请求关联的 return merchandise authorization（RMA）记录。仅当 `RETURN_MERCHANDISE_AUTHORIZATIONS` 包含在 `whitelisted_data_fields` 中且有匹配的 RMA 数据可用时，才返回此字段。 |
   ^^^id |string |2894521704838895640 |此 RMA 数据的唯一标识符。 |
   ^^^package_id |string |2894521704838895645 |关联的物理退货包裹的标识符。 |
   ^^^aftersales_request_id |string |4035318504086604101 |父售后请求的标识符。 |
   ^^^status |string |AWAITING_BUYER_RETURN |此 RMA 数据的当前状态。
   可能的值：
* `INIT`
* `AWAITING_BUYER_RETURN`
* `RETURN_IN_TRANSIT`
* `PENDING_PACKAGE_REVIEW`
* `PACKAGE_REVIEW_COMPLETED` |
   ^^^line_items |[]object | |此退货包裹中预期的商品列表。 |
   ^^^^return_line_item_id |string |4035227657962164811 |此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于原始父商品捆绑的 id。 |
   ^^^^sub_return_line_item_id |string |4035227657962164815 |此商品在退货中的唯一标识符。在虚拟捆绑商品的情况下，这对应于当前被退货的子商品的 id。 |
   ^^^^sku_id |string |2729382476852921560 |与此商品关联的 SKU 标识符（用于商品详情）。 |
   ^^^^main_order_id |string |577686530908261117 |关联的主（正向）订单的标识符。 |
   ^^^^sku_return_request_id |string |4035318504086604100 |关联的 SKU 级子退货请求的标识符。 |
   ^total_count |int |12345 |总结果集大小，与分页无关。 |
   ^next_page_token |string |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |用于获取下一页/下一组结果。 |

# 响应示例
```json
{"code":0,"data":{"aftersales_requests":[{"id":"4035318504086604101","line_items":[{"return_line_item_id":"4035227657962164811","sub_return_line_item_id":"4035227657962164815","sku_id":"2729382476852921560","main_order_id":"577686530908261117","sku_return_request_id":"4035318504086604100"}],"status":"PENDING_REQUEST_REVIEW","sku_return_requests":[{"order_id":"577686530908261117","return_id":"4035318504086604100","return_type":"REFUND","return_status":"RETURN_OR_REFUND_REQUEST_PENDING","arbitration_status":"IN_PROGRESS","role":"BUYER","return_reason":"ecom_order_to_ship_canceled_reason_created_by_mistakes","return_reason_text":"Order created by mistake","seller_next_action_response":[{"action":"SELLER_RESPOND_REFUND","deadline":1690554680}],"shipment_type":"PLATFORM","handover_method":"DROP_OFF","return_tracking_number":"213456789098765433456","return_provider_name":"J\u0026T Express","return_provider_id":"TH27014E9R5Q4G","pre_return_id":"4035310341095393452","next_return_id":"4035310341095393463","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"},"return_line_items":[{"return_line_item_id":"4035227657962164811","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"},"return_sub_line_items":[{"return_sub_line_item_id":"4035227657962164812","return_line_item_id":"4035227657962164811","sub_order_line_item_id":"576473917261451852","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"}}]}],"create_time":1690451136,"update_time":1690453136,"discount":{"product_platform_discount":"0.1","product_seller_discount":"0.1","shipping_fee_platform_discount":"0.1","shipping_fee_seller_discount":"0.1"},"shipping_fee":{"seller_paid_return_shipping_fee_amount":"0.1","buyer_paid_return_shipping_fee_amount":"0.1","platform_paid_return_shipping_fee_amount":"0.1"},"buyer_keep_item":true,"return_shipping_document_type":"SHIPPING_LABEL","return_method":"PLATFORM_SHIPPED","is_combined_return":false,"combined_return_id":"4035309948547073951","seller_proposed_return_type":"PARTIAL_REFUND","partial_refund_amount":{"partial_refund_total":"10","currency":"IDR"},"buyer_rejected_partial_refund":true,"return_warehouse_address":{"full_address":"1199 Coleman Ave San Jose, CA 95110"},"exchange_order_lines":[{"order_line_id":"0","sku_id":"0","sku_name":"0","product_name":"0","seller_sku_name":"0","product_image":{"url":"0","width":0,"height":0},"price_detail":{"currency":"0","refund_total":"0","refund_subtotal":"0","refund_shipping_fee":"0","refund_tax":"0"}}],"reshipment_order_id":"0","is_quick_refund":false,"return_sub_line_items":[{"return_sub_line_item_id":"4035227657962164812","return_line_item_id":"4035227657962164811","sub_order_line_item_id":"576473917261451852","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"}}]}],"return_merchandise_authorizations":[{"id":"2894521704838895640","package_id":"2894521704838895645","aftersales_request_id":"4035318504086604101","status":"AWAITING_BUYER_RETURN","line_items":[{"return_line_item_id":"4035227657962164811","sub_return_line_item_id":"4035227657962164815","sku_id":"2729382476852921560","main_order_id":"577686530908261117","sku_return_request_id":"4035318504086604100"}]}]}],"total_count":12345,"next_page_token":"aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查您是否具有正确的参数类型和格式。 |
| 25020005 | No permission to process this order |
| 25020008 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

