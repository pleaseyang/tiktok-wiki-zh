# 创建 Compass 离线导出任务

# 路径：/affiliate_seller/202603/compass/offline_task
# 方法：[POST]
# 功能描述
此 API 用于创建异步离线导出任务。导出任务将生成包含所选指标数据的文件，供后续下载。

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
| module_type | string | N | BASE | 要导出的 Compass 数据类型。允许的值： |

* CREATOR: 达人列表数据。
* BASE: 核心业绩数据。 |
   window_type |string |N |PAST_24H |导出包含的时间窗口，以 end_day 结束。允许的值：PAST_24H、PAST_7_DAYS、PAST_30_DAYS。 |
   end_day |int |N |20260301 |指定地区本地时区的结束日期，格式为 YYYYMMDD。
   * id：UTC+7
   * my：UTC+8
   * sg：UTC+8
   * vn：UTC+7
   * th：UTC+7
   * ph：UTC+8
   * sa：UTC+3
   * us：UTC-8
   * mx：UTC-6
   * br：UTC-3
   * jp：UTC+9
   * gb：UTC+0
   * ie：UTC+0
   * es：UTC+1
   * de：UTC+1
   * fr：UTC+1
   * it：UTC+1
   * pl：UTC+1
   * nl：UTC+1
   * be：UTC+1
   * cz：UTC+1
   * at：UTC+1
   * gr：UTC+2
   * pt：UTC+0
   * hu：UTC+1 |
      plan_type |string |N |ALL |计划类型。允许的值：ALL、TARGET、OPEN、PARTNER。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202603/compass/offline_task?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"module_type":"BASE","window_type":"PAST_24H","end_day":20260301,"plan_type":"ALL"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^task | object |  | 用于创建可下载文件的任务 |
| ^^id | string | 1234 | 任务的 ID。 |
# 响应示例
```json
{"code":0,"data":{"task":{"id":"1234"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

