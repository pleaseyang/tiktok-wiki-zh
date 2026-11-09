# 列出商品 SKPP 状态

# 路径：/product/202606/skpps/search
# 方法：[POST]
# 功能描述
批量查询卖家商品的 SKPP 状态。

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
* vi-VN。 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_ids | []string | N | ["7345678901","7345678902"] | 由 Tiktok Shop 生成的商品 ID; 每次调用最多 100 个。 |
| skpp_status | string | N | QUALIFIED | Optional filter. |
| 可选值：QUALIFIED（已是 SKPP 商品）/ NOT_QUALIFIED（尚未达到标准，但可参加 SKPP 任务）。 |  |  |  |  |
| page_size | int | N | 50 | 每页返回的商品数量. 取值范围: 1–100. 默认值: 50。 |
| page_no | int | N | 1 | 页码，从 1 开始. 默认值: 1。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202606/skpps/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en
```

**Body**
```json
{"product_ids":["7345678901","7345678902"],"skpp_status":"QUALIFIED","page_size":50,"page_no":1}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 商品列表，每项及其 SKPP 状态.。 |
| ^^product_id | string | 7345678901234567890 | 由 Tiktok Shop 生成的商品 ID |
| ^^title | string | Premium Cotton T-Shirt | Product title. |
| ^^skpp_status | string | QUALIFIED | 可能的值： QUALIFIED / NOT_QUALIFIED |
| ^^affiliate_program_status | string | ACTIVE | Affiliate Program 的加入状态。可选值：ACTIVE / INACTIVE。 |
| ^^total_score | int | 8 | 截至 update_time 的当前 SKPP 总分。 |
| ^^target_score | int | 7 | 获得 SKPP 资格所需的分数阈值。 |
| ^^rewards | []object |  | Rewards data. |
| ^^^reward_type | string | ADS_CREDIT | 可能的值： ADS_CREDIT / TOP_CREATOR_MATCHMAKING / SHOPTAB_PV。 |
| ^^^status | string | AVAILABLE | 可能的值： NOT_GRANTED (below threshold, locked) / PENDING (qualified, not yet granted) / AVAILABLE (granted)。 |
| ^^^value | string | $15 | 发放的金额/数量；仅在 status = AVAILABLE 时出现。货币类型（ADS_CREDIT）以货币符号开头（例如 $15）；计数类型（TOP_CREATOR_MATCHMAKING、SHOPTAB_PV）为纯数字。 |
| ^^^ad_credit_claim_status | string | CLAIMED | 广告金专属子状态，仅当 reward_type = ADS_CREDIT 且 status = AVAILABLE 时返回。可选值：UNCLAIMED（符合条件，尚未领取）/ CLAIMED（已领取）。广告金必须手动领取。 |
| ^total_count | int | 1234 | 符合筛选条件的商品总数。 |
| ^update_time | int | 1779148799 | total_score 和 rewards 所依据的离线数据快照的日期，以 Unix 时间戳（秒）返回，固定为 UTC 该日期的最后一秒 (23:59:59Z)。该值仅为日期级别 — 时间部分始终为 23:59:59 UTC — 因为 SKPP 评分在离线流水线中运行，没有日内粒度。延迟通常为 T+1（第 N 天晚上发布第 N−1 天的快照），最多 T+2。 |
# 响应示例
```json
{"code":0,"data":{"products":[{"product_id":"7345678901234567890","title":"Premium Cotton T-Shirt","skpp_status":"QUALIFIED","affiliate_program_status":"ACTIVE","total_score":8,"target_score":7,"rewards":[{"reward_type":"ADS_CREDIT","status":"AVAILABLE","value":"$15","ad_credit_claim_status":"CLAIMED"}]}],"total_count":1234,"update_time":1779148799},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12081001 | Invalid request parameters. |
| 12081003 | Internal server error. |
| 12081006 | Unauthorized for SKPP on this shop. |

