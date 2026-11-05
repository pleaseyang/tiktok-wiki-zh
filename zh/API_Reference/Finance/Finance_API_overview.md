# Finance API 概述

# 背景
您可以获取指定订单或日期范围的交易详情，也可以获取指定日期范围的付款详情。
| API | 描述  |
| --- | --- |
| [GET Statements](https://partner.tiktokshop.com/docv2/page/get-statements-202309) <br/>  | 获取指定日期范围内的账单记录列表，按日结算。您可以根据付款状态筛选账单。 |
| [GET Payments](https://partner.tiktokshop.com/docv2/page/get-payments-202309) | 根据日期范围获取付款列表，包括当前付款状态。使用此列表将付款与卖家的银行账户进行对账。 |
| [GET Transactions by Statement](https://partner.tiktokshop.com/docv2/page/get-transactions-by-statement-202501) | 根据 statement_id 获取交易列表。我们将返回订单列表。如果您需要 SKU 级别的交易详情，请将 order_id 传入 GET Transactions by Order。 |
| [GET Transactions by Order](https://partner.tiktokshop.com/docv2/page/get-transactions-by-order-202501) | 获取与订单 ID 指定的订单关联的交易列表。它还返回 SKU 级别的交易详情。  |
| [GET Unsettled Transactions](https://partner.tiktokshop.com/docv2/page/get-unsettled-transactions-202507) | 获取卖家生成的未结算交易列表，返回订单 ID 和调整 ID 的详细费用明细。 |

### Endpoint 使用建议：
如果您想获取订单级别的结算交易：
— 从 **GET Statements** 获取每日账单信息，包括 statement ID
— 使用从 **GET Statements** 获取的 statement ID，通过 **GET Transactions by Statement** 获取订单级别的结算详情

如果您想获取订单级别的未结算交易：
— 从 **GET Unsettled Transactions** 获取未结算交易信息，包括 order ID 和 adjustment ID

如果您想获取 SKU 级别的结算交易：
— 从 **GET Statements** 获取每日账单信息，包括 statement ID
— 使用从 **GET Statements** 获取的 statement ID，通过 **GET Transactions by Statement** 获取订单级别的结算详情，包括 order ID
— 使用从 **GET Transactions by Statement** 获取的 order ID，通过 **GET Transactions by Order** 获取 SKU 级别的结算详情
# 重要概念
**Statements（账单）**：用于描述已结算订单集合的记录。每个卖家每天有一个账单。账单每天（UTC 0:00）生成，并在次日 0:00 关闭。关闭后，账单将自动发出并发起付款。一个账单对应一笔付款。但在特殊情况下（例如，结算金额太小，不满足付款要求），多个账单将合并为一笔付款。
**Payments（付款）**：用于描述付款资金交易的记录。当付款发起时，此文档可作为与银行账户对账的依据。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/eb49e5b7a4df450db870eb9f113ece72~tplv-k9wyc2ijk0-image.image)


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/087759034bd841a7a8ec237820805763~tplv-k9wyc2ijk0-image.image)

# 常见问题 
## 为什么订单尚未结算？
请参考 TikTok Shop Academy 上您所在市场的具体结算规则。

<br/>

## 调整类型有哪些？
| **调整类型** | **描述** |
| --- | --- |
| Shipping fee adjustment（运费调整） | 当卖家支付的运费存在差异或错误时进行的调整。 |
| Shipping fee compensation（运费补偿） | 由于实际运费与预付运费之间的差异而给予卖家的补偿。 |
| Chargeback（拒付） | 客户成功在其账户账单或交易报告中对某笔交易提出争议后，退回至支付卡的款项。 |
| Customer service compensation（客服补偿） | 这是售后期内由客服向客户支付的额外补偿或赔偿金。 |
| Promotion adjustment（促销调整） | 当卖家参加平台促销活动，且促销价格与卖家实际支付金额之间存在差异时进行的调整。 |
| Platform compensation（平台补偿） | 因卖家成功申诉客户争议而向卖家支付的补偿。 |
| Platform penalty（平台罚款） | 在确认违反平台政策后，我们已根据政策从您的账户中扣除了相应的罚款金额。请参阅发送给您的邮件通知。 |
| Sample shipping fee（样品运费） | 使用平台物流服务商寄送样品时收取的费用。 |
| Logistics reimbursement（物流赔偿） | 您的订单因物流问题丢失或损坏。我们对此问题深表歉意，并已为该订单提供了赔偿。 <br/> 平台已核实退货或退款订单 ID，且该订单的退货/退款申请已获批准。由于此退款原因非卖家责任，TikTok 已向客户支付退款金额。 <br/> TikTok Shop 因物流相关问题造成的损失支付的赔偿金 |
| Platform reimbursement（平台赔偿） | 平台无退货退款：订单已按 TikTok 无退货退款政策处理。由于买家对订单问题负有责任，我们已提供赔偿以弥补损失。有关更多详情，请参阅 TikTok 无退货退款政策。  <br/> 平台无退货退款：订单已按 TikTok 无退货退款政策处理。经审核订单后，您可能会获得补贴以弥补您的成本。有关更多详情，请参阅 TikTok 无退货退款政策。  <br/> 平台已核实退货或退款订单 ID，且该订单的退货/退款申请已获批准。由于此退款原因非卖家责任，TikTok 已承担向客户的退款金额。 <br/> TikTok Shop 因客户不满意而支付的补贴 |
| Deductions incurred by seller（卖家扣款） | 用户已为订单提交了"退货退款"申请。根据 TikTok Shop 政策，如果退货或退款是由产品问题或延迟发货引起的，卖家将承担退货运费。 <br/> 订单被发现符合欺诈定义，且存在以下问题之一或类似问题：向客户发送空包裹、发送的商品与商品展示页面不符、发送的商品价值低于宣传价值。卖家负责与此问题相关的费用。 <br/> 根据 TikTok Shop 反假冒政策，订单中的商品被视为假冒商品。卖家负责与此问题相关的费用。 <br/> 订单中的商品被视为存在缺陷并给客户造成了不良体验。根据 TikTok Shop 的政策，卖家负责承担向客户提供的补偿券的费用。 <br/> 当客户因卖家责任的问题而不满意其体验时，卖家负责承担相关费用。 |
| Shipping fee rebate（运费返还） | 作为参与平台活动的一部分而给予卖家的运费返还。 |
| Warehouse service fee（仓储服务费） | 作为仓储服务提供的一部分收取的费用，例如包装服务操作费、包装服务费、条码贴标费、新产品检验服务费等。 |
| Platform commission adjustment（平台佣金调整） | 当卖家支付的平台佣金存在差异时进行的调整。 |
| Platform commission compensation（平台佣金补偿） | 当卖家支付的平台佣金存在差异时向卖家支付的补偿。 |
| Other adjustment（其他调整） | 因其他原因进行的调整。 |

<br/>

## 我在哪里可以在 TikTok Shop 卖家中心查看 API 返回的数据？
| API 名称 | 相关卖家中心页面 |
| --- | --- |
| Get Payments <br/>  | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9c84e160dfca436aaffc3e4535949b64~tplv-k9wyc2ijk0-image.image) <br/>  |
| Get Statements <br/>  | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/21931823181c4c39be3e1f767b3c7c63~tplv-k9wyc2ijk0-image.image) <br/>  |
| Get Statement Transactions | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/06f0d12a6bd547b7bd260f0f951b2b92~tplv-k9wyc2ijk0-image.image) <br/>  |
| Get Order Statement Transactions | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/90f3e31424dd4b1395317d514b580dff~tplv-k9wyc2ijk0-image.image) <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9b820eba88284d59ace5e0d88d4e296d~tplv-k9wyc2ijk0-image.image) <br/>  |

<br/>

## **为什么 API 响应中缺少某个订单？**
尚未结算的订单不会出现在 OpenAPI 响应中。有关订单未结算的更多可能原因，请参阅[常见问题](https://partner.tiktokshop.com/docv2/page/650b1f13c16ffe02b8012c2e#Frequently%20Asked%20Questions)中的问题 1。

