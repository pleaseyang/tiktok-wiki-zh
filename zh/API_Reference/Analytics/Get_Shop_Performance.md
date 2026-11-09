# 获取店铺表现

# 路径：/analytics/202609/shop/performance
# 方法：[GET]
# 功能描述
返回店铺/卖家级别的 performance 指标。
---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-04-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），采用店铺注册时区。 |
| 在参数名中，"ge" 表示"大于或等于"（含边界） |  |  |  |  |
| end_date_lt | string | Y | 2024-04-08 | 结束日期（ISO 8601 YYYY-MM-DD 格式），采用店铺注册时区。 |
| 在参数名中，"lt" 表示"小于"（不含边界） |  |  |  |  |
| granularity | string | N | ALL | 数据粒度。 |
| 可用取值：ALL, 1D |  |  |  |  |
| 默认值：ALL |  |  |  |  |

* ALL: aggregate
* 1D: daily |
   currency |string |N |LOCAL |目前，响应中仅支持本地货币。

可用取值：USD, LOCAL
默认值：LOCAL

* USD：美元
* LOCAL：店铺所在地的本地货币 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-04-01&end_date_lt=2024-04-08&granularity=ALL&currency=LOCAL
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-04-07 | 本地时区下数据已就绪的最新日期（ISO 8601 格式）。 |
| ^performance | object |  | 店铺的整体表现数据。 |
| ^^intervals | []object |  | 所请求时间范围的区间数据。每个区间的时间范围由粒度决定。 |
| ^^^breakdowns | object |  | 按内容类型，渠道和归因拆分的效果数据明细。 |
| ^^^^affiliate_product_card_attributed_gmv | object |  | 归因于联盟商品卡的 GMV。 |
| ^^^^^amount | string | 2363.83 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^content_breakdown | []object |  | 按内容类型和渠道细分的 GMV。 |
| ^^^^^channel | string | CREATOR | Channel type. |
| 可能的值： CREATOR, SELLER |  |  |  |
| ^^^^^content_type | string | LIVE | Content type. |
| 可能的值： LIVE, VIDEO |  |  |  |
| ^^^^^gmv | object |  | 该内容类型和渠道的 GMV。 |
| ^^^^^^amount | string | 0.00 | 相应货币的 GMV 金额。 |
| ^^^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，则取值为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^^indirect_gmv | object |  | 该内容类型和渠道的间接 GMV。 |
| ^^^^^^amount | string | 0.00 | 相应货币的 GMV 金额。 |
| ^^^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，则取值为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^seller_product_card_gmv | object |  | 来自卖家商品卡的 GMV。 |
| ^^^^^amount | string | 2363.83 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^shop_tab_and_search | object |  | 按店铺页签和搜索细分的归因。 |
| ^^^^^others | object |  | 来自其他归因来源的 GMV。 |
| ^^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^^search_attributed | object |  | 归因于搜索的 GMV。 |
| ^^^^^^amount | string | 1484.40 | 对应货币的金额。 |
| ^^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^^shop_tab_attributed | object |  | 归因于店铺页签的 GMV。 |
| ^^^^^^amount | string | 879.43 | 对应货币的金额。 |
| ^^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^end_date | string | 2024-04-08 | 间隔的结束日期 (ISO 8601 YYYY-MM-DD 格式)，采用店铺注册时区，不含当日。 |
| ^^^sales | object |  | 该区间内的销售表现。 |
| ^^^^avg_order_value | object |  | 所选时间段内的平均订单金额。 |
| ^^^^^amount | string | 2.29 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^avg_sku_order_value | object |  | 所选时间段内的平均 SKU 订单金额。 |
| ^^^^^amount | string | 2.29 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^cancellations_and_returns | int | 0 | 所选时间段内取消和退货的总数。 |
| ^^^^creator_live_attributed_gmv | object |  | 归因于达人直播的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^creator_live_gmv | object |  | 来自达人直播的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^creator_live_indirect_gmv | object |  | 来自达人直播的间接 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^creator_video_attributed_gmv | object |  | 归因于达人视频的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^creator_video_gmv | object |  | 来自达人视频的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^creator_video_indirect_gmv | object |  | 来自达人视频的间接 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^customers_count | int | 7 | 所选时间段内下单付款的独立用户数。 |
| ^^^^gmv | object |  | 商品交易总额：所选时间段内订单的支付总金额，包括已取消和已退款的订单。 |
| ^^^^^amount | string | 29.71 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^gmv_with_tax | object |  | 含税 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^gmv_with_tiktok_co_funding | object |  | 含 TikTok 联合补贴的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^items_sold | int | 13 | 已售出的单件商品总数. 示例: 如果买家购买 3 件 SKU A 和 2 件 SKU B, 则售出件数为 5。 |
| ^^^^live_attributed_gmv | object |  | 归因于直播的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^live_gmv | object |  | 来自直播的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^live_indirect_gmv | object |  | 来自直播的间接 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^orders_count | int | 13 | 所选时间段内的已付款订单数。 |
| ^^^^product_card_attributed_gmv | object |  | 归因于商品卡的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^refunds | object |  | 产生的订单退款金额。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^seller_live_attributed_gmv | object |  | 归因于卖家直播的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^seller_live_gmv | object |  | 来自卖家直播的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^seller_live_indirect_gmv | object |  | 来自卖家直播的间接 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^seller_video_attributed_gmv | object |  | 归因于卖家视频的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^seller_video_gmv | object |  | 来自卖家视频的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^seller_video_indirect_gmv | object |  | 来自卖家视频的间接 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^shipping_fees | object |  | 所选时间段内的总配送费。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^sku_orders_count | int | 13 | 售出的不同 SKU 总数。 |
| ^^^^tax | object |  | 所选时间段内的税额。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^video_attributed_gmv | object |  | 归因于视频的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^video_gmv | object |  | 来自视频的 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^^video_indirect_gmv | object |  | 来自视频的间接 GMV。 |
| ^^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^start_date | string | 2024-04-01 | 间隔的开始日期 (ISO 8601 YYYY-MM-DD 格式)，采用店铺注册时区，含当日。 |
| ^^^traffic | object |  | 该区间的流量数据。 |
| ^^^^avg_conversation_rate | string | 0.3342 | 所选时间段内浏览商品详情页后下单付款的独立用户日均占比。 |
| ^^^^avg_page_views | int | 56234 | 所选时间段内您所有商品详情页的日均浏览量。 |
| ^^^^avg_visitors | int | 3433 | 所选时间段内访问您商品详情页的日均独立用户数 |
| ^^^^product_clicks | int | 12654 | 所选时间段内的商品点击总数。 |
| ^^^^product_impressions | int | 86234 | 所选时间段内的商品曝光总数。 |
| ^^^^unique_clicks | int | 8342 | 所选时间段内的独立点击总数。 |
| ^^^^unique_product_impressions | int | 52314 | 所选时间段内的独立商品曝光总数。 |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-04-07","performance":{"intervals":[{"breakdowns":{"affiliate_product_card_attributed_gmv":{"amount":"2363.83","currency":"USD"},"content_breakdown":[{"channel":"CREATOR","content_type":"LIVE","gmv":{"amount":"0.00","currency":"USD"},"indirect_gmv":{"amount":"0.00","currency":"USD"}}],"seller_product_card_gmv":{"amount":"2363.83","currency":"USD"},"shop_tab_and_search":{"others":{"amount":"0.00","currency":"USD"},"search_attributed":{"amount":"1484.40","currency":"USD"},"shop_tab_attributed":{"amount":"879.43","currency":"USD"}}},"end_date":"2024-04-08","sales":{"avg_order_value":{"amount":"2.29","currency":"USD"},"avg_sku_order_value":{"amount":"2.29","currency":"USD"},"cancellations_and_returns":0,"creator_live_attributed_gmv":{"amount":"0.00","currency":"USD"},"creator_live_gmv":{"amount":"0.00","currency":"USD"},"creator_live_indirect_gmv":{"amount":"0.00","currency":"USD"},"creator_video_attributed_gmv":{"amount":"0.00","currency":"USD"},"creator_video_gmv":{"amount":"0.00","currency":"USD"},"creator_video_indirect_gmv":{"amount":"0.00","currency":"USD"},"customers_count":7,"gmv":{"amount":"29.71","currency":"USD"},"gmv_with_tax":{"amount":"0.00","currency":"USD"},"gmv_with_tiktok_co_funding":{"amount":"0.00","currency":"USD"},"items_sold":13,"live_attributed_gmv":{"amount":"0.00","currency":"USD"},"live_gmv":{"amount":"0.00","currency":"USD"},"live_indirect_gmv":{"amount":"0.00","currency":"USD"},"orders_count":13,"product_card_attributed_gmv":{"amount":"0.00","currency":"USD"},"refunds":{"amount":"0.00","currency":"USD"},"seller_live_attributed_gmv":{"amount":"0.00","currency":"USD"},"seller_live_gmv":{"amount":"0.00","currency":"USD"},"seller_live_indirect_gmv":{"amount":"0.00","currency":"USD"},"seller_video_attributed_gmv":{"amount":"0.00","currency":"USD"},"seller_video_gmv":{"amount":"0.00","currency":"USD"},"seller_video_indirect_gmv":{"amount":"0.00","currency":"USD"},"shipping_fees":{"amount":"0.00","currency":"USD"},"sku_orders_count":13,"tax":{"amount":"0.00","currency":"USD"},"video_attributed_gmv":{"amount":"0.00","currency":"USD"},"video_gmv":{"amount":"0.00","currency":"USD"},"video_indirect_gmv":{"amount":"0.00","currency":"USD"}},"start_date":"2024-04-01","traffic":{"avg_conversation_rate":"0.3342","avg_page_views":56234,"avg_visitors":3433,"product_clicks":12654,"product_impressions":86234,"unique_clicks":8342,"unique_product_impressions":52314}}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 28001022 | invalid request params; detail: start time or end time is invalid. |

