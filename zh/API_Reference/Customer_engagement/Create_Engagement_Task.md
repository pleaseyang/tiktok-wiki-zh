# 创建 Engagement Task

# Path: /customer_engagement/202412/engagement_tasks
# Method: [POST]
# 功能描述
创建一个 engagement task，充当将具有相似内容和规则的消息分组的容器，允许卖家追踪和比较不同类型内容的任务绩效。
请注意，每个任务都有强制的结束时间，一旦过期，就不能用于发送额外消息。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| idempotency_key | string | Y | 372dd4e7-9c02-4db0-a14b-0b23ce54e142 | 用于识别请求并防止重复处理同一请求的唯一 key，特别是在连接问题的情况下。确保每个请求使用唯一的 key 以避免意外重复。 |
| **注意**：我们建议您生成 v4 UUID 作为 key。 |  |  |  |  |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| template_id | string | Y | 50002_20011 | TikTok Shop 预定义的 engagement 消息模板 ID。从 [Get Message Templates](67777e44223fde02fdfdc157) 获取值。 |
| task_name | string | Y | Task1 for mega sale | 任务名称。长度：1-256 字节。 |
| end_time | int | Y | 1744344885 | 任务结束时间，届时将不再发送消息。Unix 时间戳（秒）。 |
| channel | string | Y | TIKTOK_IM | Engagement 渠道。仅支持 `TIKTOK_IM`。 |
| product_ids | []string | N | [8646958016719848812] | 商品 ID。从 [Search Products API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda) 获取此值。 |
| coupon_ids | []string | N | [8646958016719848812] | 优惠券 ID。从 [Search Coupons API](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd) 获取此值和其他优惠券相关信息。 |
**注意**：优惠券属性必须符合 [Get Message Templates API](67777e44223fde02fdfdc157) 中 `coupon_card_rules.coupon_type` 定义的规则。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_engagement/202412/engagement_tasks?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&idempotency_key=372dd4e7-9c02-4db0-a14b-0b23ce54e142
```

**Body**
```json
{"template_id":"50002_20011","task_name":"Task1 for mega sale","end_time":1744344885,"channel":"TIKTOK_IM","product_ids":[8646958016719848000],"coupon_ids":[8646958016719848000]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^task_id | string | 475910475643 | Customer engagement 任务的唯一标识符。在 [Send Engagement Message API](67777e448e882e030d29676e) 中传递此值，以将任务与消息发送操作关联。 |
# 响应示例
```json
{"code":0,"data":{"task_id":"475910475643"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 68009001 | 访问被拒绝。此店铺无法使用此 endpoint，因为卖家不满足 CRM 功能的访问条件。详情请参见 TikTok Shop Academy。 |
| 68009005 | 创建 engagement 任务失败。错误详情： |
