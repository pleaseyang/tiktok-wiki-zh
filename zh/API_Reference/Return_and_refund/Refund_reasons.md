# 退款原因

📌 不同的订单状态需要不同的原因。查看表格左侧的状态以找到适用的原因，并在调用 API 时将原因名称作为请求参数包含在内。如果取消原因不适用于该订单状态，API 将返回 '25001021 Reason not match order status' 错误。
# US market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| `AWAITING_COLLECTION` <br/> `IN_TRANSIT` | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
| `DELIVERED` | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 已收到包裹但缺少商品 | ecom_order_delivered_refund_reason_missing_product |
|  | 商品或包装损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷 | ecom_order_delivered_refund_reason_defective |
|  | 零件缺失或损坏 | ecom_order_delivered_refund_reason_missing_broken_parts |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_1 |
## 卖家拒绝退款申请原因
> ### **1st Review**

| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 商品无误 | reverse_reject_refund_request_correct_item |
| 商品分多个包裹发货  | reverse_reject_refund_request_package_delivery_multiple_boxes |
| 原因不明/缺乏证据 | reverse_reject_refund_request_unclear_evidence |
| Product functions well/错误用法 by the customer | reverse_reject_refund_request_product_function_well |
| 商品在途 | reverse_reject_refund_request_package_delivery_timing |
| 已寄出替换商品 | reverse_reject_refund_request_no_reason_shipped_replacement |
| 投递失败  | reverse_reject_refund_request_no_reason_failed_delivery_attempt |
| 包裹已成功送达所提供的收货地址。 | reverse_reject_refund_request_incorrect_address |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |

## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| `AWAITING_COLLECTION` <br/> `IN_TRANSIT` | 包裹丢失 | seller_shipped_refund_package_lost |
|  | 包裹配送失败 | seller_shipped_refund_package_delivery_failed |
|  | 超过预计送达日期 | seller_shipped_refund_miss_estimated_delivery_date |
| `DELIVERED` | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_seller |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_seller |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_seller |
|  | 包裹丢失 | seller_shipped_refund_package_lost |
|  | 包裹配送失败 | seller_shipped_refund_package_delivery_failed |


---


# UK market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 包裹未按时送达 | buyer_refund_package_didn't_arrive_on_time |
| DELIVERED | 不再需要 | ecom_order_delivered_refund_reason_no_need_uk |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_uk |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_uk |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_uk |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_uk |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective_uk |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_uk |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_uk |
|  | 其他 | ecom_order_delivered_refund_reason_other_uk |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
|  | 不适合我 | buyer_refund_does_not_suit_me |
|  | 下单了多个尺码 | buyer_refund_multiple_sizes_ordered |
|  | 质量或款式与预期不符 | buyer_refund_quality_or_style_not_as_expected |
|  | 商品太大/太长 | buyer_refund_item_is_too_big/long |
|  | 商品太小/太短 | buyer_refund_item_is_too_small/short |
|  | 下单尺码错误 | buyer_refund_ordered_incorrect_size |
|  | 未经授权的购买 | buyer_refund_unauthorised_purchase |
|  | 商品已过期/变质 | buyer_refund_product_is_expired/spoiled |
|  | 商品送达时未冷冻 | buyer_refund_product_not_frozen_on_arrival |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1_uk |
| 不适用无理由退货 | reverse_reject_request_reason_2_uk |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3_uk |
| 商品按时送达 | reverse_reject_request_reason_4_uk |
| 您已与买家达成一致 | reverse_reject_request_reason_5_uk |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 包裹丢失 | seller_package_lost_uk |
|  | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time_seller_uk |
| DELIVERED | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller_uk |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_seller_uk |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description_seller_uk |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_seller_uk |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_seller_uk |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_seller_uk |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective_seller_uk |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit_seller_uk |


---


# ID market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
| DELIVERED | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 其他 | ecom_order_delivered_refund_reason_other |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |


---


# MY market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
| DELIVERED | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
Unsupported


---


# PH market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
| DELIVERED | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
Unsupported


---


# SG market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
| DELIVERED | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
Unsupported


---


# TH market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
|  | 配送信息错误 | ecom_order_shipped_refund_wrong_delivery_info |
|  | 其他 | ecom_order_shipped_refund_other |
| DELIVERED | 不再需要 | ecom_order_delivered_refund_reason_no_need |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
|  | 其他 | ecom_order_delivered_refund_reason_other |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
Unsupported


---


# VN market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time |
| DELIVERED | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match |
|  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 无法更改地址 | seller_reject_apply_unable_to_change_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
| 买家填写地址错误的责任 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time_seller |
|  | 包裹丢失 | seller_package_lost |
| DELIVERED | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_seller |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_seller |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_seller |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_seller |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective_seller |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit_seller |


---


# MX market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品有缺陷 | ecom_order_delivered_refund_reason_defective |
|  | 商品或包装损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品在途 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
| 包裹已成功送达所提供的收货地址。 | seller_reject_apply_buyers_responsibility_for_incorrect_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 包裹丢失 | seller_package_lost |
|  | 超过预计送达日期 | seller_shipped_refund_miss_estimated_delivery_date |
|  | 包裹丢失 | seller_shipped_refund_package_lost |
|  | 包裹配送失败 | seller_shipped_refund_package_delivery_failed |
|  | 包裹丢失 | ecom_seller_order_delivered_refund_reason_return_proxy_app |
| DELIVERED | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_seller |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_seller |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_seller |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_seller |
|  | 超过预计送达日期 | seller_shipped_refund_miss_estimated_delivery_date |
|  | 包裹丢失 | seller_shipped_refund_package_lost |
|  | 包裹配送失败 | seller_shipped_refund_package_delivery_failed |
|  | 包裹丢失 | ecom_seller_order_delivered_refund_reason_return_proxy_app |


---


# BR market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 商品有缺陷 | ecom_order_delivered_refund_reason_defective |
|  | 商品或包装损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective |
## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品在途 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
| 包裹已成功送达所提供的收货地址。 | seller_reject_apply_buyers_responsibility_for_incorrect_address |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 包裹丢失 | seller_package_lost |
|  | 超过预计送达日期 | seller_shipped_refund_miss_estimated_delivery_date |
|  | 包裹丢失 | seller_shipped_refund_package_lost |
|  | 包裹配送失败 | seller_shipped_refund_package_delivery_failed |
|  | 包裹丢失 | ecom_seller_order_delivered_refund_reason_return_proxy_app |
| DELIVERED | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_seller |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_seller |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_seller |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_seller |
|  | 超过预计送达日期 | seller_shipped_refund_miss_estimated_delivery_date |
|  | 包裹丢失 | seller_shipped_refund_package_lost |
|  | 包裹配送失败 | seller_shipped_refund_package_delivery_failed |
|  | 包裹丢失 | ecom_seller_order_delivered_refund_reason_return_proxy_app |



---


# EU 市场
目前，支持的 EU 市场包括:

* Spain (ES)
* Ireland (IE)
* France (FR)
* Germany (DE)
* Italy (IT)

## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 不再需要 | ecom_order_delivered_refund_reason_no_need |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received |
|  | 其他 | ecom_order_delivered_refund_and_return_reason_other |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 缺少商品或配件 | ecom_order_delivered_refund_and_return_reason_missing_product |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 不适合我 | buyer_return_and_refund_does_not_suit_me |
|  | 商品太大/太长 | buyer_return_and_refund_item_is_too_big/long |
|  | 商品太小/太短 | buyer_return_and_refund_item_is_too_small/short |
|  | 下单了多个尺码 | buyer_return_and_refund_multiple_sizes_ordered |
|  | 质量或款式与预期不符 | buyer_return_and_refund_quality_or_style_not_as_expected |
|  | 未经授权的购买 | buyer_return_and_refund_unauthorised_purchase |
|  | 商品已过期/变质 | buyer_return_and_refund_product_is_expired/spoiled |
|  | 商品送达时未冷冻 | buyer_return_and_refund_product_not_frozen_on_arrival |
|  | 下单尺码错误 | buyer_return_and_refund_ordered_incorrect_size |


## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 商品按时送达 | reverse_reject_request_reason_4_uk |
| 不适用无理由退货 | reverse_reject_request_reason_2_uk |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered_uk |
| 包裹已成功送达所提供的收货地址。 | seller_reject_apply_buyer's_responsibility_for_incorrect_address |
| Product functions well/错误用法 by the customer | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 包裹已送达但买家未收到，需要更多信息 | seller_reject_apply_reason_is_unclear_/_lack_of_evidence |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 已与买家达成协议 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 商品在途 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
| 您的商品分多个包裹发货。 | seller_reject_apply_products_will_be_sent_separately |
| 商品已发货。物流跟踪信息即将更新。 | seller_reject_apply_product_has_been_packed |

## 卖家发起退款原因
| **订单状态** | **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 包裹丢失 | seller_package_lost |
|  | 商品无法按时送达 | ecom_order_shipped_refund_reason_not_arrive_on_time_seller |
| DELIVERED <br/>  | 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |
|  | 未收到包裹 | ecom_order_delivered_refund_reason_not_received_seller |
|  | 商品与描述不符 | ecom_order_delivered_refund_reason_not_match_description_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_reason_damaged_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product_seller |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date_seller |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_reason_defective_seller |
|  | 疑似假冒商品 | buyer_refund_suspected_counterfeit_seller |


---


# JP market
## 买家发起退款原因
| **订单状态** | **买家可选择的退款原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 不再需要 (商品必须以密封/原始状态退回)。 | ecom_order_delivered_refund_reason_no_need |
|  | 商品未按时送达。 | ecom_order_shipped_refund_reason_not_arrive_on_time_JP |
|  | 未收到包裹。 | ecom_order_delivered_refund_reason_not_received |
|  | 已收到包裹但缺少部分商品。 | ecom_order_delivered_refund_reason_missing_product_JP |
|  | 已收到包裹但缺少部件或配件。 | ecom_order_delivered_refund_and_return_reason_missing_parts_JP |
|  | 商品与描述不符。 | ecom_order_delivered_refund_and_return_reason_not_match_description_JP |
|  | 包裹或商品受损。 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法正常使用。 | ecom_order_delivered_refund_reason_defective |
|  | 发错商品。 | ecom_order_delivered_refund_and_return_reason_wrong_product_JP |
|  | 错过预计送达日期。 | ecom_order_delivered_refund_and_return_reason_missed_delivery_date_JP |


## 卖家拒绝退款申请原因
| **卖家可选择的拒绝退款原因** | **原因名称** |
| --- | --- |
| 原因不明 / 缺少证据。 | reverse_reject_refund_request_unclear_evidence_Test |
| 商品已发货。物流跟踪信息即将更新。 | ecom_reverse_reject_cancel_reason_product_packed |
| 投递失败。 | ecom_reverse_reject_refund_request_failed_delivery |
| 商品分多个包裹发货。 | ecom_reverse_reject_refund_request_package_delivery_multiple_boxes |
| 已寄出替换商品。 | ecom_reverse_reject_refund_request_replacement_shipped |
| 已与买家达成协议。 | ecom_reverse_reject_apply_buyer_agree_jp |
| 商品按时送达。 | seller_reject_apply_reason_delivered_jp |
| 包裹已成功送达所提供的收货地址。 | seller_reject_apply_buyers_responsibility_for_incorrect_address |
| 商品无误。 | seller_reject_apply_item_is_correct |
| 商品按时送达。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
| Product functions well/错误用法 by the customer。 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明 / 缺少证据。 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 无法更改地址。 | seller_reject_apply_unable_to_change_address |

## 卖家发起退款原因
| **卖家可选择的发起退款原因** | **原因名称** |
| --- | --- |
| 缺少商品或配件 | ecom_order_delivered_refund_reason_missing_product_seller |
| 常规调整。 | ecom_order_delivered_refund_reason_general_adjustment |
| 未收到包裹。 | ecom_order_delivered_refund_reason_not_received_seller |
| 商品与描述不符。 | ecom_order_delivered_refund_reason_not_match_description_seller |
| 包裹或商品受损。 | ecom_order_delivered_refund_reason_damaged_seller |
| 发送了错误的商品。 | ecom_order_delivered_refund_reason_wrong_product_seller |
| 错过预计送达日期。 | ecom_order_delivered_refund_reason_missed_delivery_date_seller |
| 包裹丢失。 | seller_package_lost |
| 包裹丢失。 | seller_shipped_refund_package_lost |
| 包裹配送失败。 | seller_shipped_refund_package_delivery_failed |
| 错过预计送达日期。 | seller_shipped_refund_miss_estimated_delivery_date |
| 包裹丢失。 | ecom_seller_order_delivered_refund_reason_return_proxy_app |
