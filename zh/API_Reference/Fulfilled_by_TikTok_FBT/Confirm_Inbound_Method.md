# 确认 Inbound 方式

# Path: /fbt/202603/confirm_inbound_method
# Method: [POST]
# 功能描述
确认 FBT inbound plan 当前可用的 warehouse 入库选项。首先调用 List Available Inbound Methods API 并选择一个带有精确 `estimate_arrival_time` 窗口的 `inbound_method`。然后使用所选内容调用 Get Inbound Method Detail API，并选择一个返回的 `placement_option_id`。使用来自同一选择的 `placement_option_id`、`inbound_method` 和 `estimate_arrival_time` 进行确认。如果该选项已过期，请重新调用两个前置 API 以获取当前选择和新的 `placement_option_id`，然后重试。响应包含为该 plan 生成的子 inbound 订单 ID。

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
| plan_id | string | Y | 5766071177167344427 | 正在确认 warehouse 入库选项的 FBT inbound plan 的标识符。 |
| placement_option_id | string | Y | 5766071177167344420 | 入库选项 ID。入库选项代表货件拆分和目的地。 |
| inbound_method | string | Y | D2FC | **可能的值：** |

* `D2FC`（直接送至 fulfillment center，可能会拆分为多个货件）
* `ONE_HUB`（单一目的地，包含费用） |
   estimate_arrival_time |object |Y | |预计到达时间。值应从 `ListAvailableInboundMethod` API 响应的 `available_time_window_list` 中获取 |
   ^start_timestamp |string |Y |1774162800 |预计到达时间窗口的开始时间，以秒为单位的 Unix 时间戳表示。例如，`1774162800` 对应 2026 年 3 月 22 日星期日 00:00 PDT（`2026-03-22T07:00:00Z`）。请使用 `ListAvailableInboundMethod` API 在 `available_time_window_list` 中返回的精确 `start_timestamp`。 |
   ^end_timestamp |string |Y |1774767600 |预计到达时间窗口的结束时间，以秒为单位的 Unix 时间戳表示。例如，`1774767600` 对应 2026 年 3 月 29 日星期日 00:00 PDT（`2026-03-29T07:00:00Z`）。请使用 `ListAvailableInboundMethod` API 在 `available_time_window_list` 中返回的精确 `end_timestamp`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202603/confirm_inbound_method?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"plan_id":"5766071177167344427","placement_option_id":"5766071177167344420","inbound_method":"D2FC","estimate_arrival_time":{"start_timestamp":"1774162800","end_timestamp":"1774767600"}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^inbound_order_ids | []string | ["5766071177167344427","5766071177167344428"] | 为已确认的 FBT inbound plan 生成的子 inbound 订单 ID 列表。 |
# 响应示例
```json
{"code":0,"data":{"inbound_order_ids":["5766071177167344427","5766071177167344428"]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |

