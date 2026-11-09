# 搜索 Open Collaboration

# 路径：/affiliate_seller/202412/open_collaborations/search
# 方法：[POST]
# 功能描述
搜索卖家的 open collaboration。响应包括商品详情、当前佣金信息、将每个商品添加到橱窗的达人数量，以及发布 LIVE 或视频内容的达人数量。

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
| page_token | string | N | b2Zmc2V0PTAK | 分页 token，用于确定搜索的起始位置。首次请求时请将此参数留空。后续请求时，传入上一次响应返回的 `next_page_token`，并复用相同的请求体筛选条件、`sort_field`、`sort_order` 和 `page_size`。 |
| page_size | int | Y | 50 | "page_size" 的值必须大于 0 且小于或等于 100。 |
| sort_order | string | N | DESC | "sort_order" 的默认值为 DESC。 |
| Enum: |  |  |  |  |

* ASC：表示按升序排序数据
* DESC：表示按降序排序数据 |
   sort_field |string |N |product_original_price |部分可排序字段如下：
* product_original_price: 按商品原始价格排序。
   默认情况下，open collaboration 按创建时间降序排列。 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| keyword_type | string | N | PRODUCT_ID | 指定 `keyword` 中的值类型。要按商品名称或商品 ID 筛选 open collaboration，请同时提供 `keyword_type` 和 `keyword`。 |
| 可能的值： |  |  |  |  |

* `PRODUCT_ID`: 搜索指定商品 ID 的 open collaboration 信息。
* `PRODUCT_NAME`: 按相关商品名称模糊搜索 open collaboration 信息。 |
   keyword |string |N |7625459350921 |基于商品名称或商品 ID 进行搜索。根据上述 keyword_type 传入相应的值。 |
   top_level_category_id |string |N |60001 |按一级分类 ID 筛选商品。
   `top_level_category_id` 的值必须大于 0。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202412/open_collaborations/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=b2Zmc2V0PTAK&page_size=50&sort_order=DESC&sort_field=product_original_price
```

**Body**
```json
{"keyword_type":"PRODUCT_ID","keyword":"7625459350921","top_level_category_id":"60001"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTEw | 下一页的分页 token。 将此值作为 `page_token` 传入下一次请求。空值表示没有更多结果。 |
| ^total_count | int | 10000 | 符合所有输入搜索条件的商品总数。 |
| ^open_collaborations | []object |  | 当前页面中符合搜索条件的 open collaboration。 |
| ^^id | string | 94297006405 | 开放协作 ID |
| ^^status | string | NORMAL | Open collaboration 的状态。 |
| 字段值： |  |  |  |

* NORMAL：NORMAL 表示当前 open collaboration 状态正常且生效。
* TERMINATING: TERMINATING 表示卖家已移除 open collaboration，该 collaboration 即将过期。过期时间可在 current_commission 的 end_time 处找到。
   已移除且已过过 collabration 过期后不会在响应中返回。 |
   ^^current_commission |object | |当前对此开放协作生效的佣金信息。 |
   ^^^rate |int |3000 |该商品的佣金率由卖家为达人的公开推广设置。
   该取值的范围是 [100, 8000]。
   该值以 1/10000 为增量表示. 例如: 3000 表示实际佣金率为 30.00%, 3555 表示 35.55% |
   ^^^start_time |int |1725334422 |佣金率开始生效的 Unix 时间戳，单位为秒。 |
   ^^^end_time |int |1727625600 |佣金率停止生效的 Unix 时间戳，单位为秒。 |
   ^^showcase_creator_count |int |15 |此字段表示通过开放协作将商品添加到橱窗的达人数量。 |
   ^^content_creator_count |int |10 |此字段表示通过开放协作发布直播或视频的达人数量。 |
   ^^product |object | |开放协作绑定商品的信息。 |
   ^^^id |string |1729432087292775344 |商品的唯一 ID。 |
   ^^^title |string |Blue t-shirt |商品名称。 |
   ^^^main_image_url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 |商品图片 URL。 |
   ^^^status |string |LIVE |商品状态。
   字段值：
* LIVE：商品正常在售时，返回 LIVE 状态
* OUT_OF_STOCK：当商品对消费者缺货时，返回 OUT_OF_STOCK 状态
* SELLER_DEACTIVATE：当商品被卖家停用时，返回 SELLER_DEACTIVATE 状态
* PLATFORM_DEACTIVATE：当商品被平台停用或不可售时，返回 PLATFORM_DEACTIVATE 状态
* GNE_REJECT: 当商品被管控或开放协作被解除时，返回 GNE_REJECT 状态
* DELETE：商品被删除时，返回 DELETE 状态
* OTHER：商品处于不可售状态（如草稿、冻结、审核中等）时，返回 OTHER 状态 |
   ^^^inventory |int |1274 |该商品的库存。 |
   ^^^original_price |object | |商品原价 |
   ^^^^currency |string |USD |商品原价的三字母货币代码。 |
   ^^^^minimum_amount |string |12.21 |此商品所有 SKU 的最低原价。 |
   ^^^^maximum_amount |string |100.00 |此商品所有 SKU 的最高原价。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTEw","total_count":10000,"open_collaborations":[{"id":"94297006405","status":"NORMAL","current_commission":{"rate":3000,"start_time":1725334422,"end_time":1727625600},"showcase_creator_count":15,"content_creator_count":10,"product":{"id":"1729432087292775344","title":"Blue t-shirt","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","status":"LIVE","inventory":1274,"original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"}}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

