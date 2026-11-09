# 提交清关信息

# 路径：/fulfillment/202607/orders/customs_info/submit
# 方法：[POST]
# 功能描述
此 API 用于提交申报信息与实物不符时的额外清关信息。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
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
| order_list | []object | N |  | 要提交清关信息的订单列表。每个请求最多：100 个订单。 |
| ^order_id | string | Y | 584882846571463232 | TikTok Shop 订单 ID |
| ^item_list | []object | N |  | 订单行的清关条目列表。在同一订单内，明确的 order_line_id 值必须唯一。 |
| ^^order_line_id | string | N | 584882846571423334 | 子订单 ID；order_line_id 和 sku_id 不应同时为空。 |
| ^^sku_id | string | N | 1735885807280883357 | SKU ID；order_line_id 和 sku_id 不应同时为空。 |
| ^^item_detail | []object | N |  | 订单行的 SKU 级别清关详情列表。 |
| ^^^sku_id | string | Y | 1735885807280883357 | 此清关详情的 SKU ID。 |
| ^^^qty | int | Y | 2 | 清关详情中此 SKU 的数量。必须大于 0。 |
| ^^^price_percent | int | Y | 10 | 分配给此 SKU 在订单行中的百分比。每个值必须为非负数，且 item_detail 中的 price_percent 值总计必须为 100。例如，10 表示 10%。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202607/orders/customs_info/submit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"order_list":[{"order_id":"584882846571463232","item_list":[{"order_line_id":"584882846571423334","sku_id":"1735885807280883357","item_detail":[{"sku_id":"1735885807280883357","qty":2,"price_percent":10}]}]}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 11001002 | 参数无效。 |
| 11036004 | 系统错误，请重试 |

