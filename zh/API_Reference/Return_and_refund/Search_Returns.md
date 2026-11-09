# 搜索退货

# 路径：/return_refund/202602/returns/search
# 方法：[POST]
# 功能描述
使用此 API 按退货 ID、订单 ID、买家、退货类型、退货状态、仲裁状态或创建/更新时间范围搜索退货。响应为分页。要获取下一页，请将上一次的 `next_page_token` 作为 `page_token` 传入，并保持所有其它筛选条件和排序不变。

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
| sort_field | string | N | create_time | 返回的结果将按指定字段排序。 |
| **Default**: `create_time` |  |  |  |  |
| 可能的值： |  |  |  |  |

* `create_time`
* `update_time`

使用 `sort_order` 参数指定返回结果的排序顺序。 |
sort_order |string |N |ASC |`sort_field` 参数的排序顺序。**默认值**: `ASC`
可能的值：

* `ASC`: Ascending order
* `DESC`: Descending order |
   page_size |string |N |10 |每页返回的结果数量。 **Default**: 10. 有效范围： [10-50]。 |
   page_token |string |N |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| return_ids | []string | N | ["4035318504086604100"] | 退货 ID 列表。每个 ID 必须是能装入有符号 64 位整数的十进制整数字符串。 |
| order_ids | []string | N | ["577686530908261117"] | TikTok Shop 订单 ID 列表。每个 ID 必须是能装入有符号 64 位整数的十进制整数字符串。 |
| buyer_user_ids | []string | N | ["7493996903972308733"] | TikTok Shop 买家用户 ID 列表。每个 ID 必须是能装入有符号 64 位整数的十进制整数字符串。 |
| return_types | []string | N | ["REFUND"] | 退货类型列表。 |
| Available values: |  |  |  |  |

* `REFUND`
* `RETURN_AND_REFUND`
* `REPLACEMENT`
* `EXCHANGE` |
   return_status |[]string |N |["RETURN_OR_REFUND_REQUEST_PENDING"] |退货状态列表。
   Available values:
* `RETURN_OR_REFUND_REQUEST_PENDING`: 买家已发起退货或退款请求. 该请求待卖家或系统审核。
* `REFUND_OR_RETURN_REQUEST_REJECT`：退货或退款申请被拒绝。
* `AWAITING_BUYER_SHIP`：退货申请已批准。卖家正等待买家将已批准的商品寄回。如果买家未在截止日期前将商品寄给卖家，平台将关闭该申请。
* `BUYER_SHIPPED_ITEM`：买家已将已批准的商品寄给卖家。
* `REJECT_RECEIVE_PACKAGE`: 卖家已检查退回商品并拒绝了退货申请。
* `RETURN_OR_REFUND_REQUEST_SUCCESS`: 退货/退款申请成功。买家将获得退款。
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
   seller_proposed_return_type |[]string |N |["PARTIAL_REFUND"] |卖家提出的退货类型列表。
   Available values:
* `PARTIAL_REFUND` |
   create_time_ge |int |N |1690340825 |筛选退货，仅显示在指定日期和时间或之后创建的退货。Unix 时间戳。

Note:
`create_time_ge` 与 `create_time_le` 共同构成创建时间筛选条件。

* 如果填写了 `create_time_ge` 但 `create_time_le` 为空，`create_time_le` 将默认为当前时间。
* 如果填写了 `create_time_lt` 但 `create_time_ge` 为空，则 `create_time_ge` 默认取最早的店铺时间。 |
   arbitration_status |[]string |N |["IN_PROGRESS"] |仲裁状态列表。
   Available values:
* `IN_PROGRESS`: TikTok Shop 平台运营方正在处理仲裁. 平台可能会要求卖家提供额外信息。
* `SUPPORT_BUYER`: 平台运营方支持买家。
* `SUPPORT_SELLER`: 平台运营方支持卖家。
* `CLOSED`：仲裁已结束。 |
   update_time_ge |int |N |1690340825 |筛选退货，仅显示在指定日期和时间或之后更新的退货。Unix 时间戳。

Note:
`update_time_ge` 和 `update_time_le` 共同定义更新时间筛选条件。

* 如果填写了 `update_time_ge` 但 `update_time_le` 为空，`update_time_le` 将默认为当前时间。
* 如果填写了 `update_time_lt` 但 `update_time_ge` 为空，则 `update_time_ge` 将默认为最早的店铺时间。 |
   update_time_lt |int |N |1690340825 |筛选在指定时间之前更新的退货. 请提供以秒为单位的 Unix 时间戳。 |
   locale |string |N |en-US |用于显示退货的 BCP-47 语言区域代码，以逗号分隔. 默认值: `en`
   请参阅 [Locale codes](678e3a47bae28f030a8c7523) 获取支持的区域设置代码列表。 |
   create_time_lt |int |N |1690340825 |筛选在指定时间之前创建的退货. 请提供以秒为单位的 Unix 时间戳。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202602/returns/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&sort_field=create_time&sort_order=ASC&page_size=10&page_token=aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA==
```

**Body**
```json
{"return_ids":["4035318504086604100"],"order_ids":["577686530908261117"],"buyer_user_ids":["7493996903972308733"],"return_types":["REFUND"],"return_status":["RETURN_OR_REFUND_REQUEST_PENDING"],"seller_proposed_return_type":["PARTIAL_REFUND"],"create_time_ge":1690340825,"arbitration_status":["IN_PROGRESS"],"update_time_ge":1690340825,"update_time_lt":1690340825,"locale":"en-US","create_time_lt":1690340825}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^return_orders | []object |  | 当前页的退货列表。当当前页不含退货记录时，此字段省略。 |
| ^^order_id | string | 577686530908261117 | TikTok Shop 订单 ID。 |
| ^^return_id | string | 4035318504086604100 | 特定退货的标识符。 |
| ^^return_type | string | REFUND | Return type. |
| Available values: |  |  |  |

* `REFUND`: 卖家将不退货直接退款. 买家无需将商品寄回卖家。
* `RETURN_AND_REFUND`：买家需将商品寄回给卖家。卖家需先检查退回商品的状况，方可向买家退款。
* `REPLACEMENT`: 买家要求卖家更换商品。
* `EXCHANGE`: 买家要求卖家换货。 |
   ^^return_status |string |RETURN_OR_REFUND_REQUEST_PENDING |退货状态。
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
* `EXCHANGE_REQUEST_COMPLETE`: 卖家已批准买家的换货请求，平台将为卖家生成新订单以供履约。
   |
   ^^arbitration_status |string |IN_PROGRESS |仲裁状态。
   Available values:
* `IN_PROGRESS`: TikTok Shop 平台运营方正在处理仲裁并可能要求卖家提供额外信息。
* `SUPPORT_BUYER`: 平台运营方支持买家。
* `SUPPORT_SELLER`: 平台运营方支持卖家。
* `CLOSED`：仲裁已结束。 |
   ^^role |string |BUYER |退货发起角色。
   Available values:
* `BUYER`
* `SELLER`
* `OPERATOR` : TikTok Shop 平台运营方。
* `SYSTEM`: TikTok Shop 系统。
   请参阅 "API 概览" 以了解更多关于角色的信息。 |
   ^^return_reason |string |ecom_order_to_ship_canceled_reason_created_by_mistakes |退货的机器可读原因码。本地化展示文本请使用 `return_reason_text`。 |
   ^^return_reason_text |string |Order created by mistake |退货原因，以本地化文本表示。
   可以使用 locale 请求参数更改语言。 |
   ^^shipment_type |string |PLATFORM |买家选择的将商品退回卖家的配送方式。
   Available values:
* `PLATFORM`: 买家使用 TikTok Shop 的配送服务. 关于买家使用 `DROP_OFF` 还是 `PICKUP`, 请参阅 `handover_method`。
* `BUYER_ARRANGE`: 买家安排退货配送。 |
   ^^handover_method |string |DROP_OFF |买家使用平台的配送服务将商品退回给卖家时所选择使用的交接方式。
* `DROP_OFF`: 买家将把商品(s)送至快递点
* `PICKUP`: 买家正在预约承运商提供的上门取件服务。 |
   ^^return_tracking_number |string |213456789098765433456 |买家退货时包裹的物流单号。 |
   ^^return_provider_name |string |J&T Express |买家退货时包裹的承运商名称。 |
   ^^return_provider_id |string |TH27014E9R5Q4G |买家退回商品时的包裹服务商 ID。 |
   ^^pre_return_id |string |4035310341095393452 |当前退货订单编辑所依据的先前退货 ID。 |
   ^^next_return_id |string |4035310341095393463 |当前退货单编辑后指向的下一个退货 ID。 |
   ^^can_buyer_keep_item |bool |true |表示买家是否可保留商品。对于换货请求，此字段返回 `true`；对于其他退货类型，此字段被省略。 |
   ^^update_time |int |1690453136 |退货最后一次更新的时间，以秒为单位的 Unix 时间戳。 |
   ^^seller_next_action_response |[]object | |卖家的下一步操作和截止时间。 |
   ^^^action |string |SELLER_RESPOND_REFUND |卖家的下一步操作。
   Available values:
* `SELLER_RESPOND_REFUND`
* `SELLER_RESPOND_RETURN`
* `SELLER_RESPOND_RECEIVE_PACKAGE`
* `SELLER_RESPOND_REPLACEMENT` |
   ^^^deadline |int |1690554680 |卖家执行指定操作的截止时间，以秒为单位的 Unix 时间戳表示。 |
   ^^create_time |int |1690451136 |退货创建时间，以秒为单位的 Unix 时间戳。 |
   ^^return_line_items |[]object | |退货订单行项目。 |
   ^^^return_line_item_id |string |4035227657962164811 |退货订单行 ID。 |
   ^^^order_line_item_id |string |576473917261451851 |订单行 ID。 |
   ^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^product_name |string |(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs |商品名称。 |
   ^^^seller_sku |string |PUTIH 1 TALI |卖家定义的 SKU 名称。 |
   ^^^product_image |object | |商品图片信息。 |
   ^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^width |int |200 |商品图片宽度. 单位: 像素 (px)。 |
   ^^^^height |int |200 |商品图片高度. 单位: 像素 (px)。 |
   ^^^refund_amount |object | |退款金额详情。 |
   ^^^^currency |string |USD |支付货币。 |
   ^^^^refund_total |string |1.23 |向买家退款的总金额。 |
   ^^^^refund_subtotal |string |1 |向买家退款的小计金额。 |
   ^^^^refund_shipping_fee |string |0.2 |退还给买家的运费金额。 |
   ^^^^refund_tax |string |0.03 |退还给买家的退税金额。 |
   ^^^^retail_delivery_fee |string |0.1 |根据 US Colorado 州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。
   |
   ^^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^^^return_sub_line_items |[]object | |退房子订单行项目。这些项目表示属于卖家定义的"虚拟组合"的 SKU。此字段包含虚拟组合中每个项目的所有相关信息。 |
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
   ^^^^^retail_delivery_fee |string |0.1 |根据 US Colorado 州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。
   |
   ^^^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^^discount_amount |[]object | |折扣退款明细。 |
   ^^^currency |string |USD |折扣货币。 |
   ^^^product_seller_discount |string |0.1 |商品卖家优惠的退款金额。 |
   ^^^shipping_fee_platform_discount |string |0.1 |运费平台优惠的退款金额。 |
   ^^^shipping_fee_seller_discount |string |0.1 |运费卖家优惠的退款金额。 |
   ^^^product_platform_discount |string |0.1 |平台折扣的退款金额。 |
   ^^shipping_fee_amount |[]object | |退货配送费用明细。 |
   ^^^currency |string |USD |退货配送费货币。 |
   ^^^seller_paid_return_shipping_fee |string |0.1 |卖家支付的退货运费金额。 |
   ^^^platform_paid_return_shipping_fee |string |0.1 |平台支付的退货运费金额。 |
   ^^^buyer_paid_return_shipping_fee |string |0.1 |买家支付的退货运费金额。 |
   ^^refund_amount |object | |退还给买家的总退款金额。 |
   ^^^currency |string |USD |退款货币。 |
   ^^^refund_total |string |1.23 |退款总金额。 |
   ^^^refund_subtotal |string |1 |退款小计金额。即所有退回商品的总价。 |
   ^^^refund_shipping_fee |string |0.2 |配送费退款。 |
   ^^^refund_tax |string |0.03 |税费退款。 |
   ^^^retail_delivery_fee |string |0.1 |根据 US Colorado 州的合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。
   |
   ^^^buyer_service_fee |string |0.1 |买家服务费。 |
   ^^return_shipping_document_type |string |SHIPPING_LABEL |买家选择的退货配送单据类型。
   Available values:
* `SHIPPING_LABEL`
* `QR_CODE` - 带框二维码
* `QR_CODE_NBNL` - 无盒无标签的二维码 |
   ^^return_method |string |PLATFORM_SHIPPED |退货方式:
* `SELLER_SHIPPED`: 卖家提供退货配送服务。
* `BUYER_SHIPPED`: 买家提供退货配送服务。
* `PLATFORM_SHIPPED`: TikTok Shop 提供退货配送服务。 |
   ^^is_combined_return |bool |true |如果买家要求将多个退货合并为一个退货包裹，此字段将返回 true。 |
   ^^combined_return_id |string |4035309948547073951 |如果 `is_combined_return` 为 `true`，此字段将返回与合并退货关联的 `combined_return_id`。 |
   ^^seller_proposed_return_type |string |PARTIAL_REFUND |卖家提出的退货方式:
* `PARTIAL_REFUND` |
   ^^partial_refund |object | |部分退款明细。 |
   ^^^currency |string |IDR |部分退款货币 |
   ^^^amount |string |10 |卖家提出的部分退款金额。
   说明: 仅卖家提出的部分退款会返回此字段。 |
   ^^buyer_rejected_partial_refund |bool |true |仅当卖家发起部分退款时返回此字段。
   Available values:
* `TRUE`: 买家拒绝卖家的部分退款提议。
* `FALSE`: 买家接受卖家的部分退款提议，或等待买家响应。 |
   ^^return_warehouse_address |object | |卖家提供的退货仓库地址详情。 |
   ^^^full_address |string |1199 Coleman Ave San Jose, CA 95110 |完整的退货仓库地址。 |
   ^^is_quick_refund |bool |false |如果退货命中极速退款策略，卖家将无法拒收已收到的包裹 |
   ^total_count |int |100 |符合查询条件的退货数量。 |
   ^next_page_token |string |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |用于获取分页结果集下一页的不透明令牌。如果 `next_page_token` 非空，请在下一个请求的 `page_token` 参数中提供该值。如果 `next_page_token` 为空，则停止分页。 |

# 响应示例
```json
{"code":0,"data":{"return_orders":[{"order_id":"577686530908261117","return_id":"4035318504086604100","return_type":"REFUND","return_status":"RETURN_OR_REFUND_REQUEST_PENDING","arbitration_status":"IN_PROGRESS","role":"BUYER","return_reason":"ecom_order_to_ship_canceled_reason_created_by_mistakes","return_reason_text":"Order created by mistake","shipment_type":"PLATFORM","handover_method":"DROP_OFF","return_tracking_number":"213456789098765433456","return_provider_name":"J\u0026T Express","return_provider_id":"TH27014E9R5Q4G","pre_return_id":"4035310341095393452","next_return_id":"4035310341095393463","can_buyer_keep_item":true,"update_time":1690453136,"seller_next_action_response":[{"action":"SELLER_RESPOND_REFUND","deadline":1690554680}],"create_time":1690451136,"return_line_items":[{"return_line_item_id":"4035227657962164811","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"},"return_sub_line_items":[{"return_sub_line_item_id":"4035227657962164812","return_line_item_id":"4035227657962164811","sub_order_line_item_id":"576473917261451852","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"(SP) [PROMO BUNDLING] NICE Tissue Facial 180s x 5 pcs","seller_sku":"PUTIH 1 TALI","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"}}]}],"discount_amount":[{"currency":"USD","product_seller_discount":"0.1","shipping_fee_platform_discount":"0.1","shipping_fee_seller_discount":"0.1","product_platform_discount":"0.1"}],"shipping_fee_amount":[{"currency":"USD","seller_paid_return_shipping_fee":"0.1","platform_paid_return_shipping_fee":"0.1","buyer_paid_return_shipping_fee":"0.1"}],"refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"0.1"},"return_shipping_document_type":"SHIPPING_LABEL","return_method":"PLATFORM_SHIPPED","is_combined_return":true,"combined_return_id":"4035309948547073951","seller_proposed_return_type":"PARTIAL_REFUND","partial_refund":{"currency":"IDR","amount":"10"},"buyer_rejected_partial_refund":true,"return_warehouse_address":{"full_address":"1199 Coleman Ave San Jose, CA 95110"},"is_quick_refund":false}],"total_count":100,"next_page_token":"aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查参数类型和格式是否正确。 |
| 25020005 | 无权处理此订单 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

