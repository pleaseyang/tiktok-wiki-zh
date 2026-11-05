# 查询 Target Collaboration 中的 Creator 推广详情

# Path: /affiliate_seller/202608/target_collaborations/creator_promotion_details/query
# Method: [POST]
# 功能描述
此 API 用于查询 target collaboration 中 creator 的推广详情。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| creator_user_open_id | string | Y | abc | Creator open id |
| invitation_group_id | string | Y | 1234 | Invitation Group Id |
| query | string | N | abc | Product ID or product title to match, as selected by `query_type`. Provide both fields to filter the returned products. |
| query_type | string | N | PRODUCT_ID | 指定 `query` 如何筛选产品。可能的值： |

* `PRODUCT_ID`: Match the product ID exactly.
* `PRODUCT_NAME`: 按区分大小写的子字符串匹配产品标题。 |
   invitation_id |string |N |1234 |Creator Invitation Id |
   product_filter |object |N | |Product Fitler |
   ^added_types |[]string |N |["ALL"] |产品添加类型列表，支持的状态：
   -ALL: all status
   -ADDED: creator added product
   NOT_ADDED：creator 未添加产品
   |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202608/target_collaborations/creator_promotion_details/query?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"creator_user_open_id":"abc","invitation_group_id":"1234","query":"abc","query_type":"PRODUCT_ID","invitation_id":"1234","product_filter":{"added_types":["ALL"]}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | Promotion details for products in the target collaboration invitation group. |
| ^^product_details | []object |  | Product detail infomation |
| ^^^product_base_info | object |  | Product basic infomation |
| ^^^^product_id | string | 1234 | Product ID |
| ^^^^title | string | product title | Product titile |
| ^^^^image | object |  | Product Image |
| ^^^^^url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476 | Product Image URL |
| ^^^^price | object |  | Product Price |
| ^^^^^min_price | object |  | Product min price |
| ^^^^^^amount | string | 1 | Price amout |
| ^^^^^^currency | string | GBP | Price currency |
| ^^^^^max_price | object |  | Product max price |
| ^^^^^^amount | string | 1 | Product amount |
| ^^^^^^currency | string | GBP | Product currency |
| ^^^^promotion_price | object |  | Product promotion price |
| ^^^^^min_price | object |  | Product promotion min price |
| ^^^^^^amount | string | 1 | Price amount |
| ^^^^^^currency | string | GBP | Price currency |
| ^^^^^max_price | object |  | Product promotion max price |
| ^^^^^^amount | string | 1 | Price amount |
| ^^^^^^currency | string | GBP | Price currency |
| ^^^^target_commission | int | 2200 | Product target collaboration commission. e.g. 2200 mean 22% commission rate |
| ^^^^open_commission | int | 2200 | Product open collaboration commission. e.g. 2200 mean 22% commission rate |
| ^^^^target_ads_commission | int | 2200 | Product target ads collaboration commission |
| ^^^^old_target_commission | int | 2200 | Product old target collaboration commission |
| ^^^^old_target_ads_commission | int | 2200 | Product old target ads collaboration commission |
| ^^^^commission_effective_time | int | 1786592565735 | Unix timestamp in milliseconds when the target collaboration commission becomes effective. |
| ^^^^ads_commission_effective_time | int | 1786592565735 | Unix timestamp in milliseconds when the target collaboration Ads commission becomes effective. |
| ^^^^product_status | string | 1 | Product status |
| 1: Active |  |  |  |
| 2; Sold out |  |  |  |
| 3: product deactivated by seller; |  |  |  |
| 4: product deactivated by platform |  |  |  |
| 5: product reject |  |  |  |
| 6: product deleted |  |  |  |
| ^^^product_add_status | bool | false | Product added or not |
| ^^^video_count | int | 1 | Creator post video count in collaboration |
| ^^^live_count | int | 1 | Creator LIVE count in collaboration |
| ^^^is_commission_effective | bool | false | Whether the target collaboration commission for this creator-product pair is currently effective. `false` means an active campaign collaboration takes precedence. |
# 响应示例
```json
{"code":0,"data":{"data":{"product_details":[{"product_base_info":{"product_id":"1234","title":"product title","image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476"},"price":{"min_price":{"amount":"1","currency":"GBP"},"max_price":{"amount":"1","currency":"GBP"}},"promotion_price":{"min_price":{"amount":"1","currency":"GBP"},"max_price":{"amount":"1","currency":"GBP"}},"target_commission":2200,"open_commission":2200,"target_ads_commission":2200,"old_target_commission":2200,"old_target_ads_commission":2200,"commission_effective_time":1786592565735,"ads_commission_effective_time":1786592565735,"product_status":"1"},"product_add_status":false,"video_count":1,"live_count":1,"is_commission_effective":false}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

