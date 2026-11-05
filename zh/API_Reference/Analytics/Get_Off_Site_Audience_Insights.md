# 获取站外受众洞察

# Path: /analytics/202610/off_site/insights
# Method: [GET]
# 功能描述
比较每周站内和站外归因客户受众分布。
列表使用 TikTok Shop 客户分布中的标签。标签过滤和 Top 10 限制意味着返回的百分比之和可能不等于 100%。
如果请求的 Pixel 和归因设置的报告不可用，结果可能使用 VIEW_14D 归因的店铺级报告。空分布可能表示报告数据不可用，并不一定意味着店铺没有客户。

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
| date | string | N | 2026-09-09 | 请求报告周内的某一天，格式为 YYYY-MM-DD。报告周从周日到周六（店铺报告时区）。如果省略，则选择最新可用的报告周。支持的周为最新可用周及之前 11 周，报告周不早于 2026-06-14。 |
| pixel_id | string | Y | 12323123123 | 授权店铺的 Pixel ID。使用同一店铺的 GET /analytics/202610/off_site/pixels 返回的 pixel_id。不属于该店铺的 ID 可能会回退到店铺级报告，而不是返回 Pixel 特定数据。 |
| attribution_setting | string | Y | VIEW_14D | 站外购买的归因设置。允许值：VIEW_14D（客户在购买前 14 天内浏览了 TikTok Shop 商业内容）和 CLICK_14D_OR_VIEW_1D（客户在购买前 14 天内点击或 1 天内浏览）。同时满足两个条件的购买只计算一次。如果请求的报告不可用，店铺级回退报告可能使用 VIEW_14D。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202610/off_site/insights?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&date=2026-09-09&pixel_id=12323123123&attribution_setting=VIEW_14D
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^age | []object | [{"name":"25-34","off_site_customers_value":"38.21%","tts_customers_value":"35.80%"}] | 年龄组分布，按 TikTok Shop 客户数降序排列。排除空标签和 `Unknown`。 |
| ^^name | string | 25-34 | 报告返回的年龄组名称；标签为源值，不保证遵循固定的显示字典。 |
| ^^off_site_customers_value | string | 38.21% | 报告中此年龄组的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 35.80% | 报告中此年龄组的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^consumption_level | []object | [{"name":"High","off_site_customers_value":"31.50%","tts_customers_value":"28.90%"}] | 消费层级分布，按 TikTok Shop 客户数降序排列。排除空标签和 `Unknown`。 |
| ^^name | string | High | 报告返回的消费层级名称；标签为源值，不保证遵循固定的显示字典。 |
| ^^off_site_customers_value | string | 31.50% | 报告中此消费层级的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 28.90% | 报告中此消费层级的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^followed_shop | []object | [{"name":"Following","off_site_customers_value":"42.00%","tts_customers_value":"39.60%"}] | 按店铺关注状态分布，按 TikTok Shop 客户数降序排列。排除空标签和 `Unknown`。 |
| ^^name | string | Following | 报告返回的店铺关注状态标签；标签为源值，不保证遵循固定的显示字典。 |
| ^^off_site_customers_value | string | 42.00% | 报告中此店铺关注状态的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 39.60% | 报告中此店铺关注状态的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^gender | []object | [{"name":"Female","off_site_customers_value":"63.20%","tts_customers_value":"61.10%"}] | 性别分布，按 TikTok Shop 客户数降序排列。排除空标签和 `Unknown`。 |
| ^^name | string | Female | 报告返回的性别标签；标签为源值，不保证遵循固定的显示字典。 |
| ^^off_site_customers_value | string | 63.20% | 报告中此性别类别的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 61.10% | 报告中此性别类别的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^personas | []object | [{"name":"Quality-focused","off_site_customers_value":"24.80%","tts_customers_value":"21.40%"}] | 受众画像分布，按 TikTok Shop 客户数降序排列。排除空标签、`Unknown` 和 `OTHERS`（不区分大小写）。返回的画像标签数量不固定为八个。 |
| ^^name | string | Quality-focused | 报告返回的受众画像标签。画像分布不保证恰好包含八个标签。 |
| ^^off_site_customers_value | string | 24.80% | 报告中此受众画像的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 21.40% | 报告中此受众画像的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^region | []object | [{"name":"Los Angeles","off_site_customers_value":"12.40%","tts_customers_value":"11.80%"}] | 城市分布，按 TikTok Shop 客户数降序排列。最多返回 10 条：在移除空标签和 `Unknown` 之前选择 Top 10 标签。 |
| ^^name | string | Los Angeles | 报告返回的城市标签。标签为源值，不保证遵循固定的显示字典。 |
| ^^off_site_customers_value | string | 12.40% | 报告中此城市的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 11.80% | 报告中此城市的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^top_favorite_content | []object | [{"name":"Beauty \u0026 Personal Care","off_site_customers_value":"29.70%","tts_customers_value":"27.30%"}] | 内容兴趣分布，按 TikTok Shop 客户数降序排列。最多返回 10 条：在移除空标签和 `Unknown` 之前选择 Top 10 标签。 |
| ^^name | string | Beauty & Personal Care | 报告返回的内容兴趣标签；不保证是规范的内容类目显示名称。 |
| ^^off_site_customers_value | string | 29.70% | 报告中此内容兴趣标签的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 27.30% | 报告中此内容兴趣标签的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^top_purchase_category_preferences | []object | [{"name":"Skin Care","off_site_customers_value":"22.60%","tts_customers_value":"20.10%"}] | 2级购买类目分布，按 TikTok Shop 客户数降序排列。最多返回 10 条；类目在标签过滤之前选择，因此返回条目可能少于 10 条。 |
| ^^name | string | Skin Care | 报告经过源标签处理后返回的2级购买类目标签；不保证使用固定的显示字典。 |
| ^^off_site_customers_value | string | 22.60% | 报告中此2级购买类目偏好的站外归因购买者百分比，按报告的总站外客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
| ^^tts_customers_value | string | 20.10% | 报告中此2级购买类目偏好的 TikTok Shop 购买者百分比，按报告的总 TikTok Shop 客户数计算。以带 % 后缀的百分比字符串返回，如 32.15%；不要再乘以 100。不可用的值可能为 null，不得替换为 0%。 |
# 响应示例
```json
{"code":0,"data":{"age":[{"name":"25-34","off_site_customers_value":"38.21%","tts_customers_value":"35.80%"}],"consumption_level":[{"name":"High","off_site_customers_value":"31.50%","tts_customers_value":"28.90%"}],"followed_shop":[{"name":"Following","off_site_customers_value":"42.00%","tts_customers_value":"39.60%"}],"gender":[{"name":"Female","off_site_customers_value":"63.20%","tts_customers_value":"61.10%"}],"personas":[{"name":"Quality-focused","off_site_customers_value":"24.80%","tts_customers_value":"21.40%"}],"region":[{"name":"Los Angeles","off_site_customers_value":"12.40%","tts_customers_value":"11.80%"}],"top_favorite_content":[{"name":"Beauty \u0026 Personal Care","off_site_customers_value":"29.70%","tts_customers_value":"27.30%"}],"top_purchase_category_preferences":[{"name":"Skin Care","off_site_customers_value":"22.60%","tts_customers_value":"20.10%"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

