# 获取全球上架规则

# Path: /product/202507/global_listing_rules
# Method: [GET]
# 功能描述
Retrieves the global listing rules for a local shop that belongs to a global seller. E.g. The supported listing methods or the inventory allocation rules. The rules differ by the markets they serve.
**Note**: Applicable only for global sellers.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202507/global_listing_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^listing_methods | []string | ["GLOBAL_PUBLISHING"] | The methods at which sellers can list products in this shop. |
| Possible values: |  |  |  |

* GLOBAL_PUBLISHING: Create a global product, then publish it to target local markets.
* LOCAL_REPLICATION: Create local product, then replicate it to other target local markets. |
   ^inventory_rules |[]object | |A list of inventory allocation rules for all warehouses linked to the shop. |
   ^^local_warehouse_id |string |7068517275539719942 |The warehouse ID associated with the shop. |
   ^^allocation_mode |string |SHARED |The inventory allocation mode used for this warehouse in the local market.
   `SHARED` – Inventory is pooled across all covered markets. An inventory deduction in one market reflects across all.
   `DYNAMIC` – Inventory is divided proportionally among covered markets. An inventory deduction in one market affects only that market.
   `MANUAL` – Inventory is configured independently by sellers for each market. An inventory deduction in one market affects only that market. |
   ^^associated_warehouses |[]object | |A list of associated warehouses whose inventory is shared with or dynamically allocated from this warehouse. Each item identifies a warehouse and its region.
   **Note**: Applicable only when `allocation_mode` is `SHARED` or `DYNAMIC`. |
   ^^^warehouse_id |string |7068517275539718842 |The associated warehouse ID. |
   ^^^region |string |DE |The country where the warehouse is located. |

# 响应示例
```json
{"code":0,"data":{"listing_methods":["GLOBAL_PUBLISHING"],"inventory_rules":[{"local_warehouse_id":"7068517275539719942","allocation_mode":"SHARED","associated_warehouses":[{"warehouse_id":"7068517275539718842","region":"DE"}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

