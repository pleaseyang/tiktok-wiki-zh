# 创建 Package

# 路径：/fulfillment/202512/packages
# 方法：[POST]
# 功能描述
使用此 API 发货订单（购买 label）。此 API 在美国、英国、EMEA 和日本地区可用。运费和配送时间仅为估算值，基于您提供的 package 尺寸和重量。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| ship_type | string | Y | 2 | 1：一个订单中的所有商品合并在一个 package 中发货，使用一个 tracking 号码 |
| 2：一个父订单中的部分商品分多个 package 发货，使用多个 tracking 号码 |  |  |  |  |
| 3：多个订单中的所有商品合并在一个 package 中发货，使用一个 tracking 号码。 |  |  |  |  |
| order_id | string | N | 2882335594258860015 | TikTok Shop 订单 ID。当 `ship_type` 为 `1` 或 `2` 时必填；当 `ship_type` 为 `3` 时不使用。 |
| warehouse_id | string | N | 7559598297381865271 | 仅用于美国本地到本地订单。 |
| 如果您需要修改发货仓库，可以编辑仓库 ID；与此 ID 关联的地址将用于生成 shipping label，对库存没有影响。 |  |  |  |  |
| 注意：我们仅支持启用状态的仓库 ID。传入其他状态的仓库 ID 将导致发货失败。 |  |  |  |  |
| order_line_item | []object | N |  | 订单行项目 ID 列表。 |
| 当 ship_type=2 时，此字段必填；当 ship_type=1 和 3 时，不使用此字段。 |  |  |  |  |
| ^order_line_id | string | N | 2882335594258860015 | TikTok Shop 订单行项目 ID。 |
| ^sub_item_id | string | N | 2882335594258860015 | 仅限虚拟 bundle 商品，子商品 ID 列表。 |
| 当 ship_type=2 时，此字段必填；当 ship_type=1 和 3 时，不使用此字段。 |  |  |  |  |
| order_list_ids | []string | N | ["2882335594258860015","2882335594258860016"] | 合并到一个 package 中的 TikTok Shop 订单 ID。当 `ship_type` 为 `3` 时必填；至少提供两个订单 ID。 |
| dimension | object | N |  | Package 尺寸。对于 `ship_type` `1` 和 `2`，每个尺寸必须在 0.01 到 999999 之间，且不超过两位小数。 |
| ^length | string | Y | 1.2 | Package 长度。 |
长度、宽度和高度必须一起传递。 |
^width |string |Y |0.2 |Package 宽度。
长度、宽度和高度必须一起传递。 |
^height |string |Y |0.03 |Package 高度。
长度、宽度和高度必须一起传递。 |
^unit |string |Y |CM |package 尺寸的计量单位。对于美国的 package，使用 `INCH`。
可用值：

* `CM`
* `INCH` |
   shipping_service_id |string |N |288233559123860015 |指定使用的 shipping 服务。
   如果未指定，使用从 [Get Eligible Shipping Service](https://partner.tiktokshop.com/docv2/page/650aa6b2bace3e02b75dda4e) 获取的默认服务。 |
   weight |object |N | |Package 重量。对于 `ship_type` `1` 和 `2`，值必须在 0.01 到 999999 之间，且不超过两位小数。 |
   ^value |string |Y |1.2 |package 重量的数值。 |
   ^unit |string |Y |GRAM |package 重量的计量单位。

可用值：

* `GRAM`
* `POUND` |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202512/packages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"ship_type":"2","order_id":"2882335594258860015","warehouse_id":"7559598297381865271","order_line_item":[{"order_line_id":"2882335594258860015","sub_item_id":"2882335594258860015"}],"order_list_ids":["2882335594258860015","2882335594258860016"],"dimension":{"length":"1.2","width":"0.2","height":"0.03","unit":"CM"},"shipping_service_id":"288233559123860015","weight":{"value":"1.2","unit":"GRAM"}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^dimension | object |  | Package 尺寸。 |
| ^^length | string | 1.2 | Package 长度。 |
| ^^width | string | 0.2 | Package 宽度。 |
| ^^height | string | 0.03 | Package 高度。 |
| ^^unit | string | CM | package 尺寸的计量单位。 |
可用值：

* `CM`
* `INCH` |
   ^shipping_service_info |object | |为 package 选择的 shipping 服务信息。 |
   ^^id |string |288233559123860015 |shipping 服务 ID。 |
   ^^name |string |UPS-first class |shipping 服务名称。 |
   ^^price |string |10 |此服务的预估价格。 |
   ^^currency |string |USD |价格的货币单位。 |
   ^^earliest_delivery_days |int |3 |包裹配送所需的最短预估时间。仅限美国。 |
   ^^latest_delivery_days |int |5 |包裹配送所需的最长预估时间。仅限美国。 |
   ^^shipping_provider_id |string |2882322591238 |物流服务商 ID。仅限美国。 |
   ^^shipping_provider_name |string |UPS |物流服务商名称。仅限美国。 |
   ^package_id |string |2882335594258860015 |包裹 ID。 |
   ^weight |object | |Package 重量。 |
   ^^value |string |1.2 |package 重量的数值。 |
   ^^unit |string |GRAM |package 重量的计量单位。

可用值：

* `GRAM`
* `POUND` |
   ^create_time |int |1623812664 |商品创建的时间。
   Unix 时间戳。 |

# 响应示例
```json
{"code":0,"data":{"dimension":{"length":"1.2","width":"0.2","height":"0.03","unit":"CM"},"shipping_service_info":{"id":"288233559123860015","name":"UPS-first class","price":"10","currency":"USD","earliest_delivery_days":3,"latest_delivery_days":5,"shipping_provider_id":"2882322591238","shipping_provider_name":"UPS"},"package_id":"2882335594258860015","weight":{"value":"1.2","unit":"GRAM"},"create_time":1623812664},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11001002 | 参数无效。 |
| 11001027 | 系统超时。如果此错误持续存在，请联系平台寻求帮助。 |
| 11003011 | Shipping 服务操作冲突错误，请检查 shipping 服务 ID。 |
| 11021009 | 此请求没有可用的 shipping 服务。请修改 package 重量或检查收件人地址。如果错误持续存在，请联系平台寻求帮助。 |
| 11021012 | 地址不合法 |
| 11021014 | 商品超尺寸 |
| 11028006 | 此 tracking 号码无法匹配到任何承运商，请检查 tracking 号码后重新上传。 |
| 11050001 | 参数无效 |
| 21001001 | 参数无效。请确保您传递了正确的请求参数。 |
| 21001011 | 系统处理错误，请稍后重试。 |
| 21004008 | 创建 label 未找到 shipping 服务 |
| 21004010 | 您的国家不支持使用此功能。 |
| 21008025 | 卖家不能操作由平台 fulfillment 的订单 |
| 21008042 | 卖家已打印 shipping label |
| 21008106 | 此接口不能在此地区使用。 |
| 21011001 | 未找到 package。如果错误持续存在，请联系平台寻求帮助。 |
| 21011003 | 不允许 fulfill_unit 操作 |
| 21011006 | 这些订单已经发货。 |
| 21011007 | Package 商品有售后请求，请先处理售后请求。 |
| 21011012 | 不匹配交易规则 |
| 21011020 | 这些订单已经发货。 |
| 21011029 | 订单不属于该 fulfill unit |
| 21011033 | 订单已合并 |
| 21011035 | 不允许拆分订单 |
| 21011037 | 此请求没有可用的 shipping 服务。请修改 package 重量，或检查收件人地址。如果多次重试后仍然出现此错误，请联系平台寻求帮助。 |
| 21011046 | 订单已合并，不允许拆分订单 |
| 21011048 | 有多个可以发货的 package，请指定需要发货的订单行。 |
| 21022025 | 已购买 shipping label。 |
| 21022026 | 无法购买 shipping label，请稍后重试。 |
| 21022029 | 系统处理错误，请稍后重试。 |
| 21030005 | 处理 create_label_status 不允许执行此操作 |
| 21030006 | Shipping label 购买成功。当前订单状态不允许此操作。 |
| 21032001 | fulfill unit 状态不允许更新 pkg 属性 |

