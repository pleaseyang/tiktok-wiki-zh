# 获取 Open Collaboration Sample 规则

# Path: /affiliate_seller/202410/open_collaborations/sample_rules
# Method: [GET]
# 功能描述
此 API 用于获取 open collaboration 的 sample 规则。

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
| product_ids | []string | Y | 172979,848746 | 要获取 sample 规则的产品 ID。每次请求指定 1 到 200 个产品 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202410/open_collaborations/sample_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&product_ids=172979,848746
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sample_rules | []object |  | 请求产品的 sample 规则。 Products whose sample rules have never been created or have been deleted are omitted. |
| ^^product_id | string | 123456 | The unique id of product. |
| ^^sample_quota | int | 100 | 卖家提供的 creator 可申请的 sample 总数量。 |
| ^^is_sample_time_unlimited | bool | true | sample 是否不限时间可申请： |

* If true, it means available all the time
* 如果为 false，表示 sample 仅在 `begin_time` 到 `end_time` 期间可申请。 |
   ^^status |string |ONGOING |Free sample rule status:
* NOT_STARTED. Not yet reached the specified `begin_time`.
* ONGOING. The sample rule is effective and the collaboration is ongoing.
* `NO_LEFT_COUNT`. `sample_quantity_available` is `0`.
* PLAN_EXCEPTION. The product commission collaboration status is abnormal
* EXPIRED. Exceeded the `end_time`. |
   ^^available_quantity |int |50 |The quantity of remaining samples available for application. |
   ^^start_time |int |1728546888 |When present, the start of the sample application period, expressed as a Unix timestamp in seconds (UTC). |
   ^^end_time |int |1728546888 |When present, the end of the sample application period, expressed as a Unix timestamp in seconds (UTC). |
   ^^thresholds |object | |Creator 必须符合的门槛条件，才有资格申请 sample。 |
   ^^^minimum_follower_count |int |200 |The creator must have a follower count greater than or equal to this value to be eligible to request the sample. |
   ^^^minimum_gmv |int |1000 |The creator must have the GMV in the past 30 days greater than this value to be eligible to request the sample. |
   ^^^avg_ec_video_views |int |5 |The creator must have an average number of e-commerce video views over the past 30 days greater than or equal to this value to be eligible to request the sample. |
   ^^^category_ids |[]string |["601152"] |A list of first-level product category IDs used to determine creator eligibility. For each creator, first-level product categories are ranked by GMV over the past 30 days. A creator is eligible if at least one category in this list is among the creator's top three categories. By default, no category restriction applies.
   For example, if a creator's top three categories are [{Cellphone_ID}, {Furniture_ID}, {Food_ID}] and this field is `[{Food_ID}]`, the creator is eligible for open collaboration. |
   ^^^predicted_fulfillment_rank |string |ALL |The creators whose predicted rate of posting a shoppable video or LIVE after receiving a sample.
* ALL. All creators regardless of the rate.
* LOW. The creators whose rate is above or equal to low.
* MEDIUM. The creators whose rate is above or equal to medium.
* HIGH. The creators whose rate is high. |

# 响应示例
```json
{"code":0,"data":{"sample_rules":[{"product_id":"123456","sample_quota":100,"is_sample_time_unlimited":true,"status":"ONGOING","available_quantity":50,"start_time":1728546888,"end_time":1728546888,"thresholds":{"minimum_follower_count":200,"minimum_gmv":1000,"avg_ec_video_views":5,"category_ids":["601152"],"predicted_fulfillment_rank":"ALL"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

