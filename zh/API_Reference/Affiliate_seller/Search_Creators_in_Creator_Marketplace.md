# 在 Creator Marketplace 中搜索 Creator

# Path: /affiliate_seller/202608/marketplace_creators/search
# Method: [POST]
# 功能描述
此 API 供卖家在 Creator Marketplace 中搜索 creator。卖家可以基于 GMV、关键词和 creator 粉丝画像等筛选条件进行搜索。所有返回的数据均为最近 30 天的数据。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | b2Zmc2V0PTAK | 分页 token，用于标识继续搜索的位置。首次请求时，请省略此参数或将其留空。每次后续请求，请传入上一次响应返回的 next_page_token。 |
| page_size | int | Y | 12 | "page_size" 的值必须为 12 或 20。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| search_key | string | N | 2E+0EcXoSk2HWdEWh2nITfkBRMbwuug0mt9s3fWgV0k= | 缓存搜索结果可提高 API 性能并确保请求结果稳定。 |
| 首次调用时无需传入值。 |  |  |  |  |
| 第二次调用时，请传入第一次调用响应中返回的值。 |  |  |  |  |
| keyword | string | N | JefreeStar | 通过关键词搜索 creator，基于 TikTok 用户名和昵称进行匹配。 |
| follower_demographics | object | N |  | 按粉丝人群画像筛选 creator |
| ^age_ranges | []string | N | ["AGE_RANGE_18_24", "AGE_RANGE_35_44"] | 粉丝年龄筛选选项，为范围区间，包括： |
| AGE_RANGE_18_24: "18-24", |  |  |  |  |
| AGE_RANGE_25_34: "25-34", |  |  |  |  |
| AGE_RANGE_35_44: "35-44", |  |  |  |  |
| AGE_RANGE_45_54: "45-54", |  |  |  |  |
| AGE_RANGE_55_AND_ABOVE: "55+" |  |  |  |  |
| ^count_range | object | N |  | 粉丝数量筛选 |
| ^^count_ge | int | N | 1000 | 粉丝数量的最小值。 |
| 传入的值必须大于或等于 0 |  |  |  |  |
| ^^count_le | int | N | 10000 | 粉丝数量的最大值。 |

* 通常需要传入大于或等于 0 的值。如果传入小于 0 的值，则表示不对该字段进行筛选。 |
   ^gender_distribution |object |N | |按粉丝性别筛选 creator。
   Possible values:
* MALE
* FEMALE |
   ^^gender |string |N |MALE |特定性别，"MALE" 或 "FEMALE" |
   ^^percentage_ge |int |N |6000 |大于或等于某个百分比，放大 10,000 倍。
   例如，6000 代表 0.6 或 60% |
   gmv_ranges |[]string |N |["GMV_RANGE_0_100", "GMV_RANGE_100_1000"] |按 GMV 范围区间筛选，包括：
   GMV_RANGE_0_100: "0-100",
   GMV_RANGE_100_1000: "100-1000",
   GMV_RANGE_1000_10000: "1000-10000",
   GMV_RANGE_10000_AND_ABOVE: "10000+"
   For example:
* If GMV_RANGE_0_100 is passed, it means filtering the creator data that is greater than or equal to 0 and less than or equal to 100.
* If GMV_RANGE_0_100 and GMV_RANGE_100_1000 are passed, it means to filter the creator data that is greater than or equal to 0 and less than or equal to 1000. |
   units_sold_ranges |[]string |N |["UNITS_SOLD_RANGE_0_10", "UNITS_SOLD_RANGE_100_1000","UNITS_SOLD_RANGE_1000_AND_ABOVE"]
   |按销售量范围区间筛选，包括：
   UNITS_SOLD_RANGE_0_10: "0-10",
   UNITS_SOLD_RANGE_10_100: "10-100",
   UNITS_SOLD_RANGE_100_1000: "100-1000",
   UNITS_SOLD_RANGE_1000_AND_ABOVE: "1000+"
   For example:
* If UNITS_SOLD_RANGE_0_10 is passed, it means filtering the creator data that is greater than or equal to 0 and less than or equal to 10.
* If UNITS_SOLD_RANGE_0_10 and UNITS_SOLD_RANGE_10_100 are passed, it means to filter the creator data that is greater than or equal to 0 and less than or equal to 100. |
   category |[]object |N | |分类筛选对象数组。使用 [Get Categories](https://partner.tiktokshop.com/docv2/page/get-categories-202309) 获取分类 ID。 |
   ^parent_category_id |string |N |600001 |父分类的分类。如果仅使用父分类，则无需传入子分类 ID。 |
   ^child_category_id_list |[]string |N |["851848"] |如果使用子分类的分类 ID，则必须同时传入父分类。子分类仅比父分类深 1 级。不支持在分类树中更深层级（部分国家有 4 级，其他国家有 7 级）。 |
   content_performance |object |N | |包含内容表现筛选条件的对象。 |
   ^avg_video_views |string |N |1 |平均视频播放量大于
   您可以传入 0 到 100k 之间的平均视频播放量
   选择 0 到 100,000 之间的任意整数，我们将返回平均视频播放量大于该数字的所有结果。
   您只能传入平均视频播放量或平均可购物视频播放量。同时使用两个筛选条件会导致 API 调用失败。 |
   ^avg_shoppable_video_views |string |N |1 |您可以传入 0 到 100k 之间的平均可购物视频播放量
   选择 0 到 100,000 之间的任意整数，我们将返回平均可购物视频播放量大于该数字的所有结果。
   您只能传入平均视频播放量或平均可购物视频播放量。同时使用两个筛选条件会导致 API 调用失败。 |
   ^avg_engagement_rate |string |N |1 |平均互动率大于 0-20。
   只能按 1% 的增量筛选，最高 20%。 |
   ^avg_shopable_engagement_rate |string |N |1 |平均可购物互动率大于 0-20。
   只能按 1% 的增量筛选，最高 20%。 |
   ^avg_live_avg_viewers_ge |string |N |1 |筛选平均直播观看人数大于或等于指定值的 creator。
   输入 0 到 100,000 之间的整数。
   您只能传入 avg_live_avg_viewers_ge 和 avg_shoppable_live_avg_viewers_ge 之一。同时使用两个筛选条件会导致 API 调用失败。 |
   ^avg_shoppable_live_avg_viewers_ge |string |N |1 |筛选平均可购物直播观看人数大于或等于指定值的 creator。
   输入 0 到 100,000 之间的整数。
   您只能传入 avg_live_avg_viewers_ge 和 avg_shoppable_live_avg_viewers_ge 之一。同时使用两个筛选条件会导致 API 调用失败。 |
   affiliate_data |object |N | |包含基于 affiliate 数据的对象。 |
   ^avg_commission_rate |string |N |LESS_THAN_20% |- ALL
* LESS_THAN_20%
* LESS_THAN_15%
* LESS_THAN_10%
* LESS_THAN_5%
   Creator 基于 showcase 产品、销售和最近 30 天推广产品的平均 commission 比率范围。
   您只能选择一个值。 |
   ^post_rate |string |N |GOOD |这些类别代表 creator 在收到 sample 后发布可购物视频或直播的频率。
* ALL
* OK
* GOOD
* BETTER
   每个国家都有自己的基准，用于区分 GOOD 和 BETTER 履约率。 BETTER 始终具有最高的履约率，包括 100% 履约率。 |
   ^creator_agency_staus |string |N |AGENCY_MANAGED |- AGENCY_MANAGED
* INDEPENDENT |
   ^is_fast_growing |bool |N |false |最近 30 天内交易、收入、可购物视频、直播观看量或粉丝增长最多的前 10% creator。 |
   ^not_invited_l90_days |bool |N |false |True/False
   选择此筛选条件以查看您在最近 90 天内未邀请过的 creator。 |
   advanced_filters |object |N | |高级筛选条件因国家/地区而异。 在使用此 API 的高级筛选条件之前，请使用 [Get Seller Search Creator Marketplace Advanced Filters](https://partner.tiktokshop.com/docv2/page/get-seller-search-creator-marketplace-advanced-filters) 获取相关国家/地区可用的筛选条件。 |
   ^content_preference_type |[]string |N |["VIDEO"] |内容偏好类型。例如
   -VIDEO
   -LIVE |
   ^eligible_flat_fee |bool |N |false |Creator 有资格获得固定费用邀请，仅适用于美国本地卖家。 |
   ^option_list |[]object |N | |Creator Marketplace 高级筛选选项列表。 请使用 "Get Seller Search Creator Marketplace Advanced Filters"(https://partner.tiktokshop.com/docv2/page/get-seller-search-creator-marketplace-advanced-filters) 先获取可用选项 |
   ^^options |[]object |N | |此 选项类型 |
   ^^^id |string |N |1 |选项 ID |
   ^^^name |string |N |English |选项名称 |
   ^^^option_children |[]object |N | |子选项 |
   ^^^^id |string |N |2 |选项 ID |
   ^^^^name |string |N |SubTypeName |选项名称, used if the option has sub-type choices. |
   ^^option_type |string |N |OPTION_LANGUAGE |选项类型 |
   ^sorter_algorithm_id |string |N |1 |排序算法 ID。 请使用 "Get Seller Search Creator Marketplace Advanced Filters"(https://partner.tiktokshop.com/docv2/page/get-seller-search-creator-marketplace-advanced-filters) get available sorter algorithm for you first. Default is 1(default sorter) |
   data_groups |[]string |N |["BASIC_CREATOR_INFORMATION","SALES_AND_GMV"] |Creator 的数据组，默认获取所有组，包括：
* BASIC_CREATOR_INFORMATION
* CONTENT_PERFORMANCE
* FOLLOWER_INFORMATION
* COLLABORATION
* SALES_AND_GMV |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202608/marketplace_creators/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=b2Zmc2V0PTAK&page_size=12
```

**Body**
```json
{"search_key":"2E+0EcXoSk2HWdEWh2nITfkBRMbwuug0mt9s3fWgV0k=","keyword":"JefreeStar","follower_demographics":{"age_ranges":["AGE_RANGE_18_24","AGE_RANGE_35_44"],"count_range":{"count_ge":1000,"count_le":10000},"gender_distribution":{"gender":"MALE","percentage_ge":6000}},"gmv_ranges":["GMV_RANGE_0_100","GMV_RANGE_100_1000"],"units_sold_ranges":["UNITS_SOLD_RANGE_0_10","UNITS_SOLD_RANGE_100_1000","UNITS_SOLD_RANGE_1000_AND_ABOVE"],"category":[{"parent_category_id":"600001","child_category_id_list":["851848"]}],"content_performance":{"avg_video_views":"1","avg_shoppable_video_views":"1","avg_engagement_rate":"1","avg_shopable_engagement_rate":"1","avg_live_avg_viewers_ge":"1","avg_shoppable_live_avg_viewers_ge":"1"},"affiliate_data":{"avg_commission_rate":"LESS_THAN_20%","post_rate":"GOOD","creator_agency_staus":"AGENCY_MANAGED","is_fast_growing":false,"not_invited_l90_days":false},"advanced_filters":{"content_preference_type":["VIDEO"],"eligible_flat_fee":false,"option_list":[{"options":[{"id":"1","name":"English","option_children":[{"id":"2","name":"SubTypeName"}]}],"option_type":"OPTION_LANGUAGE"}],"sorter_algorithm_id":"1"},"data_groups":["BASIC_CREATOR_INFORMATION","SALES_AND_GMV"]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTEy | 下一页的分页 token。要继续搜索，请将此值作为查询参数 `page_token` 传入，将同一响应中返回的 `search_key` 作为请求体 `search_key` 传入，并复用相同的 `page_size`。空 token 表示没有更多结果。 |
| ^search_key | string | k1ChOzI9e+j5BHHHEnt+VhItjVFEkPUCCXNsrU8/v4U= | 用于继续相同搜索并获得稳定结果的搜索键。请在此请求中将此值作为 search_key 传入。 |
| ^creators | []object |  | 包含基本资料、内容表现、粉丝、GMV 和销售范围信息的 Creator 记录。包含的字段取决于请求的 `data_groups`。 |
| ^^username | string | abc | Creator 的 TikTok 用户名。 |
| ^^nickname | string | cde | Creator 的 TikTok 昵称。 |
| ^^avatar | object |  | Creator 的个人资料图片。 |
| ^^^url | string | https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078&x-expires=1712988000&x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D | Creator 头像图片的 URL。 |
| ^^selection_region | string | GB | Creator 运营和推广产品的地区。 |
| ^^category_ids | []string | ["60001"] | 表示 creator 发布产品时的主要产品分类。 |
| ^^avg_ec_live_uv | int | 1331 | Creator 电商直播的平均 UV。 |
| ^^avg_ec_video_view_count | int | 112 | Creator 电商视频的平均播放量。 |
| ^^follower_count | int | 23241 | Follower count |
| ^^gmv | object |  | Creator GMV-related information |
| If the creator does not authorize sharing precise data, this will be omitted. |  |  |  |
| ^^^currency | string | USD | Currency code for the GMV amount. |
| ^^^amount | string | 1232.90 | GMV value |
| ^^live_gmv | object |  | Live stream GMV |
| If the creator does not authorize sharing precise data, this will be omitted. |  |  |  |
| ^^^currency | string | USD | Currency code for the live-stream GMV amount. |
| ^^^amount | string | 0.34 | Live stream GMV value |
| ^^video_gmv | object |  | Video GMV-related information |
| If the creator does not authorize sharing precise data, this will be omitted. |  |  |  |
| ^^^currency | string | USD | Currency code for the video GMV amount. |
| ^^^amount | string | 23.34 | Video GMV value |
| ^^gmv_range | object |  | GMV range. |
| Applicable if the target market is the US and the creator does not authorize sharing precise data. |  |  |  |
|  |  |  |  |
| ^^^currency | string | USD | Currency code for the GMV range. |
| ^^^minimum_amount | string | 0 | The minimum value of GMV range |
| ^^^maximum_amount | string | 100 | The maximum value of GMV range |
| ^^^formatted_range | string | $0-$100 | The formatted range of GMV values associated with this creator. |
| ^^units_sold_range | object |  | The range of minimum number of units sold to maximum number of units sold over the lifetime of the creator account. Note that this property is included if the target market is US only. Note that if the creator has not given permission for precise data sharing, these properties will not be present. |
| ^^^minimum_amount | int | 100 | The minimum value of sales volume range |
| ^^^maximum_amount | int | 1000 | The maximum value of sales volume range |
| ^^^formatted_range | string | 100-1K | The formatted range of minimum number of units sold to maximum number of units sold over the lifetime of the creator account. |
| ^^top_follower_demographics | object |  | Top follower information of the creator |
| ^^^age_ranges | []string | [ "AGE_RANGE_18_24", "AGE_RANGE_25_34"] | Return the top 3 age ranges of the followers. Ranges are : |
| AGE_RANGE_18_24: "18-24", |  |  |  |
| AGE_RANGE_25_34: "25-34", |  |  |  |
| AGE_RANGE_35_44: "35-44", |  |  |  |
| AGE_RANGE_45_54: "45-54", |  |  |  |
| AGE_RANGE_55_AND_ABOVE: "55+" |  |  |  |
| ^^^major_gender | object |  | Major gender of the followers |
|  |  |  |  |
| ^^^^gender | string | FEMALE | Top follower gender category of the creator, "MALE" or "FEMALE" |
| ^^^^percentage | int | 6524 | Percentage of top follower gender, scaled up by 10,000 times. |
| For example, 6524 stands for 0.6524 or 65.24%. You can then infer that the opposite gender would be 0.3476 or 34.76%. |  |  |  |
| ^^creator_open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
| ^^creator_profile | object |  | Advanced creator profile information. An empty object means that this profile information is not currently supported for your account or region. |
| ^^^is_official_recommend | bool | false | Creator has official recommend tag or not |
| ^^^creator_bind_mcn_name | string | name | Creator 绑定的 MCN 名称 |
| ^^^is_fast_growing | bool | false | Creator has fast growing tag or not |
| ^^^has_collaborated | bool | false | Has collaborated with this creator or not |
| ^^^user_type_tag | []int | [1] | User type tag. |
| Possible values: |  |  |  |

* 1: Privacy creator
* 2: Carve-out creator |
   ^^^has_invited_90d |bool |false |Has invited creaor before 90 days |
   ^^^is_creator_blocked |bool |false |Is this creator blocked by shop or not |
   ^^^pps_score |string |4.3 |Creator promotion performance score(PPS).The score reflects the quality of a creator's shoppable content and product selection over the past 30 days. 高分可能表示更好的购物体验，减少潜在的退款或负面评价。 e.g. 4.3/5.0 |
   ^^^is_eligible_flat_fee |bool |false |Is creator eligible for flat fee, only available for US local seller |
   ^^^is_rising_star |bool |false |Creator has rising star tag or not |
   ^^^creator_level |int |2 |Creator 等级 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTEy","search_key":"k1ChOzI9e+j5BHHHEnt+VhItjVFEkPUCCXNsrU8/v4U=","creators":[{"username":"abc","nickname":"cde","avatar":{"url":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078\u0026x-expires=1712988000\u0026x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D"},"selection_region":"GB","category_ids":["60001"],"avg_ec_live_uv":1331,"avg_ec_video_view_count":112,"follower_count":23241,"gmv":{"currency":"USD","amount":"1232.90"},"live_gmv":{"currency":"USD","amount":"0.34"},"video_gmv":{"currency":"USD","amount":"23.34"},"gmv_range":{"currency":"USD","minimum_amount":"0","maximum_amount":"100","formatted_range":"$0-$100"},"units_sold_range":{"minimum_amount":100,"maximum_amount":1000,"formatted_range":"100-1K"},"top_follower_demographics":{"age_ranges":["AGE_RANGE_18_24","AGE_RANGE_25_34"],"major_gender":{"gender":"FEMALE","percentage":6524}},"creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","creator_profile":{"is_official_recommend":false,"creator_bind_mcn_name":"name","is_fast_growing":false,"has_collaborated":false,"user_type_tag":[1],"has_invited_90d":false,"is_creator_blocked":false,"pps_score":"4.3","is_eligible_flat_fee":false,"is_rising_star":false,"creator_level":2}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

