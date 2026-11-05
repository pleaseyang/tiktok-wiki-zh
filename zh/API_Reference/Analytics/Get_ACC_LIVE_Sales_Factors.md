# 获取 ACC 直播销售因素

# Path: /analytics/202610/acc/preferences/live/factors
# Method: [GET]
# 功能描述
获取所选 ACC 受众、范围和报告窗口的 LIVE 类型（销售因素）分页排名。每个因素包含其 ID、显示名称、GMV 范围以及客户和订单数量。

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
| brand_id | string | Y | 1000001 | 要分析的品牌 ID。从当前店铺的 Get ACC Brands (GET /analytics/202610/acc/brands) 返回的同一条目中获取 brand_id 及其关联的 industry_id。 |
| industry_id | string | Y | 9000001 | 与 brand_id 关联的行业 ID，用于确定可用的报告日期。从 Get ACC Brands (GET /analytics/202610/acc/brands) 返回的同一品牌条目中获取。 |
| date | string | N | 2026-09-20 | 报告窗口的包含结束日期，格式为 YYYY-MM-DD（UTC）。如果省略，则使用最新可用日期。由 date 和 trend_days 选择的整个窗口必须在 earliest_available_date 和 latest_available_date 之间。使用与将消费这些因素 ID 的 LIVE 偏好列表请求相同的 date 和 trend_days。 |
| trend_days | int | N | 30 | 报告窗口的日历天数长度，包括 date。允许值：7、14、30。默认值：30。开始日期为 date 减去 (trend_days - 1) 天。 |
| audience_type | string | Y | CONVERSION | 对其 LIVE 偏好进行排名的受众细分。允许值：SHOP_NON_EXPOSED、SHOP_CLICKED_NOT_PURCHASED、CONVERSION、NEW_CONVERSION、REPEAT_CONVERSION、DTC_NEW_CONVERSION、DTC_REPEAT_CONVERSION。细分定义：SHOP_NON_EXPOSED 表示未暴露于店铺的人；SHOP_CLICKED_NOT_PURCHASED 表示点击了店铺但未购买的人；CONVERSION 表示完成购买的人；NEW_CONVERSION 表示首次店铺买家；REPEAT_CONVERSION 表示复购买家。DTC_NEW_CONVERSION 和 DTC_REPEAT_CONVERSION 选择相应的 DTC 新转化和复购队列。偏好 API 不支持 ACC、AWARENESS、CONSIDERATION 和 DRC 前缀的值。 |
| scope | string | N | MY_SHOP | 排名范围：MY_SHOP 为当前店铺，或 MARKET 为市场。默认值：MY_SHOP。 |
| category_id | string | N | 2001 | 用于选择特定类目 LIVE 因素排名的类目 ID。如果省略，则选择聚合类目（-1）；这不会合并所有特定类目的行。使用 Market 类目 API 中的 LIVE Market 类目 ID。商品 L2/L3 类目 ID 在此处无效。如果提供了类目，请在相应的 LIVE 偏好列表请求中重用。 |
| keyword | string | N | label1 | LIVE 类型标识符、显示名称或类目 ID 的不区分大小写的子字符串过滤。如果省略或为空，则不应用关键字过滤。 |
| sort_field | string | N | GMV | 用于排序因素的指标：GMV、CUSTOMERS 或 ORDERS。默认值：GMV。GMV 排序使用格式化为 gmv_range 之前的数值金额。 |
| sort_order | string | N | DESC | sort_field 的排序方向：ASC 为升序，DESC 为降序。默认值：DESC。 |
| page_size | int | N | 10 | 每页返回的最大因素数。允许值：10、20、50、100。默认值：10。 |
| page_token | string | N | cGFnZV9udW1iZXI9MQ== | 上一个响应中 next_page_token 的分页 token。第一页省略此参数。对于后续页面，将返回的 token 原样作为 page_token 传递，并保持所有其他请求参数不变。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/preferences/live/factors?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&brand_id=1000001&industry_id=9000001&date=2026-09-20&trend_days=30&audience_type=CONVERSION&scope=MY_SHOP&category_id=2001&keyword=label1&sort_field=GMV&sort_order=DESC&page_size=10&page_token=cGFnZV9udW1iZXI9MQ==
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^earliest_available_date | string | 2026-08-21 | 所请求店铺、品牌和行业的最早可用报告日期，格式为 YYYY-MM-DD（UTC）。报告窗口不得早于此日期开始。 |
| ^end_date | string | 2026-09-20 | 报告窗口的包含结束日期，格式为 YYYY-MM-DD（UTC）。为提供的 date，或在省略 date 时为 latest_available_date。 |
| ^factors | []object |  | 当前页面的 LIVE 类型因素，按 sort_field 和 sort_order 排序。空数组表示此页面和选择未返回任何因素。 |
| ^^factor_id | string | label1 | 稳定的 LIVE 因素标识符，如 label1。在 Get ACC Audience Preference List 中过滤 LIVE 时，将此值原样作为 factor_id 传递；不要传递 factor_name。 |
| ^^factor_name | string | Stable, non-shaky image | LIVE 因素的本地化显示名称（可用时）。过滤 LIVE 偏好时使用 factor_id 而非此显示名称。 |
| ^^metrics | object |  | 所选受众、范围和报告窗口中此 LIVE 因素的 GMV 范围、客户数量和订单数量。 |
| ^^^customers | string | 4210 | 所选受众、范围和报告窗口中此 LIVE 类型的客户数量，以数值字符串表示。 |
| ^^^gmv_range | string | $331,451.00 ~ $331,500.00 | 所选受众、范围和报告窗口内此 LIVE 类型的商品总额 (GMV)，以当前店铺货币的格式化范围表示。零 GMV 返回为格式化的零而非范围。 |
| ^^^orders | string | 8566 | 所选受众、范围和报告窗口中此 LIVE 类型的订单数量，以数值字符串表示。 |
| ^latest_available_date | string | 2026-09-20 | 所请求店铺、品牌和行业的最新可用报告日期，格式为 YYYY-MM-DD（UTC）。这是省略 date 时的默认 end_date。 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 下一页的 token。在下一次请求中将此值原样作为 page_token 传递，并保持所有其他请求参数不变。空字符串表示没有更多页面。 |
| ^start_date | string | 2026-08-22 | 报告窗口的包含开始日期，格式为 YYYY-MM-DD（UTC），计算方式为 end_date 减去 (trend_days - 1) 天。 |
| ^total_count | int | 1 | 分页前匹配所选范围、类目和关键字的因素行总数。 |
# 响应示例
```json
{"code":0,"data":{"earliest_available_date":"2026-08-21","end_date":"2026-09-20","factors":[{"factor_id":"label1","factor_name":"Stable, non-shaky image","metrics":{"customers":"4210","gmv_range":"$331,451.00 ~ $331,500.00","orders":"8566"}}],"latest_available_date":"2026-09-20","next_page_token":"cGFnZV9udW1iZXI9MQ==","start_date":"2026-08-22","total_count":1},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

