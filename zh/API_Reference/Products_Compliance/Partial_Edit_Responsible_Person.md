# 部分编辑负责人

# 路径：/product/202409/compliance/responsible_persons/{responsible_person_id}/partial_edit
# 方法：[POST]
# 功能描述
以 TikTok Shop 支持的欧盟语言编辑欧盟负责人的详细信息。若要编辑特定语言的负责人信息，请包含语言区域代码。
目标卖家：在欧盟国家运营的本地卖家
**注意**：

* 更新按顶层属性进行处理，因此必须提供被更新对象内的所有非空字段，以防止被空值覆盖。
* 对于未嵌套在对象中的顶层属性（例如 `name`、`email`），可单独更新。在请求中省略这些属性将使其保持不变。
* 如果你需要编辑对象内的任何嵌套属性，必须为该对象的所有嵌套属性提供值。任何省略的嵌套属性都将被空值覆盖。例如，如果要更新 `phone_number.local_number`，还必须包含 `country_code` 属性，以避免该属性的数据丢失。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| responsible_person_id | string | Y | 66d3cbe4d9c8b09ddca023f1 | TikTok Shop 中的负责人 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | N | John Doe | 要更新的负责人姓名。提供此字段时不支持中文字符。 |
| 最大长度：200 个字符 |  |  |  |  |
| email | string | N | john.doe@email.com | 要更新的负责人的电子邮箱地址。提供此字段时不支持中文字符。 |
| phone_number | object | N |  | 要更新的负责人的电话号码. 提供此对象时，`local_number` 不支持中文字符。 |
| ^country_code | string | Y | +353 | 电话号码的国家代码，以加号 `+` 开头。例如爱尔兰为 +353。仅允许欧盟国家代码。 |
| Max digits: 4 |  |  |  |  |
| ^local_number | string | Y | 80915151 | 本地号码。 |
| Length: 7 - 11 digits |  |  |  |  |
| address | object | N |  | 要更新的负责人的居住地址。所提供的任何地址字段均不支持中文字符。 |
| ^street_address_line1 | string | Y | 63 Cardiff Ln, Grand Canal Dock, Dublin City, Dublin | 位置的详细街道地址，包括门牌号，街道名称，区，城市，省份以及任何相关详细信息。 |
| 最大长度：500 个字符 |  |  |  |  |
| ^street_address_line2 | string | N | - | (**已弃用**：该字段已弃用，将在未来的 API 版本中移除。如果提供，其值将合并到 `street_address_line1`。建议直接指定 `street_address_line1`。) |
| 可选的第二行，用于填写补充地址信息（如需要）。 |  |  |  |  |
| 最大长度：500 个字符 |  |  |  |  |
| ^district | string | N | - | (**已弃用**：该字段已弃用，将在未来的 API 版本中移除。如果提供，其值将合并到 `street_address_line1`。建议直接指定 `street_address_line1`。) |
| 区县名称。 |  |  |  |  |
| 最大长度：500 个字符 |  |  |  |  |
| ^city | string | N | - | (**已弃用**：该字段已弃用，将在未来的 API 版本中移除。如果提供，其值将合并到 `street_address_line1`。建议直接指定 `street_address_line1`。) |
| 城市名称。 |  |  |  |  |
| 最大长度：500 个字符 |  |  |  |  |
| ^postal_code | string | Y | D02 HD23 | 邮政编码。 |
| 最大长度：500 个字符 |  |  |  |  |
| ^province | string | N | - | (**已弃用**：该字段已弃用，将在未来的 API 版本中移除。如果提供，其值将合并到 `street_address_line1`。建议直接指定 `street_address_line1`。) |
| 省，州或地区名称。 |  |  |  |  |
| 最大长度：500 个字符 |  |  |  |  |
| ^country | string | Y | IE | 表示地址所属国家的两位字母 ISO 3166 国家代码。必须是欧盟国家。 |
| locale | string | N | en-IE | 表示要更新的负责人信息所用语言的 BCP-47 语言区域代码。 |
| 可能的值： |  |  |  |  |

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT
   默认值：卖家注册经营地址所在的区域设置。

**说明**：仅更新此 locale 所选的语言版本；其他语言版本保持不变。请确保 locale 与所提供字段值中使用的语言一致。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202409/compliance/responsible_persons/66d3cbe4d9c8b09ddca023f1/partial_edit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"name":"John Doe","email":"john.doe@email.com","phone_number":{"country_code":"+353","local_number":"80915151"},"address":{"street_address_line1":"63 Cardiff Ln, Grand Canal Dock, Dublin City, Dublin","street_address_line2":"-","district":"-","city":"-","postal_code":"D02 HD23","province":"-","country":"IE"},"locale":"en-IE"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 38023022 | Invalid responsible person's name |
| 38023024 | Invalid responsible person's address |
| 38023025 | Internal error |
| 38023026 | Invalid EU country |
| 38023028 | Invalid EU phone country code |
| 38023041 | Invalid phone number length |
| 38023042 | Invalid email format |
| 38023043 | Invalid address length |
| 38023044 | Invalid name length |
| 38023050 | 全球卖家不支持此操作 |
| 38023051 | Resource not found |
| 38023052 | Seller is not authorised to access resource |

