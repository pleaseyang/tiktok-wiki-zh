# 列出可用 Inbound 方式

# Path: /fbt/202602/list_available_inbound_method
# Method: [POST]
# 功能描述
检索特定 plan 的有效 inbound 运输方式和到达时间窗口。选择 `inbound_method` 和一个完整的到达时间窗口后，使用相同的 `plan_id`、所选的 `inbound_method` 以及该窗口的精确 `start_timestamp` 和 `end_timestamp` 对作为 `estimate_arrival_time` 调用 **Get Inbound Method Detail**（`POST /fbt/202602/inbound_method_detail`）。

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
| plan_id | string | Y | 5766071177167344427 | Inbound plan 标识符 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202602/list_available_inbound_method?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"plan_id":"5766071177167344427"}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^available_inbound_method_list | []object |  | 指定 plan 的可用 inbound 方式列表，包括到达时间窗口、入库费用估算和 warehouse。 |
| ^^inbound_method | string | D2FC | Inbound 方式。 |

* D2FC
* ONE_HUB |
   ^^available_time_window_list |[]object | |此 inbound 方式可用的每周到达时间窗口。 |
   ^^^start_timestamp |string |1774162800 |表示周日午夜的 Epoch 秒，如 2026-03-29T07:00:00Z，在美国使用美国西部时区

**此值应在后续的 GetInboundMethodDetail API 中传递** |
^^^end_timestamp |string |1774767600 |表示周日午夜的 Epoch 秒，如 2026-03-29T07:00:00Z，在美国使用美国西部时区
**此值应在后续的 GetInboundMethodDetail API 中传递** |
^^warehouse_list |[]object | |此 inbound 方式选项可用的 warehouse 列表。 |
^^^warehouse_name |string |FC09_ATL2 |此可用 inbound 方式选项的 warehouse 名称。 |
^^^warehouse_id |string |7542187927317874487 |此可用 inbound 方式选项的 warehouse 标识符。 |
^^placement_fee_estimate |object | |此 inbound 方式的估算入库费用。截至 2026 年 4 月，只有 ONE_HUB 方式可以包含金额。 |
^^^amount |string |13.50 |入库费用金额。 |
^^^currency |string |USD |- USD

* CNY
* EUR |

# 响应示例
```json
{"code":0,"data":{"available_inbound_method_list":[{"inbound_method":"D2FC","available_time_window_list":[{"start_timestamp":"1774162800","end_timestamp":"1774767600"}],"warehouse_list":[{"warehouse_name":"FC09_ATL2","warehouse_id":"7542187927317874487"}],"placement_fee_estimate":{"amount":"13.50","currency":"USD"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |

