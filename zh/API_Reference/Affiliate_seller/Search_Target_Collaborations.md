# 搜索 Target Collaboration

# 路径：/affiliate_seller/202508/target_collaborations/search
# 方法：[POST]
# 功能描述
搜索卖家的 target collaboration。响应包括 collaboration 详情、达人信息和佣金设置。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_size | int | N | 20 | "page_size" 的取值必须为 20, 50 或 100。 |
| page_token | string | N | b2Zmc2V0PTAK | 指定从何处继续搜索的分页令牌。首次请求时省略此参数或将其留空。对于后续页面，传入上一次响应返回的 `next_page_token`，并复用相同的请求体筛选条件和 `page_size`。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| creator_accept_status | string | N | ACCEPT | 按受邀达人的接受状态筛选定向协作。 |
| Allowed values: |  |  |  |  |

* ACCEPT：达人已将商品添加到其橱窗。
* ALL：不按达人是否已将商品添加到橱窗进行筛选。
   默认值：ALL。 |
   free_sample_setting |string |N |WITH_FREE_SAMPLE |按 target collaboration 的免费 sample 设置筛选。
   您可以基于以下条件查询：
* "WITH_FREE_SAMPLE"
* "ALL"
   默认情况下，target collaboration 按 "ALL" 设置搜索。 |
   search_param |object |N | |Target collaboration 的搜索条件。提供此对象时，需同时提供 keyword_type 和 keyword。 |
   ^keyword_type |string |Y |TARGET_COLLABORATION_NAME |keyword 中提供的值类型。
   可能的值：
* PRODUCT_ID：搜索特定商品 ID。
* PRODUCT_NAME：按商品名称模糊搜索。
* TARGET_COLLABORATION_ID：搜索特定 target collaboration ID。
* TARGET_COLLABORATION_NAME：按 target collaboration 名称模糊搜索。 |
   ^keyword |string |Y |test |要搜索的值，根据 keyword_type 解释。 |
   creator_user_open_id |string |N |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |达人的 TikTok User Open ID。提供此字段以筛选指定达人的 target collaboration。 [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
   collaboration_status |string |Y |ONGOING |按 target collaboration 的状态筛选。
   您可以基于以下条件查询：
* ONGOING：如果使用 ONGOING 搜索，返回的 target collaboration 的剩余有效期将大于 7 天。
* EXPIRING：如果使用 EXPIRING 搜索，返回的 target collaboration 的剩余有效期将小于 7 天。
* VALID：如果使用 VALID 搜索，所有返回的 target collaboration 均有效。
* CANCELING：如果使用 CANCELING 搜索，所有返回的 target collaboration 均处于取消过程中。
* COMPLETED：如果使用 COMPLETED 搜索，所有返回的 target collaboration 均处于已完成状态，包括已过期和已取消的。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/target_collaborations/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=20&page_token=b2Zmc2V0PTAK
```

**Body**
```json
{"creator_accept_status":"ACCEPT","free_sample_setting":"WITH_FREE_SAMPLE","search_param":{"keyword_type":"TARGET_COLLABORATION_NAME","keyword":"test"},"creator_user_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","collaboration_status":"ONGOING"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^total_count | int | 100 | 所有页面中符合请求的 target collaboration 总数。 |
| ^next_page_token | string | b2Zmc2V0PTIw | 下一页请求的游标。 |
| ^target_collaborations | []object |  | 达人可以在 TikTok 电商中心的定向邀请中查看的 target collaboration 基本信息。 |
| ^^id | string | 789078671231123124 | 定向协作 ID。 |
| ^^name | string | target_collaboration | 定向协作名称。 |
| ^^message | string | test | 卖家向达人发送的关于卖家介绍以及为何期待合作的消息。 |
| ^^start_time | int | 1715654330 | Target collaboration 开始的 Unix 时间戳（秒）。 |
| ^^end_time | int | 1715654330 | Target collaboration 结束的 Unix 时间戳（秒）。 |
| ^^create_time | int | 1715654330 | Target collaboration 创建的 Unix 时间戳（秒）。 |
| ^^update_time | int | 1715654330 | Target collaboration 最后更新的 Unix 时间戳（秒）。 |
| ^^creator_inivited_count | int | 10 | 定向协作中受邀达人的数量。 |
| ^^showcase_creator_count | int | 2 | Target collaboration 中至少将一个商品展示到橱窗的达人数量。 |
| ^^content_creator_count | int | 1 | 发布了包含定向协作商品的内容的达人数量。 |
| ^^product_count | int | 30 | 定向协作中添加的商品数量。 |
| ^^free_sample_rule | object |  | 卖家在定向协作中设置的免费样品规则。 |
| ^^^has_free_sample | bool | true | 如果为 true, 将向受邀参与定向协作的达人提供免费样品。 |
| ^^^is_sample_approval_exempt | bool | true | 如果为 true, 受邀参加定向协作的达人无需卖家审核，将自动获批获得免费样品。 |
| 请注意，如果 has_free_sample=false, 此字段将不生效。 |  |  |  |
| ^^type | string | STANDARD | 定向协作的类型。 |
| Field values: |  |  |  |

* STANDARD：定向协作由卖家手动选择商品和达人创建。
* TOP_CREATOR_PROGRAM：卖家加入 TikTok Shop Top 达人 Program 后创建的定向协作，只需提交商品。 |

# 响应示例
```json
{"code":0,"data":{"total_count":100,"next_page_token":"b2Zmc2V0PTIw","target_collaborations":[{"id":"789078671231123124","name":"target_collaboration","message":"test","start_time":1715654330,"end_time":1715654330,"create_time":1715654330,"update_time":1715654330,"creator_inivited_count":10,"showcase_creator_count":2,"content_creator_count":1,"product_count":30,"free_sample_rule":{"has_free_sample":true,"is_sample_approval_exempt":true},"type":"STANDARD"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

