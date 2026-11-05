# 搜索 Open Collaboration

# Path: /affiliate_seller/202412/open_collaborations/search
# Method: [POST]
# 功能描述
搜索商家的 open collaboration。响应包括产品详情、当前 commission 信息、将每个产品添加到 showcase 的 creator 数量，以及发布 LIVE 或视频内容的 creator 数量。

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
| page_token | string | N | b2Zmc2V0PTAK | 分页 token，用于确定搜索的起始位置。首次请求时请将此参数留空。后续请求时，传入上一次响应返回的 `next_page_token`，并复用相同的请求体筛选条件、`sort_field`、`sort_order` 和 `page_size`。 |
| page_size | int | Y | 50 | "page_size" 的值必须大于 0 且小于或等于 100。 |
| sort_order | string | N | DESC | "sort_order" 的默认值为 DESC。 |
| Enum: |  |  |  |  |

* ASC：表示按升序排序数据
* DESC：表示按降序排序数据 |
   sort_field |string |N |product_original_price |部分可排序字段如下：
* product_original_price: 按产品原始价格排序。
   默认情况下，open collaboration 按创建时间降序排列。 |

# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| keyword_type | string | N | PRODUCT_ID | 指定 `keyword` 中的值类型。要按产品名称或产品 ID 筛选 open collaboration，请同时提供 `keyword_type` 和 `keyword`。 |
| Possible values: |  |  |  |  |

* `PRODUCT_ID`: 搜索指定产品 ID 的 open collaboration 信息。
* `PRODUCT_NAME`: 按相关产品名称模糊搜索 open collaboration 信息。 |
   keyword |string |N |7625459350921 |基于产品名称或产品 ID 进行搜索。根据上述 keyword_type 传入相应的值。 |
   top_level_category_id |string |N |60001 |按一级分类 ID 筛选产品。
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
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTEw | 下一页的分页 token。 将此值作为 `page_token` 传入下一次请求。空值表示没有更多结果。 |
| ^total_count | int | 10000 | 符合所有输入搜索条件的产品总数。 |
| ^open_collaborations | []object |  | 当前页面中符合搜索条件的 open collaboration。 |
| ^^id | string | 94297006405 | Open collaboration ID |
| ^^status | string | NORMAL | Open collaboration 的状态。 |
| 字段值： |  |  |  |

* NORMAL：NORMAL 表示当前 open collaboration 状态正常且生效。
* TERMINATING: TERMINATING 表示商家已移除 open collaboration，该 collaboration 即将过期。过期时间可在 current_commission 的 end_time 处找到。
   已移除且已过过 collabration 过期后不会在响应中返回。 |
   ^^current_commission |object | |The commission information is currently in effect for this open collaboration. |
   ^^^rate |int |3000 |The commission rate for this product is set by merchants for creators' public promotion.
   The range of this value is [100, 8000].
   This value is expressed in 1/10000 increments. For example: 3000 means the actual commission rate is 30.00%, and 3555 means 35.55% |
   ^^^start_time |int |1725334422 |The Unix timestamp, in seconds, when the commission rate becomes effective. |
   ^^^end_time |int |1727625600 |The Unix timestamp, in seconds, when the commission rate stops being effective. |
   ^^showcase_creator_count |int |15 |This field indicates the number of creators who added the product to the showcase from open collaboration. |
   ^^content_creator_count |int |10 |This field indicates the number of creators who posted the LIve or Video from open collaboration. |
   ^^product |object | |The open collaboration bound product information. |
   ^^^id |string |1729432087292775344 |Product's unique id. |
   ^^^title |string |Blue t-shirt |Product's name. |
   ^^^main_image_url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 |The product image url. |
   ^^^status |string |LIVE |Product's status.
   字段值：
* LIVE: When the product is normal for sale, return to the LIVE status
* OUT_OF_STOCK: When the product is out of stock for the consumer, the OUT_OF_STOCK state is returned
* SELLER_DEACTIVATE: When the product is deactivated by the merchant, the SELLER_DEACTIVATE status is returned
* PLATFORM_DEACTIVATE: When the product is deactivated by the platform or is not available for sale, the PLATFORM_DEACTIVATE status is returned
* GNE_REJECT: When the product is governed or the open collaboration is dismissed, the GNE_REJECT state is returned
* DELETE: When the product is deleted, the DELETE status is returned
* OTHER: When the product is in an unsaleable state, such as draft, frozen, review, etc, the OTHER status is returned |
   ^^^inventory |int |1274 |The inventory of this product. |
   ^^^original_price |object | |The product's original price |
   ^^^^currency |string |USD |The three-letter currency code of the product's original price. |
   ^^^^minimum_amount |string |12.21 |The minimum original price of all skus of this product. |
   ^^^^maximum_amount |string |100.00 |The maximum original price of all skus of this product. |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTEw","total_count":10000,"open_collaborations":[{"id":"94297006405","status":"NORMAL","current_commission":{"rate":3000,"start_time":1725334422,"end_time":1727625600},"showcase_creator_count":15,"content_creator_count":10,"product":{"id":"1729432087292775344","title":"Blue t-shirt","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","status":"LIVE","inventory":1274,"original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"}}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

