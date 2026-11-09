# 获取 Engagement Task 绩效

# 路径：/customer_engagement/202412/performances
# 方法：[POST]
# 功能描述
获取 customer engagement task 的详细绩效指标，包括消息阅读量、订单转化量和其他关键 engagement 统计数据。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| shop_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | Shop_cipher 对于跨境店铺是必填的，对于本地店铺是可选的。每个店铺的 shop_cipher 是唯一的。从 Get Authorized Shop API 动态获取此参数。使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| task_ids | []string | Y | [8646958016719848812] | 要获取绩效数据的 customer engagement task ID。提供 1 到 50 个 ID；每个 ID 必须是适合有符号 64 位整数的 base-10 字符串。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_engagement/202412/performances?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"task_ids":[8646958016719848000]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^task_performances | []object |  | 请求的任务绩效列表。 |
| ^^id | string | 8646958016719848812 | 此绩效记录对应的 customer engagement task ID。 |
| ^^status | string | SENDING | 任务的状态。 |
| 可能的值： |  |  |  |

* `UNKNOWN`：任务状态未知。
* `DRAFT`：任务处于草稿状态。
* `WAITING`：任务等待中。
* `SENDING`：任务正在发送消息。
* `FAILED`：任务发送消息失败。
* `CANCELED`：任务已取消。
* `SUCCESS`：任务成功完成。
* `DELETED`：任务已删除。 |
   ^^sent_recipient_count |int |100 |收到消息的用户数量。 |
   ^^read_recipient_count |int |20 |阅读了消息的用户数量。 |
   ^^order_count |int |10 |由消息产生的订单数量。 |
   ^^gmv_amount |string |5.50 |转化订单的收入。 |
   ^^claimed_coupons_count |int |1 |已领取的优惠券数量。 |

# 响应示例
```json
{"code":0,"data":{"task_performances":[{"id":"8646958016719848812","status":"SENDING","sent_recipient_count":100,"read_recipient_count":20,"order_count":10,"gmv_amount":"5.50","claimed_coupons_count":1}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
