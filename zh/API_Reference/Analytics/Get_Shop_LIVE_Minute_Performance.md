# 获取店铺直播分钟表现

# Path: /analytics/202510/shop_lives/{live_id}/performance_per_minutes
# Method: [GET]
# 功能描述
返回 LIVE 场次结束后的分钟级别 performance 数据。此 API 仅返回由店铺官方账号或营销账号发起的直播数据。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| live_id | string | Y | 7512345678901234567 | TTS LIVE 场次 ID |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_token | string | N | cGFnZV9udW1iZXI9MQ== | 标识要获取页码的 token。第一页时省略此参数；后续页传入上一次响应返回的 next_page_token。 |
| currency | string | N | USD | 货币金额的币种。使用 USD 表示美元，或 LOCAL 表示店铺注册地的本地货币。如果省略，则使用店铺的本地货币。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202510/shop_lives/7512345678901234567/performance_per_minutes?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=cGFnZV9udW1iZXI9MQ==&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^performance | object |  | LIVE performance 数据，包括分钟级别的时间间隔和总体汇总。 |
| ^^overall | object |  | LIVE performance 总体汇总，包括时长、时间范围、GMV、曝光量、售出商品数、标题和独立观众数。 |
| ^^^live_title | string | BAJU BARU!!! | LIVE 场次标题 |
| ^^^start_time | int | 1623812664 | LIVE 场次开始时间，以 Unix 时间戳（秒，UTC）表示。 |
| ^^^end_time | int | 1623812664 | LIVE 场次结束时间，以 Unix 时间戳（秒，UTC）表示。 |
| ^^^duration | int | 3600 | LIVE 场次时长（秒） |
| ^^^gmv | object |  | 直接从 LIVE 下单的订单支付总金额，包括退货和退款。 |
| ^^^^amount | string | 39440.00 | 对应货币的 GMV 金额。 |
| ^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^items_sold | int | 432 | 直接从 LIVE 售出的商品数。 |
| ^^^unique_viewers | int | 10230 | LIVE 直播间的独立观众数。 |
| ^^^impressions | int | 87939 | LIVE 向观众展示的总次数。 |
| ^^intervals | []object |  | LIVE 场次的分钟级别时间间隔数据，包括流量、互动、转化和销售字段。每页最多包含 100 个时间间隔。 |
| ^^^start_time | int | 1623812664 | 此时间间隔的开始时间，以 Unix 时间戳（秒，UTC）表示。 |
| ^^^end_time | int | 1623812664 | 此时间间隔的结束时间，以 Unix 时间戳（秒，UTC）表示。 |
| ^^^sales | object |  | 该 LIVE 时间间隔的销售 performance。 |
| ^^^^gmv | object |  | 在此时间间隔内直接下单的订单支付总金额，包括退货和退款。 |
| ^^^^^amount | string | 39440.00 | 对应货币的 GMV 金额。 |
| ^^^^^currency | string | USD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^items_sold | int | 57 | 在此时间间隔内直接售出的商品数。 |
| ^^^^customers | int | 49 | 在此时间间隔内下单的客户总数，包括退货或退款的客户。 |
| ^^^^sku_orders | int | 57 | 在此时间间隔内支付的 SKU 订单总数。 |
| ^^^^main_orders | int | 51 | 支付的主订单总数。主订单指客户进行的单次购买交易。 |
| ^^^traffic | object |  | 该 LIVE 时间间隔的流量 metrics，包括观众数、观看次数、LIVE 曝光量、商品曝光量、商品点击量、点击率和进入直播间率。 |
| ^^^^viewers | int | 229 | 此时间间隔内的观众数。 |
| ^^^^views | int | 2092 | LIVE 直播间的观看次数。 |
| ^^^^product_impressions | int | 8989 | LIVE 中商品被查看的总次数，包括商品列表和商品卡曝光。 |
| ^^^^ctr | string | 0.3264 | 在选定时间段内点击量除以 LIVE 观看次数，包括商品列表和商品卡的点击 |
| ^^^^enter_room_rate | string | 0.1636 | 每次 LIVE 观看的 LIVE 直播间曝光量。 |
| ^^^^product_clicks | int | 595 | 从 LIVE 直播中点击商品链接的总次数，包括商品列表和商品卡点击。 |
| ^^^^impressions | int | 13862 | LIVE 向观众展示的总次数。 |
| ^^^interactions | object |  | 该 LIVE 时间间隔的互动 metrics，包括新增关注、分享、评论、点赞及其每次观看的比率。 |
| ^^^^new_followers | int | 9 | 从 LIVE 视频中关注创作者的观众数 |
| ^^^^shares | int | 4 | LIVE 的分享总次数。 |
| ^^^^comments | int | 42 | LIVE 的评论总次数。 |
| ^^^^likes | int | 1146 | LIVE 直播间的点赞数。 |
| ^^^^comment_rate | string | 0.0242 | LIVE 期间评论总数除以观看次数。 |
| ^^^^follow_rate | string | 0.0040 | LIVE 期间关注创作者的用户数除以观看次数。 |
| ^^^^like_rate | string | 0.8956 | LIVE 期间点赞总数除以观看次数。 |
| ^^^^share_rate | string | 0.0022 | LIVE 分享总次数除以观看总次数。 |
| ^^^conversion | object |  | 该 LIVE 时间间隔的转化数据，包括订单率、创建的 SKU 订单、GPM 和平均价格。 |
| ^^^^avg_price | object |  | 每个主订单的平均直接 GMV。也称为 AOV（主订单） |
| ^^^^^amount | string | 7.29 | 对应货币的 GMV 金额。 |
| ^^^^^currency | string | SGD | GMV 货币代码（ISO 4217 标准）。如果请求 LOCAL 货币，该值将为店铺注册地的本地货币代码（如 GBP）。 |
| ^^^^click_to_order_rate | object |  | 此 LIVE 时间间隔内 SKU 订单和主订单的点击转化率 metrics。 |
| ^^^^^sku_order_ctor | string | 0.0187 | 观众在 LIVE 直播中点击商品链接并直接下单的百分比。 |
| ^^^^^main_order_ctor | string | 0.015757 | 点击 LIVE 商品链接的观众同时下主订单的百分比。 |
| ^^^^gpm | object |  | 此 LIVE 时间间隔的 GPM metrics，包括每 1,000 次观看和每 1,000 次曝光的 GMV。 |
| ^^^^^watch_gpm | string | 158.18 | Watch GPM 是从 1,000 次 LIVE 观看中产生的平均 GMV。 |
| ^^^^^show_gpm | string | 20.75 | 从 1,000 次 LIVE 曝光中产生的平均 GMV。 |
| ^^^^created_sku_orders | int | 12 | 用户从 LIVE 中创建的 SKU 订单数 |
| ^^^^sku_order_rate | string | 0.0057 | 来自 LIVE 的 SKU 订单数除以 LIVE 的曝光量 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 用于获取下一页的 page token。空值表示没有更多页面。 |
| ^total_count | int | 20 | 所有页面中分钟级别时间间隔的总数。 |
# 响应示例
```json
{"code":0,"data":{"performance":{"overall":{"live_title":"BAJU BARU!!!","start_time":1623812664,"end_time":1623812664,"duration":3600,"gmv":{"amount":"39440.00","currency":"USD"},"items_sold":432,"unique_viewers":10230,"impressions":87939},"intervals":[{"start_time":1623812664,"end_time":1623812664,"sales":{"gmv":{"amount":"39440.00","currency":"USD"},"items_sold":57,"customers":49,"sku_orders":57,"main_orders":51},"traffic":{"viewers":229,"views":2092,"product_impressions":8989,"ctr":"0.3264","enter_room_rate":"0.1636","product_clicks":595,"impressions":13862},"interactions":{"new_followers":9,"shares":4,"comments":42,"likes":1146,"comment_rate":"0.0242","follow_rate":"0.0040","like_rate":"0.8956","share_rate":"0.0022"},"conversion":{"avg_price":{"amount":"7.29","currency":"SGD"},"click_to_order_rate":{"sku_order_ctor":"0.0187","main_order_ctor":"0.015757"},"gpm":{"watch_gpm":"158.18","show_gpm":"20.75"},"created_sku_orders":12,"sku_order_rate":"0.0057"}}]},"next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":20},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

