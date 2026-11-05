# 搜索负责人

# Path: /product/202501/compliance/responsible_persons/search
# Method: [POST]
# 功能描述
Retrieve a list of responsible persons in the EU languages supported by TikTok Shop based on their ID or keywords.
When creating a product with the [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned responsible person's `id` as an element of `responsible_person_ids`.
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
| page_size | int | Y | 10 | 每页返回的结果数量。 |
| Valid range: [1-100] |  |  |  |  |
| page_token | string | N | 66d3cbe4d9c8b09ddca932a7 | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| responsible_person_ids | []string | N | ["66d3cbe4d9c8b09ddca932a7"] | Filter results by these responsible person IDs. |
| Max IDs: The value of `page_size` |  |  |  |  |
| keyword | string | N | John | Filter results to show those that contain this keyword. |
| Search scope: name, local_number, email |  |  |  |  |
| Max length: 200 characters |  |  |  |  |
**Note**: Provide either the `responsible_person_ids` or `keyword`; if both are provided, `responsible_person_ids` will take priority. |
locales |[]string |N |["en-IE", "es-ES"] |The BCP-47 locale codes for displaying the responsible person information.
Default: The locale of the seller's registered business address.
Possible values:

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202501/compliance/responsible_persons/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_size=10&page_token=66d3cbe4d9c8b09ddca932a7
```

**Body**
```json
{"responsible_person_ids":["66d3cbe4d9c8b09ddca932a7"],"keyword":"John","locales":["en-IE","es-ES"]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^responsible_persons | []object |  | The list of responsible persons that meet the query conditions. |
| ^^id | string | 66d3cbe4d9c8b09ddca932a7 | The responsible person ID in TikTok Shop. |
| ^^regional_profiles | []object |  | A list of contact details for the responsible person, presented in different languages for each supported EU country. |
| ^^^locale | string | en-IE | The BCP-47 locale code representing the language used for specifying the responsible person information. |
| Possible values: |  |  |  |

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT |
   ^^^name |string |John Doe |The responsible person name.
   Max length: 200 characters |
   ^^^email |string |john.doe@email.com |The email address of the responsible person. |
   ^^^phone_number |object | |The phone number of the responsible person. |
   ^^^^country_code |string |+353 |The country code of the phone number, prefixed by a plus `+` symbol. E.g. +353 for Ireland. Only EU country codes are allowed.
   Max digits: 4 |
   ^^^^local_number |string |80915151 |The local number.
   Length: 7 - 11 digits |
   ^^^address |object | |The residential address of the responsible person. |
   ^^^^street_address_line1 |string |63 Cardiff Ln, Grand Canal Dock, Dublin City, Dublin |The detailed street address of the location, including the building number, street name, district, city, province, and any relevant details.
   Max length: 500 characters |
   ^^^^street_address_line2 |string |- |(**Deprecated**: This field is deprecated and will return an empty string. Please refer to `street_address_line1` instead for the relevant details.)

An optional secondary line for additional address details, if necessary.
Max length: 500 characters |
^^^^district |string |- |(**Deprecated**: This field is deprecated and will return an empty string. Please refer to `street_address_line1` instead for the district name.)
The district name.
Max length: 500 characters |
^^^^city |string |- |**Deprecated**: This field returns an empty string. Use `street_address_line1` for the city name. |
^^^^postal_code |string |D02 HD23 |The postal code.
Max length: 500 characters |
^^^^province |string |- |**Deprecated**: This field returns an empty string. Use `street_address_line1` for the province, state, or region name. |
^^^^country |string |IE |The two letter ISO 3166 country code representing the country of the address. It must be an EU country. |
^total_count |int |26 |The number of responsible persons that meet the query conditions. |
^next_page_token |string |66d3cbe3d9c8b09ddca932a1 |An opaque token used to retrieve the next page of a paginated result set. Provide this value in the `page_token` parameter of your request if the current response does not return all the results. |
# 响应示例
```json
{"code":0,"data":{"responsible_persons":[{"id":"66d3cbe4d9c8b09ddca932a7","regional_profiles":[{"locale":"en-IE","name":"John Doe","email":"john.doe@email.com","phone_number":{"country_code":"+353","local_number":"80915151"},"address":{"street_address_line1":"63 Cardiff Ln, Grand Canal Dock, Dublin City, Dublin","street_address_line2":"-","district":"-","city":"-","postal_code":"D02 HD23","province":"-","country":"IE"}}]}],"total_count":26,"next_page_token":"66d3cbe3d9c8b09ddca932a1"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 38023025 | Internal error |
| 38023047 | Invalid page size |
| 38023048 | Invalid page token |
| 38023049 | The number of ids is larger than page size |
| 38023050 | Operation is not supported for global seller |

