# 获取 ACC 受众概览

# Path: /analytics/202610/acc/overview
# Method: [GET]
# 功能描述
获取 ACC 受众关键指标、基准值和趋势。

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
| brand_id | string | Y | 1000001 | 要分析的品牌 ID。使用同一店铺的 Get ACC Brands (GET /analytics/202610/acc/brands) 返回的记录中的 brand_id 和 industry_id。两个 ID 均不能为空。 |
| industry_id | string | Y | 9000001 | 用于选择数据可用性和行业基准值的行业 ID。使用与 `brand_id` 相同的 Get ACC Brands 记录中的 `industry_id`。此值必填，不能为空。 |
| date | string | N | 2026-09-20 | 关键指标的日期，格式为 `YYYY-MM-DD`（UTC）。如果省略，则使用请求的品牌和行业的最新可用日期。日期必须在可用数据范围内。 |
| benchmark | string | N | 5 | 选择行业基准值：行业 Top N 品牌的相应受众指标平均值。允许值：5、10、25 和 50。默认值：5。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/acc/overview?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&brand_id=1000001&industry_id=9000001&date=2026-09-20&benchmark=5
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^key_metrics | object | {"acc":{"benchmark":32000000,"dod_change_rate":"2.00%","value":27000000},"awareness":{"benchmark":26000000,"dod_change_rate":"2.00%","value":22000000},"consideration":{"benchmark":5000000,"dod_change_rate":"2.00%","value":4000000},"conversion":{"benchmark":1000000,"dod_change_rate":"2.00%","value":1000000},"new_conversion":{"benchmark":600000,"dod_change_rate":"2.00%","value":600000},"repeat_conversion":{"benchmark":400000,"dod_change_rate":"2.00%","value":400000}} | 所选日期的受众指标。数量和基准值仅在大于 1,000 时可用。当相应受众数量为 1,000 或更少时，日环比变化不可用。 |
| ^^acc | object | {"benchmark":32000000,"dod_change_rate":"2.00%","value":27000000} | 总 ACC 受众的受众数量、日环比变化和行业标准：认知、考虑和转化受众的去重并集。 |
| ^^^benchmark | int | 32000000 | 所选行业 Top N 品牌中此指标的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^dod_change_rate | string | 2.00% | 此受众数量相对于前一个 UTC 日历日的百分比变化，计算公式为（当前 - 前一）/ 前一 * 100，以百分比字符串返回，例如 "9.21%"。当比较数据不可用或前一数量为零时不可用。 |
| ^^^value | int | 27000000 | 此指标在所选日期的受众数量。 |
| ^^awareness | object | {"benchmark":26000000,"dod_change_rate":"2.00%","value":22000000} | 认知受众的受众数量、日环比变化和行业标准：暴露于或浏览了品牌内容或商品的人。 |
| ^^^benchmark | int | 26000000 | 所选行业 Top N 品牌中此指标的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^dod_change_rate | string | 2.00% | 此受众数量相对于前一个 UTC 日历日的百分比变化，计算公式为（当前 - 前一）/ 前一 * 100，以百分比字符串返回，例如 "9.21%"。当比较数据不可用或前一数量为零时不可用。 |
| ^^^value | int | 22000000 | 此指标在所选日期的受众数量。 |
| ^^consideration | object | {"benchmark":5000000,"dod_change_rate":"2.00%","value":4000000} | 考虑受众的受众数量、日环比变化和行业标准：通过点击、加入购物车或关注等行为表现出更深层兴趣的人。 |
| ^^^benchmark | int | 5000000 | 所选行业 Top N 品牌中此指标的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^dod_change_rate | string | 2.00% | 此受众数量相对于前一个 UTC 日历日的百分比变化，计算公式为（当前 - 前一）/ 前一 * 100，以百分比字符串返回，例如 "9.21%"。当比较数据不可用或前一数量为零时不可用。 |
| ^^^value | int | 4000000 | 此指标在所选日期的受众数量。 |
| ^^conversion | object | {"benchmark":1000000,"dod_change_rate":"2.00%","value":1000000} | 转化受众的受众数量、日环比变化和行业标准：在报告期间完成购买的人。 |
| ^^^benchmark | int | 1000000 | 所选行业 Top N 品牌中此指标的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^dod_change_rate | string | 2.00% | 此受众数量相对于前一个 UTC 日历日的百分比变化，计算公式为（当前 - 前一）/ 前一 * 100，以百分比字符串返回，例如 "9.21%"。当比较数据不可用或前一数量为零时不可用。 |
| ^^^value | int | 1000000 | 此指标在所选日期的受众数量。 |
| ^^new_conversion | object | {"benchmark":600000,"dod_change_rate":"2.00%","value":600000} | 新转化受众的受众数量、日环比变化和行业标准：在报告期间首次在店铺购买的人。 |
| ^^^benchmark | int | 600000 | 所选行业 Top N 品牌中此指标的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^dod_change_rate | string | 2.00% | 此受众数量相对于前一个 UTC 日历日的百分比变化，计算公式为（当前 - 前一）/ 前一 * 100，以百分比字符串返回，例如 "9.21%"。当比较数据不可用或前一数量为零时不可用。 |
| ^^^value | int | 600000 | 此指标在所选日期的受众数量。 |
| ^^repeat_conversion | object | {"benchmark":400000,"dod_change_rate":"2.00%","value":400000} | 复购转化受众的受众数量、日环比变化和行业标准：在报告期间的购买不是其首次在店铺购买的人。 |
| ^^^benchmark | int | 400000 | 所选行业 Top N 品牌中此指标的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^dod_change_rate | string | 2.00% | 此受众数量相对于前一个 UTC 日历日的百分比变化，计算公式为（当前 - 前一）/ 前一 * 100，以百分比字符串返回，例如 "9.21%"。当比较数据不可用或前一数量为零时不可用。 |
| ^^^value | int | 400000 | 此指标在所选日期的受众数量。 |
| ^latest_available_date | string | 2026-09-20 | 所请求品牌和行业的最新可用日期，格式为 `YYYY-MM-DD`（UTC）。这可能与请求的 `date` 不同。 |
| ^trend | []object | [{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":32000000,"date":"2026-09-20","value":27000000}],"metric":"ACC"},{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":26000000,"date":"2026-09-20","value":22000000}],"metric":"AWARENESS"},{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":5000000,"date":"2026-09-20","value":4000000}],"metric":"CONSIDERATION"},{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":1000000,"date":"2026-09-20","value":1000000}],"metric":"CONVERSION"},{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":600000,"date":"2026-09-20","value":600000}],"metric":"NEW_CONVERSION"},{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":400000,"date":"2026-09-20","value":400000}],"metric":"REPEAT_CONVERSION"}] | 六个受众指标的时间序列。每个序列包含最多 30 个可用每日数据点，按 UTC 日期升序排列。缺失日期不填充。 |
| ^^actual_end_date | string | 2026-09-20 | `intervals` 中包含的最新 UTC 日期，格式为 `YYYY-MM-DD`。当 `intervals` 为空时不可用。 |
| ^^actual_start_date | string | 2026-09-20 | `intervals` 中包含的最早 UTC 日期，格式为 `YYYY-MM-DD`。当 `intervals` 为空时不可用。 |
| ^^interval_count | int | 1 | `intervals` 中的数据点数（0 到 30）。 |
| ^^intervals | []object | [{"benchmark":32000000,"date":"2026-09-20","value":27000000}] | 此指标的每日数据点，按 UTC 日期升序排列。数量和基准值仅在大于 1,000 时可用。 |
| ^^^benchmark | int | 32000000 | 所选行业 Top N 品牌中此指标和日期的平均受众数量，其中 N 为基准值请求参数。单位：人。 |
| ^^^date | string | 2026-09-20 | 此数据点的 UTC 日期，格式为 `YYYY-MM-DD`。 |
| ^^^value | int | 27000000 | 此指标在数据点日期的受众数量。 |
| ^^metric | string | ACC | 此序列表示的受众指标。可能的值：`ACC`、`AWARENESS`、`CONSIDERATION`、`CONVERSION`、`NEW_CONVERSION` 和 `REPEAT_CONVERSION`。六个指标含义与 key_metrics 中的相应字段匹配。 |
# 响应示例
```json
{"code":0,"data":{"key_metrics":{"acc":{"benchmark":32000000,"dod_change_rate":"2.00%","value":27000000},"awareness":{"benchmark":26000000,"dod_change_rate":"2.00%","value":22000000},"consideration":{"benchmark":5000000,"dod_change_rate":"2.00%","value":4000000},"conversion":{"benchmark":1000000,"dod_change_rate":"2.00%","value":1000000},"new_conversion":{"benchmark":600000,"dod_change_rate":"2.00%","value":600000},"repeat_conversion":{"benchmark":400000,"dod_change_rate":"2.00%","value":400000}},"latest_available_date":"2026-09-20","trend":[{"actual_end_date":"2026-09-20","actual_start_date":"2026-09-20","interval_count":1,"intervals":[{"benchmark":32000000,"date":"2026-09-20","value":27000000}],"metric":"ACC"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

