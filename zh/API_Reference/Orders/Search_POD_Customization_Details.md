# 搜索 POD 定制详情

# 路径：/order/202606/pod_details/search
# 方法：[POST]
# 功能描述
搜索指定订单行的 POD 定制详情。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| main_order_id | string | 是 | 577449529742299260 | TikTok Shop 订单 ID。 |
| query_order_lines | []object | 是 |  | 要获取 POD 定制详情的订单行。 |
| ^order_line_id | string | 是 | 577449529742430332 | 订单行项目的唯一标识符。 |
| ^product_id | string | 是 | 1732453831920750867 | 商品的唯一标识符。 |
| ^sku_id | string | 是 | 1732453830297817363 | SKU 的唯一标识符。 |
| ^pod_order_data_id | string | 是 | 122343 | POD 定制数据的唯一标识符。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202606/pod_details/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"main_order_id":"577449529742299260","query_order_lines":[{"order_line_id":"577449529742430332","product_id":"1732453831920750867","sku_id":"1732453830297817363","pod_order_data_id":"122343"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^pod_details | []object |  | 请求的订单行的 POD 定制详情。 |
| ^^order_line_id | string | 577457287176491132 | 与 POD 定制详情关联的订单行的唯一标识符。 |
| ^^pod_detail | string | pod_info_json | 订单行项目的唯一标识符。 |
| ^status_code | int | 0 | POD 定制详情查询的状态码。 |
# 响应示例
```json
{"code":0,"data":{"pod_details":[{"order_line_id":"577457287176491132","pod_detail":"pod_info_json"}],"status_code":0},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

