# 创建负责人

# Path: /product/202409/compliance/responsible_persons
# Method: [POST]
# 功能描述
Add a new EU responsible person who ensures a seller's products comply with EU regulations. The provided information will be automatically translated into all EU languages supported by TikTok Shop.

* Use the [Search Responsible Persons API](67066a55f17b7d02f95d2fb1) to obtain the translations.
* Use the [Partial Edit Responsible Person API](67066a5587019802fdce19b3) to edit the translations, if necessary.
* When creating a product, pass the returned `responsible_person_id` to associate the product with the responsible person.

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
| name | string | Y | John Doe | The responsible person name. Chinese characters are not supported. |
| Max length: 200 characters |  |  |  |  |
| email | string | Y | john.doe@email.com | The email address of the responsible person. Chinese characters are not supported. |
| phone_number | object | Y |  | The phone number of the responsible person. Chinese characters are not supported in `local_number`. |
| ^country_code | string | Y | +353 | The country code of the phone number, prefixed by a plus `+` symbol. E.g. +353 for Ireland. Only EU country codes are allowed. |
| Max digits: 4 |  |  |  |  |
| ^local_number | string | Y | 80915151 | The local number. |
| Length: 7 - 11 digits |  |  |  |  |
| address | object | Y |  | The residential address of the responsible person. Chinese characters are not supported in any address field. |
| ^street_address_line1 | string | Y | 63 Cardiff Ln, Grand Canal Dock, Dublin City, Dublin | The detailed street address of the location, including the building number, street name, district, city, province, and any relevant details. |
| Max length: 500 characters |  |  |  |  |
| ^street_address_line2 | string | N | - | (**Deprecated**: This field is deprecated and will be removed in a future API version. If provided, its value will be merged into `street_address_line1`. It is recommended to specify `street_address_line1` directly.) |
| An optional secondary line for additional address details, if necessary. |  |  |  |  |
| Max length: 500 characters |  |  |  |  |
| ^district | string | N | - | (**Deprecated**: This field is deprecated and will be removed in a future API version. If provided, its value will be merged into `street_address_line1`. It is recommended to specify `street_address_line1` directly.) |
The district name.
Max length: 500 characters |
^city |string |N |- |(**Deprecated**: This field is deprecated and will be removed in a future API version. If provided, its value will be merged into `street_address_line1`. It is recommended to specify `street_address_line1` directly.)
The city name.
Max length: 500 characters |
^postal_code |string |Y |D02 HD23 |The postal code.
Max length: 500 characters |
^province |string |N |- |(**Deprecated**: This field is deprecated and will be removed in a future API version. If provided, its value will be merged into `street_address_line1`. It is recommended to specify `street_address_line1` directly.)
The province, state, or region name.
Max length: 500 characters |
^country |string |Y |IE |The two letter ISO 3166 country code representing the country of the address. It must be an EU country. |
locale |string |N |en-IE |The BCP-47 locale code representing the language used for specifying the responsible person information.
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
https://open-api.tiktokglobalshop.com/product/202409/compliance/responsible_persons?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"name":"John Doe","email":"john.doe@email.com","phone_number":{"country_code":"+353","local_number":"80915151"},"address":{"street_address_line1":"63 Cardiff Ln, Grand Canal Dock, Dublin City, Dublin","street_address_line2":"-","district":"-","city":"-","postal_code":"D02 HD23","province":"-","country":"IE"},"locale":"en-IE"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^responsible_person_id | string | 66d3cbe4d9c8b09ddca023f1 | A unique ID that identifies the responsible person in TikTok Shop. |
# 响应示例
```json
{"code":0,"data":{"responsible_person_id":"66d3cbe4d9c8b09ddca023f1"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 38023022 | Invalid responsible person's name |
| 38023024 | Invalid responsible person's address |
| 38023025 | Internal error |
| 38023026 | Invalid EU country |
| 38023027 | Number of responsible person exceeds the limit |
| 38023028 | Invalid EU phone country code |
| 38023041 | Invalid phone number length |
| 38023042 | Invalid email format |
| 38023043 | Invalid address length |
| 38023044 | Invalid name length |
| 38023050 | Operation is not supported for global seller |

