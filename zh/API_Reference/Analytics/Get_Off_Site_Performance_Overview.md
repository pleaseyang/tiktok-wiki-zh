# 获取站外表现概览

# 路径：/analytics/202610/off_site/overview
# 方法：[GET]
# 功能描述
获取每周站外 performance 指标和趋势。

---


# 公共参数
公共参数，请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
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
https://open-api.tiktokglobalshop.com/analytics/202610/off_site/overview?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&date=2026-09-09&pixel_id=12323123123&attribution_setting=VIEW_14D
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^end_date | string | 2026-09-12 | 所选报告周的最后日期（包含），格式为 YYYY-MM-DD。这是一个周六。 |
| ^key_metrics | object |  | 所选报告周的 performance 指标。效果比率为小数比率，其中 1.0000 表示 100%，可以超过 1。不可用的比率可能为 null，不得解释为零；响应不说明不可用的原因。 |
| ^^live_off_site_effect_rate | object |  | 所选报告周中 LIVE 内容的站外效果比率，包含整体、关联账户和联盟账户的明细。 |
| ^^^affiliate_account_rate | string | 0.1500 | 所选报告周中联盟账户 LIVE 内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^^^linked_account_rate | string | 0.3000 | 所选报告周中关联账户 LIVE 内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^^^overall_rate | string | 0.2000 | 所选报告周中 LIVE 内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^^off_site_effect_rate | string | 0.3000 | 所选报告周的站外 GMV 除以 TikTok Shop GMV。 |
| ^^off_site_gmv | object |  | 报告周内在所选归因设置下归因于 TikTok Shop 商业内容的站外商品总额 (GMV)。 |
| ^^^amount | string | 3000.00 | GMV 金额，以小数字符串表示。请查看 currency 获取关联的货币代码。 |
| ^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^product_card_off_site_effect_rate | string | 1.5000 | 所选报告周中商品卡片内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^^tiktok_shop_gmv | object |  | 所选报告周的 TikTok Shop 商品总额 (GMV)。 |
| ^^^amount | string | 10000.00 | GMV 金额，以小数字符串表示。请查看 currency 获取关联的货币代码。 |
| ^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^video_off_site_effect_rate | object |  | 所选报告周中 video 内容的站外效果比率，包含整体、关联账户和联盟账户的明细。 |
| ^^^affiliate_account_rate | string | 0.1500 | 所选报告周中联盟账户 video 内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^^^linked_account_rate | string | 0.3000 | 所选报告周中关联账户 video 内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^^^overall_rate | string | 0.2000 | 所选报告周中 video 内容的站外 GMV 除以 TikTok Shop GMV。 |
| ^latest_available_date | string | 2026-09-12 | 店铺报告时区内的最新可用报告日期，格式为 YYYY-MM-DD。省略 date 时选择包含该日期的周。与之前的 11 个报告周一起定义支持的查询窗口；可用日期不保证每个 Pixel 和归因设置都有数据。 |
| ^start_date | string | 2026-09-06 | 所选报告周的首个日期（包含），格式为 YYYY-MM-DD。这是一个周日。 |
| ^trend | object |  | 以所选报告周结尾的最多八个报告周的每周 performance 趋势。此历史窗口不受用于选择日期的 12 周限制截断。响应日期标识实际返回的历史；某些周的指标可能不可用。 |
| ^^actual_end_date | string | 2026-09-13 | 最后一个返回趋势区间的结束日期（不包含），格式为 YYYY-MM-DD。 |
| ^^actual_start_date | string | 2026-09-06 | 第一个返回趋势区间的开始日期（包含），格式为 YYYY-MM-DD。 |
| ^^granularity | string | 1W | 每个趋势区间的时间粒度。值为 1W，表示一个报告周。 |
| ^^interval_count | int | 1 | intervals 中返回的每周区间数，最多八个。 |
| ^^intervals | []object |  | 按 start_date 从最早到最晚排序的每周区间。最多返回八个区间。 |
| ^^^end_date | string | 2026-09-13 | 此每周区间的结束日期（不包含），格式为 YYYY-MM-DD。 |
| ^^^metrics | object |  | 此每周区间的 performance 指标。比率遵循与 key_metrics 相同的计算方式、小数格式和不可用数据行为。 |
| ^^^^live_off_site_effect_rate | string | 0.2000 | 此每周区间中 LIVE 内容的站外 GMV 除以 TikTok Shop GMV，以小数比率表示。 |
| ^^^^off_site_effect_rate | string | 0.3000 | 此每周区间中所有内容的站外 GMV 除以 TikTok Shop GMV，以小数比率表示。 |
| ^^^^off_site_gmv | object |  | 此每周区间的站外商品总额 (GMV)。 |
| ^^^^^amount | string | 3000.00 | GMV 金额，以小数字符串表示。请查看 currency 获取关联的货币代码。 |
| ^^^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^^^product_card_off_site_effect_rate | string | 1.5000 | 此每周区间中商品卡片内容的站外 GMV 除以 TikTok Shop GMV，以小数比率表示。 |
| ^^^^tiktok_shop_gmv | object |  | 此每周区间的 TikTok Shop 商品总额 (GMV)。 |
| ^^^^^amount | string | 10000.00 | GMV 金额，以小数字符串表示。请查看 currency 获取关联的货币代码。 |
| ^^^^^currency | string | USD | GMV 金额的 ISO 4217 三字母货币代码，取自授权店铺上下文。 |
| ^^^^video_off_site_effect_rate | string | 0.2000 | 此每周区间中 video 内容的站外 GMV 除以 TikTok Shop GMV，以小数比率表示。 |
| ^^^start_date | string | 2026-09-06 | 此每周区间的首个日期（包含），格式为 YYYY-MM-DD。 |
# 响应示例
```json
{"code":0,"data":{"end_date":"2026-09-12","key_metrics":{"live_off_site_effect_rate":{"affiliate_account_rate":"0.1500","linked_account_rate":"0.3000","overall_rate":"0.2000"},"off_site_effect_rate":"0.3000","off_site_gmv":{"amount":"3000.00","currency":"USD"},"product_card_off_site_effect_rate":"1.5000","tiktok_shop_gmv":{"amount":"10000.00","currency":"USD"},"video_off_site_effect_rate":{"affiliate_account_rate":"0.1500","linked_account_rate":"0.3000","overall_rate":"0.2000"}},"latest_available_date":"2026-09-12","start_date":"2026-09-06","trend":{"actual_end_date":"2026-09-13","actual_start_date":"2026-09-06","granularity":"1W","interval_count":1,"intervals":[{"end_date":"2026-09-13","metrics":{"live_off_site_effect_rate":"0.2000","off_site_effect_rate":"0.3000","off_site_gmv":{"amount":"3000.00","currency":"USD"},"product_card_off_site_effect_rate":"1.5000","tiktok_shop_gmv":{"amount":"10000.00","currency":"USD"},"video_off_site_effect_rate":"0.2000"},"start_date":"2026-09-06"}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码，请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

