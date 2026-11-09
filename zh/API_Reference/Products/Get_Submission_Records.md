# 获取提交记录

# 路径：/product/202604/opportunities/submissions
# 方法：[GET]
# 功能描述
获取已授权卖家的分页提交记录列表，包括提交状态、审核结果以及关联的商机/商品信息。可用于跟踪提交历史并监控审核结果。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| status | string | N | APPROVED | 按提交状态筛选：PENDING_REVIEW / APPROVED / REJECTED。留空则返回所有状态。 |
| opportunity_id | string | N | 7123456789012345678 | 按特定机会 ID 筛选。 |
| product_id | string | N | 7298374612938475620 | 按特定商品 ID 筛选。 |
| submit_time_ge | int | N | 1775973876 | 返回在此 Unix 时间戳之时或之后创建的提交，以秒为单位。 |
| submit_time_lt | int | N | 1776973876 | 筛选在此时间之前创建的提交，秒级时间戳 |
| page_token | string | N | 100 | 来自上一次响应的分页令牌。请求第一页时省略。 |
| page_size | int | Y | 20 | 每页结果数。最大值: 100。默认值: 20。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/opportunities/submissions?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&status=APPROVED&opportunity_id=7123456789012345678&product_id=7298374612938475620&submit_time_ge=1775973876&submit_time_lt=1776973876&page_token=100&page_size=20
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | 此请求返回的提交记录和分页信息。 |
| ^^submissions | []object |  | 提交记录列表。 |
| ^^^id | string | 8001234567890123456 | 此提交的唯一 ID。 |
| ^^^opportunity_id | string | 7123456789012345678 | 此提交所关联的机会 ID。 |
| ^^^opportunity_title | string | Women's High-Waist Yoga Leggings | 供参考的机会标题。 |
| ^^^status | string | APPROVED | 当前状态：PENDING_REVIEW / APPROVED / REJECTED |
| ^^^product_id | string | 7298374612938475620 | 提交的商品 ID。 |
| ^^^product_name | string | Premium Yoga Leggings - Black | 供参考的商品名称。 |
| ^^^submit_time | int | 1775973876 | 商品提交的时间，以秒为单位的 Unix 时间戳表示。 |
| ^^^review_time | int | 1775973876 | 审核完成时间戳 |
| ^^^rejection_reason | string | 商品与机会类目要求不符 | 状态为 REJECTED 时的拒绝原因。否则为 Null。 |
| ^^^product_orders | int | 121 | 该商品过去 30 天售出的总件数。 |
| ^^^product_pv | int | 320 | 过去 30 天的商品页面浏览量。 |
| ^^next_page_token | string | 100 | 用于获取下一页的令牌。如果没有更多页面则为空。 |
| ^^total_count | int | 300 | 匹配的提交总数 (近似值)。 |
# 响应示例
```json
{"code":0,"data":{"data":{"submissions":[{"id":"8001234567890123456","opportunity_id":"7123456789012345678","opportunity_title":"Women's High-Waist Yoga Leggings","status":"APPROVED","product_id":"7298374612938475620","product_name":"Premium Yoga Leggings - Black","submit_time":1775973876,"review_time":1775973876,"rejection_reason":"Product does not match the opportunity category requirements","product_orders":121,"product_pv":320}],"next_page_token":"100","total_count":300}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

