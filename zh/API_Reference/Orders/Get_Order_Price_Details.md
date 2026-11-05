# 获取订单价格详情

# Path: /order/202407/orders/{order_id}/price_detail
# Method: [GET]
# 功能描述
获取订单或订单行的详细价格计算信息，包括优惠券、税费等。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | 是 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求路径参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | 是 | 576461413038785752 | 订单 ID |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/order/202407/orders/576461413038785752/price_detail?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^currency | string | USD | 货币类型。三位字母代码，参见 [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)。 |
| ^total | string | 122.00 | 订单的总原价。计算方式：`sku_list_price` + `shipping_list_price` |
| ^payment | string | 101.00 | 买家为订单支付的金额。 |
| ^sku_list_price | string | 97.00 | 商品的总 MSRP 价格。 |
| ^sku_sale_price | string | 96.00 | 商品的总促销售价。计算方式：`sku_list_price` - `subtotal_deduction_seller` - `subtotal_deduction_platform` |
| ^subtotal | string | 98.00 | 订单中商品的总促销售价，含税。 |
| ^subtotal_deduction_seller | string | 0.50 | 卖家提供的商品价格折扣 |
| ^subtotal_deduction_platform | string | 0.50 | 平台提供的商品价格折扣 |
| ^subtotal_tax_amount | string | 2.00 | 商品的总税额 |
| ^voucher_deduction_platform | string | 1010000 | 订单中平台出资优惠券的商品价格总扣减。 |
| ^voucher_deduction_seller | string | 1020000 | 订单中卖家出资优惠券的商品价格总扣减。 |
| ^shipping_list_price | string | 25.00 | 原始运费价格 |
| ^shipping_sale_price | string | 3.00 | 促销运费价格。计算方式：`shipping_list_price` - `shipping_fee_deduction_seller` - `shipping_fee_deduction_platform` |
| ^shipping_fee_deduction_seller | string | 10.00 | 卖家承担的运费折扣。 |
| ^shipping_fee_deduction_platform | string | 12.00 | 平台承担的运费折扣 |
| ^shipping_fee_deduction_platform_voucher | string | 1010000 | 订单中平台出资优惠券的运费扣减。 |
| ^tax_amount | string | 2.00 | 订单的总税额。 |
| ^tax_rate | string | 0.021 | 税率 |
| ^net_price_amount | string | 97.00 | 不含税的订单价格。 |
| ^cod_fee | string | 0.00 | 运费聚合商收取的货到付款费用。对于沙特阿拉伯以外的地区，该值为 `0.00`。 |
| ^cod_fee_net_amount | string | 0.00 | 运费聚合商收取的含税费货到付款费用。对于沙特阿拉伯以外的地区，该值为 `0.00`。 |
| ^sku_gift_original_price | string | 2.00 | 卖家提供的赠品原始 SKU 列表价格。 |
| ^sku_gift_net_price | string | 2.02 | 卖家提供的含税费赠品原始 SKU 列表价格。 |
| ^distance_shipping_fee | string | 1.00 | 距离运费是由我们的物流合作伙伴收取的费用，涵盖 Horizon+ 计划下爪哇岛以外配送的单独距离成本。 |
| 仅适用于印尼（ID）市场。 |  |  |  |
| ^distance_fee | string | 2.00 | Horizon+ 计划的总距离费用。仅适用于印尼（ID）市场 |
| ^line_items | []object |  | 订单中每个订单行的价格详情。 |
| ^^id | string | 576461413032342720 | 对应的 line_item id |
| ^^currency | string | USD | 货币类型。三位字母代码，参见 [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)。 |
| ^^total | string | 122.00 | 订单行的总原价。计算方式：`sku_list_price` + `shipping_list_price` |
| ^^payment | string | 101.00 | 买家为订单行支付的金额。 |
| ^^sku_list_price | string | 97.00 | 商品的总 MSRP 价格。 |
| ^^sku_sale_price | string | 96.00 | 商品的总促销售价。计算方式：`sku_list_price` - `subtotal_deduction_seller` - `subtotal_deduction_platform` |
| ^^subtotal | string | 98.00 | 订单行的总促销售价，含税。 |
| ^^subtotal_deduction_seller | string | 0.50 | 卖家提供的商品价格折扣 |
| ^^subtotal_deduction_platform | string | 0.50 | 平台提供的商品价格折扣 |
| ^^subtotal_tax_amount | string | 2.00 | 商品的总税额 |
| ^^voucher_deduction_platform | string | 1010000 | 订单行中平台出资优惠券的商品价格扣减。 |
| ^^voucher_deduction_seller | string | 1020000 | 订单行中卖家出资优惠券的商品价格扣减。 |
| ^^shipping_list_price | string | 25.00 | 原始运费价格 |
| ^^shipping_sale_price | string | 3.00 | 促销运费价格。计算方式：`shipping_list_price` - `shipping_fee_deduction_seller` - `shipping_fee_deduction_platform` |
| ^^shipping_fee_deduction_seller | string | 10.00 | 卖家承担的运费折扣。 |
| ^^shipping_fee_deduction_platform | string | 12.00 | 平台承担的运费折扣 |
| ^^shipping_fee_deduction_platform_voucher | string | 1010000 | 订单行中平台出资优惠券的运费扣减。 |
| ^^tax_amount | string | 2.00 | 订单行的总税额。 |
| ^^tax_rate | string | 0.021 | 税率 |
| ^^net_price_amount | string | 97.00 | 不含税的订单行价格。 |
| ^^cod_fee | string | 0.00 | 运费聚合商收取的货到付款费用。对于沙特阿拉伯以外的地区，该值为 `0.00`。 |
| ^^cod_fee_amount | string | 0.00 | 运费聚合商收取的含税费货到付款费用。对于沙特阿拉伯以外的地区，该值为 `0.00`。 |
| ^^sku_gift_original_price | string | 2.00 | 卖家提供的赠品原始 SKU 列表价格。 |
| ^^sku_gift_net_price | string | 2.02 | 卖家提供的含税费赠品原始 SKU 列表价格。 |
| ^^distance_shipping_fee | string | 1.00 | 距离运费是由我们的物流合作伙伴收取的费用，涵盖 Horizon+ 计划下爪哇岛以外配送的单独距离成本。 |
| 仅适用于印尼（ID）市场。 |  |  |  |
| ^^distance_fee | string | 2.00 | Horizon+ 计划的总距离费用。仅适用于印尼（ID）市场 |
| ^^seller_funded_product_promotions | []object |  | 与订单行关联的卖家出资商品促销。 |
| ^^^activity_id | string | 7136104329798256386 | 标识不同促销活动的唯一 ID。 |
| ^^^discount_amount | string | 2.25 | 此活动的折扣金额 |
| ^^^discount_type | string | COUPON | 此活动的折扣类型。枚举值： |

* COUPON
* ACTIVITY |
   ^^seller_funded_shipping_promotions |[]object | |与订单行关联的卖家出资运费促销。 |
   ^^^activity_id |string |7136104329798256386 |标识不同促销活动的唯一 ID。 |
   ^^^discount_amount |string |2.25 |此活动的折扣金额 |
   ^^^discount_type |string |COUPON
   |此活动的折扣类型。枚举值：
* COUPON
* ACTIVITY |

# 响应示例
```json
{"code":0,"data":{"currency":"USD","total":"122.00","payment":"101.00","sku_list_price":"97.00","sku_sale_price":"96.00","subtotal":"98.00","subtotal_deduction_seller":"0.50","subtotal_deduction_platform":"0.50","subtotal_tax_amount":"2.00","voucher_deduction_platform":"1010000","voucher_deduction_seller":"1020000","shipping_list_price":"25.00","shipping_sale_price":"3.00","shipping_fee_deduction_seller":"10.00","shipping_fee_deduction_platform":"12.00","shipping_fee_deduction_platform_voucher":"1010000","tax_amount":"2.00","tax_rate":"0.021","net_price_amount":"97.00","cod_fee":"0.00","cod_fee_net_amount":"0.00","sku_gift_original_price":"2.00","sku_gift_net_price":"2.02","distance_shipping_fee":"1.00","distance_fee":"2.00","line_items":[{"id":"576461413032342720","currency":"USD","total":"122.00","payment":"101.00","sku_list_price":"97.00","sku_sale_price":"96.00","subtotal":"98.00","subtotal_deduction_seller":"0.50","subtotal_deduction_platform":"0.50","subtotal_tax_amount":"2.00","voucher_deduction_platform":"1010000","voucher_deduction_seller":"1020000","shipping_list_price":"25.00","shipping_sale_price":"3.00","shipping_fee_deduction_seller":"10.00","shipping_fee_deduction_platform":"12.00","shipping_fee_deduction_platform_voucher":"1010000","tax_amount":"2.00","tax_rate":"0.021","net_price_amount":"97.00","cod_fee":"0.00","cod_fee_amount":"0.00","sku_gift_original_price":"2.00","sku_gift_net_price":"2.02","distance_shipping_fee":"1.00","distance_fee":"2.00","seller_funded_product_promotions":[{"activity_id":"7136104329798256386","discount_amount":"2.25","discount_type":"COUPON"}],"seller_funded_shipping_promotions":[{"activity_id":"7136104329798256386","discount_amount":"2.25","discount_type":"COUPON\n"}]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 21001001 | 参数无效。请确保您传递了正确的请求参数。 |
| 21008111 | 订单或包裹不属于当前卖家。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

