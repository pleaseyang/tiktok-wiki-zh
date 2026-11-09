# 获取全球上架规则

# 路径：/product/202507/global_listing_rules
# 方法：[GET]
# 功能描述
获取隶属于全球卖家的本地店铺的全局上架规则。例如支持的上架方式或库存分配规则。这些规则因其所服务的市场而异。
**注意**： 仅适用于全球卖家。

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
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202507/global_listing_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^listing_methods | []string | ["GLOBAL_PUBLISHING"] | 卖家在此店铺上架商品可采用的方式。 |
| 可能的值： |  |  |  |

* GLOBAL_PUBLISHING: 创建全球商品，然后将其发布到目标本地市场。
* LOCAL_REPLICATION: 创建本地商品，然后将其复制到其他目标本地市场。 |
   ^inventory_rules |[]object | |与店铺关联的所有仓库的库存分配规则列表。 |
   ^^local_warehouse_id |string |7068517275539719942 |与店铺关联的仓库 ID。 |
   ^^allocation_mode |string |SHARED |该仓库在本地市场使用的库存分配模式。
   `SHARED` – 库存在所有覆盖市场间共享。某一市场的库存扣减会反映到所有市场。
   `DYNAMIC` – 库存按比例分配给各覆盖市场。某一市场的库存扣减仅影响该市场。
   `MANUAL` – 库存由卖家为每个市场独立配置。某一市场的库存扣减仅影响该市场。 |
   ^^associated_warehouses |[]object | |与此仓库共享库存或从此仓库动态分配的关联仓库列表。每一项标识一个仓库及其地区。
   **注意**: 仅当 `allocation_mode` 为 `SHARED` 或 `DYNAMIC` 时适用。 |
   ^^^warehouse_id |string |7068517275539718842 |关联仓库的 ID。 |
   ^^^region |string |DE |仓库所在的国家。 |

# 响应示例
```json
{"code":0,"data":{"listing_methods":["GLOBAL_PUBLISHING"],"inventory_rules":[{"local_warehouse_id":"7068517275539719942","allocation_mode":"SHARED","associated_warehouses":[{"warehouse_id":"7068517275539718842","region":"DE"}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

