# 获取仓库配送选项

# Path: /logistics/202309/warehouses/{warehouse_id}/delivery_options
# Method: [GET]
# 功能描述
此 API 用于获取卖家指定仓库可用的配送选项列表。

---


# 公共参数
公共参数详情请参考 [如何调用 TikTok Shop APIs - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 参数 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Path 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| warehouse_id | string | Y | 6966568648651605766 | 仓库 ID，以十进制整数字符串表示。 |
# 请求 Query 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
| scope | string | N | PRODUCT | 指定要获取的配送选项类型。 |

* `WAREHOUSE`：返回当前对仓库生效的配送选项。订单默认使用这些选项。
* `PRODUCT`：返回可以直接分配给商品以覆盖默认仓库选项的配送选项。响应可以包含 `id`、`name`、`type`、`description` 和 `platform`；此 scope 不会填充 `dimension_limit` 或 `weight_limit`。
   默认值：`WAREHOUSE` |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/logistics/202309/warehouses/6966568648651605766/delivery_options?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&scope=PRODUCT
```

# 响应参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 参数描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^delivery_options | []object |  | 卖家仓库可用或可分配给商品的配送选项，取决于 `scope`。每个选项标识其支持的平台。为 `WAREHOUSE` 返回的选项还可能包括适用的重量和尺寸限制。 |
| ^^id | string | 6955034615128000261 | 配送选项 ID。 |
| ^^name | string | LSV-TTS-STD | 配送选项名称。 |
| ^^type | string | STANDARD | 配送选项类型。 |
| 可能的值： |  |  |  |

* STANDARD
* EXPRESS
* ECONOMY
* SEND_BY_SELLER
* INSTANT
* SAMEDAY
* NEXTDAY
* CARGO |
   ^^description |string |LSV-TTS-STD S |配送选项描述。 |
   ^^dimension_limit |object | |配送选项的长度、宽度和高度限制。 |
   ^^^max_height |int |100 |最大高度限制。 |
   ^^^max_length |int |100 |最大长度限制。 |
   ^^^max_width |int |100 |最大宽度限制。 |
   ^^^unit |string |INCH |尺寸的计量单位，可能的值：
* CM
* INCH |
   ^^weight_limit |object | |此配送选项的重量限制。 |
   ^^^max_weight |int |100 |最大重量限制。 |
   ^^^min_weight |int |100 |最小重量限制。 |
   ^^^unit |string |GRAM |重量的计量单位。
   可能的值：
* GRAM
* POUND
* OUNCE
* KILOGRAM |
   ^^platform |[]string |["TOKOPEDIA","TIKTOK_SHOP"] |配送选项可用的平台
   可能的值：
* TIKTOK_SHOP
* TOKOPEDIA |

# 响应示例
```json
{"code":0,"data":{"delivery_options":[{"id":"6955034615128000261","name":"LSV-TTS-STD","type":"STANDARD","description":"LSV-TTS-STD  S","dimension_limit":{"max_height":100,"max_length":100,"max_width":100,"unit":"INCH"},"weight_limit":{"max_weight":100,"min_weight":100,"unit":"GRAM"},"platform":["TOKOPEDIA","TIKTOK_SHOP"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码详情请参考 [如何调用 TikTok Shop APIs - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
