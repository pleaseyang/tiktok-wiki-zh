# 获取畅销 LIVE 场次

# 路径：/analytics/202511/lives/bestselling
# 方法：[GET]
# 功能描述
获取最多 100 个按 GMV 排名的 LIVE 场次，基于 `date` 和 `time_slot` 定义的周期。

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
| date | string | N | 2025-11-13 | 参考日期，格式为 ISO 8601 YYYY-MM-DD，使用店铺注册的时区。该周期以此日期为截止日期（含），并根据 `time_slot` 向前延伸（例如 `7D` 覆盖以此日期结束的七天）。该日期必须不晚于最新可用数据日期。如果提交了更晚的日期，错误响应将说明最新可用数据日期；请使用该日期或更早的日期重试请求。 |
| time_slot | string | N | 7D | 指定查询时间范围。支持的值有： |

* 1D: 查询 1 天的数据
* 7D: 查询 7 天的数据
* 30D: 查询 30 天的数据

此字段决定使用 date 字段可查询的最大范围。 |
currency |string |N |USD |货币单位。使用 USD 表示美元，使用 LOCAL 表示店铺注册地的当地货币。如果省略，此参数默认为 LOCAL。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202511/lives/bestselling?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&date=2025-11-13&time_slot=7D&currency=USD
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^lives | []object |  | 目标日期范围内按 GMV 排名的畅销 LIVE 场次记录列表。 |
| ^^rank | int | 1 | LIVE 场次的 GMV 排名 |
| ^^gmv_range | string | $97000.00~$191000.00 | LIVE 场次的 GMV 范围。 |
| ^^id | string | 399123 | LIVE 场次 ID |
| ^^title | string | Dude's deal | LIVE 场次标题 |
| ^^start_time | int | 1623812664 | LIVE 场次的开始时间，为 Unix 时间戳（秒，UTC+00:00）。 |
| ^^duration | int | 7602 | LIVE 场次时长，单位为秒。 |
| ^^creator_name | string | abc_bec | 达人的唯一用户名，用于系统识别。 |
| ^^open_id | string | 41YL0AAAAAD7kUt1BK3H07WBF3MZWzCgL79vJ-xBgswGeL2BCGdmeQ | 达人的唯一 ID，在系统中唯一标识该达人。 |
| ^^creator_nick_name | string | ttnickname | 达人的显示昵称，对外可见。 |
# 响应示例
```json
{"code":0,"data":{"lives":[{"rank":1,"gmv_range":"$97000.00~$191000.00","id":"399123","title":"Dude's deal","start_time":1623812664,"duration":7602,"creator_name":"abc_bec","open_id":"41YL0AAAAAD7kUt1BK3H07WBF3MZWzCgL79vJ-xBgswGeL2BCGdmeQ","creator_nick_name":"ttnickname"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

