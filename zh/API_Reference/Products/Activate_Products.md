# 激活商品

# 路径：/product/202309/products/activate
# 方法：[POST]
# 功能描述
激活处于 `Seller_deactivated` 或 `Platform_deactivated` 状态的隐藏商品，并在 TikTok Shop 目录中展示它们。
提交激活请求后，商品将被发送到 TikTok Shop 进行审核，其状态将变为 `Pending`。如果商品通过审核，其状态将变回 `Activate`。您可以使用[产品状态变更 webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) 来监控审核状态。

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
| product_ids | []string | Y | ["1729592969712207008", "1729592969712207021"] | 要激活的商品 ID。 |
| 最大 ID 数量：20 |  |  |  |  |
| listing_platforms | []string | N | ["TIKTOK_SHOP"] | 商品将被激活的上架平台。 |
| 可能的值： |  |  |  |  |

* TOKOPEDIA
* TIKTOK_SHOP
   默认值：TIKTOK_SHOP

仅适用于从 Tokopedia 迁移的卖家。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/activate?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_ids":["1729592969712207008","1729592969712207021"],"listing_platforms":["TIKTOK_SHOP"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 无法激活的单个商品的错误。即使顶级 `code` is `0`。 |
| ^^code | int | 12052990 | 主要错误码。 |
| ^^message | string | 批量激活业务错误。 | 主要错误消息。 |
| ^^detail | object |  | 主要错误的详细信息。 |
| ^^^product_id | string | 1729382588639839583 | 无法激活的商品 ID。 |
| ^^^extra_errors | []object |  | 与主要错误相关的进一步嵌套错误或问题列表。 |
| ^^^^code | int | 12052048 | 次要错误码。 |
| ^^^^message | string | 您无法编辑其他卖家的商品 | 次要错误消息。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":12052990,"message":"Batch activate business error.","detail":{"product_id":"1729382588639839583","extra_errors":[{"code":12052048,"message":"You can't edit other sellers' products"}]}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019022 | SKU 必须包含有效仓库。 |
| 12019120 | 提供的商品 ID 数量超过限制。 |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052093 | 超过卖家的商品上架限制。 |
| 12052330 | 商品不支持在指定销售平台上架 |
| 12052332 | 店铺集成期间卖家中心被锁定，仅允许编辑库存和价格 |
| 12052700 | 卖家不活跃。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |
| 12052990 | 检查失败。 |

