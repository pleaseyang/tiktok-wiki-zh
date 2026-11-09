# 更新库存操作设置

# 路径：/product/202608/inventory/operation/settings
# 方法：[POST]
# 功能描述
在单次请求中为 1 至 500 个 SKU 配置自动补货行为。对于卖家自履约订单，此设置控制为已取消订单预留的库存是否退回该 SKU 的可用库存。

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
| seller_id | string | Y | 124129082343241 | 标识正在修改其设置的卖家。 |
| sku_ids | []string | N | ["124148921741214"] | 指定 SKU ID 的列表。每批最多 500 个 SKU。 |
| stock_operation_setting | object | N |  | 要应用于指定 SKU 的已取消订单自动补货配置。 |
| ^enable_auto_restock | bool | N | false | 控制卖家自履约（FBM）订单取消后的自动补货。当至少提供一个 SKU 时，省略 `stock_operation_setting` 或 `enable_auto_restock` 将使用 `false`。 |

* `true`: 为指定 SKU 启用自动补货。
* `false`: 为指定 SKU 禁用自动补货。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202608/inventory/operation/settings?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"seller_id":"124129082343241","sku_ids":["124148921741214"],"stock_operation_setting":{"enable_auto_restock":false}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^stock_operation | object |  | 库存操作的更新结果 |
| ^^failed_sku_ids | []string | ["124148921741214"] | 更新库存规则失败的 SkuID 列表 |
| ^^success_sku_ids | []string | ["124148921741214"] | 成功更新库存规则的 SkuID 列表 |
# 响应示例
```json
{"code":0,"data":{"stock_operation":{"failed_sku_ids":["124148921741214"],"success_sku_ids":["124148921741214"]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12001017 | sku id is invalid |
| 12019017 | The stock of SKU exceed the limit |
| 12019112 | seller id is invalid |
| 12019114 | 卖家无权限 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

