# 搜索制造商

# 路径：/product/202501/compliance/manufacturers/search
# 方法：[POST]
# 功能描述
按 ID 或关键词检索制造商列表，以 TikTok Shop 支持的欧盟语言返回。
使用 [Create Product API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) 创建商品时，将返回的制造商 `id` 作为 `manufacturer_ids` 的一个元素传入。
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
| page_size | int | Y | 10 | 每页返回的结果数量。 |
| 有效范围： [1-100] |  |  |  |  |
| page_token | string | N | 66d3cbe4d9c8b09ddca932a7 | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| manufacturer_ids | []string | N | ["66d3cbe4d9c8b09ddca932a7"] | 按这些制造商 ID 筛选结果。 |
| 最大 ID 数: `page_size` 的取值 |  |  |  |  |
| keyword | string | N | John | 筛选结果，只显示包含此关键词的条目。 |
| 搜索范围: name, 注册商号，local_number, email |  |  |  |  |
| 最大长度：200 个字符 |  |  |  |  |
**注意**：请提供 `manufacturer_ids` 或 `keyword` 之一；如果两者都提供，`manufacturer_ids` 将优先。 |
locales |[]string |N |["en-IE", "es-ES"] |用于显示制造商信息的 BCP-47 语言区域代码。
默认值：卖家注册经营地址所在的区域设置。
可能的值：

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202501/compliance/manufacturers/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_size=10&page_token=66d3cbe4d9c8b09ddca932a7
```

**Body**
```json
{"manufacturer_ids":["66d3cbe4d9c8b09ddca932a7"],"keyword":"John","locales":["en-IE","es-ES"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^manufacturers | []object |  | 符合查询条件的制造商列表。 |
| ^^id | string | 66d3cbe4d9c8b09ddca932a7 | TikTok Shop 中的制造商 ID。 |
| ^^regional_profiles | []object |  | 制造商的联系方式列表，针对每个受支持的欧盟国家以不同语言呈现。 |
| ^^^locale | string | en-IE | 表示指定制造商信息所用语言的 BCP-47 语言区域代码。 |
| 可能的值： |  |  |  |

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT |
   ^^^name |string |John Doe |制造商名称。
   最大长度: 255 个字符 |
   ^^^registered_trade_name |string |TikTok Shop |制造商的注册商号。
   最大长度: 200 个字符 |
   ^^^email |string |johndoe@email.com |制造商的电子邮件地址。 |
   ^^^phone_number |object | |制造商的电话号码。 |
   ^^^^availability |string |AVAILABLE |表示电话号码的可用性。
   可能的值：
* `AVAILABLE`：电话号码可用且必填。
* `UNAVAILABLE`: 无可用电话号码。 |
   ^^^^country_code |string |+353 |电话号码的国家代码，以加号 `+` 开头。例如爱尔兰为 +353。
   Max digits: 4
   Required if `availability=AVAILABLE`. |
   ^^^^local_number |string |81234567 |本地号码。
   Length: 7 - 20 digits
   Required if `availability=AVAILABLE`. |
   ^^^address |string |10 Earlsfort Terrace, Dublin, Ireland |制造商的邮寄地址。
   最大长度：500 个字符 |
   ^total_count |int |26 |符合查询条件的制造商数量。 |
   ^next_page_token |string |66d3cbe3d9c8b09ddca932a1 |用于获取分页结果集下一页的不透明令牌。如果当前响应未返回全部结果，请在请求的 `page_token` 参数中提供此值。 |

# 响应示例
```json
{"code":0,"data":{"manufacturers":[{"id":"66d3cbe4d9c8b09ddca932a7","regional_profiles":[{"locale":"en-IE","name":"John Doe","registered_trade_name":"TikTok Shop","email":"johndoe@email.com","phone_number":{"availability":"AVAILABLE","country_code":"+353","local_number":"81234567"},"address":"10 Earlsfort Terrace, Dublin, Ireland"}]}],"total_count":26,"next_page_token":"66d3cbe3d9c8b09ddca932a1"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 38023025 | Internal error |
| 38023047 | Invalid page size |
| 38023048 | Invalid page token |
| 38023049 | The number of ids is larger than page size |
| 38023050 | 全球卖家不支持此操作 |
| 38023057 | Unsupported locale |
| 38023060 | Invalid phone number availability. Supported values: `AVAILABLE`, `UNAVAILABLE` |

