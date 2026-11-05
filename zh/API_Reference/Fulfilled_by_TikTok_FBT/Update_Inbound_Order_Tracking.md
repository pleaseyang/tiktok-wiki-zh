# 更新 Inbound 订单追踪信息

# Path: /fbt/202602/inbound_orders/tracking_update
# Method: [POST]
# 功能描述
在发货后且订单被标记为 `Delivered` 或 `Received` 之前更新 inbound 订单的箱级别追踪信息。更新追踪时，发送完整的期望 `parcel_tracking_info` 列表；非空提交中省略的条目不会被保留，因此这不是部分补丁。箱的第一个追踪值不算作编辑，重新提交相同的规范化值也不会消耗另一次编辑。更改现有箱的追踪号会消耗该箱五次允许编辑中的一次；第六次更改将在本地更新之前被拒绝。提交的箱更新以原子方式应用于存储的追踪列表：要么保存完整的本地替换，要么都不保存。Warehouse 同步和物流追踪注册在此原子更新之外进行；warehouse 同步失败不会返回，追踪注册异步运行。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 5766071177167344427 | 要更新追踪信息的 inbound 订单的数字标识符。 |
| **注意：** 仅提供数字序列；不要包含"IBR"前缀（例如，使用 `123456` 而非 `IBR123456`）。 |  |  |  |  |
| parcel_tracking_info | []object | N |  | inbound 订单的箱级别包裹追踪信息，包括箱号、物流服务提供商名称和追踪号。 |
| ^provider_name | string | Y | FEDEX | `provider_name` 字段必须恰好包含以下字符串之一。 |

* `FEDEX` (Federal Express)
* `UPS` (United Parcel Service)
* `DHL` (DHL Express)
* `USPS` (United States Postal Service)
* `OTHER` (All other logistics providers)

**注意：** 输入必须与大写字符串完全匹配（例如，`"provider_name": "FEDEX"`）。 |
^tracking_number |string |Y |889042812410 |与此箱关联的追踪号。它不能为空或仅包含空格，且只能包含 ASCII 字母、数字、空格和连字符。去除空格和连字符后，必须剩余 8 到 40 个字母或数字。 |
^carton_number |string |Y |C0001 |此 inbound 订单中现有箱的箱号。去除前后空格后，此值与创建或替换追踪信息的箱匹配。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202602/inbound_orders/tracking_update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_id":"5766071177167344427","parcel_tracking_info":[{"provider_name":"FEDEX","tracking_number":"889042812410","carton_number":"C0001"}]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |
| 39015007 | 访问被拒绝。此 API 要求卖家绑定到恰好一个 merchant。 |
| 39015009 | SellerId 输入无效 |
| 39015010 | 未找到该 merchant 的 inbound 订单。 |
| 39015015 | 包裹追踪信息列表为空。 |
| 39015016 | 追踪服务提供商无效或不受支持。 |
| 39015017 | 箱号无效或缺失。 |
| 39015018 | 更新 inbound 订单的追踪信息失败。请检查 inbound 订单是否处于 "Shipped" 状态并重试。如果问题持续存在且原因未知，请联系平台支持。 |
| 39015019 | 追踪号无效或缺失。 |

