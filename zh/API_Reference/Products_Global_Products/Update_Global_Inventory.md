# 更新全球库存

# 路径：/product/202309/global_products/{global_product_id}/inventory/update
# 方法：[POST]
# 功能描述
更新处于 `DRAFT`、`UNPUBLISHED` 或 `PUBLISHED` 状态的全球商品的库存。您必须拥有多仓库功能的使用权限。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_product_id | string | Y | 1729592969712207013 | 要更新的全球商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_skus | []object | Y |  | 要设置库存数量的全球 SKU 的非空列表。 |
| ^id | string | Y | 1729592969712207013 | TikTok Shop 中的全球 SKU ID。 |
| ^inventory | []object | Y |  | 为此全球 SKU 设置的库存数量，每个待更新的全球仓库对应一个条目。此数组中省略的现有全球仓库保留其当前数量。 |
| ^^global_warehouse_id | string | Y | 7068517275539719942 | 存储该 SKU 的全球仓库的 ID。该仓库必须已启用且属于此店铺或卖家。可从 [Get Global Product](6509e2b0bace3e02b7490c96) 或 [Get Global Seller Warehouse](650aa3f0defece02be6e5ffb) 获取此值。 |
| ^^quantity | int | Y | 999 | 要在指定全球仓库中为该全球 SKU 设置的库存数量。必须大于或等于 0。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_products/1729592969712207013/inventory/update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"global_skus":[{"id":"1729592969712207013","inventory":[{"global_warehouse_id":"7068517275539719942","quantity":999}]}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12019113 | product status is invalid |
| 12019114 | 卖家无权限 |
| 12019117 | Missing variations (sales attributes). When there are multiple SKUs in a product, each SKU must include variation (sales attribute) details that explain how it is different from other SKUs in the product. |
| 12019150 | 商品 ID 不存在。 |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052055 | The SKU inventory quantity for the warehouse must be within allowed limits. |
| 12052094 | No multiple warehouse permission |
| 12052142 | no permission of multi global warehouse |
| 12052143 | sku warehouse must equal |
| 12052145 | activity warehouse not allowed to be deleted |
| 12052146 | The specified inventory quantity is too low. It must be greater than the locked quantity (e.g. for committed orders, campaigns, creators) to ensure a non-negative available stock. |
| 12052260 | 商品 ID 不存在 |
| 12052379 | the cover region of share warehouse can not cover the the product region |
| 12052447 | 你在中国仓库中仍有为活动预留的库存，因此暂时无法添加海外仓库。如果你已有海外仓库，必须使用它来为你的 &lbrace;&lbrace;country&rbrace;&rbrace; 店铺履约订单。 |
| 12052448 | &lbrace;&lbrace;country&rbrace;&rbrace; 店铺要求本地履约。为此，您必须至少拥有一个 &lbrace;&lbrace;country&rbrace;&rbrace; 海外仓库。 |
| 12052530 | The warehouse ' &lbrace;&lbrace;warehouse ID&rbrace;&rbrace; ' does not belong to this shop/seller. |
| 12052531 | The warehouse is disabled. |
| 12052533 | 不允许仓库的移除，添加，和更改. 请为 SKU 指定原始仓库。 |
| 12052556 | The SKU id not exist. |
| 12052700 | 卖家不活跃。 |
| 12052902 | The SKU list is empty. Either omit the list entirely, or provide all required details. |

