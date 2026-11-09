# 开发店铺手动订单状态更新指南

# 文档概述
本指南适用于在 Full Function Account 开发店铺环境中工作的卖家、测试人员和开发者。它说明了如何手动模拟通过 TikTok App 下的测试订单的订单状态推进，而无需依赖真实的履约操作（如仓储或物流）。
当你需要在开发店铺中验证端到端订单状态展示、履约回调、取消或退款行为时，请使用本指南。
# 1. 功能概述
在开发店铺环境中，卖家通常无法依赖真实的履约事件来驱动订单状态变更。手动订单状态更新功能允许测试人员在 Partner Center 中为从 TikTok App 创建的测试订单手动触发状态推进。
它涵盖了正向流程（从下单到已送达）和逆向流程（包括订单取消和退款）。这让团队能够在沙箱中端到端地验证业务逻辑和前端状态展示。
| 维度 | 描述 |
| --- | --- |
| 适用环境 | 开发店铺，Full Function Account |
| 支持市场 | 本地 Full Function Account 开发店铺。请参阅下方的国家级别表格。 |
| 支持流程 | 正向流程和逆向流程 |
| 入口 | Partner Center / Seller Center 中的开发店铺订单管理页面 |
| 目标用户 | 卖家测试人员、开发者调试工程师和运营审核人员 |
## 1.1 支持的市场
使用与 Seller Center 开发店铺指南相同的国家级别市场范围。对于 Full Function Account，支持的本地区域与 Core Function Account 相同，而跨境卖家支持目前不可用。
| 国家/地区 | 国家代码 | Full Function 本地 |
| --- | --- | --- |
| 奥地利 | AT (40) | 支持 |
| 比利时 | BE (56) | 支持 |
| 巴西 | BR (76) | 支持 |
| 捷克 | CZ (203) | 支持 |
| 法国 | FR (250) | 支持 |
| 德国 | DE (276) | 支持 |
| 希腊 | GR (300) | 支持 |
| 匈牙利 | HU (348) | 支持 |
| 印度尼西亚 | ID (360) | 支持 |
| 爱尔兰 | IE (372) | 支持 |
| 意大利 | IT (380) | 支持 |
| 日本 | JP (392) | 支持 |
| 马来西亚 | MY (458) | 支持 |
| 墨西哥 | MX (484) | 支持 |
| 荷兰 | NL (528) | 支持 |
| 菲律宾 | PH (608) | 支持 |
| 波兰 | PL (616) | 支持 |
| 葡萄牙 | PT (620) | 支持 |
| 新加坡 | SG (702) | 支持 |
| 越南 | VN (704) | 支持 |
| 西班牙 | ES (724) | 支持 |
| 泰国 | TH (764) | 支持 |
| 英国 | GB (826) | 支持 |
| 美国 | US (840) | 支持 |
特定市场的 UI 文本、运费设置、税务要求、支付行为和测试资产可能因国家/地区而异。请始终使用与开发店铺同一国家的测试产品深度链接、买家测试账户和店铺账户。
# 2. 前提条件
## 2.1 环境要求

* 你拥有一个 Full Function Account 开发店铺。
* 开发店铺已在 Partner Center / Seller Center 中完成设置。
* 用于登录 TikTok App 的买家账户已与开发店铺关联。
* 买家账户、官方测试账户、测试产品和开发店铺属于同一国家/地区。

## 2.2 测试产品准备
在 TikTok App 中下单之前，确保产品已在开发店铺中成功发布。
验收标准：

* 产品对关联的买家测试账户在 TikTok App 中可见。
* 产品可以添加到购物车。
* 完整的结账和支付流程可以在测试环境中完成。

# 3. 工作流程概述
以下图表展示了在 TikTok App 中下单后，在沙箱中手动驱动订单状态变更的完整路径，包括正向和逆向流程。
工作流程文本版：

1. 使用关联的买家测试账户在 TikTok App 中创建测试订单。
2. 确认订单出现在 Partner Center / Seller Center 中，状态为 **On Hold**。
3. 选择以下路径之一：
   * 正向流程：**On Hold -> Pending Shipment -> Awaiting Collection / In Transit -> Delivered**。
   * 卖家端逆向流程：**On Hold / Pending Shipment -> Cancelled**，或退款请求 -> 卖家审批 -> 退款状态更新。
   * 消费者端逆向流程：买家在 TikTok App 中取消订单 -> 后端订单状态更新为 **Cancelled**。
4. 每次操作后，验证后端和 TikTok App 中对应的订单状态。
5. 对后端创建的订单运行回归验证，确保现有订单操作仍然有效。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f90f283ffc2f41d1a6e4bb72fa6154cc~tplv-k9wyc2ijk0-image.image)
# 4. 详细步骤
## 4.1 步骤 1：在 TikTok App 中下单并在 Partner Center 中确认
首先，通过买家账户在 TikTok App 中下单，然后确认订单已同步到开发店铺后端。

1. 使用买家账户打开 TikTok App 中的产品详情页。
2. 完成整个流程：选择 SKU、加入购物车、下单并完成支付。
3. 进入开发店铺后端，打开**订单管理**。
4. 搜索订单 ID 或按时间筛选。
5. 确认订单可见且状态为 **On Hold**。

截图文字替代说明：

* 在 Partner Center / Seller Center 中，测试订单应出现在订单列表中。
* 订单详情页应显示订单 ID、买家信息、产品信息和当前状态。
* 此流程的预期初始状态为 **On Hold**。

验收标准：在 TikTok App 中下的单可以在 Partner Center 中找到，且状态同步正确，这意味着 TikTok App 下单路径按预期工作。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b65c33efef574d498e6306d8678348d0~tplv-k9wyc2ijk0-image.image)
## 4.2 步骤 2：正向流程 - 在后端手动驱动状态推进
### 4.2.1 挂起 -> 待发货

1. 在后端找到目标订单。当前状态应为 **On Hold**。
2. 打开订单详情页，找到**手动状态推送**操作按钮。
3. 选择 **Pending Shipment** 并确认提交。
4. 打开 TikTok App 中的**我的订单**，验证订单状态已更新为 **Pending Shipment**。

截图文字替代说明：

* 后端订单详情页应在订单符合条件时展示手动状态推送操作。
* 提交目标状态后，后端状态应先变更。
* TikTok App 应在同步后显示相同的目标状态。

注意：后端状态手动推送后，TikTok App 状态通常在几秒内同步。如果更新尚未可见，请稍等片刻并刷新页面。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/25a87058567f40869aa990ced2c6d037~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/26403bcf61ba453997c1abe3047c7993~tplv-k9wyc2ijk0-image.image)
### 4.2.2 待发货 -> 待揽收 -> 运输中

1. 确认当前订单状态为 **Pending Shipment**。
2. 点击后端中的**发货**。
3. 填写模拟物流信息。物流跟踪号可以使用测试值。
4. 提交物流信息。
5. 确认后端状态变更为 **Awaiting Collection / Shipped**。
6. 在操作可用时，继续手动将订单推送至 **In Transit**。
7. 验证 TikTok App **我的订单**中对应的订单状态是否相应更新。

截图文字替代说明：

* 后端应为处于 **Pending Shipment** 状态的订单显示**发货**操作。
* 模拟物流表单应包含市场要求的字段，如承运商和物流跟踪号。
* 提交物流信息后，状态应进入发货阶段，并可推进至 **In Transit**。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a5e21a5dbebc4630a2384187b85c5768~tplv-k9wyc2ijk0-image.image)
### 4.2.3 运输中 -> 已送达

1. 确认当前订单状态为 **In Transit**。
2. 在后端中手动将订单推送至 **Delivered**。
3. 在 TikTok App 中验证订单状态已更新为 **Delivered**。
4. 确认正向流程已完成。

截图文字替代说明：

* 后端应仅在订单到达发货阶段后允许最终的手动推进。
* 后端和 TikTok App 中的预期最终状态为 **Delivered**。

验收标准：在后端每次手动状态推送后，TikTok App 中的订单状态相应更新，确认正向状态同步路径正常工作。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/99fa0f6200474aafb821328a7952c446~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1e89b9064a1a4ed0bcbf358d8da301e3~tplv-k9wyc2ijk0-image.image)
## 4.3 步骤 3：逆向流程 - 从后端发起取消或退款
### 4.3.1 取消订单

1. 在后端中找到状态为 **On Hold** 或 **Pending Shipment** 的目标订单。
2. 点击**取消订单**。
3. 选择取消原因并确认提交。
4. 在 TikTok App 中验证订单状态已更新为 **Cancelled**。

验收标准：后端和 TikTok App 均显示目标订单为 **Cancelled**。
### 4.3.2 发起退款

1. 在后端中找到目标订单并点击**发起退款**。
2. 填写退款原因和退款金额。
3. 提交退款请求。
4. 在 Seller Center 退款管理页面中找到该请求并点击**批准退款**。
5. 退款审批完成后，在 TikTok App 中验证退款状态已更新。

重要提示：退款流程需要两个后端操作：**提交退款请求**和**作为卖家批准退款**。TikTok App 状态仅在审批步骤完成后才会变更。
## 4.4 步骤 4：在 TikTok App 中发起的逆向流程 - 取消同步回后端
此测试用例验证用户在 TikTok App 中发起的取消是否正确同步回后端。

1. 使用测试账户在 TikTok App 中下单。
2. 在后端中确认订单已创建，状态为 **On Hold**。
3. 在 TikTok App 的**我的订单**中找到订单并点击**取消订单**。
4. 在 TikTok App 中完成取消。
5. 切换到 Seller Center。
6. 刷新订单列表，确认订单状态已更新为 **Cancelled**。

验收标准：在 TikTok App 中发起取消后，后端订单状态成功更新，确认从 TikTok App 的逆向状态回调路径正常工作。
## 4.5 步骤 5：现有线上功能的回归验证
完成上述 TikTok App 相关测试用例后，还需对后端创建订单的现有正向和逆向流程进行回归测试，确保新功能不影响原有订单操作路径。

1. 使用后端中的**手动创建订单**创建一个非通过 TikTok App 下单的测试订单。
2. 执行完整正向流程：**On Hold -> Pending Shipment -> In Transit -> Delivered**。
3. 创建另一个测试订单并执行逆向流程：**取消 / 退款**。
4. 确认所有现有功能仍然正常工作，没有回归问题。

# 5. 快速参考：状态转换
| 操作类型 | 起始状态 | 目标状态 | 入口 |
| --- | --- | --- | --- |
| 正向 | On Hold | Pending Shipment | 后端 -> 订单详情 -> 手动状态推送 |
| 正向 | Pending Shipment | 待揽收 / 运输中 | 后端 -> 发货 |
| 正向 | In Transit | Delivered | 后端 -> 手动推进 |
| 逆向 | 暂挂 / 待发货 | Cancelled | 后端 -> 取消订单 |
| 逆向 | 符合退款条件的任何状态 | Refunding / Refunded | 后端 -> 发起退款 -> 批准退款 |
| 消费者端逆向 | On Hold | Cancelled | TikTok App -> 我的订单 -> 取消订单 |
# 6. 常见问题
## Q1：在 TikTok App 下单后在后端找不到订单怎么办？

* 确认登录的开发店铺账户与 TikTok App 中使用的店铺是同一个。
* 确认选择了正确的国家/地区。订单不会跨开发店铺国家共享。
* 确认买家测试账户、官方测试账户、测试产品和开发店铺属于同一国家/地区。
* 确认 TikTok App 中的支付流程已完全完成，包括支付确认。未支付的订单不会同步到后端。
* 等待约 30 秒，刷新后端中的订单列表，然后重试。

## Q2：手动推送状态后 TikTok App 订单状态未更新怎么办？

* 等待 10 到 30 秒，手动刷新 TikTok App 中的**我的订单**。
* 检查后端状态推送是否成功提交，以及后端订单状态是否已变更。
* 如果后端状态已变更但 TikTok App 尚未更新，这可能是状态传递延迟导致的。请再等一会儿或请技术团队检查消息队列。

## Q3：不同支持国家的测试流程是否相同？
是的。在所有支持的 Full Function 本地开发店铺国家中，核心流程是相同的。差异通常在于特定市场的测试资产、税务设置、运费设置、支付行为、菜单文本或特定后端操作的可用性。
请使用对应国家的测试产品深度链接、店铺账户、买家测试账户和官方测试账户。在测试前与业务负责人确认所需的特定市场测试资产。
## Q4：为什么退款流程中 TikTok App 状态没有变化？

* 退款流程需要在 Seller Center 中执行两个操作：**提交退款请求**和**批准退款**。
* 如果仅提交了退款请求，TikTok App 状态不会立即变更。
* 确保请求已在退款管理页面中找到，并且已点击**批准退款**。

## Q5：沙箱手动状态推送功能会影响生产数据吗？
不会。沙箱和生产完全隔离。开发店铺环境与生产隔离，所有测试操作不会影响真实订单或真实用户数据。
## Q6：此功能支持批量手动状态推送吗？
当前功能主要针对单订单操作设计。如果需要批量验证，请逐订单重复该流程，或向工程团队确认是否有批量接口可用。
