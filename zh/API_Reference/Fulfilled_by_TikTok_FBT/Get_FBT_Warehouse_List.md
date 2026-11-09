# 获取 FBT Warehouse 列表

# 路径：/fbt/202408/warehouses
# 方法：[GET]
# 功能描述
此 API 用于检索所有 Fulfilled by TikTok 仓库信息，包括仓库名称、仓库地址信息等。已订阅仓库的 ID 可用于查询 inventory 相关信息。

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
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202408/warehouses?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^warehouses | []object |  | Fulfilled by TikTok 仓库信息列表。 |
| ^^fbt_warehouse_id | string | 121219993203023 | Fulfilled By TikTok 系统生成的仓库标识符。 |
| ^^warehouse_ids | []string | ["161213293423029", "181213293423030"] | 与此 Fulfilled by TikTok 仓库（`fbt_warehouse_id`）关联的 TikTok Shop 生成的仓库 ID。 |
| ^^name | string | TikTok_Eastvale(CA) | Fulfilled by TikTok 仓库名称，例如 TikTok_Eastvale(CA)。 |
| ^^type | string | PLATFORM_WAREHOUSE | Fulfilled by TikTok 仓库类型。 |
| 可能的值： |  |  |  |

* `PLATFORM_WAREHOUSE`：TikTok 运营的仓库。
* `OTHER_WAREHOUSE`：不属于 platform 仓库分类的仓库。 |
   ^^subscribed |bool |true |表示仓库是否已订阅的标志。
   True: 已订阅。
   False: 未订阅。 |
   ^^addresses |[]object | |用于在 Fulfilled by TikTok 仓库接收 inbound 货件的地址列表。 |
   ^^^postal_code |string |92376 |Warehouse 地址邮政编码（也称 zip code）。 |
   ^^^region_code |string |US |Warehouse 国家或地区代码，采用两位字符的 ISO 3166-1 alpha-2 格式。 |
   ^^^state |string |CA |Warehouse 地址州或省。 |
   ^^^district |string |San Bernardino |Warehouse 地址区或县。 |
   ^^^city |string |Rialto |Warehouse 地址城市。 |
   ^^^address_line_1 |string |1420 Tamarind Ave, Rialto, San Bernardino |详细地址行 1。 |
   ^^^address_line_2 |string | |详细地址行 2，附加地址信息（可选）。 |
   ^^^address_line_3 |string | |详细地址行 3，附加地址信息（可选）。 |
   ^^logistics_services |[]object | |与当前仓库相关的物流服务信息列表。 |
   ^^^id |string |12123232323 |TikTok Shop 系统中物流服务的标识符。 |
   ^^^name |string |Fulfilled by TikTok Shop-Standard |物流服务名称。 |
   ^^^subscribed |bool |true |表示物流服务是否已订阅的标志。
   True: 已订阅。
   False: 未订阅。 |

# 响应示例
```json
{"code":0,"data":{"warehouses":[{"fbt_warehouse_id":"121219993203023","warehouse_ids":["161213293423029","181213293423030"],"name":"TikTok_Eastvale(CA)","type":"PLATFORM_WAREHOUSE","subscribed":true,"addresses":[{"postal_code":"92376","region_code":"US","state":"CA","district":"San Bernardino","city":"Rialto","address_line_1":"1420 Tamarind Ave, Rialto, San Bernardino","address_line_2":" ","address_line_3":" "}],"logistics_services":[{"id":"12123232323","name":"Fulfilled by TikTok Shop-Standard","subscribed":true}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

