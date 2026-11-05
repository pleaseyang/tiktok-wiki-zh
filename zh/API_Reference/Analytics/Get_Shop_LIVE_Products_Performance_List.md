# 获取店铺直播商品表现列表

# Path: /analytics/202512/shop/{live_id}/products_performance
# Method: [GET]
# 功能描述
返回店铺相关 LIVE 场次中每个商品的销售 performance 数据，来源于官方账号或营销账号。

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
| sort_order | string | N | DESC | 排序方向。 |
可选值：ASC, DESC
默认值：DESC

* ASC：升序
* DESC：降序 |
   sort_field |string |N |gmv |排序字段。

可选值：

* gmv
* items_sold
* customers
* created_sku_orders
* sku_orders
* main_orders
* product_impressions
* product_clicks

默认值：gmv |
currency |string |N |USD |货币金额的币种。使用 USD 表示美元，或 LOCAL 表示店铺注册地的本地货币。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202512/shop/7512345678901234567/products_performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&sort_order=DESC&sort_field=gmv&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | LIVE 场次中商品及其销售和流量 performance 的列表。 |
| ^^id | string | 1731736614984386107 | 商品 ID |
| ^^name | string | PANDAEYES |  |
| WAHIDA |  |  |  |
| KNITWEAR |  |  |  |
| CARDIGAN (CLO-CNSNSL97002BL) | 商品名称 |  |  |
| ^^sales | object |  | 该商品在 LIVE 场次中的销售 performance，包括平均价格、订单数、客户数、GMV 和售出商品数。 |
| ^^^direct_gmv | object |  | 直接从 LIVE 购买此商品的订单支付总金额，包括退货和退款。 |
| ^^^^currency | string | SGD | 直接 GMV 货币代码。 |
| ^^^^amount | string | 737.97 | 对应货币的直接 GMV 金额。 |
| ^^^items_sold | int | 24 | 该商品的售出数量 |
| ^^^customers | int | 24 | 直接从 LIVE 订购此商品的客户总数，包括退货或退款的客户。 |
| ^^^created_sku_orders | int | 27 | 直接从 LIVE 为此商品创建的 SKU 订单总数。 |
| ^^^avg_price | object |  | 每个主订单的平均直接 GMV。也称为 AOV（主订单） |
| ^^^^currency | string | SGD | 平均价格货币代码。 |
| ^^^^amount | string | 30.75 | 对应货币的平均价格金额。 |
| ^^^sku_orders | int | 24 | 直接从 LIVE 为此商品支付的 SKU 订单总数。 |
| ^^^main_orders | int | 24 | 支付的主订单总数。主订单指客户进行的单次购买交易。 |
| ^^^payment_rate | string | 0.8888 | 此商品的已支付主订单 / 已创建主订单 |
| ^^traffic | object |  | 该商品在 LIVE 场次中的流量 performance，包括加购、点击转化率、CTR、GPM、商品曝光和商品点击。 |
| ^^^product_impressions | int | 14815 | LIVE 视频中此商品的曝光次数，包括商品列表和商品卡曝光 |
| ^^^ctr | string | 0.0908 | 点击率：LIVE 视频中此商品的点击次数除以 LIVE 视频中此商品的曝光次数，包括商品列表和商品卡的商品点击和商品曝光 |
| ^^^add_to_cart_count | int | 102 | 观众将此商品加入购物车的次数。 |
| ^^^click_to_order_rate | object |  | 此商品的主订单和 SKU 订单的点击转化率 metrics。 |
| ^^^^sku_order_ctor | string | 0.0178 | 观众在 LIVE 直播中点击商品链接并直接下单的百分比。 |
| ^^^^main_order_ctor | string | 0.0178 | 点击 LIVE 商品链接的观众同时下主订单的百分比。 |
| ^^^gpm | object |  | 商品流量的 GPM 数据，包括 Watch GPM。 |
| ^^^^watch_gpm | string | 49.81 | Watch GPM 是从 1,000 次 LIVE 观看中产生的平均 GMV。 |
| ^^^produt_clicks | int | 1346 | 从此 LIVE 中点击此商品的总次数，包括从商品列表和商品卡 |
# 响应示例
```json
{"code":0,"data":{"products":[{"id":"1731736614984386107","name":"PANDAEYES \nWAHIDA   \nKNITWEAR \nCARDIGAN (CLO-CNSNSL97002BL)","sales":{"direct_gmv":{"currency":"SGD","amount":"737.97"},"items_sold":24,"customers":24,"created_sku_orders":27,"avg_price":{"currency":"SGD","amount":"30.75"},"sku_orders":24,"main_orders":24,"payment_rate":"0.8888"},"traffic":{"product_impressions":14815,"ctr":"0.0908","add_to_cart_count":102,"click_to_order_rate":{"sku_order_ctor":"0.0178","main_order_ctor":"0.0178"},"gpm":{"watch_gpm":"49.81"},"produt_clicks":1346}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

