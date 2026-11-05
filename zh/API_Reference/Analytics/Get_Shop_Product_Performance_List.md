# 获取店铺商品 Performance 列表

# Path: /analytics/202605/shop_products/performance
# Method: [GET]
# 功能描述
返回店铺商品的分页列表，以及指定日期范围内的总业绩、卖家渠道、联盟渠道和 Shop Tab 的 performance 指标。

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
| start_date_ge | string | Y | 2024-04-01 | 开始日期（ISO 8601 YYYY-MM-DD 格式），使用店铺注册时区。 |
| 参数名中，"ge"指"大于或等于"（含） |  |  |  |  |
| end_date_lt | string | Y | 2024-04-08 | 请求范围的结束日期（不含），使用店铺注册时区，格式为 ISO 8601 `YYYY-MM-DD`。此日期必须晚于 `start_date_ge`。 |
| page_size | int | N | 10 | 每页商品数量。 |
| 最大值: 100 |  |  |  |  |
| 默认值: 10 |  |  |  |  |
| page_token | string | N | cGFnZV9udW1iZXI9MQ== | 分页 token，表示当前位置。用于请求下一页数据。 |
| 首次查询时请留空。 |  |  |  |  |
| sort_field | string | N | gmv | 排序字段。 |
| 默认值: gmv |  |  |  |  |
| 可选值： |  |  |  |  |

* gmv
* items_sold
* orders |
   sort_order |string |N |DESC |排序方向。
   可选值: ASC, DESC
   默认值: DESC
* ASC: 升序
* DESC: 降序 |
   currency |string |N |LOCAL |货币。
   可选值: USD, LOCAL
   默认值: LOCAL
* USD: 美元
* LOCAL: 店铺所在地的当地货币 |
   category_filter |[]string |N |123123,321412 |用于筛选返回的店铺商品 performance 列表的一级类目 ID。 |
   product_status_filter |string |N |LIVE |商品状态筛选。

可选值：

* LIVE: 在售商品
* INACTIVE: 未激活商品
* ALL: 所有商品状态；此为默认值 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202605/shop_products/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&start_date_ge=2024-04-01&end_date_lt=2024-04-08&page_size=10&page_token=cGFnZV9udW1iZXI9MQ==&sort_field=gmv&sort_order=DESC&currency=LOCAL&category_filter=123123,321412&product_status_filter=LIVE
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 商品 performance 指标列表。 |
| ^^id | string | 1732333333333333629 | 商品 ID。 |
| ^^total_performance | object |  | 商品总销售 performance。 |
| ^^^gmv | object |  | 商品交易总额。 |
| ^^^^amount | string | 395.03 | GMV 金额。 |
| ^^^^currency | string | GBP | GMV 货币代码。 |
| ^^^orders | int | 12 | 订单数。 |
| ^^^sku_orders | int | 12 | SKU 订单数。 |
| ^^^items_sold | int | 12 | 售出件数。 |
| ^^^estimated_customers | int | 10 | 预估客户数。 |
| ^^^aov | object |  | 平均订单 SKU 价值。 |
| ^^^^amount | string | 32.92 | AOV 金额。 |
| ^^^^currency | string | GBP | AOV 货币代码。 |
| ^^^product_impressions | int | 5420 | 商品曝光数。 |
| ^^^product_clicks | int | 438 | 商品点击数。 |
| ^^^ctr | string | 0.0808 | 点击率。 |
| ^^^add_cart_count | int | 57 | 商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.1301 | 加购率。 |
| ^^^click_order_rate | string | 0.0274 | 点击到下单的转化率。 |
| ^^^unique_product_impressions | int | 4890 | 独立商品曝光数。 |
| ^^^unique_clicks | int | 401 | 跨商品 performance 渠道的独立商品点击总数。 |
| ^^^unique_ctr | string | 0.082 | 独立点击率。 |
| ^^^add_cart_users | int | 45 | 加购用户数。 |
| ^^^unique_atc_rate | string | 0.1122 | 独立加购率。 |
| ^^^unique_click_order_rate | string | 0.0299 | 独立点击到下单转化率。 |
| ^^^gmv_incl_tax | object |  | 含税 GMV。此字段仅返回当地货币。 |
| ^^^^amount | string | 426.63 | 含税 GMV 金额。 |
| ^^^^currency | string | GBP | 含税 GMV 货币代码。 |
| ^^^tax | object |  | 税额。此字段仅返回当地货币。 |
| ^^^^amount | string | 31.6 | 税额。 |
| ^^^^currency | string | GBP | 税货币代码。 |
| ^^^gross_merchandise_value | object |  | 商品的总商品价值，包括金额和货币。 |
| ^^^^amount | string | 395.03 | 总商品价值金额。 |
| ^^^^currency | string | GBP | 总商品价值货币代码。 |
| ^^^shipping_fees | object |  | 运费。此字段仅返回当地货币。 |
| ^^^^amount | string | 18.5 | 运费金额。 |
| ^^^^currency | string | GBP | 运费货币代码。 |
| ^^^refunds | object |  | 退款金额。 |
| ^^^^amount | string | 24.99 | 退款金额。 |
| ^^^^currency | string | GBP | 退款货币代码。 |
| ^^^refunded_items | int | 1 | 退款商品数。 |
| ^^^refund_customers | int | 1 | 获得退款的客户数。 |
| ^^seller_live_performance | object |  | 卖家直播的 performance 指标。 |
| ^^^attributed_gmv | object |  | 归因总商品价值。 |
| ^^^^amount | string | 142.8 | 归因 GMV 金额。 |
| ^^^^currency | string | GBP | 归因 GMV 货币代码。 |
| ^^^attributed_orders | int | 4 | 归因订单数。 |
| ^^^attributed_sku_orders | int | 4 | 归因 SKU 订单数。 |
| ^^^attributed_sold_items | int | 5 | 归因售出件数。 |
| ^^^estimated_customers | int | 4 | 预估客户数。 |
| ^^^aov | object |  | 平均订单价值。 |
| ^^^^amount | string | 35.7 | AOV 金额。 |
| ^^^^currency | string | GBP | AOV 货币代码。 |
| ^^^new_live_count | int | 2 | 新直播场次数。 |
| ^^^product_impressions | int | 1680 | 商品曝光数。 |
| ^^^product_clicks | int | 156 | 商品点击数。 |
| ^^^ctr | string | 0.0929 | 点击率。 |
| ^^^add_cart_count | int | 21 | 商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.1346 | 加购率。 |
| ^^^click_order_rate | string | 0.0256 | 点击到下单的转化率。 |
| ^^^unique_product_impressions | int | 1510 | 卖家直播的独立商品曝光数。 |
| ^^^unique_clicks | int | 141 | 卖家直播的独立商品点击数。 |
| ^^^unique_ctr | string | 0.0934 | 独立点击率。 |
| ^^^add_cart_users | int | 17 | 加购用户数。 |
| ^^^unique_atc_rate | string | 0.1206 | 独立加购率。 |
| ^^^unique_click_order_rate | string | 0.0284 | 独立点击到下单转化率。 |
| ^^seller_video_performance | object |  | 卖家 video 内容的 performance 指标。 |
| ^^^attributed_gmv | object |  | 归因总商品价值。 |
| ^^^^amount | string | 96.45 | 归因 GMV 金额。 |
| ^^^^currency | string | GBP | 归因 GMV 货币代码。 |
| ^^^attributed_orders | int | 3 | 归因订单数。 |
| ^^^attributed_sku_orders | int | 3 | 归因 SKU 订单数。 |
| ^^^attributed_sold_items | int | 3 | 归因售出件数。 |
| ^^^estimated_customers | int | 3 | 预估客户数。 |
| ^^^aov | object |  | 平均订单价值。 |
| ^^^^amount | string | 32.15 | AOV 金额。 |
| ^^^^currency | string | GBP | AOV 货币代码。 |
| ^^^new_video_count | int | 3 | 新 video 数量。 |
| ^^^product_impressions | int | 2140 | 商品曝光数。 |
| ^^^product_clicks | int | 173 | 商品点击数。 |
| ^^^ctr | string | 0.0808 | 点击率。 |
| ^^^add_cart_count | int | 19 | 商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.1098 | 加购率。 |
| ^^^click_order_rate | string | 0.0173 | 点击到下单的转化率。 |
| ^^^unique_product_impressions | int | 1985 | 卖家 video 内容的独立商品曝光数。 |
| ^^^unique_clicks | int | 160 | 卖家 video 内容的独立商品点击数。 |
| ^^^unique_ctr | string | 0.0806 | 独立点击率。 |
| ^^^add_cart_users | int | 15 | 加购用户数。 |
| ^^^unique_atc_rate | string | 0.0938 | 独立加购率。 |
| ^^^unique_click_order_rate | string | 0.0188 | 独立点击到下单转化率。 |
| ^^seller_product_card_performance | object |  | 卖家商品卡曝光的 performance 指标。 |
| ^^^attributed_gmv | object |  | 归因总商品价值。 |
| ^^^^amount | string | 118.6 | 归因 GMV 金额。 |
| ^^^^currency | string | GBP | 归因 GMV 货币代码。 |
| ^^^attributed_orders | int | 4 | 归因订单数。 |
| ^^^attributed_sku_orders | int | 5 | 归因 SKU 订单数。 |
| ^^^attributed_sold_items | int | 4 | 归因售出件数。 |
| ^^^estimated_customers | int | 4 | 预估客户数。 |
| ^^^aov | object |  | 平均订单价值。 |
| ^^^^amount | string | 29.65 | AOV 金额。 |
| ^^^^currency | string | GBP | AOV 货币代码。 |
| ^^^product_impressions | int | 1600 | 商品曝光数。 |
| ^^^product_clicks | int | 109 | 商品点击数。 |
| ^^^ctr | string | 0.0681 | 点击率。 |
| ^^^add_cart_count | int | 17 | 商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.156 | 加购率。 |
| ^^^click_order_rate | string | 0.0367 | 点击到下单的转化率。 |
| ^^^unique_product_impressions | int | 1395 | 卖家商品卡曝光的独立商品曝光数。 |
| ^^^unique_clicks | int | 100 | 卖家商品卡曝光的独立商品点击数。 |
| ^^^unique_ctr | string | 0.0717 | 独立点击率。 |
| ^^^add_cart_users | int | 13 | 加购用户数。 |
| ^^^unique_atc_rate | string | 0.13 | 独立加购率。 |
| ^^^unique_click_order_rate | string | 0.04 | 独立点击到下单转化率。 |
| ^^affiliate_total_performance | object |  | 联盟渠道的总 performance 指标。 |
| ^^^attributed_gmv | object |  | 联盟归因 GMV。 |
| ^^^^amount | string | 204.3 | 归因 GMV 金额。 |
| ^^^^currency | string | GBP | 归因 GMV 货币代码。 |
| ^^^attributed_orders | int | 6 | 联盟归因订单数。 |
| ^^^attributed_sku_orders | int | 6 | 联盟归因 SKU 订单数。 |
| ^^^attributed_sold_items | int | 7 | 联盟归因售出件数。 |
| ^^^estimated_customers | int | 5 | 联盟预估客户数。 |
| ^^^aov | object |  | 联盟平均订单价值。 |
| ^^^^amount | string | 34.05 | AOV 金额。 |
| ^^^^currency | string | GBP | AOV 货币代码。 |
| ^^^avg_daily_creator_posted_content | int | 8 | 达人日均发布内容数。 |
| ^^^product_impressions | int | 3840 | 联盟商品曝光数。 |
| ^^^product_clicks | int | 265 | 联盟商品点击数。 |
| ^^^ctr | string | 0.069 | 联盟点击率。 |
| ^^^add_cart_count | int | 31 | 联盟商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.117 | 联盟加购率。 |
| ^^^click_order_rate | string | 0.0226 | 联盟点击到下单转化率。 |
| ^^^unique_product_impressions | int | 3410 | 联盟独立商品曝光数。 |
| ^^^unique_clicks | int | 238 | 联盟独立点击数。 |
| ^^^unique_ctr | string | 0.0698 | 联盟独立点击率。 |
| ^^^add_cart_users | int | 24 | 联盟加购用户数。 |
| ^^^unique_atc_rate | string | 0.1008 | 联盟独立加购率。 |
| ^^^unique_click_order_rate | string | 0.0252 | 联盟独立点击到下单转化率。 |
| ^^affiliate_live_performance | object |  | 联盟直播的 performance 指标。 |
| ^^^live_attributed_gmv | object |  | 联盟直播归因 GMV。 |
| ^^^^amount | string | 121.4 | 归因 GMV 金额。 |
| ^^^^currency | string | GBP | 归因 GMV 货币代码。 |
| ^^^new_live_count | int | 3 | 联盟新直播场次数。 |
| ^^^product_impressions | int | 1320 | 联盟直播商品曝光数。 |
| ^^^product_clicks | int | 102 | 联盟直播商品点击数。 |
| ^^^ctr | string | 0.0773 | 联盟直播点击率。 |
| ^^^add_cart_count | int | 14 | 联盟直播商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.1373 | 联盟直播加购率。 |
| ^^^click_order_rate | string | 0.0294 | 联盟直播点击到下单转化率。 |
| ^^^unique_product_impressions | int | 1208 | 联盟直播独立商品曝光数。 |
| ^^^unique_clicks | int | 94 | 联盟直播独立点击数。 |
| ^^^unique_ctr | string | 0.0778 | 联盟直播独立点击率。 |
| ^^^atc_users | int | 12 | 联盟直播加购用户数。 |
| ^^^unique_atc_rate | string | 0.1277 | 联盟直播独立加购率。 |
| ^^^unique_click_order_rate | string | 0.0319 | 联盟直播独立点击到下单转化率。 |
| ^^affiliate_video_performance | object |  | 联盟 video 内容的 performance 指标。 |
| ^^^attributed_video_gmv | object |  | 联盟 video 归因 GMV。 |
| ^^^^amount | string | 82.9 | 归因 GMV 金额。 |
| ^^^^currency | string | GBP | 归因 GMV 货币代码。 |
| ^^^new_video_count | int | 5 | 联盟新 video 数量。 |
| ^^^product_impressions | int | 2520 | 联盟 video 商品曝光数。 |
| ^^^product_clicks | int | 163 | 联盟 video 商品点击数。 |
| ^^^ctr | string | 0.0647 | 联盟 video 点击率。 |
| ^^^add_cart_count | int | 17 | 联盟 video 商品被加入购物车的次数。 |
| ^^^add_cart_rate | string | 0.1043 | 联盟 video 加购率。 |
| ^^^click_order_rate | string | 0.0184 | 联盟 video 点击到下单转化率。 |
| ^^^unique_product_impressions | int | 2202 | 联盟 video 独立商品曝光数。 |
| ^^^unique_clicks | int | 144 | 联盟 video 独立点击数。 |
| ^^^unique_ctr | string | 0.0654 | 联盟 video 独立点击率。 |
| ^^^atc_users | int | 12 | 联盟 video 加购用户数。 |
| ^^^unique_atc_rate | string | 0.0833 | 联盟 video 独立加购率。 |
| ^^^unique_click_order_rate | string | 0.0208 | 联盟 video 独立点击到下单转化率。 |
| ^^shop_tab_performance | object |  | Shop Tab 的 performance 指标。 |
| ^^^shop_tab_product_impressions | int | 2520 | Shop Tab 商品曝光数。 |
| ^^^shop_tab_product_clicks | int | 245 | Shop Tab 商品点击数。 |
| ^^^unique_shop_tab_product_clicks | int | 210 | Shop Tab 独立商品点击数。 |
| ^^^estimated_shop_tab_customers | int | 18 | Shop Tab 预估客户数。 |
| ^^^shop_tab_ctr | string | 0.1551 | Shop Tab 点击率。 |
| ^^^shop_tab_ctor_sku | string | 0.0735 | Shop Tab 点击到下单转化率（SKU 级别）。 |
| ^^^shop_tab_gmv | object |  | Shop Tab 产生的 GMV。 |
| ^^^^amount | string | 128.4 | GMV 金额。 |
| ^^^^currency | string | GBP | 货币代码。 |
| ^^^shop_tab_sold_items | int | 4 | 通过 Shop Tab 售出的件数。 |
| ^next_page_token | string | cGFnZV9udW1iZXI9MQ== | 下一页的分页 token。将此值作为下一次请求中的 `page_token` 传入，并复用相同的 `start_date_ge`、`end_date_lt`、`sort_field`、`sort_order`、`currency`、`category_filter`、`product_status_filter` 和 `page_size` 值。空值表示没有下一页。 |
| ^total_count | int | 10 | 所有页面中与请求筛选条件匹配的商品总数。 |
| ^latest_available_date | string | 2024-04-07 | 当地时区中数据已就绪的最新日期（ISO 8601 格式）。 |
# 响应示例
```json
{"code":0,"data":{"products":[{"id":"1732333333333333629","total_performance":{"gmv":{"amount":"395.03","currency":"GBP"},"orders":12,"sku_orders":12,"items_sold":12,"estimated_customers":10,"aov":{"amount":"32.92","currency":"GBP"},"product_impressions":5420,"product_clicks":438,"ctr":"0.0808","add_cart_count":57,"add_cart_rate":"0.1301","click_order_rate":"0.0274","unique_product_impressions":4890,"unique_clicks":401,"unique_ctr":"0.082","add_cart_users":45,"unique_atc_rate":"0.1122","unique_click_order_rate":"0.0299","gmv_incl_tax":{"amount":"426.63","currency":"GBP"},"tax":{"amount":"31.6","currency":"GBP"},"gross_merchandise_value":{"amount":"395.03","currency":"GBP"},"shipping_fees":{"amount":"18.5","currency":"GBP"},"refunds":{"amount":"24.99","currency":"GBP"},"refunded_items":1,"refund_customers":1},"seller_live_performance":{"attributed_gmv":{"amount":"142.8","currency":"GBP"},"attributed_orders":4,"attributed_sku_orders":4,"attributed_sold_items":5,"estimated_customers":4,"aov":{"amount":"35.7","currency":"GBP"},"new_live_count":2,"product_impressions":1680,"product_clicks":156,"ctr":"0.0929","add_cart_count":21,"add_cart_rate":"0.1346","click_order_rate":"0.0256","unique_product_impressions":1510,"unique_clicks":141,"unique_ctr":"0.0934","add_cart_users":17,"unique_atc_rate":"0.1206","unique_click_order_rate":"0.0284"},"seller_video_performance":{"attributed_gmv":{"amount":"96.45","currency":"GBP"},"attributed_orders":3,"attributed_sku_orders":3,"attributed_sold_items":3,"estimated_customers":3,"aov":{"amount":"32.15","currency":"GBP"},"new_video_count":3,"product_impressions":2140,"product_clicks":173,"ctr":"0.0808","add_cart_count":19,"add_cart_rate":"0.1098","click_order_rate":"0.0173","unique_product_impressions":1985,"unique_clicks":160,"unique_ctr":"0.0806","add_cart_users":15,"unique_atc_rate":"0.0938","unique_click_order_rate":"0.0188"},"seller_product_card_performance":{"attributed_gmv":{"amount":"118.6","currency":"GBP"},"attributed_orders":4,"attributed_sku_orders":5,"attributed_sold_items":4,"estimated_customers":4,"aov":{"amount":"29.65","currency":"GBP"},"product_impressions":1600,"product_clicks":109,"ctr":"0.0681","add_cart_count":17,"add_cart_rate":"0.156","click_order_rate":"0.0367","unique_product_impressions":1395,"unique_clicks":100,"unique_ctr":"0.0717","add_cart_users":13,"unique_atc_rate":"0.13","unique_click_order_rate":"0.04"},"affiliate_total_performance":{"attributed_gmv":{"amount":"204.3","currency":"GBP"},"attributed_orders":6,"attributed_sku_orders":6,"attributed_sold_items":7,"estimated_customers":5,"aov":{"amount":"34.05","currency":"GBP"},"avg_daily_creator_posted_content":8,"product_impressions":3840,"product_clicks":265,"ctr":"0.069","add_cart_count":31,"add_cart_rate":"0.117","click_order_rate":"0.0226","unique_product_impressions":3410,"unique_clicks":238,"unique_ctr":"0.0698","add_cart_users":24,"unique_atc_rate":"0.1008","unique_click_order_rate":"0.0252"},"affiliate_live_performance":{"live_attributed_gmv":{"amount":"121.4","currency":"GBP"},"new_live_count":3,"product_impressions":1320,"product_clicks":102,"ctr":"0.0773","add_cart_count":14,"add_cart_rate":"0.1373","click_order_rate":"0.0294","unique_product_impressions":1208,"unique_clicks":94,"unique_ctr":"0.0778","atc_users":12,"unique_atc_rate":"0.1277","unique_click_order_rate":"0.0319"},"affiliate_video_performance":{"attributed_video_gmv":{"amount":"82.9","currency":"GBP"},"new_video_count":5,"product_impressions":2520,"product_clicks":163,"ctr":"0.0647","add_cart_count":17,"add_cart_rate":"0.1043","click_order_rate":"0.0184","unique_product_impressions":2202,"unique_clicks":144,"unique_ctr":"0.0654","atc_users":12,"unique_atc_rate":"0.0833","unique_click_order_rate":"0.0208"},"shop_tab_performance":{"shop_tab_product_impressions":2520,"shop_tab_product_clicks":245,"unique_shop_tab_product_clicks":210,"estimated_shop_tab_customers":18,"shop_tab_ctr":"0.1551","shop_tab_ctor_sku":"0.0735","shop_tab_gmv":{"amount":"128.4","currency":"GBP"},"shop_tab_sold_items":4}}],"next_page_token":"cGFnZV9udW1iZXI9MQ==","total_count":10,"latest_available_date":"2024-04-07"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 28001022 | invalid request params; detail: start time or end time is invalid. |
