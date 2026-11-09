# 获取畅销达人

# 路径：/analytics/202511/creators/bestselling
# 方法：[GET]
# 功能描述
返回最多 100 个达人，按 `author_type` 筛选，以 `date` 和 `time_slot` 定义的报告期中按所选 `currency` 的 GMV 排名。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| date | string | Y | 2025-11-13 | 报告期的截止日期（含），格式为 ISO 8601 YYYY-MM-DD，使用店铺注册的时区。该周期从此日期向前延伸，由 `time_slot` 决定（例如 `7D` 覆盖以此日期结束的七天）。该日期不得晚于最新可用日期；当提交更晚的日期时，错误消息将标识最新可用日期。 |
| time_slot | string | Y | 7D | 以 `date` 结尾的查询周期长度。支持的值有： |

* 1D — 1 天
* 7D — 7 天
* 30D — 30 天 |
   author_type |string |Y |ALL |要包含的达人类型。支持的值有：
* ALL — 包含所有达人类型
* OFFICIAL — 包含官方达人
* CHANNEL — 包含渠道达人
* AFFILIATE — 包含联盟达人 |
   currency |string |N |USD |货币单位。支持的值有：
* USD — 美元
* LOCAL — 店铺注册地的当地货币
   如果省略，默认为 LOCAL。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202511/creators/bestselling?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&date=2025-11-13&time_slot=7D&author_type=ALL&currency=USD
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^creators | []object |  | 目标日期范围内按 GMV 排名的畅销达人记录列表。 |
| ^^rank | int | 1 | 达人的 GMV 排名。 |
| ^^gmv_range | string | $97000.00~$191000.00 | 达人在所选报告期的 GMV 范围，以 `currency` 所选的货币表示。 |
| ^^open_id | string | uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg | 达人的 open id，使用此 open id 标识一个达人。 |
| ^^user_name | string | creator_example_01 | 达人的账号名称。 |
| ^^nick_name | string | abc_bec | 达人的显示名称。 |
| ^^followers_count | int | 11234 | 粉丝数 |
| ^^likes_count | int | 23342 | 获赞数 |
# 响应示例
```json
{"code":0,"data":{"creators":[{"rank":1,"gmv_range":"$97000.00~$191000.00","open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg","user_name":"creator_example_01","nick_name":"abc_bec","followers_count":11234,"likes_count":23342}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

