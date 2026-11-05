# 获取 Package Shipping 单据

# Path: /fulfillment/202309/packages/{package_id}/shipping_documents
# Method: [GET]
# 功能描述
对于使用 TikTok Shipping 发货的 package，使用此 API 获取由 `package_id` 指定的 package 的 `document_type` 所选 shipping 单据的 URL。首先调用 `Ship Package` 安排发货，然后在 package 被揽收前获取单据。

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
| document_type | string | Y | SHIPPING_LABEL | 可用的单据类型： |

* `SHIPPING_LABEL`：默认以 PDF 格式返回 shipping label。
* `PACKING_SLIP`：默认以 PDF 格式返回装箱单。
* `SHIPPING_LABEL_AND_PACKING_SLIP`：默认以 PDF 格式同时返回 package 的 shipping label 和装箱单。
* `SHIPPING_LABEL_PICTURE`：以 PNG 格式返回 shipping label。
* `HAZMAT_LABEL`：默认以 PDF 格式返回危险品标签。仅当 package 中有危险品时才能使用此值。使用此值时，`document_size` 固定为 A4，无需指定 `document_size`。
* `INVOICE_LABEL`：仅限巴西市场，document_size 固定为 A6，无需指定 `document_size`。默认以 PDF 格式返回发票标签。 |
   document_size |string |N |A6 |使用此字段指定要获取的单据大小。此参数仅适用于 PDF 格式的 shipping label、拣货单和装箱单。不适用于危险品标签，因为其固定为 A4。
如果您为 `document_type` 指定了 `SHIPPING_LABEL_PICTURE`，`document_size` 中指定的任何值都将被忽略。

可能的值：

* `A6`（默认）
* `A5` |
   document_format |string |N |PDF |shipping 单据的格式。
   可能的值：
* PDF（默认）
* ZPL（仅限 BR 和 MX 市场）

**注意**：不适用于 `SHIPPING_LABEL_PICTURE` 单据类型。 |
shipping_period |string |N |DEFAULT |为跨境场景获取指定末端配送服务商的 shipping label。
可能的值：

* DEFAULT（默认）
* LAST_MILE（仅在 4PL 模式下使用 3PL 主运输和清关 + 4PL 末端配送业务方案的跨境服务才会返回末端 shipping label；其他所有场景的调用将无效。
   ) |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/5433567853345/shipping_documents?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&document_type=SHIPPING_LABEL&document_size=A6&document_format=PDF&shipping_period=DEFAULT
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^doc_url | string | https://magelng.bytedance.net2/wsos_v2/oec_fulfillment_doc_tts/object/wsos641232 | 根据请求的 `document_type` 为指定 package 生成的 shipping 单据的 URL。URL 有效期为 24 小时。 |
| ^tracking_number | string | 752455325694 | 来自物流承运商的 package tracking 号码。 |
|  |  |  |  |
# 响应示例
```json
{"code":0,"data":{"doc_url":"https://magelng.bytedance.net2/wsos_v2/oec_fulfillment_doc_tts/object/wsos641232","tracking_number":"752455325694"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 11006010 | 内部 package 状态错误，请稍后重试。 |
| 11034002 | 此 API 仅适用于 TikTok Shipping 订单。对于商家自发货，请离线获取 shipping label 并通过 API 或卖家中心上传到 TikTok Shop。 |
| 11034009 | 仓库不存在。 |
| 11034023 | Shipping 单据生成超时错误，请稍后重试。 |
| 11034025 | 内部 package 标签错误，请稍后重试。 |
| 11034037 | Shipping 单据仍在由物流服务商生成中，请稍后重试。 |
| 21008017 | 此 API 仅适用于 TikTok Shipping 订单。对于商家自发货，请离线获取 shipping label 并通过 API 或卖家中心上传到 TikTok Shop。 |
| 21008043 | 此 package 由 TikTok fulfillment。无法打印 shipping 单据。 |
| 21008109 | 无法获取 shipping 信息，请检查订单状态。 |
| 21011001 | 未找到 package。如果错误持续存在，请联系平台寻求帮助。 |
| 21021010 | 发货失败。您可以通过选择以下原因无处罚取消订单：无法送达买家地址。 |
| 21023022 | 未知标签打印超时错误。如果错误持续存在，请联系平台寻求帮助。 |
| 21023034 | 内部 package 更新错误，请稍后重试。 |
| 21023035 | 请在获取 shipping 单据之前安排发货。 |
| 21023046 | Package 已经发货。 |
| 21023059 | Package 已经取消。 |
| 21042102 | Package 被揽收后无法打印单据。 |
| 21042104 | 发货前无法打印单据。请检查是否已安排发货后重试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

