# 编辑 Open Collaboration Sample 规则

# 路径：/affiliate_seller/202410/open_collaborations/sample_rules
# 方法：[POST]
# 功能描述
使用此 API 编辑 open collaboration 的 sample 规则。您可以为商品设置免费 sample 和付费 sample 规则。

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
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 123456 | 适用 sample 规则的商品 ID。每个 `product_id` 只能分配一个 sample 规则。仅最近的 API 调用生效。 |
| sample_rule | object | N |  | 应用于指定商品的 sample 规则设置。使用 `activate_status` 来创建、更新或停用规则。 |
| ^sample_quota | int | N | 100 | 卖家提供的达人可申请的 sample 总数量。 |
| ^is_sample_time_unlimited | bool | N | true | sample 是否随时可申请： |

* 如果为 true，sample 可随时申请。
* 如果为 false，sample 仅可在指定时间段内申请。您必须设置 start_time 和 end_time。 |
   ^start_time |int |N |1728552553 |达人可申请 sample 的起始时间，以秒为单位的 Unix 时间戳。您必须同时指定 `start_time` 和 `end_time`。 |
   ^end_time |int |N |1728552553 |达人可申请 sample 的结束时间，以秒为单位的 Unix 时间戳。您必须同时指定 `start_time` 和 `end_time`。 |
   ^thresholds |object |N | |达人必须符合的门槛条件，才有资格申请 sample。 |
   ^^minimum_follower_count |int |N |2000 |达人的粉丝数量必须大于或等于此值才有资格申请 sample。 |
   ^^minimum_gmv |int |N |1000 |达人过去 30 天的 GMV 必须大于此值才有资格申请 sample。 |
   ^^avg_ec_video_views |int |N |5 |达人过去 30 天的电商视频平均播放量必须大于或等于此值才有资格申请 sample。 |
   ^^category_ids |[]string |N |["601152"] |商品一级分类 ID 列表。
   用此来限制参与的达人：针对每位达人，按一级商品类目对其过去 30 天的 GMV 排序。如果其中某个类目的 GMV 排名前三，该达人即有资格参与该活动。默认不限制。
   例如，如果达人的前三个类目为 [{Cellphone_ID}, {Furniture_ID}, {Food_ID}]，且 tehis 参数的取值为 `[{Food_ID}]`，则该达人符合开放协作条件。 |
   ^^predicted_fulfillment_rank |string |N |LOW |The creators whose predicted rate of posting a shoppable video or LIVE after receiving a sample.
* ALL. 所有达人，不限费率。
* LOW. 费率高于或等于低档的达人。
* MEDIUM. 费率高于或等于中档的达人。
* HIGH. 费率高的达人。 |
   ^activate_status |string |Y |ACTIVATE |使用 `ACTIVATE` 激活 sample 规则；使用 `DEACTIVATE` 停用 sample 规则。
   使用 `ACTIVATE` 时，您必须指定规则详情；使用 `DEACTIVATE` 时，只需指定 `product_id`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202410/open_collaborations/sample_rules?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"product_id":"123456","sample_rule":{"sample_quota":100,"is_sample_time_unlimited":true,"start_time":1728552553,"end_time":1728552553,"thresholds":{"minimum_follower_count":2000,"minimum_gmv":1000,"avg_ec_video_views":5,"category_ids":["601152"],"predicted_fulfillment_rank":"LOW"},"activate_status":"ACTIVATE"}}
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
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

