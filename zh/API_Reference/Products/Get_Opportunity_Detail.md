# 获取商机详情

# 路径：/product/202604/opportunities/{opportunity_id}
# 方法：[GET]
# 功能描述
按 ID 获取单个商机线索的完整详情，包括市场趋势数据、竞争程度和推荐操作。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| opportunity_id | string | Y | 7123456789012345678 | TikTok Shop 生成的机会线索的唯一 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| locale | string | N | en-US | 用于本地化商机内容的语言区域，按 BCP 47 以 `{language_code}-{COUNTRY_CODE}` 格式表示。如果省略，接口将使用已认证店铺所在地区配置的第一个语言区域。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/opportunities/7123456789012345678?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^opportunity | object |  | 详细的商机信息，包括基本信息、市场与内容数据、上架条件以及推荐操作。 |
| ^^id | string | 7123456789012345678 | 机会的唯一 ID |
| ^^action_type | string | LIST_SAME | 建议的操作。 |
| 可能的值： |  |  |  |

* LIST_SAME: 上架相同商品。
* LIST_SIMILAR: 上架相似商品。 |
   ^^listing_criteria |object | |与商机线索匹配的商品的条件。 |
   ^^^product_brand |string |brand1 |Requirement for product brand. |
   ^^^product_category |string |Phones & Electronics > Gaming & Consoles > Console Accessories |Requirement for product category. |
   ^^^product_status |string |LIVE |Requirement for product status : LIVE / DRAFT |
   ^^^keywords |string |word1,word2 |必须包含在商品标题、属性、描述或其他适用内容中的关键词列表，以逗号分隔。 |
   ^^content_data |object | |过去 30 天的相关数据。 |
   ^^^video_view_pv |string |7k+ |与该商品机会关联的所有短视频的累计观看次数。 |
   ^^^shoppable_video_search_pv |string |336k+ |过去 30 天与该商品机会关联的带货短视频的搜索页面浏览量，以近似区间返回: `<100`、向下取整的百位值（如 `300+`）、向下取整的千位值（如 `12k+`）、向下取整的百万位值（如 `1M+`）或 `100M+`。 |
   ^^^trending_hashtag |string |tag1,tag2 |商品相关视频中排名第一的视频话题标签，按观看次数排序。 |
   ^^^top_shoppable_video_links |[]string |["https://www.tiktok.com/@/video/v15044gf0000d4l7p57og65m3s0tqfa0","https://www.tiktok.com/@/video/v15044gf0000d306lrnog65h1a6283ug"] |与该商品相关、按观看次数排序的前 10 个带货短视频的链接。 |
   ^^market_data |object | |过去 30 天的相关数据。 |
   ^^^est_market_sales_volume |string |100k+ |过去 30 天的预估市场销量，以近似区间返回: `<100`、向下取整至百位且以 `00+` 结尾的值、`k+` 或 `M+` 值，或 `100M+`。 |
   ^^^est_market_gmv |string |9M+ |过去 30 天以 USD 计的预估市场销售 GMV，以近似区间返回: `<100`、向下取整至百位且以 `00+` 结尾的值、`k+` 或 `M+` 值，或 `100M+`。 |
   ^^^market_buzz |string |HOT |Popularity level of the product: HOT / HIGH / MEDIUM |
   ^^^search_volume |string |100000 |TikTok Shop 站内搜索量，四舍五入为整数并以十进制字符串返回。 |
   ^^^search_keyword |string |holiday |与商机关联的 TikTok Shop 站内搜索关键词，以逗号分隔。 |
   ^^^competitor_product_count |string |100+ |过去 30 天上架的竞品商品近似数量，返回值为 `< 10`、`< 50`、`< 100` 或 `100+` 之一。 |
   ^^^competitor_seller_count |string |35 |当前有商品在售的竞品卖家数量。 |
   ^^basic_info |object | |商机的详细信息。 |
   ^^^opportunity_type |string |PRODUCT |商机类型。
   可能的值：
* PRODUCT: 商品商机。
* KEYWORD: 关键词商机。
* CATEGORY: 类目商机。 |
   ^^^status |string |ACTIVE |Opportunity status: ACTIVE / EXPIRED / FULFILLED(已提报) |
   ^^^create_time |int |1775973876 |商机创建时间，以秒为单位的 Unix 时间戳 (UTC)。 |
   ^^^expire_time |int |1775973876 |商机到期日期，秒级时间戳 |
   ^^^title |string |title |商机标题。 |
   ^^^category_id_level_1 |string |901128 |TikTok Shop L1 类目 ID。 |
   ^^^category_id_level_2 |string |30122212 |TikTok Shop L2 类目 ID。 |
   ^^^category_id_level_3 |string |40122212 |TikTok Shop L3 类目 ID。 |
   ^^^category_name_level_1 |string |Shoes |一级类目的类目名称。 |
   ^^^category_name_level_2 |string |Women's Shoes |二级类目的类目名称。 |
   ^^^category_name_level_3 |string |Sandals & Flip Flops |三级类目的类目名称。 |
   ^^^reference_price |string |$36.300 - $38.500 |待上架商品的参考价格，使用适用的货币符号并保留三位小数格式。如果两个价格边界都可用，则以区间形式返回该值；如果仅一个可用，则返回单个价格；如果都不可用，则返回空字符串。 |
   ^^^reference_images |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/61e605ce483f4f7b9b419d510f74fd22~tplv-o3syd03w52-resize-image:400:400.image?dr=15586&t=555f072d&ps=933b5bde&shp=5563f2fb&shcp=122e87b3&idc=maliva&from=1432613627&from_p=305039283"] |待上架商品的参考商品图片。 |
   ^^^brand_info |string |some brand info |该商机指定的商品品牌要求。 |
   ^^^reward_info |string |Boost shoptab visibility |卖家按要求上架商品可获得的奖励描述，以逗号分隔。有可用翻译时取值会本地化；否则返回配置的奖励描述。 |
   ^^^recom_info |string |Trending, but out of stock |该商机的推荐原因。 |
   ^^^tags |string |Pencarian teratas,Pencarian trending,Persaingan rendah,Trending di TikTok,Terlaris |商机标签的展示值，以逗号分隔。有可用翻译时每个取值会本地化；否则返回配置的标签描述或标签代码。 |
   ^^^tag_codes |[]string |["core_product"] |机会的标签代码。可用代码取决于卖家和市场配置。Latam 的示例包括 `core_product` 和 `top_product`。 |
   ^^^external_product_id |string |SH1234567890 |参考来源上的商品 ID。 |
   ^^^reference_source |string |1 |参考平台代码，仅当 `external_product_id` 存在时返回。
   可能的值：
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

# 响应示例
```json
{"code":0,"data":{"opportunity":{"id":"7123456789012345678","action_type":"LIST_SAME","listing_criteria":{"product_brand":"brand1","product_category":"Phones \u0026 Electronics \u003e Gaming \u0026 Consoles \u003e Console Accessories","product_status":"LIVE","keywords":"word1,word2"},"content_data":{"video_view_pv":"7k+","shoppable_video_search_pv":"336k+","trending_hashtag":"tag1,tag2","top_shoppable_video_links":["https://www.tiktok.com/@/video/v15044gf0000d4l7p57og65m3s0tqfa0","https://www.tiktok.com/@/video/v15044gf0000d306lrnog65h1a6283ug"]},"market_data":{"est_market_sales_volume":"100k+","est_market_gmv":"9M+","market_buzz":"HOT","search_volume":"100000","search_keyword":"holiday","competitor_product_count":"100+","competitor_seller_count":"35"},"basic_info":{"opportunity_type":"PRODUCT","status":"ACTIVE","create_time":1775973876,"expire_time":1775973876,"title":"title","category_id_level_1":"901128","category_id_level_2":"30122212","category_id_level_3":"40122212","category_name_level_1":"Shoes","category_name_level_2":"Women's Shoes","category_name_level_3":"Sandals \u0026 Flip Flops","reference_price":"$36.300 - $38.500","reference_images":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/61e605ce483f4f7b9b419d510f74fd22~tplv-o3syd03w52-resize-image:400:400.image?dr=15586\u0026t=555f072d\u0026ps=933b5bde\u0026shp=5563f2fb\u0026shcp=122e87b3\u0026idc=maliva\u0026from=1432613627\u0026from_p=305039283"],"brand_info":"some brand info","reward_info":"Boost shoptab visibility","recom_info":"Trending, but out of stock","tags":"Pencarian teratas,Pencarian trending,Persaingan rendah,Trending di TikTok,Terlaris","tag_codes":["core_product"],"external_product_id":"SH1234567890","reference_source":"1"}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

