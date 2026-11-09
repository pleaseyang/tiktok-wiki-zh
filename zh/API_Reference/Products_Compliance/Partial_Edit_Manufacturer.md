# 部分编辑制造商

# 路径：/product/202409/compliance/manufacturers/{manufacturer_id}/partial_edit
# 方法：[POST]
# 功能描述
以 TikTok Shop 支持的欧盟语言编辑制造商的详细信息。若要编辑特定语言的制造商信息，请包含语言区域代码。
目标卖家：在欧盟国家运营的本地卖家
**注意**：

* 制造商名称，注册商号，电子邮件地址，本地电话号码和地址字段不得包含中文字符。
* 更新按顶层属性进行处理，因此必须提供被更新对象内的所有非空字段，以防止被空值覆盖。
* 对于未嵌套在对象中的顶层属性（例如 `name`、`email`），可单独更新。在请求中省略这些属性将使其保持不变。
* 如果你需要编辑对象内的任何嵌套属性，必须为该对象的所有嵌套属性提供值。任何省略的嵌套属性都将被空值覆盖。对于可用的电话号码，请同时提供 `availability=AVAILABLE`、`country_code` 和 `local_number`。如果卖家支持 `availability=UNAVAILABLE`，则提供 `availability=UNAVAILABLE` 并省略 `country_code` 和 `local_number`；否则仍需要提供有效的电话号码。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| manufacturer_id | string | Y | 66d3cbe4d9c8b09ddca932a7 | TikTok Shop 中的制造商 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | N | John Doe | 制造商名称。 |
| 最大长度: 255 个字符 |  |  |  |  |
| registered_trade_name | string | N | TikTok Shop | 制造商的注册商号。 |
| 最大长度：200 个字符 |  |  |  |  |
| email | string | N | johndoe@email.com | 制造商的电子邮件地址. 请使用有效的电子邮件格式，如 `name@example.com`。 |
| phone_number | object | N |  | 制造商的电话号码。 |
| ^availability | string | N | AVAILABLE | 指示该电话号码是否可用。 |
| 可能的值： |  |  |  |  |

* `AVAILABLE`：电话号码可用且必填。
* `UNAVAILABLE`: 无可用电话号码。

Default: AVAILABLE |
^country_code |string |N |+353 |电话号码的国家代码，以加号 `+` 开头。例如爱尔兰为 +353。
Max digits: 4
Required if `availability=AVAILABLE`. |
^local_number |string |N |81234567 |本地号码。
Length: 7 - 20 digits
Required if `availability=AVAILABLE`. |
address |string |N |10 Earlsfort Terrace, Dublin, Ireland |制造商的邮寄地址。
最大长度：500 个字符 |
locale |string |N |en-IE |表示待更新制造商信息所用语言的 BCP-47 语言区域代码。
可能的值：

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
https://open-api.tiktokglobalshop.com/product/202409/compliance/manufacturers/66d3cbe4d9c8b09ddca932a7/partial_edit?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"name":"John Doe","registered_trade_name":"TikTok Shop","email":"johndoe@email.com","phone_number":{"availability":"AVAILABLE","country_code":"+353","local_number":"81234567"},"address":"10 Earlsfort Terrace, Dublin, Ireland","locale":"en-IE"}
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
| 38023025 | Internal error |
| 38023033 | Invalid manufacturer's name |
| 38023034 | Invalid manufacturer's address |
| 38023037 | Invalid manufacturer's registered trade name |
| 38023041 | Invalid phone number length |
| 38023042 | Invalid email format |
| 38023043 | Invalid address length |
| 38023044 | Invalid name length |
| 38023045 | Invalid registered trade name length |
| 38023046 | Invalid phone country code format |
| 38023050 | 全球卖家不支持此操作 |
| 38023051 | Resource not found |
| 38023052 | Seller is not authorised to access resource |
| 38023060 | Invalid phone number availability. Supported values: `AVAILABLE`, `UNAVAILABLE` |

