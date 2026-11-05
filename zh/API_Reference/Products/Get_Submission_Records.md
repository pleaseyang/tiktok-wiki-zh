# 获取提交记录

# Path: /product/202604/opportunities/submissions
# Method: [GET]
# 功能描述
Retrieve a paginated list of submission records for the authorized seller, including submission status, review results, and linked opportunity/product information. Useful for tracking submission history and monitoring review outcomes.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| status | string | N | APPROVED | Filter by submission status: PENDING_REVIEW / APPROVED / REJECTED. Leave empty to return all statuses. |
| opportunity_id | string | N | 7123456789012345678 | Filter by specific opportunity ID. |
| product_id | string | N | 7298374612938475620 | Filter by specific product ID. |
| submit_time_ge | int | N | 1775973876 | Return submissions created at or after this Unix timestamp, in seconds. |
| submit_time_lt | int | N | 1776973876 | Filter submissions created before this time, second-level timestamp |
| page_token | string | N | 100 | Pagination token from previous response. Omit for first page. |
| page_size | int | Y | 20 | Number of results per page. Max: 100. Default: 20. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/opportunities/submissions?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&status=APPROVED&opportunity_id=7123456789012345678&product_id=7298374612938475620&submit_time_ge=1775973876&submit_time_lt=1776973876&page_token=100&page_size=20
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | The submission records and pagination information returned for this request. |
| ^^submissions | []object |  | List of submission records. |
| ^^^id | string | 8001234567890123456 | Unique ID of this submission. |
| ^^^opportunity_id | string | 7123456789012345678 | The opportunity ID this submission is linked to. |
| ^^^opportunity_title | string | Women's High-Waist Yoga Leggings | Opportunity title for reference. |
| ^^^status | string | APPROVED | Current status: PENDING_REVIEW / APPROVED / REJECTED |
| ^^^product_id | string | 7298374612938475620 | The submitted product ID. |
| ^^^product_name | string | Premium Yoga Leggings - Black | Product name for reference. |
| ^^^submit_time | int | 1775973876 | The time when the product was submitted, expressed as a Unix timestamp in seconds. |
| ^^^review_time | int | 1775973876 | Review completion timestamp |
| ^^^rejection_reason | string | Product does not match the opportunity category requirements | Rejection reason if status is REJECTED. Null otherwise. |
| ^^^product_orders | int | 121 | The total number of units sold for the product in the last 30 days. |
| ^^^product_pv | int | 320 | The product page view count for the last 30 days. |
| ^^next_page_token | string | 100 | Token for fetching next page. Empty if no more pages. |
| ^^total_count | int | 300 | Total number of matching submissions (approximate). |
# 响应示例
```json
{"code":0,"data":{"data":{"submissions":[{"id":"8001234567890123456","opportunity_id":"7123456789012345678","opportunity_title":"Women's High-Waist Yoga Leggings","status":"APPROVED","product_id":"7298374612938475620","product_name":"Premium Yoga Leggings - Black","submit_time":1775973876,"review_time":1775973876,"rejection_reason":"Product does not match the opportunity category requirements","product_orders":121,"product_pv":320}],"next_page_token":"100","total_count":300}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

