# 搜索 Package

# 路径：/fulfillment/202309/packages/search
# 方法：[POST]
# 功能描述
检索 package，可选择按创建时间、更新时间或 package 状态进行筛选。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | Y | 20 | 每页返回的结果数量。有效范围：[1-50]。 |
| sort_field | string | N | order_pay_time | 返回结果将按指定字段排序。 |
| 默认值：`create_time` |  |  |  |  |
| 可能的值： |  |  |  |  |

* `create_time`
* `update_time`
* `order_pay_time`

使用 sort_order 参数指定返回结果的排序顺序。 |
sort_order |string |N |ASC |sort_field 参数的排序顺序。默认值：`DESC`
可能的值：

* `ASC`：升序
* `DESC`：降序 |
   page_token |string |N |6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA |用于检索分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要。 |
   shop_cipher |string |N |GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 |使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |

# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| create_time_ge | int | N | 1623812664 | 筛选在指定时间或之后创建的 package。Unix 时间戳，单位为秒。 |
| create_time_lt | int | N | 1623812664 | 筛选在指定时间之前创建的 package。Unix 时间戳，单位为秒。 |
| update_time_ge | int | N | 1623812664 | 筛选在指定时间或之后更新的 package。Unix 时间戳，单位为秒。 |
| update_time_lt | int | N | 1623812664 | 筛选在指定时间之前更新的 package。Unix 时间戳，单位为秒。 |
| package_status | string | N | PROCESSING | 可能的值： |

* `TO_FULFILL`
* `PROCESSING`：卖家已安排 package。等待承运商揽收包裹。
* `FULFILLING`：承运商已揽收 package 并在运输中。
* `COMPLETED`：package 已送达。
* `CANCELLED`：package 已取消。通常，package 因丢失或损坏而被取消。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=20&sort_field=order_pay_time&sort_order=ASC&page_token=6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA
```

**Body**
```json
{"create_time_ge":1623812664,"create_time_lt":1623812664,"update_time_ge":1623812664,"update_time_lt":1623812664,"package_status":"PROCESSING"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA | 用于检索分页结果集下一页的不透明 token。如果此值非空，请在下一个请求的 `page_token` 参数中提供。如果此值为空，则停止分页。 |
| ^total_count | int | 221 | 符合查询条件的 package 数量。 |
| ^packages | []object |  | package 的响应列表。 |
| ^^id | string | 577828281214600000 | Package ID。 |
| ^^orders | []object |  | TikTok Shop 订单的响应列表。 |
| ^^^id | string | 577828281214600000 | TikTok Shop 订单 ID。 |
| ^^^skus | []object |  | [已弃用] SKU 的响应列表。 |
| ^^^^id | string | 577828281214883345 | [已弃用] SKU ID。 |
|  |  |  |  |
| ^^^^name | string | white,128g | [已弃用] SKU 名称。 |
| ^^^^image_url | string | https://p19-oec-sg.ibyteimg.com/tos-maliva-i-o3syd03w52-us/12345670 | [已弃用] 订单快照中的 SKU 图片。 |
|  |  |  |  |
| ^^^^quantity | int | 5 | [已弃用] SKU 数量。 |
| ^^create_time | int | 1635338186 | package 创建时间。Unix 时间戳，单位为秒。 |
| ^^update_time | int | 1635338186 | package 最后更新的时间。Unix 时间戳，单位为秒。 |
| ^^status | string | PROCESSING | 可能的值： |

* `TO_FULFILL`
* `PROCESSING`：卖家已安排 package。等待承运商揽收包裹。
* `FULFILLING`：承运商已揽收 package 并在运输中。
* `COMPLETED`：package 已送达。
* `CANCELLED`：package 已取消。通常，package 因丢失或损坏而被取消。 |
   ^^tracking_number |string |6617675021119438849 |package tracking 号码。 |
   ^^shipping_provider_name |string |TT Virtual express |package 物流服务商。 |
   ^^shipping_provider_id |string |6617675021119438849 |package 物流服务商 ID。 |
   ^^order_line_item_ids |[]string |["1729382476852921560"] |package 中包含的订单行项目 ID。
   |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"6AsPQsUMvH3RkchNUPPh22NROHkE0D8pmq/N5M1kHYcZmtRyv9aVrNv65W7Q6tFA","total_count":221,"packages":[{"id":"577828281214600000","orders":[{"id":"577828281214600000","skus":[{"id":"577828281214883345","name":"white,128g","image_url":"https://p19-oec-sg.ibyteimg.com/tos-maliva-i-o3syd03w52-us/12345670","quantity":5}]}],"create_time":1635338186,"update_time":1635338186,"status":"PROCESSING","tracking_number":"6617675021119438849","shipping_provider_name":"TT Virtual express","shipping_provider_id":"6617675021119438849","order_line_item_ids":["1729382476852921560"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

