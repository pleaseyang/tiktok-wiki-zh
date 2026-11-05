# 搜索全球产品

# Path: /product/202312/global_products/search
# Method: [POST]
# 功能描述
Retrieve a list of global products that meet the specified conditions. Results are sorted by creation time in descending order. This API returns only key product properties. To obtain more details, pass a returned global product ID to the [Get Global Product API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96).

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | Y | 100 | 每页返回的结果数量。 |
| Valid range: [1-100] |  |  |  |  |
|  |  |  |  |  |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| status | string | N | PUBLISHED | Filter global products by their status. |
| Possible values: |  |  |  |  |

* PUBLISHED
* UNPUBLISHED
* DRAFT
* DELETED |
   seller_skus |[]string |N |["Color-Red-001"] |A Seller SKU used to filter global products. Provide no more than one Seller SKU. The API returns global products that include the specified Seller SKU. |
   create_time_ge |int |N |1694576429 |Filter global products to show only those that are created on or after the specified date and time. Unix timestamp in seconds.

**Note**:
The "create_time_ge" and "create_time_le" together constitute the creation time filter condition.

* If "create_time_ge" is filled but "create_time_le" is empty, "create_time_le" will default to the current time.
* If "create_time_le" is filled but "create_time_ge" is empty, "create_time_ge" will default to the earliest shop time. |
   create_time_le |int |N |1694576429 |Filter global products to show only those that are created on or before the specified date and time. Unix timestamp in seconds.
   Refer to notes in "create_time_ge" for more usage information. |
   update_time_ge |int |N |1694576429 |Filter global products to show only those that are updated on or after the specified date and time. Unix timestamp in seconds.

**Note**:
The fields "update_time_ge" and "update_time_le" together define the update time filter condition.

* If "update_time_ge" is filled but "update_time_le" is empty, "update_time_le" will default to the current time.
* If "update_time_le" is filled but "update_time_ge" is empty, "update_time_ge" will default to the earliest shop time. |
   update_time_le |int |N |1694576429 |Filter global products to show only those that are updated on or before the specified date and time. Unix timestamp in seconds.
   Refer to notes in `update_time_ge` for more usage information. |

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
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | b2Zmc2V0PTAK | An opaque token used to retrieve the next page of a paginated result set. Provide this value in the `page_token` parameter of your request if the current response does not return all the results. |
| ^total_count | int | 100 | The total number of global products that meet the query conditions. |
| ^global_products | []object |  | The list of global products that meet the query conditions. |
| ^^id | string | 1729592969712207008 | The global product ID in TikTok Shop. |
| ^^title | string | Men's Fashion Sports Low Cut Cotton Breathable Ankle Short Boat Invisible Socks | 产品标题。 |
| ^^status | string | PUBLISHED | The status of the product. |
| Possible values: |  |  |  |

* PUBLISHED
* UNPUBLISHED
* DRAFT
* DELETED |
   ^^skus |[]object | |A list of global Stock Keeping Units (SKUs) used to identify distinct variants of the product. |
   ^^^id |string |1729592969712207012 |The global SKU ID in TikTok Shop. One product can contain multiple SKU IDs. |
   ^^^seller_sku |string |Color-Red-XM001 |用于管理 SKU 的内部代码/名称，对买家不可见。 |
   ^^create_time |int |1694576429 |The time when the product is created.
   Unix timestamp in seconds. |
   ^^update_time |int |1694576429 |The time when the product is last updated.
   Unix timestamp in seconds. |

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
| 12052032 | The product does not exist |
| 12052180 | The total number of search results can not exceed 10000. |
| 12052700 | The seller is inactive. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12052901 | The product in its current status is not available for this operation. Change the product status and try again. |
| 12052910 | Invalid input parameters. Refer to the API documentation for details. |

