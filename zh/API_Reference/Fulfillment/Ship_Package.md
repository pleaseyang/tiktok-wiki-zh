# 发货 Package

# Path: /fulfillment/202309/packages/{package_id}/ship
# Method: [POST]
# 功能描述
使用此 API 发货 package。有两种 shipping 选项可用：`TikTok Shipping` 或 `Seller Shipping`。

* `TikTok Shipping`：安排 package 交接时间，由 TikTok Shipping 承运商从卖家处揽收 package。
* `Seller Shipping`：卖家自行安排发货，并上传 tracking 号码和 `shipping_provider_id`。Package ID 可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0#Back%20To%20Top) 获取。
* `In-store Pickup`：确认发货并通知买家订单已准备好取货。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| package_id | string | Y | 5433567853345 | TikTok Shop package ID。 |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| handover_method | string | N | PICKUP | 可能的值： |

* `PICKUP`：物流承运商将从卖家的揽收地址揽收 package。
* `DROP_OFF`：卖家需要将 package 送到指定地点。 |
   pickup_slot |object |N | |揽收时间段。
   |
   ^start_time |int |N |1623812664 |package 揽收时间段的开始日期和时间，Unix 时间戳，单位为秒。 |
   ^end_time |int |N |1623812664 |package 揽收时间段的结束日期和时间，Unix 时间戳，单位为秒。 |
   self_shipment |object |N | |仅商家自发货 package 需要。检查 [Get Package Detail](https://partner.tiktokshop.com/docv2/page/650aa39fbace3e02b75d8617?external_id=650aa39fbace3e02b75d8617#Back%20To%20Top) 的 `delivery_option` 字段以区分平台物流和自发货。使用从 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) 获取的 `shipping_provider_id` 并上传对应的 `tracking_number`。 |
   ^tracking_number |string |Y |JX12345 |对于 `delivery_option` 为 `SEND_BY_SELLER` 的 package（商家自发货模式），您必须输入 `tracking_number` 来调用此 API。 |
   ^shipping_provider_id |string |Y |6617675021119438849 |对于 `delivery_option` 为 `SEND_BY_SELLER` 的 package（商家自发货模式），您必须输入 `shipping_provider_id` 来调用此 API。请使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) 获取 `shipping_provider_id`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/5433567853345/ship?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"handover_method":"PICKUP","pickup_slot":{"start_time":1623812664,"end_time":1623812664},"self_shipment":{"tracking_number":"JX12345","shipping_provider_id":"6617675021119438849"}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11001002 | 参数无效。 |
| 11001031 | 系统处理错误，请稍后重试。 |
| 11006013 | package 发货失败。Phones & Tablets 品类下的产品不能与同一 package 中的其他商品一起发货。请拆分订单。 |
| 11006014 | package 发货失败。如果您正在发货多个 Phones & Tablets 品类下的产品，它们必须在单独的 package 中发货。请拆分订单以继续。 |
| 11006021 | Package 已发货。请勿重复发货。 |
| 11021009 | 此请求没有可用的 shipping 服务。请修改 package 重量或检查收件人地址。如果错误持续存在，请联系平台寻求帮助。 |
| 11021010 | 由于邮政编码无效，发货失败。请要求买家修改地址。如果地址无法更改，您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021011 | 由于产品名称无效，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021012 | 地址不合法 |
| 11021013 | 由于收货地址过长，发货失败。请要求买家缩短地址。如果地址无法更改，您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021014 | 产品超尺寸 |
| 11021015 | 由于 package 超重，无法发货。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021016 | 由于 SKU 重量超过允许限制，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021017 | 由于 SKU 尺寸超过允许限制，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021018 | 由于 package 中的商品数量超过允许限制，无法发货。 |
| 11021019 | 由于 package 尺寸超过允许限制，无法发货。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021020 | 由于 package 周长超过允许限制，无法发货。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021021 | 由于 SKU 名称无效，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021022 | 由于 package 最长边超过允许限制，无法发货。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021023 | 由于买家和/或卖家地址无效，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021024 | 由于买家收货地址无效，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11021025 | 由于卖家发货地址无效，无法发货 package。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 11028006 | 此 tracking 号码无法匹配到任何承运商，请检查 tracking 号码后重新上传。 |
| 11050001 | 参数无效 |
| 21001001 | 参数无效。请确保您传递了正确的请求参数。 |
| 21001003 | 系统超时。如果错误持续存在，请联系平台寻求帮助。 |
| 21001008 | 未找到错误 |
| 21001011 | 系统处理错误，请稍后重试。 |
| 21001028 | 订单正在处理中。请稍后重试。 |
| 21004006 | 发货失败。请确保在发货前上传发票。 |
| 21004017 | 按需 RTS 不在揽收时间内。 |
| 21004019 | 需要在 RTS 前为所有订单上传发票。 |
| 21004020 | Fulfillment 发票状态不成功，无法 RTS package。 |
| 21004024 | 由于平台限制，订单发货失败。 |
| 21008025 | 卖家不能操作由平台 fulfillment 的订单 |
| 21008044 | 逆向 fulfillment unit 无法操作 |
| 21008099 | Package 已发货。请勿重复发货。 |
| 21011001 | 未找到 package。如果错误持续存在，请联系平台寻求帮助。 |
| 21011003 | 不允许 fulfill_unit 操作 |
| 21011007 | Package 商品有售后请求，请先处理售后请求。 |
| 21011008 | Package 不完整。如果错误持续存在，请联系平台寻求帮助。 |
| 21011020 | 这些订单已经发货。 |
| 21011022 | 无效的 tracking 号码或服务商 ID。请检查后重试。 |
| 21011025 | 重复的 tracking 号码。 |
| 21011026 | fulfillment tracking 号码使用次数超过限制 |
| 21011027 | Package 已经送达。 |
| 21011028 | 该 package 不属于当前店铺。请确保您提供了正确的 package ID 和/或 shop cipher。 |
| 21011030 | fulfillment 不允许更新 tracking 号码 |
| 21011040 | Package 已经发货。 |
| 21011041 | 订单已取消时无法完成操作。 |
| 21011050 | tracking 号码只能在一定小时数内更新。 |
| 21011051 | tracking 号码只能更新一次。 |
| 21011053 | 由于发货时间在揽收时间段之外，无法发货 package。 |
| 21011054 | 由于缺少揽收时间段，此请求没有可用的 shipping 服务。请联系客服寻求帮助。 |
| 21014009 | 发货失败。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 21021010 | 发货失败。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 21022029 | 系统处理错误，请稍后重试。 |
| 21022032 | 匹配服务商失败。 |
| 21034012 | tracking 号码已被使用 |
| 21042001 | 系统处理错误，请稍后重试。 |
| 21042067 | 物流服务商无法处理您的订单。 |
| 21042076 | 系统处理错误，请稍后重试。 |
| 21042227 | 对于 pop 4pl（跨境），发货位置的退货仓库尚未配置。 |
| 21042251 | 订单状态异常，商品无法发货。 |

