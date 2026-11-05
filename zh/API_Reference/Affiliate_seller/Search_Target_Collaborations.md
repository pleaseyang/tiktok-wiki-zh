# 搜索 Target Collaboration

# Path: /affiliate_seller/202508/target_collaborations/search
# Method: [POST]
# 功能描述
搜索商家的 target collaboration。响应包括 collaboration 详情、creator 信息和 commission 设置。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_size | int | N | 20 | The value of "page_size" must be 20, 50 or 100. |
| page_token | string | N | b2Zmc2V0PTAK | Pagination token that specifies where to continue the search. Omit this parameter or leave it empty in the first request. For subsequent pages, pass the `next_page_token` returned by the previous response and reuse the same request-body filters and `page_size`. |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| creator_accept_status | string | N | ACCEPT | Filter target collaborations by the acceptance status of invited creators. |
| Allowed values: |  |  |  |  |

* ACCEPT：Creator 已将产品添加到其 showcase。
* ALL：不按 creator 是否已将产品添加到 showcase 进行筛选。
   默认值：ALL。 |
   free_sample_setting |string |N |WITH_FREE_SAMPLE |按 target collaboration 的免费 sample 设置筛选。
   您可以基于以下条件查询：
* "WITH_FREE_SAMPLE"
* "ALL"
   默认情况下，target collaboration 按 "ALL" 设置搜索。 |
   search_param |object |N | |Target collaboration 的搜索条件。提供此对象时，需同时提供 keyword_type 和 keyword。 |
   ^keyword_type |string |Y |TARGET_COLLABORATION_NAME |keyword 中提供的值类型。
   Possible values:
* PRODUCT_ID：搜索特定产品 ID。
* PRODUCT_NAME：按产品名称模糊搜索。
* TARGET_COLLABORATION_ID：搜索特定 target collaboration ID。
* TARGET_COLLABORATION_NAME：按 target collaboration 名称模糊搜索。 |
   ^keyword |string |Y |test |要搜索的值，根据 keyword_type 解释。 |
   creator_user_open_id |string |N |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |Creator 的 TikTok User Open ID。提供此字段以筛选指定 creator 的 target collaboration。 [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
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
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^total_count | int | 100 | 所有页面中符合请求的 target collaboration 总数。 |
| ^next_page_token | string | b2Zmc2V0PTIw | 下一页请求的游标。 |
| ^target_collaborations | []object |  | Creator 可以在 TikTok 电商中心的定向邀请中查看的 target collaboration 基本信息。 |
| ^^id | string | 789078671231123124 | Target collaboration ID. |
| ^^name | string | target_collaboration | Target collaboration name. |
| ^^message | string | test | Message seller has sent to creators about seller's introduction and why excited to collaborate. |
| ^^start_time | int | 1715654330 | Target collaboration 开始的 Unix 时间戳（秒）。 |
| ^^end_time | int | 1715654330 | Target collaboration 结束的 Unix 时间戳（秒）。 |
| ^^create_time | int | 1715654330 | Target collaboration 创建的 Unix 时间戳（秒）。 |
| ^^update_time | int | 1715654330 | Target collaboration 最后更新的 Unix 时间戳（秒）。 |
| ^^creator_inivited_count | int | 10 | The count of creators invited in the target collaboration. |
| ^^showcase_creator_count | int | 2 | Target collaboration 中至少将一个产品展示到 showcase 的 creator 数量。 |
| ^^content_creator_count | int | 1 | The number of creators who posted content featuring products from target collaboration. |
| ^^product_count | int | 30 | The count of products added in the target collaboration. |
| ^^free_sample_rule | object |  | The free sample rules set by the seller in the target collaboration. |
| ^^^has_free_sample | bool | true | If true, free samples are provided to creators invited to the target collaboration. |
| ^^^is_sample_approval_exempt | bool | true | If true, creators invited to the target collaboration are exempt from seller review and will automatically be approved for a free sample. |
| Note that if has_free_sample=false, this field will not take effect. |  |  |  |
| ^^type | string | STANDARD | The type of target collaboration. |
| Field values: |  |  |  |

* STANDARD: The target collaboration is created by sellers manually selecting products and creators.
* TOP_CREATOR_PROGRAM: The target collaboration created by seller joining TikTok Shop Top Creator Program, requiring only product submission. |

# 响应示例
```json
{"code":0,"data":{"total_count":100,"next_page_token":"b2Zmc2V0PTIw","target_collaborations":[{"id":"789078671231123124","name":"target_collaboration","message":"test","start_time":1715654330,"end_time":1715654330,"create_time":1715654330,"update_time":1715654330,"creator_inivited_count":10,"showcase_creator_count":2,"content_creator_count":1,"product_count":30,"free_sample_rule":{"has_free_sample":true,"is_sample_approval_exempt":true},"type":"STANDARD"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

