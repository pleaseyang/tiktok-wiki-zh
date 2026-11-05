# 获取店铺 video Performance 列表

# Path: /analytics/202605/shop_videos/performance
# Method: [GET]
# 功能描述
返回店铺的 video 列表及相关指标。

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
| start_date_ge | string | Y | 2024-09-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。 |
| 参数名中，"ge"指"大于或等于"（含） |  |  |  |  |
开始日期和结束日期之间的时间范围不得超过 60 天。 |
end_date_lt |string |Y |2024-09-08 |结束日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。
参数名中，"lt"指"小于"（不含）。
开始日期和结束日期之间的时间范围不得超过 60 天。
|
page_size |int |N |10 |每页 video 数量。
最小值: 1
最大值: 100
默认值: 10 |
sort_field |string |N |gmv |用于排序店铺 video performance 列表的字段。
默认值: gmv
可选值：

* gmv: 按总 GMV 排序。
* gpm: 按每 1,000 次观看产生的平均 GMV 排序。
* avg_customers: 按日均客户数排序。
* sku_orders: 按已付款 SKU 订单数排序。
* items_sold: 按售出件数排序。
* views: 按 video 播放量排序。
* click_through_rate: 按商品点击量与 video 播放量的比率排序。
* post_time: 按 video 发布时间排序。 |
   sort_order |string |N |DESC |排序方向。
   可选值: ASC, DESC
   默认值: DESC
* ASC: 升序
* DESC: 降序 |
   currency |string |N |USD |目前响应中仅支持当地货币。

可选值: USD, LOCAL
默认值: LOCAL

* USD: 美元
* LOCAL: 店铺所在地的当地货币 |
   page_token |string |N |cGFnZV9udW1iZXI9MQ== |分页 token，表示当前位置。用于请求下一页数据。
   首次查询时请留空。 |
   account_type |string |N |ALL |video 创建时的账号类型。
   可选值: ALL, OFFICIAL_ACCOUNTS, MARKETING_ACCOUNTS, AFFILIATE_ACCOUNTS
   默认值: ALL
* ALL: 所有账号类型
* OFFICIAL_ACCOUNTS: 官方账号
* MARKETING_ACCOUNTS: 营销账号
* AFFILIATE_ACCOUNTS: 联盟账号 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202605/shop_videos/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-09-01&end_date_lt=2024-09-08&page_size=10&sort_field=gmv&sort_order=DESC&currency=USD&page_token=cGFnZV9udW1iZXI9MQ==&account_type=ALL
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-07 | 当地时区中数据已就绪的最新日期（ISO 8601 格式）。 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 下一页请求的分页 token。将返回的非空 token 作为下一次请求中的 `page_token` 传入，并复用相同的 `start_date_ge`、`end_date_lt`、`sort_field`、`sort_order`、`currency`、`account_type` 和 `page_size` 值。空值表示没有更多页面。 |
| ^total_count | int | 10 | 所有页面中与请求筛选条件匹配的 video 总数。 |
| ^videos | []object |  | Video performance 指标列表。 |
| ^^advertisable | bool | true | 该 video 是否可用于广告。 |
| ^^attributed_gmv | object |  | 归因于该 video 的总 GMV。 |
| ^^^amount | string | 125.50 | 对应货币的金额。 |
| ^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^avg_customers | int | 35 | 日均客户数。 |
| ^^click_through_rate | string | 0.0525 | 商品点击量与 video 播放量的比率（原始小数格式）。 |
| ^^comments | int | 12 | video 收到的评论数。 |
| ^^creator | object |  | video 的达人信息。 |
| ^^^author_type | string | OFFICIAL | 达人账号类型。 |
| ^^^creator_country | string | US | 达人所在国家或地区。 |
| ^^^creator_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | 达人 ID。 |
| ^^^nick_name | string | abc_bec | 达人昵称。 |
| ^^^open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | 达人 open ID。 |
| ^^^user_name | string | creator_shop_01 | 达人用户名（handle）。 |
| ^^ctor | string | 0.0528 | 点击到下单的转化率（原始小数格式）。 |
| ^^duration | int | 34 | video 时长，单位为秒。 |
| ^^gmv | object |  | 直接归因于该 video 的 GMV。 |
| ^^^amount | string | 125.50 | 对应货币的金额。 |
| ^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^gpm | object |  | 每 1,000 次 video 观看产生的平均 GMV。 |
| ^^^amount | string | 32.40 | 对应货币的金额。 |
| ^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^hash_tags | []string | ["#racuntiktok","fyp"] | video 的话题标签。 |
| ^^id | string | 172xxxxxxxxxxxxx089 | performance 列表中 video 的唯一标识符。 |
| ^^indirect_gmv | object |  | 间接归因于该 video 的 GMV。 |
| ^^^amount | string | 125.50 | 对应货币的金额。 |
| ^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^items_sold | int | 18 | 从该 video 售出的件数。 |
| ^^likes | int | 86 | video 收到的点赞数。 |
| ^^new_followers | int | 10 | 归因于该 video 的新增粉丝数。 |
| ^^product_clicks | int | 63 | 从该 video 产生的商品点击数。 |
| ^^product_impressions | int | 1200 | 从该 video 产生的商品曝光数。 |
| ^^products | []object |  | video 中推广的商品列表。 |
| ^^^id | string | 105xxxxxxxxxxxxx247 | 商品的唯一标识符。 |
| ^^^name | string | Wireless Earbuds | 商品名称。 |
| ^^review_type | string | IMPROVEMENT | video 的审核分类。 |
| ^^shares | int | 8 | video 被分享的次数。 |
| ^^sku_orders | int | 12 | 直接从当前 video 下单的已付款 SKU 订单总数。 |
| ^^title | string | How to Style Summer Outfits | video 标题。 |
| ^^username | string | creator_shop_01 | 与 video 关联的用户名。 |
| ^^v_to_l_clicks | int | 42 | 从 video 点击进入 LIVE 间的次数。 |
| ^^v_to_l_rate | string | 0.0350 | 从 video 点击进入 LIVE 间的比率（原始小数格式）。 |
| ^^video_finish_rate | string | 0.3800 | video 完播率（原始小数格式）。 |
| ^^video_post_time | string | 2025-01-01 00:00:00 | video 发布的日期和时间。 |
| ^^views | int | 1200 | 所选时间范围内的 video 播放量。 |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-07","next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":10,"videos":[{"advertisable":true,"attributed_gmv":{"amount":"125.50","currency":"USD"},"avg_customers":35,"click_through_rate":"0.0525","comments":12,"creator":{"author_type":"OFFICIAL","creator_country":"US","creator_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","nick_name":"abc_bec","open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","user_name":"creator_shop_01"},"ctor":"0.0528","duration":34,"gmv":{"amount":"125.50","currency":"USD"},"gpm":{"amount":"32.40","currency":"USD"},"hash_tags":["#racuntiktok","fyp"],"id":"172xxxxxxxxxxxxx089","indirect_gmv":{"amount":"125.50","currency":"USD"},"items_sold":18,"likes":86,"new_followers":10,"product_clicks":63,"product_impressions":1200,"products":[{"id":"105xxxxxxxxxxxxx247","name":"Wireless Earbuds"}],"review_type":"IMPROVEMENT","shares":8,"sku_orders":12,"title":"How to Style Summer Outfits","username":"creator_shop_01","v_to_l_clicks":42,"v_to_l_rate":"0.0350","video_finish_rate":"0.3800","video_post_time":"2025-01-01 00:00:00","views":1200}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 28001022 | invalid request params; detail: start time or end time is invalid. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

