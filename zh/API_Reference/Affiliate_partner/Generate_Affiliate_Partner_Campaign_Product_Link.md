# 生成 Affiliate Partner Campaign Product Link

# Path: /affiliate_partner/202405/campaigns/{campaign_id}/products/{product_id}/promotion_link/generate
# Method: [POST]
# 功能描述
为现有在线 campaign 中的产品生成推广链接。产品必须与该 campaign 关联，并且在 Get Affiliate Partner Campaign Product List 的响应中 `review_status` 设置为 `APPROVED` 或 `PENDING_CLOSED`。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Path Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| campaign_id | string | Y | 7373988288167036678 | campaign 的 ID。 |
| product_id | string | Y | 1730064726487763199 | product 的 ID。 |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Body Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| creator_commission_rate | int | Y | 1000 | 支付给 creator 的 commission 率，以百分之一的百分比（0.01%）为单位。值必须至少为 100（1%），且不得超过 seller 设置的总 commission 率。 |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202405/campaigns/7373988288167036678/products/1730064726487763199/promotion_link/generate?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"creator_commission_rate":1000}
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_promotion_link | string | https://affiliate.tiktok.com/api/v1/share/AIxvOHlaJoKO | 用于产品推广内容的 URL。此 URL 提供给机构，用于与参与合作的 creator 分享。Creator 通过 TikTok App 与粉丝分享此链接。请注意，creator 可以控制在弹出窗口中是否将产品添加到其展示橱窗。 |
# Response Sample
```json
{"code":0,"data":{"product_promotion_link":"https://affiliate.tiktok.com/api/v1/share/AIxvOHlaJoKO"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 16032005 | Campaign not found |
| 16032007 | Permission denied |
| 16032008 | Operation denied |
| 16032009 | Product operation denied, please ensure campaign is under online status. |
| 16032010 | Campaign product not found |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

