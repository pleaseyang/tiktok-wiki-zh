# 按订单获取交易

# 路径：/finance/202501/orders/{order_id}/statement_transactions
# 方法：[GET]
# 功能描述
检索订单交易的 SKU 级别详情。涵盖与销售、费用、佣金、运费、税金和退款相关的交易。
适用于所有地区的卖家。仅提供 2023-07-01 之后的数据（请注意，对于美国跨境卖家，2025-04-30 之前的数据不可用）。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 5793990727963214852 | TikTok Shop 中的订单 ID。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/finance/202501/orders/5793990727963214852/statement_transactions?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^order_id | string | 5793990727963214852 | TikTok Shop 中的订单 ID。 |
| ^order_create_time | int | 1685548800 | 订单创建时间，以 Unix 时间戳（秒）表示。 |
| ^currency | string | GBP | ISO 4217 格式的三字母货币代码。 |
| ^revenue_amount | string | 200 | 订单结算时的收入金额。等同于净销售金额。 |
| ^fee_and_tax_amount | string | -30 | 订单结算时平台收取的费用和税金。不含运费相关成本。 |
| ^shipping_cost_amount | string | -70 | 订单结算时的运费。 |
| ^settlement_amount | string | 130 | 订单的结算金额。 |
公式：revenue_amount - shipping_cost_amount - fee_tax_amount |
^sku_transactions |[]object | |订单的 SKU 交易记录列表。 |
^^sku_id |string |1636700041413599290 |TikTok Shop 中的 SKU ID。 |
^^sku_name |string |Test SKU name |SKU 名称。 |
^^statement_id |string |7238804564097517339 |账单 ID。 |
^^product_name |string |Test Product name |商品标题。 |
^^quantity |string |1 |订单结算中包含的 SKU 数量。 |
^^settlement_amount |string |130 |SKU 的结算金额。 |
^^revenue_amount |string |200 |订单结算时的收入金额。等同于 `revenue_breakdown` 中所有金额的总和。 |
^^revenue_breakdown |object | |包含直接贡献于 `revenue_amount` 的金额的 object。 |
^^^subtotal_before_discount_amount |string |210 |所有订单商品在扣除任何卖家折扣和平台折扣之前的总价。等同于店铺的总销售额。 |
^^^seller_discount_amount |string |-10 |卖家出资的折扣总金额，包括：

* 卖家促销（商品折扣、限时特卖、买多省多、优惠券和捆绑优惠）
* 联合出资优惠券活动中卖家承担的折扣部分
* 活动期间卖家折扣 |
   ^^^refund_subtotal_before_discount_amount |string |0 |所有退款商品在任何卖家折扣之前的总价。等同于店铺的总销售退款。 |
   ^^^seller_discount_refund_amount |string |0 |因退货或退款而退还给卖家的折扣。 |
   ^^^cod_service_fee_amount |string |0 |向买家收取的货到付款服务费。
   仅适用于沙特阿拉伯。 |
   ^^^refund_cod_service_fee_amount |string |0 |货到付款服务费的退款。
   仅适用于沙特阿拉伯。 |
   ^^^distant_item_fee_amount |string |0 |客户支付的远距离商品费用。根据您当前的 Horizon+ 计划设置，此费用包含在发往爪哇岛以外地区的订单商品价格中。 |
   ^^shipping_cost_amount |string |-70 |订单结算时的运费。等同于 `shipping_cost_breakdown` 中所有贡献金额的总和。 |
   ^^shipping_cost_breakdown |object | |包含直接贡献于 `shipping_cost_amount` 的金额的 object。 |
   ^^^actual_shipping_fee_amount |string |-50 |根据承运商测量的重量/尺寸计算的实际运费。详情请查看 `shipping_cost_breakdown.supplementary_component`。 |
   ^^^international_leg_logistics_amount |string |0 |跨境运输国际段向卖家收取的配送费 |
   ^^^shipping_fee_discount_amount |string |0 |平台提供的运费补贴和激励。这包括所有补贴，无论履约渠道或政策。详情请查看 `shipping_cost_breakdown.supplementary_component`。 |
   ^^^customer_paid_shipping_fee_amount |string |0 |客户承担的实际运费，根据卖家上传的商品重量计算。负数表示客户支付运费的退款金额 |
   ^^^return_shipping_fee_amount |string |-10 |卖家为退货配送支付的运费。 |
   ^^^replacement_shipping_fee_amount |string |-10 |卖家为换货配送支付的运费。
   仅适用于印度尼西亚。 |
   ^^^exchange_shipping_fee_amount |string |5 |卖家为换货配送支付的运费。
   仅适用于印度尼西亚。 |
   ^^^signature_confirmation_fee_amount |string |5 |需要签名确认服务的包裹产生的费用 |
   ^^^shipping_insurance_fee_amount |string |0 |卖家为购买额外 TikTok 运输保险服务而产生的运输保险费。 |
   ^^^fbt_fulfillment_fee_reimbursement_amount |string |5 |TikTok Shop 对不符合免运费条件的 Fulfilled by TikTok（FBT）订单的赔偿。
   仅适用于美国。 |
   ^^^return_shipping_label_fee_amount |string |5 |客户承担的退货标签费用。此费用由卖家代收并按约定的付款条件结算。 |
   ^^^seller_self_shipping_service_fee_amount |string |5 |对通过您自己的物流服务商发货的订单收取的服务费。适用于不符合豁免条件的包裹。 |
   ^^^return_shipping_fee_paid_buyer_amount |string |5 |客户为退货包裹支付的运费赔偿 |
   ^^^failed_delivery_subsidy_amount |string |5 |对于配送失败的运费，您支付至标准费率，TikTok Shop 承担剩余金额。 |
   ^^^fbt_free_shipping_fee_amount |string |5 |这是您通过 FBT 向客户提供免运费时承担的费用。 |
   ^^^free_return_subsidy_amount |string |5 |作为向客户提供的免费退货的一部分，对平台出资的退货运费部分的赔偿。 |
   ^^^distant_shipping_fee_amount |string |0 |客户支付的远距离运费。根据您当前的 Horizon+ 计划设置，此费用包含在发往爪哇岛以外地区的订单商品价格中。 |
   ^^^shipping_app_service_fee_amount |string |0 |使用运费生成运单的运费应用服务费 |
   ^^^logistics_service_fee |string |0 |在整个订单生命周期内因物流相关服务向卖家收取的费用，包括处理、协调、配送相关事务的处理以及基本运费激励。这是每笔订单的金额，基于包裹的重量等级和运输路线。它使平台能够在不断变化的全球环境中持续提升服务于卖家和客户的优质、可持续物流网络。 |
   ^^^fbt_overall_merchant_subsidy |string |0 |适用于您的订单的补贴，在账单周期内提供给所有 FBT（Fulfilled by TikTok）卖家。金额根据您在此期间的合格 FBT 订单量计算。 |
   ^^^fbt_key_merchant_subsidy |string |0 |基于关键卖家计划资格适用于您的订单的补贴。金额根据您在账单周期内的合格 FBT（Fulfilled by TikTok）订单量计算。 |
   ^^^tiktok_shop_shipping_incentive_amount |string |0 |TikTok Shop 提供的运费激励。
   |
   ^^^supplementary_component |object | |补充成本，仅供参考。这些金额不直接贡献于 `shipping_cost_amount`。 |
   ^^^^fbt_fulfillment_fee_reimbursement_amount |string |5 |（**已弃用**：此字段已弃用，将返回空字符串。相关详情请参阅 `shipping_cost_breakdown.fbt_fulfillment_fee_reimbursement_amount`。） |
   ^^^^platform_shipping_fee_discount_amount |string |20 |根据活动政策提供的运费折扣。这是 `shipping_fee_discount_amount` 的一部分。 |
   ^^^^promo_shipping_incentive_amount |string |0 |如果卖家注册了联合出资免运费计划，将获得的额外运费激励。负数表示因归咎于卖家责任的订单退款而撤销的激励冲回。这是 `shipping_fee_discount_amount` 的一部分。 |
   ^^^^shipping_fee_subsidy_amount |string |0 |平台为卖家发货提供的运费补贴。这是 `shipping_fee_discount_amount` 的一部分。
* 正数表示卖家收到的补贴。
* 负数表示卖家必须退还给 TikTok Shop 的补贴。 |
   ^^^^seller_shipping_fee_discount_amount |string |0 |卖家提供的运费折扣。 |
   ^^^^fbt_shipping_cost_amount |string |-30 |卖家为由 TikTok（FBT）履约的订单产生的运费。这是 `actual_shipping_fee_amount` 的一部分。
   仅适用于欧盟和英国。 |
   ^^^^customer_shipping_fee_offset_amount |string |-6.99 |用于抵消 TikTok Shop 运费激励或客户支付运费的费用，使卖家净收费为 $0。
   仅适用于美国。 |
   ^^^^fbm_shipping_cost_amount |string |30 |卖家使用 TikTok Shipping 产生的运费。这是 `actual_shipping_fee_amount` 的一部分。 |
   ^^^^fbt_fulfillment_fee_amount |string |0 |卖家为由 TikTok（FBT）履约的订单产生的运输和仓储履约费。这是 `actual_shipping_fee_amount` 的一部分。
   仅适用于美国。 |
   ^^^^return_refund_subsidy_amount |string |0 |对于退货和退款的运费，您支付至标准费率，TikTok Shop 承担剩余金额。这是 `customer_paid_shipping_fee_amount` 的一部分。 |
   ^^^^refunded_customer_shipping_fee_amount |string |0 |因退货和退款退还给客户的运费。不含补贴。这是 `customer_paid_shipping_fee_amount` 的一部分。
   |
   ^^^^shipping_fee_guarantee_reimbursement |string |0 |运费保障计划对配送失败或退货的赔偿 |
   ^^^hazmat_noncompliance_fee |string |0 |当含有危险品的包裹在未进行_required 申报或合规包装的情况下发货时收取的费用，由承运商评估。在包裹送达时收取。 |
   ^^^hazmat_handling_fee |string |0 |为运输含有危险品的包裹所需的额外处理而收取的费用。在包裹送达时收取。 |
   ^^^non_standard_weight_fee |string |0 |当包裹超出标准重量范围时收取的费用。费率由 TikTok Shop 设定，在包裹送达时收取。 |
   ^^^non_standard_dimension_fee |string |0 |当包裹超出标准尺寸范围时收取的费用。费率由 TikTok Shop 设定，在包裹送达时收取。 |
   ^^fee_tax_amount |string |-30 |订单结算时 TikTok Shop 收取的总费用和税金。不含运费相关成本。等同于 `fee_tax_breakdown` 中所有贡献金额的总和。 |
   ^^fee_tax_breakdown |object | |包含直接贡献于 `fee_tax_amount` 的费用和税金金额的 object。 |
   ^^^fee |object | |包含贡献于 `fee_tax_amount` 的费用金额的 object。 |
   ^^^^platform_commission_amount |string |0 |TikTok Shop 收取的佣金金额。 |
   ^^^^referral_fee_amount |string |-2 |为处理成功订单收取的推荐费。
   仅适用于美国。 |
   ^^^^refund_administration_fee_amount |string |0 |从推荐费退款总额中扣除的 20% 退款管理费。 |
   ^^^^transaction_fee_amount |string |-2 |为处理成功订单收取的交易费。 |
   ^^^^credit_card_handling_fee_amount |string |0 |买家使用信用卡支付时收取的手续费。 |
   ^^^^affiliate_commission_amount |string |0 |向卖家收取的用于支付给达人的佣金金额。 |
   ^^^^affiliate_commission_amount_before_pit |string |-2 |在扣除任何个人所得税预扣之前支付给达人的联盟广告佣金。
   仅适用于东南亚市场。 |
   ^^^^affiliate_partner_commission_amount |string |0 |通过联盟合作伙伴链接购买的佣金金额。 |
   ^^^^affiliate_ads_commission_amount |string |0 |来自广告的符合条件的订单佣金。 |
   ^^^^sfp_service_fee_amount |string |2 |参与 [卖家 Free Shipping Programme] 收取的服务费。 |
   ^^^^live_specials_fee_amount |string |2 |参与 [LIVE Specials Programme] 收取的服务费。 |
   ^^^^bonus_cashback_service_fee_amount |string |0 |参与返现奖励计划收取的服务费。 |
   ^^^^mall_service_fee_amount |string |0 |使用 TikTok Shop Mall 收取的服务费。 |
   ^^^^voucher_xtra_service_fee_amount |string |100 |参与 Voucher Xtra 计划收取的服务费。 |
   ^^^^flash_sales_service_fee_amount |string |50 |参与限时特卖收取的服务费。 |
   ^^^^cofunded_promotion_service_fee_amount |string |100 |联合出资促销收取的服务费。
   |
   ^^^^pre_order_service_fee_amount |string |10 |卖家加入预订计划收取的服务费。 |
   ^^^^tsp_commission_amount |string |10 |TikTok Shop Partners（TSP）收取的佣金金额。 |
   ^^^^dt_handling_fee_amount |string |10 |由 Dilayani Tokopedia 履约的订单收取的手续费。 |
   ^^^^epr_pob_service_fee_amount |string |-10 |TikTok Shop 代表您向合格的生产者责任组织（PRO）支付的生态贡献。 |
   ^^^^fee_per_item_sold_amount |string |0 |平台对每件售出商品向卖家收取的费用。
   仅适用于巴西市场。 |
   ^^^^seller_paylater_handling_fee_amount |string |-10 |向参与 PayLater 计划的卖家收取的手续费。 |
   ^^^^cofunded_creator_bonus_amount |string |-10 |作为佣金提升活动的一部分，您联合出资的达人奖金部分。 |
   ^^^^dynamic_commission_amount |string |5 |动态佣金是平台对每笔成功配送的订单向所有卖家收取的金额。
   仅适用于印度尼西亚。 |
   ^^^^external_affiliate_marketing_fee_amount |string |10 |参与外部联盟营销解决方案计划的服务费，如注册时所述。 |
   ^^^^vn_fix_infrastructure_fee |string |0 |基础设施费是 TikTok Shop 为提供、维护和发展配送服务基础设施而收取的固定服务费。适用于主订单级别的已配送订单。 |
   ^^^^affiliate_commission_deposit |string |0 |订单支付后为达人佣金预留的金额。仅适用于与订单量挂钩的佣金，基于最高收益费率。 |
   ^^^^affiliate_commission_release |string |0 |订单结算后退还给您的佣金押金。仅适用于与订单量挂钩的佣金。 |
   ^^^^tap_shop_ads_commission |string |0 |卖家向 TikTok Shop Affiliate Partner（TAP）支付的广告佣金成本。 |
   ^^^^shipping_fee_guarantee_service_fee |string |0 |运费保障计划下每笔订单收取的固定服务费 |
   ^^^^installation_service_fee |string |0 |TikTok Shop 对您使用平台安装服务收取的费用 |
   ^^^^campaign_resource_fee |string |0 |卖家参加活动的活动资源费金额 |
   ^^^^platform_special_service_fee_amount |string |0 |客户支付的远距离运费中超过物流服务商收费的部分，由 TikTok Shop 保留以支持安全的履约体验 |
   ^^^^smart_promotion_fee_amount |string |0 |此费用包含 TikTok Shop 用于帮助向客户提供促销的资金 |
   ^^^^gmv_max_ad_fee_amount |string |0 |每笔订单净销售额中按百分比扣除的 GMV Max（净销售目标）广告费。 |
   ^^^^platform_semi_managed_commission_fee |string |0 |按（原价 - 卖家折扣 + 客户支付运费）的百分比计算。 |
   ^^^^platform_semi_managed_commission_fee_tax |string |0 |此金额代表政府代收。 |
   ^^^^campaign_period_fee_cfp_amount |string |0 |联合出资促销活动期间收取的费用。 |
   ^^^^campaign_period_fee_sp_amount |string |0 |智能促销活动期间收取的费用。 |
   ^^^^campaign_period_fee_sp_tax_amount |string |0 |智能促销活动期间费用适用的销售税。 |
   ^^^^campaign_period_fee_cfp_tax_amount |string |0 |联合出资促销活动期间费用适用的销售税。 |
   ^^^^seller_growth_fee_amount |string |0 |对每笔成功订单收取的费用，用于提供返现奖励和其他增长福利。 |
   ^^^^category_led_campaign_fee_amount |string |0 |参与品类主导活动收取的费用。
   |
   ^^^^category_led_campaign_fee_tax_amount |string |0 |该费用收取的销售税。 |
   ^^^^brand_amplification_program_commission |string |0 |参与品牌放大计划收取的佣金。 |
   ^^^^brand_amplification_program_fee_tax |string |0 |该费用收取的销售税。
   |
   ^^^^brand_campaign_fee |string |0 |参与品牌活动收取的费用。 |
   ^^^^brand_campaign_fee_tax |string |0 |该费用收取的销售税。 |
   ^^^^failed_delivery_shipping_fee |string |0 |未能配送给客户的订单运费。在某些情况下，此费用可能由卖家和平台分担。 |
   ^^^^buyer_fault_return_shipping_fee |string |0 |买家责任的退货运费。在某些情况下，此费用可能由卖家和平台分担。 |
   ^^^^insurance_fee |string |0 |每笔订单收取的保险费用 |
   ^^^^gmv_max_coupon_fee |string |0 |GMV Max 优惠券的成本。 |
   ^^^^cps_shop_ads_commission_tax_amount |string |0 |GMV Max 广告费适用的销售税 |
   ^^^^shipping_insurance_fee_tax_amount |string |0 |运输保险费收取的税金。 |
   ^^^^new_customer_growth_package_fee |string |0 |使用新客增长包提供折扣以吸引新客户到您店铺的费用。 |
   ^^^^target_product_gmv_growth_package_fee |string |0 |使用商品 GMV 增长包对精选商品提供折扣以增加销量的费用。 |
   ^^^^store_gmv_growth_package_fee |string |0 |使用店铺 GMV 增长包提供全店折扣并提升整体销售额的费用。 |
   ^^^^auto_post_shoppable_video_commission_fee |string |0 |对归因于 AI 生成自动发布的可购物视频的订单向卖家收取的佣金。 |
   ^^^^seller_funded_user_spoint_service_fee |string |0 |对卖家出资发放给用户 S-Points 的服务费。基于订单实际支付金额计算，如果订单后续退货则退还。 |
   ^^^tax |object | |包含贡献于 `fee_tax_amount` 的税金金额的 object。 |
   ^^^^vat_amount |string |0 |平台代表卖家支付的 VAT。
   仅适用于跨境店铺订单。 |
   ^^^^import_vat_amount |string |0 |进口增值税，即在一个国家购买并进口到另一个国家的商品上缴纳的税。
   仅适用于跨境店铺订单。在日本，指日本消费税（JCT）。 |
   ^^^^customs_duty_amount |string |0 |关税，由政府征收的跨境商品税。
   仅适用于跨境店铺订单。 |
   ^^^^customs_clearance_amount |string |0 |物流供应商收取的清关服务费。
   仅适用于跨境店铺订单。 |
   ^^^^sst_amount |string |0 |自 2024 年 1 月 1 日起，平台为进口到马来西亚的低价值商品征收并缴纳给税务机关的销售和服务税（SST）。 |
   ^^^^gst_amount |string |0 |自 2023 年 1 月 1 日起，平台为进口到新加坡的低价值商品征收并缴纳给税务机关的商品和服务税（GST）。 |
   ^^^^iva_amount |string |0 |TikTok Shop 需要在您的应税商品上预扣并缴纳给税务机关的墨西哥 VAT。 |
   ^^^^isr_amount |string |0 |TikTok Shop 需要预扣的墨西哥联邦所得税。 |
   ^^^^anti_dumping_duty_amount |string |20 |政府对进口商品征收的反倾销税。 |
   ^^^^local_vat_amount |string |10 |平台代表卖家支付的 VAT。仅适用于本地店铺订单。 |
   ^^^^pit_amount |string |10 |平台代表卖家支付的个人所得税（PIT）。 |
   ^^^^sales_tax_referral_fee_amount |string |0 |部分美国州将推荐费视为应税项目。为遵守州税法，TikTok Inc. 在收取应税费用时征收并缴纳适用的销售税。 |
   ^^^^smart_promotion_fee_tax_amount |string |0 |智能促销费的销售税 |
   ^^^^cedular_tax |string |0 |墨西哥瓜纳华托分类税 |
   ^^^^new_customer_growth_package_fee_tax |string |0 |新客增长包费适用的销售税。 |
   ^^^^store_gmv_growth_package_fee_sales_tax |string |0 |店铺 GMV 增长包费适用的销售税。 |
   ^^^^target_product_gmv_growth_package_tax |string |0 |商品 GMV 增长包费适用的销售税。 |
   ^^^^auto_post_shoppable_video_sales_tax |string |0 |自动发布可购物视频佣金费适用的销售税。 |
   ^^^^article_22_income_tax_withheld |string |0 |平台根据 PMK 37/2025 预扣的第 22 条所得税 |
   ^total_count |int |2 |交易记录数量 |

# 响应示例
```json
{"code":0,"data":{"order_id":"5793990727963214852","order_create_time":1685548800,"currency":"GBP","revenue_amount":"200","fee_and_tax_amount":"-30","shipping_cost_amount":"-70","settlement_amount":"130","sku_transactions":[{"sku_id":"1636700041413599290","sku_name":"Test SKU name","statement_id":"7238804564097517339","product_name":"Test Product name","quantity":"1","settlement_amount":"130","revenue_amount":"200","revenue_breakdown":{"subtotal_before_discount_amount":"210","seller_discount_amount":"-10","refund_subtotal_before_discount_amount":"0","seller_discount_refund_amount":"0","cod_service_fee_amount":"0","refund_cod_service_fee_amount":"0","distant_item_fee_amount":"0"},"shipping_cost_amount":"-70","shipping_cost_breakdown":{"actual_shipping_fee_amount":"-50","international_leg_logistics_amount":"0","shipping_fee_discount_amount":"0","customer_paid_shipping_fee_amount":"0","return_shipping_fee_amount":"-10","replacement_shipping_fee_amount":"-10","exchange_shipping_fee_amount":"5","signature_confirmation_fee_amount":"5","shipping_insurance_fee_amount":"0","fbt_fulfillment_fee_reimbursement_amount":"5","return_shipping_label_fee_amount":"5","seller_self_shipping_service_fee_amount":"5","return_shipping_fee_paid_buyer_amount":"5","failed_delivery_subsidy_amount":"5","fbt_free_shipping_fee_amount":"5","free_return_subsidy_amount":"5","distant_shipping_fee_amount":"0","shipping_app_service_fee_amount":"0","logistics_service_fee":"0","fbt_overall_merchant_subsidy":"0","fbt_key_merchant_subsidy":"0","tiktok_shop_shipping_incentive_amount":"0","supplementary_component":{"fbt_fulfillment_fee_reimbursement_amount":"5","platform_shipping_fee_discount_amount":"20","promo_shipping_incentive_amount":"0","shipping_fee_subsidy_amount":"0","seller_shipping_fee_discount_amount":"0","fbt_shipping_cost_amount":"-30","customer_shipping_fee_offset_amount":"-6.99","fbm_shipping_cost_amount":"30","fbt_fulfillment_fee_amount":"0","return_refund_subsidy_amount":"0","refunded_customer_shipping_fee_amount":"0","shipping_fee_guarantee_reimbursement":"0"},"hazmat_noncompliance_fee":"0","hazmat_handling_fee":"0","non_standard_weight_fee":"0","non_standard_dimension_fee":"0"},"fee_tax_amount":"-30","fee_tax_breakdown":{"fee":{"platform_commission_amount":"0","referral_fee_amount":"-2","refund_administration_fee_amount":"0","transaction_fee_amount":"-2","credit_card_handling_fee_amount":"0","affiliate_commission_amount":"0","affiliate_commission_amount_before_pit":"-2","affiliate_partner_commission_amount":"0","affiliate_ads_commission_amount":"0","sfp_service_fee_amount":"2","live_specials_fee_amount":"2","bonus_cashback_service_fee_amount":"0","mall_service_fee_amount":"0","voucher_xtra_service_fee_amount":"100","flash_sales_service_fee_amount":"50","cofunded_promotion_service_fee_amount":"100","pre_order_service_fee_amount":"10","tsp_commission_amount":"10","dt_handling_fee_amount":"10","epr_pob_service_fee_amount":"-10","fee_per_item_sold_amount":"0","seller_paylater_handling_fee_amount":"-10","cofunded_creator_bonus_amount":"-10","dynamic_commission_amount":"5","external_affiliate_marketing_fee_amount":"10","vn_fix_infrastructure_fee":"0","affiliate_commission_deposit":"0","affiliate_commission_release":"0","tap_shop_ads_commission":"0","shipping_fee_guarantee_service_fee":"0","installation_service_fee":"0","campaign_resource_fee":"0","platform_special_service_fee_amount":"0","smart_promotion_fee_amount":"0","gmv_max_ad_fee_amount":"0","platform_semi_managed_commission_fee":"0","platform_semi_managed_commission_fee_tax":"0","campaign_period_fee_cfp_amount":"0","campaign_period_fee_sp_amount":"0","campaign_period_fee_sp_tax_amount":"0","campaign_period_fee_cfp_tax_amount":"0","seller_growth_fee_amount":"0","category_led_campaign_fee_amount":"0","category_led_campaign_fee_tax_amount":"0","brand_amplification_program_commission":"0","brand_amplification_program_fee_tax":"0","brand_campaign_fee":"0","brand_campaign_fee_tax":"0","failed_delivery_shipping_fee":"0","buyer_fault_return_shipping_fee":"0","insurance_fee":"0","gmv_max_coupon_fee":"0","cps_shop_ads_commission_tax_amount":"0","shipping_insurance_fee_tax_amount":"0","new_customer_growth_package_fee":"0","target_product_gmv_growth_package_fee":"0","store_gmv_growth_package_fee":"0","auto_post_shoppable_video_commission_fee":"0","seller_funded_user_spoint_service_fee":"0"},"tax":{"vat_amount":"0","import_vat_amount":"0","customs_duty_amount":"0","customs_clearance_amount":"0","sst_amount":"0","gst_amount":"0","iva_amount":"0","isr_amount":"0","anti_dumping_duty_amount":"20","local_vat_amount":"10","pit_amount":"10","sales_tax_referral_fee_amount":"0","smart_promotion_fee_tax_amount":"0","cedular_tax":"0","new_customer_growth_package_fee_tax":"0","store_gmv_growth_package_fee_sales_tax":"0","target_product_gmv_growth_package_tax":"0","auto_post_shoppable_video_sales_tax":"0","article_22_income_tax_withheld":"0"}}}],"total_count":2},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

