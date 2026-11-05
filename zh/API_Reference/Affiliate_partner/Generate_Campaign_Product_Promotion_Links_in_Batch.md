# 批量生成 Campaign Product 推广链接

# Path: /affiliate_partner/202505/campaigns/{campaign_id}/products/promotion_links/generate_batch
# Method: [POST]
# 功能描述
为在线 campaign 中的多个产品批量生成推广链接。对于 OPS 或 seller 发起的 campaign，请使用 partner 加入 campaign 后创建的已加入 campaign ID，而不是原始 campaign ID。

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
| campaign_id | string | Y | 7362840009596339923 | campaign 的 ID |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | N | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3= | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Body Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_ids | []string | N | [7362840009596339971,7362840009596339923] | product ID 列表。最大长度为 50。 |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202505/campaigns/7362840009596339923/products/promotion_links/generate_batch?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":[7362840009596340000,7362840009596340000]}
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_promotion_links | []object |  | 成功生成推广链接的产品列表。 |
| ^^product_id | string | 7362840009596339971 | 要推广的产品 ID。 |
| ^^link | string | https://affiliate.tiktok.com/api/v1/share/AIxvOHlaJoKO | 这是产品推广链接，机构可以与合作的 creator 分享。Creator 可以将此链接复制/粘贴到网络浏览器中。Creator 将被重定向到 TikTok app 中的添加产品链接页面。Creator 可以在弹出窗口中决定是否将产品添加到其展示橱窗。 |
| ^failed_product_ids | []string | [7362840009596339923] | 推广链接生成失败的产品列表。 |
# Response Sample
```json
{"code":0,"data":{"product_promotion_links":[{"product_id":"7362840009596339971","link":"https://affiliate.tiktok.com/api/v1/share/AIxvOHlaJoKO"}],"failed_product_ids":[7362840009596340000]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

