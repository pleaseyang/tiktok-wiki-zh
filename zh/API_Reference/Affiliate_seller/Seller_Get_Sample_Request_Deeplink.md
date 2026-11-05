# 卖家获取 Sample 请求 Deeplink

# Path: /affiliate_seller/202512/sample_applications/deeplink
# Method: [GET]
# 功能描述
此 API 用于获取 TikTok deeplink，卖家可以将此链接发送给 creator，creator 通过该链接提交 sample 申请。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| product_id | string | Y | 123456 | The ID of a product that belongs to the authenticated shop. If neither `campaign_id` nor `collaboration_id` is provided, the product must be in an active open collaboration. |
| sku_id | string | Y | 123456 | The ID of a SKU that belongs to the product identified by `product_id`. |
| campaign_id | string | N | 3939495 | If the product belongs to a TAP campaign, `campaign_id` is required. The specified campaign must be active and contain the product identified by `product_id`. |
Supported campaign types:

* `MY_CAMPAIGNS`
* `SELLER_CAMPAIGNS` |
   collaboration_id |string |N |710240393 |If the product belongs to a seller collaboration, `collaboration_id` is required. Do not provide `collaboration_id` together with `campaign_id`. |
   valid_days |int |N |14 |7 days by default.
   14 days maximum.
   1 day minimum. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202512/sample_applications/deeplink?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&product_id=123456&sku_id=123456&campaign_id=3939495&collaboration_id=710240393&valid_days=14
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^deeplink | string | snssdk1180://roma_redirect/?*pia*=1&app_key=aaaa&callback_dp_key=f3318dbad42e495eaa12f3b9bec5af92&enter_from=deeplink&product_id=1729504817131129797&roma_group_key=spark_page_seller_free_sample_apply&roma_page_key=p&sample_apply_source=1&sku_id=1729504817131195333&spark_page=seller_free_sample_apply&track_data=%7B%22is_from_selection_scenarios%22%3A%221%22%2C%22selection_channel%22%3A%22deeplink%22%7D | Use this deeplink to invoke TikTok: |
|  |  |  |  |
# 响应示例
```json
{"code":0,"data":{"deeplink":"snssdk1180://roma_redirect/?_pia_=1\u0026app_key=aaaa\u0026callback_dp_key=f3318dbad42e495eaa12f3b9bec5af92\u0026enter_from=deeplink\u0026product_id=1729504817131129797\u0026roma_group_key=spark_page_seller_free_sample_apply\u0026roma_page_key=p\u0026sample_apply_source=1\u0026sku_id=1729504817131195333\u0026spark_page=seller_free_sample_apply\u0026track_data=%7B%22is_from_selection_scenarios%22%3A%221%22%2C%22selection_channel%22%3A%22deeplink%22%7D"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

