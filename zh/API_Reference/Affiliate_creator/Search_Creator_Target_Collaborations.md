# 搜索达人 Target Collaboration

# 路径：/affiliate_creator/202405/target_collaborations/search
# 方法：[POST]
# 功能描述
搜索已认证达人在 `shop_id` 所指定的 TikTok Shop 中的定向协作及其中的商品。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
| page_token | string | N | b2Zmc2V0PTAK | 用于检索分页结果集下一页的不透明令牌。第一页不需要该令牌。对于后续的每一页，将上一次响应中的 `next_page_token` 原样作为 `page_token` 传入，并复用相同的 `page_size`、`shop_id`、`keyword` 和 `keyword_type` 取值，包括可选的 `keyword` 和 `keyword_type` 是省略还是提供。 |
| page_size | int | Y | 20 | 每页返回的结果数。有效范围：[0-100]。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| shop_id | string | Y | 789078671231 | TikTok Shop 标识符。 |
| keyword_type | string | N | TARGET_COLLABORATIONS_ID | 在 `keyword` 中指定的取值类型。同时提供 `keyword` 和 `keyword_type` 以按 ID 或名称筛选。省略这两个字段以在不使用 ID 或名称筛选的情况下搜索。可选值: |

* `TARGET_COLLABORATIONS_ID`: 按定向协作 ID 匹配，并返回处于 `LIVE`、`EXPIRED`、`DELETED` 或 `ENDED` 状态的匹配协作。
* `TARGET_COLLABORATIONS_NAME`：按定向协作名称匹配，且仅返回处于 `LIVE` 状态的匹配协作。 |
   keyword |string |N |12312312 |要搜索的定向协作 ID 或名称，由 `keyword_type` 指定。对于 `TARGET_COLLABORATIONS_ID`，提供十进制整数。对于 `TARGET_COLLABORATIONS_NAME`，提供小于 500 字节的值。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202405/target_collaborations/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&page_token=b2Zmc2V0PTAK&page_size=20
```

**Body**
```json
{"shop_id":"789078671231","keyword_type":"TARGET_COLLABORATIONS_ID","keyword":"12312312"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^total_count | int | 100 | 符合搜索条件的 target collaboration 总数。 |
| ^next_page_token | string | b2Zmc2V0PTIw | 用于获取分页结果集下一页的不透明 token。 |
| ^target_collaborations | []object |  | target collaboration 对象列表。 |
| ^^id | string | 789078671231123124 | target collaboration 标识符。 |
| ^^name | string | target_collaboration | target collaboration 名称。 |
| ^^status | string | LIVE | target collaboration 状态。这是枚举类型，取值如下： |

* LIVE
* EXPIRED
* DELETED
* ENDED |
   ^^products |[]object | |与 target collaboration 关联的商品列表。 |
   ^^^id |string |1729432087292775344 |商品标识符。 |
   ^^^title |string |Blue t-shirt |商品名称。 |
   ^^^main_image_url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499 |TikTok Shop 中的商品图片 URL。 |
   ^^^佣金 |object | |此 target collaboration 中商品的佣金费率和预估佣金金额。 |
   ^^^^rate |int |1000 |定向协作的佣金率，以百分比的百分之一为单位。例如，`3587` 表示 `35.87%` 的佣金率。 |
   ^^^^amount |string |121.23 |根据商品最低价格计算的预估佣金金额，以 `currency` 指定的货币计价。 |
   ^^^^currency |string |USD |货币代码。 |

# 响应示例
```json
{"code":0,"data":{"total_count":100,"next_page_token":"b2Zmc2V0PTIw","target_collaborations":[{"id":"789078671231123124","name":"target_collaboration","status":"LIVE","products":[{"id":"1729432087292775344","title":"Blue t-shirt","main_image_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/fa0387fa5a204dcfa44d5be75877a163~tplv-o3syd03w52-origin-webp.webp?from=3478900499","commission":{"rate":1000,"amount":"121.23","currency":"USD"}}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

