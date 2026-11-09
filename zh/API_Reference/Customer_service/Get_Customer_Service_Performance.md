# 获取客服绩效

# 路径：/customer_service/202407/performance
# 方法：[GET]
# 功能描述
获取店铺在所选时间段内的客服绩效指标。

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
| support_date_ge | string | Y | 2024-07-01 | 用于选择纳入绩效评估的聊天支持 session 的起始日期（YYYY-MM-DD）。 |
| support_date_lt | string | Y | 2024-07-08 | 用于选择纳入绩效评估的聊天支持 session 的截止日期（YYYY-MM-DD）。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202407/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&support_date_ge=2024-07-01&support_date_lt=2024-07-08
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^performance | object |  | 基于所选评估期内聊天支持 session 的店铺客服绩效指标。 |
| ^^support_session_count | int | 15 | 客户发起的聊天支持 session 总数。当客户首次点击 FAQ 卡片或在聊天中发送消息（文本、图片、视频、表情、商品卡片、订单卡片等）时，session 开始。纳入计算的是在指定时间段内开始的 session。 |
| ^^response_percentage | string | 93.4 | 在 24 小时内首次回复的聊天支持 session 百分比。纳入计算的是在指定时间段内开始的 session。 |

* 自动回复（如 FAQ 卡片）视为 24 小时内的回复。
* 休假模式下发起的 session 不纳入此计算。 |
   ^^satisfaction_percentage |string |95.2 |评价为"满意"（4 星或 5 星）的聊天支持 session 百分比。纳入计算的是在指定时间段内完成评价的 session；未评价的 session 不纳入计算。 |
   ^^response_time_mins |string |3.4 |聊天支持 session 的平均首次回复时间（分钟）。纳入计算的是在指定时间段内开始的 session。 |
   ^^conversion_rate |string |66.67 |基于潜在客户总数计算的成功转化客户百分比。 |
   ^^cs_guided_gmv |string |36500 |在您回复客户聊天后 7 天内客户下单产生的收入。 |
   ^^currency |string |USD |`cs_guided_gmv` 使用的 ISO 4217 三字母货币代码。参见 [货币代码](https://www.iso.org/iso-4217-currency-codes.html)。 |

# 响应示例
```json
{"code":0,"data":{"performance":{"support_session_count":15,"response_percentage":"93.4","satisfaction_percentage":"95.2","response_time_mins":"3.4","conversion_rate":"66.67","cs_guided_gmv":"36500","currency":"USD"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
