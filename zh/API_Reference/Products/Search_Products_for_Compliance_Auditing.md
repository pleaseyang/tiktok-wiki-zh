# 搜索合规审核商品

# 路径：/product/202601/compliance/auditing/research
# 方法：[POST]
# 功能描述
搜索在售商品并获取合规服务商准备合规检测报告所需的商品信息。选择行为如下：

* 如果 `product_ids` 非空，此操作将检索这些已知商品。此分支优先；卖家、商品标题、类目和品牌筛选以及分页均不用于选择商品。
* 否则，该操作执行店铺搜索，并要求提供 `seller_id`、`seller_name` 或两者。当同时提供两个店铺标识符时，其匹配到的卖家会合并。你还可以按商品标题、类目 ID 和品牌 ID 进一步筛选此搜索并对结果分页。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| shop_cipher | string | N | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |
| category_asset_cipher | string | N | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值，将返回 API 请求中使用的合作伙伴标识符。 |
| 通过使用 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此取值。 |  |  |  |  |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_token | string | N | ["1733419489460520284"] | 用于获取下一页的不透明令牌。首页请省略此参数或传入空字符串。后续页面请传入上一次响应返回的 `next_page_token`。 |
| page_size | int | Y | 20 | 每页返回的结果数量。 |
| 有效范围： [1-50] |  |  |  |  |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_title | string | N | mike noritama cute calico cat | 商品标题。 |
| 标题长度： |  |  |  |  |

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* 其他地区: [25, 255] |
   product_ids |[]string |N |["123123","1235677","456756"] |由 TikTok Shop 生成的商品 ID。最多 20 个 |
   seller_id |string |N |1733337095719126364 |店铺身份 ID。 |
   category_ids |[]string |N |["602118"] |按 TikTok Shop 类目 ID 筛选店铺搜索结果。 |
   brand_ids |[]string |N |["602118"] |按 TikTok Shop 品牌 ID 筛选店铺搜索结果。 |
   seller_name |string |N |shopname1 |商品所属店铺的名称。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202601/compliance/auditing/research?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_token=[\"1733419489460520284\"]&page_size=20
```

**Body**
```json
{"product_title":"mike noritama cute calico cat","product_ids":["123123","1235677","456756"],"seller_id":"1733337095719126364","category_ids":["602118"],"brand_ids":["602118"],"seller_name":"shopname1"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | ["1733419489460520284"] | 为下一页返回的不透明令牌。当该值非空时，请在下次请求的 `page_token` 中传入。 |
| ^total_count | int | 454 | 当前模式下选中的商品总数。对于按商品 ID 直接查找，这是用于查找的商品 ID 数量。对于店铺搜索，这是匹配卖家、商品标题、类目和品牌筛选条件的商品总数。 |
| ^products | []object |  | Product information |
| ^^id | string | 1729592969712207008 | TikTok Shop 生成的商品 ID。 |
| ^^title | string | mike noritama cute calico cat | 商品标题。 |
| 标题长度： |  |  |  |

* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
* BR, MX: [1, 300]
* 其他地区: [25, 255] |
   ^^country |string |FR |商品销售所在地区。
   可能的值：
* BR: 巴西
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MX: 墨西哥
* MY: 马来西亚
* PH: 菲律宾
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南 |
   ^^description |string |
   购买前请将上述详细尺码与您的测量尺寸进行比较。
* M-Size
* XL-Size

![Image](https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627)
 |HTML 格式的商品描述。 | ^^variants |[]object | |用于标识商品不同变体的 SKU（库存单位）列表。 | ^^^id |string |11111 |TikTok Shop 生成的 SKU ID。 | ^^listing_url |string |https://shop.tiktok.com/view/product/1733990243784295749?region=FR |商品详情页的 URL。 | ^^seller_name |string |Essential Shop |商品所属店铺的名称。 | ^^seller_id |string |11111 |店铺身份 ID。 | ^^main_image_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |查看图片的 URL。 | ^^brand_id |string |1111 |此商品的品牌 ID。 | ^^brand_name |string |Labor |品牌名称。 | ^^categories |[]object | |商品的类目层级。 | ^^^id |string |1111 |该商品所属类目的 ID。 | ^^^name |string |Kostum |店铺运营所在国家的类目名称。 | ^^^level |int |1 |店铺运营所在国家的类目层级。 | ^^^parent_id |string |1111 |父分类 ID。 对于根分类，父 ID 为 0 | ^^^is_leaf |bool |false |标识该分类是否为叶子分类的标志。
Note: 您只能创建或编辑属于叶子分类的商品。 |
# 响应示例
```json
{"code":0,"data":{"next_page_token":"[\\\"1733419489460520284\\\"]","total_count":454,"products":[{"id":"1729592969712207008","title":"mike noritama cute calico cat","country":"FR","description":"\u003cp\u003ePlease compare above detailed size with your measurement before purchase.\u003c/p\u003e\n\u003cul\u003e \n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" /\u003e\n","variants":[{"id":"11111"}],"listing_url":"https://shop.tiktok.com/view/product/1733990243784295749?region=FR","seller_name":"Essential Shop","seller_id":"11111","main_image_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"brand_id":"1111","brand_name":"Labor","categories":[{"id":"1111","name":"Kostum","level":1,"parent_id":"1111","is_leaf":false}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

