# 获取 Affiliate Campaign Creator 产品内容统计

# Path: /affiliate_partner/202508/campaigns/{campaign_id}/products/{product_id}/creator/{creator_temp_id}/content/statistics
# Method: [GET]
# 功能描述
获取与 affiliate campaign 产品关联的 creator 视频或直播间内容的 performance 统计数据。

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
| campaign_id | string | Y | 123 | campaign 标识符。 |
| product_id | string | Y | 123 | product 标识符。 |
| creator_temp_id | string | Y | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| affiliate_product_id | string | Y | 123456789 | 用于筛选返回内容统计数据的 affiliate product 标识符。 |
| content_type | string | N | VIDEO | 内容类型。使用 `VIDEO` 表示视频内容，使用 `LIVE_ROOM` 表示直播间内容。 |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202508/campaigns/123/products/123/creator/uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg/content/statistics?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&affiliate_product_id=123456789&content_type=VIDEO
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^creator_content_statistics | []object |  | 表示关联 creator 内容统计数据的对象列表。 |
| ^^content_type | string | VIDEO | 内容类型：`VIDEO` 表示视频内容，`LIVE_ROOM` 表示直播间内容。 |
| ^^cover_img_url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 | TikTok CDN 中直播间封面图片的 URL。视频内容没有此值。 |
| ^^source_url | string | https://www.tiktok.com/@cbseveningnews/video/7458098283332767006?q=Victor%20Shaw%20Dies%20In%20Fire%20Rescue%20Attempt&t=1736545359958 | TikTok 公开网站上可以播放直播间视频的 URL。当 content_type == VIDEO 时，值为源视频的 URL；当 content_type == LIVE_ROOM 时，值为可以回放直播录屏的 URL。 |
|  |  |  |  |
| ^^view_count | string | 1 | 直播间或视频的公开观看次数。 |
| ^^like_count | string | 1 | 与直播间或视频关联的 TikTok 用户点赞数。 |
| ^^comment_num | string | 0 | 与直播间或视频关联的 TikTok 用户评论数。 |
| ^^paid_order_num | string | 0 | 与直播间或视频关联的已付款订单总数。 |
| ^^paid_amount | string | 0 | 与直播间或视频关联的产品订单总金额。 |
| ^^linked_tiktok_video | string | http://xxx.tiktok.com/xxxx | TikTok 网站上视频的友好 URL。 |
| ^^published_date | string | 2024-11-13 | 当 content_type == VIDEO 时，此为视频发布日期；当 content_type == LIVE_ROOM 时，此为直播开始日期。值格式为 YYYY_MM_DD。 |
|  |  |  |  |
| ^^content_end_date | string | 2024-11-13 | 当 content_type == VIDEO 时，此字段为 None；当 content_type == LIVE_ROOM 时，此为直播结束日期。值格式为 YYYY_MM_DD。 |
|  |  |  |  |
# Response Sample
```json
{"code":0,"data":{"creator_content_statistics":[{"content_type":"VIDEO","cover_img_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","source_url":"https://www.tiktok.com/@cbseveningnews/video/7458098283332767006?q=Victor%20Shaw%20Dies%20In%20Fire%20Rescue%20Attempt\u0026t=1736545359958","view_count":"1","like_count":"1","comment_num":"0","paid_order_num":"0","paid_amount":"0","linked_tiktok_video":"http://xxx.tiktok.com/xxxx","published_date":"2024-11-13","content_end_date":"2024-11-13"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

