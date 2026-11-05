# 创建自定义品牌

# Path: /product/202309/brands
# Method: [POST]
# 功能描述
创建自定义品牌，供您在所有市场中使用。
创建品牌时不需要授权。您可以先创建品牌，然后稍后通过 TikTok Shop 卖家中心的资质中心获得品牌授权。
**Note**: You can create up to 50 brands per day, with a total limit of 1,000 brands.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | Y | Teas | 品牌名称。 |
**Note**:

* Length: [2, 30]
* No language restrictions, but do not use Chinese.
* Do not use a name that already exists.
* Do not include special fonts or emoticons.
* Do not include 5 or more consecutive numbers.
* The name will not be translated into multiple languages. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/brands?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"name":"Teas"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^id | string | 7082427311584347905 | 在 TikTok Shop 中标识品牌的唯一 ID。 |
# 响应示例
```json
{"code":0,"data":{"id":"7082427311584347905"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052189 | Brand names must be at least 2 characters. |
| 12052190 | Brand names must not be longer than 30 characters. |
| 12052191 | Brand names can't include special fonts or emoticons. |
| 12052192 | The brand name can't contain 5 or more consecutive numbers. |
| 12052202 | The total number of brands you have created today exceeds the limit. |
| 12052203 | The total number of brands you have created exceeds the limit. |
| 12052204 | The brand name you created is invalid. |
| 12052205 | This brand name already exists. |
| 12052206 | The number of characters of the created brand name is invalid. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

