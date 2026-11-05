# 更新盲盒开箱结果

# Path: /order/202605/orders/blind_box_result/callback
# Method: [POST]
# 功能描述
商家在直播间完成盲盒开箱后，使用此回调将订单的开箱结果发送回平台。请求支持两种结果格式：`blind_box_results` 包含每个商品一个开箱商品，而 `blind_batch_box_results` 将一个或多个开箱商品归组在订单行下。如果 `blind_batch_box_results` 非空，平台将处理它并忽略 `blind_box_results`。买家随后可以在订单详情中查看开箱结果。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| main_order_id | string | 否 | 576461413038785752 | TikTok Shop 订单的唯一标识符。 |
| blind_box_results | []object | 否 |  | 使用传统结果格式时，提供指定订单中一个或多个盲盒订单行的开箱结果。 |
| ^order_line_id | string | 否 | 577086512123755123 | 指定订单中盲盒的 TikTok Shop 订单行 ID。 |
| ^blind_result_product_id | string | 否 | 1732042550463074704 | 开箱后揭示的 TikTok Shop 商品 ID。 |
| ^blind_result_sku_id | string | 否 | 1732042694638604688 | 开箱后揭示的 TikTok Shop SKU ID。 |
| ^blind_open_time | int | 否 | 1762782183118 | 盲盒开箱时间的 Unix 时间戳（毫秒）。 |
| blind_batch_box_results | []object | 否 |  | 订单下订单行的批量开箱结果。 |
| ^order_line_id | string | 否 | 577086512123755123 | 指定订单中此批量开箱结果所属的盲盒的 TikTok Shop 订单行 ID。 |
| ^blind_box_order_line_list | []object | 否 |  | 订单下订单行的开箱结果。批量盒版本。 |
| ^^blind_result_product_id | string | 否 | 1732042550463074704 | 此商品在批量开箱结果中揭示的 TikTok Shop 商品 ID。 |
| ^^blind_result_sku_id | string | 否 | 1732042694638604688 | 此商品在批量开箱结果中揭示的 TikTok Shop SKU ID。 |
| ^^blind_open_time | int | 否 | 1762782183118 | 盲盒开箱时间的 Unix 时间戳（毫秒）。 |
| ^^product_type | string | 否 | NORMAL | 开箱商品类型。 |
| 可能的值： |  |  |  |  |

* `NORMAL`：普通开箱商品。
* `GIFT`：赠品行开箱商品。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202605/orders/blind_box_result/callback?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"main_order_id":"576461413038785752","blind_box_results":[{"order_line_id":"577086512123755123","blind_result_product_id":"1732042550463074704","blind_result_sku_id":"1732042694638604688","blind_open_time":1762782183118}],"blind_batch_box_results":[{"order_line_id":"577086512123755123","blind_box_order_line_list":[{"blind_result_product_id":"1732042550463074704","blind_result_sku_id":"1732042694638604688","blind_open_time":1762782183118,"product_type":"NORMAL"}]}]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 10007002 | 当前订单不是商家盲盒订单。 |
| 10007006 | 参数无效，请检查所有必填参数是否合法。 |
| 10007008 | 未获取到订单信息。 |
| 10007109 | 订单更新失败，请联系平台。 |
| 10007143 | 未获取到商品信息。请确认商品信息是否已同步到 TikTok Shop。 |
| 10007999 | 系统异常，请联系平台。 |

