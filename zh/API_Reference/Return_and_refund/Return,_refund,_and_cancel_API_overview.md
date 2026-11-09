# Return, refund, and cancel API 概览

# 背景
Cancel/Return/Refund，也称为"交易后"或"售后"，可以由 buyer 发起或由卖家直接处理。TikTok Shop 为卖家提供两个 API 来处理这些售后情况。Cancel API 允许卖家处理 buyer 的订单取消请求以及卖家直接取消订单。Return API 允许卖家处理 buyer 的订单 refund/return & refund 请求。对于 TikTok Shop 取消/退款订单的情况，请参阅 TikTok Shop 卖家 Academy 了解详情。
<br/>
取消订单：buyer 可以在 buyer remorse 窗口后发起订单取消，或者由卖家直接取消。对于每个取消的订单，都有 buyer/卖家取消原因、取消状态、取消订单创建时间以及卖家处理 buyer 取消请求的时间。在 US 和 UK 市场，TikTok Shop 允许卖家在商品缺货场景下处理部分订单取消。
<br/>
退货订单：退货订单是指 buyer 请求退回或退款一个订单中的一个或多个商品。buyer 在收到商品后可以发起退货。退货订单包含 buyer/卖家退货或退款原因、退货/退款状态、退货或退款请求时间、卖家处理 buyer 退货/退款请求的时间以及退款金额。
<br/>
有两种方式来实现 Search Cancel API 和 Search Return API：

* 订阅 [Cancellation Status Change](https://partner.tiktokshop.com/docv2/page/65030150746462028285f657) 和 [Return Status Change](https://partner.tiktokshop.com/docv2/page/65030162bb2a4d028d50cc51) webhook：您必须订阅 reverse order webhook。更多详情，[点击此处](https://partner.tiktokshop.com/docv2/page/650512b42f024f02be19755f#Back%20To%20Top)。定期轮询 Order List
* 定期轮询 Cancel order/Return order

# 重要概念
**下表说明了根据订单状态何时可以使用"Cancellation"、"Return"和"Refund"。**
|  | **发起方** | **UNPAID** | **ON_HOLD** | **AWAITING_SHIPMENT** | **AWAITING_COLLECTION** | **IN_TRANSIT** | **DELIVERED** | **COMPLETED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Cancel** | Buyer | Y | Y（取消请求由平台自动审批。仅在 UK 可用） | Y <br/>  | N <br/>  | N | N | N |
|  | Seller | N | Y | 取决于市场策略。详情请参见附录卖家 Academy 链接 | Y <br/>  | N | N | N |
| **Refund** | Buyer | N | N | N | Y | 取决于市场策略。详情请参见附录卖家 Academy | Y | N |
|  | Seller | N | N | N | Y |  | 取决于市场策略。详情请参见附录卖家 Academy 链接 | N |
| **Return** | Buyer | N | N | N | N |  | Y | N |
|  | Seller | N | N | N | N |  | 取决于市场策略。详情请参见附录卖家 Academy 链接 | N |

## Cancel/Return/Refund 发起方说明

* BUYER：下单的 buyer。
* SELLER：TikTok Shop 卖家。
* SYSTEM：TikTok Shop 系统可能会根据 TikTok Shop 的策略自动取消订单。例如，如果包裹在运输途中丢失，且 TikTok Shop 检测到 tracking number 超过 7 天未更新，就可能发生这种情况。
* OPERATOR：TikTok Shop 客服也可能因各种原因取消订单。


## Cancel
**订单取消：** 此 API 允许卖家取消已付款订单以及管理订单取消请求。请注意，只有尚未发货的订单才能被取消。
<br/>
注意：Buyer 无法取消多行项目订单中的单个行项目。目前，仅 US 和 UK 卖家允许在商品缺货场景下进行部分取消。
<br/>
**取消类型：** 在 TikTok Shop 平台上，TikTok Shop 有两种类型的订单取消：buyer 发起的取消（即 BUYER_CANCEL）和直接取消（即 CANCEL）。卖家/System/Operator 可以直接取消订单。BUYER_CANCEL 需要卖家审核取消请求。如果订单状态为"ON_HOLD"且 buyer 发起取消，TikTok Shop 将自动代表卖家接受取消请求。卖家无需审核取消请求。在这种情况下，该订单将具有"CANCEL"取消类型。
<br/>
**取消原因：** 请参阅[我们的取消原因列表](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d#Back%20To%20Top)。
<br/>
**取消订单状态：**
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c040e21e9b904bd793949d13349afaba~tplv-k9wyc2ijk0-image.image)

**业务场景：**

* Buyer 发起取消请求

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/75e61ed442ab415e9c1319db3b163d4c~tplv-k9wyc2ijk0-image.image)

> **注意**：如果 buyer 取消请求是在订单日期起 **2 个工作日** Standard Shipping SLA **之前**发起的，卖家必须在 24 小时内采取行动。如果未采取任何操作，TikTok Shop 将自动批准取消并退款。卖家必须通过以下方式之一解决该请求：

>    * 将 tracking number 上传到取消请求中
>    * 批准取消

> 发货或不采取任何其他操作将导致取消被批准。
>
> **注意**：如果取消请求是在订单日期起 **2 个工作日** Standard Shipping SLA **之后**但在订单被标记为 **"In transit"** 之前发起的，TikTok Shop 将自动批准取消并退款。

>    * 有关 SLA 的更多信息，请参阅 [Fulfillment Policy](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3995852763301633&from=policy)。




* 卖家发起取消

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/78c244b9a1c846e0b21c43c1281ef58f~tplv-k9wyc2ijk0-image.image)

## Refund
**退款：** Buyer/卖家可以为行项目发起退款。此 API 允许卖家处理 buyer 退款请求并发放部分或全额退款。
<br/>
注意：目前，不同市场有不同的退款策略。请参阅卖家 Academy 了解更多详情。
<br/>
**退款原因：** 请参阅[我们的退款原因列表](https://partner.tiktokshop.com/docv2/page/67e61e7b8ceb0d04a320061e)。
<br/>
**退款订单状态：**
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/190ddcc2cc9a4a959d482a4a66b750bf~tplv-k9wyc2ijk0-image.image)

退款订单状态说明
| **状态** | **描述** |
| --- | --- |
| RETURN_OR_REFUND_REQUEST_PENDING | Buyer 发起退款请求，需要卖家或平台审批。 |
| REQUEST_SUCCESS | 退款请求成功，buyer 将获得退款。 |
| REQUEST_REJECTED | 卖家拒绝了退款请求。 |
| RETURN_OR_REFUND_CANCEL | 退款请求已被 buyer 或系统取消。 |
| RETURN_OR_REFUND_REQUEST_COMPLETE | 退款请求成功，退款金额已退还。 |

流程 1：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 REQUEST_SUCCESS，然后从 REQUEST_SUCCESS 到 RETURN_OR_REFUND_REQUEST_COMPLETE
触发条件：退款请求已获批准，然后退款金额已退还。
触发发起方：卖家/System
<br/>
流程 2：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 REQUEST_REJECTED
触发条件：退款请求被拒绝。
触发发起方：卖家
<br/>
流程 3：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 RETURN_OR_REFUND_CANCEL
触发条件：buyer 取消退款请求。
触发发起方：Buyer。
<br/>
**业务场景：**

* Buyer 发起退款请求

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e9669f5de4e3454e9992dd61f36362c9~tplv-k9wyc2ijk0-image.image)


* 卖家发起退款

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/76f5c2d1f56241598968628c4c4270e7~tplv-k9wyc2ijk0-image.image)

## Return
**退货：** Buyer 可以发起退货并获得退货订单行项目的退款。此 API 允许卖家接受 buyer 的退货请求以及代表 buyer 发起退货。
<br/>
**退货原因：** [点击此处查看我们的退货原因列表](https://partner.tiktokshop.com/docv2/page/67e61d87fcf2dd04c982ef1d)。
<br/>
**无退货退款：** TikTok Shop 允许卖家更改 buyer 的退货请求并直接发放退款。当卖家通过 Approve Return API 接受退货时，他们可以选择允许 buyer 保留商品并以无退货退款的方式完成退货。当卖家通过 Approve Return API 接受退货时，可以选择 buyer 保留商品选项来实现无退货退款。
<br/>
**退货订单状态**

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1dfbcb33322f47f48074d94b733e0402~tplv-k9wyc2ijk0-image.image)

<br/>

退货订单状态说明
| **状态** | **描述** |
| --- | --- |
| RETURN_OR_REFUND_REQUEST_PENDING | Buyer 发起退货请求，等待卖家审核。 |
| AWAITING_BUYER_SHIP | 退货请求已获批准，等待 buyer 发货。如果 buyer 错过退货截止日期，请求将移至 RETURN_OR_REFUND_CANCEL。 |
| BUYER_SHIPPED_ITEM | Buyer 已发货或上传物流信息。 |
| REQUEST_REJECTED | 卖家拒绝了退货请求。 |
| RECEIVE_REJECTED | 卖家拒绝了 buyer 的退货包裹。 |
| REQUEST_SUCCESS | 退货请求成功，buyer 将获得退款。 |
| RETURN_OR_REFUND_REQUEST_COMPLETE | 退货请求已完成，退款金额已成功支付。 |
| RETURN_OR_REFUND_CANCEL | 退货请求被 buyer 取消，或在截止日期到期后由系统关闭，或卖家有利的结果。 |

**流程 1 :-**
步骤 1：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 AWAITING_BUYER_SHIP
触发条件：卖家或平台批准退货请求。
触发发起方：卖家/System
<br/>
步骤 2：状态从 AWAITING_BUYER_SHIP 到 BUYER_SHIPPED_ITEM
场景 A（buyer 使用平台 shipping 退货）
触发条件：buyer 已寄出退货包裹且包裹被承运商揽收。
触发发起方：System
<br/>
场景 B（buyer 使用自行安排的 shipping 退货）
触发条件：buyer 上传 tracking number
触发发起方：Buyer
<br/>
步骤 3：状态从 BUYER_SHIPPED_ITEM 到 REQUEST_SUCCESS
触发条件：卖家完成退货商品质检并确认退款。
触发发起方：卖家/System
<br/>
步骤 4：状态从 REQUEST_SUCCESS 到 RETURN_OR_REFUND_REQUEST_COMPLETE
触发条件：退货退款成功
触发发起方：System
<br/>
**流程 2a :-**
步骤 1：状态从 BUYER_SHIPPED_ITEM 到 RECEIVE_REJECTED
触发条件：卖家检查退货商品后，拒绝为退货退款。
触发发起方：卖家
<br/>
步骤 2：状态从 RECEIVE_REJECTED 到 REQUEST_SUCCESS
触发条件：buyer 向平台提交仲裁请求，平台批准 buyer 的退货请求。
触发发起方：System
<br/>
**流程 2b :-**
步骤 1：状态从 BUYER_SHIPPED_ITEM 到 RECEIVE_REJECTED
触发条件：卖家检查退货商品后，拒绝为退货退款。
触发发起方：卖家
<br/>
步骤 2：状态从 RECEIVE_REJECTED 到 RETURN_OR_REFUND_CANCEL
触发条件：buyer 的退货请求被拒绝后，在给定时间内未提出仲裁，或仲裁结果有利于卖家。
触发发起方：System
<br/>
**流程 3a :-**
步骤 1：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 REQUEST_REJECTED
触发条件：卖家拒绝 buyer 的退货请求。
触发发起方：卖家
<br/>
步骤 2：状态从 REQUEST_REJECTED 到 AWAITING_BUYER_SHIP
触发条件：buyer 向平台提交仲裁请求，平台批准 buyer 的退货请求。
触发发起方：System
<br/>
**流程 3b :-**
步骤 1：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 REQUEST_REJECTED
触发条件：卖家拒绝 buyer 的退货请求。
触发发起方：卖家
<br/>
步骤 2：状态从 REQUEST_REJECTED 到 RETURN_OR_REFUND_CANCEL
触发条件：buyer 的退货请求被拒绝后，在给定时间内未提出仲裁，或仲裁结果有利于卖家。
触发发起方：System
<br/>
**流程 4 :-**
步骤 1：状态从 RETURN_OR_REFUND_REQUEST_PENDING 到 RETURN_OR_REFUND_CANCEL
触发条件：请求已被 buyer 取消。
触发发起方：Buyer
<br/>
**业务场景：**

* Buyer 发起退货请求

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/53f8bdc473654e42bb3fe7234cc1256f~tplv-k9wyc2ijk0-image.image)


* 卖家发起退货

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1e501178d5724395ad1e5b2071e6c1ca~tplv-k9wyc2ijk0-image.image)

## **批量退货：**
**背景：** 批量退货是退货的一个子场景，buyer 在 TikTok App 中订购多个 SKU 并提交一个退货请求。buyer 期望一次退货旅程和一个 shipping label/QR，而下游卖家系统通常期望一个 RMA 包含所有预期的行项目。
旧行为可以将唯一的 `sku_id` 值解耦为单独的 `return_id` / RMA 记录。这破坏了需要统一记录的退货平台、OMS、WMS 和仓库操作。
| 对象 | 用途 | 关键卖家操作 | 关键标识符 |
| --- | --- | --- | --- |
| Aftersales Request | 面向 buyer 的请求对象，将一次批量退货中所有请求的 SKU 和数量分组。 | 在行项目级别进行首次审核。 | `aftersales_request_id` |
| RMA（包裹级退货订单） | 包裹拆分后从已批准商品创建的物流可执行对象。 | 上传 shipping 信息并完成每个包裹的二次审核。 | `rma_id` |

**业务流程：**

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/72e796505b754081b8438811e3acf62e~tplv-k9wyc2ijk0-image.image)

**业务场景：**

* Buyer 发起退货请求

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f7069924fdcc4e169d55daa748b072c5~tplv-k9wyc2ijk0-image.image)
**新 Webhook：**
| Webhook | 示例状态 | 用途 |
| --- | --- | --- |
| `AFTERSALES_REQUEST_STATUS_UPDATE` | `PENDING_REQUEST_REVIEW`, `REQUEST_REVIEW_COMPLETED` | 通知请求级生命周期和首次审核完成 |
| `RMA_STATUS_UPDATE` | `RMA_CREATED` | 通知统一 RMA 创建，用于二次审核/仓库工作流 |
| `REFUND_SUCCESS` | `REFUND_SUCCESS` | 通知给定 SKU 的退款成功。 |
#### 新增/关键 API 接口
| API | 角色 | 备注 |
| --- | --- | --- |
| `/return_refund/{api_version}/aftersales/search` | 搜索 Aftersales Request | 使用 `aftersales_request_id` 检索统一请求 |
| `/return_refund/{api_version}/rma/search` | 搜索 RMA 请求 | 检索包含行级退货详情的统一 RMA |
| `/return_refund/{api_version}/aftersales/review` | 审核 Aftersales / RMA | 支持 `request_id_type = AFTERSALES` 和 `request_id_type = RMA` |
| 搜索售后请求 API | 首次审核数据获取 | 暴露统一请求的所有退货行项目 ID |
| 搜索 RMA 请求 API | 二次审核数据获取 | 在 `RMA_CREATED` 后用于同步 OMS/WMS |
| 上传配送单据 API | Label / QR 上传 | 由 ISV/退货平台使用，当 TikTok 需要向 buyer 展示 label/QR 时 |
#### 审核决策模型
| 审核阶段 | `request_id_type` | 示例决策 |
| --- | --- | --- |
| 首次审核 | `AFTERSALES` | 批准或拒绝退货请求 |
| 二次审核 | `RMA` | `APPROVE_RETURN_PACKAGE`、`REJECT_RETURN_PACKAGE` 或混合行级决策 |

行级决策是一项重大改进：卖家可以根据仓库分级批准部分退货行项目并拒绝其他行项目。ARD 记录了同 SKU 拆分决策的 MVP 限制；第二阶段将扩展支持。
## Replacement（换货）
**换货订单状态**

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/12b46ab08d524988a0d7da025076d7b5~tplv-k9wyc2ijk0-image.image)
| **状态** | **描述** |
| --- | --- |
| REPLACEMENT_REQUEST_PENDING | Buyer 已发起换货请求。请求等待卖家审核。卖家有 24 小时响应请求。 |
| REPLACEMENT_REQUEST_REJECT | 卖家拒绝 buyer 的换货请求。 |
| REPLACEMENT_REQUEST_REFUND_SUCCESS | 由于库存不足，buyer 的换货请求已通过退款解决。 |
| REPLACEMENT_REQUEST_CANCEL | Buyer 取消了换货请求。 |
| REPLACEMENT_REQUEST_COMPLETE | 卖家已批准 buyer 的换货请求。平台将生成新订单供卖家履行。 |

功能简介：换货由 buyer 发起。卖家可以拒绝/接受/退款 buyer 的请求。如果卖家/system 接受 buyer 的请求，TikTok Shop 将生成新订单供卖家重新发货。如果卖家没有足够的换货库存或无法发送换货商品，他们可以直接退款给 buyer。

从 [Item Replacement for Orders](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3253210454181634&from=policy&anchor_link=EB7800D0) 了解更多关于换货策略的信息。

案例 1：状态从 REPLACEMENT_REQUEST_PENDING 变为 REPLACEMENT_REQUEST_REJECT
触发条件：卖家收到 buyer 换货请求并拒绝了 buyer 的换货请求。请注意，如果卖家拒绝 buyer 的换货请求，buyer 可以发起争议。
触发发起方：卖家

案例 2：状态从 REPLACEMENT_REQUEST_PENDING 变为 REPLACEMENT_REQUEST_COMPLETE
触发条件：卖家或系统自动接受换货请求。请注意，如果卖家/system 接受 buyer 的换货请求，TikTok Shop 平台将自动生成新订单供卖家履行。对于为换货生成的新订单，卖家应遵循与正常订单相同的履行策略。
触发发起方：卖家/System

案例 3：状态从 REPLACEMENT_REQUEST_PENDING 变为 REPLACEMENT_REQUEST_REFUND_SUCCESS
触发条件：卖家直接退款给 buyer。
触发发起方：卖家

案例 4：状态从 REPLACEMENT_REQUEST_REJECT 变为 REPLACEMENT_REQUEST_COMPLETE
触发条件：当 buyer 发起争议且 TikTok Shop 做出卖家应为 buyer 执行换货请求的解决方案时，TikTok Shop 将发起新订单供卖家履行。请注意，对于为换货生成的新订单，卖家应遵循与正常订单相同的履行策略。

**业务场景**
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/97d72133b18b49cda4d3e25426fad903~tplv-k9wyc2ijk0-image.image)


# TikTok Shop Marketplace 策略
## 响应 Buyer 请求的策略

* 以下取消/退货/退款请求的审批节点需要卖家操作，卖家必须在 48 小时内响应请求。如果 48 小时内没有响应，TikTok Shop 将自动批准相应请求。
   * Cancel
      * 当 buyer 发起取消请求成功后，卖家应在 48 小时内响应请求。
   * Refund
      * 当 buyer 发起退款请求成功后，卖家应在 48 小时内响应请求。
   * Return
      * 当 buyer 发起退货请求成功后，卖家应在 48 小时内响应请求。
      * 如果卖家接受 buyer 的退货请求，buyer 将寄回商品。退货包裹送达后，卖家必须在 48 小时内响应退货请求。


## 取消/退货/退款发起策略
**发起取消的策略**
Buyer

* Buyer 可以自由取消未付款订单。

<br/>
对于 UK，TikTok Shop 使用 ON_HOLD 状态来定义处于 buyer remorse 窗口内的订单。如果 buyer 在订单处于 ON_HOLD 状态时请求取消订单，TikTok Shop 将自动代表卖家接受 buyer 的取消请求。对于 UK 以外的地区，buyer remorse 窗口从订单变为 AWAITING_SHIPMENT 状态 +1 小时开始。如果卖家已履行订单，buyer 将无法再请求取消。
<br/>

* 超出 buyer remorse 窗口的订单

一旦订单超出 buyer remorse 窗口，取消必须由卖家审核。如果订单状态变为 AWAITING_COLLECTION，buyer 将无法再请求取消。
<br/>
Seller

* 卖家不能取消未付款订单。
* 卖家可以取消具有以下状态的订单：'ON_HOLD'、'AWAITING_SHIPMENT' 和 'AWAITING_COLLECTION'。

<br/>
更多详情请参阅卖家 Academy。

**发起退款的策略**

* 当订单状态为 'AWAITING_COLLECTION'、'IN_TRANSIT' 和 'DELIVERED' 时，Buyer 可以发起退款请求
* 当订单状态为 'DELIVERED' 时，卖家可以发起退款请求

<br/>
更多详情请参阅卖家 Academy。

**发起退货的策略**

* 当订单状态为 'DELIVERED' 时，Buyer 可以发起退货请求
* 在 US，当订单状态为 'IN_TRANSIT' 和 'DELIVERED' 时，卖家可以发起退款请求。在其他市场，卖家不允许代表 buyer 发起退货。

<br/>
更多详情请参阅卖家 Academy。


# 常见问题

* 卖家可以向 buyer 发放部分退款吗？
   * 不同市场有不同的策略。详情请参阅卖家 Academy。

<br/>

* 取消和退款之间有什么区别？
   * 取消请求可以由 buyer 在卖家发货之前发起。一旦订单已发货，buyer 将无法再取消订单。如果包裹仍在配送中且 buyer 坚持取消订单，卖家应要求 buyer 发起退款请求。

<br/>

* 如果卖家发起退款，是否需要额外的审批？
   * 不需要。TikTok Shop 将自动退款给 buyer。


# 附录
卖家 Academy 取消/退款/退货 TikTok Shop 策略
US：

* https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3253210454181634&from=policy

GB：

* 取消：https://seller-uk.tiktok.com/university/essay?identity=1&role=1&knowledge_id=7753822474782466&from=policy
* 退款和退货：https://seller-uk.tiktok.com/university/essay?identity=1&role=1&knowledge_id=7753847099623170&from=policy

ID：

* https://seller-id.tiktok.com/university/essay?identity=1&role=1&knowledge_id=6837727601690370&from=policy

TH：

* https://seller-th.tiktok.com/university/essay?identity=1&role=1&knowledge_id=6837799362217730&from=policy

MY：

* https://seller-my.tiktok.com/university/essay?identity=1&role=1&knowledge_id=7753775054259970&from=policy

VN：

* https://seller-vn.tiktok.com/university/essay?identity=1&role=1&knowledge_id=6837773789234946&from=policy

PH：

* https://seller-ph.tiktok.com/university/essay?identity=1&role=1&knowledge_id=7654203686340353&from=policy

SG：

* https://seller-sg.tiktok.com/university/essay?identity=1&role=1&knowledge_id=7654182014830338&from=policy



