# 获取 ACC 受众渗透率

# Path: /analytics/202610/acc/penetration
# Method: [GET]
# 功能描述
获取品牌在所选报告窗口内的已观看、已点击和已下单受众数量及渗透率。
使用当前店铺的 Get ACC Brands (GET /analytics/202610/acc/brands) 返回的同一 brands[] 记录中的 brand_id 和 industry_id。使用 audience_type 选择初始受众；account_type 和 form 过滤报告的受众细分。

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
| brand_id | string | Y | 1000001 | 要分析的品牌 ID。使用当前店铺的 Get ACC Brands 返回的 brands[] 记录中的 brand_id，以及同一记录中的 industry_id。不能为空。 |
| industry_id | string | Y | 9000001 | 用于确定可用报告日期的行业 ID。使用与 brand_id 相同的 Get ACC Brands brands[] 记录中的 industry_id。不能为空。 |
| date | string | N | 2026-09-20 | 报告窗口的包含结束日期，格式为 YYYY-MM-DD（UTC）。如果省略或为空，则使用最新可用日期。trend_days 选择的整个窗口必须在所选店铺、品牌和行业的可用日期范围内。 |
| trend_days | int | N | 30 | 报告窗口中的日历天数，包括 date。支持的值：7、14、30。省略或设为 0 时默认为 30。 |
| account_type | string | N | ALL | 用于过滤报告细分的账户类型。支持的值：ALL（所有账户类型）、LINK_ACCOUNT（店铺关联账户）、CREATOR_ACCOUNT（联盟创作者账户）。省略或为空时默认为 ALL。 |
| form | string | N | ALL | 用于过滤报告细分的内容形式。支持的值：ALL（所有形式）、PRODUCT（商品卡片）、VIDEO（短视频）、LIVE（直播）、PHOTO（图文帖子）。省略或为空时默认为 ALL。 |
| audience_type | string | N | ACC | 用作渗透率基准的初始受众细分。支持的值：ACC（认知、考虑和转化受众的去重并集）、AWARENESS（暴露于或浏览了品牌内容或商品的人）、CONSIDERATION（点击、加购物车、关注或以其他方式表现出更深兴趣的人）、CONVERSION（购买者）、NEW_CONVERSION（首次店铺买家）和 REPEAT_CONVERSION（复购买家）。省略或为空时默认为 ACC。基准数量在报告窗口开始时取值。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/penetration?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&brand_id=1000001&industry_id=9000001&date=2026-09-20&trend_days=30&account_type=ALL&form=ALL&audience_type=ACC
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^funnel | object | {"clicked":{"not_rate":"80.00%","not_value":21600000,"rate":"20.00%","value":5400000},"ordered":{"not_rate":"96.30%","not_value":26000000,"rate":"3.70%","value":1000000},"total":{"value":27000000},"viewed":{"not_rate":"50.00%","not_value":13500000,"rate":"50.00%","value":13500000}} | 所选报告窗口的受众渗透漏斗。所有细分比例使用窗口开始时所选初始受众数量作为分母。当细分受众不超过 1,000 人时，细分数量和比率不可用；不可用的值不应解释为零。 |
| ^^clicked | object | {"not_rate":"80.00%","not_value":21600000,"rate":"20.00%","value":5400000} | 所选报告窗口中已点击和未点击的受众细分，包含数量和与初始受众基准的比率。 |
| ^^^not_rate | string | 80.00% | clicked.not_value 所占初始受众的百分比，计算公式为 clicked.not_value / funnel.total.value * 100，以百分比字符串返回，例如 "55.12%"。不要将返回的百分比再乘以 100。当初始受众数量不为正数时不可用。 |
| ^^^not_value | int | 21600000 | 所选报告窗口中未点击细分的受众数量。 |
| ^^^rate | string | 20.00% | clicked.value 所占初始受众的百分比，计算公式为 clicked.value / funnel.total.value * 100，以百分比字符串返回，例如 "44.88%"。不要将返回的百分比再乘以 100。当初始受众数量不为正数时不可用。 |
| ^^^value | int | 5400000 | 所选报告窗口中已点击细分的受众数量。 |
| ^^ordered | object | {"not_rate":"96.30%","not_value":26000000,"rate":"3.70%","value":1000000} | 所选报告窗口中已下单和未下单的受众细分，包含数量和与初始受众基准的比率。 |
| ^^^not_rate | string | 96.30% | ordered.not_value 所占初始受众的百分比，计算公式为 ordered.not_value / funnel.total.value * 100，以百分比字符串返回，例如 "55.12%"。不要将返回的百分比再乘以 100。当初始受众数量不为正数时不可用。 |
| ^^^not_value | int | 26000000 | 所选报告窗口中未下单细分的受众数量。 |
| ^^^rate | string | 3.70% | ordered.value 所占初始受众的百分比，计算公式为 ordered.value / funnel.total.value * 100，以百分比字符串返回，例如 "44.88%"。不要将返回的百分比再乘以 100。当初始受众数量不为正数时不可用。 |
| ^^^value | int | 1000000 | 所选报告窗口中已下单细分的受众数量。 |
| ^^total | object | {"value":27000000} | 在报告窗口开始时由 audience_type 选择的初始受众基准。此基准不按 account_type 或 form 过滤。 |
| ^^^value | int | 27000000 | 在报告窗口开始时所选初始受众中的受众数量。仅在获得正基准数量时可用。 |
| ^^viewed | object | {"not_rate":"50.00%","not_value":13500000,"rate":"50.00%","value":13500000} | 所选报告窗口中已观看和未观看的受众细分，包含数量和与初始受众基准的比率。 |
| ^^^not_rate | string | 50.00% | viewed.not_value 所占初始受众的百分比，计算公式为 viewed.not_value / funnel.total.value * 100，以百分比字符串返回，例如 "55.12%"。不要将返回的百分比再乘以 100。当初始受众数量不为正数时不可用。 |
| ^^^not_value | int | 13500000 | 所选报告窗口中未观看细分的受众数量。 |
| ^^^rate | string | 50.00% | viewed.value 所占初始受众的百分比，计算公式为 viewed.value / funnel.total.value * 100，以百分比字符串返回，例如 "44.88%"。不要将返回的百分比再乘以 100。当初始受众数量不为正数时不可用。 |
| ^^^value | int | 13500000 | 所选报告窗口中已观看细分的受众数量。 |
| ^latest_available_date | string | 2026-09-20 | 所选店铺、品牌和行业的最新可用报告日期，格式为 YYYY-MM-DD（UTC）。当请求日期被省略或为空时使用此日期；它可能晚于明确请求的日期。 |
# 响应示例
```json
{"code":0,"data":{"funnel":{"clicked":{"not_rate":"80.00%","not_value":21600000,"rate":"20.00%","value":5400000},"ordered":{"not_rate":"96.30%","not_value":26000000,"rate":"3.70%","value":1000000},"total":{"value":27000000},"viewed":{"not_rate":"50.00%","not_value":13500000,"rate":"50.00%","value":13500000}},"latest_available_date":"2026-09-20"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

