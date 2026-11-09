# 上传发票

# 路径：/fulfillment/202502/invoice/upload
# 方法：[POST]
# 功能描述
上传发票文件。
**注意**：仅适用于巴西市场的本地卖家。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| invoices | []object | N |  | 要上传的发票列表。当提供 `invoices` 时，包含 1 到 500 个项目。 |
| ^package_id | string | Y | 1231231231231 | TikTok Shop package ID，从 [Search Package](650aa592bace3e02b75db748) 获取。 |
| ^order_ids | []string | Y | ["58747683456"] | TikTok Shop 订单 ID 列表，从 [Get Order List](650aa8094a0bb702c06df242) 获取。 |
| ^file_type | string | Y | XML | 发票文件格式。 |
| 可能的值： |  |  |  |  |

* `XML` |
   ^file |string |Y |PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGL |要上传的发票文件的 Base64 编码。
   最大文件大小：1MB |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202502/invoice/upload?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"invoices":[{"package_id":"1231231231231","order_ids":["58747683456"],"file_type":"XML","file":"PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGL"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 发票级别的上传错误。即使顶级 `code` 为 `0`，也可能返回此列表；每个条目标识受影响的 package 和订单 ID。 |
| ^^code | int | 10007014 | 错误码。 |
| ^^message | string | The invoice already exists in the upload. Please try again later | 错误消息。 |
| ^^detail | object |  | 错误详情。 |
| ^^^package_id | string | 1231231231231 | 发生错误的 package ID。 |
| ^^^order_ids | []string | ["58747683456"] | 发生错误的订单 ID。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":10007014,"message":"The invoice already exists in the upload. Please try again later","detail":{"package_id":"1231231231231","order_ids":["58747683456"]}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 21001028 | 订单正在处理中。请稍后重试。 |

