# 通过商机提交产品

# Path: /product/202604/opportunities/{opportunity_id}/submit
# Method: [POST]
# 功能描述
Submit an existing product as a response to a specific opportunity lead. The product must belong to the authorized shop and be in `ACTIVATE` status. It will be linked to the opportunity and enter the standard submission review flow.
If you need a new local product, call the [Create Product API](https://partner.tiktokshop.com/docv2/page/create-product-202309) with `save_mode=LISTING`, use the returned `data.product_id`, and wait until the product reaches `ACTIVATE`. A product saved with `save_mode=AS_DRAFT` is not yet eligible. For a global seller that has not migrated to local replication, first call the [Create Global Product API](https://partner.tiktokshop.com/docv2/page/6509de61bace3e02b7489cba) to get a `global_product_id`, then call the [Publish Global Product API](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309). From `data.products`, select the local product `id` for the authorized shop and wait until that product reaches `ACTIVATE` before submitting it here.
After submission, use the [Get Submission Records API](https://partner.tiktokshop.com/docv2/page/get-submission-records-202604) and filter by `opportunity_id` or `product_id` to track the review outcome.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| opportunity_id | string | Y | 7123456789012345678 | The opportunity lead to respond to. This API does not support opportunities whose `opportunity_type` is `CATEGORY`. |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 7298374612938475620 | The TikTok Shop product ID to submit. Must be in ACTIVATE status. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/opportunities/7123456789012345678/submit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_id":"7298374612938475620"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^submission | object |  | The submission record that links the product to the opportunity. |
| ^^id | string | 8001234567890123456 | Unique ID of this submission record. Use for tracking review status. |
| ^^opportunity_id | string | 7123456789012345678 | The opportunity ID this submission is linked to. |
| ^^product_id | string | 7298374612938475620 | The submitted product ID. |
| ^^status | string | PENDING_REVIEW | APPROVED, UNDER_REVIEW, REJECTED are supported. |
| Initial submission status: PENDING_REVIEW. |  |  |  |
| ^^submit_time | int | 1775979270 | The submission time as a Unix timestamp in seconds (UTC). |
| ^^rejection_reason | string | The submitted product does not match the opportunity | the reason when the status is REJECTED |
# 响应示例
```json
{"code":0,"data":{"submission":{"id":"8001234567890123456","opportunity_id":"7123456789012345678","product_id":"7298374612938475620","status":"PENDING_REVIEW","submit_time":1775979270,"rejection_reason":"The submitted product does not match the opportunity"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

