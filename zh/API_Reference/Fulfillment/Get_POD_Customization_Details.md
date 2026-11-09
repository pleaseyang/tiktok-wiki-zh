# 获取 POD 定制详情

# 路径：/fulfillment/202606/pod_details/get
# 方法：[POST]
# 功能描述
获取 TikTok Shop 订单中指定订单行的 POD 定制详情。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时，如果未传递正确的值，将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
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
| main_order_id | string | Y | 576461413038785752 | TikTok Shop 订单 ID。 |
| query_order_lines | []object | Y |  | 要获取 POD 定制详情的非空订单行列表。 |
| ^order_line_id | string | Y | 577086512123755123 | 订单行项目的唯一标识符。 |
| ^product_id | string | Y | 1732453831920750867 | 商品的唯一标识符。 |
| ^sku_id | string | Y | 1732453830297817363 | sku 的唯一标识符。 |
| ^pod_order_data_id | string | Y | 123456 | pod 数据的唯一标识符。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202606/pod_details/get?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"main_order_id":"576461413038785752","query_order_lines":[{"order_line_id":"577086512123755123","product_id":"1732453831920750867","sku_id":"1732453830297817363","pod_order_data_id":"123456"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^pod_details | []object |  | 为所请求的订单行返回的 POD 定制详情。 |
| ^^pod_info_json | string | {"pod_template_id":123456} | 包含该订单行的 POD 定制模板的 JSON 编码字符串。 |
| ^^order_line_id | string | 577457287176491132 | 订单行项目的唯一标识符。 |
| ^status_code | int | 0 | response status |
# 响应示例
```json
{"code":0,"data":{"pod_details":[{"pod_info_json":"{\"pod_template_id\":123456}","order_line_id":"577457287176491132"}],"status_code":0},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

