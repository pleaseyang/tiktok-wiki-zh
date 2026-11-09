# 查询 Target Collaboration 详情

# 路径：/affiliate_seller/202508/target_collaborations/{target_collaboration_id}
# 方法：[GET]
# 功能描述
此 API 用于查询 target collaboration 的详细信息，包括达人信息、商品信息和佣金设置。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| target_collaboration_id | string | Y | 1234 | Target collaboration 的 ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202508/target_collaborations/1234?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^target_collaboration | object |  | Target Collaboration 详情。 |
| ^^id | string | 789078671231123124 | 定向协作 ID。 |
| ^^name | string | target_collaboration | Target collaboration 名称。 |
| ^^message | string | test | 卖家向达人发送的关于卖家介绍及合作期望的消息。 |
| ^^seller_contact_info | object |  | Target collaboration 中卖家的联系信息。 |
| ^^^email | string | test@bytedance.com | 卖家的电子邮件联系信息。 |
| ^^^phone_number | string | 1234 | 卖家的电话号码。 |
| ^^^whatsapp | string | aaaa | 卖家注册 WhatsApp 使用的电话号码。 |
| ^^^telegram | string | 1234 | 卖家的 Telegram 用户名或电话号码。 |
| ^^^line | string | asd | 卖家注册 Line 应用使用的电话号码。 |
| ^^start_time | int | 1715654330 | Target collaboration 的开始时间，以秒为单位的 Unix 时间戳。 |
| ^^end_time | int | 1715654330 | Target collaboration 的结束时间，以秒为单位的 Unix 时间戳。 |
| ^^update_time | int | 1715654330 | Target collaboration 的更新时间，以秒为单位的 Unix 时间戳。 |
| ^^creator_invited_count | int | 10 | Target collaboration 中邀请的达人数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^showcase_creator_count | int | 2 | 此字段表示从 target collaboration 将商品添加到橱窗的达人数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^content_creator_count | int | 1 | 发布包含 target collaboration 商品内容的达人数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^product_count | int | 30 | Target collaboration 中添加的商品数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^free_sample_rule | object |  | 卖家在 in the target collaboration 中设置的免费 sample 规则。 |
| ^^^has_free_sample | bool | true | 如果为 true，则向邀请到 target collaboration 组的达人提供免费 sample。 |
| ^^^is_sample_approval_exempt | bool | true | 如果为 true，邀请到 target collaboration 的达人将免除卖家审核，并自动获得免费 sample。 |
| 请注意，如果 has_free_sample=false，则此字段不生效。 |  |  |  |
| ^^products | []object |  | Target collaboration 中的商品信息。 |
| ^^^id | string | 789078671231312312 | 商品标识符。 |
| ^^^main_image_url | string | https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a/12345~c5_168x168.webp?lk3s=a5d48078&nonce=49646&refresh_token=b53364a3a1947c4ac7a0c4bea62e31ea&x-expires=1727175600&x-signature=ASPIxFDNDkN1cknLEItlyC%2Bcfbw%3D&shp=a5d48078&shcp=39dffb78 | 商品图片 URL。 |
|  |  |  |  |
| ^^^title | string | Christmas Gift | 商品名称。 |
| ^^^original_price | object |  | 商品的原始价格。 |
| ^^^^currency | string | USD | 币种代码。 |
| ^^^^minimum_amount | string | 12.21 | 商品所有 SKU 的最低原始价格。 |
| ^^^^maximum_amount | string | 100.00 | 商品所有 SKU 的最高原始价格。 |
| ^^^commission | object |  | 佣金信息。 |
| ^^^^rate | int | 3000 | 佣金比率，以百分之一为单位。例如，3587 表示 35.87% 的佣金比率。此值最小为 1000。此值范围为 [100, 8000]。 |
| ^^^^effective_time | string | 1715654330 | 佣金生效时间，以字符串形式的秒级 Unix 时间戳表示。 |
| ^^^^currency | string | USD | 币种代码。 |
| ^^^^minimum_amount | string | 34.3 | 此商品所有 SKU 的最低预估佣金金额。 |
| ^^^^maximum_amount | string | 55.7 | 此商品所有 SKU 的最高预估佣金金额。 |
| ^^^^shop_ads_commission_rate | int | 100 | 该佣金率仅适用于广告产生的订单。如果达人的视频被用作广告而未设置此费率，产生的订单将改为按以下之一获得佣金： |

* 您在 open collaboration 中配置的 Shop Ads 佣金，或
* 此邀请中定义的标准佣金。
   佣金比率以万分之一为增量指定。
   例如，1000 代表 0.1 或 10%。 |
   ^^^status |string |LIVE |商品状态。
   字段值：
* LIVE：商品正常在售时，返回 LIVE 状态
* OUT_OF_STOCK：当商品对消费者缺货时，返回 OUT_OF_STOCK 状态
* SELLER_DEACTIVATE：当商品被卖家停用时，返回 SELLER_DEACTIVATE 状态
* PLATFORM_DEACTIVATE：当商品被平台停用或不可售时，返回 PLATFORM_DEACTIVATE 状态
* GNE_REJECT: 当商品被管控或定向协作被解除时，返回 GNE_REJECT 状态
* DELETE：商品被删除时，返回 DELETE 状态
* OTHER：商品处于不可售状态（如草稿、冻结、审核中等）时，返回 OTHER 状态 |
   ^^^commission_effective_status |string |EFFECTIVE_ALL |此商品的 target collaboration 佣金在各达人中的有效性。
   字段值：
* EFFECTIVE_ALL: 佣金对所有达人生效。
* EFFECTIVE_PARTIALLY: 佣金对部分达人生效。
* EFFECTIVE_NONE: 佣金对任何达人都不生效。
   通常，商品的佣金对所有达人相同。
   如果卖家参与 TOP_CREATOR_PROGRAM，且 TOP_CREATOR_PROGRAM 包含当前商品和部分达人，则佣金比率将基于 TOP_CREATOR_PROGRAM。 当前 Target Collaboration 下的商品佣金将对部分达人生效，对应 EFFECTIVE_PARTIALLY 状态。 |
   ^^^collaboration_status |string |NORMAL |商品在当前 target cooperation 中的状态。
   字段值：
* NORMAL: 当前定向协作中商品状态正常。
* DELETING：商品在当前定向协作中的状态为删除中。处于 DELETING 状态的商品将结束其延迟生效状态，并于次日 00:00 转入 DELETED 状态。
* DELETED: 当前定向协作中商品状态为已删除。 |
   ^^creators |[]object | |Target collaboration 中的达人信息。 |
   ^^^username |string |123456 |TikTok 用户名。 |
   ^^^nickname |string |123456 |TikTok 昵称。 |
   ^^^avatar |object | |与 TikTok 达人个人资料头像关联的数据。 |
   ^^^^url |string |https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078&x-expires=1712988000&x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D |TikTok 达人头像图片文件的 URL。 |
   ^^^selection_region |string |US |达人有资格在橱窗、视频和直播中推广商品的地区。 |
   ^^^showcase_product_count |int |2 |此字段表示达人从 target collaboration 添加到橱窗的商品数量。
   计数包括 NORMAL 和 DELETING 状态。 |
   ^^^content_product_count |int |1 |此字段表示达人从 target collaboration 发布视频或直播的商品数量。
   计数包括 NORMAL 和 DELETING 状态。 |
   ^^^collaboration_status |string |NORMAL |达人在当前定向协作中的状态。
   字段值：
* NORMAL: 当前定向协作中达人状态正常。
* DELETING: 达人在当前定向协作中的状态为删除中。处于 DELETING 状态的达人商品推广关系将结束延迟生效状态，并于次日 00:00 转为 DELETED 状态。
* DELETED: 当前定向协作中达人状态为已删除。 |
   ^^^product_effective_status |string |EFFECTIVE_ALL |Target collaboration 的商品佣金对该达人的有效性。
   字段值：
* EFFECTIVE_ALL: 佣金对该达人在定向协作中的所有商品生效。
* EFFECTIVE_PARTIALLY: 该佣金在定向协作中对此达人的部分商品生效。
* EFFECTIVE_NONE: 佣金对该达人在定向协作中的任何商品均不生效。
   通常，定向协作下所有商品的佣金率均生效。
   如果卖家参与了 TOP_CREATOR_PROGRAM，且 TOP_CREATOR_PROGRAM 包含当前达人和部分商品，则佣金率将基于 TOP_CREATOR_PROGRAM。当前定向协作下这些商品的佣金对该达人仅部分生效，对应 EFFECTIVE_PARTIALLY 状态。 |
   ^^^creator_open_id |string |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
   ^^type |string |STANDARD |Target collaboration 的类型。
   字段值：
* STANDARD：定向协作由卖家手动选择商品和达人创建。
* TOP_CREATOR_PROGRAM：卖家加入 TikTok Shop Top 达人 Program 后创建的定向协作，只需提交商品。 |

# 响应示例
```json
{"code":0,"data":{"target_collaboration":{"id":"789078671231123124","name":"target_collaboration","message":"test","seller_contact_info":{"email":"test@bytedance.com","phone_number":"1234","whatsapp":"aaaa","telegram":"1234","line":"asd"},"start_time":1715654330,"end_time":1715654330,"update_time":1715654330,"creator_invited_count":10,"showcase_creator_count":2,"content_creator_count":1,"product_count":30,"free_sample_rule":{"has_free_sample":true,"is_sample_approval_exempt":true},"products":[{"id":"789078671231312312","main_image_url":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a/12345~c5_168x168.webp?lk3s=a5d48078\u0026nonce=49646\u0026refresh_token=b53364a3a1947c4ac7a0c4bea62e31ea\u0026x-expires=1727175600\u0026x-signature=ASPIxFDNDkN1cknLEItlyC%2Bcfbw%3D\u0026shp=a5d48078\u0026shcp=39dffb78","title":"Christmas Gift","original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"},"commission":{"rate":3000,"effective_time":"1715654330","currency":"USD","minimum_amount":"34.3","maximum_amount":"55.7","shop_ads_commission_rate":100},"status":"LIVE","commission_effective_status":"EFFECTIVE_ALL","collaboration_status":"NORMAL"}],"creators":[{"username":"123456","nickname":"123456","avatar":{"url":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078\u0026x-expires=1712988000\u0026x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D"},"selection_region":"US","showcase_product_count":2,"content_product_count":1,"collaboration_status":"NORMAL","product_effective_status":"EFFECTIVE_ALL","creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"}],"type":"STANDARD"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 50001700 | seller cannot access this target collaboration |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

