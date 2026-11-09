# 创建制造商

# 路径：/product/202409/compliance/manufacturers
# 方法：[POST]
# 功能描述
为卖家添加制造商。提供的信息将自动翻译成 TikTok Shop 支持的所有欧盟语言。

* 使用 [Search Manufacturers API](67066a580dcee902fa03ccf9) 获取译文。
* 如有需要，请使用 [Partial Edit Manufacturer API](67066a55c55b3a03044eea29) 编辑翻译。
* 创建商品时，传入返回的 `manufacturer_id` 以将商品与制造商关联。
   目标卖家：在欧盟国家运营的本地卖家


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| name | string | Y | John Doe | 制造商名称。不支持中文字符。 |
| 最大长度: 255 个字符 |  |  |  |  |
| registered_trade_name | string | N | TikTok Shop | 制造商的注册商号。不支持中文字符。 |
| 最大长度：200 个字符 |  |  |  |  |
| email | string | Y | johndoe@email.com | 制造商的电子邮箱地址。请使用有效的邮箱格式，例如 `name@example.com`。不支持中文字符。 |
| phone_number | object | Y |  | 制造商的电话号码。 |
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
address |string |Y |10 Earlsfort Terrace, Dublin, Ireland |制造商的邮寄地址. 不支持中文字符。
最大长度：500 个字符 |
locale |string |N |en-IE |表示用于填写制造商信息所使用语言的 BCP-47 语言区域代码。
可能的值：

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT
   默认值：卖家注册经营地址所在的区域设置。

**说明**：所提供的信息将自动翻译为 TikTok Shop 支持的所有 EU 语言。请确保 locale 与字段值中使用的语言一致，以避免翻译不准确。 |
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
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^manufacturer_id | string | 66d3cbe4d9c8b09ddca932a7 | 在 TikTok Shop 中标识制造商的唯一 ID。 |
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
| 38023050 | 全球卖家不支持此操作 |
| 38023060 | Invalid phone number availability. Supported values: `AVAILABLE`, `UNAVAILABLE` |

