# 获取每周达人外联配额

# 路径：/affiliate_seller/202607/creator_outreach/quota
# 方法：[GET]
# 功能描述
此 API 用于获取卖家每周可向达人发送外联消息的剩余配额。

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
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202607/creator_outreach/quota?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | 店铺的达人外联配额信息。 |
| ^^shop_id | string | 1234 | 店铺 ID |
| ^^quota_type | string | BONUS | 配额类型，例如 |
| 奖励配额； |  |  |  |
| 周期配额 |  |  |  |
| ^^gmv_tier | string | 1 | 店铺 GMV 等级 |
| ^^quota_sum | string | 1000 | 店铺配额总额 |
| ^^quota_use | string | 500 | 店铺已使用配额 |
| ^^unlimited | bool | false | 店铺是否拥有无限达人外联配额。 |
| ^^reached_max_follower_cnt | string | 1000 | 此店铺可达到的最大达人粉丝数量 |
| ^^new_connect_count | string | 100 | 此配额期间新建立连接的达人数量 |
| ^^pair_connect_count | string | 100 | 此配额期间配对连接的达人数量 |
| ^^start_time | string | 1754296736852 | 配额周期开始时间 |
| ^^end_time | string | 1754296736852 | 配额周期结束时间 |
| ^^gmv_level_rule | []object |  | 配额 GMV 等级规则 |
| ^^^reached_max_follower_cnt | string | 1000 | 在此 GMV 等级下店铺可达到的达人最大粉丝数量。 |
| ^^^gmv_tier | string | 1 | GMV 等级 ID |
| ^^^left_gmv | object |  | 规则 GMV 左边界 |
| ^^^^amount | string | 1000 | GMV 金额 |
| ^^^^currency | string | JPY | GMV 币种 |
| ^^^right_gmv | object |  | 规则 GMV 右边界 |
| ^^^^amount | string | 2000 | GMV 金额 |
| ^^^^currency | string | JPY | GMV 币种 |
| ^^^quota_details | []object |  | 达人级别配额详细规则 |
| ^^^^creator_levels | []int | [1,2] | 当前配额分层中包含的达人等级 |
| ^^^^quota_period_sum | int | 100 | 当前配额分层中的周期配额数量 |
| ^^^^quota_bonus_sum | int | 60 | 当前配额分层中的奖励配额数量，如果卖家达到曝光帖子百分位阈值，将获得奖励配额。 |
| ^^quota_details | []object |  | 达人级别配额详细信息 |
| ^^^creator_levels | []int | [1,2] | 当前配额分层中包含的达人等级 |
| ^^^quota_period_sum | int | 100 | 当前配额分层中的周期配额数量 |
| ^^^quota_period_use | int | 1 | 当前配额分层中已使用的周期配额 |
| ^^^quota_bonus_sum | int | 60 | 当前配额分层中的奖励配额数量，如果卖家达到曝光帖子百分位阈值，将获得奖励配额。 |
| ^^^quota_bonus_use | int | 60 | 当前配额分层中已使用的奖励配额，奖励配额将优先消耗。 |
| ^^bonus_exposure_post_percentile_threshold | string | 0.8 | 卖家获得达人级别配额额外奖励的曝光帖子百分位阈值，0.8 表示第 80 百分位。 |
# 响应示例
```json
{"code":0,"data":{"data":{"shop_id":"1234","quota_type":"BONUS","gmv_tier":"1","quota_sum":"1000","quota_use":"500","unlimited":false,"reached_max_follower_cnt":"1000","new_connect_count":"100","pair_connect_count":"100","start_time":"1754296736852","end_time":"1754296736852","gmv_level_rule":[{"reached_max_follower_cnt":"1000","gmv_tier":"1","left_gmv":{"amount":"1000","currency":"JPY"},"right_gmv":{"amount":"2000","currency":"JPY"},"quota_details":[{"creator_levels":[1,2],"quota_period_sum":100,"quota_bonus_sum":60}]}],"quota_details":[{"creator_levels":[1,2],"quota_period_sum":100,"quota_period_use":1,"quota_bonus_sum":60,"quota_bonus_use":60}],"bonus_exposure_post_percentile_threshold":"0.8"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

