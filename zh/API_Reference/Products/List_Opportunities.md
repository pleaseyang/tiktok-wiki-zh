# 列出商机

# 路径：/product/202604/opportunities/query
# 方法：[POST]
# 功能描述
搜索并检索已授权卖家可获得的商机线索分页列表，可按类型、状态、类目等进行可选筛选，并按算法排序模型排序。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | Y | 20 | 每页结果数。最大值: 100。默认值: 20。 |
| page_token | string | N | 100 | 来自上一次响应的分页令牌。请求第一页时省略。 |
| locale | string | N | en-US | 用于本地化类目名称、标签和奖励信息的 locale，以 BCP-47 语言-国家代码表示，例如 `en-US`。若省略，则使用卖家店铺所在地区的主要 locale。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| opportunity_type | string | Y | PRODUCT | 商机的类型。 |
| 可能的值： |  |  |  |  |

* `PRODUCT`: Product opportunity
* `KEYWORD`: 搜索关键词机会
* `CATEGORY`: Category opportunity |
   category_ids |[]string |N |["601310","601311"] |按类目 ID 筛选. 留空则返回卖家可用的所有线索。 |
   create_time_ge |int |N |1775976752 |筛选在此时间或之后创建的商机. 请提供以秒为单位的 Unix 时间戳 (UTC)。 |
   create_time_lt |int |N |1776976752 |筛选在此时间之前创建的机会。时间戳，单位为秒 |
   tag_codes |[]string |N |["core_product","top_product"] |用于筛选结果的标签代码列表。最多可提供 20 个值。请使用小写标签代码。`core_product` 和 `top_product` 标签代码仅在 `opportunity_type` 为 `PRODUCT` 时受支持；其可用性还取决于卖家和市场配置。 |

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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | 分页的商机结果。 |
| ^^opportunities | []object |  | 当前页返回的商机。 |
| ^^^id | string | 7123456789012345678 | 机会的唯一 ID |
| ^^^title | string | title info | Opportunity title. |
| ^^^reference_images | []string | ["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/61e605ce483f4f7b9b419d510f74fd22~tplv-o3syd03w52-resize-image:400:400.image?dr=15586&t=555f072d&ps=933b5bde&shp=5563f2fb&shcp=122e87b3&idc=maliva&from=1432613627&from_p=305039283"] | 待上架商品的参考商品图片。 |
| ^^^category_id_level_1 | string | 901128 | TikTok Shop L1 类目 ID。 |
| ^^^category_id_level_2 | string | 30122212 | TikTok Shop L2 类目 ID。 |
| ^^^category_id_level_3 | string | 3321212 | TikTok Shop L3 类目 ID。 |
| ^^^category_name_level_1 | string | Shoes | 分类 name of 1st level category。 |
| ^^^category_name_level_2 | string | Women's Shoes | 分类 name of 2nd level category。 |
| ^^^category_name_level_3 | string | 凉鞋 & 人字拖 | 分类 name of 3rd level category。 |
| ^^^is_collected | bool | false | 已授权的卖家是否已将该商机保存至其收藏。 |
| ^^^query_words | string | word1,word2 | 与商机关联的 TikTok Shop 站内搜索关键词，以逗号分隔。 |
| ^^^opportunity_type | string | PRODUCT | 类型 of opportunity: PRODUCT（品线索）/ KEYWORD（词线索）/ CATEGORY（类目线索） |
| 若某一商机类型返回为空，表示业务团队尚未在相应市场为该线索类型开放卖家提报。 |  |  |  |
|  |  |  |  |
| ^^^brand_name | string | brand1 | 商机指定商品所需的品牌名称。 |
| ^^^create_time | int | 1712544000 | 机会创建时间，以秒为单位的 Unix 时间戳 (UTC)。 |
| ^^^expire_time | int | 1712544000 | 机会到期日期，秒级时间戳 |
| ^^^est_market_sales_volume | string | 100k+ | 最近 30 天的预估市场销量，以近似区间返回：`<100`、向下取整到以 `00+` 结尾的百位区间、`k+` 或 `M+` 取值，或 `100M+`。 |
| ^^^est_market_gmv | string | 9M+ | 最近 30 天以 USD 计的预估市场销售 GMV，以近似区间返回：`<100`、向下取整到以 `00+` 结尾的百位区间、`k+` 或 `M+` 取值，或 `100M+`。 |
| ^^^search_volume | string | 3312 | TikTok Shop 站内搜索量，四舍五入为最接近的整数并以十进制字符串返回。 |
| ^^^competitor_product_count | string | 100+ | 过去 30 天内上架的竞品数量的近似值，以 `< 10`、`< 50`、`< 100` 或 `100+` 之一返回。 |
| ^^^video_view_pv | string | 7k+ | 与该商品机会关联的所有短视频的累计观看次数。 |
| ^^^tags | string | Pencarian teratas,Pencarian trending,Persaingan rendah,Trending di TikTok,Terlaris | 机会标签的展示值，以逗号分隔。每个值在有可用翻译时进行本地化；否则返回配置的标签描述或标签代码。 |
| ^^^tag_codes | []string | ["core_product"] | 该商机的标签代码。可用代码取决于卖家和市场配置。拉美地区的示例包括 `core_product` 和 `top_product`。 |
| ^^^reward_info | string | Boost shoptab visibility | 卖家按要求上架商品可获得的奖励描述，以逗号分隔。取值在有可用翻译时进行本地化；否则返回配置的奖励描述。 |
| ^^^external_product_id | string | SH1234567890 | 参考来源上的商品 ID。 |
| ^^^reference_source | string | 1 | 参考平台代码，仅当 `external_product_id` 存在时返回。 |
| 可能的值： |  |  |  |

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
   ^^next_page_token |string |100 |在下一个请求中作为 `page_token` 传入的分页令牌。当没有更多结果时，此字段将被省略。 |
   ^^total_count |int |200 |匹配的机会总数 (近似值)。 |

# 响应示例
```json
{"code":0,"data":{"data":{"opportunities":[{"id":"7123456789012345678","title":"title info","reference_images":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/61e605ce483f4f7b9b419d510f74fd22~tplv-o3syd03w52-resize-image:400:400.image?dr=15586\u0026t=555f072d\u0026ps=933b5bde\u0026shp=5563f2fb\u0026shcp=122e87b3\u0026idc=maliva\u0026from=1432613627\u0026from_p=305039283"],"category_id_level_1":"901128","category_id_level_2":"30122212","category_id_level_3":"3321212","category_name_level_1":"Shoes","category_name_level_2":"Women's Shoes","category_name_level_3":"Sandals \u0026 Flip Flops","is_collected":false,"query_words":"word1,word2","opportunity_type":"PRODUCT","brand_name":"brand1","create_time":1712544000,"expire_time":1712544000,"est_market_sales_volume":"100k+","est_market_gmv":"9M+","search_volume":"3312","competitor_product_count":"100+","video_view_pv":"7k+","tags":"Pencarian teratas,Pencarian trending,Persaingan rendah,Trending di TikTok,Terlaris","tag_codes":["core_product"],"reward_info":"Boost shoptab visibility","external_product_id":"SH1234567890","reference_source":"1"}],"next_page_token":"100","total_count":200}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

