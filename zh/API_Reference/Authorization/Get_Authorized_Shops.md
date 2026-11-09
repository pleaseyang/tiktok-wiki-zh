# 获取已授权店铺

# 路径：/authorization/202309/shops
# 方法：[GET]
# 功能描述
获取卖家为应用授权的店铺列表。
在应用访问店铺数据之前，需要获得卖家的授权。使用此 API 可以查看当前为应用授权的店铺，并获取相应的店铺 cipher，用作店铺相关 API 的输入参数。
有关卖家授权的更多信息，请参阅[卖家授权指南](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0)。
目标卖家：所有

---


# 公共参数
有关公共参数，请参阅[如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | 是 | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/authorization/202309/shops?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^shops | []object |  | 卖家为应用授权的店铺列表。 |
| ^^id | string | 7000714532876273420 | TikTok Shop 的内部标识符。 |
| ^^name | string | Maomao beauty shop | TikTok Shop 名称。 |
| ^^region | string | GB | 店铺所在区域。 |
| ^^seller_type | string | CROSS_BORDER | 卖家类型。 |
| 可能的值： |  |  |  |

* CROSS_BORDER：在多个国家拥有多个店铺的跨境卖家。
* LOCAL：仅拥有 1 个店铺的本地卖家。 |
   ^^cipher |string |GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 |用于在 API 请求中安全标识店铺的加密 token。接收端无需解密。 |
   ^^code |string |CNGBCBA4LLU8 |TikTok Shop 代码，也显示在卖家中心。 |

# 响应示例
```json
{"code":0,"data":{"shops":[{"id":"7000714532876273420","name":"Maomao beauty shop","region":"GB","seller_type":"CROSS_BORDER","cipher":"GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3","code":"CNGBCBA4LLU8"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅[如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |


