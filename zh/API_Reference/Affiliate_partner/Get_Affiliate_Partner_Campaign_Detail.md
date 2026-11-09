# 获取 Affiliate Partner 活动详情

# 路径：/affiliate_partner/202405/campaigns/{campaign_id}
# 方法：[GET]
# 功能描述
此 API 提供获取 affiliate 活动详情的功能。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| campaign_id | string | Y | 7373988288167036678 | 十进制整数格式的活动 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202405/campaigns/7373988288167036678?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^id | string | 7356876895365105455 | 活动标识符。 |
| ^name | string | test_campaign | 活动名称。最大长度：50 个字符。 |
| ^description | string | Campaign for api test. | 活动描述。最大长度：1000 个字符。 |
| ^status | string | READY | 活动状态。此状态为枚举类型，取值如下： |

* READY
* UPCOMING
* ONGOING
* CLOSED |
   ^region |string |US |活动关联的区域。 |
   ^registration_start_time |int |1712941200 |计划的卖家商品注册开始时间，为 Unix 时间戳（秒）。此字段仅在活动状态为 `READY` 或 `UPCOMING` 时可以更新。 |
   ^registration_end_time |int |1713891599 |计划的卖家商品注册结束时间，为 Unix 时间戳（秒）。当活动状态为 `CLOSED` 时，此字段不再可编辑。 |
   ^campaign_start_time |int |1712941200 |计划的活动开始时间，为 Unix 时间戳（秒）。此字段仅在活动状态为 `READY` 或 `UPCOMING` 时可以更新。 |
   ^campaign_end_time |int |1715878799 |计划的活动结束时间，为 Unix 时间戳格式。请注意，结束时间必须距开始日期少于 360 天。当活动状态设置为 `CLOSED` 时，此字段不再可编辑。 |
   ^commission_rate |int |1000 |affiliate 合作伙伴提出的总佣金率，以百分之一的百分比（0.01%）为单位，用于向卖家展示。佣金率必须大于 100 且小于 8000。 |
   ^contact_info |object | |活动达人的联系信息。 |
   ^^whatsapp |string |+14255550100 |WhatsApp 账号 |
   ^^email |string |123456@gmail.com |电子邮件 |
   ^^phone |string |+14255550100 |电话号码 |
   ^^zalo |string |+14255550100 |Zalo 账号 |
   ^^viber |string |+14255550100 |Viber 账号 |
   ^^line |string |+14255550100 |Line 账号 |
   ^target_shops |[]object | |有权注册活动的 TikTok Shop 卖家 shop code 和名称列表。 |
   ^^code |string |THCBELNL4Y |卖家 shop code，可在 TikTok Shop 卖家 Central 中点击右上角的卖家 Profile 图标查看。 |
   ^^name |string |my_shop |TikTok Shop 名称。 |
   ^target_seller_types |[]string |["LOCAL"] |有资格注册活动的卖家类型列表。使用此字段可以广泛针对卖家类型，而不是 `target_shops` 中列出的特定 shop。可能的值：
* LOCAL
* CROSS_BORDER |

# 响应示例
```json
{"code":0,"data":{"id":"7356876895365105455","name":"test_campaign","description":"Campaign for api test.","status":"READY","region":"US","registration_start_time":1712941200,"registration_end_time":1713891599,"campaign_start_time":1712941200,"campaign_end_time":1715878799,"commission_rate":1000,"contact_info":{"whatsapp":"+14255550100","email":"123456@gmail.com","phone":"+14255550100","zalo":"+14255550100","viber":"+14255550100","line":"+14255550100"},"target_shops":[{"code":"THCBELNL4Y","name":"my_shop"}],"target_seller_types":["LOCAL"]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 16032005 | Campaign not found |
| 16032007 | Permission denied |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

