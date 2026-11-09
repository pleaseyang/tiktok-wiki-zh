# 退货原因

# US market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| `AWAITING_COLLECTION` <br/> `IN_TRANSIT` | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need |
| `DELIVERED` | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need |
|  | 商品不合适 (部分类目) | buyer_return_and_refund_item_doesn't_fit |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 缺少或损坏的部件 (缺少部件) | ecom_order_delivered_refund_and_return_reason_missing_product |
|  | 商品或包装损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 商品送达太晚 | buyer_return_and_refund_item_arrived_too_late |
|  | 面料、材质或款式与预期不符 | buyer_return_and_refund_fabric,_material_or_style_not_as_expected |
|  | 商品过大 | ecom_order_delivered_refund_and_return_reason_item_too_big |
|  | 商品过小 | ecom_order_delivered_refund_and_return_reason_item_too_small |
## 卖家拒绝退货申请原因
### **1st Review**
| **卖家可选择的拒绝退货原因** | **原因名称** |
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

### **2nd Review**
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| `DELIVERED` | 不再需要 | seller_ecom_delivered_return_refund_reason1 |


---


# UK market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need_uk |
| DELIVERED | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description_uk |
|  | 缺少商品或配件 | ecom_order_delivered_refund_and_return_reason_missing_product_uk |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged_uk |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective_uk |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product_uk |
|  | 其他 | ecom_order_delivered_refund_and_return_reason_other_uk |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
|  | 不适合我 | buyer_return_and_refund_does_not_suit_me |
|  | 商品太大/太长 | buyer_return_and_refund_item_is_too_big/long |
|  | 商品太小/太短 | buyer_return_and_refund_item_is_too_small/short |
|  | 下单了多个尺码 | buyer_return_and_refund_multiple_sizes_ordered |
|  | 质量或款式与预期不符 | buyer_return_and_refund_quality_or_style_not_as_expected |
|  | 下单尺码错误 | buyer_return_and_refund_ordered_incorrect_size |
|  | 未经授权的购买 | buyer_return_and_refund_unauthorised_purchase |
|  | 商品已过期/变质 | buyer_return_and_refund_product_is_expired/spoiled |
|  | 商品送达时未冷冻 | buyer_return_and_refund_product_not_frozen_on_arrival |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1_uk |
| 不适用无理由退货 | reverse_reject_request_reason_2_uk |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3_uk |
| 商品按时送达 | reverse_reject_request_reason_4_uk |
| 您已与买家达成一致 | reverse_reject_request_reason_5_uk |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1_uk |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2_uk |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3_uk |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4_uk |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5_uk |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 不再需要 | seller_ecom_delivered_return_refund_reason1_uk |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description_seller_uk |
|  | 缺少商品或配件 | ecom_order_delivered_refund_and_return_reason_missing_product_seller_uk |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged_seller_uk |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective_seller_uk |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product_seller_uk |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit_seller_uk |


---


# ID market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_and_return_reason_missed_delivery |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product_seller |


---


# MY market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_and_return_reason_missed_delivery |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
Unsupported


---


# PH market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_and_return_reason_missed_delivery |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
Unsupported


---


# SG market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_and_return_reason_missed_delivery |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
Unsupported


---


# TH market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_and_return_reason_missed_delivery |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
Unsupported


---


# VN market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product |
|  | 超过预计送达日期 | ecom_order_delivered_refund_and_return_reason_missed_delivery |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 买家退货原因无效 | reverse_reject_request_reason_1 |
| 不适用无理由退货 | reverse_reject_request_reason_2 |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3 |
| 商品按时送达 | reverse_reject_request_reason_4 |
| 您已与买家达成一致 | reverse_reject_request_reason_5 |
| 商品无误 | seller_reject_apply_item_is_correct |
| 商品将分开发货 | seller_reject_apply_products_will_be_sent_separately |
| 原因不明或缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品功能正常/买家使用不当 | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 商品已发货，无法从物流处召回包裹。 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与买家达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 不再需要 | seller_ecom_delivered_return_refund_reason1 |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description_seller |
|  | 缺少商品或配件 | ecom_order_delivered_refund_and_return_reason_missing_product_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged_seller |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product_seller |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit_seller |


---


# MX market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 尺寸不合适 | buyer_return_and_refund_item_doesn't_fit |
|  | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need |
|  | 商品有缺陷 | ecom_order_delivered_refund_reason_defective |
|  | 商品送达太晚 | buyer_return_and_refund_item_arrived_too_late |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 面料、材质或款式与预期不符 | buyer_return_and_refund_fabric,_material_or_style_not_as_expected |
|  | 颜色或图案与预期不符 | buyer_return_and_refund_color_or_pattern_not_as_expected |
|  | 商品或包装损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| Product functions well/错误用法 by the customer | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品无误 | seller_reject_apply_item_is_correct |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 商品在途 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
| 您的商品分多个包裹发货。 | seller_reject_apply_products_will_be_sent_separately |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与客户达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 不再需要 | seller_ecom_delivered_return_refund_reason1 |
|  | 配送延迟 (商品送达太晚) | seller_return_late_delivery |
|  | 缺少商品或部件 | seller_return_missing_item |
|  | 商品或包装损坏 | seller_return_damaged_item |
|  | 商品有缺陷 | seller_return_defective_item |
|  | 发送了错误的商品 | seller_return_wrong_item_was_sent |


---


# BR market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED | 尺寸不合适 | buyer_return_and_refund_item_doesn't_fit |
|  | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need |
|  | 商品有缺陷 | ecom_order_delivered_refund_reason_defective |
|  | 商品送达太晚 | buyer_return_and_refund_item_arrived_too_late |
|  | 发送了错误的商品 | ecom_order_delivered_refund_reason_wrong_product |
|  | 面料、材质或款式与预期不符 | buyer_return_and_refund_fabric,_material_or_style_not_as_expected |
|  | 颜色或图案与预期不符 | buyer_return_and_refund_color_or_pattern_not_as_expected |
|  | 商品或包装损坏 | ecom_order_delivered_refund_and_return_reason_damaged |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description |
|  | 已收到包裹但缺少商品 | ecom_order_delivered_refund_and_return_reason_missing_product |
## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| Product functions well/错误用法 by the customer | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 商品无误 | seller_reject_apply_item_is_correct |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 商品在途 | seller_reject_apply_package_has_not_exceeded_estimated_delivery_time |
| 您的商品分多个包裹发货。 | seller_reject_apply_products_will_be_sent_separately |
| 需要申请退款和退货 | seller_reject_apply_need_to_apply_for_refund&return |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |
| 您已与客户达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 不再需要 | seller_ecom_delivered_return_refund_reason1 |
|  | 配送延迟 (商品送达太晚) | seller_return_late_delivery |
|  | 缺少商品或部件 | seller_return_missing_item |
|  | 商品或包装损坏 | seller_return_damaged_item |
|  | 商品有缺陷 | seller_return_defective_item |
|  | 发送了错误的商品 | seller_return_wrong_item_was_sent |


---


# EU 市场
目前，支持的 EU 市场包括:

* Spain (ES)
* Ireland (IE)
* France (FR)
* Germany (DE)
* Italy (IT)

## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED <br/>  | 不再需要 | ecom_order_delivered_refund_reason_no_need |
|  | 不再需要 | ecom_order_delivered_refund_and_return_reason_no_need |
|  | 超过预计送达日期 | ecom_order_delivered_refund_reason_missed_delivery_date |
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

## 卖家拒绝退货申请原因
卖家拒绝退货请求
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 商品按时送达 | reverse_reject_request_reason_4_uk |
| 不适用无理由退货 | reverse_reject_request_reason_2_uk |
| 不符合退货条件（如已使用或破损） | reverse_reject_request_reason_3_uk |
| 商品按时送达 | order_manage_list_action_respond_popup_reject_reason_delivered_uk |
| 买家退货原因无效 | reverse_reject_request_reason_1_uk |
| Product functions well/错误用法 by the customer | seller_reject_apply_product_functions_well/buyer_use_in_wrong_way |
| 原因不明/缺乏证据 | seller_reject_apply_reason_is_unclear_or_lack_of_evidence |
| 已与买家达成协议 | order_manage_list_action_respond_popup_reject_reason_buyer_agree |
| 您已与客户达成一致 | reverse_reject_request_reason_5 |
| 您的商品分多个包裹发货。 | seller_reject_apply_products_will_be_sent_separately |
卖家拒绝接收包裹
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 您已与客户达成一致 | seller_reject_apply_you_have_reached_an_agreement_with_the_buyer |
| 退回的商品与发出的商品不符 | reverse_reject_return_parcel_reason_1 |
| 不符合退货条件（如已使用或破损） | reverse_reject_return_parcel_reason_2 |
| 缺少商品和/或商品部件 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用 | reverse_reject_return_parcel_reason_5 |

## 卖家发起退货原因
| **订单状态** | **卖家可选择的发起退货原因** | **原因名称** |
| --- | --- | --- |
| DELIVERED | 不再需要 | seller_ecom_delivered_return_refund_reason1 |
|  | 商品与描述不符 | ecom_order_delivered_refund_and_return_reason_not_match_description_seller |
|  | 缺少商品或配件 | ecom_order_delivered_refund_and_return_reason_missing_product_seller |
|  | 包裹或商品已损坏 | ecom_order_delivered_refund_and_return_reason_damaged_seller |
|  | 商品有缺陷或无法使用 | ecom_order_delivered_refund_and_return_reason_defective_seller |
|  | 发送了错误的商品 | ecom_order_delivered_refund_and_return_reason_wrong_product_seller |
|  | 疑似假冒商品 | buyer_return_and_refund_suspected_counterfeit_seller |


---


# JP market
## 买家发起退货原因
| **订单状态** | **买家可选择的退货原因** | **原因名称** |
| --- | --- | --- |
| AWAITING_COLLECTION <br/> IN_TRANSIT <br/> DELIVERED <br/>  | 不再需要 (商品必须以密封/原始状态退回)。 | ecom_order_delivered_refund_reason_no_need |
|  | 已收到包裹但缺少部件或配件。 | ecom_order_delivered_refund_and_return_reason_missing_parts_JP |
|  | 商品与描述不符。 | ecom_order_delivered_refund_and_return_reason_not_match_description_JP |
|  | 包裹或商品受损。 | ecom_order_delivered_refund_reason_damaged |
|  | 商品有缺陷或无法正常使用。 | ecom_order_delivered_refund_reason_defective |
|  | 发错商品。 | ecom_order_delivered_refund_and_return_reason_wrong_product_JP |
|  | 错过预计送达日期。 | ecom_order_delivered_refund_and_return_reason_missed_delivery_date_JP |
## 卖家拒绝退货申请原因
卖家拒绝退货请求。
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| reverse_reject_refund_request_unclear_evidence_Test | 原因不明 / 缺少证据。 |
| ecom_reverse_reject_cancel_reason_product_packed | 商品已发货。物流跟踪信息即将更新。 |
| ecom_reverse_reject_refund_request_failed_delivery | 投递失败。 |
| ecom_reverse_reject_refund_request_package_delivery_multiple_boxes | 商品分多个包裹发货。 |
| ecom_reverse_reject_refund_request_replacement_shipped | 已寄出替换商品。 |
| ecom_reverse_reject_apply_buyer_agree_jp | 已与买家达成协议。 |
| seller_reject_apply_reason_delivered_jp | 商品按时送达。 |
| seller_reject_apply_buyers_responsibility_for_incorrect_address | 包裹已成功送达所提供的收货地址。 |
| seller_reject_apply_item_is_correct | 商品无误。 |
| seller_reject_apply_package_has_not_exceeded_estimated_delivery_time | 商品按时送达。 |
| seller_reject_apply_product_functions_well/buyer_use_in_wrong_way | Product functions well / 错误用法 by the customer。 |
| seller_reject_apply_reason_is_unclear_or_lack_of_evidence | 原因不明 / 缺少证据。 |
| seller_reject_apply_unable_to_change_address | 无法更改地址。 |
卖家拒绝接收包裹。
| **卖家可选择的拒绝退货原因** | **原因名称** |
| --- | --- |
| 退回的商品与发出的商品不一致。 | reverse_reject_return_parcel_reason_1 |
| 缺少商品和/或商品零件。 | reverse_reject_return_parcel_reason_3 |
| 我未收到包裹。 | reverse_reject_return_parcel_reason_4 |
| 商品已损坏或已使用。 | reverse_reject_return_parcel_reason_5 |
