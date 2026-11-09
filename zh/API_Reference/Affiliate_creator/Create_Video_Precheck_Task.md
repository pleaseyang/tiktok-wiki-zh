# 创建视频预审任务

# 路径：/affiliate_creator/202511/videos/precheck_task
# 方法：[POST]
# 功能描述
使用此接口创建一个任务，用于检查视频及其可购物内容锚点是否存在违规。若任务创建成功，响应将返回任务 ID。

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
| ^file_id | string | Y | v12d00gd0024d3nfqr7og65 | 来自 [Upload Shoppable Video File](https://api/affiliate_creator/202505/videos/video_files) 的视频 file_id |
| product_link_info | object | Y |  | 商品链接信息 |
| ^product_id | string | Y | 17294069642063424 | 使用 product_id 将商品与视频绑定。 |
| 来自 [Get Shop Products](https://api/affiliate_creator/202509/shop_products) 或 [Get Showcase Products](https://api/affiliate_creator/202405/showcases/products) 的 product_id |  |  |  |  |
| ^title | string | Y | 样品商品锚点标题 | 商品锚点上显示的标题。锚点标题应少于 30 个字符。标题可能因标点、表情符号或不当用语被拒绝。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202511/videos/precheck_task?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"video_info":{"file_id":"v12d00gd0024d3nfqr7og65"},"product_link_info":{"product_id":"17294069642063424","title":"Sample product anchor title"}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^precheck | object |  | 所创建的视频内容预检任务的信息。 |
| ^^task_id | string | 1123123123 | 所创建视频预检任务的 ID。将此值作为 `task_id` 路径参数传入 `GET /affiliate_creator/202511/videos/precheck_tasks/{task_id}` 以获取结果。 |
# 响应示例
```json
{"code":0,"data":{"precheck":{"task_id":"1123123123"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16011007 | Product link title should be no longer than 30 characters. |
| 16011009 | Product link title contains offensive language. |
| 16011069 | Product link title contains punctuation or emoji. |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 170001002 | Creator TikTok Shop permission check failed. |
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
| 170001019 | The user has exceeded allocated daily quota for precheck resource |

