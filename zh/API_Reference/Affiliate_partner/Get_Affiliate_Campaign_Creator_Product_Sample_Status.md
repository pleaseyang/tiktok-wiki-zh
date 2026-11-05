# 获取 Affiliate Campaign Creator 产品样品状态

# Path: /affiliate_partner/202508/campaigns/{campaign_id}/products/{product_id}/creator/{creator_temp_id}/content/statistics/sample/status
# Method: [GET]
# 功能描述
获取 affiliate campaign 中 creator 产品样品的配送和跟踪详情。在调用此 API 之前，creator 必须已申请过该产品的样品。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Path Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| campaign_id | string | Y | 123 | campaign 标识符。 |
| product_id | string | Y | 123 | product 标识符。 |
| creator_temp_id | string | Y | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202508/campaigns/123/products/123/creator/uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg/content/statistics/sample/status?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sample_status | object |  | Creator 的样品状态 |
| ^^shipping_provider_name | string | USPS | 物流服务商名称 |
| ^^delivery_option | string | PREMIUM_SHIPPING | 配送选项： |

* ECONOMY_SHIPPING
* PREMIUM_SHIPPING
   |
   ^^estimated_earliest_delivery_date |string |1712941200 |预计最早的配送日期，为 Unix 时间戳格式。 |
   ^^estimated_latest_delivery_date |string |1712941200 |预计最晚的配送日期，为 Unix 时间戳格式。 |
   ^^quantity |int |1 |配送的产品数量。 |
   ^^tracking_results |[]object | |表示物流跟踪事件的对象列表。 |
   ^^^tracking_event_update_date |string |1712941200 |物流跟踪事件最后更新的日期，为 Unix 时间戳格式。 |
   ^^^tracking_event_description |string |THE_PACKAGE_HAS_BEEN_DELIVERED |物流跟踪事件的标题。
* THE_PACKAGE_HAS_BEEN_DELIVERED
* OUT_FOR_DELIVERY
* ORDER_PACKED_AND_READY_FOR_DROP_OFF_AT_CARRIERS_FACILITY
* ORDER_PLACED |
   ^^^tracking_event_description_extended |string |delivering | 关于物流跟踪事件的更多信息 |

# Response Sample
```json
{"code":0,"data":{"sample_status":{"shipping_provider_name":"USPS","delivery_option":"PREMIUM_SHIPPING","estimated_earliest_delivery_date":"1712941200","estimated_latest_delivery_date":"1712941200","quantity":1,"tracking_results":[{"tracking_event_update_date":"1712941200","tracking_event_description":"THE_PACKAGE_HAS_BEEN_DELIVERED","tracking_event_description_extended":"delivering"}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

