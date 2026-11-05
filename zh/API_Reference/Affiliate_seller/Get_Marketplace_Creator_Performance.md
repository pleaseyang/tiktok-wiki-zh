# 获取 Marketplace Creator 表现

# Path: /affiliate_seller/202608/marketplace_creators/{creator_user_id}
# Method: [GET]
# 功能描述
返回指定 creator 的 marketplace 信息和表现指标。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| creator_user_id | string | Y | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| data_groups | []string | N | BASIC_CREATOR_INFORMATION | 响应中包含的 creator 数据组。如果省略，则选择全部五个组。单个字段的可用性仍取决于各字段记录的市场、权限和可用性条件。如需请求多个组，请以逗号分隔的查询字符串形式提供值，例如 BASIC_CREATOR_INFORMATION,CONTENT_PERFORMANCE。 |
| Available values: |  |  |  |  |

* BASIC_CREATOR_INFORMATION: Creator 基本资料信息。
* CONTENT_PERFORMANCE: 内容表现指标、推广表现分数 (PPS)、履约分数和推广产品数量。
* FOLLOWER_INFORMATION: 粉丝地区、年龄和性别分布。
* COLLABORATION: 合作品牌和 commission 信息。
* SALES_AND_GMV: 销售件数；GMV 和 GPM 指标及分布；产品价格范围；以及每位买家的平均 GMV。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202608/marketplace_creators/uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&data_groups=BASIC_CREATOR_INFORMATION
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^creator | object |  | 与 creator 的 TikTok 个人资料关联的数据。 |
| ^^username | string | dioab | TikTok 用户名。 |
| ^^nickname | string | Dion | TikTok 昵称。 |
| ^^avatar | object |  | 与 creator 的 TikTok 个人资料头像关联的元数据和数据。 |
| ^^^url | string | https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078&x-expires=1712988000&x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D | Creator 的 TikTok 个人资料头像 URL。 |
| ^^selection_region | string | US | Creator 选择推广产品的地区。 |
| ^^bio_description | string | This is my personal introduction | 与 creator 关联的个人简介描述。 |
| ^^follower_count | int | 2323 | Creator 的粉丝数量。 |
| ^^profile_tt_uri | string | aweme://user/profile/7200669046446064666?sec_uid=MS4wLjABAAAAvkrSOIMxn2YpXW5qBFVHIbfQ11u2L1hamtgg3mbk5GRPpl1TrnKo5zzQe5T77YLw&from_scene=8&enter_from=scan | Creator 的 TikTok 个人资料深度链接 URI。 |
| ^^category_ids | []string | ["60001"] | 与 creator 已创建帖子的产品关联的分类标识符列表。 |
| ^^top_collaborated_brand_ids | []string | ["8363021"] | Creator 之前合作过的前 10 个品牌列表。 |
| ^^brand_collaboration_count | int | 76 | Creator 之前合作过的品牌总数。 |
| ^^units_sold | int | 234 | 销售总件数。件数按 SKU 索引。请注意，如果 creator 未授权精确数据共享，则此属性不存在。 |
| ^^units_sold_range | object |  | Creator 账户生命周期内最小销售件数到最大销售件数的范围。请注意，此属性仅在目标市场为 `US` 时包含。如果 creator 未授权精确数据共享，则这些属性不存在。 |
| ^^^minimum_amount | int | 100 | 最低销售件数。 |
| ^^^maximum_amount | int | 1000 | 最高销售件数。 |
| ^^^formatted_range | string | 0-10 | Creator 账户生命周期内最小销售件数到最大销售件数的格式化范围。 |
| ^^gmv | object |  | 与 creator 关联的商品交易总额 (GMV) 元数据和数据。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
| ^^^currency | string | USD | 币种代码。 |
| ^^^amount | string | 3434.23 | 与 creator 关联的总 GMV。 |
| ^^video_gmv | object |  | 与 creator 关联的视频 GMV 元数据和数据。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
| ^^^currency | string | USD | 币种代码。 |
| ^^^amount | string | 39232.34 | 与 creator 关联的总视频 GMV。 |
| ^^live_gmv | object |  | 与 creator 关联的直播 GMV 元数据和数据。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
| ^^^currency | string | USD | 币种代码。 |
| ^^^amount | string | 3432.34 | 与 creator 关联的总直播 GMV。 |
| ^^gmv_range | object |  | 与此 creator 关联的 GMV 值范围。请注意，此属性仅在目标市场为 `US` 时包含。如果 creator 未授权精确数据共享，则这些属性不存在。 |
| ^^^currency | string | USD | 币种代码。 |
| ^^^minimum_amount | string | 1000.00 | 最低 GMV 值。 |
| ^^^maximum_amount | string | 10000.00 | 最高 GMV 值。 |
| ^^^formatted_range | string | $0-$100 | 与此 creator 关联的 GMV 值的格式化范围。 |
| ^^ec_live_engagement_rate | string | 6000 | 电商直播互动率，以百分之一为单位。例如，`6000` 为 60%。 |
| ^^category_gmv_distribution | []object |  | 按分类的 GMV 分布。 |
| ^^^category_id | string | 66666 | 顶级分类标识符。值为 `-1` 表示所有其他分类。 |
| ^^^value | string | 0.3035 | creator 的 GMV 归属于该分类的比例，以 `0` 到 `1` 的小数表示（例如，`0.3035` = 30.35%）。 |
| ^^content_gmv_distribution | []object |  | 按内容类型划分的 creator 内容关联 GMV。 |
| ^^^content_type | string | VIDEO | 内容类型。此为枚举类型，值包括： |

* VIDEO
* LIVE
* SHOWCASE |
   ^^^value |string |0.3035 |creator 的 GMV 归属于该内容类型的比例，以 `0` 到 `1` 的小数表示（例如，`0.3035` = 30.35%）。 |
   ^^product_original_price_range |object | |Creator 在最近 30 天推广的产品原始价格范围。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^minimum_amount |string |2.59 |最低原始推广产品价格。 |
   ^^^maximum_amount |string |343.23 |最高原始推广产品价格。 |
   ^^gpm |object | |与 creator 关联的每千次展示 GMV (GPM) 元数据和数据。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^amount |string |10.23 |GPM 金额。 |
   ^^live_gpm |object | |Livestream 与 creator 关联的每千次展示 GMV (GPM) 元数据和数据。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^amount |string |44.96 |直播 GPM 金额。 |
   ^^video_gpm |object | |Video 与 creator 关联的每千次展示 GMV (GPM) 元数据和数据。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^amount |string |28.89 |视频 GPM 金额。 |
   ^^gpm_range |object | |与 creator 关联的 GPM 值范围。请注意，此属性仅在目标市场为 `US` 时包含。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^minimum_amount |string |100.00 |最低 GPM 值。 |
   ^^^maximum_amount |string |1000.00 |最高 GPM 值。 |
   ^^^formatted_range |string |$0-$100 |与 creator 关联的 GPM 值的格式化范围。 |
   ^^video_gpm_range |object | |与 creator 关联的视频 GPM 值范围。 Note that this property is included if the target market is `US`. Note that if the creator has not given permission for precise data sharing, these properties will not be present. |
   ^^^currency |string |USD |币种代码。 |
   ^^^minimum_amount |string |100.00 |最低视频 GPM 值。 |
   ^^^maximum_amount |string |1000.00 |最高视频 GPM 值。 |
   ^^^formatted_range |string |$0-$100 |与 creator 关联的视频 GPM 值的格式化范围。 |
   ^^live_gpm_range |object | |与 creator 关联的直播 GPM 值范围。 Note that this property is included if the target market is `US` only. Note that if the creator has not given permission for precise data sharing, these properties will not be present. |
   ^^^currency |string |USD |币种代码。 |
   ^^^minimum_amount |string |100.00 |最低直播 GPM 值。 |
   ^^^maximum_amount |string |1000.00 |最高直播 GPM 值。 |
   ^^^formatted_range |string |$0-$100 |与 creator 关联的直播 GPM 值的格式化范围。 |
   ^^promoted_product_num |int |311 |Creator 在最近 30 天推广的产品数量。 |
   ^^ec_live_count |int |12 |与 creator 关联的最近 30 天电商直播数量。 |
   ^^ec_video_count |int |34 |与 creator 关联的最近 30 天电商视频发布数量。 |
   ^^avg_ec_video_play_count |int |1234 |电商视频平均播放次数。 |
   ^^avg_commission_rate |int |6000 |平均 commission 比率，以百分之一为单位。请注意，如果 creator 未授权精确数据共享，则这些属性不存在。 |
   ^^avg_commission_rate_range |object | |与 creator 关联的平均 commission 比率范围。 |
   ^^^minimum_amount |int |6000 |最小平均 commission 比率，以百分之一为单位。 |
   ^^^maximum_amount |int |7000 |最大平均 commission 比率，以百分之一为单位。 |
   ^^avg_gmv_per_buyer |object | |与 creator 关联的每位买家平均 GMV 元数据和数据。请注意，此属性仅在目标市场为 `US` 时包含。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^amount |string |45.68 |每位买家平均 GMV 金额。 |
   ^^avg_gmv_per_buyer_range |object | |与 creator 关联的每位买家平均 GMV 范围。 |
   ^^^currency |string |USD |币种代码。 |
   ^^^minimum_amount |string |100.00 |最小每位买家平均 GMV。 |
   ^^^maximum_amount |string |1000.00 |最大每位买家平均 GMV。 |
   ^^^formatted_range |string |$15-$20 |与 creator 关联的每位买家平均 GMV 的格式化范围。 |
   ^^avg_ec_live_view_count |int |4355 |推广产品的平均直播观看量。 |
   ^^avg_ec_live_like_count |int |344 |电商直播平均点赞数。 |
   ^^avg_ec_live_comment_count |int |23 |电商直播平均评论数。 |
   ^^avg_ec_live_share_count |int |3434 |电商直播平均分享数。 |
   ^^avg_ec_video_like_count |int |324 |电商视频平均点赞数。 |
   ^^avg_ec_video_comment_count |int |343 |电商视频平均评论数。 |
   ^^avg_ec_video_share_count |int |22 |电商视频平均分享数。 |
   ^^follower_location |[]object | |表示粉丝按地区分布的键值对列表。 |
   ^^^key |string |ID |粉丝所在地区的国家代码（例如，ID）。 |
   ^^^value |string |0.3705 |来自该地区的粉丝比例，以小数表示（例如，0.3705 = 37.05%）。 |
   ^^follower_age |[]object | |表示粉丝按年龄范围分布的键值对列表。 |
   ^^^key |string |18-23 |年龄范围（例如，"18-23"）。 |
   ^^^value |string |0.2500 |该年龄范围内的粉丝比例，以小数表示（例如，0.2500 = 25.00%）。 |
   ^^follower_gender |[]object | |表示粉丝按性别分布的键值对列表。 |
   ^^^key |string |Male |性别（例如，"Male"、"Female"）。 |
   ^^^value |string |0.5000 |该性别的粉丝比例，以小数表示（例如，0.5000 = 50.00%）。 |
   ^^pps |string |4.5 |推广表现分数 (PPS)
   该分数反映 creator 在过去 90 天内的可购物内容和产品选择的质量。 高分可能表示更好的购物体验，减少潜在的退款或负面评价。 |
   ^^rating |string |3.2 |与此 creator 合作过的卖家的评分。 |
   ^^ec_video_engagement_rate |string |3000 |帖子互动次数（点赞、分享和评论）除以最近 30 天视频的平均总播放量。
   例如，3000 代表 0.3 或 30% |
   ^^post_rate |string |100 |Creator 在收到 sample 后可能发布可购物视频或直播的预估比率。
   例如，3000 代表 0.3 或 30% |
   ^^creator_profile |object | |高级 creator 个人资料信息。空对象表示此信息对调用者的账号或地区不可用。 |
   ^^^is_official_recommend |bool |false |Creator 是否有官方推荐标签 |
   ^^^contact_info_available |bool |false |Creator 联系信息是否可用 |
   ^^^creator_bind_mcn_name |string |name |Creator 绑定的 MCN 名称 |
   ^^^live_engagement_rate_30d |int |50 |Creator 最近 30 天的互动率 |
   ^^^video_play_cnt_30d_med |int |10 |Creator 最近 30 天的平均视频播放量 |
   ^^^live_view_cnt_30d_med |int |10 |Creator 最近 30 天的平均直播观看量 |
   ^^^live_like_cnt_30d |int |10 |Creator 最近 30 天的直播点赞数 |
   ^^^live_comment_cnt_30d_med |int |10 |Creator 最近 30 天的平均直播评论数 |
   ^^^live_share_cnt_30d_med |int |10 |Creator 最近 30 天的平均直播分享数 |
   ^^^video_publish_cnt_30d_med |int |10 |Creator 最近 30 天的平均视频发布数 |
   ^^^has_invited_90d |bool |false |是否在 90 天内邀请过 |
   ^^^is_creator_blocked |bool |false |Creator 是否被店铺拉黑 |
   ^^^creator_level |int |2 |Creator 等级 |
   ^^^creator_fulfillment_reviews |int |10 |卖家在最近 90 天内为该 creator 提交的履约评价数量。 |
   ^^^is_eligible_flat_fee |bool |false |Creator 有资格获得固定费用邀请 |
   ^^^is_rising_star |bool |false |Creator has rising star tag or not |
   ^^^creator_fulfillment_score_90d |string |4.1 |Creator fulfillment score during last 90 days |
   ^^^sample_score |int |75 |Creator credit total score. e.g. 75 means creator' sample scole is 75/100. |
   ^^^creator_connect_info |object | |Creator connect infomation |
   ^^^^is_paired |bool |false |Creator is paired or not |
   ^^^^is_connect |bool |false |Creator is connect or not |
   ^^^^is_blocked |bool |false |Creator is blocked or not |
   ^^^creator_trend_profile |[]object | |Creator trend infomation |
   ^^^^start_timestamp |int |1784419200 |Trend start timestamp |
   ^^^^end_timestamp |int |1784419200 |Trend end timestamp |
   ^^^^gmv |object | |Trend GMV infomation |
   ^^^^^amount |string |1000 |GMV amount |
   ^^^^^symbol |string |$ |GMV symbol |
   ^^^^units_sold |int |1000 |Trend units sold |
   ^^^^follower |int |1000 |Trend follower |
   ^^^^engagement_rate |int |558 |Trend engagement rate e.g. 558 means creator's engagement rate is 5.58% |

# 响应示例
```json
{"code":0,"data":{"creator":{"username":"dioab","nickname":"Dion","avatar":{"url":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078\u0026x-expires=1712988000\u0026x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D"},"selection_region":"US","bio_description":"This is my personal introduction","follower_count":2323,"profile_tt_uri":"aweme://user/profile/7200669046446064666?sec_uid=MS4wLjABAAAAvkrSOIMxn2YpXW5qBFVHIbfQ11u2L1hamtgg3mbk5GRPpl1TrnKo5zzQe5T77YLw\u0026from_scene=8\u0026enter_from=scan","category_ids":["60001"],"top_collaborated_brand_ids":["8363021"],"brand_collaboration_count":76,"units_sold":234,"units_sold_range":{"minimum_amount":100,"maximum_amount":1000,"formatted_range":"0-10"},"gmv":{"currency":"USD","amount":"3434.23"},"video_gmv":{"currency":"USD","amount":"39232.34"},"live_gmv":{"currency":"USD","amount":"3432.34"},"gmv_range":{"currency":"USD","minimum_amount":"1000.00","maximum_amount":"10000.00","formatted_range":"$0-$100"},"ec_live_engagement_rate":"6000","category_gmv_distribution":[{"category_id":"66666","value":"0.3035"}],"content_gmv_distribution":[{"content_type":"VIDEO","value":"0.3035"}],"product_original_price_range":{"currency":"USD","minimum_amount":"2.59","maximum_amount":"343.23"},"gpm":{"currency":"USD","amount":"10.23"},"live_gpm":{"currency":"USD","amount":"44.96"},"video_gpm":{"currency":"USD","amount":"28.89"},"gpm_range":{"currency":"USD","minimum_amount":"100.00","maximum_amount":"1000.00","formatted_range":"$0-$100"},"video_gpm_range":{"currency":"USD","minimum_amount":"100.00","maximum_amount":"1000.00","formatted_range":"$0-$100"},"live_gpm_range":{"currency":"USD","minimum_amount":"100.00","maximum_amount":"1000.00","formatted_range":"$0-$100"},"promoted_product_num":311,"ec_live_count":12,"ec_video_count":34,"avg_ec_video_play_count":1234,"avg_commission_rate":6000,"avg_commission_rate_range":{"minimum_amount":6000,"maximum_amount":7000},"avg_gmv_per_buyer":{"currency":"USD","amount":"45.68"},"avg_gmv_per_buyer_range":{"currency":"USD","minimum_amount":"100.00","maximum_amount":"1000.00","formatted_range":"$15-$20"},"avg_ec_live_view_count":4355,"avg_ec_live_like_count":344,"avg_ec_live_comment_count":23,"avg_ec_live_share_count":3434,"avg_ec_video_like_count":324,"avg_ec_video_comment_count":343,"avg_ec_video_share_count":22,"follower_location":[{"key":"ID","value":"0.3705"}],"follower_age":[{"key":"18-23","value":"0.2500"}],"follower_gender":[{"key":"Male","value":"0.5000"}],"pps":"4.5","rating":"3.2","ec_video_engagement_rate":"3000","post_rate":"100","creator_profile":{"is_official_recommend":false,"contact_info_available":false,"creator_bind_mcn_name":"name","live_engagement_rate_30d":50,"video_play_cnt_30d_med":10,"live_view_cnt_30d_med":10,"live_like_cnt_30d":10,"live_comment_cnt_30d_med":10,"live_share_cnt_30d_med":10,"video_publish_cnt_30d_med":10,"has_invited_90d":false,"is_creator_blocked":false,"creator_level":2,"creator_fulfillment_reviews":10,"is_eligible_flat_fee":false,"is_rising_star":false,"creator_fulfillment_score_90d":"4.1","sample_score":75,"creator_connect_info":{"is_paired":false,"is_connect":false,"is_blocked":false},"creator_trend_profile":[{"start_timestamp":1784419200,"end_timestamp":1784419200,"gmv":{"amount":"1000","symbol":"$"},"units_sold":1000,"follower":1000,"engagement_rate":558}]}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 16032012 | only affiliate partner cipher can access this api |
| 16901005 | this creator does't have e-commerce permission,please check the request params. |
| 16901006 | creator selection region doesn't match seller's region |
| 16901007 | The seller could not obtain an official creator profile due to insufficient permissions. |
| 16901008 | The creator didn't didn't have e-commerce permissions or has been deactivated. |
| 16901009 | can't access tiktok linkshare creator |
| 36009002 | Too many requests. You've made too many requests in a short period of time. |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 98001004 | Parameter {param_name} is invalid. Reason: {reason}. Expected: {expected_value} |

