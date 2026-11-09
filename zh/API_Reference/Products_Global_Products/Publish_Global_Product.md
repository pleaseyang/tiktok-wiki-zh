# 发布全球商品

# 路径：/product/202309/global_products/{global_product_id}/publish
# 方法：[POST]
# 功能描述
在受支持市场的一个或多个店铺中发布全球商品并将其转换为本地商品。发布后，商品将由 TikTok Shop 在相应市场送审。对于欧盟市场的卖家，所提供的信息还将自动翻译为 TikTok Shop 支持的所有欧盟语言。
**注意**：

* 每个市场只能发布一次。要更改商品信息，请使用 [Edit Global Product API](6509e1bcc16ffe02b8dc3cd7) 编辑全球商品。更改将自动同步到该商品已发布的所有市场
* 使用 [Get Product API](6509d85b4a0bb702c057fdda) 获取目标市场语言下转换后的本地商品信息。
* 如有需要，使用 [Edit Product API](6509da7d0fcef602bf1caddf) 或 [Partial Edit Product API](650a98d74a0bb702c06c3289) 修改本地商品信息。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_product_id | string | Y | 1729592969712207008 | 全球商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| publish_target | []object | Y |  | 发布全球商品的目标市场。 |
|  |  |  |  |  |
| ^region | string | Y | MY | 要发布该全球商品的新市场。 |
| 可能的值： |  |  |  |  |

* AT: 奥地利
* BE:Belgium
* CZ:捷克
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU:Hungary
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MY: 马来西亚
* NL: 荷兰(NL)
* PH: 菲律宾
* PO: Poland
* PT:Portugal
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥 |
   ^responsible_person_ids |[]string |N |["67726293bf1eb1e92401a"] |负责人 ID 列表。从 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1)。
   默认值：创建全球商品时提供的 ID。
   **注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Global Category Rules API](650a056df1fd3102b91b5b8e) 检查要求。 |
   ^manufacturer_ids |[]string |N |["67726293bf1eb1e92401a"] |制造商 ID 列表。从 [Search Manufacturers API](67066a580dcee902fa03ccf9)。
   默认值：创建全球商品时提供的 ID。
   **注意**： 仅适用于欧盟市场的特定分类。 Use the [Get Global Category Rules API](650a056df1fd3102b91b5b8e) 检查要求。 |
   ^skus |[]object |Y | |要在指定市场上架的 SKU。
* EU、JP、UK、US 的最大 SKU 数：300
* 其他地区的最大 SKU 数量：100 |
   ^^related_global_sku_id |string |Y |1729592969712207400 |待发布的全球 SKU ID。
   发布后，将创建对应的本地商品 SKU 并关联到全球 SKU。 |
   ^^price |object |N | |指定市场中 SKU 的本地价格信息。

**注意**：

* 仅当您想要手动覆盖默认的本地价格时提供此值，默认本地价格由全球统一价格自动计算得出。
* 请指定 `amount` 或 `sale_price` 之一，另一项将自动填充。如果两者都提供，`sale_price` 优先。
* 使用中国仓库的 JP 和 US 店铺必须提供 `price.sale_price`。 |
   ^^^amount |string |N |10.01 |SKU 的**本地税前价格**。其中不含任何适用费用，如跨境配送成本、税费及其他费用，因此不会显示在商品页面上。
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

**注意**: 不适用于使用中国仓库的 JP 和 US 店铺，请改用 `price.sale_price`。 |
^^^currency |string |Y |MYR |货币。
基于地区的可能值：

* BRL: 巴西
* CZK: 捷克共和国
* EUR: 法国、德国、爱尔兰、意大利、西班牙、荷兰、比利时、奥地利、希腊、葡萄牙
* GBP: 英国
* HUF: 匈牙利
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* PLN: 波兰
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^sale_price |string |N |100.00 |SKU 在商品页面上折扣前显示的**本地展示价格**。
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

**注意**：

* 对于使用中国仓库的 JP 和 US 店铺为必填，其他为可选。
* 这是商品页面上显示的最终确定价格，所有其他价格将被忽略。 |
   ^^inventory |object |N | |各仓库的 SKU 库存信息。
   没有多个仓库的卖家必填，其他卖家可选。

**说明**：如果未提供库存明细，全球 SKU 数量将在所有市场间平均分配，余数将加到最后一个已发布的商品 SKU 上。 |
^^^warehouse_id |string |N |7068517275539719942 |仓库 ID。可从 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6) 获取此值。
Default:

* 没有多个仓库的卖家：将使用可用仓库，优先使用指定市场内的本地仓库，其次为卖家基准国家的仓库。
* 拥有多个仓库的卖家: 全局仓库 ID |
   ^^^quantity |int |N |999 |仓库中可用的 SKU 数量。
   有效范围：[1, 99,999]

**注意**： 如果本地 SKU 库存数量超过全球 SKU 数量，则全球 SKU 数量将更新为所有本地库存的总和。 |
^^fees |[]object |N | |根据 TikTok Shop 政策该商品所需的费用。仅某些商品类目需要费用，请从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取要求。 |
^^^type |string |N |PFAND |费用类型。
可能的值：PFAND |
^^^amount |string |N |1.01 |费用金额。
有效范围：

* PFAND: [0.00 - 6300.00] |
   ^^^additional_attribute |string |N |SINGLE_USE |提供费用附加上下文的可选属性。接受的值可能因费用类型和市场而异。

Pfand 的可能值：

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_products/1729592969712207008/publish?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"publish_target":[{"region":"MY","responsible_person_ids":["67726293bf1eb1e92401a"],"manufacturer_ids":["67726293bf1eb1e92401a"],"skus":[{"related_global_sku_id":"1729592969712207400","price":{"amount":"10.01","currency":"MYR","sale_price":"100.00"},"inventory":{"warehouse_id":"7068517275539719942","quantity":999},"fees":[{"type":"PFAND","amount":"1.01","additional_attribute":"SINGLE_USE"}]}]}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 由全球商品转换而来的本地商品。按 `region` 将每个项目与 `publish_result` 中对应的发布结果进行匹配。当某地区的状态为 `FAILED` 时，该地区可以有 `publish_result` 项目但没有对应的本地商品。 |
| ^^region | string | MY | 该本地商品所在的市场。 |
| 可能的值： |  |  |  |

* AT: 奥地利
* BE:Belgium
* CZ:捷克
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU:Hungary
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MY: 马来西亚
* NL: 荷兰(NL)
* PH: 菲律宾
* PO: Poland
* PT:Portugal
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥 |
   ^^shop_id |string |7494083603082020484 |指定市场中本地店铺的 ID. 一个市场只能有一个本地店铺。 |
   ^^skus |[]object | |指定市场中新创建的本地 SKU。 |
   ^^^related_global_sku_id |string |1729696746528737924 |关联的全局 SKU ID。 |
   ^^^id |string |1729592969712207400 |新生成的本地 SKU ID。 |
   ^^^seller_sku |string |XL-COLOR-001 |用于管理 SKU 的内部代码/名称，对买家不可见。 |
   ^^^sale_attributes |[]object | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。 |
   ^^^^id |string |100001 |新生成的本地销售属性 ID。 |
   ^^^^value_id |string |7272008676829824800 |新生成的本地销售属性值 ID。 |
   ^^id |string |1929592969712207410 |新生成的本地商品 ID。 |
   ^publish_result |[]object | |全球商品发布的结果。 |
   ^^region |string |MY |与此发布结果关联的市场。
   可能的值：
* AT: 奥地利
* BE:Belgium
* CZ:捷克
* DE: 德国
* ES: Spain
* FR: 法国
* GB: 英国
* GR: 希腊
* HU:Hungary
* ID: 印度尼西亚
* IE: 爱尔兰
* IT: Italy
* JP: Japan
* MY: 马来西亚
* NL: 荷兰(NL)
* PH: 菲律宾
* PO: Poland
* PT:Portugal
* SG: 新加坡
* TH: 泰国
* US: 美国
* VN: 越南
* MX: 墨西哥 |
   ^^status |string |SUCCESS |将商品发布到市场的状态。
   可能的值：
* SUCCESS：全球商品已成功发布到本地店铺，已提交上架，目前正在审核中。
* DRAFT: 由于校验错误，该全球商品被保存为草稿本地商品。
* FAILED：全球商品同步到本地店铺未成功。 |
   ^^fail_reasons |[]object | |发生的错误列表。 |
   ^^^message |string |The publish region is inactive. |错误消息。 |

# 响应示例
```json
{"code":0,"data":{"products":[{"region":"MY","shop_id":"7494083603082020484","skus":[{"related_global_sku_id":"1729696746528737924","id":"1729592969712207400","seller_sku":"XL-COLOR-001","sale_attributes":[{"id":"100001","value_id":"7272008676829824800"}]}],"id":"1929592969712207410"}],"publish_result":[{"region":"MY","status":"SUCCESS","fail_reasons":[{"message":"The publish region is inactive."}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019004 | Seller is inactive |
| 12019010 | product price is invalid |
| 12019016 | Unable to publish or sync products to target markets due to missing or invalid warehouse details. |
| 12019028 | Multiple warehouses detected. Include all warehouse IDs and the corresponding details and try again. |
| 12019113 | product status is invalid |
| 12019121 | calculate price error |
| 12019150 | 商品 ID 不存在。 |
| 12019212 | region already published |
| 12052055 | The SKU inventory quantity for the warehouse must be within allowed limits. |
| 12052084 | 所提供的货币不适用于该店铺/地区。 |
| 12052117 | seller publish global product over limit and save draft |
| 12052145 | activity warehouse not allowed to be deleted |
| 12052146 | The specified inventory quantity is too low. It must be greater than the locked quantity (e.g. for committed orders, campaigns, creators) to ensure a non-negative available stock. |
| 12052260 | 商品 ID 不存在 |
| 12052379 | the cover region of share warehouse can not cover the the product region |
| 12052424 | Missing 'sale price' value |
| 12052531 | The warehouse is disabled. |
| 12052556 | The SKU id not exist. |
| 12052700 | 卖家不活跃。 |
| 12052701 | do not support cross-boarder seller create local product directly |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |
| 12052903 | The publish region is inactive. |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |

