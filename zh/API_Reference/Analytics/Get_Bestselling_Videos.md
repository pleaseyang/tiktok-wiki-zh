# 获取畅销 video

# Path: /analytics/202511/videos/bestselling
# Method: [GET]
# 功能描述
返回按 GMV 降序排列的最多 100 个 video，基于 `date` 和 `time_slot` 选择的日期范围。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| date | string | Y | 2025-11-13 | 参考日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册的时区。查询从此日期根据 `time_slot` 向前计算数据（例如 `7D` 返回以此日期结束的 7 天数据）。此日期包含在内，且必须不晚于最新可用数据日期。 |
| time_slot | string | Y | 7D | 以 `date` 结尾的查询周期长度。支持的值有： |

* 1D: 1 天
* 7D: 7 天
* 30D: 30 天 |
   currency |string |N |USD |货币单位。使用 `USD` 表示美元，使用 `LOCAL` 表示店铺注册地的当地货币。如果省略，默认值为 `LOCAL`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202511/videos/bestselling?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&date=2025-11-13&time_slot=7D&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^videos | []object |  | 目标日期范围内的畅销 video 记录列表。 |
| ^^rank | int | 1 | video 的 GMV 排名 |
| ^^id | string | 10484583 | Video ID |
| ^^nick_name | string | abc_bec | 达人名称 |
| ^^gmv_range | string | $97000.00~$191000.00 | video 的 GMV 范围 |
| ^^views | int | 939829 | video 发布以来的累计播放量。 |
| ^^likes | int | 83894 | video 发布以来的累计点赞数。 |
| ^^comments | int | 1934 | video 发布以来的累计评论数。 |
| ^^shares | int | 223 | video 发布以来的累计分享数。 |
| ^^product_infos | []object |  | video 关联的商品锚点列表，包括商品 ID 和商品名称。不包括已下架和已售罄的商品。 |
| ^^^product_id | string | 1731736614984386107 | 商品锚点中的商品 ID。不包括已下架和已售罄的商品。 |
| ^^^product_name | string | labubu | 商品锚点中的商品名称。不包括已下架和已售罄的商品。 |
| ^^publish_time | int | 1623812664 | video 的发布时间，为 Unix 时间戳（秒，UTC）。 |
| ^^duration | int | 7602 | video 时长，单位为秒。 |
# 响应示例
```json
{"code":0,"data":{"videos":[{"rank":1,"id":"10484583","nick_name":"abc_bec","gmv_range":"$97000.00~$191000.00","views":939829,"likes":83894,"comments":1934,"shares":223,"product_infos":[{"product_id":"1731736614984386107","product_name":"labubu"}],"publish_time":1623812664,"duration":7602}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

