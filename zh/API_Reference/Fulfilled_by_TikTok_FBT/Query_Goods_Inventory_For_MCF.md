# 查询 MCF 商品 Inventory

# 路径：/fbt/202601/mcf/goods/inventory/search
# 方法：[POST]
# 功能描述
查询 MCF 商品的可用 inventory。使用此 API 检索指定 Fulfilled by TikTok 商品 ID 的可用数量。

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
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| goods | []object | Y |  | 要查询的商品。数组必须包含 1 到 50 个条目。 |
| ^goods_id | string | Y | 69167899745030 | Fulfilled by TikTok 商品 ID。值必须表示正整数。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202601/mcf/goods/inventory/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"goods":[{"goods_id":"69167899745030"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^goods_inventory_list | []object |  | 所请求商品的库存条目。对于 MCF，仅返回与店铺地区卖家关联且具有库存组结果的商品。没有库存组结果的请求商品 ID 会被省略；接口不会添加 `available_qty` 设为 `0` 的条目。当所请求商品均无库存组结果时，列表为空。每条条目代表一个商品与库存组结果，因此当同一 `goods_id` 具有多个库存组时，可能出现在多条条目中。请求的商品 ID 不会去重；重复 `goods_id` 可能重复相同的库存组条目。每个 `goods_id` 仅包含一次，且不要按列表位置将响应条目与请求条目对齐。 |
| ^^goods_id | string | 69167899745030 | 由 Fulfilled by TikTok 系统生成的货品标识符。 |
| ^^available_qty | int | 10 | 货品的可用库存 |
# 响应示例
```json
{"code":0,"data":{"goods_inventory_list":[{"goods_id":"69167899745030","available_qty":10}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

