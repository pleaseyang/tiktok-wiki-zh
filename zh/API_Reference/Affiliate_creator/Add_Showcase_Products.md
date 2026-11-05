# 添加 Showcase 产品

# Path: /affiliate_creator/202405/showcases/products/add
# Method: [POST]
# 功能描述
此 API 将产品添加到已认证 creator 的 showcase 中。Global Shop 用户在调用此 API 之前必须至少选择一个区域。成功的 API 响应仍可能包含未添加产品的 `errors`；当没有产品级别的添加错误时，`errors` 将被省略。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop APIs - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| add_type | string | Y | PRODUCT_ID | 指定产品添加到 showcase 的方式。这是枚举类型，取值如下： |

* PRODUCT_ID
* PRODUCT_LINK |
   product_ids |[]string |N |["12390753231","7102893481290"] |当 `add_type` 设置为 `PRODUCT_ID` 时包含的产品标识符列表。与标识符关联的产品将被添加到 showcase 中。列表最大长度为 20 个产品标识符。 |
   product_link |string |N |https://www.example.com/api/v1/share/AImHx6DlXqP1 |当 `add_type` 设置为 `PRODUCT_LINK` 时使用的产品 URL。与 URL 关联的产品将被添加到 showcase 中。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202405/showcases/products/add?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"add_type":"PRODUCT_ID","product_ids":["12390753231","7102893481290"],"product_link":"https://www.example.com/api/v1/share/AImHx6DlXqP1"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 产品 showcase 添加错误列表。 |
| ^^code | int | 16001001 | 错误码。 |
| ^^message | string | Encounter network error, please try again. | 人类可读的错误消息。 |
| ^^detail | object |  | 关于产品 showcase 添加错误的额外详情。 |
| ^^^product_id | string | 12390753231 | 产品标识符。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":16001001,"message":"Encounter network error, please try again.","detail":{"product_id":"12390753231"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop APIs - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |

