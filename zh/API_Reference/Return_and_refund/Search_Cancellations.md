# 搜索取消

# 路径：/return_refund/202602/cancellations/search
# 方法：[POST]
# 功能描述
使用此 API 搜索并获取一个或多个订单取消记录。

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
| sort_field | string | N | update_time | 返回的结果将按指定字段排序。 |
| **Default:** `create_time` |  |  |  |  |
| 可能的值： |  |  |  |  |

* `create_time`
* `update_time`

使用 sort_order 参数指定返回结果的排序顺序。 |
sort_order |string |N |ASC |sort_field 参数的排序顺序。
**Default:** `ASC`
可能的值：

* `ASC`: Ascending order
* `DESC`: Descending order |
   page_size |string |N |10 |每页返回的结果数量。
   **Default:** 10.
   有效范围： [1-50]。 |
   page_token |string |N |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |用于检索分页结果集下一页的不透明 token。从上一次响应的 next_page_token 结果中获取此值。第一页不需要此参数。 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| cancel_ids | []string | N | ["577087614418520388"] | 订单取消 ID 列表。 |
| order_ids | []string | N | ["577087614418520388"] | TikTok Shop 订单 ID 列表。 |
| buyer_user_ids | []string | N | ["7494845267308415300"] | TikTok Shop 买家用户 ID 列表。 |
| cancel_types | []string | N | ["CANCEL"] | 订单取消类型列表。 |
| 可能的值： |  |  |  |  |

* `CANCEL`: 由卖家或系统取消。
* `BUYER_CANCEL`: 买家取消. 需要卖家或系统审批。 |
   cancel_status |[]string |N |["CANCELLATION_REQUEST_PENDING"] |订单取消状态列表。
   可能的值：
* `CANCELLATION_REQUEST_PENDING`
* `CANCELLATION_REQUEST_SUCCESS`
* `CANCELLATION_REQUEST_CANCEL`
* `CANCELLATION_REQUEST_COMPLETE`

有关这些状态的更多信息，请参阅 "API Overview"。 |
create_time_ge |int |N |1690340825 |筛选取消记录，仅显示在指定日期和时间之后创建的订单。Unix 时间戳。 |
create_time_lt |int |N |1690340825 |筛选取消记录，仅显示在指定日期和时间之前创建的订单。Unix 时间戳。 |
update_time_ge |int |N |1690340825 |筛选取消记录，仅显示在指定日期和时间之后更新的订单。Unix 时间戳。 |
update_time_lt |int |N |1690340825 |筛选取消记录，仅显示在指定日期和时间之前更新的订单。Unix 时间戳。 |
locale |string |N |en-US |用于显示订单的 BCP-47 语言区域代码，以逗号分隔. 默认值: en-US
请参阅 [Locale codes](678e3a47bae28f030a8c7523) 获取支持的区域设置代码列表。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202602/cancellations/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&sort_field=update_time&sort_order=ASC&page_size=10&page_token=aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA==
```

**Body**
```json
{"cancel_ids":["577087614418520388"],"order_ids":["577087614418520388"],"buyer_user_ids":["7494845267308415300"],"cancel_types":["CANCEL"],"cancel_status":["CANCELLATION_REQUEST_PENDING"],"create_time_ge":1690340825,"create_time_lt":1690340825,"update_time_ge":1690340825,"update_time_lt":1690340825,"locale":"en-US"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^cancellations | []object |  | 订单取消列表。 |
| ^^order_id | string | 577087614418520388 | TikTok Shop 订单 ID。 |
| ^^cancel_type | string | CANCEL | 订单取消类型。 |
| 可能的值： |  |  |  |

* `CANCEL`: 由卖家或系统取消。
* `BUYER_CANCEL`: 买家取消. 需要卖家或系统审批。 |
   ^^cancel_status |string |CANCELLATION_REQUEST_PENDING |订单取消状态。
   可能的值：
* `CANCELLATION_REQUEST_PENDING`
* `CANCELLATION_REQUEST_SUCCESS`
* `CANCELLATION_REQUEST_CANCEL`
* `CANCELLATION_REQUEST_COMPLETE` |
   ^^role |string |BUYER |订单取消发起方。
   可能的值：
* `BUYER`
* `SELLER`
* `OPERATOR`
* `SYSTEM` |
   ^^cancel_reason |string |ecom_order_to_ship_canceled_reason_created_by_mistakes |订单取消原因。 |
   ^^cancel_reason_text |string |Order created by mistake |订单取消原因，已本地化为另一种语言。
   您可以使用请求参数中的 locale 字段更改语言。 |
   ^^create_time |int |1690451136 |订单取消创建的时间。Unix 时间戳，单位为秒。 |
   ^^update_time |int |1690451136 |订单取消最近一次更新的时间. 以秒为单位的 Unix 时间戳。 |
   ^^seller_next_action_response |[]object | |卖家的下一步操作和截止时间。 |
   ^^^action |string |SELLER_RESPOND_BUYER_CANCEL |**可选。** 对于仍需卖家处理的买家发起的取消请求，操作取值为 `SELLER_RESPOND_BUYER_CANCEL`。 |
   ^^^deadline |int |1690554680 |以秒为单位的 Unix 时间戳，表示卖家执行下一步操作的截止时间。 |
   ^^refund_amount |object | |退款金额信息。 |
   ^^^currency |string |USD |退款货币。 |
   ^^^refund_total |string |1.23 |向买家退款的总金额。 |
   ^^^refund_subtotal |string |1 |向买家退款的小计金额。 |
   ^^^refund_shipping_fee |string |0.2 |退还给买家的运费金额。 |
   ^^^refund_tax |string |0.03 |退还给买家的退税金额。 |
   ^^^retail_delivery_fee |string |0.1 |根据 Colorado (US) 合规规则，当平台 GMV 超过 $500,000 USD 时，零售配送费生效。 |
   ^^^buyer_service_fee |string |1000 |仅适用于 ID 市场. 平台将根据具体场景向买家收取服务费。 |
   ^^cancel_line_items |[]object | |取消行项目。 |
   ^^^cancel_line_item_id |string |4035227913481196964 |取消订单行 ID。 |
   ^^^order_line_item_id |string |576468844534141348 |订单行项目 ID。 |
   ^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^product_image |object | |商品图片对象。包含商品图片信息。 |
   ^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^width |int |200 |商品图片宽度。
   Unit: px |
   ^^^^height |int |200 |商品图片高度。
   Unit: px |
   ^^^product_name |string |bundle No Heel Flat Heel Summer Winter Round Toe |商品名称。 |
   ^^^seller_sku |string |YYAPC23078TRT30 |卖家定义的 SKU 名称。 |
   ^^^refund_amount |object | |退款金额信息。 |
   ^^^^currency |string |USD |退款货币。 |
   ^^^^refund_total |string |1.23 |向买家退款的总金额。 |
   ^^^^refund_subtotal |string |1 |向买家退款的小计金额。 |
   ^^^^refund_shipping_fee |string |0.2 |退还给买家的运费金额。 |
   ^^^^refund_tax |string |0.03 |向买家退还的税款金额。 |
   ^^^^retail_delivery_fee |string |0.1 |根据 Colorado (US) 合规规则，当平台 GMV 超过 500,000 USD 时，零售配送费生效。
   |
   ^^^^buyer_service_fee |string |1000 |仅适用于 ID 市场. 平台将根据具体场景向买家收取买家服务费。 |
   ^^^cancel_sub_line_items |[]object | |取消的子订单行项目。
   子项表示属于卖家定义的"虚拟组合装"的 SKU。sub_items 将包含虚拟组合装中每个商品的所有相关信息。 |
   ^^^^cancel_sub_line_item_id |string |4035227657962164812 |取消子行项目 ID。 |
   ^^^^cancel_line_item_id |string |4035227657962164811 |取消订单行 ID。 |
   ^^^^sub_order_line_item_id |string |576473917261451852 |子订单行 ID。 |
   ^^^^order_line_item_id |string |576473917261451851 |订单行项目 ID。 |
   ^^^^sku_id |string |2729382476852921560 |SKU ID. |
   ^^^^sku_name |string |1#, Standard |SKU 名称。 |
   ^^^^product_image |object | |商品图片对象。包含商品图片信息。 |
   ^^^^^url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447 |商品图片 URL。 |
   ^^^^^width |int |200 |商品图片宽度。
   Unit: px |
   ^^^^^height |int |200 |商品图片高度。
   Unit: px |
   ^^^^product_name |string |bundle No Heel Flat Heel Summer Winter Round Toe |商品名称。 |
   ^^^^seller_sku |string |YYAPC23078TRT30 |卖家定义的 SKU 名称。 |
   ^^^^refund_amount |object | |退款金额信息。 |
   ^^^^^currency |string |USD |退款货币。 |
   ^^^^^refund_total |string |1.23 |向买家退款的总金额。 |
   ^^^^^refund_subtotal |string |1 |向买家退款的小计金额。 |
   ^^^^^refund_shipping_fee |string |0.2 |退还给买家的运费金额。 |
   ^^^^^refund_tax |string |0.03 |向买家退还的税款金额。 |
   ^^^^^retail_delivery_fee |string |0.1 |根据 Colorado (US) 合规规则，当平台 GMV 超过 $500,000 USD 时，零售配送费生效。 |
   ^^^^^buyer_service_fee |string |1000 |仅适用于 ID 市场. 平台将根据具体场景向买家收取服务费。 |
   ^^cancel_id |string |4035318504086604100 |特定订单取消的标识符。 |
   ^^should_replenish_stock |bool |false |订单成功取消后卖家是否应补充库存。 |
   ^total_count |int |100 |符合查询条件的取消订单数量。 |
   ^next_page_token |string |aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA== |用于获取下一页结果的不透明令牌。如果此值非空，请在下一次请求的 `page_token` 参数中提供它。空值表示没有更多结果。 |

# 响应示例
```json
{"code":0,"data":{"cancellations":[{"order_id":"577087614418520388","cancel_type":"CANCEL","cancel_status":"CANCELLATION_REQUEST_PENDING","role":"BUYER","cancel_reason":"ecom_order_to_ship_canceled_reason_created_by_mistakes","cancel_reason_text":"Order created by mistake","create_time":1690451136,"update_time":1690451136,"seller_next_action_response":[{"action":"SELLER_RESPOND_BUYER_CANCEL","deadline":1690554680}],"refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"1000"},"cancel_line_items":[{"cancel_line_item_id":"4035227913481196964","order_line_item_id":"576468844534141348","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"bundle No Heel Flat Heel Summer Winter Round Toe","seller_sku":"YYAPC23078TRT30","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"1000"},"cancel_sub_line_items":[{"cancel_sub_line_item_id":"4035227657962164812","cancel_line_item_id":"4035227657962164811","sub_order_line_item_id":"576473917261451852","order_line_item_id":"576473917261451851","sku_id":"2729382476852921560","sku_name":"1#, Standard","product_image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/004797ebfd8c4d3da2df1cc4bfdb0614~tplv-o3syd03w52-origin-jpeg.jpeg?from=4246405447","width":200,"height":200},"product_name":"bundle No Heel Flat Heel Summer Winter Round Toe","seller_sku":"YYAPC23078TRT30","refund_amount":{"currency":"USD","refund_total":"1.23","refund_subtotal":"1","refund_shipping_fee":"0.2","refund_tax":"0.03","retail_delivery_fee":"0.1","buyer_service_fee":"1000"}}]}],"cancel_id":"4035318504086604100","should_replenish_stock":false}],"total_count":100,"next_page_token":"aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 25001001 | 传递了无效的请求参数。请检查参数类型和格式是否正确。 |
| 25020005 | 无权处理此订单 |
| 25020008 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

