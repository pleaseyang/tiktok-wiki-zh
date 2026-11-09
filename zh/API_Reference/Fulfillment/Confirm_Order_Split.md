# 确认订单拆分

# 路径：/fulfillment/202309/orders/{order_id}/split
# 方法：[POST]
# 功能描述
使用此 API 确认订单拆分。支持的拆分级别因地区而异：

* 部分地区支持商品级别拆分（拆分同一 SKU 的单个单位）。
* 其他地区仅支持全部单位拆分（将不同 SKU 拆分到单独的 package 中）。

以下是两个支持的拆分示例：

* **情况 1：全部单位拆分**，适用于 BR、SEA、MX（本地卖家）的订单
   将一个买家订单中 SKU A 数量 2 和 SKU B 数量 1 拆分为两个独立的 package：
   * **Package 1**：SKU A 的所有单位
   * **Package 2**：SKU B 的所有单位
* **情况 2：商品级别拆分**，适用于 EU、JP、MX（全球卖家）、UK、US 的订单
   将相同的订单内容拆分为三个独立的 package：
   * **Package 1**：SKU A 的 1 个单位
   * **Package 2**：SKU A 的 1 个单位
   * **Package 3**：SKU B 的 1 个单位


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 556643423444 | TikTok Shop 订单 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| splittable_groups | []object | Y |  | 要拆分的订单行项目组。每个成功拆分的组将作为单独的 package 返回。 |
| ^id | string | Y | 123 | 开发者定义的此拆分组的标识符。响应在 `splittable_group_id` 中返回相同的值，以将组与其新创建的 package 关联。 |
| ^order_line_item_ids | []string | Y | ["57646237751283022", "576462377512830223"] | 需要拆分到此组的订单行项目 ID。 |
| splittable_groups_v2 | []object | N |  | 此新参数与之前的 splittable groups 字段完全向后兼容，此外还支持 bundle 订单拆分，请相应使用子项。 |
| ^id | string | N | 123 | 开发者定义的此拆分组的标识符。响应在 `splittable_group_id` 中返回相同的值，以将组与其新创建的 package 关联。 |
| ^order_line_list | []object | N |  | 此新参数与之前的 order_line_items_ids 字段完全向后兼容，此外还支持 bundle 订单拆分，请相应使用子项。 |
| ^^order_line_id | string | N | 57646237751283022 | 对应的订单行 ID。 |
| ^^sub_item_id | string | N | 57646237751283022 | bundle 商品内的子订单行 ID。 |

* bundle 商品必填。
* 非 bundle 商品不必填。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/orders/556643423444/split?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"splittable_groups":[{"id":"123","order_line_item_ids":["57646237751283022","576462377512830223"]}],"splittable_groups_v2":[{"id":"123","order_line_list":[{"order_line_id":"57646237751283022","sub_item_id":"57646237751283022"}]}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^packages | []object |  | 拆分创建的 package。每个返回的 package 包含请求组标识符 `splittable_group_id` 及其新的 package ID `id`。 |
| ^^splittable_group_id | string | 123 | 请求中 `splittable_groups` 或 `splittable_groups_v2` 对应组的开发者定义的 `id`。 |
| ^^id | string | 223362377512830222 | 拆分成功后的 package ID。使用此新的 package ID 调用 [Ship Package API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1?external_id=650aa4f1defece02be6e7cb1) 来发货。 |
# 响应示例
```json
{"code":0,"data":{"packages":[{"splittable_group_id":"123","id":"223362377512830222"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 21001028 | 订单正在处理中。请稍后重试。 |
| 21011005 | 传递了无效的请求参数。请检查您是否具有正确的参数类型和格式。 |
| 21011035 | 不允许拆分订单 |

