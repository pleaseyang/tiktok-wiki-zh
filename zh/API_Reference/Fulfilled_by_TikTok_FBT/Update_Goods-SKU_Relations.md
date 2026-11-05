# 更新 Goods-SKU 关联关系

# Path: /fbt/202603/goods/update_goods_sku_relation
# Method: [POST]
# 功能描述
绑定或解绑 TikTok Shop SKU 与 FBT 商品的关联关系。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| operate_goods_sku_relation_list | []object | Y |  | 需要绑定或解绑的商品与 SKU 关联列表。 |
| ^tts_goods_id | string | Y | 334556677 | Fulfilled by TikTok 系统生成的商品标识符 |
| ^tts_sku_ids | []string | Y | ["723456789012345678"] | 需要绑定到或从指定 FBT 商品解绑的 TikTok Shop SKU 标识符。 |
| operation_type | string | Y | BIND | 商品-SKU 关联的操作类型。可能的值：BIND（将列出的 SKU 绑定到商品）；UN_BIND（将列出的 SKU 从商品解绑）。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202603/goods/update_goods_sku_relation?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"operate_goods_sku_relation_list":[{"tts_goods_id":"334556677","tts_sku_ids":["723456789012345678"]}],"operation_type":"BIND"}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^operate_goods_sku_relation_info | object |  | 请求的 TikTok Shop SKU 与 FBT 商品绑定或解绑的结果。 |
| ^^operate_result_list | []object |  | 商品-SKU 关联结果，包括商品 ID、SKU ID、成功状态和失败原因（如适用）。 |
| ^^^tts_goods_id | string | 9988776655 | Fulfilled by TikTok 系统生成的商品标识符 |
| ^^^tts_sku_id | string | 723456789012345678 | TikTok Shop 系统生成的 SKU 标识符 |
| ^^^is_success | bool | false | 商品-SKU 关联操作是否成功。 |
| ^^^fail_reason | string | SKU does not exist. | 商品-SKU 关联操作失败的原因。 |
# 响应示例
```json
{"code":0,"data":{"operate_goods_sku_relation_info":{"operate_result_list":[{"tts_goods_id":"9988776655","tts_sku_id":"723456789012345678","is_success":false,"fail_reason":"SKU does not exist."}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

