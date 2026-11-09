# TikTok 退货模式与换货 API 解决方案指南

# **售后交易概述**
退货/退款、取消和换货是可由买家或卖家发起的售后操作。TikTok Shop 为卖家提供 API 权限范围，以编程方式处理这些情况：

* **Cancel API**：支持买家发起的取消请求和卖家发起的订单取消。
* **Return API**：支持买家发起的退款或退货退款请求。


**取消订单**
订单可由买家要求或卖家直接取消。每个取消的订单都包含取消原因、状态、创建时间和卖家处理时间。在美国和英国，卖家还可以在商品缺货时部分取消订单。
**退货订单**
退货订单发生在买家在收货后对一个或多个商品申请退货或仅退款时。每个退货订单都包含退货/退款原因、状态、请求时间、卖家处理时间和退款金额。

**本文档将重点介绍退货交易**、退货标签模式的细节，以及基于不同退货模式使用 TikTok Shop 开放 API 开发端到端解决方案的指导。
--
如需了解所有 TikTok Shop 售后流程的更**全面**概述，请参阅以下文档：

* [Return, refund, and cancel API overview](https://partner.tiktokshop.com/docv2/page/return-refund-and-cancel-api-overview)
* [Return reasons](https://partner.tiktokshop.com/docv2/page/return-reasons)
* [Refund reasons](https://partner.tiktokshop.com/docv2/page/refund-reasons)
* [Cancel reasons](https://partner.tiktokshop.com/docv2/page/cancel-reasons)




# **售后阶段**
在深入了解详细的 API 序列之前，了解 TikTok Shop 中售后/退货记录的**阶段**非常重要。TikTok Shop 会在不同的退货阶段衡量卖家的操作，以确保买家沟通/体验符合我们的 SLA/政策。**注意**：这些被衡量的**阶段**与 API/webhook 中公开的细粒度退货**状态** *不同*。
| **阶段** | **发生事项** | **卖家操作** | **SLA / 截止时间** | **结果 / 备注** |
| --- | --- | --- | --- | --- |
| **第一次审核阶段：**  <br/> 退货请求 | 买家提交退货请求。TikTok 现在会根据商品品类自动批准 **95%** 的请求。一旦批准，TikTok 将生成官方 **RMA_ID**，供卖家/ISV 获取退货及相关行项目。  | 对于仍需审核的约 5% 的请求，卖家必须通过 API 或 Seller Center **批准或拒绝**该**请求**。 <br/>  | 自请求提交起 **24 小时** | 如果在 24 小时内未做出决定，TikTok 将**自动批准**请求并生成退货运输标签。某些请求可能因品类限制或买家可疑退货行为而需要审核。 |
| **第二次审核阶段：**  <br/> 退货决定 | 退货包裹收到并检查后，卖家审核退款决定。 | 卖家必须根据其商品检查 SOP 或自动化规则**批准或拒绝退货**。 | 退货包裹物流显示 `DELIVERED` 后 **4 个工作日**  | 如果在 4 个工作日内未做出决定，TikTok 将**自动批准**退货，买家将获得与原始支付相关的退款。 |

对于所有退货交易，TikTok Shop API/webhook 会公开必要的退货状态更新和物流信号，使卖家能够识别在退货生命周期中需要执行的下一步操作。


# **按状态划分的退货操作**
在退货生命周期中，买家或卖家可以执行特定操作，具体取决于 `order_id` 状态以及 `return_id` 状态。

以下表格说明了基于当前订单状态何时可以**发起**退货。
|  | **发起方** | **`UNPAID`** | **`ON_HOLD`** | **`AWAITING_SHIPMENT`** | **`AWAITING_COLLECTION`** | **`IN_TRANSIT`** | **`DELIVERED`** | **`Completed`** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **退货** <br/> **发起** | 买家 | 否 | 否 | 否 | 否 | **是** | **是** | 否 |
|  | 卖家 | 否 <br/>  | 否 | 否 | 否 <br/>  | 否 <br/>  | 取决于市场政策。美国允许卖家创建离线退货记录，但必须自动批准退款金额给买家。 | 否 |

以下表格说明了基于当前退货状态，卖家或买家可以对退货执行哪些操作。
| **退货状态** | **请求类型 / ID** | **描述** | **卖家操作** | **买家操作** |
| --- | --- | --- | --- | --- |
| `RETURN_OR_REFUND_REQUEST_PENDING` <br/>  | 售后 <br/>  | 买家发起退货请求，创建售后请求 ID。虽然 TikTok 自动批准 95% 的请求，但仍有部分记录待卖家审核。 | 批准或拒绝请求 |  |
| `AWAITING_BUYER_RETURN` <br/>  | RMA  | 售后退货请求已批准，官方 RMA `id` 已创建。等待买家寄回商品。 | - <br/>  | 将商品寄回给卖家 |
| `RETURN_IN_TRANSIT` | RMA | 买家已寄出商品，物流追踪确认退货在途中。 | 如有需要，卖家可以在退货到达其仓库之前批准退款。  | - |
| `PENDING_PACKAGE_REVIEW` | RMA | 物流确认退货包裹已 `DELIVERED`。 | 检查/评估商品并决定批准或拒绝退货行项目的退款。 | - |
| `PACKAGE_REVIEW_COMPLETED` | RMA | 退货包裹已完成检查并做出最终退款决定。  | 如果结果未达成一致，买家和 TT 客服进行仲裁。 | 如果结果未达成一致，买家和 TT 客服进行仲裁。 |



# **退货标签模式**
TikTok 有 **2 种退货标签模式** —— API 集成路径将由哪种模式更适合卖家的具体运营/系统架构来决定。一旦卖家选择了其系统所需的退货标签模式，他们就可以使用 TikTok 的开放 API 为这两种退货模式构建完整的退货管理集成。
| **退货模式** | **描述** |
| --- | --- |
| ###  **4PL 模式：** <br/> **TikTok 退货标签** <br/>  | TikTok 负责使用我们自己的 TikTok 物流账户生成退货运输标签。 <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/d10e9007db6147e1b81876a7a9db4d82~tplv-k9wyc2ijk0-image.image) <br/>  |
| ###  **3PL 模式：** <br/> **外部退货标签** <br/>  | 卖家/外部退货平台负责生成退货运输标签，**并且**还负责通过我们的开放 API 将该运输标签**上传**到 TikTok。  <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/10ffa64b8edf488ea2f1ab1fa6c784c0~tplv-k9wyc2ijk0-image.image) <br/>  <br/>  <br/> ***注意***：TikTok Shop 对 3PL 标签的定义是指这是第三方物流***标签***，*不一定来自第三方物流履约服务商。3PL 标签可以来自卖家自己的 UPS/USPS/FedEx 账户，也可以由退货平台生成，例如：***Loop Returns***、***Happy Returns*** 等。 <br/>  <br/> *这种生成并上传第三方退货运输标签的功能在 TikTok 生态系统中通常被称为 **V2 退货**。* <br/>  |


# **4PL 模式：TikTok 退货标签**
TikTok Shop 的标准退货行为是为买家使用 TikTok 的退货运输标签。总体而言，卖家可以使用我们的开放 API 构建端到端的退货管理集成，使其能够：

1. 获取新的退货/RMA 详情
2. 将退货/RMA 详情提交到其退货仓库系统（WMS/DB）
3. 买家使用 TikTok 运输标签将退货包裹寄送到卖家的退货仓库
4. 仓库运营识别退货包裹，检查并评估商品
5. 根据仓库评估结果，向 TikTok 发送批准或拒绝退货退款的决定。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4af84bdf9ebf4bbaa50a6e0a1251b28f~tplv-k9wyc2ijk0-image.image)


> ### **4PL 模式 API 文档**


退货 API 和 webhook 文档如下：

* [Aftersales Request Status Update Webhook](https://partner.tiktokshop.com/docv2/page/h4cxaxub)
* [Search Aftersales Request API](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603)
* [RMA Status Update Webhook](https://partner.tiktokshop.com/docv2/page/2f0jrrxc)
* [Search Return Merchandise Authorization (RMA) API](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604)
* [Review Aftersales API](https://partner.tiktokshop.com/docv2/page/review-aftersales-202603)
* [Refund Success Webhook](https://partner.tiktokshop.com/docv2/page/8y10pibm)


> ### **4PL 解决方案架构与实施**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3bb8248cfccb4af9a5baebfce08b79ed~tplv-k9wyc2ijk0-image.image)


| # **售后** <br/> # **阶段** | # **步骤** | # **系统** | # **需求详情** |
| --- | --- | --- | --- |
| ### 买家发起退货并开始（第一次审核阶段） |  |  |  |
| **第一次审核** <br/>  <br/>   <br/>  <br/>   <br/>   <br/>   <br/>  | **[1]** 买家提交退货请求 <br/>  | **TikTok**  <br/>  | 买家在 TT 应用中选择了退货方式并提交退货请求。 |
|  | **[2]** Webhook：`AFTERSALES_REQUEST_STATUS_UPDATE` <br/> Webhook 主题：**64** <br/>  | **TikTok** <br/>  | TikTok 触发 webhook topic：**Aftersales Request Status Update** <br/> "aftersales_request_status" : `PENDING_REQUEST_REVIEW` <br/> [Webhook topic 64 文档](https://partner.tiktokshop.com/docv2/page/h4cxaxub) <br/>  |
|  | **[3]** 搜索售后请求 API | **卖家/ISV** <br/>  | 使用 webhook 中提供的 aftersales_request_id 作为调用 "Search Aftersales Request API" 时的搜索参数。响应将公开与此统一售后请求关联的所有 return_line_item_id <br/> [Search Aftersales Request API 文档](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603) <br/>  |
|  | **[4]** 将售后请求同步到卖家 OMS <br/>  | **卖家/ISV** | 售后请求详情同步到卖家的 OMS/UI/工作台等进行审核  |
|  | **[5]** 决定批准或拒绝**请求** <br/>  | **卖家/ISV** | 卖家决定是否**批准**或**拒绝**退货**请求**。这被视为第一次审核决策步骤。  <br/> > **注意**：对于大多数卖家，此第一次审核步骤会根据退货请求中商品的品类**自动**批准。对于任何自动批准的售后请求，卖家无需执行请求批准操作，但在退货包裹显示仓库送达扫描后，仍必须在我们的 48 小时政策 SLA 内执行退款决策。  |
|  | **[6]** 审核售后 API | **卖家/ISV** | 使用此 API 决定是否**批准**或**拒绝**退货请求。指定 **request_id_type**：**`AFTERSALES`** <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
|  | **[7]** Webhook：`AFTERSALES_REQUEST_STATUS_UPDATE` | **TikTok** | **Webhook：AFTERSALES_REQUEST_STATUS_UPDATE** <br/> status: `REQUEST_REVIEW_COMPLETED` <br/> [Webhook topic 64 文档](https://partner.tiktokshop.com/docv2/page/h4cxaxub) |
| ### 第一次审核流程完成后，官方 RMA 工作流将开始（第二次审核阶段） |  |  |  |
| **第二次审核** <br/>  | **[8]** TikTok RMA 创建  | **TikTok** <br/>  | 售后请求批准后，TikTok 将立即创建 RMA，这是一个统一的退货标识符，涵盖与买家退货提交关联的所有唯一 SKU 行和数量 |
|  | **[9]** Webhook：`RMA_STATUS_UPDATE` <br/> Webhook 主题：**65** | **TikTok** <br/>  | **Webhook：RMA_STATUS_UPDATE** <br/> **status**：**`RMA_CREATED`** <br/> 一旦官方 TikTok RMA 在 TikTok 系统中创建，此 webhook 将触发 <br/> [Webhook topic 65 文档](https://partner.tiktokshop.com/docv2/page/2f0jrrxc) |
|  | **[10]** 搜索 RMA 请求 API | **卖家/ISV** | 调用此 API 获取退货的完整详情，包括所有嵌套的退货订单和行级商品详情。  <br/> [Search Return Merchandise Authorization API 文档](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604) <br/>  |
|  | **[11]** 同步退货 RMA  | **卖家/ISV** | 将退货 RMA 详情同步到 OMS 和 WMS 层，确保 RMA 记录在数据库中，以便仓库在收到时识别。 |
|  | **[12A] 和 [12B]** 买家寄出/投递商品 | **TTS 买家** | 买家将商品送到最近的物流投递点或将商品寄送到仓库 |
|  | **[13]** 仓库运营收到 RMA 包裹 | **仓库运营** | 仓库运营接收并识别 RMA 包裹，与 WMS 中的 RMA 记录进行匹配处理。  |
|  | **[14]** 仓库运营检查 | **仓库运营** | 仓库运营对 RMA 退货行项目执行评估/检查 SOP |
| ### 第二次审核检查结果有 4 种可能路径（A、B、C、D） |  |  |  |
| ### **路径 A：** 所有预期商品已收到并接受，全额退款 |  |  |  |
| **路径 A** <br/>  | **[15.A]** WMS 更新 OMS | **WMS** <br/>  | 仓库人员检查商品并更新 RMA 状态，确认与 RMA 关联的所有行项目均处于"良好"状态 <br/>  |
| **路径 A** <br/>  | **[16.A]** OMS 更新 TikTok 应用 | **OMS** <br/>  | 根据仓库商品评估结果所有商品状态良好，OMS 更新退货应用，确认所有商品符合全额退款条件。 <br/>  |
| **路径 A** | **[17.A]** 审核售后 API <br/>  | **ISV** | 触发 RMA 中所有 return_line_item_id 的退款。 <br/> request_id_type: `RMA` <br/> action: `APPROVE_RETURN_PACKAGE` <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 A** | **[18.A]** 退款给买家  | **TikTok** | 买家退款支付完成 |
| ### **路径 B：** 部分商品不符合仓库评估验收标准（部分商品缺失/损坏）。 |  |  |  |
| **路径 B** <br/>  | **[15.B]** WMS RMA 状态 = 部分商品评估为"损坏/缺失" <br/>  | **WMS** | 仓库人员检查商品并更新 RMA 状态，与 RMA 关联的部分行项目处于"良好"状态，部分为"损坏/缺失" |
| **路径 B** <br/>  | **[16.B]** 使用混合退款决定指示 TTS 应用（所有行） | **OMS** | 根据仓库商品评估结果，部分行项目处于"良好"状态，部分为"损坏/缺失"，使用基于行项目的部分退款更新退货平台 RMA。 |
| **路径 B** | **[17.B]** 审核售后 API <br/> <br/>  | **卖家/ISV** <br/>  | 触发已批准行项目的退款并拒绝缺失/损坏的行项目。使用 "Review Aftersales API" 时，您可以为不同的 return_line_item_id 定义不同的决策/操作枚举。示例： <br/> return_line_item_id: 111 = 良好状态。 <br/> action: `APPROVE_RETURN_PACKAGE` <br/> - <br/> return_line_item_id: 222 = 损坏/缺失 <br/> Action: `REJECT_RETURN_PACKAGE`  <br/>  <br/> > **注意**：TTS **不允许**同一 sku_id 具有**不同**的决策（已知平台限制）。卖家必须对同一 sku_id 的多个数量执行相同的操作/决策。我们将在 2026 年第三季度末解决此平台问题，允许真正灵活的 return_line_item_id 决策，不受 sku_id 配置的限制。 <br/>  <br/>  <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 B** | **[18.B]** 按 SKU 行混合退款 <br/>  | **TikTok** | 根据不同的 sku_id 决策完成买家的部分退款支付。  |
| ### **路径 C：** 所有商品不符合仓库评估验收标准（缺失/损坏）。  |  |  |  |
| **路径 C** | **[15.C]** OMS RMA 状态 = 所有商品评估为"损坏/缺失" | **WMS** | 仓库人员检查商品并更新 RMA 状态，与 RMA 关联的所有行项目均为"损坏/缺失" |
| **路径 C** | **[16.C]** 指示 TTS 应用拒绝 RMA（所有行） <br/>  | **OMS** | 根据仓库商品评估结果所有行项目均为"损坏/缺失"状态，更新退货平台 RMA 以拒绝所有行项目的退款 |
| **路径 C** | **[17.C]** 审核售后 API | **卖家/ISV** | 触发拒绝 RMA 中所有行项目的退款 <br/> request_id_type: `RMA` <br/> action: `REJECT_RETURN_PACKAGE` <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 C** | **[18.C]** 退货退款被拒绝（所有行） | **TikTok** | 所有退货商品的退款被拒绝，通知已发送给买家 |
| ### **路径 D：** 同一 sku_id 的部分数量不符合仓库评估验收标准（缺失/损坏）。提供部分退款 |  |  |  |
| **路径 D** | **[15.D]** OMS RMA 状态 = 同一 SKU / 多个数量具有不同状态。 <br/>  | **WMS** | RMA 包含完全相同 SKU 的多个数量（SKU:A x 2 件）。仓库人员检查包裹/商品后发现： <br/>  第 1 件状态良好 <br/>  第 2 件完全损坏或完全缺失。  |
| **路径 D** | **[16.D] 指示 TTS 应用** `OFFER_PARTIAL_REFUND` <br/>  | **OMS** | 根据仓库商品评估结果，1 件应退款，1 件因损坏应拒绝。然而，如前所述，TikTok Shop 平台存在一个已知限制，即不允许对同一 sku_id 的多个数量做出不同的退款决策。为解决此平台行为，OMS 必须执行计算，为每个数量/行触发部分退款金额，以等于买家应收到的总金额。示例：  <br/> 买家订购了 SKU:A x 2 件。每件商品原始支付价格 = $10.00 <br/> 第 1 件收到时状态为"良好/可售" <br/> 第 2 件损坏或缺失。 <br/> - <br/> 卖家希望**批准**第 1 件并**拒绝**第 2 件，使买家仅获得两行原始支付 $20.00 中的 **$10.00** 退款。但 TTS 平台/API 不允许对同一 SKU 做出不同决策（已知平台行为/限制）。  <br/>  <br/> 卖家可以使用 Review Aftersales API 并为两行使用 `OFFER_PARTIAL_REFUND` 枚举。但 OMS 逻辑**必须**使用以下公式计算金额： <br/>（退款总金额）/（return_line_item_id 总数） <br/> 以上示例： <br/> $10.00（退款总金额）/（2 个退货行）= $5.00 <br/> `OFFER_PARTIAL_REFUND` 金额将为同一 SKU 的**两行**都设为 `5.00`，以确保买家获得 $10.00 的退款金额。 <br/>  |
|  **路径 D** | **[17.D]** 审核售后 API <br/> request_id_type: `RMA` <br/> action: `OFFER_PARTIAL_REFUND` | **卖家/ISV** | 触发同一 SKU 所有行项目的 `OFFER_PARTIAL_REFUND` 操作 <br/> request_id_type: `RMA` <br/> action: `OFFER_PARTIAL_REFUND` <br/> - <br/> 在 alternative_solutions_details 对象中： <br/> 定义 `partial_refund_amount` 和 `currency` <br/>  <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 D** | **[18.D]** 买家收到准确的部分金额退款 | **TikTok** | 部分退款金额和通知已发送给买家 |
| **路径 D** |  |  | **买家安抚使用场景** <br/> `OFFER_PARTIAL_REFUND` 也可用作安抚机制。例如 <br/> **如果**：买家本应只寄回 SKU A 第 1 件，但商品有轻微损坏、明显磨损、包装轻微损坏等 <br/> **则**：卖家可以决定对该单个 return_line_item_id 执行 `OFFER_PARTIAL_REFUND`，TikTok 将按卖家指定的金额退款给该买家。  |




# **3PL 模式：外部退货标签**
***也称为：V2 退货***
3PL 标签模式**最常见**的使用场景是卖家希望将其现有的 DTC 退货平台与 TikTok 退货活动结合使用。通常，卖家的 DTC 流程会利用**退货平台**负责为买家**生成运输标签**，并**协调数据流**以及退货平台与其自有 DTC/OMS/WMS 层之间的运营功能。

通过将这些**现有的**退货平台工作流用于 TikTok Shop 退货，卖家可以**减少工程工作和成本**，并在其 DTC 和 TikTok Shop 退货之间保持**一致的**端到端流程。此外，一些卖家通过这些退货平台在退货运输标签上渲染自定义属性/条形码。这些标签属性是其仓库 SOP 的一部分，用于在仓库设施收到退货包裹时扫描和识别。

### 已与 TikTok 合作构建 3PL 标签/二维码模式的退货平台：

* Loop Returns
* Happy Returns
* Amazon MCF
* Redo Returns
* Narvar（范围确定中）


总体而言，这些现有的退货平台集成遵循以下模型

1. 获取新的退货/RMA 详情
2. 生成第三方退货运输标签（3PL，非 TikTok 平台）
3. 将第三方退货标签上传回 TikTok，以便渲染/通过电子邮件发送给买家
4. 将退货/RMA 详情提交到其退货仓库系统（WMS/DB）
5. 买家使用卖家的 3PL 标签将退货包裹寄送到卖家的退货仓库
6. 仓库运营识别退货包裹，检查并评估商品
7. 根据仓库评估结果，将退货状态发送到 OMS 层，以便退货平台/应用做出退款决策。
8. 退货平台应用向 TikTok 发送批准或拒绝退货退款的决定。


然而，卖家**不必**利用这些现有的退货平台集成。他们也可以**开发自己的 3PL 标签模型**。**** 这本质上允许卖家执行退货平台管理的完全相同步骤，但卖家**使用自己的标签**并在其系统与 TikTok API 之间直接上传。



![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/6f1e289079bf429b9306a3087f211caf~tplv-k9wyc2ijk0-image.image)


> ### **3PL 模式前提条件清单**

每个卖家的店铺需要多个前提配置。卖家必须**在**能够测试标签生成和标签上传流程到 TikTok 应用买家视图之前完成以下清单。
| **清单任务** | **负责人** | **备注** |  |
| --- | --- | --- | --- |
| 定义哪些 **`seller_id`** 需要 3PL 标签功能 | 卖家/TTS | 将沙箱和生产环境的 **`seller_id`** 分享给 TikTok 解决方案 POC 以进行后端配置 | - [ ]  |
| 定义哪个 **`app_key`** 将管理退货 API | 卖家/TTS | 将 **`app_key`** 分享给 TikTok 解决方案 POC 以进行后端配置 | - [ ]  |
| 定义向买家提供的具体承运商退货方式 <br/>  | 卖家/TTS <br/>  | TikTok 需要配置 **`seller_id`**，使其仅在买家 UX 流程中展示卖家预期的退货方式。承运商退货方式因承运商而异：**`USPS`**、**`UPS`**、**`FedEx`**。每个承运商在运输标签与投递二维码的退货方式上也有差异。  | - [ ]  |
| 申请 [Upload Shipping Document API](https://partner.tiktokshop.com/docv2/page/upload-shipping-document-and-tracking-info-202405) 的 API 访问权限 | 卖家/TTS | TTS 解决方案 POC 必须将您的 **`app_key`** 加入白名单以访问此 API 权限范围。 | - [ ]  |
| 申请新的批量退货 API/Webhook 的 API 访问权限 <br/>  | 卖家/TTS | 背景：TikTok 于 2026 年 5 月发布了一组新的退货管理 API/webhook。新 API 遵循 RMA 数据结构的行业标准。有关旧版行为的更多详情以及我们部署新版本的原因，请参阅[此文档](https://bytedance.us.larkoffice.com/docx/JSUAdGU59ol2uexgVeFuvi0ssrc)。  | - [ ]  |
| 创建用于测试的 TikTok 用户账户 <br/>  | 卖家 | 将 TikTok **`user_id`** 分享给 TikTok 解决方案 POC 以标记为"测试"用户，该用户可以访问测试店铺商品以执行订单创建和退货提交，验证 3PL 标签上传是否在 TikTok 应用中正确渲染。  <br/> **获取 TikTok UID 的步骤（插入文档）** | - [ ]  |
| 在您的沙箱 TikTok Shop 账户中创建测试商品 | 卖家  | 将价格设置为 $1.00，因为这将需要实际的信用卡结账 | - [ ]  |
| 使用 TikTok 测试用户账户创建包含测试商品的订单 | 卖家 | 此订单将出现在您的 Partner Center 开发店铺控制台中，您可以将状态强制设为 `DELIVERED`。  | - [ ]  |
完成这些前提条件后，当在 TikTok 应用中针对测试订单发起退货时，预期卖家将协调 webhook 和 API 调用，然后将运输标签上传到 TikTok。

**此测试的成功标准是退货运输标签将直接渲染到 TikTok 用户视图中（如下所示）**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/66ea5f2f2b7840d8a895d62bb84b20b4~tplv-k9wyc2ijk0-image.image)


> ### **3PL 模式 API 文档**

退货 API 和 webhook 文档如下：

* [Aftersales Request Status Update Webhook](https://partner.tiktokshop.com/docv2/page/h4cxaxub)
* [Search Aftersales Request API](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603)
* [RMA Status Update Webhook](https://partner.tiktokshop.com/docv2/page/2f0jrrxc)
* [Search Return Merchandise Authorization (RMA) API](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604)
* [Get External Order Reference API](https://partner.tiktokshop.com/docv2/page/get-external-order-references-202406)（需要 TikTok 启用）**可选使用**
* [Upload Shipping Document API](https://partner.tiktokshop.com/docv2/page/upload-shipping-document-and-tracking-info-202405)（需要 TikTok 启用）
* [Review Aftersales API](https://partner.tiktokshop.com/docv2/page/review-aftersales-202603)
* [Refund Success Webhook](https://partner.tiktokshop.com/docv2/page/8y10pibm)


> ### **3PL 解决方案架构与实施步骤（3PL 模式）**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5a20c6f3f49c48878615866292948fcb~tplv-k9wyc2ijk0-image.image)



| # **售后** <br/> # **阶段** | # **步骤** | # **系统** | # **需求详情** |
| --- | --- | --- | --- |
| ### 买家发起退货并开始（第一次审核阶段） |  |  |  |
| **第一次审核** <br/>  <br/>   <br/>  <br/>   <br/>   <br/>   <br/>  | **[1]** 买家提交退货请求 <br/>  | **TikTok**  <br/>  | 买家在 TT 应用中选择了退货方式并提交退货请求。 |
|  | **[2]** Webhook：`AFTERSALES_REQUEST_STATUS_UPDATE` <br/> Webhook 主题 ID：64 <br/>  | **TikTok** <br/>  | TikTok 触发 webhook topic：**Aftersales Request Status Update** <br/> "aftersales_request_status" : `PENDING_REQUEST_REVIEW` <br/> [Webhook topic 64 文档](https://partner.tiktokshop.com/docv2/page/h4cxaxub) <br/>  |
|  | **[3]** 搜索售后请求 API | **卖家/ISV** <br/>  | 使用 webhook 中提供的 aftersales_request_id 作为调用 "Search Aftersales Request API" 时的搜索参数。响应将公开与此统一售后请求关联的所有 return_line_item_id <br/> [Search Aftersales Request API 文档](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603) <br/>  |
|  | **[4]** 将售后请求同步到卖家 OMS <br/>  | **卖家/ISV** <br/>  | 售后请求详情同步到卖家的 OMS/UI/工作台等进行审核  |
|  | **[5]** 决定批准或拒绝**请求** <br/>  | **卖家** | 卖家决定是否**批准**或**拒绝**退货**请求**。这被视为第一次审核决策步骤。  <br/> > **注意**：对于大多数卖家，此第一次审核步骤会根据退货请求中商品的品类**自动**批准。对于任何自动批准的售后请求，卖家无需执行请求批准操作，但在退货包裹显示仓库送达扫描后，仍必须在我们的 48 小时政策 SLA 内执行退款决策。  <br/>  <br/>  |
|  | **[6]** 审核售后 API | **卖家/ISV** | 使用此 API 决定是否**批准**或**拒绝**退货请求。指定 **request_id_type**：**`AFTERSALES`** <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) |
|  | **[7]** Webhook：`AFTERSALES_REQUEST_STATUS_UPDATE` | **TikTok** | **Webhook：AFTERSALES_REQUEST_STATUS_UPDATE** <br/> status: `REQUEST_REVIEW_COMPLETED` <br/> [Webhook topic 64 文档](https://partner.tiktokshop.com/docv2/page/h4cxaxub) |
| ### 第一次审核流程完成后，官方 RMA 工作流将开始（第二次审核阶段） |  |  |  |
| **第二次审核** <br/>  | **[8]** TikTok RMA 创建  | **TikTok** <br/>  | 售后请求批准后，TikTok 将立即创建 RMA，这是一个统一的退货标识符，涵盖与买家退货提交关联的所有唯一 SKU 行和数量 |
|  | **[9]** Webhook：`RMA_STATUS_UPDATE` <br/> Webhook 主题：**65** <br/>  | **TikTok** | **Webhook：RMA_STATUS_UPDATE** <br/> **status**：**`RMA_CREATED`** <br/> 一旦官方 TikTok RMA 在 TikTok 系统中创建，此 webhook 将触发。 <br/> [Webhook topic 65 文档](https://partner.tiktokshop.com/docv2/page/2f0jrrxc) |
|  | **[10]** 搜索退货授权 API | **卖家/ISV** | 调用此 API 获取退货的完整详情，包括所有退货订单和行级标识符。  <br/> [Search Return Merchandise Authorization API 文档](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604) <br/>  |
|  | **[11]** 获取外部订单参考 API | **卖家/ISV** | 获取卖家的 OMS order_id 以与 TikTok order_id 关联 <br/> [Get External Order References API 文档](https://partner.tiktokshop.com/docv2/page/get-external-order-references-202406) |
|  | **[12.1]** Create Return API / 工作流 | **卖家/ISV** | Create Return API endpoint 将根据用于 RMA 记录/标签/二维码生成的退货平台而有所不同。 |
|  | **[12.2]** 退货标签 / 二维码生成 | **退货平台** | RMA 二维码在响应体中提供 |
|  | **[13]** 上传配送单据 API | **卖家/ISV** | 将标签/二维码文档上传到 TikTok Shop <br/> [Upload Shipping Document API 文档](https://partner.tiktokshop.com/docv2/page/upload-shipping-document-and-tracking-info-202405) |
|  | **[14]** 渲染二维码 + 发送邮件给买家 | **TikTok** | TikTok 应用将在买家应用 UX 中渲染二维码 |
|  | **[15]** 同步退货平台 RMA  | **退货平台** | 退货平台向卖家发送新 RMA 信号（现有集成路径） |
|  | **[16]** 买家寄出/投递商品 | **TTS 买家** | 买家将商品送到最近的物流投递点或将商品寄送到仓库 |
|  | **[17]** 买家寄出信号 | **承运商** | 承运商信号确认退货包裹/商品已寄出/投递 |
| ### 第二次审核检查结果有 4 种可能路径（A、B、C、D） |  |  |  |
| ### **路径 A：** 所有预期商品已收到并接受，全额退款 |  |  |  |
| **路径 A** <br/>  | **[18.A]** WMS 更新 OMS | **WMS** <br/>  | 仓库人员检查商品并更新 RMA 状态，确认与 RMA 关联的所有行项目均处于"良好"状态 <br/>  |
| **路径 A** <br/>  | **[19.A]** OMS 更新 TikTok 应用 | **OMS** <br/>  | 根据仓库商品评估结果所有商品状态良好，OMS 更新退货应用，确认所有商品符合全额退款条件。 <br/>  |
| **路径 A** | **[20.A]** 审核售后 API <br/>  | **卖家/ISV** | 触发 RMA 中所有 return_line_item_id 的退款。 <br/> request_id_type: `RMA` <br/> action: `APPROVE_RETURN_PACKAGE` <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) |
| **路径 A** | **[21.A]** 退款给买家  | **TikTok** | 买家退款支付完成 |
| ### **路径 B：** 部分商品不符合仓库评估验收标准（部分商品缺失/损坏）。 |  |  |  |
| **路径 B** <br/>  | **[18.B]** WMS RMA 状态 = 部分商品评估为"损坏/缺失" <br/>  | **WMS** | 仓库人员检查商品并更新 RMA 状态，与 RMA 关联的部分行项目处于"良好"状态，部分为"损坏/缺失" |
| **路径 B** <br/>  | **[19.B]** 使用混合退款决定指示 TTS 应用（所有行） | **OMS** | 根据仓库商品评估结果，部分行项目处于"良好"状态，部分为"损坏/缺失"，使用基于行项目的部分退款更新退货平台 RMA。 |
| **路径 B** | **[20.B]** 审核售后 API <br/>  | **卖家/ISV** <br/>  | 触发已批准行项目的退款并拒绝缺失/损坏的行项目。使用 "Review Aftersales API" 时，您可以为不同的 return_line_item_id 定义不同的决策/操作枚举。示例： <br/> return_line_item_id: 111 = 良好状态。 <br/> action: `APPROVE_RETURN_PACKAGE` <br/> - <br/> return_line_item_id: 222 = 损坏/缺失 <br/> Action: `REJECT_RETURN_PACKAGE`  <br/>  <br/> > **注意**：TTS **不允许**同一 sku_id 具有**不同**的决策（已知平台限制）。卖家必须对同一 sku_id 的多个数量执行相同的操作/决策。我们将在 2026 年第三季度末解决此平台问题，允许真正灵活的 return_line_item_id 决策，不受 sku_id 配置的限制。 <br/>  <br/>  <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 B** | **[21.B]** 按 SKU 行混合退款 <br/>  | **TikTok** | 根据不同的 sku_id 决策完成买家的部分退款支付。  |
| ### **路径 C：** 所有商品不符合仓库评估验收标准（缺失/损坏）。  |  |  |  |
| **路径 C** | **[18.C]** OMS RMA 状态 = 所有商品评估为"损坏/缺失" | **WMS** | 仓库人员检查商品并更新 RMA 状态，与 RMA 关联的所有行项目均为"损坏/缺失" |
| **路径 C** | **[19.C]** 指示 TTS 应用拒绝 RMA（所有行） <br/>  | **OMS** | 根据仓库商品评估结果所有行项目均为"损坏/缺失"状态，更新退货平台 RMA 以拒绝所有行项目的退款 |
| **路径 C** | **[20.C]** 审核售后 API | **卖家/ISV** | 触发拒绝 RMA 中所有行项目的退款 <br/> request_id_type: `RMA` <br/> action: `REJECT_RETURN_PACKAGE` <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 C** | **[21.C]** 退货退款被拒绝（所有行） | **TikTok** | 所有退货商品的退款被拒绝，通知已发送给买家 |
| ### **路径 D：** 同一 sku_id 的部分数量不符合仓库评估验收标准（缺失/损坏）。提供部分退款 |  |  |  |
| **路径 D** | **[18.D]** OMS RMA 状态 = 同一 SKU / 多个数量具有不同状态。 <br/>  | **WMS** | RMA 包含完全相同 SKU 的多个数量（SKU:A x 2 件）。仓库人员检查包裹/商品后发现： <br/>  第 1 件状态良好 <br/>  第 2 件完全损坏或完全缺失。  |
| **路径 D** | **[19.D] 指示 TTS 应用** `OFFER_PARTIAL_REFUND` <br/>  | **OMS** | 根据仓库商品评估结果，1 件应退款，1 件因损坏应拒绝。然而，如前所述，TikTok Shop 平台存在一个已知限制，即不允许对同一 sku_id 的多个数量做出不同的退款决策。为解决此平台行为，OMS 必须执行计算，为每个数量/行触发部分退款金额，以等于买家应收到的总金额。示例：  <br/> 买家订购了 SKU:A x 2 件。每件商品原始支付价格 = $10.00 <br/> 第 1 件收到时状态为"良好/可售" <br/> 第 2 件损坏或缺失。 <br/> - <br/> 卖家希望**批准**第 1 件并**拒绝**第 2 件，使买家仅获得两行原始支付 $20.00 中的 **$10.00** 退款。但 TTS 平台/API 不允许对同一 SKU 做出不同决策（已知平台行为/限制）。  <br/>  <br/> 卖家可以使用 Review Aftersales API 并为两行使用 `OFFER_PARTIAL_REFUND` 枚举。但 OMS 逻辑**必须**使用以下公式计算金额： <br/>（退款总金额）/（return_line_item_id 总数） <br/> 以上示例： <br/> $10.00（退款总金额）/（2 个退货行）= $5.00 <br/> `OFFER_PARTIAL_REFUND` 金额将为同一 SKU 的**两行**都设为 `5.00`，以确保买家获得 $10.00 的退款金额。 <br/>  |
|  **路径 D** | **[20.D]** 审核售后 API <br/>  | **卖家/ISV** | 触发同一 SKU 所有行项目的 `OFFER_PARTIAL_REFUND` 操作 <br/> request_id_type: `RMA` <br/> action: `OFFER_PARTIAL_REFUND` <br/> - <br/> 在 `alternative_solutions_details` 对象中： <br/> 定义 `partial_refund_amount` 和 `currency` <br/>  <br/> [Review Aftersales API 文档](https://partner.tiktokshop.com/docv2/page/review-aftersales-202606) <br/>  |
| **路径 D** | **[21.D]** 买家收到准确的部分金额退款 | **TikTok** | 部分退款金额和通知已发送给买家 |
| **路径 D** |  |  | **买家安抚使用场景** <br/> `OFFER_PARTIAL_REFUND` 也可用作安抚机制。例如 <br/> **如果**：买家本应只寄回 SKU A 第 1 件，但商品有轻微损坏、明显磨损、包装轻微损坏等 <br/> **则**：卖家可以决定对该单个 return_line_item_id 执行 `OFFER_PARTIAL_REFUND`，TikTok 将按卖家指定的金额退款给该买家。  |




# **换货**
TikTok 买家可以执行换货操作，通过 TikTok 应用内的退货流程发起。这使卖家能够保留 GMV，而不仅仅是为退货商品退款。当买家提交换货请求时，Returns & Orders API 中有 API 字段标识需要换货。
| **市场** <br/>  | * 美国（US） <br/> * 英国（UK） |
| --- | --- |
| **Returns API** | **参数更新** |
| --- | --- |
| [Search Returns API](https://partner.tiktokshop.com/docv2/page/search-returns-202602) <br/> [Search Aftersales Request API](https://partner.tiktokshop.com/docv2/page/search-aftersales-request-202603#Back%20To%20Top) <br/> [Search Return Merchandise Authorization API](https://partner.tiktokshop.com/docv2/page/search-return-merchandise-authorization-202604#Back%20To%20Top) <br/> [Webhook Topic: Return Status Change](https://partner.tiktokshop.com/docv2/page/12-return-status-change) <br/>  | 1. 在 `return_type` 字段中新增以下枚举： <br/>    * `EXCHANGE` <br/> 2. 在 `return_status` 字段中新增以下枚举： <br/>    * `EXCHANGE_REQUEST_PENDING` <br/>    * `EXCHANGE_REQUEST_REFUND_SUCCESS` <br/>    * `EXCHANGE_REQUEST_CANCEL` <br/>    * `EXCHANGE_REQUEST_COMPLETE` |
|  |  |
|  |  |
| [Get Decision Eligibility API](https://partner.tiktokshop.com/docv2/page/get-decision-eligibility-202601) | 1. 在 `check_decisions` 和 `decision` 字段中新增以下枚举： <br/>    *  `ISSUE_EXCHANGE_REFUND` |

| **订单 API 端点** | **参数更新** |
| --- | --- |
| [Get Order Details API](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507) <br/> [Get Order List API](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) <br/>  <br/>  | 1. `is_exchange_order`：当为 `true` 时，这是一个卖家必须履行的换货订单。 <br/> 2. `exchange_source_order_id`：如果订单是换货订单，此字段返回生成该换货订单的原始订单的 order ID。仅在 `is_exchange_order`= `true` 时返回。 <br/>  <br/>  <br/> > ***注意***：当买家已通过物流承运商寄出/投递退货时，来自承运商与 TikTok 集成的信号将确认包裹在途中，TikTok 然后将自动创建新的换货订单。* <br/> > *此新的出库订单的订单价值也将为 $0.00，因为付款/GMV 已在原始 *`order_id`* 中获取，且不需要任何财务交易，因为 TikTok 目前仅允许相同价值的商品进行换货。* <br/>  ` |
|  |  |
|  |  |


> ### **4PL 模式：换货工作流**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/04cede45a9cf4e0fa802a39d4e1a6613~tplv-k9wyc2ijk0-image.image)



1. 当买家发起换货时，他们将选择不再需要的 SKU，然后选择希望换货收到的 SKU。
2. 换货提交后，TikTok Shop 将创建与买家请求关联的新 `rma_id`，并触发 RMA Status Update webhook，状态为 `rma_created`
   1. TikTok 将生成退货运输标签并分享到买家的应用和电子邮件
3. 卖家系统调用 Search Return Merchandise Authorization API 获取完整的 RMA 详情：
   1. `return_type` 参数 = `EXCHANGE`
   2. 这将使卖家的 OMS 了解此退货创建的具体使用场景。
4. 买家将使用退货结账时选择的特定承运商寄出退货（或投递）
5. 此承运商寄出/投递信号同步到 TikTok，确认买家已完成退货操作
6. 收到承运商信号后，TikTok 将**自动**为 SKU-B 创建新的出库订单。在 **Get Order Details API 和 Get Order Lists API** 中，有两个参数标识换货场景：
   1. `is_exchange_order`：布尔值
   2. `exchange_source_order_id`：生成换货订单的原始订单的 order ID。仅在 `is_exchange_order` = `true` 时返回。
7. 卖家的仓库在收到此换货的订单数据后，应履行包含换货商品的订单。



> ### **3PL 模式换货工作流**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b04ff2f23027418ca033c577d0b8a168~tplv-k9wyc2ijk0-image.image)



1. 当买家发起换货时，他们将选择不再需要的 SKU，然后选择希望换货收到的 SKU。
2. 换货提交后，TikTok Shop 将创建与买家请求关联的新 `rma_id`，并触发 RMA Status Update webhook，状态为 `rma_created`
   1. TikTok **不会**生成退货运输标签，我们期望卖家的外部系统/退货应用提供标签
3. 卖家系统调用 Search Return Merchandise Authorization API 获取完整的 RMA 详情：
   1. `return_type` 参数 = `EXCHANGE`
   2. 这将使卖家的 OMS 了解此退货创建的具体使用场景。
4. 卖家系统/退货应用将生成退货运输标签，并使用 Upload Shipping Document API 上传回 TikTok
5. 买家将使用退货结账时选择的特定承运商寄出退货（或投递）
6. 此承运商寄出/投递信号同步到 TikTok，确认买家已完成退货操作
7. 收到承运商信号后，TikTok 将**自动**为 SKU-B 创建新的出库订单。在 **Get Order Details API 和 Get Order Lists API** 中，有两个参数标识换货场景：
   1. `is_exchange_order`：布尔值
   2. `exchange_source_order_id`：生成换货订单的原始订单的 order ID。仅在 `is_exchange_order` = `true` 时返回。
8. 卖家的仓库在收到此换货的订单数据后，应履行包含换货商品的订单。


# 换货常见问题
**问题 1：** TikTok 在买家寄出退货包裹后会自动创建换货出库订单。如果我收到退货包裹，仓库检查商品后发现损坏或缺失怎么办？我有什么流程可以与买家和 TikTok 进行争议？
**回答：** 作为卖家，您可以提交仲裁流程来争议您预期收到的损坏/缺失商品。

**问题 2：** 这是破坏性变更吗？
**回答：** 不是。这是一个新增的响应字段。现有集成将继续正常工作。

**问题 3**：我的应用需要新的授权范围吗？
**回答：** 已调用 Returns & Order 范围的应用不需要新的授权。
