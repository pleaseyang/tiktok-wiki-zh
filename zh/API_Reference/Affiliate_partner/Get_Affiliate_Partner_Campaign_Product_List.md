# 获取 Affiliate Partner 活动 Product 列表

# 路径：/affiliate_partner/202405/campaigns/{campaign_id}/products
# 方法：[GET]
# 功能描述
此 API 提供列出 Affiliate Partner 活动中卖家提交的商品的功能。

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
| campaign_id | string | Y | 7373988288167036678 | 现有 Affiliate Partner 活动的数字 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
| page_size | int | Y | 10 | 每页返回的结果数量。值必须在 1 到 100 之间。 |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此参数。 |
| review_status | string | N | PENDING | 商品审核状态。此为枚举类型，取值如下： |

* PENDING
* APPROVED
* REJECTED
* PENDING_CLOSED
* CLOSED |
   product_name |string |N |sample |按商品名称筛选商品列表。如果 `product_name` 的值包含在 `product.name` 中，则该商品将包含在响应中。 |
   product_id |string |N |1730305356901683547 |按商品 ID 筛选商品列表。值必须为数字字符串。当此值与 `product.id` 匹配时，商品将被包含。 |
   shop_name |string |N |Test Shop |按 shop 名称筛选商品列表。如果 `shop_name` 的值包含在 `product.shop_name` 中，则该商品将包含在响应中。 |
   category_id |string |N |991496 |按 category ID 筛选商品列表。如果 `category_id` 的值与 `product.category.id` 匹配，或商品属于指定 category 的叶子类目，则该商品将包含在响应中。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202405/campaigns/7373988288167036678/products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=10&page_token=b2Zmc2V0PTAK&review_status=PENDING&product_name=sample&product_id=1730305356901683547&shop_name=Test Shop&category_id=991496
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 商品列表。 |
| ^^id | string | 1729442777527587334 | product 标识符。 |
| ^^review_status | string | PENDING | 商品审核状态。此为枚举类型，取值如下： |

* PENDING
* APPROVED
* REJECTED
* PENDING_CLOSED
* CLOSED |
   ^^name |string |test case number 4 test case number 4 |商品名称。 |
   ^^main_image_url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 |商品图片 URL。 |
   ^^lowest_price |object | |该商品所有 SKU 的最低原价。 |
   ^^^currency |string |USD |销售区域的货币代码。 |
   ^^^amount |string |1.1 |最低价格金额。 |
   ^^highest_price |object | |该商品所有 SKU 的最高原价。 |
   ^^^currency |string |USD |商品销售区域的货币代码。 |
   ^^^amount |string |12.21 |最高价格金额。 |
   ^^inventory |int |89 |该商品所有 SKU 的库存单位数量。 |
   ^^shop_name |string |my_shop |TikTok Shop 名称。 |
   ^^total_commission_rate |int |6600 |总佣金率，以百分之一的百分比（0.01%）为单位。 |
   ^^creator_commission_rate |int |1000 |达人佣金率，以百分之一的百分比（0.01%）为单位。 |
   ^^partner_commission_rate |int |5600 |合作伙伴佣金率，以百分之一的百分比（0.01%）为单位。 |
   ^^open_collaboration_commission_rate |int |1000 |商品开放合作佣金率，以百分之一的百分比（0.01%）为单位。
   |
   ^^is_available |bool |true |如果商品 URL 可用则设置为 `true`。如果商品 URL 不可用则设置为 `false`。 |
   ^^product_sales |int |10 |该活动中该商品的总销售单位数。 |
   ^^category |object | |该商品关联的叶子类目。 |
   ^^^id |string |12222 |category 标识符。 |
   ^^^name |string |COMPUTER |category 名称。 |
   ^^sample_quota |int |12 |卖家可用于分配给达人的样品库存总量。 |
   ^^sku_information_list |[]object | |用于标识商品不同变体的库存单位（SKU）列表。 |
   ^^^sku_name |string |factory product |sku 名称 |
   ^^^sku_id |string |1729666531097281876 |sku 的 id |
   ^^^inventory |object | |SKU 库存详情。 |
   ^^^^available_quantity |string |80 |仓库中可用的 SKU 总量。 |
   ^^^base_price |object | |sku 的基础价格 |
   ^^^^region_code |string |MY |sku 的区域代码 |
   ^^^^currency |string |MYR |SKU 价格的货币代码。
   基于区域的可能值：
* BRL: 巴西
* EUR: 法国、德国、爱尔兰、意大利、西班牙
* GBP: 英国
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^^list_price |string |162.34 |SKU 的标价信息，已经过审核团队验证合法。等同于制造商建议零售价（MSRP），或建议零售价（RRP）。 |
   ^^^^sale_price |string |162.34 |SKU 的售价，含税。
   仅适用于来自中国的跨境电商卖家。 |
   ^^^^localized_dutiable_price |string |141.58 |本地化应税价格
   |
   ^^^region_prices |[]object | |区域价格 |
   ^^^^region_code |string |MY |sku 的区域代码 |
   ^^^^currency |string |MYR |SKU 价格的货币代码。
   基于区域的可能值：
* BRL: 巴西
* EUR: 法国、德国、爱尔兰、意大利、西班牙
* GBP: 英国
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^^list_price |string |162.34 |SKU 的标价信息，已经过审核团队验证合法。等同于制造商建议零售价（MSRP），或建议零售价（RRP）。 |
   ^^^^sale_price |string |162.34 |SKU 的售价，含税。
   仅适用于来自中国的跨境电商卖家。 |
   ^^^^localized_dutiable_price |string |141.58 |本地化应税价格 |
   ^^^properties |[]object | |sku 的属性 |
   ^^^^name |string |Spesifikasi |属性名称 |
   ^^^^value_name |string |lalai |值名称 |
   ^^product_description |string |
   This is an example product description.
   |返回商品描述 |
   ^next_page_token |string |cGFnZV9udW1iZXI9Mg== |用于获取分页结果集下一页的不透明 token。当此值非空时，将其作为下一次请求中的 `page_token` 传入，并复用相同的 `campaign_id`、`category_asset_cipher`、`page_size`、`review_status`、`product_name`、`product_id`、`shop_name` 和 `category_id` 值，包括任何被省略的optional筛选条件。空的 `next_page_token` 表示没有更多页面。 |
   ^total_count |int |1570 |列表中的商品总数。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"id":"1729442777527587334","review_status":"PENDING","name":"test case number 4 test case number 4","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","lowest_price":{"currency":"USD","amount":"1.1"},"highest_price":{"currency":"USD","amount":"12.21"},"inventory":89,"shop_name":"my_shop","total_commission_rate":6600,"creator_commission_rate":1000,"partner_commission_rate":5600,"open_collaboration_commission_rate":1000,"is_available":true,"product_sales":10,"category":{"id":"12222","name":"COMPUTER"},"sample_quota":12,"sku_information_list":[{"sku_name":"factory product","sku_id":"1729666531097281876","inventory":{"available_quantity":"80"},"base_price":{"region_code":"MY","currency":"MYR","list_price":"162.34","sale_price":"162.34","localized_dutiable_price":"141.58"},"region_prices":[{"region_code":"MY","currency":"MYR","list_price":"162.34","sale_price":"162.34","localized_dutiable_price":"141.58"}],"properties":[{"name":"Spesifikasi","value_name":"lalai"}]}],"product_description":"\u003cp\u003eThis is an example product description.\u003c/p\u003e"}],"next_page_token":"cGFnZV9udW1iZXI9Mg==","total_count":1570},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 16032005 | Campaign not found |
| 16032007 | Permission denied |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

