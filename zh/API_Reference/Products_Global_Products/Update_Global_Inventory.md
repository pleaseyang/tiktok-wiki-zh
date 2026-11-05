# 更新全球库存

# Path: /product/202309/global_products/{global_product_id}/inventory/update
# Method: [POST]
# 功能描述
Update the inventory of a global product in `DRAFT`, `UNPUBLISHED`, or `PUBLISHED` status. You must have access to the Multi-Warehouse feature.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_product_id | string | Y | 1729592969712207013 | The global product ID to be updated. |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| global_skus | []object | Y |  | A non-empty list of global SKUs whose inventory quantities you want to set. |
| ^id | string | Y | 1729592969712207013 | The global SKU ID in TikTok Shop. |
| ^inventory | []object | Y |  | The inventory quantities to set for this global SKU, with one entry for each global warehouse to update. Existing global warehouses omitted from this array retain their current quantities. |
| ^^global_warehouse_id | string | Y | 7068517275539719942 | The ID of the global warehouse where the SKU is stored. The warehouse must be enabled and belong to this shop or seller. Retrieve this value from [Get Global Product](6509e2b0bace3e02b7490c96) or [Get Global Seller Warehouse](650aa3f0defece02be6e5ffb). |
| ^^quantity | int | Y | 999 | The number of inventory units to set for this global SKU in the specified global warehouse. Must be 0 or greater. |
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
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
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
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12019113 | product status is invalid |
| 12019114 | Seller has no permission |
| 12019117 | Missing variations (sales attributes). When there are multiple SKUs in a product, each SKU must include variation (sales attribute) details that explain how it is different from other SKUs in the product. |
| 12019150 | The product ID does not exist. |
| 12052048 | You cannot edit the specified product(s) as it isn't listed in your account or shop. |
| 12052055 | The SKU inventory quantity for the warehouse must be within allowed limits. |
| 12052094 | No multiple warehouse permission |
| 12052142 | no permission of multi global warehouse |
| 12052143 | sku warehouse must equal |
| 12052145 | activity warehouse not allowed to be deleted |
| 12052146 | The specified inventory quantity is too low. It must be greater than the locked quantity (e.g. for committed orders, campaigns, creators) to ensure a non-negative available stock. |
| 12052260 | The product ID does not exist |
| 12052379 | the cover region of share warehouse can not cover the the product region |
| 12052447 | You still have stock reserved for campaigns in your Chinese warehouse(s), so you cannot add an overseas warehouse yet. If you have an overseas warehouse, you must use it to fulfill orders for your &lbrace;&lbrace;country&rbrace;&rbrace; shop. |
| 12052448 | Local fulfillment is required for &lbrace;&lbrace;country&rbrace;&rbrace; shop. You must have at least one &lbrace;&lbrace;country&rbrace;&rbrace; overseas warehouse for it. |
| 12052530 | The warehouse ' &lbrace;&lbrace;warehouse ID&rbrace;&rbrace; ' does not belong to this shop/seller. |
| 12052531 | The warehouse is disabled. |
| 12052533 | Removal, addition, and change of warehouses are not permitted. Please specify the original warehouses for the SKUs. |
| 12052556 | The SKU id not exist. |
| 12052700 | The seller is inactive. |
| 12052902 | The SKU list is empty. Either omit the list entirely, or provide all required details. |

