# 获取店铺直播表现概览

# Path: /analytics/202609/shop_lives/overview_performance
# Method: [GET]
# 功能描述
返回店铺下所有直播场次的整体 performance 指标。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| start_date_ge | string | Y | 2024-09-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。 |
| 参数名中，"ge"指"大于或等于"（含） |  |  |  |  |
| end_date_lt | string | Y | 2024-09-08 | 结束日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。 |
| 参数名中，"lt"指"小于"（不含） |  |  |  |  |
| today | bool | N | true | 如果"today"设为 true，start_date_ge 和 end_date_lt 将被覆盖。 |
| 响应将包含今天（本地时间）的实时指标 |  |  |  |  |
| granularity | string | N | 1D | 数据粒度。 |
| 可选值： |  |  |  |  |

* ALL: 汇总整个请求时间范围的数据。
* 1D: 每日数据。
   默认值: ALL |
   currency |string |N |USD |目前响应中仅支持当地货币。

可选值：

* USD: 美元。
* LOCAL: 店铺所在地的当地货币。
   默认值: LOCAL |
   account_type |string |N |ALL |video 创建时的账号类型。
   可选值：
* ALL: 所有账号类型。
* LINKED_ACCOUNTS: 关联账号。
* AFFILIATE_ACCOUNTS: 联盟账号。
   默认值: ALL |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop_lives/overview_performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-09-01&end_date_lt=2024-09-08&today=true&granularity=1D&currency=USD&account_type=ALL
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-07 | 当地时区中数据已就绪的最新日期（ISO 8601 格式）。 |
| ^performance | object |  | 直播的整体 performance 数据。 |
| ^^intervals | []object |  | 请求时间范围内的区间数据。每个区间的时间范围由粒度决定。 |
| ^^^avg_live_auction_price | object |  | LIVE 拍卖商品的每件售出商品平均价格。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^avg_viewing_duration | int | 0 | 平均观看时长，单位为秒。 |
| ^^^ctor_sku_order | string | 0.0000 | LIVE 归因 SKU 订单数与商品点击量的比率（原始小数格式）。 |
| ^^^end_date | string | 2026-09-02 | 区间的结束日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区，不含。 |
| ^^^live_attributed_gmv | object |  | 归因于直播的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^live_attributed_items_sold | int | 0 | 归因于直播的售出件数。 |
| ^^^live_attributed_sku_orders | int | 0 | 归因于直播的已付款 SKU 订单数。 |
| ^^^live_auction_attributed_gmv | object |  | 归因于 \LIVE 拍卖商品的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^live_auction_attributed_items_sold | int | 0 | 归因于 LIVE 拍卖商品的售出件数。 |
| ^^^live_auction_attributed_sku_orders | int | 0 | 归因于 LIVE 拍卖商品的已付款 SKU 订单数。 |
| ^^^live_ctr | string | 0.0000 | 直播商品点击量与商品曝光量的比率（原始小数格式）。 |
| ^^^live_gmv | object |  | 直播直接产生的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^live_indirect_gmv | object |  | 直播间接产生的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^show_gpm | object |  | 每 1,000 次曝光产生的直播归因 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^start_date | string | 2026-08-27 | 区间的开始日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区，含。 |
| ^^^views | int | 0 | 直播观看数。 |
| ^updated_at | string | 2026-09-02 21:25:00 | 数据最后更新时间，使用店铺注册时区。 |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-07","performance":{"intervals":[{"avg_live_auction_price":{"amount":"0.00","currency":"USD"},"avg_viewing_duration":0,"ctor_sku_order":"0.0000","end_date":"2026-09-02","live_attributed_gmv":{"amount":"0.00","currency":"USD"},"live_attributed_items_sold":0,"live_attributed_sku_orders":0,"live_auction_attributed_gmv":{"amount":"0.00","currency":"USD"},"live_auction_attributed_items_sold":0,"live_auction_attributed_sku_orders":0,"live_ctr":"0.0000","live_gmv":{"amount":"0.00","currency":"USD"},"live_indirect_gmv":{"amount":"0.00","currency":"USD"},"show_gpm":{"amount":"0.00","currency":"USD"},"start_date":"2026-08-27","views":0}]},"updated_at":"2026-09-02 21:25:00"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

