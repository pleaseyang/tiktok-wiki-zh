# 更新库存

# 路径：/product/202309/products/{product_id}/inventory/update
# 方法：[POST]
# 功能描述
更新属于某商品的 SKU 的库存数量。该商品必须处于 `DRAFT`、`PENDING`、`FAILED`、`ACTIVATE` 或 `SELLER_DEACTIVATED` 状态。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 1729382561353664372 | TikTok Shop 生成的商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| skus | []object | Y |  | 用于标识商品不同变体的 SKU（库存单位）列表。 |
| ^id | string | Y | 1729592969712207013 | TikTok Shop 生成的 SKU ID。一个商品可包含多个 SKU ID。 |
**注意**：

* SKU ID 必须属于未处于 `FREEZE` 或 `DELETED` 状态的商品。
* 如果要更新多个 SKU, 所有 SKU ID 必须属于同一商品。 |
   ^inventory |[]object |Y | |SKU 库存信息。
   **注意**： 您必须包含分配给此 SKU 的所有仓库 ID，以及各自对应的数量。不得遗漏任何仓库，也不得添加不相关的仓库。 |
   ^^warehouse_id |string |N |7068517275539719942 |SKU 存放仓库的 ID。 Retrieve this value from the [Get Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda)。

**注意**: 如果只有 1 个仓库则可选. 否则，请提供此 ID。 |
^^quantity |int |Y |999 |仓库中可用的 SKU 总数量。
有效范围：[1, 99,999]
注意：此数量特指可以立即发货的有库存的库存量。 |
^^backorder_quantity |int |N |888 |当现货库存售罄时，`backorder_quantity` 会自动转换为 `quantity`。其履约遵循指定的 `handling_time`。
**注意**：

* 请同时提供 `backorder_quantity` 和 `handling_time`。
* 如果省略 `backorder_quantity`，现有缺货预订数量保持不变。 |
   ^^handling_time |int |N |5 |The estimated number of working days needed for a backorder to be shipped. Provide `handling_time` and `backorder_quantity` together. All warehouses for the same SKU must use the same `handling_time`. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/1729382561353664372/inventory/update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"skus":[{"id":"1729592969712207013","inventory":[{"warehouse_id":"7068517275539719942","quantity":999,"backorder_quantity":888,"handling_time":5}]}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 单个 SKU 与仓库组合的库存更新错误。即使顶层响应成功，当个别更新失败时仍可能包含此列表，因此在将所有更新视为成功之前请检查此列表。 |
| ^^code | int | 12052990 | 主要错误码。 |
| ^^message | string | Batch update inventory error. | 主要错误消息。 |
| ^^detail | object |  | 主要错误的详细信息。 |
| ^^^sku_id | string | 1729592969712207013 | 发生错误的 SKU 的 ID。 |
| ^^^extra_errors | []object |  | 与主错误相关的次要错误或问题列表。 |
| ^^^^warehouse_id | string | 7068517275539719942 | 发生错误的仓库的 ID。 |
| ^^^^code | int | 12052097 | 次要错误码。 |
| ^^^^message | string | The warehouse does not exist | 次要错误消息。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":12052990,"message":"Batch update inventory error.","detail":{"sku_id":"1729592969712207013","extra_errors":[{"warehouse_id":"7068517275539719942","code":12052097,"message":"The warehouse does not exist"}]&rbrace;&rbrace;]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019022 | SKU 必须包含有效仓库。 |
| 12019024 | stock count is invalid |
| 12019028 | Multiple warehouses detected. Include all warehouse IDs and the corresponding details and try again. |
| 12052031 | Invalid product ID(s) found |
| 12052032 | 商品不存在 |
| 12052036 | The SKU ID is necessary |
| 12052037 | 无法更新库存。可能原因: |

* 库存自动分配，无法手动修改
* 提供的仓库 ID 不正确
* 缺少仓库 ID（必须包含存放该商品的所有仓库） |
   12052048 |您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
   12052050 |A single product cannot have more than 100 different SKUs |
   12052055 |The SKU inventory quantity for the warehouse must be within allowed limits. |
   12052094 |No multiple warehouse permission |
   12052096 |Unable to update the price for SKUs with no warehouse. Assign a warehouse and try again. |
   12052097 |The warehouse does not exist |
   12052115 |seller has no warehouse |
   12052141 |please edit stock from global |
   12052160 |sku count must be one and disable variables |
   12052207 |receipt brand not support warehouse |
   12052260 |商品 ID 不存在 |
   12052308 |There's an ongoing appeal. If you wish to edit product details, please revoke the appeal first. |
   12052364 |The warehouse is unavailable because this product cannot be shipped to the target market from this warehouse. |
   12052371 |Auction product is bidding when it is not supported to change product info |
   12052393 |Product locked for Promotion and stock can't be updated below current stock |
   12052403 |The warehouse does not support fulfillment for the current shop. |
   12052465 |warehouse is unavailable for eu gpr product |
   12052530 |The warehouse ' &lbrace;&lbrace;warehouse ID&rbrace;&rbrace; ' does not belong to this shop/seller. |
   12052531 |The warehouse is disabled. |
   12052532 |该仓库非配送仓库 |
   12052533 |不允许移除、新增或更改仓库。请为 SKU 指定原始仓库。 |
   12052535 |Couldn't publish this product as you haven't set the return warehouse for your shop. Add the return warehouse information on TikTok Shop Seller Center first and try again. |
   12052553 |Sku id duplicate |
   12052556 |The SKU id not exist. |
   12052700 |卖家不活跃。 |
   12052703 |Invalid seller tax number |
   12052704 |卖家 ID 不存在 |
   12052849 |You don't have the permission to operate combo. |
   12052850 |The stock of combo does not support being edited. |
   36009003 |内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
   12052901 |商品当前状态不支持此操作。请更改商品状态后重试。 |
   12052902 |The SKU list is empty. Either omit the list entirely, or provide all required details. |
   12052921 |Couldn't edit the inventory quantity because this product shares the inventory with the source shop |
   12052990 |检查失败。 |


