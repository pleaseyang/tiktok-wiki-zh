# 获取 ACC 受众偏好摘要

# Path: /analytics/202610/acc/preferences/summary
# Method: [GET]
# 功能描述
获取所选品牌、受众细分、范围和时间窗口的 ACC 商品、直播、video 和图文帖子受众偏好摘要。
---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
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
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^audience_type | string | CONVERSION | 用于摘要的受众细分，以大写的 audience_type 值返回。 |
| ^channel_summaries | []object |  | 按以下顺序排列的渠道摘要：PRODUCT、LIVE、VIDEO、PHOTO。当没有可用项目时，每个摘要中的列表可以为空。这些是结构化的 Top 3 结果，而非生成的叙述文本。当底层查询失败时列表也可能为空；仅凭空列表不能确定该渠道没有活动。 |
| ^^channel | string | PRODUCT | 此摘要代表的渠道：PRODUCT、LIVE、VIDEO 或 PHOTO。 |
| ^^live_top_items | []object |  | Up to 3 livestreams with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order. Populated in the LIVE summary when data is available. |
| ^^^live_room_type | string | demo_room_type | Livestream room category label. |
| ^^^live_start_time | string | 2026-09-18 | Date when the livestream started, in YYYY-MM-DD format (UTC). |
| ^^^live_type | string | label1 | Livestream type label. |
| ^^^replay_url | string | https://example.com/live/1000000000000000005/replay | URL of the livestream replay. |
| ^^^room_id | string | 1000000000000000005 | ID of the livestream room. |
| ^^^room_image_url | string | https://example.com/images/live-001.jpg | URL of the livestream cover image. |
| ^^^room_title | string | Demo LIVE Session | Title of the livestream. |
| ^^^seller_own_id | string | 1000000000000000004 | ID of the content author. |
| ^^^seller_own_name | string | Demo Creator | Display name of the content author. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^live_type_top_items | []object |  | Up to 3 livestream types with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order. Populated in the LIVE summary when data is available. |
| ^^^live_type | string | label1 | Stable LIVE type identifier, such as label1. Use this identifier as factor_id in Get ACC Audience Preference List for entity_type=LIVE; the localized display name is not a query value. |
| ^^^live_type_name | string | Stable, non-shaky image | Localized display name of the LIVE factor. Use live_type, rather than this display name, as the stable identifier for filtering LIVE preferences. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^photo_top_items | []object |  | Up to 3 photo posts with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order. Populated in the PHOTO summary when data is available. |
| ^^^image_urls | []string | ["https://example.com/images/photo-001.jpg"] | URLs of images in the photo post. The cover image URL can be returned when no other image URLs are available. |
| ^^^linked_products | []object |  | Products linked to the photo post, when provided. |
| ^^^^product_id | string | 1000000000000000001 | ID of the product. |
| ^^^^product_image_url | string | https://example.com/images/product-001.jpg | URL of the product image. |
| ^^^^product_name | string | Demo Makeup Set | Name of the product. |
| ^^^^product_scan_url | string | https://example.com/products/1000000000000000001 | URL associated with the linked product. |
| ^^^photo_id | string | 1000000000000000007 | ID of the photo post. |
| ^^^photo_title | string | Demo Product Photo Post | Title of the photo post. |
| ^^^post_images | []object |  | Image metadata for the images in the photo post. |
| ^^^^color | string | #FFFFFF | Color of the image metadata for the images in the photo post. |
| ^^^^height | int | 1080 | Height of the image metadata for the images in the photo post. |
| ^^^^mimetype | string | image/jpeg | MIME type of the image. |
| ^^^^size | string | 204800 | Size of the image metadata for the images in the photo post. |
| ^^^^thumb_uri | string | demo/photo-001-thumb | Resource URI identifying the image thumbnail. |
| ^^^^thumb_url_list | []string | ["https://example.com/images/photo-001-thumb.jpg"] | URLs for the image thumbnail. |
| ^^^^tint_color | string | #F0F0F0 | Tint color of the image metadata for the images in the photo post. |
| ^^^^uri | string | demo/photo-001 | Resource URI identifying the image. |
| ^^^^url_list | []string | ["https://example.com/images/photo-001.jpg"] | URLs for the image. |
| ^^^^width | int | 1080 | Width of the image metadata for the images in the photo post. |
| ^^^publish_time | string | 2026-09-18 | Publication date of the photo post, in YYYY-MM-DD format (UTC). |
| ^^^seller_own_avatar_url | string | https://example.com/images/creator-001.png | URL of the content author's avatar. |
| ^^^seller_own_id | string | 1000000000000000004 | ID of the content author. |
| ^^^seller_own_name | string | Demo Creator | Display name of the content author. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^product_category_top_items | []object |  | Up to 3 level-2 product categories with the highest GMV, in descending GMV order, in the PRODUCT summary. Each category includes its available level-3 children; the 3-category limit applies to level-2 entries. |
| ^^^category_id | string | 848648 | ID of this level-2 product category. |
| ^^^category_name | string | Makeup | Name of this level-2 product category. |
| ^^^children | []object |  | Level-3 product categories belonging to this level-2 category. The top-3 limit on product_category_top_items does not independently limit this child list. |
| ^^^^category_id | string | 601529 | ID of this level-3 product category. |
| ^^^^category_name | string | Makeup Sets | Name of this level-3 product category. |
| ^^^^level | int | 3 | Product category level. This node is level 3. |
| ^^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^^level | int | 2 | Product category level. This node is level 2. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^product_top_items | []object |  | Up to 3 products with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order. Populated in the PRODUCT summary when data is available. |
| ^^^l2_category_id | string | 848648 | ID of the product's level-2 category. |
| ^^^l2_category_name | string | Makeup | Name of the product's level-2 category. |
| ^^^l3_category_id | string | 601529 | ID of the product's level-3 category. |
| ^^^l3_category_name | string | Makeup Sets | Name of the product's level-3 category. |
| ^^^product_id | string | 1000000000000000001 | ID of the product. |
| ^^^product_image_url | string | https://example.com/images/product-001.jpg | URL of the product image. |
| ^^^product_name | string | Demo Makeup Set | Name of the product. |
| ^^^product_scan_url | string | https://example.com/products/1000000000000000001 | Share link for the product. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^seller_own_top_items | []object |  | Content-author preference summaries for the channel. This list can be empty. |
| ^^^content_type | string | VIDEO | Content classification associated with this content-author summary. |
| ^^^seller_own_avatar_url | string | https://example.com/images/creator-001.png | URL of the content author's avatar. |
| ^^^seller_own_id | string | 1000000000000000004 | ID of the content author. |
| ^^^seller_own_name | string | Demo Creator | Display name of the content author. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Gross merchandise value (GMV) range associated with this content-author summary. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^^sub_channel | string | VIDEO | Channel associated with this content-author summary. |
| ^^video_top_items | []object |  | Up to 3 videos with the highest GMV for the selected audience, scope, and reporting window, in descending GMV order. Populated in the VIDEO summary when data is available. |
| ^^^linked_products | []object |  | Products linked to the video, when provided. |
| ^^^^product_id | string | 1000000000000000001 | ID of the product. |
| ^^^^product_image_url | string | https://example.com/images/product-001.jpg | URL of the product image. |
| ^^^^product_name | string | Demo Makeup Set | Name of the product. |
| ^^^^product_scan_url | string | https://example.com/products/1000000000000000001 | URL associated with the linked product. |
| ^^^publish_time | string | 2026-09-18 | Publication date of the video, in YYYY-MM-DD format (UTC). |
| ^^^seller_own_avatar_url | string | https://example.com/images/creator-001.png | URL of the content author's avatar. |
| ^^^seller_own_id | string | 1000000000000000004 | ID of the content author. |
| ^^^seller_own_name | string | Demo Creator | Display name of the content author. |
| ^^^stats | object |  | Audience preference metrics for this item in the selected reporting window. |
| ^^^^customers | string | 4210 | Reported customer count for this item in the selected reporting window, represented as a string. |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's region and currency information where available. |
| ^^^^orders | string | 8566 | Reported order count for this item in the selected reporting window, represented as a string. |
| ^^^video_cover_url | string | https://example.com/images/video-001.jpg | URL of the video cover image. |
| ^^^video_id | string | 1000000000000000006 | ID of the video. |
| ^^^video_infos | []object |  | Available video file representations and their playback metadata. |
| ^^^^backup_url | string | https://example.com/media/video-001-backup.mp4 | Backup playback URL for this video representation. |
| ^^^^bitrate | int | 1200000 | Bitrate of this video representation. |
| ^^^^file_hash | string | 00000000000000000000000000000000 | Hash identifying this video file. |
| ^^^^format | string | mp4 | File format of this video representation. |
| ^^^^height | int | 720 | Height format of this video representation. |
| ^^^^main_url | string | https://example.com/media/video-001.mp4 | Primary playback URL for this video representation. |
| ^^^^size | int | 10485760 | Size of this video representation. |
| ^^^^url_expire | int | 1793505600 | Url expire timestamp format of this video representation. |
| ^^^^video_quality | string | 720p | Quality label of this video representation. |
| ^^^^width | int | 1280 | Width of this video representation. |
| ^^^video_title | string | Demo Product Video | Title of the video. |
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
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

