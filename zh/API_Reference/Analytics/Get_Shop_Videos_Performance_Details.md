# 获取店铺视频表现详情

# 路径：/analytics/202609/shop_videos/batch_performance
# 方法：[GET]
# 功能描述
返回请求 video 的详细 performance 指标。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| video_ids | []int | Y | [7523456789012345678] | 请求 performance 详情的店铺 video ID。 |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-09-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。 |
| 参数名中，"ge"指"大于或等于"（含） |  |  |  |  |
开始日期和结束日期之间的时间范围不得超过 60 天。 |
end_date_lt |string |Y |2024-09-08 |结束日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。
参数名中，"lt"指"小于"（不含）
开始日期和结束日期之间的时间范围不得超过 60 天。 |
granularity |string |N |ALL |数据粒度。
可选值: ALL, 1D
默认值: ALL

* ALL: 汇总
* 1D: 每日 |
   currency |string |N |USD |目前响应中仅支持当地货币。

可选值: USD, LOCAL
默认值: LOCAL

* USD: 美元
* LOCAL: 店铺所在地的当地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop_videos/batch_performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&video_ids=[7523456789012345678]&start_date_ge=2024-09-01&end_date_lt=2024-09-08&granularity=ALL&currency=USD
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-07 | 当地时区中数据已就绪的最新日期（ISO 8601 格式）。 |
| ^videos | []object |  | 请求 video 的 performance 详情。 |
| ^^error | object |  | 当无法返回该 video 的 performance 详情时的错误信息。 |
| ^^^code | string | 300001 | 该 video 的错误码。 |
| ^^^message | string | Invalid video ID. | 该 video 的错误消息。 |
| ^^performance | object |  | 该 video 的 performance 详情。当 video 处理成功时返回。 |
| ^^^intervals | []object |  | 请求时间范围内的区间数据。 |
| ^^^^end_date | string | 2024-09-08 | 区间的结束日期，不含。 |
| ^^^^sales | object |  | 销售 performance 数据。 |
| ^^^^^overall | object |  | 整体销售 performance 数据。 |
| ^^^^^^ctr | string | 0.029 | video 的商品点击量除以所有 video 商品的曝光量。 |
| ^^^^^^customers | int | 12 | 直接从可购物 video 下单的客户总数。 |
| ^^^^^^gmv | object |  | 从可购物 video 直接产生的总商品价值。 |
| ^^^^^^^amount | string | 230.02 | 对应货币的金额。 |
| ^^^^^^^currency | string | USD | ISO 4217 格式的货币代码。 |
| ^^^^^^gpm | object |  | 每 1,000 次 video 观看产生的 GMV。 |
| ^^^^^^^amount | string | 230.02 | 对应货币的金额。 |
| ^^^^^^^currency | string | USD | ISO 4217 格式的货币代码。 |
| ^^^^^^items_sold | int | 22 | 从可购物 video 直接售出的件数。 |
| ^^^^^^product_clicks | int | 21232 | video 的商品点击数。 |
| ^^^^^^product_impressions | int | 32092 | 所有 video 商品的曝光数。 |
| ^^^^start_date | string | 2024-09-01 | 区间的开始日期，含。 |
| ^^^^traffic | object |  | video 的流量 performance。 |
| ^^^^^comments | int | 8 | video 收到的评论数。 |
| ^^^^^likes | int | 2 | video 收到的点赞数。 |
| ^^^^^new_followers | int | 11 | 归因于该 video 的新增粉丝数。 |
| ^^^^^shares | int | 23 | video 被分享的次数。 |
| ^^^^^views | int | 76649 | video 播放量。 |
| ^^^viewer_profile | []object |  | video 的观众画像。 |
| ^^^^age_distribution | []object |  | 按年龄段分布的观众。 |
| ^^^^^age | string | 25-34 | 观众年龄段。可选值：18-24、25-34、35-44、45-54、55+。 |
| ^^^^^percentage | string | 0.293 | 该年龄段观众的占比，以 0 到 1 之间的小数表示。 |
| ^^^^country_distribution | []object |  | 按国家或地区分布的观众。 |
| ^^^^^country_code | string | MY | 观众 TikTok 账号所在的地区。 |
| ^^^^^percentage | string | 0.993 | 来自该国家或地区的观众占比，以 0 到 1 之间的小数表示。 |
| ^^^^gender_distribution | []object |  | 按性别分布的观众。 |
| ^^^^^gender | string | MALE | 观众性别。可选值：MALE、FEMALE。 |
| ^^^^^percentage | string | 0.349 | 该性别观众的占比，以 0 到 1 之间的小数表示。 |
| ^^^^type | string | VIEWERS | 观众画像类型。可选值：NEW_FOLLOWER、VIEWERS。 |
| ^^video | object |  | video 的基本信息。 |
| ^^^duration | int | 10 | video 时长。 |
| ^^^id | string | 7523456789012345678 | video ID。 |
| ^^^play_url | string | `https://example.com/video.mp4` | video 播放 URL。 |
| ^^^thumbnail_url | string | `https://example.com/thumbnail.jpg` | video 缩略图 URL。 |
| ^^^title | string | `Summer collection` | video 标题。 |
| ^^^username | string | `shop_creator` | video 达人的用户名。 |
| ^^^video_post_time | string | 1725148800 | video 发布时间。 |
| ^^video_id | string | 7523456789012345678 | 请求的 video ID。 |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-07","videos":[{"error":{"code":"300001","message":"Invalid video ID."},"performance":{"intervals":[{"end_date":"2024-09-08","sales":{"overall":{"ctr":"0.029","customers":12,"gmv":{"amount":"230.02","currency":"USD"},"gpm":{"amount":"230.02","currency":"USD"},"items_sold":22,"product_clicks":21232,"product_impressions":32092}},"start_date":"2024-09-01","traffic":{"comments":8,"likes":2,"new_followers":11,"shares":23,"views":76649}}],"viewer_profile":[{"age_distribution":[{"age":"25-34","percentage":"0.293"}],"country_distribution":[{"country_code":"MY","percentage":"0.993"}],"gender_distribution":[{"gender":"MALE","percentage":"0.349"}],"type":"VIEWERS"}]},"video":{"duration":10,"id":"7523456789012345678","play_url":"`https://example.com/video.mp4`","thumbnail_url":"`https://example.com/thumbnail.jpg`","title":"`Summer collection`","username":"`shop_creator`","video_post_time":"1725148800"},"video_id":"7523456789012345678"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

