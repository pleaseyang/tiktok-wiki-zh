# 库存搜索

# 路径：/product/202309/inventory/search
# 方法：[POST]
# 功能描述
获取多个商品或 SKU 的库存信息。
**注意**：

* 如果同时传入 `sku_ids` 和 `product_ids`，则以 `sku_ids` 为准，`product_ids` 将被忽略。
* 传入商品 ID 可返回指定商品下所有 SKU 的库存信息。
* 传入 SKU ID 将返回指定 SKU 的库存信息。


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
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_ids | []string | N | ["1729592969712207008"] | 用于查询库存信息的商品 ID 列表。 |
| Max IDs: 100 |  |  |  |  |
| sku_ids | []string | N | ["1729388324987897824"] |  |
| 用于查询库存信息的 SKU ID 列表。 |  |  |  |  |
| Max IDs: 600 |  |  |  |  |
**注意**: 如果同时传入 `sku_ids` 和 `product_ids`，将以 `sku_ids` 为准。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/inventory/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":["1729592969712207008"],"sku_ids":["1729388324987897824"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^inventory | []object |  | 所请求商品或 SKU 的库存信息。 |
| ^^product_id | string | 1729592969712207008 | 所请求商品的 ID。 |
| ^^skus | []object |  | 所请求的 SKU 列表。 |
| ^^^id | string | 1729388324987897824 | TikTok Shop 生成的 SKU ID。 |
| ^^^seller_sku | string | Color-Red-XM01 | 用于管理 SKU 的内部代码/名称，对买家不可见。 |
| ^^^total_available_quantity | int | 100 | 所有仓库中可订购的总件数。 |
| 它是所有仓库中 `warehouse_inventory.available_quantity` 取值的总和。 |  |  |  |
|  |  |  |  |
| ^^^total_committed_quantity | int | 10 | 所有仓库中由现有客户订单预留（因此不可用于订购）的商品件数总和。 |
| 它是所有仓库中 `warehouse_inventory.committed_quantity` 取值的总和。 |  |  |  |
| ^^^warehouse_inventory | []object |  | SKU 仓库库存信息。 |
| ^^^^warehouse_id | string | 7054915283043174149 | SKU 存放仓库的 ID。 |
| 从 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6) 获取仓库详情。 |  |  |  |
| ^^^^available_quantity | int | 100 | 此仓库中可订购的总件数。 |
| 这等同于 [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) 中返回的 `inventory.quantity` 取值。 |  |  |  |
| ^^^^committed_quantity | int | 10 | 此仓库中由现有客户订单预留（因此不可用于订购）的商品件数总和。 |
| ^^^total_available_inventory_distribution | object |  | 该 SKU 可用总库存在不同渠道间的分布。 |
| ^^^^campaign_inventory | []object |  | 分配给特定活动的库存。 |
| ^^^^^quantity | int | 30 | 已分配的件数。 |
| ^^^^^campaign_name | string | Big Sale | 关联活动的名称。 |
| ^^^^creator_inventory | []object |  | 分配给 TikTok 达人的库存。 |
| ^^^^^quantity | int | 20 | 已分配的件数。 |
| ^^^^^creator_name | string | py001 | 关联的 TikTok 达人名称。 |
| ^^^^in_shop_inventory | object |  | 扣除分配给活动和达人的库存后，店铺可用的剩余库存。 |
| ^^^^^quantity | int | 50 | 已分配的件数。 |
# 响应示例
```json
{"code":0,"data":{"inventory":[{"product_id":"1729592969712207008","skus":[{"id":"1729388324987897824","seller_sku":"Color-Red-XM01","total_available_quantity":100,"total_committed_quantity":10,"warehouse_inventory":[{"warehouse_id":"7054915283043174149","available_quantity":100,"committed_quantity":10}],"total_available_inventory_distribution":{"campaign_inventory":[{"quantity":30,"campaign_name":"Big Sale"}],"creator_inventory":[{"quantity":20,"creator_name":"py001"}],"in_shop_inventory":{"quantity":50}}}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12019008 | Product id is invalid |
| 12019015 | The number of SKU exceed the limit |
| 12019022 | SKU 必须包含有效仓库。 |
| 12019112 | seller id is invalid |
| 12019114 | 卖家无权限 |
| 12019120 | 提供的商品 ID 数量超过限制。 |

