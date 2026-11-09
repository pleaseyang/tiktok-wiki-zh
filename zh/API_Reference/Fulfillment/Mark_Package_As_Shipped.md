# 标记包裹为已发货

# 路径：/fulfillment/202610/orders/{order_id}/packages
# 方法：[POST]
# 功能描述
**此接口目前仅适用于以下市场: US, UK, ES, IE, IT, DE, FR, JP.**
此接口适用于通过自选/首选物流承运商履约订单的卖家，允许卖家向 TikTok Shop 上传有效的包裹信息（包裹内商品、物流服务商信息和运单号）订单/订单行商品。使用 [Get Shipping Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) 获取物流服务商的 `shipping_provider_id`。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时，如果未传递正确的值，将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 576461413038785752 | TikTok Shop 订单的唯一标识符。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_line_list | []object | N |  | 此新参数与之前的 oder_line_items_ids 字段完全向后兼容，此外还支持捆绑订单拆分，请相应使用子商品 |
| ^order_line_id | string | N | 5767675021119438849 | 对应的订单行 ID。 |
| ^sub_item_id | string | N | 5767675021119438849 | 组合商品内的子订单行 ID。 |

* 组合商品必填。
* 非捆绑商品不需要。 |
   shipping_info_list |[]object |N | |"仅支持在 3PL 单品场景（非虚拟捆绑）的分拆发货中上传多个运单号（此功能仅支持白名单卖家；如果您不在允许名单中，建议联系 AM 申请）
   其他场景下，一次只能上传一个运单号。" |
   ^tracking_number |string |N |6617675021119438849 |运单号。 |
   ^shipping_provider_id |string |N |12312312321323432 |使用 Get Shipping Provider API 获取物流服务商的 shipping_provider_id。 |
   ^note |string |N |this is a table |"仅对部分白名单卖家可用。这适用于大件单品需要分多个包裹发货的场景。不在白名单中的卖家上传此字段将被平台自动忽略。
   例如，包裹 1 标记为 ""headboard""，包裹 2 标记为 ""bed frame""。
   此字段将展示给买家，请谨慎填写。" |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202610/orders/576461413038785752/packages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_line_list":[{"order_line_id":"5767675021119438849","sub_item_id":"5767675021119438849"}],"shipping_info_list":[{"tracking_number":"6617675021119438849","shipping_provider_id":"12312312321323432","note":"this is a table"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^order_id | string | 32131324123321 | TikTok Shop 订单 ID。 |
| ^order_line_item_ids | []string | ["31322412312312"] | 订单行项目 ID 列表。 |
| ^package_id | string | 32141235124234 | Package ID. |
| ^warning | object |  | Warning message. |
| ^^message | string | match more than one provider | 具体的警告信息。 |
# 响应示例
```json
{"code":0,"data":{"order_id":"32131324123321","order_line_item_ids":["31322412312312"],"package_id":"32141235124234","warning":{"message":"match more than one provider"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11001027 | System timeout. If this error persists, please contact the platform for assistance. |
| 11001031 | System process error, please try again later. |
| 11005004 | warehouse not exist |
| 11005010 | get lead time from card service error |
| 11006005 | System process error, please try again later. |
| 11006026 | System process error, please try again later. |
| 11021009 | No available shipping services for this request. Please modify the package weight or check the recipient address. If the error persists, please contact the platform for assistance. |
| 11028006 | This tracking number cannot be matched to any carrier, please check the tracking number and upload again. |
| 11050001 | invalid param |
| 21001001 | Invalid parameters. Please ensure you are passing the correct request parameter(s). |
| 21001008 | not found error |
| 21001011 | System process error, please try again later. |
| 21001028 | The order is being processed. Try again later. |
| 21001029 | rpc logistics_logistics_service_4b failed |
| 21001043 | System process error, please try again later. |
| 21001055 | System process error, please try again later. |
| 21004012 | Tracking number has special characters, verify failed. |
| 21004015 | Tracking number mismatch provider. |
| 21004016 | Tracking number verify, not avalible logsitics service or provider |
| 21004019 | Need invoice uploaded for all order before rts. |
| 21004020 | Fulfillment Invoice status is not success, can not rts pkg. |
| 21008025 | Seller cannot operate orders which are fulfilled by platform |
| 21008042 | seller already print shipping label |
| 21008044 | SellerFulfillUnitInReverseCannotOperate |
| 21008099 | Package has been shipped. Please not ship the package again. |
| 21008106 | This interface cannot be used in this region. |
| 21008300 | System process error, please try again later. |
| 21011001 | Package not found. If the error persists, please contact the platform for assistance. |
| 21011003 | fulfill_unit action not allowed |
| 21011004 | 此接口不能用于更新非卖家发货包裹的配送信息。 |
| 21011006 | These orders are already shipped. |
| 21011007 | Package item has after-sale request, please process the after-sale request first. |
| 21011012 | not match trade rule |
| 21011013 | not match logistics rule |
| 21011020 | These orders are already shipped. |
| 21011022 | Invalid tracking number or provider ID. Please double check and try again. |
| 21011025 | Duplicate tracking number. |
| 21011026 | fulfillment tracking no used times over limit |
| 21011029 | order does not belong to fulfill unit |
| 21011030 | fulfillment not allow update tracking no |
| 21011033 | order already combined |
| 21011036 | split same sku in Multi Package not allow. |
| 21011046 | Order has combine, not allow split order |
| 21011048 | There are multiple packages that can be shipped, please specify the order line that needs to be shipped. |
| 21011050 | The tracking number can only be updated within a certain number of hours. |
| 21011051 | The tracking number can only be updated once. |
| 21021010 | Failed to ship. You may cancel the order without penalty by selecting the following reason: Unable to deliver to buyer address. |
| 21022025 | A shipping label has already been purchased. |
| 21022026 | Cannot purchase shipping label, please try again later. |
| 21022028 | split pkg fail. |
| 21022029 | System process error, please try again later. |
| 21022030 | System process error, please try again later. |
| 21032001 | fulfill unit status not allow to update pkg attr |
| 21034006 | decision route occurs error |
| 21034012 | tracking no has been used |
| 21042056 | These orders are already shipped. |
| 21042057 | These orders are not in the Awaiting shipment status. Couldn't create labels for them. |

