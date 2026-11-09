# 获取符合条件的 shipping 服务

# 路径：/fulfillment/202309/orders/{order_id}/shipping_services/query
# 方法：[POST]
# 功能描述
获取美国和日本可用的 shipping 服务。package 尺寸和重量是可选输入，用于计算可用选项。运费和配送时间是基于用于查询的 package 属性的估算值，如果在发货时这些属性发生变化，可用选项可能会改变。

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
| order_id | string | Y | 32132124331234 | TikTok Shop 订单 ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_line_item_ids | []string | N | ["32132124331234"] | 订单行项目 ID 列表 |
| warehouse_id | string | N | 7559598297381865271 | 指定发货仓库。调用获取仓库列表 API 获取可用仓库列表。 |
| weight | object | N |  | 计划 package 的重量。 |
| ^value | string | Y | 0.4 | 计划 package 的重量。 |
| ^unit | string | Y | GRAM | 用于测量重量的计量单位。 |

* GRAM
* POUND |
   dimension |object |N | |计划 package 的尺寸。 |
   ^length |string |Y |0.3 |package 的长度。长度、宽度、高度必须一起传递。 |
   ^width |string |Y |0.2 |package 的宽度。长度、宽度、高度必须一起传递。 |
   ^height |string |Y |0.2 |package 的高度。长度、宽度、高度必须一起传递。 |
   ^unit |string |Y |INCH |package 尺寸的计量单位。
* CM
* INCH |
   order_line_list |[]object |N | |此新参数与之前的 order_line_items_ids 字段完全向后兼容，此外还支持 bundle 订单拆分，请相应使用子项。 |
   ^order_line_id |string |N |57632132124331234 |对应的订单行 ID。 |
   ^sub_item_id |string |N |57632132124331234 |bundle 商品内的子订单行 ID。
* bundle 商品必填。
* 非 bundle 商品不必填。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/orders/32132124331234/shipping_services/query?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_line_item_ids":["32132124331234"],"warehouse_id":"7559598297381865271","weight":{"value":"0.4","unit":"GRAM"},"dimension":{"length":"0.3","width":"0.2","height":"0.2","unit":"INCH"},"order_line_list":[{"order_line_id":"57632132124331234","sub_item_id":"57632132124331234"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^order_id | string | 28823355942588 | TikTok Shop 订单 ID |
| ^order_line_id | []string | ["32132124331234"] | 行项目 ID 列表 |
| ^weight | object |  | 计划 package 的重量。 |
| ^^value | string | 1.2 | 计划 package 的重量。 |
| ^^unit | string | GRAM | 用于测量重量的计量单位。 |

* GRAM
* POUND |
   ^shipping_services |[]object | |订单可用的 shipping 服务。 |
   ^^id |string |288233559123860015 |shipping 服务 ID |
   ^^name |string |UPS-first class |shipping 服务名称 |
   ^^price |string |5 |此 shipping 服务的预估总价 |
   ^^currency |string |USD |价格的货币单位 |
   ^^earliest_delivery_days |int |3 |包裹配送所需的最短预估时间。仅限美国。 |
   ^^latest_delivery_days |int |5 |包裹配送所需的最长预估时间。仅限美国。 |
   ^^is_default |bool |false |是否为默认 shipping 服务 |
   ^^shipping_provider_name |string |UPS |物流服务商名称。仅限美国。 |
   ^^shipping_provider_id |string |288233559123860012 |物流服务商 ID。仅限美国。 |
   ^^shipping_fee |string |3 |运费 |
   ^^shipping_app_service_fee |string |1 |支付给 ERP 的运费附加费 |
   ^^signature_fee |string |1 |签收服务费 |
   ^dimension |object | |计划 package 的尺寸。 |
   ^^length |string |0.3 |package 的长度。 |
   ^^width |string |0.2 |package 的宽度。 |
   ^^height |string |0.04 |package 的高度。 |
   ^^unit |string |INCH |package 尺寸的计量单位。
* CM
* INCH |

# 响应示例
```json
{"code":0,"data":{"order_id":"28823355942588","order_line_id":["32132124331234"],"weight":{"value":"1.2","unit":"GRAM"},"shipping_services":[{"id":"288233559123860015","name":"UPS-first class","price":"5","currency":"USD","earliest_delivery_days":3,"latest_delivery_days":5,"is_default":false,"shipping_provider_name":"UPS","shipping_provider_id":"288233559123860012","shipping_fee":"3","shipping_app_service_fee":"1","signature_fee":"1"}],"dimension":{"length":"0.3","width":"0.2","height":"0.04","unit":"INCH"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10006402 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 21001001 | 参数无效。请确保您传递了正确的请求参数。 |
| 21011001 | 未找到 package。如果错误持续存在，请联系平台寻求帮助。 |
| 21011006 | 这些订单已经发货。 |
| 21011029 | 订单不属于该 fulfill unit |
| 21011037 | 此请求没有可用的 shipping 服务。请修改 package 重量，或检查收件人地址。如果多次重试后仍然出现此错误，请联系平台寻求帮助。 |
| 21011048 | 有多个可以发货的 package，请指定需要发货的订单行。 |

