# 创建 Affiliate Partner 活动

# 路径：/affiliate_partner/202405/campaigns
# 方法：[POST]
# 功能描述
为通过 shop code 识别的特定卖家或符合条件的卖家类型创建 affiliate 合作伙伴活动。配置活动时间段、卖家注册时间段、佣金率和联系信息。活动创建成功后，操作会同步返回新的 `campaign_id`。创建后活动不会立即展示给卖家。要发布已创建成功的活动，请调用 `POST /affiliate_partner/202405/campaigns/{campaign_id}/publish` 并传入返回的活动 ID。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | Y | my first campaign | 活动名称。必须包含 1 到 50 个字符（含），且不能以空格开头。 |
| description | string | Y | campaign for test | 活动描述。必须包含 1 到 1000 个字符（含），且不能以空格开头。 |
| campaign_start_time | int | Y | 1712941200 | 计划的活动开始时间，为 Unix 时间戳（秒）。不得早于当前时间。在后续编辑中，仅当活动状态为 `READY` 或 `UPCOMING` 时才能更改此值。 |
| campaign_end_time | int | Y | 1715878799 | 计划的活动结束时间，为 Unix 时间戳（秒）。必须晚于 `campaign_start_time`，活动周期必须在 1 到 360 天之间（含）。在后续编辑中，当活动状态为 `CLOSED` 时不能更改此值。 |
| registration_start_time | int | Y | 1712941200 | 计划的卖家商品注册开始时间，为 Unix 时间戳（秒）。必须等于 `campaign_start_time`。在后续编辑中，仅当活动状态为 `READY` 或 `UPCOMING` 时才能更改此值。 |
| registration_end_time | int | Y | 1713891599 | 计划的卖家商品注册结束时间，为 Unix 时间戳（秒）。必须晚于 `registration_start_time`；注册周期必须至少为 1 天，且不得超出 `campaign_end_time`。在后续编辑中，当活动状态为 `CLOSED` 时不能更改此值。 |
| commission_rate | int | Y | 1000 | affiliate 合作伙伴提出的总佣金率，以百分之一的百分比（0.01%）为单位，用于向卖家展示。值必须在 100 到 8000 之间（含）。 |
| contact_info | object | Y |  | 合作伙伴的联系信息。 |
| ^whatsapp | string | N | +14255550100 | 合作伙伴在 WhatsApp 上注册的电话号码，采用 E.164 国际格式。如果目标市场是 MY、SG、GB 或 ID 则为必填；如果目标市场是 US 则为选填；其他情况不适用。 |
| ^email | string | Y | 123456@gmail.com | 合作伙伴的电子邮件地址。 |
| ^phone | string | N | +14255550100 | 合作伙伴的电话号码，采用 E.164 国际格式。 |
| ^zalo | string | N | +14255550100 | 合作伙伴在 Zalo 上注册的电话号码，采用 E.164 国际格式。如果目标市场是 VN 则为必填；其他情况不适用。 |
| ^viber | string | N | +14255550100 | 合作伙伴在 Viber 上注册的电话号码，采用 E.164 国际格式。如果目标市场是 PH 则为必填；其他情况不适用。 |
| ^line | string | N | +14255550100 | 合作伙伴在 LINE 上注册的电话号码，采用 E.164 国际格式。如果目标市场是 TH 则为必填；其他情况不适用。 |
| target_shop_codes | []string | N | ["THCBELNL4Y"] | 可以注册活动的 TikTok Shop 卖家 shop code 列表。在 TikTok Shop 卖家 Central 中，通过点击右上角的卖家 Profile 图标找到卖家的 shop code。在 `target_shop_codes` 和 `target_seller_types` 中恰好指定一个。列表必须包含少于 100 个项目。 |
| target_seller_types | []string | N | ["CROSS_BORDER"] | 可以注册活动的符合条件的卖家类型列表。使用此字段来针对卖家类型，而不是 `target_shop_codes` 中的特定卖家。在 `target_seller_types` 和 `target_shop_codes` 中恰好指定一个。 |
| 可能的值: |  |  |  | |

* `LOCAL`
* `CROSS_BORDER` |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202405/campaigns?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"name":"my first campaign","description":"campaign for test","campaign_start_time":1712941200,"campaign_end_time":1715878799,"registration_start_time":1712941200,"registration_end_time":1713891599,"commission_rate":1000,"contact_info":{"whatsapp":"+14255550100","email":"123456@gmail.com","phone":"+14255550100","zalo":"+14255550100","viber":"+14255550100","line":"+14255550100"},"target_shop_codes":["THCBELNL4Y"],"target_seller_types":["CROSS_BORDER"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^campaign_id | string | 7356411663443183367 | 活动标识符。 |
# 响应示例
```json
{"code":0,"data":{"campaign_id":"7356411663443183367"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 16032002 | Invalid campaign period |
| 16032003 | Invalid registration period |
| 16032004 | Invalid campaign seller scope |
| 16032013 | Payment account not yet activated |

