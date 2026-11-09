# 获取 Open Collaboration Sample 规则

# 路径：/affiliate_seller/202410/open_collaborations/sample_rules
# 方法：[GET]
# 功能描述
此 API 用于获取 open collaboration 的 sample 规则。

---


# 通用参数
有关通用参数，请参阅 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求跨境店铺 API 时未传递正确值将返回不正确的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送者。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| product_ids | []string | Y | 172979,848746 | 要获取 sample 规则的商品 ID。每次请求指定 1 到 200 个商品 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202410/open_collaborations/sample_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&product_ids=172979,848746
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sample_rules | []object |  | 请求商品的 sample 规则。 Products whose sample rules have never been created or have been deleted are omitted。 |
| ^^product_id | string | 123456 | 商品的唯一 id。 |
| ^^sample_quota | int | 100 | 卖家提供的达人可申请的 sample 总数量。 |
| ^^is_sample_time_unlimited | bool | true | sample 是否不限时间可申请： |

* 若为 true, 则表示始终可用
* 如果为 false，表示 sample 仅在 `begin_time` 到 `end_time` 期间可申请。 |
   ^^status |string |ONGOING |免费样品规则状态:
* NOT_STARTED. 尚未到达指定的 `begin_time`。
* ONGOING. 样品规则已生效，协作正在进行中。
* `NO_LEFT_COUNT`. `sample_quantity_available` is `0`.
* PLAN_EXCEPTION. 商品佣金协作状态异常
* EXPIRED. 已超过 `end_time`。 |
   ^^available_quantity |int |50 |可供申请的剩余样品数量。 |
   ^^start_time |int |1728546888 |如存在，表示样品申请期的开始时间，以秒为单位的 Unix 时间戳 (UTC) 表示。 |
   ^^end_time |int |1728546888 |如存在，表示样品申请期的结束时间，以秒为单位的 Unix 时间戳 (UTC) 表示。 |
   ^^thresholds |object | |达人必须符合的门槛条件，才有资格申请 sample。 |
   ^^^minimum_follower_count |int |200 |达人的粉丝数必须大于或等于此取值，才有资格申请样品。 |
   ^^^minimum_gmv |int |1000 |达人过去 30 天的 GMV 必须大于此取值才有资格申请样品。 |
   ^^^avg_ec_video_views |int |5 |达人过去 30 天的电商视频平均观看量必须大于或等于此取值，才有资格申请样品。 |
   ^^^category_ids |[]string |["601152"] |用于判定达人资格的一级商品类目 ID 列表。针对每位达人，一级商品类目按过去 30 天的 GMV 排名。如果此列表中至少有一个类目位于该达人的前三大类目中，则该达人符合条件。默认情况下不应用类目限制。
   例如，如果达人的前三个类目为 [{Cellphone_ID}, {Furniture_ID}, {Food_ID}]，而此字段为 `[{Food_ID}]`，则该达人符合开放协作条件。 |
   ^^^predicted_fulfillment_rank |string |ALL |The creators whose predicted rate of posting a shoppable video or LIVE after receiving a sample.
* ALL. 所有达人，不限费率。
* LOW. 费率高于或等于低档的达人。
* MEDIUM. 费率高于或等于中档的达人。
* HIGH. 费率高的达人。 |

# 响应示例
```json
{"code":0,"data":{"sample_rules":[{"product_id":"123456","sample_quota":100,"is_sample_time_unlimited":true,"status":"ONGOING","available_quantity":50,"start_time":1728546888,"end_time":1728546888,"thresholds":{"minimum_follower_count":200,"minimum_gmv":1000,"avg_ec_video_views":5,"category_ids":["601152"],"predicted_fulfillment_rank":"ALL"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

