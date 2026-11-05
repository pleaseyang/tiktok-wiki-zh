# 获取站外表现详情

# Path: /analytics/202610/off_site/details
# Method: [GET]
# 功能描述
获取 video、LIVE 场次或商品的分页每周站外 performance 详情，包括 GMV 和站外效果指标。
如果请求的 Pixel 和归因设置的报告不可用，结果可能使用 VIEW_14D 归因的店铺级报告。如果两个报告都不可用，则不返回内容记录。

---


# 公共参数
公共参数，请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| date | string | N | 2026-09-09 | 请求报告周中的某一天，格式为 YYYY-MM-DD。每个报告周从周日到周六（店铺报告时区）。对于两种归因设置，最早支持的报告周从 2026-06-14 开始。选择最新可用周或之前 11 周中的某一。如果省略，则使用最新可用周。 |
| pixel_id | string | Y | 12323123123 | 授权店铺的 Pixel ID。使用同一店铺的 GET /analytics/202610/off_site/pixels 返回的 pixel_id。不属于该店铺的 ID 可能会回退到店铺级报告，而不是返回 Pixel 特定数据。 |
| attribution_setting | string | Y | VIEW_14D | 站外购买的归因设置。允许值：VIEW_14D（客户在购买前 14 天内浏览了 TikTok Shop 商业内容）和 CLICK_14D_OR_VIEW_1D（客户在购买前 14 天内点击或 1 天内浏览）。同时满足两个条件的购买只计算一次。如果请求的报告不可用，店铺级回退报告可能使用 VIEW_14D。 |
| content_type | string | Y | VIDEO | 要检索的项目类型。允许值： |

* VIDEO：video。
* LIVE：直播场次。
* PRODUCT：商品。 |
   sort_field |string |N |total_gmv |用于排序报告候选集的指标。允许值：off_site_gmv、tiktok_shop_gmv、total_gmv 和 off_site_effect_rate。默认值：total_gmv。指标值相同的记录没有保证的次要排序，包括跨页面请求。 |
   sort_order |string |N |DESC |排序方向。允许值：ASC（升序）和 DESC（降序）。默认值：DESC。 |
   page_size |int |N |10 |每页返回的最大记录数。支持的值：10、20 和 50。默认值：10。相同的值适用于 VIDEO、LIVE 和 PRODUCT 详情。 |
   page_token |string |N |cGFnZV9udW1iZXI9MQ== |上一个响应中 next_page_token 的分页 token。第一页省略此参数。对于后续页面，将返回的 token 原样作为 page_token 传递，并保持所有其他请求参数不变。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/off_site/details?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&date=2026-09-09&pixel_id=12323123123&attribution_setting=VIEW_14D&content_type=VIDEO&sort_field=total_gmv&sort_order=DESC&page_size=10&page_token=cGFnZV9udW1iZXI9MQ==
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^contents | []object |  | 当前页面中的 performance 记录，按请求的排序顺序排列。报告为四个降序指标排名各选择最多 100 个项目：tiktok_shop_gmv、off_site_gmv、total_gmv 和 off_site_effect_rate。GMV 排名要求排名指标为正值；效果比率排名要求两个 GMV 值均为正值。结果是这些选择的并集，按内容 ID 去重。请求的排序和分页仅适用于此子集，该子集可能不包含请求的 content_type 的每个项目。可用的元数据取决于 content_type。 |
| ^^content_id | string | 7000000000000000001 | VIDEO 项目的 video ID、LIVE 项目的 LIVE 房间 ID 或 PRODUCT 项目的商品 ID。 |
| ^^content_type | string | VIDEO | 项目类型：VIDEO（video）、LIVE（LIVE 场次）或 PRODUCT（商品）。 |
| ^^cover_image_url | string | https://example.com/video-cover.jpg | video、LIVE 场次或商品的封面图片 URL（可用时）。 |
| ^^creator | object |  | VIDEO 项目的创作者信息（元数据可用时）。LIVE 和 PRODUCT 项目不提供创作者信息。缺失的创作者信息返回为 null。 |
| ^^^avatar_url | string | https://example.com/creator-avatar.jpg | video 创作者的头像图片 URL（可用时）。 |
| ^^^id | string | 7000000000000000002 | video 创作者的 TikTok 用户 ID，以字符串表示。 |
| ^^^name | string | demo_creator | video 创作者的显示名称（可用时）。 |
| ^^duration_seconds | int | 38 | VIDEO 或 LIVE 场次的时长（秒）（可用时）。不适用于 PRODUCT 项目；缺失或不适用的元数据可能为 null。 |
| ^^metrics | object |  | 报告周内此项目的 GMV 和站外效果指标。 |
| ^^^off_site_effect_rate | string | 0.2500 | 报告周内此项目的站外 GMV 除以 TikTok Shop GMV，以小数比率表示；1.0000 表示 100%，比率可以超过 1。null 值表示比率不可用，不得解释为零；响应不说明不可用的原因。 |
| ^^^off_site_gmv | object |  | 报告周内归因于此项目的站外 GMV。 |
| ^^^^amount | string | 1000.00 | GMV 金额，以小数字符串表示。小数位数不固定。 |
| ^^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^^tiktok_shop_gmv | object |  | 报告周内此项目的 TikTok Shop GMV。它在店铺和项目级别聚合，与 pixel_id 和 attribution_setting 无关。 |
| ^^^^amount | string | 4000.00 | GMV 金额，以小数字符串表示。小数位数不固定。 |
| ^^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^^total_gmv | object |  | 报告周内此项目的 TikTok Shop GMV 与站外 GMV 之和。 |
| ^^^^amount | string | 5000.00 | GMV 金额，以小数字符串表示。小数位数不固定。 |
| ^^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^post_time | string | 2026-09-08T15:26:40Z | VIDEO 项目的发布时间或 LIVE 场次的开始时间，以带时区的 ISO 8601 时间戳表示。不适用于 PRODUCT 项目；不可用的元数据可能为 null。 |
| ^^rank | int | 1 | 当前排序结果集中从一开始的显示位置，跨页面连续。这不是稳定的业务排名；排序值相同的记录可能在请求之间改变顺序。 |
| ^^title | string | Demo product styling video | Video 标题、LIVE 场次标题或商品名称，取决于 content_type（可用时）。 |
| ^latest_available_date | string | 2026-09-12 | 店铺报告时区内的最新可用报告日期，格式为 YYYY-MM-DD。省略 date 时选择包含该日期的周。与之前的 11 个报告周一起定义支持的查询窗口；可用日期不保证每个 Pixel 和归因设置都有数据。 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 下一页的 token。在下一次请求中将此值原样作为 page_token 传递，并保持所有其他请求参数不变。空字符串表示没有更多页面。 |
| ^total_count | int | 1 | 当前报告周、Pixel、归因设置和内容类型的报告候选集中唯一项目的总数，在分页和元数据丰富之前。这不是当前页面中的项目数量或店铺中所有匹配项目的数量。缺失或已删除的内容元数据不会减少计数。 |
# 响应示例
```json
{"code":0,"data":{"contents":[{"content_id":"7000000000000000001","content_type":"VIDEO","cover_image_url":"https://example.com/video-cover.jpg","creator":{"avatar_url":"https://example.com/creator-avatar.jpg","id":"7000000000000000002","name":"demo_creator"},"duration_seconds":38,"metrics":{"off_site_effect_rate":"0.2500","off_site_gmv":{"amount":"1000.00","currency":"USD"},"tiktok_shop_gmv":{"amount":"4000.00","currency":"USD"},"total_gmv":{"amount":"5000.00","currency":"USD"}},"post_time":"2026-09-08T15:26:40Z","rank":1,"title":"Demo product styling video"}],"latest_available_date":"2026-09-12","next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":1},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

