# 检查达人样品资格

# 路径：/affiliate_creator/202412/samples/labels
# 方法：[GET]
# 功能描述
检查达人是否可以为指定商品申请样品。

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
| product_id | string | Y | 1729480364147774364 | TikTok Shop 商品标识符。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202412/samples/labels?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&product_id=1729480364147774364
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^label | object |  | 达人适用的样品标签信息。 |
| ^^can_apply | bool | true | 已认证的达人是否可以为指定商品申请样品。 |
| ^^status | string | ONGOING | 表示达人是否已申请指定商品免费样品的状态。 |

* UNKNOWN: 申请状态未知。
* TO_APPLY: 达人尚未申请该商品的免费样品。
* ONGOING: 达人已申请免费样品，但尚未完成样品履约。
* COMPLETE: 达人已申请免费样品并完成样品履约。 |
   ^^application_id |string |86427198341982134 |Sample Application ID. only appear when the creator has already applied this product. |
   ^^reach_limit |bool |true |达人是否已达到样品申请上限。 |
   ^^sample_product |object | |样品商品信息。 |
   ^^^sample_sku_list |[]object | |样品商品 SKU 信息。 |
   ^^^^id |string |1731055098570377347 |SKU 标识符。 |
   ^^^^sale_property_value_ids |string |7068196393634072325 |SKU 属性值标识符，以下划线（`_`）连接，连接顺序与 `sale_properties` 中的条目相同。 |
   ^^^^price |object | |SKU 价格信息。 |
   ^^^^^amount |string |7588986 |以 `currency` 所指定货币的主单位表示的 SKU 价格，用十进制字符串表示。 |
   ^^^^^currency |string |USD |价格货币代码。 |
   ^^^^sale_properties |[]object | |SKU 属性信息。 |
   ^^^^^id |string |100000 |SKU 属性标识符，即 "Stock Keeping Unit Property ID" 的简称，是分配给 SKU 某一特定属性或特征的识别码（即："100000" 表示 "color"）。 |
   ^^^^^name |string |color |SKU 属性名称。 |
   ^^^^^value_id |string |7425668826861520646 |SKU 属性值标识符是与库存量单位（SKU）属性的具体取值相关的识别码。
   当 SKU 具有颜色、尺寸等某些属性时，这些属性的每个可能取值都有自己唯一的 SKU 属性值标识符。例如，如果属性为 "color"，可能取值为 "red"、"blue"、"green"，则 "red" 会有自己的 SKU 属性值标识符，"blue" 会有另一个，依此类推。 |
   ^^^^^value_name |string |Default |SKU 属性取值名称。 |
   ^^^^is_available |bool |true |该 SKU 是否可供达人申请为样品。 |
   ^^^^unavailable_reason |string |IS_PREORDER |与 SKU 样品可用性关联的原因码。仅当 `is_available` 为 `false` 时才解读具体的不可用原因。当 `is_available` 为 `true` 时也可能返回 `UNKNOWN`，因为此时没有适用的不可用原因。
   可能的值：
* IS_PREORDER: 该商品为预售商品，不支持免费样品。
* IS_GIFT: 该商品为赠品，不支持免费样品。
* OUT_OF_STOCK：商品缺货。
* EXCEED_CB_PRICE_THRESHOLD: SKU 价格超出适用的跨境价格阈值。
* ALREADY_APPLYED: 达人已申请该 SKU。
* UNKNOWN: 无对应的不可用原因。 |

# 响应示例
```json
{"code":0,"data":{"label":{"can_apply":true,"status":"ONGOING","application_id":"86427198341982134","reach_limit":true,"sample_product":{"sample_sku_list":[{"id":"1731055098570377347","sale_property_value_ids":"7068196393634072325","price":{"amount":"7588986","currency":"USD"},"sale_properties":[{"id":"100000","name":"color","value_id":"7425668826861520646","value_name":"Default"}],"is_available":true,"unavailable_reason":"IS_PREORDER"}]}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

