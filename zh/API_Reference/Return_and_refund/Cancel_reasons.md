# 取消原因

📌 不同的订单状态需要不同的原因。查看表格左侧的状态以找到适用的原因，并在调用 API 时将原因名称作为请求参数包含在内。如果取消原因不适用于该订单状态，API 将返回 '25001021 Reason not match order status' 错误。
# US market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 首选支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 误下单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 不再需要 | ecom_order_unpaid_canceled_reason_no_longer_needed |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
|  | 忘记使用优惠券 | ecom_order_to_ship_canceled_reason_forgot_to_apply_coupons |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误购 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 收货地址错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |
|  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed |
|  | 忘记使用优惠券 | ecom_order_to_ship_canceled_reason_forgot_to_apply_coupons |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
|  | 买家请求取消 | seller_cancel_unpaid_reason_buyer_requested_cancellation |
|  | 卖家无法履约订单 | seller_cancel_unpaid_reason_unable_to_fulfill_order |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver |
|  | 买家请求取消 | seller_cancel_paid_reason_buyer_requested_cancellation |
|  | 卖家无法履约订单 | seller_cancel_reason_unable_to_fulfill_order |
## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因未在预计送达时间起 30 天内送达而自动取消 | system_cancel_order_exceed_edt_not_arrive |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |



# UK market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available_uk |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info_uk |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes_uk |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price_uk |
|  | 不再需要 | ecom_order_unpaid_canceled_reason_no_longer_needed_uk |
|  | 其他 | ecom_order_unpaid_canceled_reason_other_uk |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected_uk |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs_uk |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed_uk |
|  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method_uk |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected_uk |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes_uk |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs_uk |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price_uk |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info_uk |
|  | 发货延迟 | buyer_cancel_late_shipment |
|  | 其他 | ecom_order_unpaid_canceled_reason_other_uk |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason_uk |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered_uk |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree_uk |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock_uk |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price_uk |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed_uk |
|  | 卖家无法履约订单 | seller_cancel_unpaid_reason_unable_to_fulfill_order |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 定价错误 | seller_cancel_reason_wrong_price_uk |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver_uk |
|  | 缺货 | seller_cancel_reason_out_of_stock_uk |
|  | 卖家无法履约订单 | seller_cancel_reason_unable_to_fulfill_order |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out_uk |
| 未通过风控审核 | system_cancel_anti_span_block_uk |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2_uk |
| 订单被系统取消 | package_cancel_uk |
| 订单被系统取消 | platform_cancel_uk |
| 包裹被拒收 | returned_to_shipper_refused_uk |
| 包裹配送失败 | returned_to_shipper_other_uk |
| 包裹破损 | package_damagaed_uk |
| 包裹丢失 | package_lost_uk |
| 配送延迟 | threepl_breach_uk |
| 包裹报废 | package_scrap_uk |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout_uk |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked_uk |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |



# ID market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 需要输入/更改优惠码 | buyer_cancel_need_to_input/change_coupon_code |
|  | 商品款式错误（颜色、尺码等） | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 不再需要 | ecom_order_unpaid_canceled_reason_no_longer_needed |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |
| 订单被系统取消 | system_cancel_failed_due_to_tts |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver |
## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 因充值超时自动取消 | system_cancel_virtual_timeout |
| 充值失败 | system_cancel_virtual_top_up_failed |
| 手机号无效 | system_cancel_virtual_phone_number_invalid |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |



# MY market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 需要输入/更改优惠码 | buyer_cancel_need_to_input/change_coupon_code |
|  | 商品款式错误（颜色、尺码等） | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |


## 卖家拒绝取消申请原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver |

## 系统取消原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |

# PH market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 需要输入/更改优惠码 | buyer_cancel_need_to_input/change_coupon_code |
|  | 商品款式错误（颜色、尺码等） | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
|  | 买家请求取消 | seller_cancel_unpaid_reason_buyer_requested_cancellation |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver |
|  | 买家请求取消 | seller_cancel_paid_reason_buyer_requested_cancellation |
## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |

# SG market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 需要输入/更改优惠码 | buyer_cancel_need_to_input/change_coupon_code |
|  | 商品款式错误（颜色、尺码等） | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_unable_to_deliver_to_buyer_address |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |

# TH market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 商品款式错误（颜色、尺码等） | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 需要输入/更改优惠码 | buyer_cancel_need_to_input/change_coupon_code |
|  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 不再需要 | ecom_order_unpaid_canceled_reason_no_longer_needed |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |
|  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |


# VN market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 需要输入/更改优惠码 | buyer_cancel_need_to_input/change_coupon_code |
|  | 商品款式错误（颜色、尺码等） | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 期望的支付方式不可用 | ecom_order_unpaid_canceled_reason_payment_method_not_available |
|  | 配送信息错误 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 有更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 其他 | ecom_order_unpaid_canceled_reason_other |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 取消原因无效 | order_manage_list_action_respond_popup_reject_reason_invalid_cancellation_reason |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered |
| 已与买家达成一致 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 商品已打包 | seller_reject_apply_product_has_been_packed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 买家未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至买家地址 | seller_cancel_paid_reason_address_not_deliver |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 买家付款逾期 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时自动取消 | system_cancel_order_reason_shipping_timeout |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因运单号无法追踪自动取消 | system_cancel_order_untracked |
| 买家未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们检测到您的订单存在风险，为保障交易安全已取消该订单。 | system_cancel_order_reason_potential_fraud |
| 订单被系统取消。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理买家的售后申请。  | system_cancel_order_reason_nrr_related |

# MX Market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed |
|  | 误购 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 忘记使用优惠券 | ecom_order_to_ship_canceled_reason_forgot_to_apply_coupons |
|  | 收货地址错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed |
|  | 误购 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 忘记使用优惠券 | ecom_order_to_ship_canceled_reason_forgot_to_apply_coupons |
|  | 收货地址错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 商品已发货。物流跟踪信息即将更新。 | seller_reject_apply_product_has_been_packed |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 客户未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
|  | 客户请求取消 | seller_cancel_unpaid_reason_buyer_requested_cancellation |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 客户请求取消 | seller_cancel_paid_reason_buyer_requested_cancellation |
|  | 无法配送至客户地址 | seller_cancel_paid_reason_address_not_deliver |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 客户逾期未付款 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时而自动取消 | system_cancel_order_reason_shipping_timeout |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 因运单号无法追踪而自动取消 | system_cancel_order_untracked |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因未在预计送达时间起 30 天内送达而自动取消 | system_cancel_order_exceed_edt_not_arrive |
| 客户未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |
| 因客户付款方式无法扣款，该订单已自动取消。 | system_cancel_payment_capture_failed |
| 因支付风控拦截，该订单已自动取消。 | system_cancel_payment_risk_review_failed |
| 因库存不足，该订单已自动取消。 | system_cancel_create_valid_order_failed |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们发现您的订单存在风险，出于安全原因已取消您的订单，以保护您的交易。 | system_cancel_order_reason_potential_fraud |
| 在例行审核中，我们发现您下的订单存在潜在问题，可能导致体验不符合我们的标准。为确保您获得良好的购物体验，我们已主动为您全额退款。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理客户的售后申请。  | system_cancel_order_reason_nrr_related |

# BR Market
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed |
|  | 误购 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 忘记使用优惠券 | ecom_order_to_ship_canceled_reason_forgot_to_apply_coupons |
|  | 收货地址错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 不再需要 | ecom_order_to_ship_canceled_reason_no_longer_needed |
|  | 误购 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 忘记使用优惠券 | ecom_order_to_ship_canceled_reason_forgot_to_apply_coupons |
|  | 收货地址错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 商品未按时发货 | ecom_order_to_ship_canceled_reason_not_shipped_on_time |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |


## 卖家拒绝取消申请原因
卖家可用于拒绝买家取消请求的原因
| **卖家可选择的拒绝取消原因** | **原因名称** |
| --- | --- |
| 商品已发货。物流跟踪信息即将更新。 | seller_reject_apply_product_has_been_packed |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 客户未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
|  | 客户请求取消 | seller_cancel_unpaid_reason_buyer_requested_cancellation |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 客户请求取消 | seller_cancel_paid_reason_buyer_requested_cancellation |
|  | 无法配送至客户地址 | seller_cancel_paid_reason_address_not_deliver |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 客户逾期未付款 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时而自动取消 | system_cancel_order_reason_shipping_timeout |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 因运单号无法追踪而自动取消 | system_cancel_order_untracked |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 因未在预计送达时间起 30 天内送达而自动取消 | system_cancel_order_exceed_edt_not_arrive |
| 客户未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |
| 因客户付款方式无法扣款，该订单已自动取消。 | system_cancel_payment_capture_failed |
| 因支付风控拦截，该订单已自动取消。 | system_cancel_payment_risk_review_failed |
| 因库存不足，该订单已自动取消。 | system_cancel_create_valid_order_failed |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们发现您的订单存在风险，出于安全原因已取消您的订单，以保护您的交易。 | system_cancel_order_reason_potential_fraud |
| 在例行审核中，我们发现您下的订单存在潜在问题，可能导致体验不符合我们的标准。为确保您获得良好的购物体验，我们已主动为您全额退款。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理客户的售后申请。  | system_cancel_order_reason_nrr_related |

# ES/IE/FR/DE/IT 市场
## 买家发起取消原因
买家发起取消请求时可使用以下原因。
| **订单状态** | **买家可选择的取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID <br/>  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 卖家未回复我的询问 / 卖家要求取消 | ecom_order_unpaid_canceled_reason_other |
|  | 不再需要 | ecom_order_unpaid_canceled_reason_no_longer_needed |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 无原因 | ecom_order_delivered_refund_reason_none |
|  | 发货延迟 | buyer_cancel_late_shipment |
|  | 配送信息错误 | ecom_order_to_ship_canceled_reason_wrong_delivery_info |
|  | 有更优惠的价格 | ecom_order_to_ship_canceled_reason_better_price |
|  | 配送费用过高 | ecom_order_to_ship_canceled_reason_high_delivery_costs |
|  | 折扣不及预期 | ecom_order_to_ship_canceled_reason_discount_not_expected |
|  | 误下订单 | ecom_order_to_ship_canceled_reason_created_by_mistakes |
|  | 卖家未回复我的询问 / 卖家要求取消 | ecom_order_unpaid_canceled_reason_other |
|  | 需要更改支付方式 | ecom_order_to_ship_canceled_reason_change_payment_method |
|  | 不再需要 | ecom_order_unpaid_canceled_reason_no_longer_needed |

## 卖家发起取消原因
卖家发起取消的可用原因
| **订单状态** | **卖家可选择的发起取消原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 客户未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
|  | 客户请求取消 | seller_cancel_unpaid_reason_buyer_requested_cancellation |
|  | 卖家无法履约订单 | seller_cancel_unpaid_reason_unable_to_fulfill_order |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 无法配送至客户地址 | seller_cancel_paid_reason_address_not_deliver |
|  | 客户请求取消 | seller_cancel_paid_reason_buyer_requested_cancellation |
|  | 卖家无法履约订单 | seller_cancel_reason_unable_to_fulfill_order |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 客户逾期未付款 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时而自动取消 | system_cancel_order_reason_shipping_timeout |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 因运单号无法追踪而自动取消 | system_cancel_order_untracked |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 客户未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |
| 因未在预计送达时间起 30 天内送达而自动取消 | system_cancel_order_exceed_edt_not_arrive |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 我们发现您的订单存在风险，出于安全原因已取消您的订单，以保护您的交易。 | system_cancel_order_reason_potential_fraud |
| 在例行审核中，我们发现您下的订单存在潜在问题，可能导致体验不符合我们的标准。为确保您获得良好的购物体验，我们已主动为您全额退款。 | system_cancel_order_reason_experience_related |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理客户的售后申请。  | system_cancel_order_reason_nrr_related |

# JP market
## 买家发起取消原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED <br/>  | 误下订单 | ecom_order_unpaid_canceled_reason_created_by_mistakes |
|  | 需要更改支付方式 | ecom_order_unpaid_canceled_reason_payment_method_not_available_S |
|  | 需要使用优惠券 | buyer_cancel_need_to_input/change_coupon_code |
|  | 需要更换颜色或尺码 | buyer_cancel_wrong_item_variation_(colour,_size,_etc.) |
|  | 需要更改配送地址 | ecom_order_unpaid_canceled_reason_wrong_delivery_info |
|  | 找到更优惠的价格 | ecom_order_unpaid_canceled_reason_better_price |
|  | 不再需要该商品 | ecom_order_unpaid_canceled_reason_no_longer_needed |
|  | 卖家未响应 | ecom_order_to_ship_canceled_reason_seller_no_response |
|  | 卖家请求取消订单 | ecom_order_unpaid_canceled_reason_seller_ask_cancel |


## 卖家发起取消原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| UNPAID | 定价错误 | seller_cancel_unpaid_reason_wrong_price |
|  | 缺货 | seller_cancel_unpaid_reason_out_of_stock |
|  | 客户请求取消 | seller_cancel_unpaid_reason_buyer_requested_cancellation |
|  | 客户未按时付款 | seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed |
|  | 卖家无法履约订单 | seller_cancel_unpaid_reason_unable_to_fulfill_order |
| ON_HOLD 和 AWAITING_SHIPMENT <br/>  | 定价错误 | seller_cancel_reason_wrong_price |
|  | 缺货 | seller_cancel_reason_out_of_stock |
|  | 客户请求取消 | seller_cancel_paid_reason_buyer_requested_cancellation |
|  | 无法配送至客户地址 | seller_cancel_paid_reason_address_not_deliver |
|  | 取消 / 退款可能性较高的订单  | seller_cancel_order_reason_potential_fraud |
|  | 卖家无法履约订单 | seller_cancel_reason_unable_to_fulfill_order |

## 系统取消原因
| **取消原因** | **原因名称** |
| --- | --- |
| 客户逾期未付款 | system_cancel_unpaid_time_out |
| 未通过风控审核 | system_cancel_anti_span_block |
| 入库失败 | system_cancel_cross_border_entry_warehouse_failed_reason2 |
| 订单被系统取消 | package_cancel |
| 订单被系统取消 | platform_cancel |
| 包裹被拒收 | returned_to_shipper_refused |
| 包裹配送失败 | returned_to_shipper_other |
| 包裹破损 | package_damagaed |
| 包裹丢失 | package_lost |
| 配送延迟 | threepl_breach |
| 包裹报废 | package_scrap |
| 因揽收超时而自动取消 | system_cancel_order_reason_shipping_timeout |
| 由于您未提供收货地址，该订单已自动取消。 | system_cancel_add_address_overtime |
| 因运单号无法追踪而自动取消 | system_cancel_order_untracked |
| 订单被系统取消 | ecom_cb_sc_out_return |
| 该订单因未在预计送达时间内送达而被自动取消。 | system_cancel_order_exceed_edt_not_arrive |
| 客户未付款 | ecom_order_unpaid_canceled_reason_not_want_pay |
| 因客户付款方式无法扣款，该订单已自动取消。 | system_cancel_payment_capture_failed |
| 因支付风控拦截，该订单已自动取消。 | system_cancel_payment_risk_review_failed |
| 因库存不足，该订单已自动取消。 | system_cancel_create_valid_order_failed |
| 证书未上传 | system_cancel_order_reason_coa_upload_more_than_24hrs |
| 无法验证证书 | system_cancel_order_reason_coa_2nd_upload_rejected |
| 无法完成认证 | system_cancel_order_reason_coa_rejected_fraud |
| 验证超时 | system_cancel_order_reason_coa_moderation_more_than_12hrs |
| 由于标签错误、邮资问题、第三方履约问题或重量差异，包装或配送未达到标准。 | system_cancel_unpaid_postage |
| 包裹配送失败 | early_refund_returned_to_shipper |

## Operator Cancel
| **取消原因** | **原因名称** |
| --- | --- |
| 我们发现您的订单存在风险，出于安全原因已取消您的订单，以保护您的交易。 | system_cancel_order_reason_potential_fraud |
| 在例行审核中，我们发现您下的订单存在潜在问题，可能导致体验不符合我们的标准。为确保您获得良好的购物体验，我们已主动为您全额退款。 | system_cancel_order_reason_experience_related |
| 未通过风控审核 | operator_cancel_risk_control_block |
| 由于您的商品违反平台差评政策，我们已取消此交易。建议您处理客户的售后申请。  | system_cancel_order_reason_nrr_related |
