# 查询 Target Collaboration 中的达人推广详情

# 路径：/affiliate_seller/202608/target_collaborations/creator_promotion_details/query
# 方法：[POST]
# 功能描述
此 API 用于查询 target collaboration 中达人的推广详情。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| creator_user_open_id | string | Y | abc | 达人 open id |
| invitation_group_id | string | Y | 1234 | 邀请组 Id |
| query | string | N | abc | 用于匹配的商品 ID 或商品标题，由 `query_type` 选定. 同时提供这两个字段以筛选返回的商品。 |
| query_type | string | N | PRODUCT_ID | 指定 `query` 如何筛选商品。可能的值： |

* `PRODUCT_ID`: 精确匹配商品 ID。
* `PRODUCT_NAME`: 按区分大小写的子字符串匹配商品标题。 |
   invitation_id |string |N |1234 |达人邀请 ID |
   product_filter |object |N | |商品筛选 |
   ^added_types |[]string |N |["ALL"] |商品添加类型列表，支持的状态：
   -ALL: 所有状态
   -ADDED: 达人已添加商品
   NOT_ADDED：达人未添加商品
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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | 定向协作邀请组中商品的推广详情。 |
| ^^product_details | []object |  | 商品详细信息 |
| ^^^product_base_info | object |  | 商品基本信息 |
| ^^^^product_id | string | 1234 | Product ID |
| ^^^^title | string | product title | Product titile |
| ^^^^image | object |  | Product Image |
| ^^^^^url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476 | 商品图片 URL |
| ^^^^price | object |  | Product Price |
| ^^^^^min_price | object |  | 商品最低价格 |
| ^^^^^^amount | string | 1 | Price amout |
| ^^^^^^currency | string | GBP | Price currency |
| ^^^^^max_price | object |  | 商品最高价格 |
| ^^^^^^amount | string | 1 | Product amount |
| ^^^^^^currency | string | GBP | Product currency |
| ^^^^promotion_price | object |  | 商品推广价格 |
| ^^^^^min_price | object |  | 商品推广最低价格 |
| ^^^^^^amount | string | 1 | Price amount |
| ^^^^^^currency | string | GBP | Price currency |
| ^^^^^max_price | object |  | 商品推广最高价格 |
| ^^^^^^amount | string | 1 | Price amount |
| ^^^^^^currency | string | GBP | Price currency |
| ^^^^target_commission | int | 2200 | 商品定向协作佣金. e.g. 2200 表示 22% 佣金率 |
| ^^^^open_commission | int | 2200 | 商品开放协作佣金. 例如 2200 表示 22% 佣金率 |
| ^^^^target_ads_commission | int | 2200 | 商品定向广告协作佣金 |
| ^^^^old_target_commission | int | 2200 | 商品原定向协作佣金 |
| ^^^^old_target_ads_commission | int | 2200 | 商品原定向广告协作佣金 |
| ^^^^commission_effective_time | int | 1786592565735 | 定向协作佣金生效时间的 Unix 毫秒时间戳。 |
| ^^^^ads_commission_effective_time | int | 1786592565735 | 定向协作广告佣金生效时间的 Unix 毫秒时间戳。 |
| ^^^^product_status | string | 1 | Product status |
| 1: Active |  |  |  |
| 2; Sold out |  |  |  |
| 3: 商品被卖家停用; |  |  |  |
| 4: 商品被平台停用 |  |  |  |
| 5: product reject |  |  |  |
| 6: product deleted |  |  |  |
| ^^^product_add_status | bool | false | 商品是否已添加 |
| ^^^video_count | int | 1 | 协作中达人发布的视频数 |
| ^^^live_count | int | 1 | 协作中达人的直播数量 |
| ^^^is_commission_effective | bool | false | 该达人-商品组合的定向协作佣金当前是否生效。`false` 表示生效中的活动协作优先。 |
# 响应示例
```json
{"code":0,"data":{"data":{"product_details":[{"product_base_info":{"product_id":"1234","title":"product title","image":{"url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476"},"price":{"min_price":{"amount":"1","currency":"GBP"},"max_price":{"amount":"1","currency":"GBP"}},"promotion_price":{"min_price":{"amount":"1","currency":"GBP"},"max_price":{"amount":"1","currency":"GBP"}},"target_commission":2200,"open_commission":2200,"target_ads_commission":2200,"old_target_commission":2200,"old_target_ads_commission":2200,"commission_effective_time":1786592565735,"ads_commission_effective_time":1786592565735,"product_status":"1"},"product_add_status":false,"video_count":1,"live_count":1,"is_commission_effective":false}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

