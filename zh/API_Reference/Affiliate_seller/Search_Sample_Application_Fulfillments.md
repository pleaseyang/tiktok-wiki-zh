# 搜索 Sample 申请履约

# 路径：/affiliate_seller/202409/sample_applications/{application_id}/fulfillments/search
# 方法：[POST]
# 功能描述
此 API 用于搜索 sample 申请的履约状态。您可以查看 sample 订单的物流和履约信息。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| application_id | string | Y | 123456789 | 申请标识符。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| content_format | string | N | LIVE | 达人收到样品后生成的内容类型。可选枚举: |

* LIVE
* VIDEO |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202409/sample_applications/123456789/fulfillments/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"content_format":"LIVE"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^fulfillments | []object |  | Fulfillments |
| ^^product | object |  | Product information |
| ^^^id | string | 123456 | 商品标识符。 |
| ^^^main_image_url | string | https://www.example.com | 商品封面图片的 url。 |
| ^^content | object |  | 履约内容信息。 |
| ^^^id | string | 123456 | 视频或直播间的标识符。 |
| ^^^format | string | LIVE | 生成内容的格式: |

* LIVE
* `VIDEO` |
   ^^^url |string |https://www.example.com |内容来源链接。 |
   ^^^view_count |int |100 |内容的累计观看次数。 |
   ^^^like_count |int |123 |内容的累计点赞数。 |
   ^^^comment_count |int |10 |内容的累计评论数。 |
   ^^^paid_order_count |int |1 |内容产生的已支付订单累计总数。 |
   ^^^page_link |string |https://www.example.com |TikTok 内容页面 URL。 |
   ^^^description |string |abc def gh |视频标题或直播间描述。 |
   ^^^create_time |int |1723529426 |- 当 `format` 为 `VIDEO` 时，此为视频首次公开并关联到商品时的 Unix 时间戳，单位为秒。
* 当 `format` 为 `LIVE` 时，此为商品链接首次添加到直播中的 Unix 时间戳（以秒为单位）。 |
   ^^^live_end_time |int |1723529426 |仅当 `format==LIVE` 时。
   指商品链接从直播间移除的时间。若商品链接保持有效且未被移除，则取直播结束时间。 |

# 响应示例
```json
{"code":0,"data":{"fulfillments":[{"product":{"id":"123456","main_image_url":"https://www.example.com"},"content":{"id":"123456","format":"LIVE","url":"https://www.example.com","view_count":100,"like_count":123,"comment_count":10,"paid_order_count":1,"page_link":"https://www.example.com","description":"abc def gh","create_time":1723529426,"live_end_time":1723529426}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

