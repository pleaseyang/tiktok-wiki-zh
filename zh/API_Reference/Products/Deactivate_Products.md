# 下架商品

# 路径：/product/202309/products/deactivate
# 方法：[POST]
# 功能描述
下架处于 `Activate` 状态的商品并对买家隐藏。下架后状态变为 `Seller_deactivated`。
当商品出现某些问题（例如缺货）时，可以下架该商品并暂时对买家隐藏。问题解决后，可使用 [Activate Product API](https://partner.tiktokshop.com/docv2/page/650306ff5a12ff0294eab4a9) 重新激活该商品。

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
| product_ids | []string | Y | ["1729592969712207008"] | 要下架的商品 ID。 |
| 最大 ID 数量：20。 |  |  |  |  |
| listing_platforms | []string | N | ["TIKTOK_SHOP", "TOKOPEDIA"] | 将下架该商品的上架平台。 |
| 可能的值： |  |  |  |  |

* TOKOPEDIA
* TIKTOK_SHOP
   默认值：TIKTOK_SHOP

仅适用于从 Tokopedia 迁移的卖家。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/deactivate?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":["1729592969712207008"],"listing_platforms":["TIKTOK_SHOP","TOKOPEDIA"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 未能下架的各商品的错误。即使顶层 `code` 为 `0`，也请检查此列表。 |
| ^^code | int | 12052048 | 主要错误码。 |
| ^^message | string | 您无法编辑其他卖家的商品 | 主要错误消息。 |
|  |  |  |  |
| ^^detail | object |  | 主要错误的详细信息。 |
| ^^^product_id | string | 1729382588639839583 | 未能下架的商品 ID。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":12052048,"message":"You can't edit other sellers' products","detail":{"product_id":"1729382588639839583"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019120 | 提供的商品 ID 数量超过限制。 |
| 12052032 | 商品不存在 |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052330 | 商品不支持在指定销售平台上架 |
| 12052332 | 店铺集成期间卖家中心被锁定，仅允许编辑库存和价格 |
| 12052371 | Auction product is bidding when it is not supported to change product info |
| 12052700 | 卖家不活跃。 |
| 12052703 | 卖家税号无效 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |

