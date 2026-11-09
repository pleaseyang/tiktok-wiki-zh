# 编辑 Affiliate Partner 活动

# 路径：/affiliate_partner/202405/campaigns/{campaign_id}/partial_edit
# 方法：[POST]
# 功能描述
部分更新 Affiliate Partner 活动。请求中省略的字段将保留其当前值，包括 `contact_info` 中省略的字段。`target_seller_types` 和 `target_shop_codes` 互斥。要切换定向模式，请将之前使用的字段发送为空数组，并将新字段与其值一起发送。活动关闭后无法编辑。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop APIs - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过使用 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| campaign_id | string | Y | 7373988288167036678 | 十进制整数格式的活动 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过使用 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | N | test campaign | 活动名称。必须包含 1 到 50 个字符，且不能以空格开头。 |
| description | string | N | campaign for api test. | 活动描述。必须包含 1 到 1000 个字符，且不能以空格开头。 |
| campaign_start_time | int | N | 1712941200 | 计划的活动开始时间，Unix 时间戳（秒）。仅当活动状态为 `READY` 或 `UPCOMING` 时才能更新此字段。 |
| campaign_end_time | int | N | 1715878799 | 计划的活动结束时间，Unix 时间戳（秒）。请注意，结束时间必须距开始日期少于 360 天。当活动状态设置为 `CLOSED` 时，此字段不再可编辑。 |
| registration_start_time | int | N | 1712941200 | 计划的卖家商品注册开始时间，Unix 时间戳（秒）。仅当活动状态为 `READY` 或 `UPCOMING` 时才能更新此字段。 |
| registration_end_time | int | N | 1713891599 | 计划的卖家商品注册结束时间，Unix 时间戳（秒）。当活动状态为 `CLOSED` 时，此字段不再可编辑。 |
| commission_rate | int | N | 1000 | affiliate 合作伙伴提议的总佣金 rate，以 0.01% 为单位。值必须在 100 到 8000 之间（含）。 |
| contact_info | object | N |  | 合作伙伴的联系信息。 |
| ^whatsapp | string | N | +14255550100 | 合作伙伴在 WhatsApp 上注册的电话号码，E.164 国际格式。适用于目标市场为 MY、SG、GB、ID 或 US 的情况。 |
| ^email | string | N | 123456@gmail.com | 合作伙伴的电子邮件地址。 |
| ^phone | string | N | +14255550100 | 合作伙伴的电话号码，E.164 国际格式。 |
| ^zalo | string | N | +14255550100 | 合作伙伴在 Zalo 上注册的电话号码，E.164 国际格式。适用于目标市场为 VN 的情况。 |
| ^viber | string | N | +14255550100 | 合作伙伴在 Viber 上注册的电话号码，E.164 国际格式。适用于目标市场为 PH 的情况。 |
| ^line | string | N | +14255550100 | 合作伙伴在 LINE 上注册的电话号码，E.164 国际格式。适用于目标市场为 TH 的情况。 |
| target_shop_codes | []string | N | ["THCBELNL4Y"] | 允许注册活动的 TikTok Shop 卖家 shop code 列表。卖家 shop code 可在 TikTok Shop 卖家 Central 中通过点击界面右上角的卖家 Profile 图标获取。列表长度必须少于 100 个项目。 |
| target_seller_types | []string | N | ["CROSS_BORDER"] | 允许注册活动的符合条件的卖家类型列表。使用此字段来广泛定向卖家类型，而不是 `target_shop_codes` 字段中的特定卖家。此为枚举类型，可能的值： |

* LOCAL
* CROSS_BORDER |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202405/campaigns/7373988288167036678/partial_edit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"name":"test campaign","description":"campaign for api test.","campaign_start_time":1712941200,"campaign_end_time":1715878799,"registration_start_time":1712941200,"registration_end_time":1713891599,"commission_rate":1000,"contact_info":{"whatsapp":"+14255550100","email":"123456@gmail.com","phone":"+14255550100","zalo":"+14255550100","viber":"+14255550100","line":"+14255550100"},"target_shop_codes":["THCBELNL4Y"],"target_seller_types":["CROSS_BORDER"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop APIs - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 16032002 | Invalid campaign period |
| 16032003 | Invalid registration period |
| 16032004 | Invalid campaign seller scope |
| 16032005 | Campaign not found |
| 16032007 | Permission denied |
| 16032008 | Operation denied |
