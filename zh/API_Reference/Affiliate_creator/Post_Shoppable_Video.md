# 发布可购物视频

# 路径：/affiliate_creator/202603/videos
# 方法：[POST]
# 功能描述
使用此 API 提交可购物视频进行发布。提交成功后，将返回的视频 ID 作为 `video_id` 路径参数传给 Get Shoppable Video Status (`GET /affiliate_creator/202509/videos/{video_id}/status`)，以获取发布状态：`PROCESSING`、`SUCCESS` 或 `FAIL`。如果状态为 `PROCESSING`，请稍后再次调用状态 API 以检查最终状态。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| video_info | object | Y |  | Video information |
| ^file_id | string | Y | v12d00gd0024d3nfqr7og65 | 由上传可购物视频文件 (`POST /affiliate_creator/202505/videos/video_files`) 返回的视频文件 ID。 |
| ^title | string | Y | Sample video title | 视频文案。 |
| 最大长度为 2200 个 UTF-16 runes。 |  |  |  |  |
| 若未指定，工单帖子将不包含任何字幕。 |  |  |  |  |
| ^cover_uri | string | N | v12d00gd0024d3nfqr7og65oooiuuyy | 由 Upload Shoppable Photo File（`POST /affiliate_creator/202511/photos/photo_files`）返回的视频封面图片 URI。 |
| ^cover_timestamp_ms | int | N | 1000 | 输入参数为时间戳，用于指定视频中的特定时刻。该时间戳处的帧将用作视频封面。如果 cover_uri 和 cover_timestamp_ms 都未提供，封面将默认使用所上传视频的第一帧。cover_uri 或 cover_timestamp_ms 只能提供其中一个。如果两个参数都传入，则以 cover_uri 为准。 |
| ^music_id | string | N | 717294069642063456 | 视频背景音乐的音乐 ID。可从 Search Music（`GET /affiliate_creator/202602/music/search`）获取。如果未提供，视频将不关联任何音乐。 |
| product_link_info | object | Y |  | 商品链接信息 |
| ^product_id | string | Y | 17294069642063424 | 要绑定到视频的商品 ID。可从 Get Shop Products（`GET /affiliate_creator/202509/shop_products`）或 Get 橱窗 Products（`GET /affiliate_creator/202405/showcases/products`）获取。 |
| ^title | string | Y | 样品商品锚点标题 | 商品锚点上显示的标题。锚点标题应少于 30 个字符。标题可能因标点、表情符号或不当用语被拒绝。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202603/videos?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"video_info":{"file_id":"v12d00gd0024d3nfqr7og65","title":"Sample video title","cover_uri":"v12d00gd0024d3nfqr7og65oooiuuyy","cover_timestamp_ms":1000,"music_id":"717294069642063456"},"product_link_info":{"product_id":"17294069642063424","title":"Sample product anchor title"}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^video | object |  | 已提交的可购物视频信息。 |
| ^^id | string | 7548431509997292816 | 视频 ID, 使用此 ID 查询视频发布状态。 |
# 响应示例
```json
{"code":0,"data":{"video":{"id":"7548431509997292816"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16011007 | Product link title should be no longer than 30 characters. |
| 16011009 | Product link title contains offensive language. |
| 16011069 | Product link title contains punctuation or emoji. |
| 38007001 | System Error |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 170001002 | Creator TikTok Shop permission check failed. |
| 170001003 | Creator Tiktok Shop permission temporarily banned. |
| 170001004 | Creator TikTok Shop permission is permanently banned. |
| 170001005 | Creator terms of service not signed. Please contact TikTok for more details. |
| 170001006 | GKA terms not signed. Please try again after signing GKA term. |
| 170001007 | Creator did not sign the EU data share agreement. |
| 170001008 | Creator Age verification failed. Please verify age first. |
| 170001009 | 该商品属于不支持的类目。 |
| 170001010 | The commission plan gets failed or rejected. |
| 170001011 | The product doesn't exist. |
| 170001012 | The product is not available. |
| 170001013 | Showcase SPU exceeds limit. |
| 170001014 | Blocked by spam check. |
| 170001015 | Blocked by TikTok Shop risk control. |
| 170001018 | Get creator pay account error. Please verify the pay account first. |
| 170001020 | You have exceeded the frequency to post EC short videos. Please take a rest. |
| 170001024 | cover_timestamp_ms must be a non-negative integer within the video duration. |
| 170001025 | cover_timestamp_ms exceeds the video duration. |
| 170001030 | Creator account banned. Please contact TikTok agent for your account. |
| 170001031 | Creator forbidden to post content. |
| 170001040 | Please use valid video file id to post TikTok Shop short video. |
| 170001050 | Getting errors during video posting workflow. Please try again or contact TikTok. |
| 170001060 | Posting quota exceeded: the creator is under violation control, resulting in a reduced posting limit. |
| 170001061 | Posting quota exceeded: creator is in the newbie period. |
| 170001062 | Posting quota exceeded: platform-level posting limit reached. |
| 170001063 | The product you added only supports auction sales and cannot be used in shoppable videos or Carousels. |

