# 通过产品 ID 获取 Open Collaboration 产品列表

# Path: /affiliate_creator/202509/open_collaborations/products
# Method: [POST]
# 功能描述
获取指定产品 ID 的 open collaboration 产品信息。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop APIs - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| product_ids | []string | N | 123,456 | 以逗号分隔的数字产品 ID 列表。每次请求最多 50 个 ID。 |
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
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 根据请求的产品 ID 找到的产品。响应可能包含的产品数少于请求数。 |
| ^^shop | object |  | 产品的店铺信息。 |
| ^^^name | string | Test shop | 产品所属店铺的名称。 |
| ^^id | string | 1729432087292775344 | 产品的唯一 ID。 |
| ^^has_inventory | bool | false | 此产品是否有库存。 |
| ^^units_sold | int | 12 | 此产品的已售总件数。 |
| ^^title | string | Blue t-shirt | 产品名称。 |
| ^^sale_region | string | ID | 该区域代表产品可以销售的地区。 |
| ^^main_image_url | string | https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 | 产品图片 URL。 |
| ^^detail_link | string | https://shop.tiktok.com/view/product/1729624807198591373?region=ID&local=en | 产品详情链接，用于在移动端获取产品详情。 |
| ^^original_price | object |  | 产品原价 |
| ^^^currency | string | USD | 销售区域的货币。 |
| ^^^minimum_amount | string | 12.21 | 此产品所有 SKU 的最低原价。 |
| ^^^maximum_amount | string | 100.00 | 此产品所有 SKU 的最高原价。 |
| ^^category_chains | []object |  | 此产品的类别。 |
| 最多返回前三个类别 |  |  |  |
| ^^^id | string | 3435545 | 此产品的当前类别 ID。 |
| ^^^local_name | string | COMPUTER | 此产品当前级别的类别名称。 |
| ^^^is_leaf | bool | false | 指示当前节点是否为叶节点 |
| ^^^parent_id | string | 12345 | 其父类别的类别 ID |
| ^^commission | object |  | 此产品的 commission。 |
| ^^^rate | int | 100 | - 此产品的 commission 费率由商家为 creator 公开推广设置。 |

* 此值的范围为 [100, 8000]。
* 此值等于实际 commission 费率乘以 10000。例如：3000 表示实际 commission 费率为 30.00%，3555 表示 35.55% |
   ^^^currency |string |USD |Currency code for the commission amount. |
   ^^^amount |string |0 |The commission amount calculated from the product's promotional price and commission rate. When both minimum and maximum promotional prices are available, the value is formatted as `<minimum commission> - <maximum commission>`; otherwise, it contains the available commission amount. If neither price is available, the value is `0`. The currency is specified by `commission.currency`. |
   ^^sales_price |object | |Sales price information of the product |
   ^^^currency |string |USD |Currency code for the promotional price. |
   ^^^minimum_amount |string |34.3 |The minimum promotion price of all skus of this product. |
   ^^^maximum_amount |string |55.7 |The maximum promotion price of all skus of this product. |
   ^^shop_ads_commission |object | |The ads commission rate applies only to orders generated from ads. If a creator’s video is used as an ad without this rate being set, the resulting orders will instead earn either:
* 您在 open collaboration 中配置的 Shop Ads commission，或
* 此邀请中定义的标准 commission。 |
   ^^^rate |int |100 |The Shop Ads commission rate for this product, multiplied by 10,000. The range is 100 to 8,000. For example, 3,000 represents 30.00% and 3,555 represents 35.55%. |

# 响应示例
```json
{"code":0,"data":{"products":[{"shop":{"name":"Test shop"},"id":"1729432087292775344","has_inventory":false,"units_sold":12,"title":"Blue t-shirt","sale_region":"ID","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","detail_link":"https://shop.tiktok.com/view/product/1729624807198591373?region=ID\u0026local=en","original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"},"category_chains":[{"id":"3435545","local_name":"COMPUTER","is_leaf":false,"parent_id":"12345"}],"commission":{"rate":100,"currency":"USD","amount":"0"},"sales_price":{"currency":"USD","minimum_amount":"34.3","maximum_amount":"55.7"},"shop_ads_commission":{"rate":100}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop APIs - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |

