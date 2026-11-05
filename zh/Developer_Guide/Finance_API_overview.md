# Finance API 概述

# 背景
你可以获取指定订单或日期范围的交易详情。还可以获取指定日期范围的付款详情。
| API | 描述 |
| --- | --- |
| [GET Statements](https://partner.tiktokshop.com/docv2/page/get-statements-202309) <br/> | 获取指定日期范围内的对账单记录列表，按日结算。你可以根据付款状态筛选对账单。 |
| [GET Payments](https://partner.tiktokshop.com/docv2/page/get-payments-202309) | 根据日期范围获取付款列表，包括当前付款状态。使用此列表与卖家的银行账户进行对账。 |
| [GET Transactions by Statement](https://partner.tiktokshop.com/docv2/page/get-transactions-by-statement-202501) | 根据 statement_id 获取交易列表。我们将返回订单列表。如果需要 SKU 级别的交易详情，将 order_id 传入 GET Transactions by Order。 |
| [GET Transactions by Order](https://partner.tiktokshop.com/docv2/page/get-transactions-by-order-202501) | 获取与指定订单 ID 关联的交易列表。它还返回 SKU 级别的交易详情。 |
| [GET Unsettled Transactions](https://partner.tiktokshop.com/docv2/page/get-unsettled-transactions-202507) | 获取卖家生成的未结算交易列表，返回订单 ID 和调整 ID 的详细费用明细。 |

### Endpoint 使用建议：
如果你想获取订单级别的结算交易：
— 从 **GET Statements** 获取每日对账单信息，包括 statement ID
— 使用从 **GET Statements** 获取的 statement ID，从 **GET Transactions by Statement** 获取订单级别的结算详情

如果你想获取订单级别的未结算交易：
— 从 **GET Unsettled Transactions** 获取未结算交易信息，包括 order ID 和 adjustment ID

如果你想获取 SKU 级别的结算交易：
— 从 **GET Statements** 获取每日对账单信息，包括 statement ID
— 使用从 **GET Statements** 获取的 statement ID，从 **GET Transactions by Statement** 获取订单级别的结算详情，包括 order ID
— 使用从 **GET Transactions by Statement** 获取的 order ID，从 **GET Transactions by Order** 获取 SKU 级别的结算详情
# 重要概念
**对账单（Statements）**：用于描述已结算订单集合的记录。每个卖家每天有一份对账单。对账单每天生成（UTC 0:00），并在次日 0:00 关闭。关闭后，对账单将自动签发并发起付款。一份对账单对应一笔付款。但在特殊情况下（例如结算金额太小，不满足付款要求时），多份对账单将合并为一笔付款。
**付款（Payments）**：用于描述资金支出交易的记录。当付款发起时，此文档可作为与银行账户对账的依据。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/eb49e5b7a4df450db870eb9f113ece72~tplv-k9wyc2ijk0-image.image)


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/087759034bd841a7a8ec237820805763~tplv-k9wyc2ijk0-image.image)

# 常见问题
## 为什么订单尚未结算？
请参阅 TikTok Shop Academy 中适用于你所在市场的结算规则。

<br/>

## 调整类型有哪些？
| **调整类型** | **描述** |
| --- | --- |
| 运费调整 | 当卖家支付的运费存在差异或错误时的调整。 |
| 运费补偿 | 因实际运费与预付运费之间的差异而给予卖家的补偿。 |
| 拒付（Chargeback） | 客户在其账户对账单或交易报告中成功对某项交易提出争议后，退回至支付卡的款项。 |
| 客户服务补偿 | 售后期间由客户服务向客户支付的额外补偿。 |
| 促销调整 | 当卖家参与平台促销且促销价格与卖家实际支付金额之间存在差异时的调整。 |
| 平台补偿 | 因卖家成功申诉客户争议而向卖家支付的补偿。 |
| 平台罚款 | 在确认违反平台政策后，我们已根据政策从account中扣除了相应的罚款金额。请参阅发送给您的电子邮件通知。 |
| 样品运费 | 使用平台物流服务商发送样品时收取的费用。 |
| 物流赔偿 | 你的订单因物流问题丢失或损坏。我们对此问题深表歉意，并已为此订单提供赔偿。<br/>平台已核实退货或退款订单 ID 的物流信息，且订单的退货/退款申请已获批准。由于此次退款的原因非卖家责任，TikTok 已向客户支付退款金额。<br/>由 TikTok Shop 支付的因物流相关问题造成的损失赔偿 |
| 平台赔偿 | 平台仅退款不退货：订单已按 TikTok 仅退款不退货政策处理。由于买家对订单问题负责，我们已提供赔偿以弥补损失。详情请参阅 TikTok 仅退款不退货政策。<br/>平台仅退款不退货：订单已按 TikTok 仅退款不退货政策处理。审核订单后，你可能会获得补贴以抵消成本。详情请参阅 TikTok 仅退款不退货政策。<br/>平台已核实退货或退款订单 ID，且订单的退货/退款申请已获批准。由于此次退款的原因非卖家责任，TikTok 已承担向客户的退款金额。<br/>由 TikTok Shop 支付的因客户不满意导致的赔偿 |
| 卖家扣款 | 用户已为订单提交"退货退款"申请。根据 TikTok Shop 政策，如果退货或退款是由商品问题或延迟发货引起的，卖家将承担退货运费。<br/>订单被发现符合欺诈定义，且存在以下问题之一或类似问题：发送空包裹给客户、发送的商品与商品展示页面不符、发送的商品价值低于宣传。卖家负责与此问题相关的费用。<br/>根据 TikTok Shop 防伪政策，订单中的商品被视为假冒商品。卖家负责与此问题相关的费用。<br/>订单中的商品被视为存在缺陷并给客户造成了不良体验。根据 TikTok Shop 的政策，卖家负责向客户提供的补偿券的费用。<br/>当客户因卖家责任的问题对体验不满意时，卖家负责相关费用。 |
| 运费退还 | 作为参与平台活动的一部分给予卖家的运费退还。 |
| 仓库服务费 | 作为仓库服务提供的一部分收取的费用，如包装服务操作费、包装费、条码贴标费、新品检验服务费等。 |
| 平台佣金调整 | 当卖家支付的平台佣金存在差异时的调整。 |
| 平台佣金补偿 | 当卖家支付的平台佣金存在差异时向卖家支付的补偿。 |
| 其他调整 | 其他原因的调整。 |

<br/>
## 在哪里可以查看 API 返回的数据（在 TikTok Shop Seller Center 中）？
| API 名称 | 相关 Seller Center 页面 |
| --- | --- |
| Get Payments <br/> | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9c84e160dfca436aaffc3e4535949b64~tplv-k9wyc2ijk0-image.image) <br/> |
| Get Statements <br/> | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/21931823181c4c39be3e1f767b3c7c63~tplv-k9wyc2ijk0-image.image) <br/> |
| Get Statement Transactions | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/06f0d12a6bd547b7bd260f0f951b2b92~tplv-k9wyc2ijk0-image.image) <br/> |
| Get Order Statement Transactions | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/90f3e31424dd4b1395317d514b580dff~tplv-k9wyc2ijk0-image.image) <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9b820eba88284d59ace5e0d88d4e296d~tplv-k9wyc2ijk0-image.image) <br/> |

<br/>

## **为什么 API 响应中缺少订单？**
尚未结算的订单不会出现在 OpenAPI 响应中。有关订单未结算的更多可能原因，请参阅[常见问题](https://partner.tiktokshop.com/docv2/page/650b1f13c16ffe02b8012c2e#Frequently%20Asked%20Questions)中的问题 1。

