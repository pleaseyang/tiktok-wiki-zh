# 提交尺码表申诉

# 路径：/product/202604/appeals/submit
# 方法：[POST]
# 功能描述
#### 申诉尺码表验证
为因尺码表校验失败而在上架阶段被拦截的商品发起申诉流程。
当卖家认为其商品被我们的自动尺码表校验系统错误拦截时使用此接口。校验会检查三类潜在问题：

1. 尺码表是否包含所有必填尺寸。
2. 尺码表是否覆盖所有在售 Stock-Keeping Units (SKUs)。
3. 尺码表中的数值是否有效。
   如果校验系统检测到问题，商品上架将被阻止。通过使用此接口，卖家可提交申诉。若申诉获批，阻止将被解除，卖家可重新上架商品。
   使用 `[Appeal Status Webhook]` 监控申诉进度，或将 `appeal_id` 传入 `[Get Appeal Status API]` 以获取当前状态。
   Note:
* 提交申诉后请至少等待 5 分钟，再通过 API 查询其状态，以确保数据已同步。
* 每天最多可提交 50 次申诉。超出此限制的请求将被拒绝。


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
| product_id | int | Y | 1729532326804361713 | product_id |
| appeal_message | object | Y |  | 提交申诉的商品详情 |
| ^field_name | string | Y | APPEAL_MESSAGE_FIELD_SIZE_CHART | 要申诉的目标字段。 |
| 可能的值： |  |  |  |  |

* APPEAL_MESSAGE_FIELD_SIZE_CHART |
   ^indicator_details |[]object |Y | |提交申诉的商品的指标详情 |
   ^^indicator_type |string |Y |CONTAINS_ALL_SALE_PROPERTY |此字段申诉所针对的目标 indicator_type。
   可能的值：
* REQUIRED_DIMENSION：尺码表是否包含所有必填尺寸?
* CONTAINS_ALL_SALE_PROPERTY：尺码表是否覆盖所有销售属性?""
* VALUE_RANGE_OUT_OF_RANGE：尺码表中的取值区间是否有效? |
   ^size_chart_id |string |N |7597302357391361806 |size_chart_id |
   ^size_chart_image_uri |string |N |tos-alisg-i-aphluv4xwc-sg/ebf6d1b2204a4aa883abb0befb6fee50 |size_chart_image 的 uri |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202604/appeals/submit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_id":1729532326804361713,"appeal_message":{"field_name":"APPEAL_MESSAGE_FIELD_SIZE_CHART","indicator_details":[{"indicator_type":"CONTAINS_ALL_SALE_PROPERTY"}],"size_chart_id":"7597302357391361806","size_chart_image_uri":"tos-alisg-i-aphluv4xwc-sg/ebf6d1b2204a4aa883abb0befb6fee50"}}
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
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

