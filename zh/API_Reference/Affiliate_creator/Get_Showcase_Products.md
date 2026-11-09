# 获取橱窗商品

# 路径：/affiliate_creator/202405/showcases/products
# 方法：[GET]
# 功能描述
此 API 列出达人橱窗中的商品，按指定的 page size 分页，并通过 page token 迭代页面，最多展示橱窗中的 2000 个商品。当达人想要查看橱窗中的商品时，通常使用此 API。平台将返回橱窗中的商品详情，以及达人正在直播时 livebag 中的商品。

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
| page_size | int | Y | 10 | 每页返回的结果数。有效范围：[1-20]。 |
| page_token | string | N | V231as2V0PTAK | 用于检索分页结果集下一页的不透明 token。从上一次响应的 next_page_token 结果中获取此值。第一页不需要此参数。 |
| origin | string | Y | LIVE | 设置为 `LIVE` 表示请求来自直播间。设置为 `SHOWCASE` 表示请求来自橱窗。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202405/showcases/products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_size=10&page_token=V231as2V0PTAK&origin=LIVE
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 商品列表。 |
| ^^id | string | 53219092314 | 商品的 product ID |
| ^^shop | object |  | 与卖家的 TikTok Shop 相关的数据和元数据。 |
| ^^^name | string | Gift store | TikTok Shop 名称。 |
| ^^addition | object |  | 包含商品图片数据的对象。 |
| ^^^customized_main_images | []object |  | 商品图片列表。 |
| ^^^^width | int | 100 | 图片宽度（像素）。 |
| ^^^^heigth | int | 100 | 图片高度（像素）。 |
| ^^^^url | string | https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d76b8cc1b598de90ad5048df46e672b3~c5_100x100.webp?x-expires=1691895600&x-signature=oAT9KOL7aCN3Did9U%2FoKEsbBDj0%3D | 商品的 TikTok Shop 图片 URL。 |
| ^^price | object |  | 包含商品价格数据的对象。 |
| ^^^original_price | object |  | 商品原价。 |
| ^^^^minimum_amount | string | 12.21 | 商品最低原价。 |
| ^^^^maximum_amount | string | 100.00 | 商品最高原价。 |
| ^^^^currency | string | USD | ISO 4217 货币代码。 |
| ^^^seller_discount_price | object |  | 包含商品折扣价数据的对象。 |
| ^^^^minimum_amount | string | 12.21 | 最低折扣价。 |
| ^^^^maximum_amount | string | 100.00 | 最高折扣价。 |
| ^^^^currency | string | USD | ISO 4217 货币代码。 |
| ^^^platform_discount_price | object |  | 包含商品平台折扣价数据的对象。 |
| ^^^^minimum_amount | string | 12.21 | 最低商品平台折扣价。 |
| ^^^^maximum_amount | string | 100.00 | 最高商品平台折扣价。 |
| ^^^^currency | string | USD | ISO 4217 货币代码。 |
| ^^title | string | Chirstmas Gift | 商品展示标题。 |
| ^^main_images | []object |  | 商品图片列表。 |
| ^^^width | int | 100 | 图片宽度（像素）。 |
| ^^^heigth | int | 100 | 图片高度（像素）。 |
| ^^^url | string | https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d76b8cc1b598de90ad5048df46e672b3~c5_100x100.webp?x-expires=1691895600&x-signature=oAT9KOL7aCN3Did9U%2FoKEsbBDj0%3D | 商品的 TikTok Shop 图片 URL。 |
| ^^status | object |  | 包含商品状态信息的对象。 |
| ^^^inventory_status | string | IN_STOCK | 商品库存状态。这是枚举类型，取值如下： |

* IN_STOCK（有库存）
* SOLD_OUT（售罄） |
   ^^^review_status |string |APPROVED |商品审核状态。这是枚举类型，取值如下：
* APPROVED（已通过）
* UNDER_REVIEW（审核中）
* CHANGES_UNDER_REVIEW（变更审核中）
* UNAVAILABLE（不可用）
* REJECTED（已拒绝）
* ZERO_COMMISSION（零佣金） |
   ^^^is_hidden |bool |false |如果商品在橱窗中可见，则设置为 `false`。如果商品从橱窗中隐藏，则设置为 `true`。 |
   ^^^added_status |string |ADDED |商品针对请求来源的添加状态。对于 `SHOWCASE`，`ADDED` 表示商品已在橱窗中，而 `REJECTED` 表示商品被拒绝在当前语境下使用。对于 `LIVE`，`ADDED` 表示商品已在直播间商品列表（live bag）中，`NOT_ADDED` 表示商品可添加，`REJECTED` 表示商品无法添加。 |
   ^^source |string |AFFILIATE |商品来源。这是枚举类型，取值如下：
* THIRD_PARTY（第三方）
* AFFILIATE
* TIKTOK_STORE |
   ^^detail_link |string |https://shop.tiktok.com/view/product/248901892031?region=US&local=en |商品详情页 URL。 |
   ^^third_party_link |string |https://storename.myshopify.com/products/gold-bracelet-engraved-with-diamonds |TikTok Shop 外部商品详情页 URL。 |
   ^^sale_regions |[]string |["US"] |商品提供销售的区域列表。 |
   ^^佣金 |object | |包含与商品相关的佣金数据的对象。 |
   ^^^rate |int |3000 |佣金率，以 0.01% 为单位。例如，`3587` 表示 `35.87%` 的佣金率。该取值的范围为 [100, 8000]。 |
   ^^^reward_rate |int |500 |奖励佣金率，以万分之一为单位. 例如，`3587` 表示 `35.87%` 的佣金率。 |
   ^^collaboration |object | |包含商品 collaboration 数据的对象。 |
   ^^^id |string |7495383576027499219 |collaboration 标识符。 |
   ^^^type |string |1 |collaboration 类型。这是枚举类型，取值如下：
   1 - Open Collaboration
   2 - Target Collaboration
   5 - Partner Campaign
   11 - Flat Fee
   12 - Collaboration Plus
   13 - Affiliate Promotion |
   ^^^合作伙伴 |object | |合作伙伴信息。 |
   ^^^^id |string |123456789 |合作伙伴标识符。 |
   ^^^^name |string |合作伙伴 Name |合作伙伴名称。 |
   ^next_page_token |string |V231as2V0PTAK |用于获取分页结果集下一页的不透明 token。 |
   ^total_count |int |15 |响应中商品的总数。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"id":"53219092314","shop":{"name":"Gift store"},"addition":{"customized_main_images":[{"width":100,"heigth":100,"url":"https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d76b8cc1b598de90ad5048df46e672b3~c5_100x100.webp?x-expires=1691895600\u0026x-signature=oAT9KOL7aCN3Did9U%2FoKEsbBDj0%3D"}]},"price":{"original_price":{"minimum_amount":"12.21","maximum_amount":"100.00","currency":"USD"},"seller_discount_price":{"minimum_amount":"12.21","maximum_amount":"100.00","currency":"USD"},"platform_discount_price":{"minimum_amount":"12.21","maximum_amount":"100.00","currency":"USD"}},"title":"Chirstmas Gift","main_images":[{"width":100,"heigth":100,"url":"https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d76b8cc1b598de90ad5048df46e672b3~c5_100x100.webp?x-expires=1691895600\u0026x-signature=oAT9KOL7aCN3Did9U%2FoKEsbBDj0%3D"}],"status":{"inventory_status":"IN_STOCK","review_status":"APPROVED","is_hidden":false,"added_status":"ADDED"},"source":"AFFILIATE","detail_link":"https://shop.tiktok.com/view/product/248901892031?region=US\u0026local=en","third_party_link":"https://storename.myshopify.com/products/gold-bracelet-engraved-with-diamonds","sale_regions":["US"],"commission":{"rate":3000,"reward_rate":500},"collaboration":{"id":"7495383576027499219","type":"1","partner":{"id":"123456789","name":"Partner Name"}}}],"next_page_token":"V231as2V0PTAK","total_count":15},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop APIs - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
| 18001405 | 该达人账户没有选择区域。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

