# 获取商品 SKPP 详情

# 路径：/product/202606/skpps/{product_id}
# 方法：[GET]
# 功能描述
返回单个商品的 SKPP 资质状态、当前分与目标分、任务进度与建议操作、奖励资格与状态以及离线快照时间。此 API 仅对美国市场获 SKPP 授权的卖家开放。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 7311223344556677889 | Tiktok Shop 生成的商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| locale | string | N | en | 用于显示分类信息的 BCP-47 语言环境代码。 |
| Default: 您店铺的默认语言环境。 |  |  |  |  |
| 可能的值： |  |  |  |  |

* en
* en-GB
* zh-CN
* de-DE
* id-ID
* it-IT
* ja-JP
* ms-MY
* pt-BR
* th-TH
* vi-VN |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202606/skpps/7311223344556677889?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^product_id | string | 7311223344556677889 | 平台商品 ID。 |
| ^affiliate_program_status | string | ACTIVE | Affiliate Program enrolment. 可能的值： ACTIVE / INACTIVE。 |
| ^total_score | int | 6 | 截至 update_time 的当前 SKPP 总分。 |
| ^target_score | int | 8 | 获得 SKPP 资格所需的分数阈值。 |
| ^rewards | []object |  | Reward list. |
| ^^reward_type | string | BIG_PROMOTION_CAMPAIGN | 可能的值： ADS_CREDIT / TOP_CREATOR_MATCHMAKING / SHOPTAB_PV / BIG_PROMOTION_CAMPAIGN / OFF_PLATFORM_BESTSELLER_ADS_CREDIT。 |
| ^^title | string | 广告金奖励 | 本地化的奖励名称，根据请求的区域设置从共享卖家-Center 内容解析而来。 |
| ^^status | string | AVAILABLE | 可能的值： NOT_GRANTED / PENDING / AVAILABLE |
| ^^ad_credit_claim_status | string | UNCLAIMED | 广告金专属子状态，仅当 reward_type = ADS_CREDIT 且 status = AVAILABLE 时返回。可选值：UNCLAIMED（符合条件，尚未领取）/ CLAIMED（已领取）。 |
| ^^value | string | 100 | 授予的金额/数量; 货币类型取值以货币符号开头。 |
| ^^claim_conditions | []object |  | 解锁奖励的阈值; 由 ADS_CREDIT 使用。 |
| ^^^condition_type | string | GMV | 可能的值： GMV / ORDER。 |
| ^^^current_value | string | 72 | 当前进度; GMV 类型的取值以货币符号开头。 |
| ^^^target_value | string | 100 | 阈值; 格式与 current_value 相同。 |
| ^^campaign_id | string | 7390000000000000000 | 仅当 reward_type = BIG_PROMOTION_CAMPAIGN 时返回。 |
| ^task_details | []object |  | 按类目划分的得分明细及建议操作。 |
| ^^category | string | INFORMATION_QUALITY | 评分类目的键。 |
| 可能的值： |  |  |  |

* COMMISSION_RATE
* FULFILMENT
* PRICING
* FREE_SHIPING
* FOLLOWER_BENEFITS
* SAMPLING
* ADS_SPEND
* STOCK
* SHOPPABLE_VIDEOS
* INFORMATION_QUALITY
* CRM_HOSTING |
   ^^name |string |Improve product title |本地化的类目名称，根据请求语言区域通过共享内容从类目解析得到。 |
   ^^current_value |string |12 |该维度指标的当前取值 (例如当前价格，佣金率，包邮状态)。 |
   ^^target_value |string |20 |此维度为通过所必须达到的阈值。其单位与 `current_value` 相同，并可在开头包含比较运算符，例如 `≥` 或 `≤`，以表示所需方向。 |
   ^^passed |bool |false |该维度是否达到其 target_value。 |
   ^^action_suggestions |[]object | |完成此任务的建议操作；仅在 passed = false 时返回。一个任务可能有多条建议。 |
   ^^^score_increase |int |8 |完成此操作时加到 total_score 的 SKPP 分数；对于分层操作，为最高层级。 |
   ^^^url |string |https://seller.tiktokglobalshop.com/product/edit |指向完成该操作的 Seller Center 页面的链接。 |
   ^update_time |int |1779148799 |total_score、rewards 和得分明细所依据的离线数据快照的日期，以 Unix 时间戳（秒）返回，固定为 UTC 该日期的最后一秒 (23:59:59Z)。该值仅为日期级别 — 时间部分始终为 23:59:59 UTC — 因为 SKPP 评分在离线流水线中运行，没有日内粒度。延迟通常为 T+1（第 N 天晚上发布第 N−1 天的快照），最多 T+2。 |
   ^skpp_status |string |QUALIFIED |可能的值： QUALIFIED / NOT_QUALIFIED / NOT_ELIGIBLE。 |

# 响应示例
```json
{"code":0,"data":{"product_id":"7311223344556677889","affiliate_program_status":"ACTIVE","total_score":6,"target_score":8,"rewards":[{"reward_type":"BIG_PROMOTION_CAMPAIGN","title":"Ad credit reward","status":"AVAILABLE","ad_credit_claim_status":"UNCLAIMED","value":"100","claim_conditions":[{"condition_type":"GMV","current_value":"72","target_value":"100"}],"campaign_id":"7390000000000000000"}],"task_details":[{"category":"INFORMATION_QUALITY","name":"Improve product title","current_value":"12","target_value":"20","passed":false,"action_suggestions":[{"score_increase":8,"url":"https://seller.tiktokglobalshop.com/product/edit"}]}],"update_time":1779148799,"skpp_status":"QUALIFIED"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12081001 | Invalid request parameters. |
| 12081003 | Internal server error. |
| 12081006 | Unauthorized for SKPP on this shop. |

