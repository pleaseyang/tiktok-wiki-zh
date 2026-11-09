# 搜索 Sessions

# 路径：/customer_service/202602/sessions/search
# 方法：[POST]
# 功能描述
按开始时间范围以及可选的买家昵称搜索客服 sessions。

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
| page_size | int | Y | 10 | 每页返回的结果数量。 |
| 有效范围：[1-100] |  |  |  |  |
| page_token | string | N | 1 | 用于获取分页结果集下一页的不透明 token。从上一次响应的 next_page_token 结果中获取此值。第一页不需要此参数。 |
| locale | string | N | en-US | 用于显示拒绝原因的 BCP-47 locale 代码，以逗号分隔。默认值：en-US |
| 支持的 locale 代码列表请参考 https://partner.tiktokshop.com/docv2/page/678e3a47bae28f030a8c7523。 |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| begin_time_ge | int | Y | 1773222516 | 返回 begin_time 大于或等于此 Unix 时间戳（秒）的 sessions。仅支持最近 90 天的数据。 |
| begin_time_lt | int | Y | 1773242516 | 返回 begin_time 小于此 Unix 时间戳（秒）的 sessions。该值必须大于或等于 begin_time_ge。 |
| buyer_nickname | string | N | Albert | 按买家昵称筛选 sessions。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202602/sessions/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=10&page_token=1&locale=en-US
```

**Body**
```json
{"begin_time_ge":1773222516,"begin_time_lt":1773242516,"buyer_nickname":"Albert"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 10 | 如果没有更多记录，此字段将为 ""（空字符串）。 |
| ^sessions | []object |  | 符合请求筛选条件的客服 sessions。 |
| ^^id | string | 7494560109732334261 | Session ID。 |
| ^^conversation_id | string | 7601726193700929800 | Conversation ID。 |
| ^^begin_time | int | 1773222516 | Session 开始时的 Unix 时间戳（秒）。 |
| ^^end_time | int | 1773232516 | Session 结束时的时间戳。 |
| ^^buyer_nickname | string | Albert | 买家昵称。 |
| ^^chat_tags | []string | ["Logistics"] | AfterSale/Logistics/Presale |
| ^^satisfaction_score | int | 4 | 客户对该 session 的满意度评分（例如 1-5 分）。分数越高表示满意度越高。 |
| ^^dissatisfaction_reason | string | 响应或处理缓慢 | 买家给出低满意度评分时提供的原因。 |
| 原因的语言由 locale 请求参数决定。 |  |  |  |
| ^^first_response_late | bool | false | 指示首次回复是否超过了预期响应时间或 SLA。 |
| ^^first_response_time | int | 123 | 从买家发送第一条消息到卖家发送首次回复之间经过的时间（秒）。 |
# 响应示例
```json
{"code":0,"data":{"next_page_token":"10","sessions":[{"id":"7494560109732334261","conversation_id":"7601726193700929800","begin_time":1773222516,"end_time":1773232516,"buyer_nickname":"Albert","chat_tags":["Logistics"],"satisfaction_score":4,"dissatisfaction_reason":"Slow response or resolution","first_response_late":false,"first_response_time":123}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
