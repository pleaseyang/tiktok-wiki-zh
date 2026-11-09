# 获取 Open Collaboration 达人内容详情

# 路径：/affiliate_seller/202508/open_collaborations/creator_content_details
# 方法：[GET]
# 功能描述
此 API 用于获取 open collaboration 中达人的内容详情，包括视频和直播数据。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | b2Zmc2V0PTAK | 分页令牌。首次请求时省略此参数或传入空字符串。后续请求请传入上一次响应返回的 `next_page_token`，并复用相同的 `product_id` 和 `page_size`。 |
| page_size | int | Y | 50 | "page_size" 的值必须大于 0 且小于或等于 100。 |
| product_id | string | Y | 1730076583746441639 | 需要查询的商品 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/open_collaborations/creator_content_details?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=b2Zmc2V0PTAK&page_size=50&product_id=1730076583746441639
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTEw | 下一页的分页 token。 Pass this value as `page_token` in the next request. An empty token means there are no more results。 |
| ^total_count | int | 1 | 符合所有输入搜索条件的达人总数。 |
| ^creator_content_details | []object |  | 指定商品的达人资料、内容计数和推广详情。 |
| ^^creator_profile | object |  | 达人的资料详情。 |
| ^^^username | string | example_creator | 达人的用户名。 |
| ^^^nickname | string | nickname | 达人的昵称。 |
| ^^^follower_count | int | 10023 | 达人的粉丝数。 |
| ^^^avatar | object |  | 达人的头像详情。 |
| ^^^^url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 | 达人头像的 url。 |
| ^^^creator_open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
| ^^video_count | int | 101 | 此字段表示达人发布的视频数量。 |
| ^^live_count | int | 2 | 此字段表示达人发布的直播数量。 |
| ^^promotion_status | string | NORMAL | 达人的推广状态。 |
| Field values: |  |  |  |

* NORMAL: 当达人正常推广时，状态恢复为 NORMAL
* TERMINATING：当卖家要求达人终止推广时，状态将返回 TERMINATING，表示达人的推广权限即将到期。 |
   ^^promotion_end_time |int |1734682697 |达人推广的结束时间。 |
   ^product |object | |商品详情。 |
   ^^id |string |1734823553672710512 |商品的唯一 ID。 |
   ^^image_url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 |商品图片 URL。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTEw","total_count":1,"creator_content_details":[{"creator_profile":{"username":"example_creator","nickname":"nickname","follower_count":10023,"avatar":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499"},"creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"},"video_count":101,"live_count":2,"promotion_status":"NORMAL","promotion_end_time":1734682697}],"product":{"id":"1734823553672710512","image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

