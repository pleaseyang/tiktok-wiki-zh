# 确认包裹发货

# 路径：/supply_chain/202309/packages/sync
# 方法：[POST]
# 功能描述
使用此接口提交包裹发货信息。只有经 TikTok Shop 认证的仓储服务商才能访问此接口。包裹独立处理，因此请求可能部分成功。处理响应时请同时检查 `success_packages` 和 `errors`。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| warehouse_provider_id | string | Y | 7342984797904049750 | TikTok Shop 分配的仓库服务商唯一 ID。该取值必须为正的十进制整数。 |
| packages | []object | Y |  | 待确认的包裹列表。请至少提供一个包裹。 |
| ^id | string | Y | 28427944530283 | 包裹 ID。该取值必须为长度不超过 40 个 UTF-8 字节的非零十进制整数字符串。 |
| ^wms_order_id | string | Y | 324246554745 | 仓库管理系统订单号 |
| ^provider_warehouse_code | string | N | 7475973290484254255 | 仓库编码。最大值：40 个 UTF-8 字节。 |
| ^shipping_origin_city | string | N | CityA | 货件始发城市名称 |
| ^time_zone | string | Y | UTC+8 | 仓库时区 |
| ^ship_time_millis | int | Y | 1694176625765 | 订单从仓库发出的时间（Unix 时间戳，单位毫秒） |
| ^create_time_millis | int | Y | 1694176625765 | 仓库接收订单的时间（Unix 时间戳，单位毫秒） |
| ^handover_time_millis | int | Y | 1694176625765 | 订单交付给物流服务商的时间（Unix 时间戳，单位毫秒） |
| ^shipping_provider_id | string | Y | 2435653524354624 | 配送服务商 ID |
| ^shipping_provider_name | string | Y | ProviderA | 配送服务商名称 |
| ^tracking_number | string | Y | WB53452356 | Tracking number |
| ^dimension | object | Y |  | 包裹尺寸信息 |
| ^^length | int | N | 34 | 包裹长度。必须大于或等于 `0`。 |
| ^^width | int | N | 425 | 包裹宽度。必须大于或等于 `0`。 |
| ^^height | int | N | 42 | 包裹高度。必须大于或等于 `0`。 |
| ^^unit | string | N | METER | 包裹尺寸单位 |
| 可能的值： |  |  |  |  |

* METER
* CENTIMETER
* MILLIMETER
* MICRON
* FOOT
* INCH |
   ^weight |object |N | |包裹重量信息 |
   ^^value |int |N |342 |包裹重量。必须大于或等于 `0`。 |
   ^^unit |string |N |KILOGRAM |包裹重量单位
   可能的值：
* KILOGRAM
* GRAM
* MILLIGRAM
* POUND
* OUNCE |
   ^skus |[]object |Y | |包裹中订单 SKU 的列表。请至少提供一个 SKU。 |
   ^^id |string |Y |4235346547 |TikTok Shop SKU ID。取值必须表示正的十进制整数。 |
   ^^quantity |int |Y |13 |包裹中此 SKU 的数量。必须大于 `0`。 |
   ^provider_warehouse_name |string |N |Central Warehouse |仓库名称 |
   ^tcw_warehouse_type |string |N |STANDARD |TikTok 仓库类型
   可能的值：
* STANDARD: 未经 TikTok 专门认证的标准仓库
* TIKTOK_CERTIFIED_WAREHOUSE_FULFILLMENT: TikTok 认证仓库，通常提供更好的服务水平。认证仓库必须满足 TikTok 设定的履约时效标准 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/supply_chain/202309/packages/sync?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"warehouse_provider_id":"7342984797904049750","packages":[{"id":"28427944530283","wms_order_id":"324246554745","provider_warehouse_code":"7475973290484254255","shipping_origin_city":"CityA","time_zone":"UTC+8","ship_time_millis":1694176625765,"create_time_millis":1694176625765,"handover_time_millis":1694176625765,"shipping_provider_id":"2435653524354624","shipping_provider_name":"ProviderA","tracking_number":"WB53452356","dimension":{"length":34,"width":425,"height":42,"unit":"METER"},"weight":{"value":342,"unit":"KILOGRAM"},"skus":[{"id":"4235346547","quantity":13}],"provider_warehouse_name":"Central Warehouse","tcw_warehouse_type":"STANDARD"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^success_packages | []string | ["5345241234","42365346"] | 已成功确认的包裹列表 |
| ^errors | []object |  | 未确认的包裹列表，包含每个包裹的失败信息。当所有包裹均已确认时，此字段省略。 |
| ^^code | string | 39003015 | Error code |
| ^^message | string | Provider is not supported by TikTok Shop | 错误消息 |
| ^^detail | object |  | 失败包裹详情 |
| ^^^package_id | string | 4645645645 | 失败包裹 ID |
# 响应示例
```json
{"code":0,"data":{"success_packages":["5345241234","42365346"],"errors":[{"code":"39003015","message":"Provider is not supported by TikTok Shop","detail":{"package_id":"4645645645"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 39003015 | provider is not in package information send-back white list |
| 39003016 | package param invalid, please check detail fail reason |
| 39003017 | save warehouse package info err |
| 39003018 | the package list is empty in the request |
| 39003019 | warehouse provider id is invalid |
| 39003020 | the provider id in your request is not match your app_key |

