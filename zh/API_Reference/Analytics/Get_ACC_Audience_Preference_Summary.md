# 获取 ACC 受众偏好摘要

# 路径：/analytics/202610/acc/preferences/summary
# 方法：[GET]
# 功能描述
获取所选品牌、受众细分、范围和时间窗口的 ACC 商品、直播、video 和图文帖子受众偏好摘要。
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
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| brand_id | string | Y | 1000001 | 要分析的授权品牌 ID。使用当前店铺的同一 Get ACC Brands 记录中的 brand_id 和 industry_id。不能为空。 |
| industry_id | string | Y | 9000001 | 用于确定可用报告日期的行业 ID。使用与 brand_id 相同的 Get ACC Brands 记录中的 industry_id。不能为空。 |
| date | string | N | 2026-09-20 | 报告窗口的截止日期（含），格式为 YYYY-MM-DD（UTC）。如果省略或为空，则使用最新可用日期。trend_days 选择的整个窗口必须介于 earliest_available_date 和 latest_available_date 之间。 |
| trend_days | int | N | 30 | 报告窗口中的日历天数（含截止日期）。支持的值：7、14、30。省略或设为 0 时默认为 30。 |
| audience_type | string | Y | CONVERSION | 要分析的受众细分。支持的值：SHOP_NON_EXPOSED、SHOP_CLICKED_NOT_PURCHASED、CONVERSION、NEW_CONVERSION、REPEAT_CONVERSION、DTC_NEW_CONVERSION、DTC_REPEAT_CONVERSION。细分定义：SHOP_NON_EXPOSED 表示未接触过店铺的人群；SHOP_CLICKED_NOT_PURCHASED 表示点击了店铺但未购买的人群；/CONVERSION 表示完成购买的人群；NEW_CONVERSION 表示首次购买店铺商品的人群；REPEAT_CONVERSION 表示复购人群。DTC_NEW_CONVERSION 和 DTC_REPEAT_CONVERSION 选择相应的 DTC 新转化和复购队列。偏好 API 不支持 ACC、AWARENESS、CONSIDERATION 和 DRC 前缀的值。 |
| scope | string | N | MY_SHOP | 偏好数据的范围。支持的值：MY_SHOP 表示店铺级别数据；MARKET 表示市场级别数据。省略或为空时默认为 MY_SHOP。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/preferences/summary?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&brand_id=1000001&industry_id=9000001&date=2026-09-20&trend_days=30&audience_type=CONVERSION&scope=MY_SHOP
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^audience_type | string | CONVERSION | 用于摘要的受众细分，以大写的 audience_type 值返回。 |
| ^channel_summaries | []object |  | 按以下顺序排列的渠道摘要：PRODUCT、LIVE、VIDEO、PHOTO。当没有可用项目时，每个摘要中的列表可以为空。这些是结构化的 Top 3 结果，而非生成的叙述文本。当底层查询失败时列表也可能为空；仅凭空列表不能确定该渠道没有活动。 |
| ^^channel | string | PRODUCT | 此摘要代表的渠道：PRODUCT、LIVE、VIDEO 或 PHOTO。 |
| ^^live_top_items | []object |  | 所选受众、范围和报告窗口内 GMV 最高的最多 3 场直播，按 GMV 降序排列。有数据时填充在 LIVE 汇总中。 |
| ^^^live_room_type | string | demo_room_type | 直播间类目标签。 |
| ^^^live_start_time | string | 2026-09-18 | 直播开始日期，采用 YYYY-MM-DD 格式 (UTC)。 |
| ^^^live_type | string | label1 | 直播类型标签。 |
| ^^^replay_url | string | https://example.com/live/1000000000000000005/replay | 直播回放的 URL。 |
| ^^^room_id | string | 1000000000000000005 | 直播间的 ID。 |
| ^^^room_image_url | string | https://example.com/images/live-001.jpg | 直播封面图片的 URL。 |
| ^^^room_title | string | Demo LIVE Session | 直播标题。 |
| ^^^seller_own_id | string | 1000000000000000004 | 内容作者的 ID。 |
| ^^^seller_own_name | string | Demo Creator | 内容作者的显示名称。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^live_type_top_items | []object |  | 所选受众、范围和报告窗口内 GMV 最高的最多 3 种直播类型，按 GMV 降序排列。有数据时填充在 LIVE 汇总中。 |
| ^^^live_type | string | label1 | 稳定的 LIVE 类型标识符，例如 label1。在 Get ACC Audience Preference List 中将此标识符用作 factor_id，用于 entity_type=LIVE；本地化展示名称不是查询取值。 |
| ^^^live_type_name | string | 稳定、不抖动的画面 | LIVE 因子的本地化显示名称。请使用 live_type 而非此显示名称，作为筛选 LIVE 偏好的稳定标识符。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^photo_top_items | []object |  | 所选受众、范围和报告窗口内 GMV 最高的最多 3 条图文帖子，按 GMV 降序排列。有数据时填充在 PHOTO 汇总中。 |
| ^^^image_urls | []string | ["https://example.com/images/photo-001.jpg"] | 照片帖子中图片的 URL。当没有其他可用的图片 URL 时，可以返回封面图片 URL。 |
| ^^^linked_products | []object |  | 关联到该图文帖的商品，如有提供。 |
| ^^^^product_id | string | 1000000000000000001 | 商品的 ID。 |
| ^^^^product_image_url | string | https://example.com/images/product-001.jpg | 商品图片的 URL。 |
| ^^^^product_name | string | Demo Makeup Set | 商品名称。 |
| ^^^^product_scan_url | string | https://example.com/products/1000000000000000001 | 与关联商品对应的 URL。 |
| ^^^photo_id | string | 1000000000000000007 | 照片帖子的 ID。 |
| ^^^photo_title | string | Demo Product Photo Post | 照片帖子的标题。 |
| ^^^post_images | []object |  | 照片帖子中图片的图片元数据。 |
| ^^^^color | string | #FFFFFF | 照片帖子中图片的图片元数据的颜色。 |
| ^^^^height | int | 1080 | 照片帖子中图片的图片元数据的高度。 |
| ^^^^mimetype | string | image/jpeg | 图片的 MIME 类型。 |
| ^^^^size | string | 204800 | 照片帖子中图片的图片元数据的大小。 |
| ^^^^thumb_uri | string | demo/photo-001-thumb | 标识图片缩略图的资源 URI。 |
| ^^^^thumb_url_list | []string | ["https://example.com/images/photo-001-thumb.jpg"] | 图片缩略图的 URL。 |
| ^^^^tint_color | string | #F0F0F0 | 照片帖子中图片的图片元数据的色调颜色。 |
| ^^^^uri | string | demo/photo-001 | 标识图片的资源 URI。 |
| ^^^^url_list | []string | ["https://example.com/images/photo-001.jpg"] | 图片的 URL。 |
| ^^^^width | int | 1080 | 照片帖子中图片的图片元数据的宽度。 |
| ^^^publish_time | string | 2026-09-18 | 图文帖的发布日期，采用 YYYY-MM-DD 格式 (UTC)。 |
| ^^^seller_own_avatar_url | string | https://example.com/images/creator-001.png | 内容达人头像的 URL。 |
| ^^^seller_own_id | string | 1000000000000000004 | 内容作者的 ID。 |
| ^^^seller_own_name | string | Demo Creator | 内容作者的显示名称。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^product_category_top_items | []object |  | PRODUCT 汇总中 GMV 最高的最多 3 个二级商品类目，按 GMV 降序排列。每个类目包含其可用的三级子类目；3 个类目的上限适用于二级条目。 |
| ^^^category_id | string | 848648 | 此二级商品类目的 ID。 |
| ^^^category_name | string | Makeup | 此二级商品类目的名称。 |
| ^^^children | []object |  | 属于此二级类目的三级商品类目。product_category_top_items 的 top-3 限制不单独限制此子列表。 |
| ^^^^category_id | string | 601529 | 此三级商品类目的 ID。 |
| ^^^^category_name | string | Makeup Sets | 此三级商品类目的名称。 |
| ^^^^level | int | 3 | 商品类目层级。此节点为第 3 级。 |
| ^^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^^level | int | 2 | 商品类目层级。此节点为第 2 级。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^product_top_items | []object |  | 所选受众、范围和报告窗口内 GMV 最高的最多 3 个商品，按 GMV 降序排列。有数据时填充在 PRODUCT 汇总中。 |
| ^^^l2_category_id | string | 848648 | 商品的二级类目 ID。 |
| ^^^l2_category_name | string | Makeup | 商品的二级类目名称。 |
| ^^^l3_category_id | string | 601529 | 商品的三级类目 ID。 |
| ^^^l3_category_name | string | Makeup Sets | 商品的三级类目名称。 |
| ^^^product_id | string | 1000000000000000001 | 商品的 ID。 |
| ^^^product_image_url | string | https://example.com/images/product-001.jpg | 商品图片的 URL。 |
| ^^^product_name | string | Demo Makeup Set | 商品名称。 |
| ^^^product_scan_url | string | https://example.com/products/1000000000000000001 | 商品的分享链接。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^seller_own_top_items | []object |  | 渠道的内容达人偏好摘要。此列表可以为空。 |
| ^^^content_type | string | VIDEO | 与此内容达人摘要关联的内容分类。 |
| ^^^seller_own_avatar_url | string | https://example.com/images/creator-001.png | 内容达人头像的 URL。 |
| ^^^seller_own_id | string | 1000000000000000004 | 内容作者的 ID。 |
| ^^^seller_own_name | string | Demo Creator | 内容作者的显示名称。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 与此内容达人摘要关联的商品交易总额 (GMV) 区间。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^^sub_channel | string | VIDEO | 与此内容达人摘要关联的渠道。 |
| ^^video_top_items | []object |  | 所选受众、范围和报告窗口内 GMV 最高的最多 3 个视频，按 GMV 降序排列。有数据时填充在 VIDEO 汇总中。 |
| ^^^linked_products | []object |  | 关联到该视频的商品，如有提供。 |
| ^^^^product_id | string | 1000000000000000001 | 商品的 ID。 |
| ^^^^product_image_url | string | https://example.com/images/product-001.jpg | 商品图片的 URL。 |
| ^^^^product_name | string | Demo Makeup Set | 商品名称。 |
| ^^^^product_scan_url | string | https://example.com/products/1000000000000000001 | 与关联商品对应的 URL。 |
| ^^^publish_time | string | 2026-09-18 | 视频的发布日期，采用 YYYY-MM-DD 格式 (UTC)。 |
| ^^^seller_own_avatar_url | string | https://example.com/images/creator-001.png | 内容达人头像的 URL。 |
| ^^^seller_own_id | string | 1000000000000000004 | 内容作者的 ID。 |
| ^^^seller_own_name | string | Demo Creator | 内容作者的显示名称。 |
| ^^^stats | object |  | 所选统计周期内该商品的受众偏好指标。 |
| ^^^^customers | string | 4210 | 所选报告时间窗口内该商品的举报客户数，以字符串形式表示。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 该商品的商品交易总额（GMV）格式化区间。正值以 50 为一档，用 " ~ " 分隔；非正值显示为格式化后的零。货币格式在可用时使用店铺的地区和货币信息。 |
| ^^^^orders | string | 8566 | 所选报告时间窗口内该商品的举报订单数，以字符串形式表示。 |
| ^^^video_cover_url | string | https://example.com/images/video-001.jpg | 视频封面图片的 URL。 |
| ^^^video_id | string | 1000000000000000006 | 视频的 ID。 |
| ^^^video_infos | []object |  | 可用的视频文件表示及其播放元数据。 |
| ^^^^backup_url | string | https://example.com/media/video-001-backup.mp4 | 此视频表示的备用播放 URL。 |
| ^^^^bitrate | int | 1200000 | 此视频表示的比特率。 |
| ^^^^file_hash | string | 00000000000000000000000000000000 | 标识此视频文件的哈希。 |
| ^^^^format | string | mp4 | 此视频表示的文件格式。 |
| ^^^^height | int | 720 | 此视频表示的高度格式。 |
| ^^^^main_url | string | https://example.com/media/video-001.mp4 | 此视频表示的主播放 URL。 |
| ^^^^size | int | 10485760 | 此视频表示的大小。 |
| ^^^^url_expire | int | 1793505600 | 此视频表示的 Url 过期时间戳格式。 |
| ^^^^video_quality | string | 720p | 此视频表示的质量标签。 |
| ^^^^width | int | 1280 | 此视频表示的宽度。 |
| ^^^video_title | string | Demo Product Video | 视频的标题。 |
| ^earliest_available_date | string | 2026-08-21 | 所选店铺、品牌和行业的最早可用日期，格式为 YYYY-MM-DD（UTC）。 |
| ^end_date | string | 2026-09-20 | 报告窗口的截止日期（含），格式为 YYYY-MM-DD（UTC）。 |
| ^latest_available_date | string | 2026-09-20 | 所选店铺、品牌和行业的最新可用日期，格式为 YYYY-MM-DD（UTC）。 |
| ^scope | string | MY_SHOP | 摘要使用的范围：MY_SHOP 表示店铺级别数据，MARKET 表示市场级别数据。 |
| ^start_date | string | 2026-08-22 | 报告窗口的开始日期（含），格式为 YYYY-MM-DD（UTC）。 |
# 响应示例
```json
{"code":0,"data":{"audience_type":"CONVERSION","channel_summaries":[{"channel":"PRODUCT","live_top_items":[{"live_room_type":"demo_room_type","live_start_time":"2026-09-18","live_type":"label1","replay_url":"https://example.com/live/1000000000000000005/replay","room_id":"1000000000000000005","room_image_url":"https://example.com/images/live-001.jpg","room_title":"Demo LIVE Session","seller_own_id":"1000000000000000004","seller_own_name":"Demo Creator","stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"live_type_top_items":[{"live_type":"label1","live_type_name":"Stable, non-shaky image","stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"photo_top_items":[{"image_urls":["https://example.com/images/photo-001.jpg"],"linked_products":[{"product_id":"1000000000000000001","product_image_url":"https://example.com/images/product-001.jpg","product_name":"Demo Makeup Set","product_scan_url":"https://example.com/products/1000000000000000001"}],"photo_id":"1000000000000000007","photo_title":"Demo Product Photo Post","post_images":[{"color":"#FFFFFF","height":1080,"mimetype":"image/jpeg","size":"204800","thumb_uri":"demo/photo-001-thumb","thumb_url_list":["https://example.com/images/photo-001-thumb.jpg"],"tint_color":"#F0F0F0","uri":"demo/photo-001","url_list":["https://example.com/images/photo-001.jpg"],"width":1080}],"publish_time":"2026-09-18","seller_own_avatar_url":"https://example.com/images/creator-001.png","seller_own_id":"1000000000000000004","seller_own_name":"Demo Creator","stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"product_category_top_items":[{"category_id":"848648","category_name":"Makeup","children":[{"category_id":"601529","category_name":"Makeup Sets","level":3,"stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"level":2,"stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"product_top_items":[{"l2_category_id":"848648","l2_category_name":"Makeup","l3_category_id":"601529","l3_category_name":"Makeup Sets","product_id":"1000000000000000001","product_image_url":"https://example.com/images/product-001.jpg","product_name":"Demo Makeup Set","product_scan_url":"https://example.com/products/1000000000000000001","stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"seller_own_top_items":[{"content_type":"VIDEO","seller_own_avatar_url":"https://example.com/images/creator-001.png","seller_own_id":"1000000000000000004","seller_own_name":"Demo Creator","stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"},"sub_channel":"VIDEO"}],"video_top_items":[{"linked_products":[{"product_id":"1000000000000000001","product_image_url":"https://example.com/images/product-001.jpg","product_name":"Demo Makeup Set","product_scan_url":"https://example.com/products/1000000000000000001"}],"publish_time":"2026-09-18","seller_own_avatar_url":"https://example.com/images/creator-001.png","seller_own_id":"1000000000000000004","seller_own_name":"Demo Creator","stats":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"},"video_cover_url":"https://example.com/images/video-001.jpg","video_id":"1000000000000000006","video_infos":[{"backup_url":"https://example.com/media/video-001-backup.mp4","bitrate":1200000,"file_hash":"00000000000000000000000000000000","format":"mp4","height":720,"main_url":"https://example.com/media/video-001.mp4","size":10485760,"url_expire":1793505600,"video_quality":"720p","width":1280}],"video_title":"Demo Product Video"}]}],"earliest_available_date":"2026-08-21","end_date":"2026-09-20","latest_available_date":"2026-09-20","scope":"MY_SHOP","start_date":"2026-08-22"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

