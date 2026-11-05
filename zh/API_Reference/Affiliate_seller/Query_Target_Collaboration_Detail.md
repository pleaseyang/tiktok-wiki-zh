# 查询 Target Collaboration 详情

# Path: /affiliate_seller/202508/target_collaborations/{target_collaboration_id}
# Method: [GET]
# 功能描述
此 API 用于查询 target collaboration 的详细信息，包括 creator 信息、产品信息和 commission 设置。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| target_collaboration_id | string | Y | 1234 | Target collaboration 的 ID |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
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
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^target_collaboration | object |  | Target Collaboration 详情。 |
| ^^id | string | 789078671231123124 | Target collaboration ID。 |
| ^^name | string | target_collaboration | Target collaboration 名称。 |
| ^^message | string | test | 卖家向 creator 发送的关于卖家介绍及合作期望的消息。 |
| ^^seller_contact_info | object |  | Target collaboration 中卖家的联系信息。 |
| ^^^email | string | test@bytedance.com | 卖家的电子邮件联系信息。 |
| ^^^phone_number | string | 1234 | 卖家的电话号码。 |
| ^^^whatsapp | string | aaaa | 卖家注册 WhatsApp 使用的电话号码。 |
| ^^^telegram | string | 1234 | 卖家的 Telegram 用户名或电话号码。 |
| ^^^line | string | asd | 卖家注册 Line 应用使用的电话号码。 |
| ^^start_time | int | 1715654330 | Target collaboration 的开始时间，以秒为单位的 Unix 时间戳。 |
| ^^end_time | int | 1715654330 | Target collaboration 的结束时间，以秒为单位的 Unix 时间戳。 |
| ^^update_time | int | 1715654330 | Target collaboration 的更新时间，以秒为单位的 Unix 时间戳。 |
| ^^creator_invited_count | int | 10 | Target collaboration 中邀请的 creator 数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^showcase_creator_count | int | 2 | 此字段表示从 target collaboration 将产品添加到 showcase 的 creator 数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^content_creator_count | int | 1 | 发布包含 target collaboration 产品内容的 creator 数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^product_count | int | 30 | Target collaboration 中添加的产品数量。 |
| 计数仅包括 NORMAL 状态。 |  |  |  |
| ^^free_sample_rule | object |  | 卖家在 in the target collaboration 中设置的免费 sample 规则。 |
| ^^^has_free_sample | bool | true | 如果为 true，则向邀请到 target collaboration 组的 creator 提供免费 sample。 |
| ^^^is_sample_approval_exempt | bool | true | 如果为 true，邀请到 target collaboration 的 creator 将免除卖家审核，并自动获得免费 sample。 |
| 请注意，如果 has_free_sample=false，则此字段不生效。 |  |  |  |
| ^^products | []object |  | Target collaboration 中的产品信息。 |
| ^^^id | string | 789078671231312312 | 产品标识符。 |
| ^^^main_image_url | string | https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a/12345~c5_168x168.webp?lk3s=a5d48078&nonce=49646&refresh_token=b53364a3a1947c4ac7a0c4bea62e31ea&x-expires=1727175600&x-signature=ASPIxFDNDkN1cknLEItlyC%2Bcfbw%3D&shp=a5d48078&shcp=39dffb78 | 产品图片 URL。 |
|  |  |  |  |
| ^^^title | string | Christmas Gift | 产品名称。 |
| ^^^original_price | object |  | 产品的原始价格。 |
| ^^^^currency | string | USD | 币种代码。 |
| ^^^^minimum_amount | string | 12.21 | 产品所有 SKU 的最低原始价格。 |
| ^^^^maximum_amount | string | 100.00 | 产品所有 SKU 的最高原始价格。 |
| ^^^commission | object |  | Commission 信息。 |
| ^^^^rate | int | 3000 | Commission 比率，以百分之一为单位。例如，3587 表示 35.87% 的 commission 比率。此值最小为 1000。此值范围为 [100, 8000]。 |
| ^^^^effective_time | string | 1715654330 | Commission 生效时间，以字符串形式的秒级 Unix 时间戳表示。 |
| ^^^^currency | string | USD | 币种代码。 |
| ^^^^minimum_amount | string | 34.3 | 此产品所有 SKU 的最低预估 commission 金额。 |
| ^^^^maximum_amount | string | 55.7 | 此产品所有 SKU 的最高预估 commission 金额。 |
| ^^^^shop_ads_commission_rate | int | 100 | The commission rate applies only to orders generated from ads. If a creator’s video is used as an ad without this rate being set, the resulting orders will instead earn either: |

* 您在 open collaboration 中配置的 Shop Ads commission，或
* 此邀请中定义的标准 commission。
   Commission 比率以万分之一为增量指定。
   例如，1000 代表 0.1 或 10%。 |
   ^^^status |string |LIVE |产品状态。
   字段值：
* LIVE: When the product is normal for sale, return to the LIVE status
* OUT_OF_STOCK: When the product is out of stock for the consumer, the OUT_OF_STOCK state is returned
* SELLER_DEACTIVATE: When the product is deactivated by the merchant, the SELLER_DEACTIVATE status is returned
* PLATFORM_DEACTIVATE: When the product is deactivated by the platform or is not available for sale, the PLATFORM_DEACTIVATE status is returned
* GNE_REJECT: When the product is governed or the target collaboration is dismissed, the GNE_REJECT state is returned
* DELETE: When the product is deleted, the DELETE status is returned
* OTHER: When the product is in an unsaleable state, such as draft, frozen, review, etc, the OTHER status is returned |
   ^^^commission_effective_status |string |EFFECTIVE_ALL |此产品的 target collaboration commission 在各 creator 中的有效性。
   字段值：
* EFFECTIVE_ALL: The commission is effective for all creators.
* EFFECTIVE_PARTIALLY: The commission is effective for some creators.
* EFFECTIVE_NONE: The commission is not effective for any creators.
   通常，产品的 commission 对所有 creator 相同。
   如果商家参与 TOP_CREATOR_PROGRAM，且 TOP_CREATOR_PROGRAM 包含当前产品和部分 creator，则 commission 比率将基于 TOP_CREATOR_PROGRAM。 当前 Target Collaboration 下的产品 commission 将对部分 creator 生效，对应 EFFECTIVE_PARTIALLY 状态。 |
   ^^^collaboration_status |string |NORMAL |产品在当前 target cooperation 中的状态。
   字段值：
* NORMAL: The status of the product in the current target collaboration is normal.
* DELETING: The status of the product in the current target collaboration is deleting.Product in the DELETING state will end their delayed effectiveness state and move to the DELETED state at 00:00 the next day.
* DELETED: The status of the product in the current target collaboration is deleted. |
   ^^creators |[]object | |Target collaboration 中的 creator 信息。 |
   ^^^username |string |123456 |TikTok 用户名。 |
   ^^^nickname |string |123456 |TikTok 昵称。 |
   ^^^avatar |object | |与 TikTok creator 个人资料头像关联的数据。 |
   ^^^^url |string |https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078&x-expires=1712988000&x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D |TikTok creator 头像图片文件的 URL。 |
   ^^^selection_region |string |US |Creator 有资格在 showcase、视频和直播中推广产品的地区。 |
   ^^^showcase_product_count |int |2 |此字段表示 creator 从 target collaboration 添加到 showcase 的产品数量。
   计数包括 NORMAL 和 DELETING 状态。 |
   ^^^content_product_count |int |1 |此字段表示 creator 从 target collaboration 发布视频或直播的产品数量。
   计数包括 NORMAL 和 DELETING 状态。 |
   ^^^collaboration_status |string |NORMAL |The status of the creator in the current target cooperation.
   字段值：
* NORMAL: The status of the creator in the current target collaboration is normal.
* DELETING: The status of the creator in the current target collaboration is deleting.The creator's product promotion relationship in the DELETING status will end the delayed effectiveness status and flow to the DELETED status at 00:00 the next day.
* DELETED: The status of the creator in the current target collaboration is deleted. |
   ^^^product_effective_status |string |EFFECTIVE_ALL |Target collaboration 的产品 commission 对该 creator 的有效性。
   字段值：
* EFFECTIVE_ALL: The commission is effective for this creator on all products in the target collaboration.
* EFFECTIVE_PARTIALLY: The commission is effective for this creator on some products in the target collaboration.
* EFFECTIVE_NONE: The commission is not effective for this creator on any products in the target collaboration.
   Normally, the commission rate for all products under Target Collaboration is effective.
   If the merchant participates in TOP_CREATOR_PROGRAM, and TOP_CREATOR_PROGRAM includes the current creator and some products, the commission rate will be based on TOP_CREATOR_PROGRAM. The products' commission under the current Target Collaboration will only be partially effective for the creator, corresponding to EFFECTIVE_PARTIALLY status. |
   ^^^creator_open_id |string |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
   ^^type |string |STANDARD |Target collaboration 的类型。
   字段值：
* STANDARD: The target collaboration is created by sellers manually selecting products and creators.
* TOP_CREATOR_PROGRAM: The target collaboration created by seller joining TikTok Shop Top Creator Program, requiring only product submission. |

# 响应示例
```json
{"code":0,"data":{"target_collaboration":{"id":"789078671231123124","name":"target_collaboration","message":"test","seller_contact_info":{"email":"test@bytedance.com","phone_number":"1234","whatsapp":"aaaa","telegram":"1234","line":"asd"},"start_time":1715654330,"end_time":1715654330,"update_time":1715654330,"creator_invited_count":10,"showcase_creator_count":2,"content_creator_count":1,"product_count":30,"free_sample_rule":{"has_free_sample":true,"is_sample_approval_exempt":true},"products":[{"id":"789078671231312312","main_image_url":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a/12345~c5_168x168.webp?lk3s=a5d48078\u0026nonce=49646\u0026refresh_token=b53364a3a1947c4ac7a0c4bea62e31ea\u0026x-expires=1727175600\u0026x-signature=ASPIxFDNDkN1cknLEItlyC%2Bcfbw%3D\u0026shp=a5d48078\u0026shcp=39dffb78","title":"Christmas Gift","original_price":{"currency":"USD","minimum_amount":"12.21","maximum_amount":"100.00"},"commission":{"rate":3000,"effective_time":"1715654330","currency":"USD","minimum_amount":"34.3","maximum_amount":"55.7","shop_ads_commission_rate":100},"status":"LIVE","commission_effective_status":"EFFECTIVE_ALL","collaboration_status":"NORMAL"}],"creators":[{"username":"123456","nickname":"123456","avatar":{"url":"https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/2bf6a2485ec8bf93483e4a6ed907e6fd~c5_720x720.webp?lk3s=a5d48078\u0026x-expires=1712988000\u0026x-signature=E8US22KfUCwKz0R%2FMFF6%2FMOmogs%3D"},"selection_region":"US","showcase_product_count":2,"content_product_count":1,"collaboration_status":"NORMAL","product_effective_status":"EFFECTIVE_ALL","creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"}],"type":"STANDARD"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 50001700 | seller cannot access this target collaboration |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

