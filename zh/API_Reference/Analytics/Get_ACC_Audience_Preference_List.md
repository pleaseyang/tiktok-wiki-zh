# 获取 ACC 受众偏好列表

# Path: /analytics/202610/acc/preferences
# Method: [GET]
# 功能描述
获取品牌的所选 ACC 受众偏好的商品、直播、video 或图文帖子的分页排名。
使用 `entity_type` 选择排名类型。每个条目包含其排名、实体信息和偏好指标；`entity_detail` 因实体类型而异。使用 `date` 和 `trend_days` 选择分析窗口，使用 `scope` 选择店铺级或市场级结果。要获取更多结果，将返回的 `page_token` 作为下一次请求中的 `page_token` 传递。

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
| brand_id | string | Y | 1000001 | 要分析的授权品牌 ID。去除周围空白后，此值必须非空。使用当前店铺的 Get ACC Brands (GET /analytics/202610/acc/brands) 返回的同一记录中的 brand_id 和 industry_id。 |
| industry_id | string | Y | 9000001 | 用于确定可用分析日期的行业 ID。去除周围空白后，此值必须非空。使用与 brand_id 相同的 Get ACC Brands 记录中的 industry_id。 |
| date | string | N | 2026-09-20 | 分析窗口的结束日期，格式为 `YYYY-MM-DD`（UTC）。省略时默认为最新可用日期。整个窗口（包括由 `trend_days` 确定的开始日期）必须在 `earliest_available_date` 和 `latest_available_date` 范围内。 |
| trend_days | int | N | 30 | 分析窗口中的日历天数，包括 date。支持的值：7、14、30。省略或设为 0 时默认为 30。开始日期为 date 减去 (trend_days - 1) 天。 |
| audience_type | string | Y | CONVERSION | 要分析的 ACC 受众细分。支持的值：`SHOP_NON_EXPOSED`、`SHOP_CLICKED_NOT_PURCHASED`、`CONVERSION`、`NEW_CONVERSION`、`REPEAT_CONVERSION`、`DTC_NEW_CONVERSION`、`DTC_REPEAT_CONVERSION`。细分定义：SHOP_NON_EXPOSED 表示未暴露于店铺的人；SHOP_CLICKED_NOT_PURCHASED 表示点击了店铺但未购买的人；CONVERSION 表示完成购买的人；NEW_CONVERSION 表示首次店铺买家；REPEAT_CONVERSION 表示复购买家。DTC_NEW_CONVERSION 和 DTC_REPEAT_CONVERSION 选择相应的 DTC 新转化和复购队列。偏好 API 不支持 ACC、AWARENESS、CONSIDERATION 和 DRC 前缀的值。 |
| entity_type | string | Y | PRODUCT | 要排名的实体类型。支持的值：PRODUCT（商品）、LIVE（直播）、VIDEO（video）和 PHOTO（图文帖子）；匹配不区分大小写。items[].entity_detail 中的字段取决于此值。对于类目和因素过滤，PRODUCT 支持 l2_category_id 和 l3_category_id；LIVE 支持 category_id 和 factor_id；VIDEO 和 PHOTO 支持 category_id。为不支持的实体类型提供这些类目或因素过滤中的任何一个均无效。 |
| scope | string | N | MY_SHOP | 排名范围。支持的值：`MY_SHOP`（店铺级结果）、`MARKET`（市场级结果）。默认值：`MY_SHOP`。 |
| keyword | string | N | Demo | 可选搜索过滤。 |

* `PRODUCT`：数值型商品 ID 执行精确 ID 匹配；否则，关键字为商品名称的区分大小写的子字符串。
* `LIVE`：对直播 ID、直播类型、类目或标题进行不区分大小写的子字符串匹配。
* `VIDEO` 或 `PHOTO`：对内容 ID、创作者 ID、标题、创作者别名或创作者账号进行不区分大小写的子字符串匹配。
   省略、为空或仅含空白字符的值不应用关键字过滤。不应用关键字长度验证。 |
   l2_category_id |string |N |848648 |用于过滤的2级商品类目 ID。仅支持 `entity_type=PRODUCT`；其他实体类型请省略。提供 `l3_category_id` 时必填。使用 `GET /analytics/202610/acc/preferences/product/categories` 返回的 `category_level=2` 的 `category_id`，以相同的店铺、品牌、行业、受众、分析窗口和范围查询。 |
   l3_category_id |string |N |601529 |用于过滤的3级商品类目 ID。仅支持 `entity_type=PRODUCT` 且要求 `l2_category_id` 非空；其他实体类型请省略。省略以使用默认的3级类目选择；提供以选择特定的3级类目。使用 `GET /analytics/202610/acc/preferences/product/categories` 返回的所选2级类目下的3级子 `category_id`，以相同的店铺、品牌、行业、受众、分析窗口和范围查询。 |
   category_id |string |N |2001 |`entity_type=LIVE`、`VIDEO` 或 `PHOTO` 用于过滤的类目 ID。`PRODUCT` 请省略此参数。对于 `LIVE`，省略不应用类目过滤。对于 `VIDEO` 和 `PHOTO`，省略使用默认类目选择；提供类目 ID 以选择特定类目。 |
   factor_id |string |N |label1 |用于过滤的直播类型 ID。仅支持 `entity_type=LIVE`；其他实体类型请省略。省略此参数不应用直播类型过滤。使用 `GET /analytics/202610/acc/preferences/live/factors` 返回的 `factor_id`，以相同的店铺、品牌、行业、受众、分析窗口、范围和任何所选 `category_id` 查询。此值用作稳定的查询标识符；不要传递显示名称 factor_name。 |
   sort_field |string |N |GMV |用于排序排名的指标。支持的值：`GMV`、`CUSTOMERS`、`ORDERS`。默认值：`GMV`。 |
   sort_order |string |N |DESC |`sort_field` 的排序方向。支持的值：`DESC`（降序）、`ASC`（升序）。默认值：`DESC`。 |
   page_size |int |N |10 |每页返回的最大排名条目数。允许值：10、20、50、100。默认值：10。 |
   page_token |string |N |cGFnZV9udW1iZXI9MQ== |上一个响应中作为 `page_token` 返回的分页 token。第一页省略此参数。将返回的 token 原样传递以获取下一页，保持相同的 `page_size`、过滤和排序设置。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/preferences?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&brand_id=1000001&industry_id=9000001&date=2026-09-20&trend_days=30&audience_type=CONVERSION&entity_type=PRODUCT&scope=MY_SHOP&keyword=Demo&l2_category_id=848648&l3_category_id=601529&category_id=2001&factor_id=label1&sort_field=GMV&sort_order=DESC&page_size=10&page_token=cGFnZV9udW1iZXI9MQ==
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^audience_type | string | CONVERSION | 用于此排名的 ACC 受众细分，对应请求的 `audience_type`。 |
| ^earliest_available_date | string | 2026-08-21 | 所选店铺、品牌和行业的最早可用分析日期，格式为 `YYYY-MM-DD`（UTC）。分析窗口不得早于此日期开始。 |
| ^end_date | string | 2026-09-20 | 分析窗口的包含结束日期，格式为 `YYYY-MM-DD`（UTC）。等于请求的 `date`，或在省略 `date` 时为最新可用日期。 |
| ^entity_type | string | PRODUCT | 此排名中的实体类型：`PRODUCT`、`LIVE`、`VIDEO` 或 `PHOTO`，对应请求的 `entity_type`。 |
| ^items | []object |  | 请求的 `entity_type` 在当前分页中的排名实体列表，已应用所选受众、范围和过滤条件。每个条目包含其排名、实体信息和偏好指标。空数组表示所选实体和过滤条件下无结果；缺失的实体元数据不会移除原本有效的指标记录。 |
| ^^entity_cover | string | https://example.com/images/product-001.jpg | 商品、直播、video 或图文帖子的封面图片 URL（可用时）。对于 `PHOTO`，这是第一个图片 URL。 |
| ^^entity_detail | object |  | 所选实体类型的附加详情（可用时）： |

* `PRODUCT`: `product_url`, `l2_category_id`, `l3_category_id`.
* `LIVE`: `live_start_time`, `replay_url`.
* `VIDEO` 或 `PHOTO`：`post_time`、`creator_id`、`creator_name`。 |
   ^^^creator_id |string |1000000000000000004 |video 或图文帖子的创作者 ID（可用时）。适用于 `VIDEO` 和 `PHOTO`。 |
   ^^^creator_name |string |Demo Creator |video 或图文帖子的创作者显示名称（可用时）。适用于 `VIDEO` 和 `PHOTO`。 |
   ^^^l2_category_id |string |848648 |排名商品的2级类目 ID。适用于 `PRODUCT`。 |
   ^^^l3_category_id |string |601529 |与此排名条目关联的3级类目标识符。适用于 `PRODUCT`。值 `-1` 表示默认的3级类目选择。 |
   ^^^live_start_time |string |2026-09-18 |直播开始的 UTC 日历日期，格式为 `YYYY-MM-DD`（可用时）。适用于 `LIVE`。 |
   ^^^post_time |string |2026-09-18 |video 或图文帖子的 UTC 发布日期，格式为 `YYYY-MM-DD`（可用时）。适用于 `VIDEO` 和 `PHOTO`。 |
   ^^^product_url |string |https://example.com/products/1000000000000000001 |排名商品的链接（可用时）。适用于 `PRODUCT`。 |
   ^^^replay_url |string |https://example.com/live/1000000000000000005/replay |直播回放的链接（可用时）。适用于 `LIVE`。 |
   ^^entity_id |string |1000000000000000001 |排名实体的 ID：`PRODUCT` 的商品 ID、`LIVE` 的直播间 ID、`VIDEO` 的 video ID 或 `PHOTO` 的图文帖子 ID。 |
   ^^entity_name |string |Demo Makeup Set |`PRODUCT` 的商品名称、`LIVE` 的直播标题或 `VIDEO` 和 `PHOTO` 的内容标题（可用时）。 |
   ^^metrics |object | |所选受众、范围和分析窗口内此实体的偏好指标。 |
   ^^^customers |string |4210 |所选受众、范围和分析窗口内此实体的客户数量，以字符串表示。 |
   ^^^gmv_range |string |$331,451.00 ~ $331,500.00 |此实体的格式化商品总额 (GMV) 范围，使用店铺货币。零表示为格式化的零而非范围。正 GMV 按店铺本地货币的 50 单位区间分组。格式化值返回时不转换为其他货币。 |
   ^^^orders |string |8566 |所选受众、范围和分析窗口内此实体的订单数量，以字符串表示。 |
   ^^rank |int |1 |此条目在请求排序中从一开始的位置，跨页面连续。这是当前分页序列的显示位置，不是稳定的业务排名。 |
   ^latest_available_date |string |2026-09-20 |所选店铺、品牌和行业的最新可用分析日期，格式为 `YYYY-MM-DD`（UTC）。当请求 `date` 被省略时用作分析结束日期。 |
   ^next_page_token |string |cGFnZV9udW1iZXI9MQ== |下一页的 token。在下一次请求中将此值原样作为 page_token 传递，并保持所有其他请求参数不变。空字符串表示没有更多页面。 |
   ^scope |string |MY_SHOP |此排名使用的范围：`MY_SHOP` 为店铺级结果，`MARKET` 为市场级结果。 |
   ^start_date |string |2026-08-22 |分析窗口的包含开始日期，格式为 `YYYY-MM-DD`（UTC）。计算方式为 `end_date` 减去 `trend_days - 1` 天。 |
   ^total_count |int |1 |过滤后分页前的匹配排名条目总数。 |

# 响应示例
```json
{"code":0,"data":{"audience_type":"CONVERSION","earliest_available_date":"2026-08-21","end_date":"2026-09-20","entity_type":"PRODUCT","items":[{"entity_cover":"https://example.com/images/product-001.jpg","entity_detail":{"creator_id":"1000000000000000004","creator_name":"Demo Creator","l2_category_id":"848648","l3_category_id":"601529","live_start_time":"2026-09-18","post_time":"2026-09-18","product_url":"https://example.com/products/1000000000000000001","replay_url":"https://example.com/live/1000000000000000005/replay"},"entity_id":"1000000000000000001","entity_name":"Demo Makeup Set","metrics":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"},"rank":1}],"latest_available_date":"2026-09-20","next_page_token":"cGFnZV9udW1iZXI9MQ==","scope":"MY_SHOP","start_date":"2026-08-22","total_count":1},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

