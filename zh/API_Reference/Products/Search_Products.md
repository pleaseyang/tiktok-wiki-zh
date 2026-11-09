# 搜索商品

# 路径：/product/202502/products/search
# 方法：[POST]
# 功能描述
获取满足指定条件的商品列表。
此接口仅返回关键商品属性。可将返回的商品 ID 传入 [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) 以获取商品的更多详细信息。

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
| page_size | int | Y | 100 | 每页返回的结果数量。 |
| 有效范围： [1-100] |  |  |  |  |
| page_token | string | N | WzE3ODY0Njk5NDg1MTgsIjE3MzY5OTA2MTM0NTI5ODE4MTciXQ== | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| status | string | N | ALL | 基于商品的基础版本筛选商品。换言之，此筛选不适用于上架后的草稿或编辑。例如，`status=DRAFT` 仅返回处于 DRAFT 状态的未上架商品，而不返回有生效草稿的在售商品。 |
可能的值：

* ALL
* DRAFT
* PENDING
* FAILED
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED
   Default: ALL |
   seller_skus |[]string |N |["Color-Red-XM001"] |按这些卖家 SKU 编码筛选商品。 |
   create_time_ge |int |N |1694309208 |筛选商品，仅显示在指定日期和时间或之后创建的商品。以秒为单位的 Unix 时间戳。

**注意**：
`create_time_ge` 与 `create_time_le` 共同构成创建时间筛选条件。

* 如果填写了 `create_time_ge` 但 `create_time_le` 为空，`create_time_le` 将默认为当前时间。
* 如果填写了 `create_time_le` 但 `create_time_ge` 为空，则 `create_time_ge` 将默认为最早的店铺时间。 |
   create_time_le |int |N |1694319208 |筛选商品，仅显示在指定日期和时间或之前创建的商品。以秒为单位的 Unix 时间戳。
   更多使用信息请参阅 `create_time_ge` 中的说明。 |
   update_time_ge |int |N |1694319208 |筛选商品，仅显示在指定日期和时间或之后更新的商品。以秒为单位的 Unix 时间戳。

**注意**：
`update_time_ge` 和 `update_time_le` 共同定义更新时间筛选条件。

* 如果填写了 `update_time_ge` 但 `update_time_le` 为空，`update_time_le` 将默认为当前时间。
* 如果填写了 `update_time_le` 但 `update_time_ge` 为空，则 `update_time_ge` 将默认为最早的店铺时间。 |
   update_time_le |int |N |1694319208 |筛选商品，仅显示在指定日期和时间或之前更新的商品。以秒为单位的 Unix 时间戳。
   更多使用信息请参阅 `update_time_ge` 中的说明。 |
   category_version |string |N |v1 |按类目树版本筛选商品。
   基于地区的可能值：
* US：`v2`，表示 7 级类目树。
* 其他地区：`v1`，表示 3 级类目树。
   默认: 返回 `v1` 和 `v2` 类目树中的所有商品。 |
   listing_quality_tiers |[]string |N |["POOR","FAIR"] |按商品的上架质量等级筛选商品。
   可能的值：
* POOR
* FAIR
* GOOD
* EXCELLENT
   默认：返回全部
   **注意**：仅适用于美国市场。 |
   listing_platforms |[]string |N |["TIKTOK_SHOP"] |按上架平台筛选商品。
   可能的值：
* TOKOPEDIA
* TIKTOK_SHOP
   默认：返回所有商品，无论其上架平台。

仅适用于从 Tokopedia 迁移的卖家。
**注意**：

* 按上架平台筛选时，还必须指定 `ALL` 以外的 `status` 取值. 不支持返回所有状态。
* 如果传入一个平台，搜索将返回在该平台上架的商品，包括同时在两个平台上架的商品。
* 如果传入 `["TIKTOK_SHOP", "TOKOPEDIA"]`, 则仅返回同时在这两个平台上架的商品，不返回仅在一个平台上架的商品。 |
   audit_status |[]string |N |["AUDITING"] |按商品在 TikTok Shop 的审核状态筛选商品。
   可能的值：
* AUDITING: 返回基础版本或直播后编辑当前正在审核中的商品。
* FAILED: 返回基础版本或直播后编辑未通过审核，或审核被取消的商品。
* APPROVED: 返回已通过审核并已在平台上架的商品。 |
   sku_ids |[]string |N |["1729592969712207230"] |按 SKU ID 筛选商品。
   最大数量：10 |
   sns_filter |string |N |CONFIGURED |按商品的 Subscribe and Save (SNS) 状态筛选商品。可选值：
* CONFIGURED
* ELIGIBLE |
   return_draft_version |bool |N |true |筛选商品，仅显示有草稿的商品。
* true: 仅返回草稿版本的商品. 排除没有草稿的商品。
* false: 返回所有商品，无论其是否有草稿。
   默认值：false

**注意**： 仅当商品状态筛选条件为 `ALL`, `DRAFT`, `ACTIVATE`, `SELLER_DEACTIVATED` 或 `PLATFORM_DEACTIVATED` 时适用。 |
locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。
Default: 您店铺的默认语言环境。
可能的值：

* cs-CZ
* de-AT
* de-BE
* de-DE
* el-GR
* en-GB
* en-IE
* en-US
* es-ES
* es-MX
* fr-FR
* fr-BE
* hu-HU
* id-ID
* it-IT
* ja-JP
* ms-MY
* nl-NL
* nl-BE
* pl-PL
* pt-BR
* pt-PT
* th-TH
* vi-VN
* zh-CN |
   include_live_quick_products |bool |N |false |是否在查询结果中包含 LIVE_QUICK 商品。
   true — 返回 LIVE_QUICK 商品和普通商品。
   false —仅返回普通商品。

默认值：false |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202502/products/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=100&page_token=WzE3ODY0Njk5NDg1MTgsIjE3MzY5OTA2MTM0NTI5ODE4MTciXQ==
```

**Body**
```json
{"status":"ALL","seller_skus":["Color-Red-XM001"],"create_time_ge":1694309208,"create_time_le":1694319208,"update_time_ge":1694319208,"update_time_le":1694319208,"category_version":"v1","listing_quality_tiers":["POOR","FAIR"],"listing_platforms":["TIKTOK_SHOP"],"audit_status":["AUDITING"],"sku_ids":["1729592969712207230"],"sns_filter":"CONFIGURED","return_draft_version":true,"locale":"en-US","include_live_quick_products":false}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^total_count | int | 200 | 符合查询条件的商品总数。 |
| ^products | []object |  | 符合查询条件的商品列表。 |
| ^^id | string | 1729592969712207008 | TikTok Shop 生成的商品 ID。 |
| ^^title | string | Short Boat Invisible Socks | 商品标题。 |
| ^^status | string | ACTIVATE | 商品在 TikTok Shop 中的状态。 |
| 可能的值： |  |  |  |

* UNKNOWN
* DRAFT
* PENDING
* FAILED
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED

**注意**： 对于印度尼西亚卖家，如果您在创建或编辑商品时未将上架平台设置为 `TIKTOK_SHOP`，则此字段将被省略。 |
^^skus |[]object | |用于标识商品不同变体的 SKU（库存单位）列表。 |
^^^id |string |1729592969712207012 |TikTok Shop 生成的 SKU ID。 |
^^^seller_sku |string |Color-Red-XM01 |用于管理 SKU 的内部代码/名称，对买家不可见。 |
^^^price |object | |SKU 定价信息。 |
^^^^currency |string |USD |货币。
可能的值：

* BRL: 巴西
* EUR：法国、德国、爱尔兰、意大利、西班牙
* GBP: 英国
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^^tax_exclusive_price |string |111.01 |**本地卖家/欧盟内部卖家**
   SKU 在商品页面上折扣前显示的**本地展示价格**。

**全球卖家**
SKU 的**本地税前价格**。不含跨境配送费用、税费及其他适用费用等，因此不会显示在商品页面上。
**注意**: 不含税定价不适用于 JP 市场，因此此取值与 `sale_price` 相同。 |
^^^^sale_price |string |121.11 |**全球卖家**
SKU 在商品页面上折扣前显示的**本地展示价格**。 |
^^^^starting_bid_price |string |2 |拍卖商品的起始竞价 |
^^^inventory |[]object | |SKU 库存信息。
**说明**：直播后草稿不支持此字段，因此即使设置 `return_draft_version=true`，此处的取值也始终反映基础版本中的取值。 |
^^^^warehouse_id |string |7068517275539719942 |SKU 存放仓库的 ID。
从 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6) 获取仓库详情。 |
^^^^quantity |int |999 |仓库中可用的 SKU 总数量。
有效范围：[1, 99,999]
注意：此数量特指可以立即发货的有库存的库存量。 |
^^^^backorder_quantity |int |888 |现货库存售罄后，`backorder_quantity` 将自动转换为 `quantity`。此库存的履约遵循下文指定的 `handling_time`。
注意：按单生产（MTO）、预售和定制商品不支持缺货预订，因此与 backorder_quantity 不兼容。 |
^^^^handling_time |int |5 |The estimated number of working days needed for a backorder to be shipped. Currently, different warehouses for the same SKU are not allowed to have different `handling_time` |
^^^list_price |object | |经审核团队验证为合规的 SKU 标价信息。相当于制造商建议零售价（MSRP）或建议零售价（RRP）。
仅适用于美国市场。
**注意**：

* 如果提交的价格未通过校验，此字段将为空或显示上次核验的价格。
* 该值可能作为划线价显示在商品页面上。但是，是否显示划线价以及显示的金额由审核团队根据各种定价信息审核并决定。 |
   ^^^^amount |string |1 |价格金额。 |
   ^^^^currency |string |USD |货币。
   可能的值： USD |
   ^^^external_list_prices |[]object | |SKU 标价（如 MSRP、RRP）或外部电商平台上的原价信息。
   仅适用于美国市场的部分卖家。

**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^^^source |string |SHOPIFY_COMPARE_AT_PRICE |价格来源的外部电商平台。
可能的值：

* SHOPIFY_COMPARE_AT_PRICE: Shopify 中的 compare_at_price。 |
   ^^^^amount |string |1 |价格金额。 |
   ^^^^currency |string |USD |货币。
   可能的值： USD |
   ^^^pre_sale |object | |SKU presale information, used to tag a product as a presale product based on its presale type.

如果未返回此项，表示该商品为普通的非预售商品。 |
^^^^type |string |PRE_ORDER |预售类型。
基于地区的可能值：
**US**

* `PRE_ORDER`：商品尚未上架或发布。可通过指定发布日期延长履约。
* `MADE_TO_ORDER`：商品仅在收到订单后生产。可通过指定时长延长履约。
* `CUSTOM`：因其他因素，商品所需的履约时限超出标准。可通过指定时长延长履约。

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`：商品尚未上架或发布。可通过指定时长延长履约。 |
   ^^^^fulfillment_type |object | |关于预售订单履约类型及相应时间范围的信息。
* `handling_duration_days` 适用于延长时长的履约。
* `release_date` 用于在固定日期开始履约。 |
   ^^^^^handling_duration_days |int |7 |处理预售订单并移交承运商所需的期望持续时间。

仅适用于以下地区和预售类型：
**US**

* `MADE_TO_ORDER`: Business days
* `CUSTOM`: Business days

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`: Calendar days |
   ^^^^^release_date |int |1619611761 |商品转为普通商品并可供一般购买的日期。在此日期，订单处理也将开始，订单状态将变为 [AWAITING_SHIPMENT](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011)。

仅适用于美国的 `PRE_ORDER`。
**注意**: 此日期是基于卖家在 Seller Center 所选时区的 Unix 时间戳（秒）。 |
^^^status_info |object | |SKU 的状态信息。 |
^^^^status |string |DEACTIVATED |该 SKU 在 TikTok Shop 中的状态。
可能的值：

* NORMAL
* DEACTIVATED |
   ^^^^deactivation_source |string |PLATFORM |处于 `DEACTIVATED` 状态的 SKU 的停用来源。
   可能的值：
* SELLER: 表示卖家停用了该 SKU
* PLATFORM: 表示平台因违规原因停用了该 SKU
* COMBO_RELATION: 表示子 SKU 停用导致平台停用了组合 SKU。 |
   ^^^fees |[]object | |根据 TikTok Shop 政策该商品所需的费用。仅某些商品类目需要费用，请从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取要求。 |
   ^^^^type |string |PFAND |费用类型。
   可能的值：PFAND |
   ^^^^amount |string |1.01 |费用金额。
   有效范围：
* PFAND: [0.00 - 6300.00] |
   ^^^^additional_attribute |string |SINGLE_USE |提供费用附加上下文的可选属性。接受的值可能因费用类型和市场而异。

Pfand 的可能值：

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |
   ^^sales_regions |[]string |["US"] |商品销售所在的地区。
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
   ^^create_time |int |1234567890 |商品的创建时间。
   以秒为单位的 Unix 时间戳。 |
   ^^update_time |int |1234567800 |商品最后一次更新的时间。
   以秒为单位的 Unix 时间戳。 |
   ^^product_sync_fail_reasons |[]string |["The required qualification is missed."] |全球商品信息同步到本地商品失败的原因。
   仅适用于跨境卖家。 |
   ^^is_not_for_sale |bool |true |指示商品是否不可售的标志。
   True：不出售。
   False: 在售。 |
   ^^recommended_categories |[]object | |基于商品标题、描述和图片为商品推荐的类目。 |
   ^^^id |string |853000 |推荐类目的 ID。 |
   ^^^local_name |string |Botol & Stoples Penyimpanan |The localized category name. For a shop in a region that supports multiple languages, a non-empty requested `locale` determines the language. Otherwise, the language is derived from the shop region. |
   ^^listing_quality_tier |string |POOR |此商品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc。

可能的值：

* POOR
* FAIR
* GOOD
* EXCELLENT

**注意**：仅适用于美国市场。 |
^^integrated_platform_statuses |[]object | |商品在与 TikTok Shop 原生集成的平台上的当前状态 (例如 TOKOPEDIA)。
**注意**： 对于印度尼西亚卖家，如果您在创建或编辑商品时未将上架平台设置为 `TOKOPEDIA`，则此字段将被省略。 |
^^^platform |string |TOKOPEDIA |集成平台名称。
可能的值：

* TOKOPEDIA |
   ^^^status |string |PLATFORM_DEACTIVATED |商品在集成平台中的状态。
   可能的值：
* DRAFT
* PENDING
* FAILED
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED |
   ^^audit |object | |TikTok Shop 的商品审核信息。 |
   ^^^status |string |AUDITING |商品审核状态。
   可能的值：
* NONE: 商品仍处于草稿、冻结或停用状态，因此不适用审核。
* AUDITING：商品正在审核中。
* FAILED: 商品审核未通过，或审核已被取消。
* PRE_APPROVED: 商品已通过审核，但因前置条件尚未完成而未上架。
* APPROVED: 商品已通过审核并在平台上架。 |
   ^^^pre_approved_reasons |[]string |["KYC_PENDING"] |商品被预先批准的原因。
   仅当 `audit.status=PRE_APPROVED` 时适用，否则返回空数组。
   可能的值：
* KYC_PENDING: 卖家的入驻(KYC - Know Your Customer 信息)不完整或待处理。
* RESTRICTED_CATEGORY_PENDING: 该商品属于受限类目，且类目审批仍在等待中。要申请访问权限，请通过 TikTok Shop Seller Center 上的 Qualification Center 提交申请。仅适用于美国市场。 |
   ^^product_families |[]object | |该商品所属的**在售**商品系列。商品系列是一组共享共同特征（如口味、版本或尺寸）的虚拟商品分组，使它们可以在商品页面上作为可选变体展示。
   **注意**：
* 仅适用于美国本地卖家。
* 如果该商品不属于任何商品系列，则省略。 |
   ^^^id |string |1000592969712207000 |商品系列 ID。 |
   ^^^products |[]object | |属于该商品系列的商品列表。 |
   ^^^^id |string |1729592969712207008 |商品 ID。 |
   ^^has_draft |bool |true |指示商品是否有草稿的标志。
* true: 有草稿。
* false: 没有草稿。
   使用 Get Product 并传入 `return_draft_version=true` 以获取草稿的完整详情。 |
   ^^scheduled_sale |object | |商品的定时上架配置，包括是否启用定时上架以及定时上架时间。 |
   ^^^is_enabled_scheduled_sale |bool |false |该商品是否启用了定时上架。 |
   ^^^schedule_sale_time |int |1768899145000 |为商品存储的计划上架时间，以毫秒为单位的 Unix 时间戳表示。当 `is_enabled_scheduled_sale` 为 `true` 时，此取值适用。 |
   ^^product_tags |[]string |["AUCTION"] |用于标识特殊类型商品的商品标签
   可能的值： AUCTION、LIVE_QUICK |
   ^^selling_format |string |FIXED_PRICE |The product's sale format. 可能的值： FIXED_PRICE, LIVE_AUCTION, FIXED_PRICE_AND_LIVE_AUCTION。 |
   ^next_page_token |string |WzE3ODY0Njk5NDg1MTgsIjE3MzY5OTA2MTM0NTI5ODE4MTciXQ== |用于检索分页结果集下一页的不透明令牌。如果当前响应未返回所有结果，请在请求的 `page_token` 参数中提供此值。 |

# 响应示例
```json
{"code":0,"data":{"total_count":200,"products":[{"id":"1729592969712207008","title":"Short Boat Invisible Socks","status":"ACTIVATE","skus":[{"id":"1729592969712207012","seller_sku":"Color-Red-XM01","price":{"currency":"USD","tax_exclusive_price":"111.01","sale_price":"121.11","starting_bid_price":"2"},"inventory":[{"warehouse_id":"7068517275539719942","quantity":999,"backorder_quantity":888,"handling_time":5}],"list_price":{"amount":"1","currency":"USD"},"external_list_prices":[{"source":"SHOPIFY_COMPARE_AT_PRICE","amount":"1","currency":"USD"}],"pre_sale":{"type":"PRE_ORDER","fulfillment_type":{"handling_duration_days":7,"release_date":1619611761}},"status_info":{"status":"DEACTIVATED","deactivation_source":"PLATFORM"},"fees":[{"type":"PFAND","amount":"1.01","additional_attribute":"SINGLE_USE"}]}],"sales_regions":["US"],"create_time":1234567890,"update_time":1234567800,"product_sync_fail_reasons":["The required qualification is missed."],"is_not_for_sale":true,"recommended_categories":[{"id":"853000","local_name":"Botol \u0026 Stoples Penyimpanan"}],"listing_quality_tier":"POOR","integrated_platform_statuses":[{"platform":"TOKOPEDIA","status":"PLATFORM_DEACTIVATED"}],"audit":{"status":"AUDITING","pre_approved_reasons":["KYC_PENDING"]},"product_families":[{"id":"1000592969712207000","products":[{"id":"1729592969712207008"}]}],"has_draft":true,"scheduled_sale":{"is_enabled_scheduled_sale":false,"schedule_sale_time":1768899145000},"product_tags":["AUCTION"],"selling_format":"FIXED_PRICE"}],"next_page_token":"WzE3ODY0Njk5NDg1MTgsIjE3MzY5OTA2MTM0NTI5ODE4MTciXQ=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019027 | 搜索筛选条件中 “seller_skus” 的最大数量为 10。 |
| 12019087 | The number of SKU IDs exceeds the limit of 10 |
| 12019108 | page number is invalid |
| 12019109 | page size is invalid |
| 12019118 | search create time invalid |
| 12019119 | search update time invalid |
| 12052180 | The total number of search results can not exceed 10000. |
| 12052700 | 卖家不活跃。 |
| 12052704 | 卖家 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |

