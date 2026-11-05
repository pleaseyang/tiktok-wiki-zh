import re

# Read the current translated file
with open('D:/tiktok/tiktok-docs/zh/Developer_Guide/Solution_Guidance/TikTok_Return_Models_&_Exchanges_API_Solution_Guide.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Second pass: translate remaining English prose in tables and body text
replacements = [
    # Cancel/Return API bullet points
    ("* **Cancel API**: Supports buyer-initiated cancellation requests and seller-initiated order cancellations.",
     "* **取消 API**：支持买家发起的取消请求和卖家发起的订单取消。"),
    ("* **Return API**: Supports buyer-initiated refund or return-and-refund requests.",
     "* **退货 API**：支持买家发起的仅退款或退货退款请求。"),
    
    # Cancel Order paragraph
    ("Orders can be canceled at the buyer's request or directly by the seller. Each canceled order includes the cancel reason, status, creation time, and seller processing time. In the US and UK, sellers can also partially cancel orders when items are out of stock.",
     "订单可以根据买家的请求或卖家直接取消。每个取消的订单包括取消原因、状态、创建时间和卖家处理时间。在美国和英国，卖家还可以在商品缺货时部分取消订单。"),
    
    # Table row translations - 1st Review Stage
    ("| **1st Review Stage:**  <br> Return Request | Buyer submits a return request. TikTok now auto-approves **95%** of requests based on product category. Once approved, TikTok generates the official **RMA_ID** for the seller/ISV to capture the return and related line items.  | For ~5% of requests that still require review, the seller must **approve or reject** the **request** via API or Seller Center. <br>  | **24 hours** from request submission | If no decision is made within 24 hours, TikTok will **auto-approve** the request and generate the return shipping label. Some requests may require review due to restricted categories or suspicious buyer return activity. |",
     "| **第一阶段审核：**  <br> 退货请求 | 买家提交退货请求。TikTok 现在根据商品类目自动批准 **95%** 的请求。一旦批准，TikTok 将生成官方 **RMA_ID**，供卖家/ISV 记录退货及相关行项目。  | 对于仍需审核的约 5% 的请求，卖家必须通过 API 或 Seller Center **批准或拒绝****请求**。 <br>  | 自请求提交起 **24 小时** | 如果 24 小时内未做出决定，TikTok 将**自动批准**请求并生成退货运费标签。由于受限类目或可疑的买家退货活动，某些请求可能需要审核。 |"),
    
    # Table row - 2nd Review Stage
    ("| **2nd Review Stage:**  <br> Return Decision | After the returned package is received and inspected, the seller reviews the refund decision. | Seller must **approve or reject the return,** based on their item inspection SOP or automated rules. | **4 business days** after return package's tracking shows `DELIVERED`  | If no decision is made within 4 business days , TikTok will **auto-approve** the return, and the buyer will be refunded the money associated with their original payment. |",
     "| **第二阶段审核：**  <br> 退货决定 | 在收到并检查退货包裹后，卖家审核退款决定。 | 卖家必须根据其其商品检查标准操作流程或自动化规则****批准或拒绝退货**。 | 退货包裹物流显示 `DELIVERED` 后 **4 个工作日**  | 如果 4 个工作日内未做出决定，TikTok 将**自动批准**退货，买家将获得获得与其原始付款相关的退款。 |"),
    
    # After table text
    ("For all return transactions, TikTok Shop API/webhooks expose the necessary return status updates, and delivery signals that enable sellers to indentify what action they need to perform next within the return lifecycle.",
     "对于所有退货交易，TikTok Shop API/webhook 提供必要的退货状态更新和物流信号，使卖家能够识别在退货生命周期中接下来需要执行的操作。"),
    
    # Initiator table
    ("|  | **Initiator** | **`UNPAID` ** | **`ON_HOLD`** | **`AWAITING_SHIPMENT`** | **`AWAITING_COLLECTION`** | **`IN_TRANSIT`** | **`DELIVERED`** | **`Completed`** |",
     "|  | **发起方** | **`UNPAID`** | **`ON_HOLD`** | **`AWAITING_SHIPMENT`** | **`AWAITING_COLLECTION`** | **`IN_TRANSIT`** | **`DELIVERED`** | **`Completed`** |"),
    ("| **Return** <br> **Initiation** | Buyer | No | No | No | No | **Yes** | **Yes** | No |",
     "| **退货** <br> **发起** | 买家 |否 | 否 | 否 | 否 | **是** | **是** | 否 |"),
    ("|  | Seller | No <br>  | No | No | No <br>  | No <br>  | Depends on market policy. US allows for seller to create an offline return record, but it must be automatically approved for the refund amount to the buyer, | No |",
     "|  | 卖家 | 否 <br>  | 否 | 否 | 否 <br>  | 否 <br>  | 取决于市场政策。美国允许卖家创建离线退货记录，但必须自动批准退款金额给买家， | 否 |"),
    
    # Return status table rows
    ("| `RETURN_OR_REFUND_REQUEST_PENDING` <br>  | Aftersales <br>  | Buyer initiates a return request which creates an Aftersales Request ID. Although TikTok auto-approves 95% of these requests, there are some records that are pending seller review. | Approve or reject the request |  |",
     "| `RETURN_OR_REFUND_REQUEST_PENDING` <br>  | 售后 <br>  | 买家发起退货请求，创建售后请求 ID。虽然 TikTok 自动批准 95% 的此类请求，但仍有部分记录待卖家审核。 | 批准或拒绝请求 |  |"),
    ("| `AWAITING_BUYER_RETURN` <br>  | RMA  | The Aftersales return request has been approved and the official RMA `id` is created. Awaiting for the buyer to ship the item. | - <br>  | Ship the items back to seller |",
     "| `AWAITING_BUYER_RETURN` <br>  | RMA  | 售后退货请求已获批准，官方 RMA `id` 已创建。等待买家寄回商品。 | - <br>  | 将商品寄回卖家 |"),
    ("| `RETURN_IN_TRANSIT` | RMA | The buyer has shipped the item and carrier tracking confirms the return is on-route. | Seller can approve the refund of the return if needed, even before it arrives at their facility.  | - |",
     "| `RETURN_IN_TRANSIT` | RMA | 买家已寄出商品，物流追踪确认退货在途中。 | 如有需要，卖家可以在退货到达其设施之前批准退货退款。  | - |"),
    ("| `PENDING_PACKAGE_REVIEW` | RMA | The return package is confirmed `DELIVERED` by the carrier. | Inspect/grade items and make a decision to either approve or reject the refund of the return line items. | - |",
     "| `PENDING_PACKAGE_REVIEW` | RMA | 退货包裹已被物流确认为 `DELIVERED`。 | 检查/评估商品并做出批准或拒绝退货行项目退款的决定。 | - |"),
    ("| `PACKAGE_REVIEW_COMPLETED` | RMA | The return package has finished inspection and final decisions for refunds.  | Arbitration with buyer and TT CS if the results are not agreed upon. | Arbitration with buyer and TT CS if the results are not agreed upon. |",
     "| `PACKAGE_REVIEW_COMPLETED` | RMA | 退货包裹已完成检查和退款最终决定。  | 如果结果未达成一致，与买家和 TikTok 客服进行仲裁。 | 如果结果未达成一致，与买家和 TikTok 客服进行仲裁。 |"),
    
    # Return Label Models table
    ("| ###  **4PL Model:** <br> **TikTok Return Labels** <br>  | TikTok is responsible for generating the return shipping label, using our own TikTok carrier accounts. <br>  <br>",
     "| ###  **4PL 模式：** <br> **TikTok 退货标签** <br>  | TikTok 负责使用我们自己的 TikTok 物流账户生成退货运费标签。 <br>  <br>"),
    ("| ###  **3PL Model:** <br> **External Return Labels** <br>  | The seller/or external return platforms are responsible for generating a return shipping label, **AND** also responsible for **uploading** that shipping label to TikTok through our open API.  <br>  <br>",
     "| ###  **3PL 模式：** <br> **外部退货标签** <br>  | 卖家或外部退货平台负责生成退货运费标签，**并且**还负责通过我们的unser 开放 API 将该运费标签**上传**到 TikTok。 <br>  <br>"),
    
    # 4PL steps
    ("1. Capture the new return/RMA details", "1. 获取新的退货/RMA 详情"),
    ("2. Submit the return/RMA details to their return warehouse's systems (WMS/DB)", "2. 将退货/RMA 详情提交到其退货仓库系统的 systems (WMS/DB)"),
    ("3. Buyers use the TikTok shipping label to send the return package to the seller's return warehouse location", "3. 买家使用 TikTok 运费标签将退货包裹发送到卖家的退货仓库地址"),
    ("4. Warehouse operations identify the return package, inspect and grade the items", "4. 仓库运营识别退货包裹，检查和评估商品"),
    ("5. Based on the warehouse grading, send TikTok the decision to either APPROVE or REJECT the return refund to the buyer.", "5. 根据仓库评估结果，向 TikTok 发送批准或拒绝退货退款的决定。"),
    
    # 3PL steps
    ("2. Generate a 3rd party return shipping label (3PL, off TikTok's platform)", "2. 生成第三方退货运费标签（3PL，非 TikTok 平台）"),
    ("3. Upload that the 3rd party return back to TikTok to render/email to the buyer", "3. 将第三方退货标签上传回 TikTok 以展示/通过电子邮件发送给买家"),
    ("4. Submit the return/RMA details to their return warehouse's systems (WMS/DB)", "4.et 将退货/RMA 详情提交到其退货仓库的系统 (WMS/DB)"),
    ("5. Buyers use the seller's 3PL label to send the return package to the seller's return warehouse location", "5. 买家使用卖家的 3PL 标签将退货包裹发送到卖家的退货仓库地址"),
    ("6. Warehouse operations identify the return package, inspect and grade the items", "6. 仓库运营识别退货包裹，检查和评估商品"),
    ("7. Based on the warehouse grading, send return status to an OMS layer for refund decision to return platform/app.", "7. 根据仓库评估结果，将退货状态发送到 OMS 层，用于退货平台/应用的退款决定。"),
    ("8. Return Platform app to send TikTok the decision to either APPROVE or REJECT the return refund to the buyer.", "8. 退货平台应用向 TikTok 发送批准或拒绝退货退款的决定。"),
    
    # 4PL Model section
    ("The standard returns behavior for TikTok Shop is use TikTok's return shipping labels for the buyers. At a high-level, sellers can use our open APIs to build an end-to-end integration for returns management that will allow them:",
     "TikTok Shop 的标准退货行为是为买家使用 TikTok 的退货运费标签。从宏观层面来看，卖家可以使用我们的开放 API 构建端到端的退货管理集成，使他们能够："),
    
    # 3PL Model section
    ("The **most common** use-case for the 3PL label model is when sellers want to leverage their existing DTC return platforms with TikTok return activity. Oftentimes, sellers' DTC process will leverage **return platforms** that are responsible for **generating a shipping label** for the buyers, and **orchestrating the data flows** and for operational functions between the return platform and their own DTC/OMS/WMS layers.",
     "3PL 标签模式**最常见**的使用场景是卖家希望将其现有的 DTC 退货平台与 TikTok 退货活动结合使用。通常，卖家的 DTC 流程会利用**退货平台**，这些平台负责为买家**生成运费标签**，并**协调数据流**和退货平台与其自有 DTC/OMS/WMS 层之间的运营功能。"),
    
    ("By leveraging these **existing** return platform workflows for TikTok Shop returns, sellers can **alleviate engineering efforts and costs**. And maintain a **consistent** end-to-end process between their DTC and TikTok Shop returns. Also, some sellers have customized attributes/barcodes rendered on the return shipping label through these return platforms. These label attributes are part of their warehouse SOPs for scanning and identifying return packages once received at their warehouse facilities.",
     "通过利用这些**现有的**退货平台工作流处理 TikTok Shop 退货，卖家可以**减轻工程工作量和成本**。并在其 DTC 和 TikTok Shop 退货之间保持**一致的**端到端流程。此外，一些卖家通过这些退货平台在退货标签上渲染自定义属性/条形码。这些标签属性是其仓库标准操作程序的一部分，用于在仓库设施收到退货包裹时扫描和识别。"),
    
    # 3PL Prerequisites
    ("> ### **3PL Model Prerequisites Checklist**", "> ### **3PL 模式前提条件检查清单**"),
    ("There are multiple prerequisite configurations required for each sellers' shops. Sellers must have the following checklist completed **before** they are able to test the label generation & label upload flow back to the TikTok app buyer view.",
     "每个卖家的店铺都需要多个前提配置。卖家必须在能够测试标签生成和标签上传流程回到 TikTok 应用买家视图**之前**完成以下检查清单。"),
    ("| **Checklist Tasks** | **Owner** | **Comments** |  |", "| **检查清单任务** | **负责方** | **备注** |  |"),
    
    # 4PL Model API documentation
    ("> ### **4PL Model API documentation**", "> ### **4PL 模式 API 文档**"),
    ("Returns API and webhook documentation below:", "退货 API 和 webhook 文档如下："),
    ("> ### **4PL Solution Architecture & Implementation**", "> ### **4PL 解决方案架构与实施**"),
    ("> ### **3PL Model API documentation**", "> ### **3PL 模式 API 文档**"),
    ("> ### **3PL Solution Architecture & Implementation Steps (3PL Model)**", "> ### **3PL 解决方案架构与实施步骤（3PL 模式）**"),
    
    # 4PL Model: Exchange workflow
    ("> ### **4PL Model: Exchange workflow**", "> ### **4PL 模式：换货工作流**"),
    ("1. When a buyer initiates an exchange, they will select which SKU they no longer want, and then select which SKU they want to receive for the exchange.", "1. 当买家发起换货时，他们将选择不再需要的 SKU，然后选择希望换货收到的 SKU。"),
    ("2. Once the exchange is submitted, TikTok Shop will create a new `rma_id` associated with the buyer's request and trigger the RMA Status Update webhook with status `rma_created`", "2. 提交换货后，TikTok Shop 将创建与买家请求关联的新 `rma_id`，并触发状态为 `rma_created` 的 RMA 状态更新 webhook"),
    ("3. TikTok will generate a return shipping label and share that to the buyer's app and email", "3. TikTok 将生成退货运费标签并分享到买家的应用和邮箱"),
    ("3. Sellers system to call Search Return Merchandise Authorization API to capture full RMA details:", "3. 卖家系统调用搜索退货授权 API 以获取完整的 RMA 详情："),
    ("4. The buyer will ship the return (or drop-off) with the specific carrier they selected during the return check-out", "4. 买家将通过在退货结账过程中选择的特定物流方式寄回退货（或投递）"),
    ("5. This carrier shipped/dropped-off signal is synced to TikTok, confirming the buyer has performed their action to return the item", "5. 此物流的已寄出/已投递信号同步到 TikTok，确认买家已完成退货操作"),
    ("6. Upon receiving the carrier signal, TikTok will **automatically** create a new outbound order for SKU-B. Within the **Get Order Details API & Get Order Lists API,** there are two parameters that identify the exchange scenario:", "6. 收到物流信号后，TikTok 将**自动**为 SKU-B 创建新的出库订单。在**获取订单详情 API 和获取订单列表 API** 中，有两个参数标识换货场景："),
    ("7. The seller's warehouse is expected to fulfill the order with the exchange item once they receive the order data for this exchange.", "7. 卖家的仓库在收到此换货的订单数据后，应使用换货商品完成订单履约。"),
    
    # 3PL Model Exchange workflow
    ("> ### **3PL Model Exchange workflow**", "> ### **3PL 模式换货工作流**"),
    ("3. TikTok will **not** generate a return shipping label, and we are expecting the seller's external system/return app to provide the label/", "3. TikTok **不会**生成退货运费标签，我们期望卖家的外部系统/退货应用提供标签/"),
    ("4. Sellers system/Return app will generate a return shipping label and upload it back to TikTok using the Upload Shipping Document API", "4. 卖家系统/退货应用将生成退货运费标签，并使用上传货运单据 API 将其上传回 TikTok"),
    
    # FAQ
    ("**Question 1:** TikTok automatically creates the exchange outbound order as soon as the buyer ships the return package. What happens if I receive the return package, and my warehouse inspects the item(s) to find them either damaged or missing? What processes do I have to dispute with the buyer and TikTok?",
     "**问题 1：** TikTok 在买家寄出退货包裹后会自动创建换货出库订单。如果我收到退货包裹，我的仓库检查商品后发现商品损坏或丢失怎么办？我有什么流程可以与买家和 TikTok 进行争议？"),
    ("**Answer:** As a seller, you can submit an arbitration process to dispute the damaged/missing items you were expecting to receive for this exchange.",
     "**回答：** 作为卖家，您可以提交仲裁流程来对此换货中预期收到的损坏/丢失商品进行争议。"),
    ("**Question 2:** Is this a breaking change?",
     "**问题 2：** 这是破坏性变更吗？"),
    ("**Answer:** No. This is an additive response field. Existing integrations will continue to work",
     "**回答：** 不是。这是一个新增响应字段。现有集成将继续正常工作。"),
    ("**Question 3**: Does my app need a new authorization scope?",
     "**问题 3**：我的应用需要新的授权范围吗？"),
    ("**Answer:** Apps that already call Returns & Order scopes do not need new authorization.",
     "**回答：** 已经调用退货和订单权限范围的应用不需要新的授权。"),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write the result
with open('D:/tiktok/tiktok-docs/zh/Developer_Guide/Solution_Guidance/TikTok_Return_Models_&_Exchanges_API_Solution_Guide.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File updated successfully, length: {len(content)}")
