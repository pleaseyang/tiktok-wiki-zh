import re

# Read the original file
with open('D:/tiktok/tiktok-docs/Developer_Guide/Solution_Guidance/TikTok_Return_Models_&_Exchanges_API_Solution_Guide.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Define text replacements
replacements = [
    ("# TikTok Return Models & Exchanges API Solution Guide", "# TikTok 退货模式与换货 API 解决方案指南"),
    ("# **Aftersales Transactions Overview**", "# **售后交易概述**"),
    ("Returns/refunds, cancellations, & exchanges are post-sales (after-sales) actions that can be initiated by either buyers or sellers. TikTok Shop provides API scopes for sellers to programatically handle these cases:", "退货/退款、取消和换货是可以由买家或卖家发起的售后（售后服务）操作。TikTok Shop 为卖家提供 API 权限范围，以编程方式处理这些情况："),
    ("**Cancel Order**", "**取消订单**"),
    ("Orders can be canceled at the buyer's request or directly by the seller. Each canceled order includes the cancel reason, status, creation time, and seller processing time. In the US and UK, sellers can also partially cancel orders when items are out of stock.", "订单可以根据买家的请求或卖家直接取消。每个取消的订单包括取消原因、状态、创建时间和卖家处理时间。在美国和英国，卖家还可以在商品缺货时部分取消订单。"),
    ("**Return Order**", "**退货订单**"),
    ("Return orders occur when a buyer requests a return or refund only for one or more items after delivery. Each return order includes the return/refund reason, status, request time, seller processing time, and refund amount.", "退货订单发生在买家在收货后对一个或多个商品申请退货或仅退款时。每个退货订单包括退货/退款原因、状态、申请时间、卖家处理时间和退款金额。"),
    ("**This document will focus on Return transactions**, nuanced return label models, and give guidance on developing end-to-end solutions using the TikTok Shop open APIs based on the different return models.", "**本文档将重点介绍退货交易**、细致的退货标签模式，并指导如何基于不同的退货模式使用 TikTok Shop 开放 API 开发端到端解决方案。"),
    ("For a more **generalized** overview of all TikTok Shop Aftersales workflows, please see our documentation below:", "有关所有 TikTok Shop 售后工作流更**全面**的概述，请参阅以下文档："),
    ("# **Aftersales Stages**", "# **售后阶段**"),
    ("Before diving into the detailed API sequence, it's important to understand the **stages** of an aftersales/return record in TikTok Shop. TikTok Shops measures the seller's actions in these different return stages, to ensure the buyer communications/experience meets our SLAs/policies. **Note**: These measured **stages** are *different* from the granular return **status** that are exposed in the API/webhooks", "在深入了解详细的 API 序列之前，了解 TikTok Shop 中售后/退货记录的**阶段**非常重要。TikTok Shop 在这些不同的退货阶段衡量卖家的操作，以确保买家沟通/体验符合我们的 SLA/政策。**注意**：这些被衡量的**阶段**与 API/webhook 中暴露的细粒度退货**状态**是*不同*的"),
    ("| **Stage** | **What Happens** | **Seller Action** | **SLA / Deadline** | **Outcome / Notes** |", "| **阶段** | **发生什么** | **卖家操作** | **SLA / 截止时间** | **结果 / 备注** |"),
    ("# **Return Actions by Status**", "# **按状态划分的退货操作**"),
    ("During the lifecycle of a return, there are specific actions buyers or sellers are allowed to perform, based on the forward `order_id` status, as well as what the `return_id` status.", "在退货的生命周期中，根据正向 `order_id` 状态以及 `return_id` 状态，买家或卖家被允许执行特定操作。"),
    ("The following table illustrates when a \"Return\" can be **initiated** based on the current order status.", "下表说明了基于当前订单状态何时可以**发起**\"退货\"。"),
    ("| **Initiator** | **发起方** |", "| **发起方** | **发起方** |"),
    ("The following table illustrates what actions a seller or buyer may perform on a return, based on the current return status.", "下表说明了基于当前退货状态，卖家或买家可以对退货执行哪些操作。"),
    ("| **Return Status** | **Request Type / ID** | **Description** | **Seller Action** | **Buyer Action** |", "| **退货状态** | **请求类型 / ID** | **描述** | **卖家操作** | **买家操作** |"),
    ("# **Return Label Models**", "# **退货标签模式**"),
    ("TikTok has **2 return label models** - and the API integration path will be defined by which model is right for the sellers' specific operations/system architecture. Once the seller selects which return label model is required for their systems, they can build a holistic returns management integration with TikTok's open APIs for either of these return models.", "TikTok 有 **2 种退货标签模式** - API 集成路径取决于哪种模式适合卖家的具体运营/系统架构。一旦卖家选择了其系统所需的退货标签模式，他们就可以使用 TikTok 的开放 API 为这两种退货模式构建全面的退货管理集成。"),
    ("| **Return Model** | **Description** |", "| **退货模式** | **描述** |"),
    ("# **4PL Model: TikTok Return Labels**", "# **4PL 模式：TikTok 退货标签**"),
    ("The standard returns behavior for TikTok Shop is use TikTok's return shipping labels for the buyers. At a high-level, sellers can use our open APIs to build an end-to-end integration for returns management that will allow them:", "TikTok Shop 的标准退货行为是为买家使用 TikTok 的退货运费标签。从宏观层面来看，卖家可以使用我们的开放 API 构建端到端的退货管理集成，使他们能够："),
    ("# **3PL Model: External Return Labels**", "# **3PL 模式：外部退货标签**"),
    ("***Also known as: V2 Returns***", "***也称为：V2 退货***"),
    ("The **most common** use-case for the 3PL label model is when sellers want to leverage their existing DTC return platforms with TikTok return activity. Oftentimes, sellers' DTC process will leverage **return platforms** that are responsible for **generating a shipping label** for the buyers, and **orchestrating the data flows** and for operational functions between the return platform and their own DTC/OMS/WMS layers.", "3PL 标签模式**最常见**的使用场景是卖家希望将其现有的 DTC 退货平台与 TikTok 退货活动结合使用。通常，卖家的 DTC 流程会利用**退货平台**，这些平台负责为买家**生成运费标签**，并**协调数据流**和退货平台与其自有 DTC/OMS/WMS 层之间的运营功能。"),
    ("By leveraging these **existing** return platform workflows for TikTok Shop returns, sellers can **alleviate engineering efforts and costs**. And maintain a **consistent** end-to-end process between their DTC and TikTok Shop returns. Also, some sellers have customized attributes/barcodes rendered on the return shipping label through these return platforms. These label attributes are part of their warehouse SOPs for scanning and identifying return packages once received at their warehouse facilities.", "通过利用这些**现有的**退货平台工作流处理 TikTok Shop 退货，卖家可以**减轻工程工作量和成本**。并在其 DTC 和 TikTok Shop 退货之间保持**一致的**端到端流程。此外，一些卖家通过这些退货平台在退货标签上渲染自定义属性/条形码。这些标签属性是其仓库标准操作程序的一部分，用于在仓库设施收到退货包裹时扫描和识别。"),
    ("### Return platforms that have partnered with TikTok to build the 3PL label/QR code model:", "### 已与 TikTok 合作构建 3PL 标签/二维码模式的退货平台："),
    ("At a high-level, these existing return platform integrations follow this model outlined below", "从宏观层面来看，这些现有的退货平台集成遵循以下概述模型"),
    ("However, sellers **do not** have to leverage these existing return platform integrations. They are also able to **develop their own 3PL label model**. **** This essentially allows the seller to perform the exact steps the return platforms are managing outlined above, but the seller **use their own label** and upload directly between their systems and TikTok's API.", "但是，卖家**不必**利用这些现有的退货平台集成。他们也可以**开发自己的 3PL 标签模式**。这本质上允许卖家执行上述退货平台管理的完全相同步骤，但卖家**使用自己的标签**并在其系统与 TikTok API 之间直接上传。"),
    ("# **Exchanges**", "# **换货**"),
    ("TikTok buyers have the ability to perform an exchange, which is initiated through their return journey within the TikTok application. This allows sellers to save GMV, rather than just giving a refund for a returned item. When a buyer submits an exchange, there are API fields within the Returns & Orders API that identify an exchange is required.", "TikTok 买家可以执行换货，这是通过 TikTok 应用内的退货流程发起的。这使卖家能够保留 GMV，而不仅仅是为退货商品退款。当买家提交换货时，退货和订单 API 中有 API 字段标识需要换货。"),
    ("| **Markets** | * United States (US) * United Kingdom (UK) |", "| **市场** | * 美国 (US) * 英国 (UK) |"),
    ("| **Returns APIs** | **Parameter Update** |", "| **退货 API** | **参数更新** |"),
    ("| **Orders API Endpoints** | **Parameter Update** |", "| **订单 API 端点** | **参数更新** |"),
    ("# FAQ for Exchanges", "# 换货常见问题"),
    ("**Question 1:** TikTok automatically creates the exchange outbound order as soon as the buyer ships the return package. What happens if I receive the return package, and my warehouse inspects the item(s) to find them either damaged or missing? What processes do I have to dispute with the buyer and TikTok?", "**问题 1：** TikTok 在买家寄出退货包裹后会自动创建换货出库订单。如果我收到退货包裹，我的仓库检查商品后发现商品损坏或丢失怎么办？我有什么流程可以与买家和 TikTok 进行争议？"),
    ("**Answer:** As a seller, you can submit an arbitration process to dispute the damaged/missing items you were expecting to receive for this exchange.", "**回答：** 作为卖家，您可以提交仲裁流程来争议您预期收到的此换货的损坏/丢失商品。"),
    ("**Question 2:** Is this a breaking change?", "**问题 2：** 这是破坏性变更吗？"),
    ("**Answer:** No. This is an additive response field. Existing integrations will continue to work", "**回答：** 不是。这是一个新增的响应字段。现有集成将继续正常工作"),
    ("**Question 3**: Does my app need a new authorization scope?", "**问题 3**：我的应用需要新的授权范围吗？"),
    ("**Answer:** Apps that already call Returns & Order scopes do not need new authorization.", "**回答：** 已经调用退货和订单权限范围的应用不需要新的授权。"),
    ("| **Checklist Tasks** | **Owner** | **Comments** |", "| **检查清单任务** | **负责方** | **备注** |"),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write the result
with open('D:/tiktok/tiktok-docs/zh/Developer_Guide/Solution_Guidance/TikTok_Return_Models_&_Exchanges_API_Solution_Guide.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File written successfully, length: {len(content)}")
