# 创建首程 Bundle (V2)

# 路径：/fulfillment/202510/first_mile_bundle
# 方法：[POST]
# 功能描述
如果您在单个首程 bundle 中向 TikTok Shop 仓库发送多个 package，可以使用此 API 在 TikTok Shop 上创建首程 bundle 并获取 bundle ID。

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
| order_ids | []string | Y | ["578967030217083407"] | 在单个首程 bundle 中发送的所有订单的 ID。每个请求最多：9,999 个订单 ID。 |
| 订单必须遵循以下限制： |  |  |  |  |

* 每个订单必须存在且已 RTS 并打印了 shipping label。
* 订单由同一卖家发送。
* 订单属于 TikTok Shop 服务区的单个分组。分组如下：
   * 分组 1：PH、SG、MY、VN、TH 和 JP。
   * 分组 2：DE、FR、IT、ES。

您不能使用此 API 为美国/英国订单创建首程 bundle。 |
handover_method |string |Y |PICKUP |您发送首程 bundle 的方式。可能的枚举值：

* `PICKUP`：您使用 TikTok Shop 提供的物流服务发送 bundle。
* `DROP_OFF`：您联系物流服务商并发送 bundle。物流服务商必须在 TikTok Shop 注册。 |
   shipping_provider_id |string |N |7463353253533 |TikTok Shop 中的物流服务商 ID。当 `handover_method == DROP_OFF` 时必填。 |
   tracking_number |string |N |SF1244442424 |bundle 的物流 tracking 号码。当 `handover_method == DROP_OFF` 时必填。 |
   phone_tail_number |string |N |1234 |发件人手机号的最后 4 位。当 `handover_method == DROP_OFF` 时必填。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202510/first_mile_bundle?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_ids":["578967030217083407"],"handover_method":"PICKUP","shipping_provider_id":"7463353253533","tracking_number":"SF1244442424","phone_tail_number":"1234"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^first_mile_bundle_id | string | BA123444534 | 首程 bundle 的 ID。 |
| ^url | string | https://open-fs-va.tiktokshop.com/doc_tts/object/28b05?skipCookie=true&timeStamp=1721272360&sign=ef63cd6 | 返回的运单链接。 |
| ^errors | []object |  | 与请求的订单关联的错误。条目可能表示无法解析请求的订单，或者与订单关联的 package 无法包含在 bundle 中。即使顶级 `code` 为 `0`，也可能返回多个错误。 |
| ^^code | int | 21008121 | 订单的错误码。 |
| ^^message | string | invalid order id | 解释订单错误的消息。 |
| ^^detail | object |  | 错误详情 |
| ^^^order_id | string | 578967030217083407 | TikTok Shop 订单 ID |
# 响应示例
```json
{"code":0,"data":{"first_mile_bundle_id":"BA123444534","url":"https://open-fs-va.tiktokshop.com/doc_tts/object/28b05?skipCookie=true\u0026timeStamp=1721272360\u0026sign=ef63cd6","errors":[{"code":21008121,"message":"invalid order id","detail":{"order_id":"578967030217083407"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

