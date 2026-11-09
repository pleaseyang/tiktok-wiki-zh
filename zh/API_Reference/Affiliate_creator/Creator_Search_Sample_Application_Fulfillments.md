# 达人搜索样品申请履约

# 路径：/affiliate_creator/202409/sample_applications/fulfillments/search
# 方法：[POST]
# 功能描述
你作为达人，可以使用此接口查询已收到的样品申请的履约状态。

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
| sort_order | string | N | DESC | sort_field 参数中指定字段的排序顺序。 |
| 默认值：ASC |  |  |  |  |
| 可能的值： |  |  |  |  |
| ASC: 升序 |  |  |  |  |
| DESC: 降序 |  |  |  |  |
| sort_field | string | N | expired_time | 可能的值： |

* expired_time: 按剩余履约时间排序。
* create_time: 按履约记录创建时间排序。
   默认: expired_time。 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| fulfillment_statuses | []string | Y | ["PENDING", "ONGOING"] | 履约状态列表。响应将筛选为仅包含 `status` 字段取值为指定值之一的样品履约记录。可能取值为： |

* PENDING：达人尚未履行内容创作义务。
* ONGOING：履约进行中；内容已创建并正在按标准评估。
* SUCCEED：履约已成功完成；内容符合要求的标准。
* FAILED：履约失败；内容未达到要求的标准。
* OVERDUE：履约已逾期；达人未在截止时间内完成。
* SUSPEND：履约已暂停。
* CANCELLED：履约已取消，由达人取消或因运营原因取消。
* EXEMPTED：达人免除履约义务。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202409/sample_applications/fulfillments/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&sort_order=DESC&sort_field=expired_time
```

**Body**
```json
{"fulfillment_statuses":["PENDING","ONGOING"]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^fulfillments | []object |  | 达人履约内容。 |
| ^^id | string | 123456 | 履约标识符。 |
| ^^shop_id | string | 123456 | TikTok Shop 标识符。 |
| ^^application_id | string | 123456 | 样品申请标识符。 |
| ^^sample_application_type | string | FREE_SAMPLE | 样品申请的类型。可能的取值: |

* FREE_SAMPLE
* SAMPLE_COUPON
* SAMPLE_CAMPAIGN
* PLATFORM_FREE_SAMPLE
* REFUNDABLE_SAMPLE
* UNSPECIFIED |
   ^^product_id |string |123456 |商品标识符。 |
   ^^expiration_time |int |1728542813 |履约截止时间戳。
   通常取值为 `{you_receiving_sample_time} + 14Days`。但如果申请履约暂停，取值为 `{you_receiving_sample_time} + 14Days + total_suspend_duration`。 |
   ^^total_suspend_duration |int |100020 |您申请的履约暂停时长（秒）。 |
   ^^status |string |ONGOING |履约状态。这是一个枚举类型，取值如下:
* PENDING：达人尚未履行内容创作义务。
* ONGOING：履约进行中；内容已创建并正在按标准评估。
* SUCCEED：履约已成功完成；内容符合要求的标准。
* FAILED：履约失败；内容未达到要求的标准。
* OVERDUE: 履约已逾期; 达人未在截止日期前完成.SUSPEND: 履约已暂停。
* CANCELLED：履约已取消，由达人取消或因运营原因取消。
* EXEMPTED：达人免除履约义务。 |
   ^^bound_product_status |string |LIVE |The promotion status of the product associated with the fulfillment. Possible values:
* UNKNOWN: 商品的推广状态未知。
* LIVE: 商品可用于推广。
* OUT_OF_STOCK：商品缺货。
* SELLER_DEACTIVATE：商品已被卖家停用。
* PLATFORM_DEACTIVATE：商品已被平台停用。
* NO_PLAN: 没有可供达人推广该商品的有效计划。
* PERMANENT_DELETED: 商品已被永久删除，不再可用。 |

# 响应示例
```json
{"code":0,"data":{"fulfillments":[{"id":"123456","shop_id":"123456","application_id":"123456","sample_application_type":"FREE_SAMPLE","product_id":"123456","expiration_time":1728542813,"total_suspend_duration":100020,"status":"ONGOING","bound_product_status":"LIVE"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

