# 创建制造商

# Path: /product/202409/compliance/manufacturers
# Method: [POST]
# 功能描述
为卖家添加制造商。提供的信息将自动翻译成 TikTok Shop 支持的所有欧盟语言。

* Use the [Search Manufacturers API](67066a580dcee902fa03ccf9) to obtain the translations.
* Use the [Partial Edit Manufacturer API](67066a55c55b3a03044eea29) to edit the translations, if necessary.
* When creating a product, pass the returned `manufacturer_id` to associate the product with the manufacturer.
   Target seller: Local sellers operating in EU countries


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
| name | string | Y | John Doe | The manufacturer name. Chinese characters are not supported. |
| Max length: 255 characters |  |  |  |  |
| registered_trade_name | string | N | TikTok Shop | The registered trade name of the manufacturer. Chinese characters are not supported. |
| Max length: 200 characters |  |  |  |  |
| email | string | Y | johndoe@email.com | The manufacturer's email address. Use a valid email format such as `name@example.com`. Chinese characters are not supported. |
| phone_number | object | Y |  | The phone number of the manufacturer. |
| ^availability | string | N | AVAILABLE | Indicates the availability of the phone number. |
| Possible values: |  |  |  |  |

* `AVAILABLE`: The phone number is available and required.
* `UNAVAILABLE`: No phone number is available.

Default: AVAILABLE |
^country_code |string |N |+353 |The country code of the phone number, prefixed by a plus `+` symbol. E.g. +353 for Ireland.
Max digits: 4
Required if `availability=AVAILABLE`. |
^local_number |string |N |81234567 |The local number.
Length: 7 - 20 digits
Required if `availability=AVAILABLE`. |
address |string |Y |10 Earlsfort Terrace, Dublin, Ireland |The postal address of the manufacturer. Chinese characters are not supported.
Max length: 500 characters |
locale |string |N |en-IE |The BCP-47 locale code representing the language used for specifying the manufacturer information.
Possible values:

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT
   Default: The locale of the seller's registered business address.

**Note**: The information provided will be automatically translated into all EU languages supported by TikTok Shop. Ensure the locale matches the language used in field values to avoid inaccurate translations. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202409/compliance/manufacturers?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"name":"John Doe","registered_trade_name":"TikTok Shop","email":"johndoe@email.com","phone_number":{"availability":"AVAILABLE","country_code":"+353","local_number":"81234567"},"address":"10 Earlsfort Terrace, Dublin, Ireland","locale":"en-IE"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^manufacturer_id | string | 66d3cbe4d9c8b09ddca932a7 | A unique ID that identifies the manufacturer in TikTok Shop. |
# 响应示例
```json
{"code":0,"data":{"manufacturer_id":"66d3cbe4d9c8b09ddca932a7"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 38023025 | Internal error |
| 38023032 | Number of manufacturers exceeds the limit |
| 38023033 | Invalid manufacturer's name |
| 38023034 | Invalid manufacturer's address |
| 38023037 | Invalid manufacturer's registered trade name |
| 38023041 | Invalid phone number length |
| 38023042 | Invalid email format |
| 38023043 | Invalid address length |
| 38023044 | Invalid name length |
| 38023045 | Invalid registered trade name length |
| 38023046 | Invalid phone country code format |
| 38023050 | Operation is not supported for global seller |
| 38023060 | Invalid phone number availability. Supported values: `AVAILABLE`, `UNAVAILABLE` |

