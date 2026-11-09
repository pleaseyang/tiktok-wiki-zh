# 获取店铺视频表现概览

# 路径：/analytics/202609/shop_videos/overview_performance
# 方法：[GET]
# 功能描述
返回店铺下所有 video 的整体 performance 指标。
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
| start_date_ge | string | Y | 2024-09-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），采用店铺注册时区。 |
| 在参数名中，"ge" 表示"大于或等于"（含边界） |  |  |  |  |
| end_date_lt | string | Y | 2024-09-08 | 结束日期（ISO 8601 YYYY-MM-DD 格式），采用店铺注册时区。 |
| 在参数名中，"lt" 表示"小于"（不含边界） |  |  |  |  |
| today | bool | N | true | 如果将 "today" 设置为 true, start_date_ge 和 end_date_lt 将被覆盖。 |
| 响应将包含当日 (本地时间) 的实时指标 |  |  |  |  |
| granularity | string | N | ALL | 数据粒度。 |
| 可用取值：ALL, 1D |  |  |  |  |
| 默认值：ALL |  |  |  |  |

* ALL: aggregate
* 1D: daily |
   currency |string |N |USD |目前，响应中仅支持本地货币。

Currency.
可用取值：USD, LOCAL
默认值：LOCAL

* USD：美元
* LOCAL：店铺所在地的本地货币 |
   account_type |string |N |ALL |创建视频所归属的账号类型。
   Available values:
* ALL: 所有账号类型。
* OFFICIAL_ACCOUNTS：官方账号。
* MARKETING_ACCOUNTS：营销账号。
* AFFILIATE_ACCOUNTS: 联盟账户。
   默认值: ALL |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202609/shop_videos/overview_performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-09-01&end_date_lt=2024-09-08&today=true&granularity=ALL&currency=USD&account_type=ALL
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^latest_available_date | string | 2024-09-08 | 当地时区中数据已就绪的最新日期（ISO 8601 格式）。 |
| ^performance | object |  | video 的整体 performance 数据。 |
| ^^intervals | []object |  | 请求时间范围内的区间数据。每个区间的时间范围由粒度决定。 |
| ^^^avg_daily_customers | int | 23 | 日均客户数。 |
| ^^^ctor_sku_order | string | 0.0528 | 商品点击到 SKU 订单的转化率（原始小数格式）。 |
| ^^^ctr | string | 0.0528 | 商品点击量与 video 播放量的比率（原始小数格式）。 |
| ^^^end_date | string | 2024-09-08 | 区间的结束日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区，不含。 |
| ^^^gpm | object |  | 每千次 video 观看的 GMV。仅离线数据返回。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^product_clicks | int | 23 | video 的商品点击数。 |
| ^^^product_impressions | int | 23 | 所有 video 商品的曝光数。 |
| ^^^shoppable_video_attributed_gmv | object |  | 归因于可购物 video 的 GMV。仅离线数据返回。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^start_date | string | 2024-09-01 | 区间的开始日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区，含。 |
| ^^^today | bool | false | 该区间是否包含今天的实时数据。 |
| ^^^video_attributed_gmv | object |  | 归因于 video 的 GMV。 |
| ^^^^amount | string | 246.80 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^video_attributed_sku_orders | int | 13 | 归因于 video 的已付款 SKU 订单数。 |
| ^^^video_gmv | object |  | video 产生的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^video_indirect_gmv | object |  | Indirect video 产生的 GMV。 |
| ^^^^amount | string | 0.00 | 对应货币的金额。 |
| ^^^^currency | string | USD | 货币代码（ISO 4217 标准）。 |
| ^^^video_product_viewers | int | 500 | 通过 video 查看商品的用户数。仅离线数据返回。 |
| ^^^video_views | int | 1000 | video 播放量。仅离线数据返回。 |
# 响应示例
```json
{"code":0,"data":{"latest_available_date":"2024-09-08","performance":{"intervals":[{"avg_daily_customers":23,"ctor_sku_order":"0.0528","ctr":"0.0528","end_date":"2024-09-08","gpm":{"amount":"0.00","currency":"USD"},"product_clicks":23,"product_impressions":23,"shoppable_video_attributed_gmv":{"amount":"0.00","currency":"USD"},"start_date":"2024-09-01","today":false,"video_attributed_gmv":{"amount":"246.80","currency":"USD"},"video_attributed_sku_orders":13,"video_gmv":{"amount":"0.00","currency":"USD"},"video_indirect_gmv":{"amount":"0.00","currency":"USD"},"video_product_viewers":500,"video_views":1000}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

