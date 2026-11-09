# 获取物流追踪信息

# 路径：/logistics/202604/orders/{order_id}/tracking
# 方法：[GET]
# 功能描述
使用此 API 获取订单的详细物流追踪信息。此 API 目前仅支持跨境贸易（CBT）订单。与 Get Tracking 相比，此 API 按包裹分组信息，并可包含每个包裹的承运商、最新运单号和追踪事件历史。
有关 `action_code` 和 `action_code_name` 之间的映射关系，请参见 https://partner.tiktokshop.com/docv2/page/37tihrdq。

---


# 公共参数
公共参数详情请参考 [如何调用 TikTok Shop APIs - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 参数 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 576461413038785752 | TikTok Shop 订单 ID。 |
# 请求 Query 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/logistics/202604/orders/576461413038785752/tracking?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 参数描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^order_id | string | 577071607420326620 | TikTok Shop 订单 ID。 |
| ^logistics_details | []object |  | 订单中的包裹列表。每项描述一个包裹，可包含其承运商、最新运单号和追踪事件历史。 |
| ^^newest_tracking_no | string | 861651122474 | 此包裹的最新物流追踪号。 |
| ^^carrier_name | string | J&T Express | 承运商名称。 |
| ^^track_list | []object |  | 此包裹的物流追踪事件列表。 |
| ^^^description | string | 包裹已送达！\n | 此追踪事件的描述。 |
| ^^^tracking_no | string | 861651122474 | 与此追踪事件关联的物流追踪号。 |
| ^^^update_time_millis | int | 1694686949000 | 此追踪事件更新的 Unix 时间戳（毫秒，GMT/UTC+00:00）。 |
| ^^^action_code | int | 50101 | 此追踪事件的 action code。它是一个枚举状态值；完整的枚举列表由业务方维护。 |
| 参考：action_code/action_code_name 映射详情 https://partner.tiktokshop.com/docv2/page/37tihrdq |  |  |  |
| ^^^action_code_name | string | signed_personally | 与 `action_code` 对应的机器可读状态名称。有关 action code 和 name 映射详情，请参见 https://partner.tiktokshop.com/docv2/page/37tihrdq。 |
# 响应示例
```json
{"code":0,"data":{"order_id":"577071607420326620","logistics_details":[{"newest_tracking_no":"861651122474","carrier_name":"J\u0026T Express","track_list":[{"description":"Package has been delivered!\\n","tracking_no":"861651122474","update_time_millis":1694686949000,"action_code":50101,"action_code_name":"signed_personally"}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码详情请参考 [如何调用 TikTok Shop APIs - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11007009 | 此订单不在支持的业务场景中 |
| 11007010 | 系统繁忙，请稍后重试。 |
