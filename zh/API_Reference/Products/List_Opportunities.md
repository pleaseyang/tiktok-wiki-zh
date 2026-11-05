# 列出商机

# Path: /product/202604/opportunities/query
# Method: [POST]
# 功能描述
Search and retrieve a paginated list of opportunity leads available to the authorized seller, with optional filters by type, status, category, etc and ordered by the algorithm ranking model.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | Y | 20 | Number of results per page. Max: 100. Default: 20. |
| page_token | string | N | 100 | Pagination token from previous response. Omit for first page. |
| locale | string | N | en-US | The locale for localized category names, tags, and reward information, expressed as a BCP-47 language-country code, for example `en-US`. If omitted, the primary locale for the seller's shop region is used. |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| opportunity_type | string | Y | PRODUCT | The type of opportunity. |
| Possible values: |  |  |  |  |

* `PRODUCT`: Product opportunity
* `KEYWORD`: Search keyword opportunity
* `CATEGORY`: Category opportunity |
   category_ids |[]string |N |["601310","601311"] |Filter by category IDs. Leave empty to return all leads that available to the seller. |
   create_time_ge |int |N |1775976752 |Filter opportunities created at or after this time. Provide a Unix timestamp in seconds (UTC). |
   create_time_lt |int |N |1776976752 |Filter opportunities created before this time. timestamp in seconds |
   tag_codes |[]string |N |["core_product","top_product"] |A list of tag codes used to filter the results. You can provide at most 20 values. Use lowercase tag codes. The `core_product` and `top_product` tag codes are supported only when `opportunity_type` is `PRODUCT`; their availability also depends on the seller and market configuration. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/opportunities/query?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=20&page_token=100&locale=en-US
```

**Body**
```json
{"opportunity_type":"PRODUCT","category_ids":["601310","601311"],"create_time_ge":1775976752,"create_time_lt":1776976752,"tag_codes":["core_product","top_product"]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | Paginated opportunity results. |
| ^^opportunities | []object |  | The opportunities returned on the current page. |
| ^^^id | string | 7123456789012345678 | Unique ID of the opportunity |
| ^^^title | string | title info | Opportunity title. |
| ^^^reference_images | []string | ["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/61e605ce483f4f7b9b419d510f74fd22~tplv-o3syd03w52-resize-image:400:400.image?dr=15586&t=555f072d&ps=933b5bde&shp=5563f2fb&shcp=122e87b3&idc=maliva&from=1432613627&from_p=305039283"] | Reference product images of the product to list. |
| ^^^category_id_level_1 | string | 901128 | TikTok Shop L1 category ID. |
| ^^^category_id_level_2 | string | 30122212 | TikTok Shop L2 category ID. |
| ^^^category_id_level_3 | string | 3321212 | TikTok Shop L3 category ID. |
| ^^^category_name_level_1 | string | Shoes | 分类 name of 1st level category. |
| ^^^category_name_level_2 | string | Women's Shoes | 分类 name of 2nd level category. |
| ^^^category_name_level_3 | string | Sandals & Flip Flops | 分类 name of 3rd level category. |
| ^^^is_collected | bool | false | Whether the authorized seller has saved this opportunity to their collection. |
| ^^^query_words | string | word1,word2 | Comma-separated TikTok Shop in-site search keywords associated with the opportunity. |
| ^^^opportunity_type | string | PRODUCT | 类型 of opportunity: PRODUCT（品线索）/ KEYWORD（词线索）/ CATEGORY（类目线索） |
| Empty return for a specific opportunity type indicates the business team has not enabled merchant submission for this lead type in the corresponding market. |  |  |  |
|  |  |  |  |
| ^^^brand_name | string | brand1 | The brand name for products specified by the opportunity. |
| ^^^create_time | int | 1712544000 | The opportunity creation time as a Unix timestamp in seconds (UTC). |
| ^^^expire_time | int | 1712544000 | Opportunity expiry date, second-level timestamp |
| ^^^est_market_sales_volume | string | 100k+ | Estimated market sales volume for the last 30 days, returned as an approximate bucket: `<100`, a value rounded down to a hundreds bucket ending in `00+`, a `k+` or `M+` value, or `100M+`. |
| ^^^est_market_gmv | string | 9M+ | Estimated market sales GMV in USD for the last 30 days, returned as an approximate bucket: `<100`, a value rounded down to a hundreds bucket ending in `00+`, a `k+` or `M+` value, or `100M+`. |
| ^^^search_volume | string | 3312 | TikTok Shop in-site search volume, rounded to the nearest whole number and returned as a decimal string. |
| ^^^competitor_product_count | string | 100+ | Approximate number of competing products listed in the last 30 days, returned as one of `< 10`, `< 50`, `< 100`, or `100+`. |
| ^^^video_view_pv | string | 7k+ | The cumulative short video view count of all videos associated with this product opportunity. |
| ^^^tags | string | Pencarian teratas,Pencarian trending,Persaingan rendah,Trending di TikTok,Terlaris | Comma-separated display values for the opportunity tags. Each value is localized when a translation is available; otherwise, the configured tag description or tag code is returned. |
| ^^^tag_codes | []string | ["core_product"] | Tag codes for the opportunity. The available codes depend on seller and market configuration. Examples for Latam include `core_product` and `top_product`. |
| ^^^reward_info | string | Boost shoptab visibility | Comma-separated descriptions of rewards that sellers can gain by listing products as required. Values are localized when a translation is available; otherwise, the configured reward description is returned. |
| ^^^external_product_id | string | SH1234567890 | Product ID on the reference source. |
| ^^^reference_source | string | 1 | The reference platform code, returned only when `external_product_id` is present. |
| Possible values: |  |  |  |

* `1`: SHOPEE
* `2`: AMAZON
* `3`: LOOKFANTASTIC
* `4`: WALMART
* `5`: TTS
* `6`: ASOS
* `7`: UNIVERSAL_PRODUCT
* `8`: DTCNEXUS
* `9`: TEMU
* `10`: SHOPIFY
* `11`: NEXUS_SHOPIFY
* `12`: SHEIN
* `13`: PIXEL
* `14`: SHOPIFY_NON_1P
* `15`: MIRAVIA
* `16`: RAKUTEN
* `17`: EBAY
* `18`: ONBUY
* `19`: MERCADO_LIBRE
* `20`: ALLEGRO
* `21`: BOL
* `22`: DTC |
   ^^next_page_token |string |100 |Pagination token to pass as `page_token` in the next request. This field is omitted when there are no more results. |
   ^^total_count |int |200 |Total number of matching opportunities (approximate). |

# 响应示例
```json
{"code":0,"data":{"data":{"opportunities":[{"id":"7123456789012345678","title":"title info","reference_images":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/61e605ce483f4f7b9b419d510f74fd22~tplv-o3syd03w52-resize-image:400:400.image?dr=15586\u0026t=555f072d\u0026ps=933b5bde\u0026shp=5563f2fb\u0026shcp=122e87b3\u0026idc=maliva\u0026from=1432613627\u0026from_p=305039283"],"category_id_level_1":"901128","category_id_level_2":"30122212","category_id_level_3":"3321212","category_name_level_1":"Shoes","category_name_level_2":"Women's Shoes","category_name_level_3":"Sandals \u0026 Flip Flops","is_collected":false,"query_words":"word1,word2","opportunity_type":"PRODUCT","brand_name":"brand1","create_time":1712544000,"expire_time":1712544000,"est_market_sales_volume":"100k+","est_market_gmv":"9M+","search_volume":"3312","competitor_product_count":"100+","video_view_pv":"7k+","tags":"Pencarian teratas,Pencarian trending,Persaingan rendah,Trending di TikTok,Terlaris","tag_codes":["core_product"],"reward_info":"Boost shoptab visibility","external_product_id":"SH1234567890","reference_source":"1"}],"next_page_token":"100","total_count":200}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

