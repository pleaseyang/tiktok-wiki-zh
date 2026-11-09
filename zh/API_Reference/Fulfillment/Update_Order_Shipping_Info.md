# 更新订单 Shipping 信息

# 路径：/fulfillment/202309/orders/{order_id}/shipping_info/update
# 方法：[POST]
# 功能描述
如果卖家输入了错误的 tracking 号码，此 API 允许卖家更新已发货订单的 tracking 号码和物流服务商。

* 此 API 仅适用于卖家发货的订单（或 package）。
* 仅用于更新已发货 package 的 tracking 号码和物流服务商。
* 对于已拆分发货的订单，请使用 [Update Package Shipping Info API](https://partner.tiktokshop.com/docv2/page/650aa666c16ffe02b8f1203c?external_id=650aa666c16ffe02b8f1203c)。

请注意，TikTok Shop 仅允许卖家在发货后 72 小时内更新 shipping 信息。

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
| order_id | string | Y | 576461413038785752 | TikTok Shop 订单 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| tracking_number | string | Y | 576460868968549926 | 承运商提供的 shipment tracking 号码。必须包含 4 到 50 个字符，仅由字母、数字、连字符（`-`）、下划线（`_`）、句点（`.`）或斜杠（`/`）组成。 |
| shipping_provider_id | string | Y | 6965352555291346690 | 标识将配送 package 的承运商。请调用 [Get Shipping Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd#Back%20To%20Top) 获取可用的物流服务商。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/orders/576461413038785752/shipping_info/update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"tracking_number":"576460868968549926","shipping_provider_id":"6965352555291346690"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
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
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10007002 | 当前订单不是卖家盲盒订单。 |
| 21001028 | 订单正在处理中。请稍后重试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 21011001 | 未找到 package。如果错误持续存在，请联系平台寻求帮助。 |
| 21011004 | 此 API 不能用于更新非卖家发货的 package 的 shipping 信息。 |
| 21011007 | Package 商品有售后请求，请先处理售后请求。 |
| 21011022 | 无效的 tracking 号码或服务商 ID。请检查后重试。 |
| 21011028 | 该 package 不属于当前店铺。请确保您提供了正确的 package ID 和/或 shop cipher。 |
| 21011030 | fulfillment 不允许更新 tracking 号码 |
| 21011041 | 订单已取消时无法完成操作。 |
| 21011042 | 订单已取消时无法完成操作。 |
| 21011043 | package 尚未发货。 |
| 21011049 | 由于平台规则限制，您无法更新 tracking 号码。 |
| 25001010 | 退货请求已完成，或订单已取消。 |

