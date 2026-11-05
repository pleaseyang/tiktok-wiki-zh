# 获取 ACC 热销类目

# Path: /analytics/202610/acc/preferences/product/categories
# Method: [GET]
# 功能描述
获取所选受众、品牌和日期窗口的 ACC 商品类目销售排名。结果包含2级类目及其3级子类目；排序和分页作用于2级类目。

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
| brand_id | string | Y | 1000001 | ACC 品牌 ID。使用同一店铺的 Get ACC Brands (GET /analytics/202610/acc/brands) 返回的 brand_id。 |
| industry_id | string | Y | 9000001 | ACC 行业 ID，与 brand_id 一起用于确定可用数据日期。使用 Get ACC Brands (GET /analytics/202610/acc/brands) 与该品牌一起返回的 industry_id。 |
| date | string | N | 2026-09-20 | 数据窗口的包含结束日期，UTC 时间，格式为 YYYY-MM-DD。省略时默认为最新可用日期。整个 trend_days 窗口（包括其开始日期）必须在 earliest_available_date 和 latest_available_date 之间。使用与将消费这些类目 ID 的商品偏好列表请求相同的 date 和 trend_days。 |
| trend_days | int | N | 30 | 数据窗口中的天数，包括 date。有效值：7、14、30。默认值：30。开始日期为 date - (trend_days - 1) 天。 |
| audience_type | string | Y | CONVERSION | 用于类目排名的 ACC 受众细分。有效值：SHOP_NON_EXPOSED、SHOP_CLICKED_NOT_PURCHASED、CONVERSION、NEW_CONVERSION、REPEAT_CONVERSION、DTC_NEW_CONVERSION、DTC_REPEAT_CONVERSION。细分定义：SHOP_NON_EXPOSED 表示未暴露于店铺的人；SHOP_CLICKED_NOT_PURCHASED 表示点击了店铺但未购买的人；CONVERSION 表示完成购买的人；NEW_CONVERSION 表示首次店铺买家；REPEAT_CONVERSION 表示复购买家。DTC_NEW_CONVERSION 和 DTC_REPEAT_CONVERSION 选择相应的 DTC 新转化和复购队列。偏好 API 不支持 ACC、AWARENESS、CONSIDERATION 和 DRC 前缀的值。 |
| scope | string | N | MY_SHOP | 类目指标的范围。有效值：MY_SHOP（店铺数据）、MARKET（市场数据）。默认值：MY_SHOP。 |
| keyword | string | N | Makeup | 按类目 ID 或类目名称的不区分大小写的子字符串过滤类目。过滤在构建和分页类目树之前应用。省略此参数以禁用关键字过滤。 |
| sort_field | string | N | GMV | 用于排序2级类目的指标。有效值：GMV、CUSTOMERS、ORDERS。默认值：GMV。值相同的类目按类目 ID 升序排列。3级子类目单独按类目 ID 排序。 |
| sort_order | string | N | DESC | 2级类目的排序方向。有效值：ASC（升序）、DESC（降序）。默认值：DESC。 |
| page_size | int | N | 10 | 每页的最大2级类目数。允许值：10、20、50、100。默认值：10。3级子类目不计入此限制。 |
| page_token | string | N | cGFnZV9udW1iZXI9MQ== | 上一个响应中 next_page_token 的分页 token。第一页省略此参数。对于后续页面，将返回的 token 原样作为 page_token 传递，并保持所有其他请求参数不变。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/preferences/product/categories?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&brand_id=1000001&industry_id=9000001&date=2026-09-20&trend_days=30&audience_type=CONVERSION&scope=MY_SHOP&keyword=Makeup&sort_field=GMV&sort_order=DESC&page_size=10&page_token=cGFnZV9udW1iZXI9MQ==
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^categories | []object |  | 当前页面的2级类目排名，包含范围和关键字过滤后的3级子类目。排序、page_size 和 page_token 作用于此顶级列表。 |
| ^^category_id | string | 848648 | 2级商品类目的 ID。在 Get ACC Audience Preference List 中查询 PRODUCT 时，将此 ID 作为 l2_category_id 传递。这些商品类目 ID 不是用于 LIVE、VIDEO 或 PHOTO 的 Market 类目 ID。 |
| ^^category_level | int | 2 | 商品类目级别。此节点的值为 2。 |
| ^^category_name | string | Makeup | 2级商品类目的名称。 |
| ^^children | []object |  | 此2级类目下的3级类目，经过范围和关键字过滤后，按类目 ID 升序排列。此列表不分页。 |
| ^^^category_id | string | 601529 | 3级商品类目的 ID。要查询此节点的 PRODUCT 偏好，将此 ID 作为 l3_category_id 传递，同时将父2级 category_id 作为 l2_category_id 传递。 |
| ^^^category_level | int | 3 | 商品类目级别。此节点的值为 3。 |
| ^^^category_name | string | Makeup Sets | 3级商品类目的名称。 |
| ^^^metrics | object |  | 此3级类目在所选受众、范围和日期窗口内报告的销售指标。 |
| ^^^^customers | string | 4210 | 此类目在所选受众、范围和日期窗口内报告的客户数量。 |
| ^^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 此类目的格式化商品总额 (GMV) 范围，使用店铺货币。零显示为格式化的零金额。 |
| ^^^^orders | string | 8566 | 此类目在所选受众、范围和日期窗口内报告的订单数量。 |
| ^^metrics | object |  | 此2级类目在所选受众、范围和日期窗口内报告的销售指标（可用时）。 |
| ^^^customers | string | 4210 | 此类目在所选受众、范围和日期窗口内报告的客户数量。 |
| ^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 此类目的格式化商品总额 (GMV) 范围，使用店铺货币。零显示为格式化的零金额。 |
| ^^^orders | string | 8566 | 此类目在所选受众、范围和日期窗口内报告的订单数量。 |
| ^earliest_available_date | string | 2026-08-21 | 所请求店铺、品牌和行业的最早可用 UTC 数据日期，格式为 YYYY-MM-DD。start_date 不得早于此日期。 |
| ^end_date | string | 2026-09-20 | 用于排名的数据窗口的包含结束日期，UTC 时间，格式为 YYYY-MM-DD。为请求的日期，或在省略 date 时为最新可用日期。 |
| ^latest_available_date | string | 2026-09-20 | 所请求店铺、品牌和行业的最新可用 UTC 数据日期，格式为 YYYY-MM-DD。省略 date 时用作 end_date。 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 下一页的 token。在下一次请求中将此值原样作为 page_token 传递，并保持所有其他请求参数不变。空字符串表示没有更多页面。 |
| ^start_date | string | 2026-08-22 | 用于排名的数据窗口的包含开始日期，UTC 时间，格式为 YYYY-MM-DD。为 end_date - (trend_days - 1) 天。 |
| ^total_count | int | 1 | 分页前匹配的2级类目总数。3级子类目不包括在内。 |
# 响应示例
```json
{"code":0,"data":{"categories":[{"category_id":"848648","category_level":2,"category_name":"Makeup","children":[{"category_id":"601529","category_level":3,"category_name":"Makeup Sets","metrics":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"metrics":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"earliest_available_date":"2026-08-21","end_date":"2026-09-20","latest_available_date":"2026-09-20","next_page_token":"cGFnZV9udW1iZXI9MQ==","start_date":"2026-08-22","total_count":1},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

