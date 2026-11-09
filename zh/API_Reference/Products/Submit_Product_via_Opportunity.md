# 通过商机提交商品

# 路径：/product/202604/opportunities/{opportunity_id}/submit
# 方法：[POST]
# 功能描述
提交一个已有商品作为对特定商机线索的响应。该商品必须属于已授权店铺且处于 `ACTIVATE` 状态。它将关联到该商机并进入标准的提交审核流程。
如果需要新的本地商品，请使用 `save_mode=LISTING` 调用 [Create Product API](https://partner.tiktokshop.com/docv2/page/create-product-202309)，使用返回的 `data.product_id`，并等待商品达到 `ACTIVATE`。以 `save_mode=AS_DRAFT` 保存的商品尚不符合条件。对于尚未迁移到本地复制的全球卖家，请先调用 [Create Global Product API](https://partner.tiktokshop.com/docv2/page/6509de61bace3e02b7489cba) 获取 `global_product_id`，然后调用 [Publish Global Product API](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309)。从 `data.products` 中为已授权店铺选择本地商品 `id`，并等待该商品达到 `ACTIVATE` 后再在此处提交。
提交后，使用 [Get Submission Records API](https://partner.tiktokshop.com/docv2/page/get-submission-records-202604) 并按 `opportunity_id` 或 `product_id` 筛选，以跟踪审核结果。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| opportunity_id | string | Y | 7123456789012345678 | 要响应的商机线索. 此接口不支持 `opportunity_type` 为 `CATEGORY` 的商机。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 7298374612938475620 | 要提交的 TikTok Shop 商品 ID。必须处于 ACTIVATE 状态。 |
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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^submission | object |  | 将商品与商机关联的提交记录。 |
| ^^id | string | 8001234567890123456 | 该提交记录的唯一 ID。用于跟踪审核状态。 |
| ^^opportunity_id | string | 7123456789012345678 | 此提交所关联的机会 ID。 |
| ^^product_id | string | 7298374612938475620 | 提交的商品 ID。 |
| ^^status | string | PENDING_REVIEW | APPROVED, UNDER_REVIEW, REJECTED 均受支持。 |
| 初始提交状态：PENDING_REVIEW。 |  |  |  |
| ^^submit_time | int | 1775979270 | 提交时间为以秒为单位的 Unix 时间戳 (UTC)。 |
| ^^rejection_reason | string | The submitted product does not match the opportunity | 状态为 REJECTED 时的原因 |
# 响应示例
```json
{"code":0,"data":{"submission":{"id":"8001234567890123456","opportunity_id":"7123456789012345678","product_id":"7298374612938475620","status":"PENDING_REVIEW","submit_time":1775979270,"rejection_reason":"The submitted product does not match the opportunity"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

