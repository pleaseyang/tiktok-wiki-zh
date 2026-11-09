# 搜索 FBT Inventory 记录

# 路径：/fbt/202410/inventory_records/search
# 方法：[POST]
# 功能描述
此 API 用于检索仓库级别商品的详细 inventory 变更记录。

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
| 分页限制为前 20,000 条结果。 |  |  |  |  |
| page_token | string | N | cGFnZV9udW1iZXI9Mg== | 分页 page token。第一页应为空。 |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | string | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| goods_ids | []string | N | ["256080616234","2231616264"] | 要搜索的 Fulfilled by TikTok 系统生成的商品 ID。最多 100 个 ID。如果提供了 ID，API 仅返回这些商品的 inventory 记录；如果省略，则返回所有具有非零 inventory 的商品的 inventory 记录。 |
| fbt_warehouse_ids | []string | N | ["7232382932030232"] | 要搜索的 Fulfilled by TikTok 仓库的 ID。最多 100 个 ID。API 仅搜索卖家可用的仓库：如果提供了 ID，搜索仅限于匹配的 ID；如果省略，则搜索所有可用的仓库。 |
| create_time_ge | int | N | 1293013251 | 筛选 inventory 记录创建时间，仅显示在指定日期和时间或之后创建的记录。以秒为单位的 Unix 时间戳。`create_time_ge` 默认为 0。 |
| create_time_le | int | N | 1393013251 | 筛选 inventory 记录创建时间，仅显示在指定日期和时间或之前创建的记录。以秒为单位的 Unix 时间戳。`create_time_le` 默认为当前时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202410/inventory_records/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=50&page_token=cGFnZV9udW1iZXI9Mg==
```

**Body**
```json
{"goods_ids":["256080616234","2231616264"],"fbt_warehouse_ids":["7232382932030232"],"create_time_ge":1293013251,"create_time_le":1393013251}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^inventory_records | []object |  | inventory 记录信息列表。 |
| ^^goods | object |  | 用于在 Fulfilled by TikTok 网络中跟踪商品和 SKU 的引用。 |
| ^^^id | string | 12324323 | Fulfilled by TikTok 系统生成的商品标识符。 |
| ^^^reference_code | string | water01 | 卖家定义的商品标识符。 |
| ^^^name | string | 100ml water | 商品名称。 |
| ^^fbt_warehouse_id | string | 7232392932323 | Fulfilled by TikTok 系统生成的仓库标识符。 |
| ^^order | object |  | 触发当前 inventory 变更的订单信息。 |
| ^^^id | string | OBF8932302030203 | Fulfilled by TikTok 系统生成的订单标识符。 |
| ^^^type | string | INBOUND_ORDER | 订单类型。 |
| 可能的值： |  |  |  |

* INBOUND_ORDER
* RETURN_TO_SUPPLIER_ORDER
* DISPOSAL
* INVENTORY_STATUS_ADJUSTMENT_ORDER
* CONSIGN_ORDER
* INVENTORY_COUNT_ORDER
* FAILED_DELIVERY
* CUSTOMER_RETURN
* INVENTORY_QUANTITY_ADJUSTMENT_ORDER
* INVENTORY_TRANSFER_ORDER |
   ^^create_time |int |1212139230 |inventory 记录创建的时间，以秒为单位的 Unix 时间戳。 |
   ^^inventory_goods_type |string |NORMAL |当前 inventory 记录中商品的类型。
   可能的值：
* NORMAL
* DEFECTIVE |
   ^^initial_on_hand_quantity |int |10 |当前 inventory 变更之前 physically 在 Fulfilled by TikTok 仓库中的商品单位数量，不包括在途的。 |
   ^^final_on_hand_quantity |int |12 |当前 inventory 变更之后 physically 在 Fulfilled by TikTok 仓库中的商品单位数量，不包括在途的。 |
   ^^changed_quantity |int |2 |单位数量的变更计算为 `final_on_hand_quantity` - `initial_on_hand_quantity`。 |
   ^next_page_token |string |cGFnZV9udW1iZXI9Mg== |用于检索分页结果集下一页的不透明 token。如果当前响应未返回所有结果，请在请求的 `page_token` 参数中提供此值。 |
   ^total_count |int |22113 |搜索结果的总数。 |

# 响应示例
```json
{"code":0,"data":{"inventory_records":[{"goods":{"id":"12324323","reference_code":"water01","name":"100ml water"},"fbt_warehouse_id":"7232392932323","order":{"id":"OBF8932302030203","type":"INBOUND_ORDER"},"create_time":1212139230,"inventory_goods_type":"NORMAL","initial_on_hand_quantity":10,"final_on_hand_quantity":12,"changed_quantity":2}],"next_page_token":"cGFnZV9udW1iZXI9Mg==","total_count":22113},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

