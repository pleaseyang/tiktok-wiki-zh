# 搜索 Open Collaboration 商品

# 路径：/affiliate_creator/202405/open_collaborations/products/search
# 方法：[POST]
# 功能描述
此 API 用于按类别、佣金费率和关键词搜索 open collaboration 商品信息。它将返回 TikTok Shop Affiliate 商品市场上所有处于 open collaboration 状态的商品。
达人只能在其注册 affiliate 的区域内搜索 open collaboration。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop APIs - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | b2Zmc2V0PTAK | 分页 token。在第一次请求中留空此参数。要检索下一页，传递上一次响应返回的 `next_page_token`，并复用相同的 `category`、`commission_rate_range`、`sales_price_range`、`title_keywords`、`sort_field`、`sort_order` 和 `page_size` 值。空的 `next_page_token` 表示没有更多页面。 |
| page_size | int | Y | 20 | "page_size" 的值必须大于 0 且小于或等于 20。 |
| sort_field | string | N | commission_rate | 返回的结果按指定字段排序。 |
可能的值：

* commission_rate
* product_sales_price
* commission
* units_sold

使用 `sort_order` 参数指定排序顺序。
|
sort_order |string |N |DESC |响应中对象的排序顺序。默认值：ASC
可能的值：

* ASC：升序
* DESC：降序 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| title_keywords | []string | N | ["Men", "Fashion"," Sports Short"] | 用于搜索的商品关键词列表。商品标题或名称进行模糊匹配。列表中的关键词形成查询，匹配商品名称的结果集基于每个关键词之间的 `AND` 连接运算符。例如，关键词列表 `["Men", "Fashion"]` 创建查询 `"Men" AND "Fashion"`，匹配商品名称的结果集包含模糊匹配的 "Men" 和 "Fashion" 的组合，如 "Male Fashionable"。列表最大长度为 20 个关键词。关键词字符串最大长度为 255 个字符。 |
| sales_price_range | object | N |  | 将搜索结果中的商品限制为价格大于或等于指定最低价格且低于指定最高价格的商品。 |
| ^amount_ge | string | N | 12.44 | 商品价格必须大于此值才能包含在搜索结果中。该值必须大于 `0`。 |
| ^amount_lt | string | N | 100 | 商品价格必须大于此值才能包含在搜索结果中。该值必须大于 `0`。如果不包含此属性，则不设置上限。 |
| category | object | N |  | 将搜索结果中的商品限制为与指定商品类别关联的商品。 |
| ^id | string | N | 341234 | 类别标识符。请注意，仅支持一级类别。 |
| commission_rate_range | object | N |  | 搜索商品的佣金费率需要限制在此范围内。 |
| ^rate_ge | int | N | 100 | 最低佣金费率。佣金费率大于或等于此值的商品将包含在结果中。费率以百分比的百分之一表示；例如，`3587` 表示 `35.87%`。该值必须在 `100` 到 `8000` 之间（含）。 |
| ^rate_lt | int | N | 8000 | 佣金费率必须低于此值才能包含在搜索结果中。佣金费率以百分比的百分之一表示。例如，`3587` 表示佣金费率为 `35.87%`。此值最小为 `1000`。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202405/open_collaborations/products/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_token=b2Zmc2V0PTAK&page_size=20&sort_field=commission_rate&sort_order=DESC
```

**Body**
```json
{"title_keywords":["Men","Fashion"," Sports Short"],"sales_price_range":{"amount_ge":"12.44","amount_lt":"100"},"category":{"id":"341234"},"commission_rate_range":{"rate_ge":100,"rate_lt":8000}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 商品列表。 |
| ^^shop | object |  | 与卖家的 TikTok Shop 相关的数据和元数据。 |
| ^^^name | string | Test shop | TikTok Shop 名称。 |
| ^^id | string | 1729432087292775344 | 商品标识符。 |
| ^^has_inventory | bool | false | 如果商品库存大于零，设置为 `true`。如果库存为零，设置为 `false`。 |
| ^^units_sold | int | 12123 | 已售出的总件数。件数按 SKU 索引。请注意，如果达人未授予精确数据共享权限，则此属性将不存在。 |
| ^^title | string | Blue t-shirt | 商品名称。 |
| ^^sale_region | string | ID | 商品提供销售的区域。 |
| ^^main_image_url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 | 商品图片 URL。 |
| ^^detail_link | string | https://shop.tiktok.com/view/product/1729624807198591373?region=ID&local=en | 商品详情页的 URL。 |
| ^^original_price | object |  | 商品原价。 |
| ^^^currency | string | USD | 货币代码。 |
| ^^^minimum_amount | string | 12.21 | 商品所有 SKU 的最低原价。 |
| ^^^maximum_amount | string | 100.00 | 商品所有 SKU 的最高原价。 |
| ^^category_chains | []object |  | 与商品关联的类别列表。列表最大长度为 `3` 个类别。 |
| ^^^id | string | 343554 | 类别标识符。 |
| ^^^local_name | string | COMPUTER | 本地化的类别名称。 |
| ^^^is_leaf | bool | false | 如果此类别是叶节点，设置为 `true`。否则设置为 `false`。 |
| ^^^parent_id | string | 341182 | 父类别的类别标识符。 |
| ^^commission | object |  | 与商品佣金费率相关的元数据和数据。 |
| ^^^rate | int | 3000 | 佣金费率，以百分比的百分之一表示。例如，`3587` 表示佣金费率为 `35.87%`。此值最小为 `1000`。此值的范围为 [100, 8000]。 |
| ^^^currency | string | USD | 货币代码。 |
| ^^^amount | string | 121.32 | 佣金金额。 |
| ^^sales_price | object |  | 与商品销售价格相关的元数据和数据 |
| ^^^currency | string | USD | 货币代码。 |
| ^^^minimum_amount | string | 34.3 | 此商品所有 SKU 的最低推广价。 |
| ^^^maximum_amount | string | 55.7 | 此商品所有 SKU 的最高推广价。 |
| ^next_page_token | string | b2Zmc2V0PTEw | 用于检索分页结果集下一页的不透明 token。 |
| ^total_count | int | 10000 | 符合请求体中搜索条件的商品总数。 |
# 响应示例
```json
{"code":0,"data":{"products":[{"shop":{"name":"Test shop"},"id":"1729432087292775344","has_inventory":false,"units_sold":12123,"title":"Blue t-shirt","sale_region":"ID","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","detail_link":"https://shop.tiktok.com/view/product/1729624807198591373?region=ID\u0026local=en","original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"},"category_chains":[{"id":"343554","local_name":"COMPUTER","is_leaf":false,"parent_id":"341182"}],"commission":{"rate":3000,"currency":"USD","amount":"121.32"},"sales_price":{"currency":"USD","minimum_amount":"34.3","maximum_amount":"55.7"}}],"next_page_token":"b2Zmc2V0PTEw","total_count":10000},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop APIs - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |

