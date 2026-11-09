# 搜索 FBT Inventory

# 路径：/fbt/202408/inventory/search
# 方法：[POST]
# 功能描述
此 API 用于检索商品和已匹配 SKU 的详细 inventory 信息，包括仓库级别的可售 inventory、预留 inventory、不可售 inventory 和在途 inventory。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| page_size | int | Y | 50 | 每页返回的结果数量。 |
| 有效范围：[1-100]。 |  |  |  |  |
| page_token | string | N | cGFnZV9udW1iZXI9Mg== | 分页 page token。第一页应为空。 |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| goods_ids | []string | N | ["256080616234","2231616264"] | Fulfilled by TikTok 系统生成的商品标识符。每次请求最多 100 个商品 ID。如果指定，仅返回这些商品的 inventory 信息。如果 `goods_ids` 和 `sku_ids` 都省略，则返回所有具有非零 inventory 的商品。 |
不要在同一请求中同时提供 `goods_ids` 和 `sku_ids`。两个字段均可省略。 |
fbt_warehouse_ids |[]string |N |["7232382932030232"] |Fulfilled by TikTok 系统生成的仓库标识符。指定最多 100 个仓库 ID，仅返回匹配这些 ID 的已订阅仓库的 inventory 记录。如果省略或为空，则返回卖家订阅的所有仓库的 inventory 记录。 |
sku_ids |[]string |N |["256080616234"] |TikTok Shop SKU 标识符，用于选择与这些 SKU 匹配的商品。每次请求最多 100 个 SKU ID。不要在同一请求中同时提供 `sku_ids` 和 `goods_ids`；两个字段都可以省略。对于每个匹配的商品记录，返回的 `goods.skus` 列表包含为该商品记录提供的 SKU inventory，不限于请求的 SKU ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202408/inventory/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=50&page_token=cGFnZV9udW1iZXI9Mg==
```

**Body**
```json
{"goods_ids":["256080616234","2231616264"],"fbt_warehouse_ids":["7232382932030232"],"sku_ids":["256080616234"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | cGFnZV9udW1iZXI9Mg== | 用于检索分页结果集下一页的不透明 token。在下一个请求的 `page_token` 参数中提供此值。空的 `next_page_token` 表示没有更多页面。 |
| ^total_count | int | 22113 | 匹配已应用筛选条件的仓库商品 inventory 记录总数。 |
| ^inventory | []object |  | inventory 记录列表。每一项代表一个 Fulfilled by TikTok 仓库中的一个商品，可以包含关联的 SKU inventory 细分。 |
| ^^goods | object |  | 用于在 Fulfilled by TikTok 网络中跟踪商品和 SKU 的引用。 |
| ^^^id | string | 69167899745030 | Fulfilled by TikTok 系统生成的商品标识符。 |
| ^^^reference_code | string | water01 | 卖家定义的商品标识符，通常用于引用卖家其他订单管理系统中的 ID。 |
| ^^^name | string | 100ml water | 商品名称。 |
| ^^^skus | []object |  | 与当前 Fulfilled by TikTok 商品匹配的 Stock Keeping Units（SKU）的 inventory 信息列表。 |
| ^^^^id | string | 73243612345 | TikTok Shop 系统生成的 SKU 标识符。 |
| ^^^^on_hand_detail | object |  | SKU 在仓库中的实物 inventory 信息，不包括在途或损坏的。 |
| ^^^^^total_quantity | int | 20 | 当前 SKU 的总单位数，由 `available_quantity` 和 `reserved_quantity` 组成。 |
| ^^^^^available_quantity | int | 5 | 可供销售的单位数量。 |
| 注意： |  |  |  |
| 此数量不包括预留单位。 |  |  |  |
| ^^^^^reserved_quantity | int | 15 | 为客户订单预留或退回供应商货件的单位数量。 |
| ^^fbt_warehouse_id | string | 7232382932030232 | Fulfilled by TikTok 系统生成的仓库标识符。 |
| ^^in_transit_quantity | int | 10 | 当前在途至仓库的商品单位数量。inventory 包括 inbound 补货、客户退货、配送失败退货等。 |
| ^^on_hand_detail | object |  | 商品的当前仓库内 inventory 详情。 |
| ^^^total_quantity | int | 20 | 商品在 Fulfilled by TikTok 仓库的总在手数量，不包括在途 inventory。 |
| ^^^available_quantity | int | 5 | 可供销售的单位数量。 |
| 注意： |  |  |  |
| 此数量不包括预留单位。 |  |  |  |
| ^^^reserved_quantity | int | 15 | 为客户订单预留或退回供应商货件的单位数量。 |
| ^^^unfulfillable_quantity | int | 0 | 仓库中缺陷单位的数量。 |
# 响应示例
```json
{"code":0,"data":{"next_page_token":"cGFnZV9udW1iZXI9Mg==","total_count":22113,"inventory":[{"goods":{"id":"69167899745030","reference_code":"water01","name":"100ml water","skus":[{"id":"73243612345","on_hand_detail":{"total_quantity":20,"available_quantity":5,"reserved_quantity":15}}]},"fbt_warehouse_id":"7232382932030232","in_transit_quantity":10,"on_hand_detail":{"total_quantity":20,"available_quantity":5,"reserved_quantity":15,"unfulfillable_quantity":0}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

