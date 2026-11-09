# 获取店铺商品

# 路径：/affiliate_creator/202509/shop_products
# 方法：[GET]
# 功能描述
搜索已认证达人所绑定店铺中的商品。可选择使用 `title_keyword` 按标题筛选商品。调用此接口前，达人必须已绑定店铺。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| title_keyword | string | N | apple | 你想要搜索的商品标题关键词。 |
| sort_field | string | N | PRODUCT_ID | Sort field. |
| 可能的值： |  |  |  |  |

* PRODUCT_ID
* PRICE
* SALE

如果省略或为空，默认为 PRODUCT_ID. 其他任何取值将被拒绝。 |
sort_order |string |N |DESC |排序顺序。
可能的值：

* DESC
* ASC

如果省略或为空，默认为 DESC. 其他任何取值均被拒绝。 |
page_size |int |Y |20 |分页数量决定发送请求后获取的商品数量. 20 为推荐数值。
Valid Range: [1-100] |
page_token |string |N |b2Zmc2V0PTAK |用于获取下一页的不透明令牌。首次请求时请将此参数留空。对于后续请求，传入上一次响应返回的 `next_page_token`，并复用相同的 `title_keyword`、`sort_field`、`sort_order` 和 `page_size` 值。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202509/shop_products?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&title_keyword=apple&sort_field=PRODUCT_ID&sort_order=DESC&page_size=20&page_token=b2Zmc2V0PTAK
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 搜索到的商品列表。无搜索结果时为空。 |
| ^^id | string | 1729592969712207012 | TikTok 商品 ID。 |
| ^^title | string | testcase autotest Live Product | Product name. |
| ^^price | object |  | 以两位小数并带货币显示的商品价格。 |
| ^^^amount | string | 56.00 | 带两位小数的商品价格。 |
| ^^^currency | string | USD | 商品价格货币，取决于达人可销售的地区。 |
| ^^added_status | string | ADDABLE |  |
| 橱窗添加状态，可能的取值: |  |  |  |

* ADDABLE
* ADDED
* REJECTED |
   ^^brand_name |string |Apple |卖家为商品设置的品牌名称。 |
   ^^images |[]object | |商品的图片。 |
   ^^^url |string |https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/982dd6b4e46a6a24203b00611a474cca~c5_1080x1080.webp |商品图片的 URL。 |
   ^^^width |int |200 |商品图片宽度。 |
   ^^^height |int |200 |商品图片高度。 |
   ^^sales_count |int |33 |已售出的商品数量。 |
   ^total_count |int |300 |符合查询条件的商品总数。 |
   ^next_page_token |string |b2Zmc2V0PTIw |用于获取下一页的不透明令牌。在下次请求中将其作为 `page_token` 传入。当没有更多商品可检索时，此值为空。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"id":"1729592969712207012","title":"testcase autotest Live Product","price":{"amount":"56.00","currency":"USD"},"added_status":"ADDABLE\n","brand_name":"Apple","images":[{"url":"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/982dd6b4e46a6a24203b00611a474cca~c5_1080x1080.webp","width":200,"height":200}],"sales_count":33}],"total_count":300,"next_page_token":"b2Zmc2V0PTIw"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

