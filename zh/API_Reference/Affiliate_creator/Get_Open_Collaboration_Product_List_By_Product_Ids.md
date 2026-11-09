# 通过商品 ID 获取 Open Collaboration 商品列表

# 路径：/affiliate_creator/202509/open_collaborations/products
# 方法：[POST]
# 功能描述
获取指定商品 ID 的 open collaboration 商品信息。

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
| product_ids | []string | N | 123,456 | 以逗号分隔的数字商品 ID 列表。每次请求最多 50 个 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202509/open_collaborations/products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&product_ids=123,456
```

**Body**
```json
{}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 根据请求的商品 ID 找到的商品。响应可能包含的商品数少于请求数。 |
| ^^shop | object |  | 商品的店铺信息。 |
| ^^^name | string | Test shop | 商品所属店铺的名称。 |
| ^^id | string | 1729432087292775344 | 商品的唯一 ID。 |
| ^^has_inventory | bool | false | 此商品是否有库存。 |
| ^^units_sold | int | 12 | 此商品的已售总件数。 |
| ^^title | string | Blue t-shirt | 商品名称。 |
| ^^sale_region | string | ID | 该区域代表商品可以销售的地区。 |
| ^^main_image_url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 | 商品图片 URL。 |
| ^^detail_link | string | https://shop.tiktok.com/view/product/1729624807198591373?region=ID&local=en | 商品详情链接，用于在移动端获取商品详情。 |
| ^^original_price | object |  | 商品原价 |
| ^^^currency | string | USD | 销售区域的货币。 |
| ^^^minimum_amount | string | 12.21 | 此商品所有 SKU 的最低原价。 |
| ^^^maximum_amount | string | 100.00 | 此商品所有 SKU 的最高原价。 |
| ^^category_chains | []object |  | 此商品的类别。 |
| 最多返回前三个类别 |  |  |  |
| ^^^id | string | 3435545 | 此商品的当前类别 ID。 |
| ^^^local_name | string | COMPUTER | 此商品当前级别的类别名称。 |
| ^^^is_leaf | bool | false | 指示当前节点是否为叶节点 |
| ^^^parent_id | string | 12345 | 其父类别的类别 ID |
| ^^commission | object |  | 此商品的佣金。 |
| ^^^rate | int | 100 | - 此商品的佣金费率由卖家为达人公开推广设置。 |

* 此值的范围为 [100, 8000]。
* 此值等于实际佣金费率乘以 10000。例如：3000 表示实际佣金费率为 30.00%，3555 表示 35.55% |
   ^^^currency |string |USD |佣金金额的货币代码。 |
   ^^^amount |string |0 |根据商品促销价和佣金率计算出的佣金金额。当最低和最高促销价都可用时，该值格式为 `<minimum commission> - <maximum commission>`；否则包含可用的佣金金额。如果两个价格都不可用，该值为 `0`。货币由 `commission.currency` 指定。 |
   ^^sales_price |object | |商品的销售价格信息 |
   ^^^currency |string |USD |促销价格的货币代码。 |
   ^^^minimum_amount |string |34.3 |此商品所有 SKU 的最低推广价。 |
   ^^^maximum_amount |string |55.7 |此商品所有 SKU 的最高推广价。 |
   ^^shop_ads_commission |object | |广告佣金率仅适用于由广告产生的订单。如果达人的视频被用作广告且未设置此费率，则产生的订单将改为按以下之一获得佣金：
* 您在 open collaboration 中配置的 Shop Ads 佣金，或
* 此邀请中定义的标准佣金。 |
   ^^^rate |int |100 |此商品的 Shop Ads 佣金费率，乘以 10,000。范围为 100 到 8,000。例如，3,000 表示 30.00%，3,555 表示 35.55%。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"shop":{"name":"Test shop"},"id":"1729432087292775344","has_inventory":false,"units_sold":12,"title":"Blue t-shirt","sale_region":"ID","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","detail_link":"https://shop.tiktok.com/view/product/1729624807198591373?region=ID\u0026local=en","original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"},"category_chains":[{"id":"3435545","local_name":"COMPUTER","is_leaf":false,"parent_id":"12345"}],"commission":{"rate":100,"currency":"USD","amount":"0"},"sales_price":{"currency":"USD","minimum_amount":"34.3","maximum_amount":"55.7"},"shop_ads_commission":{"rate":100}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop APIs - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |

