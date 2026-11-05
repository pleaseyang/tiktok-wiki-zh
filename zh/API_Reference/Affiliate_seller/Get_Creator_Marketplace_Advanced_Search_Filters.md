# 获取 Marketplace Creator 高级搜索筛选条件

# Path: /affiliate_seller/202608/marketplace_creators/search/filter
# Method: [POST]
# 功能描述
此 API 用于获取 Creator Marketplace 的高级搜索筛选条件，包括可用的分类、价格范围等选项。

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
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| options | []object | N |  | 要获取的筛选选项类型。 If this field is omitted or empty, both `option_list` and `sorters` are returned as empty arrays. |
| ^option_type | string | N | OPTION_SORTER | 要获取的筛选选项类型。可能的值： |

* `OPTION_VERTICAL_PRO`: Category Pro, a label for creators who regularly post about one product category and generated most of their sales in that category during the past 60 days.
* `OPTION_LANGUAGE`: Creator language.
* `OPTION_CREATOR_LEVEL`: Creator 等级 based on GMV. The definition varies by country and is maintained by the TikTok Shop Creator team.
* `OPTION_SORTER`: Available creator-search sorting options, returned in `sorters`.
* `OPTION_BRAND`: Creator brand information. This value is not supported in DE, FR, IT, ES, IE, or JP. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_seller/202608/marketplace_creators/search/filter?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"options":[{"option_type":"OPTION_SORTER"}]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^data | object |  | 可用的 Creator Marketplace 搜索筛选值和排序选项。 |
| ^^option_list | []object |  | Creator Marketplace 高级筛选选项列表。 If we return an empty object, it means this filter is not currently supported by your account or region. |
| ^^^option_type | string | OPTION_LANGUAGE | The requested filter option type represented by this entry. |
| ^^^options | []object |  | The available values for this filter option type. |
| ^^^^id | string | 1 | Option id |
| ^^^^name | string | English | The option name. |
| ^^^^option_children | []object |  | Children option detail list, used if the option has sub option choices |
| ^^^^^id | string | 12 | Children Option id |
| ^^^^^name | string | SubTypeName | Children Option name |
| ^^sorters | []object |  | The available sorting options for Creator Marketplace search results. |
| ^^^algorithm_id | string | 1 | sort algorithm id |
| ^^^name | string | related | sort algorithm name |
# 响应示例
```json
{"code":0,"data":{"data":{"option_list":[{"option_type":"OPTION_LANGUAGE","options":[{"id":"1","name":"English","option_children":[{"id":"12","name":"SubTypeName"}]}]}],"sorters":[{"algorithm_id":"1","name":"related"}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

