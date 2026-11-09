# 搜索全球商品

# 路径：/product/202312/global_products/search
# 方法：[POST]
# 功能描述
获取满足指定条件的全球商品列表。结果按创建时间降序排列。此 API 仅返回关键商品属性。要获取更多详情，请将返回的全球商品 ID 传给 [Get Global Product API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96)。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | Y | 100 | 每页返回的结果数量。 |
| 有效范围： [1-100] |  |  |  |  |
|  |  |  |  |  |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| status | string | N | PUBLISHED | 按状态筛选全球商品。 |
| 可能的值： |  |  |  |  |

* PUBLISHED
* UNPUBLISHED
* DRAFT
* DELETED |
   seller_skus |[]string |N |["Color-Red-001"] |用于筛选全球商品的卖家 SKU。最多提供一个卖家 SKU。该接口返回包含指定卖家 SKU 的全球商品。 |
   create_time_ge |int |N |1694576429 |筛选全球商品，仅显示创建时间不早于指定日期和时间的商品。Unix 时间戳，单位为秒。

**注意**：
"create_time_ge" 和 "create_time_le" 共同构成创建时间筛选条件。

* 如果填写了 "create_time_ge" 但 "create_time_le" 为空，"create_time_le" 将默认为当前时间。
* 如果填写了 "create_time_le" 但 "create_time_ge" 为空，则 "create_time_ge" 将默认为最早的店铺时间。 |
   create_time_le |int |N |1694576429 |筛选全球商品，仅显示创建时间不晚于指定日期和时间的商品。Unix 时间戳，单位为秒。
   更多使用信息请参阅 "create_time_ge" 中的说明。 |
   update_time_ge |int |N |1694576429 |筛选全球商品，仅显示更新时间不早于指定日期和时间的商品。Unix 时间戳，单位为秒。

**注意**：
字段 "update_time_ge" 和 "update_time_le" 共同定义更新时间筛选条件。

* 如果填写了 "update_time_ge" 但 "update_time_le" 为空，"update_time_le" 将默认为当前时间。
* 如果填写了 "update_time_le" 但 "update_time_ge" 为空，则 "update_time_ge" 将默认为最早的店铺时间。 |
   update_time_le |int |N |1694576429 |筛选全球商品，仅显示更新时间不晚于指定日期和时间的商品。Unix 时间戳，单位为秒。
   更多使用信息请参阅 `update_time_ge` 中的说明。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202312/global_products/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_size=100&page_token=b2Zmc2V0PTAK
```

**Body**
```json
{"status":"PUBLISHED","seller_skus":["Color-Red-001"],"create_time_ge":1694576429,"create_time_le":1694576429,"update_time_ge":1694576429,"update_time_le":1694576429}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明令牌。如果当前响应未返回全部结果，请在请求的 `page_token` 参数中提供此值。 |
| ^total_count | int | 100 | 符合查询条件的全球商品总数。 |
| ^global_products | []object |  | 符合查询条件的全球商品列表。 |
| ^^id | string | 1729592969712207008 | TikTok Shop 中的全球商品 ID。 |
| ^^title | string | Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks | 商品标题。 |
| ^^status | string | PUBLISHED | 商品的状态。 |
| 可能的值： |  |  |  |

* PUBLISHED
* UNPUBLISHED
* DRAFT
* DELETED |
   ^^skus |[]object | |用于标识商品不同变体的全球库存单位 (SKUs) 列表。 |
   ^^^id |string |1729592969712207012 |TikTok Shop 中的全球 SKU ID. 一个商品可包含多个 SKU ID。 |
   ^^^seller_sku |string |Color-Red-XM001 |用于管理 SKU 的内部代码/名称，对买家不可见。 |
   ^^create_time |int |1694576429 |商品的创建时间。
   以秒为单位的 Unix 时间戳。 |
   ^^update_time |int |1694576429 |商品最后一次更新的时间。
   以秒为单位的 Unix 时间戳。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"b2Zmc2V0PTAK","total_count":100,"global_products":[{"id":"1729592969712207008","title":"Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks","status":"PUBLISHED","skus":[{"id":"1729592969712207012","seller_sku":"Color-Red-XM001"}],"create_time":1694576429,"update_time":1694576429}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019015 | The number of SKU exceed the limit |
| 12019108 | page number is invalid |
| 12019109 | page size is invalid |
| 12019118 | search create time invalid |
| 12019119 | search update time invalid |
| 12052032 | 商品不存在 |
| 12052180 | The total number of search results can not exceed 10000. |
| 12052700 | 卖家不活跃。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |

