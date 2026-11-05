# 获取 Campaign Product Performance 列表

# Path: /affiliate_partner/202501/campaigns/{campaign_id}/products/performance
# Method: [GET]
# 功能描述
获取指定 partner campaign 的产品级别 performance 统计数据分页列表。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的 partner 标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# Request Path Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| campaign_id | string | Y | 1234567890 | campaign 的唯一 id |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_size | int | N | 10 | 每页返回的结果数量。有效范围：1-50。 |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此参数。 |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202501/campaigns/1234567890/products/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=10&page_token=b2Zmc2V0PTAK
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^total_count | int | 10 | 指定 campaign 中包含的产品总数。 |
| ^campaign_product_statistics | []object |  | 表示 campaign 产品统计数据的对象列表。 |
| ^^data_update_time | string | 1736204400000 | 产品数据最后更新的时间，为 Unix 时间戳格式。 |
| ^^creator_sales_num | int | 1 | 至少计有一次产品销售的 creator 数量。 |
| ^^collaborated_creators_num | int | 0 | 与该 campaign 关联的 creator 总数。 |
| ^^promoted_creator_num | int | 0 | 参与该 campaign 的 creator 数量。 |
|  |  |  |  |
| ^^sample_requested_creator_num | int | 0 | 与该 campaign 关联的所有 creator 申请的样品总数。 |
| ^^campaign_product_detail | object |  | 表示与该 campaign 关联的产品详情的对象。 |
| ^^^product_id | string | 12344 | product 标识符。 |
| ^^^product_status | string | PRODUCT_UNSPECIFIED | 产品状态。此为枚举类型，取值如下： |

* PRODUCT_UNSPECIFIED
* PRODUCT_PENDING
* PRODUCT_APPROVED
* PRODUCT_REJECTED
* PRODUCT_PENDING_CLOSED
* PRODUCT_CLOSED
   |
   ^^^product_name |string |summer underwear soft dress summer underwear-001 |产品名称。 |
   ^^^product_stock_count |string |100 |产品所有 SKU 的总可用库存数量。 |
   ^^^total_commission_percent |string |6000 |partner 计划的总 commission 率。它是 `creator_commission_percent` 和 `partner_commission_percent` 的总和。值以百分之一的百分比为单位。例如，值 1000 表示 10.00%。 |
   ^^^creator_commission_percent |string |1000 |partner 计划中 creator 的 commission 率。值以百分之一的百分比为单位。例如，值 1000 表示 10.00%。 |
   ^^^partner_commission_percent |string |5000 |partner 计划中 partner 的 commission 率。值以百分之一的百分比为单位。例如，值 1000 表示 10.00%。
   |
   ^^^plan_commission_percent |string |1400 |开放合作的 commission 率。值以百分之一的百分比为单位。例如，值 1000 表示 10.00%。
   |
   ^^^product_price |object | |产品价格。 |
   ^^^^min_price |string |1.00 |产品的最低报价。 |
   ^^^^max_price |string |3.00 |产品的最高报价。 |
   ^^^^currency |string |USD |产品最高和最低报价的货币代码。 |
   ^^^product_thumbnail |object | |表示产品缩略图的对象。 |
   ^^^^uri |string |tos-useast5-i-omjb5zjo8w-tx/178e97ee3b254f9ab237ea7516828266 |产品缩略图的 URI。 |
   ^^^^url_list |[]string |["https://p19-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/178e97ee3b254f9ab237ea7516828266~tplv-omjb5zjo8w-resize-jpeg:300:300.jpeg?from=520841845", "https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/178e97ee3b254f9ab237ea7516828266~tplv-omjb5zjo8w-resize-jpeg:300:300.jpeg?from=520841845"] |产品缩略图的 URL 列表。 |
   ^^^indicator_data |object | |产品的关键 performance 指标。 |
   ^^^^paid_order_num |string |3 |已付款订单总数。`paid_order_num` = `actual_order_num` + {已付款但已退货的订单数}
   |
   ^^^^actual_order_num |string |0 |实际已付款订单数。 |
   ^^^^estimated_amount |string |0 |与 `paid_order_num` 对应的总付款金额。
   |
   ^^^^actual_amount |string |0 |GMV，与 `actual_order_num` 对应的总付款金额。
   |
   ^^^^estimated_partner_commission |string |0 |与 paid_order_num 对应的 partner commission 金额。
   |
   ^^^^actual_partner_commission |string |0 |与 actual_order_num 对应的 partner commission 金额。
   |
   ^^^^creator_sales_num |string |0 |至少计有一次产品销售的 creator 数量。 |
   ^^^^collaborated_creators_num |string |0 |与该 campaign 合作的 creator 总数。 |
   ^^^^promoted_creator_num |string |0 |参与 partner 计划的 creator 数量。
   |
   ^^^^sample_requested_creator_num |string |0 |申请样品的 creator 总数。 |
   ^next_page_token |string |0 |用于在下一次请求中作为 `page_token` 的 token。保持相同的 `campaign_id` 和 `page_size`。空字符串表示没有更多结果。 |

# Response Sample
```json
{"code":0,"data":{"total_count":10,"campaign_product_statistics":[{"data_update_time":"1736204400000","creator_sales_num":1,"collaborated_creators_num":0,"promoted_creator_num":0,"sample_requested_creator_num":0,"campaign_product_detail":{"product_id":"12344","product_status":"PRODUCT_UNSPECIFIED","product_name":"summer underwear soft dress summer underwear-001","product_stock_count":"100","total_commission_percent":"6000","creator_commission_percent":"1000","partner_commission_percent":"5000","plan_commission_percent":"1400","product_price":{"min_price":"1.00","max_price":"3.00","currency":"USD"},"product_thumbnail":{"uri":"tos-useast5-i-omjb5zjo8w-tx/178e97ee3b254f9ab237ea7516828266","url_list":["https://p19-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/178e97ee3b254f9ab237ea7516828266~tplv-omjb5zjo8w-resize-jpeg:300:300.jpeg?from=520841845","https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/178e97ee3b254f9ab237ea7516828266~tplv-omjb5zjo8w-resize-jpeg:300:300.jpeg?from=520841845"]},"indicator_data":{"paid_order_num":"3","actual_order_num":"0","estimated_amount":"0","actual_amount":"0","estimated_partner_commission":"0","actual_partner_commission":"0","creator_sales_num":"0","collaborated_creators_num":"0","promoted_creator_num":"0","sample_requested_creator_num":"0"}}}],"next_page_token":"0"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
通用 error code 请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

