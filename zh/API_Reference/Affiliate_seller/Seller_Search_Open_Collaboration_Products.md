# 卖家搜索 Open Collaboration 产品

# Path: /affiliate_seller/202405/open_collaborations/products/search
# Method: [POST]
# 功能描述
此 API 用于搜索 open collaboration 中的产品。您可以按产品名称、产品 ID 等条件筛选。

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
| sort_order | string | N | DESC | sort_field 参数的排序顺序。默认值：ASC |
| Possible values: |  |  |  |  |

* ASC: 升序
* DESC: 降序 |
   sort_field |string |N |commission_rate |返回结果将按指定字段排序。 See the description of the field values in the request body for more information about each field.
   Default: commission_rate
   Possible values:
* commission_rate
* product_sales_price
* commission
* units_sold |
   page_token |string |N |b2Zmc2V0PTIw |用于获取分页结果集下一页的不透明 token。请从上一次响应的 next_page_token 结果中获取此值。首页不需要此参数。 |
   page_size |int |Y |20 |每页返回的结果数量。有效范围：[1-20]。 |

# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| title_keywords | []string | N | ["Men", "Fashion"," Sports Short"] | 产品关键词列表。产品标题或名称进行模糊匹配。 Keywords in the list form a query and the resulting set of matching product names is based on the conjunctive operator `AND` between each keyword. For example, the keyword list `["Men", "Fashion"]` creates a query `"Men" AND "Fashion"` and the resulting set of matching product names contains the loosely matched conjuction of "Men" and "Fashion" such as "Male Fashionable". Maximum length of the list is 20 keywords. Maximum keyword string length is 255 characters. |
| sales_price_range | object | N |  | 将搜索结果中的产品限制为价格大于或等于指定最低价格且小于指定最高价格的产品。 |
| ^amount_ge | string | N | 12.44 | 产品价格必须大于此值才能包含在搜索结果中。值必须大于 `0`。 |
| ^amount_lt | string | N | 100 | 产品价格必须大于此值才能包含在搜索结果中。值必须大于 `0`。 No upper bound is set if this property is not included. |
| category | object | N |  | 将搜索结果中的产品限制为与指定产品分类关联的产品。 |
| ^id | string | N | 3412342 | 分类标识符。请注意，仅支持一级分类。 |
| commission_rate_range | object | N |  | 按 `rate_ge` 和 `rate_lt` 指定的 commission 比率范围筛选产品。 |
| ^rate_ge | int | N | 100 | Commission 比率大于或等于此值的产品包含在搜索结果中。比率以百分之一为单位；例如，`3587` 表示 `35.87%`。有效范围：[100, 8000]。 |
| ^rate_lt | int | N | 8000 | Commission 比率必须小于此值才能包含在搜索结果中。Commission 比率以百分之一为单位。例如，`3587` 表示 `35.87%` 的 commission 比率。此值最小为 `100`。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202405/open_collaborations/products/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&sort_order=DESC&sort_field=commission_rate&page_token=b2Zmc2V0PTIw&page_size=20
```

**Body**
```json
{"title_keywords":["Men","Fashion"," Sports Short"],"sales_price_range":{"amount_ge":"12.44","amount_lt":"100"},"category":{"id":"3412342"},"commission_rate_range":{"rate_ge":100,"rate_lt":8000}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 符合请求体中搜索条件的产品列表。 |
| ^^shop | object |  | 与销售产品的 TikTok Shop 关联的元数据和数据。 |
| ^^^name | string | Test shop | TikTok 店铺名称。 |
| ^^id | string | 1729432087292775344 | 产品标识符。 |
| ^^has_inventory | bool | false | 如果产品库存大于零，则设置为 `true`。如果库存为零，则设置为 `false`。 |
| ^^units_sold | int | 12123 | 此产品的总销售件数。 |
| ^^title | string | Blue t-shirt | 产品名称。 |
| ^^sale_region | string | ID | 产品提供销售的地区。 |
| ^^main_image_url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 | 产品图片 URL。 |
| ^^detail_link | string | https://shop.tiktok.com/view/product/1729624807198591373?region=ID&local=en | 产品详情页面的 URL。 |
| ^^original_price | object |  | The original price of the product. |
| ^^^currency | string | USD | 币种代码。 |
| ^^^minimum_amount | string | 12.21 | The lowest original price of all SKUs of the product. |
| ^^^maximum_amount | string | 100.00 | The highest original price of all SKUs of the product. |
| ^^category_chains | []object |  | 与产品关联的分类列表。 |
| ^^^id | string | 343554 | The category identifier. |
| ^^^local_name | string | COMPUTER | 分类名称。 |
| ^^^is_leaf | bool | false | 如果此分类是叶节点，则设置为 `true`。否则设置为 `false`。 |
| ^^^parent_id | string | 342948 | 该分类的父分类的分类标识符。 |
| ^^commission | object |  | 与产品 commission 比率关联的元数据和数据。 |
| ^^^rate | int | 3000 | Commission 比率，以百分之一为单位。 For example, `3587` is a commission rate of `35.87%`. This value must a minimum of `1000`. |
| ^^^currency | string | USD | 币种代码。 |
| ^^^amount | string | 121.32 | Commission 金额。 |
| ^^sales_price | object |  | 产品的促销价格范围。 |
| ^^^currency | string | USD | 币种代码。 |
| ^^^minimum_amount | string | 34.3 | 此产品所有 SKU 的最低促销价格。 |
| ^^^maximum_amount | string | 55.7 | 此产品所有 SKU 的最高促销价格。 |
| ^next_page_token | string | b2Zmc2V0PTEw | An opaque token used to retrieve the next page of a paginated result set. If this value is non-empty, pass it as page_token in the next request and keep shop_cipher, page_size, sort_field, sort_order, and the request body unchanged. An empty value means that there are no more pages. |
| ^total_count | int | 10000 | 符合请求体中搜索条件的产品总数。 |
# 响应示例
```json
{"code":0,"data":{"products":[{"shop":{"name":"Test shop"},"id":"1729432087292775344","has_inventory":false,"units_sold":12123,"title":"Blue t-shirt","sale_region":"ID","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","detail_link":"https://shop.tiktok.com/view/product/1729624807198591373?region=ID\u0026local=en","original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"},"category_chains":[{"id":"343554","local_name":"COMPUTER","is_leaf":false,"parent_id":"342948"}],"commission":{"rate":3000,"currency":"USD","amount":"121.32"},"sales_price":{"currency":"USD","minimum_amount":"34.3","maximum_amount":"55.7"}}],"next_page_token":"b2Zmc2V0PTEw","total_count":10000},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

