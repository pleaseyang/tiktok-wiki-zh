# 客服售后解决方案

## 业务场景与用例
> 本文档为独立软件供应商（ISV）和卖家开发者提供全面的技术集成指南，旨在在 TikTok Shop 开放平台上构建高级客服应用。重点是利用**消息卡片**管理售后操作——特别是**退货、退款和取消**——直接在第三方客服平台内完成。


在典型的售后场景中，买家通过聊天界面发起请求（例如退货）。然后客服人员需要前往 TikTok Shop Seller Center 处理此请求，造成了脱节且低效的工作流程。
此解决方案实现了无缝体验，售后操作完全在客服人员的主要工作空间中完成。例如：

1. **基于卡片的发起**：买家对购买不满意，发送了一条消息。客服人员不回复纯文本，而是发送一张交互式**退货/退款卡片**。买家从此卡片跳转到售后发起页面后，填写必要的详细信息（原因、证据）。
2. **聊天内操作**：提交的请求（包含买家的售后申请）在 ISV 集成了 TikTok Shop 退货/退款/取消 API 后，显示在聊天窗口侧边栏中。客服人员在聊天上下文中审核信息，并使用侧边栏上的操作按钮（例如**批准**、**拒绝**）处理请求。
3. **API 驱动的编排**：点击操作按钮会触发对相应 TikTok Shop Open API endpoint 的调用（例如 `POST /return_refund/.../approve`）。
4. **实时状态更新**：退货流程的状态（例如 `AWAITING_BUYER_SHIP`、`REFUND_COMPLETED`）实时更新。这可以通过更新原始消息卡片、发送新的系统消息或在专用 UI 面板中显示状态来实现，所有这些都由 Webhook 通知（`RETURN_STATUS_CHANGED`）驱动。

通过将消息卡片与售后 API 集成，ISV 可以提供更优的客服人员体验，缩短解决时间，并为买家提供透明、交互式的流程。
## 基于卡片的售后请求发起
基于卡片的发起将非结构化的投诉消息转化为引导式的售后流程。无需让买家导航到单独的退货页面，客服人员在聊天中发送结构化的**退货/退款卡片**，买家通过几个引导步骤即可完成请求。
| **阶段** | **参与者** | **聊天中的消息/卡片** | **后端操作/API** | **预期结果** |
| --- | --- | --- | --- | --- |
| 1. 发现问题 | 买家 | 买家发送纯文本消息（可选附带图片/视频）描述订单问题。 | ISV 应用使用现有 Customer Service API（conversation 和订单关联）解析买家和订单上下文。 | 相关订单被识别并与买家消息一起展示给客服人员。 |
| 2. 提供卡片 | 客服人员 | 客服人员发送 `RETURN_REFUND_CARD`（可选同时发送 `ORDER_CARD`），而非自由格式的回复。 | `POST /customer_service/202309/conversations/{conversation_id}/messages`，`type: "RETURN_REFUND_CARD"`，`content` 包含 `order_id` 和 `sku_id`。可先通过 `GET /return_refund/.../aftersale_eligibility` 检查资格。 | 买家收到一张结构化卡片，显示订单行、可选的售后选项和明确的行动号召。 |
| 3. 买家填写详情 | 买家 | 买家打开卡片，选择受影响的商品，选择**原因**，上传**证据**并确认请求。 | ISV 后端接收提交内容并调用相应的售后 API，例如 `POST /return_refund/202309/returns`（创建退货）或 `POST /return_refund/202309/cancellations`（创建取消）。 | 在 TikTok Shop 上创建新的 `return_id` 或 `cancel_id`，并与 conversation 标识符一起存储在 ISV 系统中。 |
| 4. 聊天中确认 | 系统 | 系统发送更新的 `RETURN_REFUND_CARD` 或确认消息，总结买家的请求（商品、金额、原因）。 | ISV 可选调用 `Search Returns` / `Search Cancellations` 验证已创建的请求，然后通过 `Send Message` 发送更新的卡片。 | 买家和客服人员在 conversation 中看到一致的已创建售后案例结构化视图。 |
| 5. 下一步指引 | 系统 | 卡片清楚指示下一步（例如"等待卖家审核"、"等待买家发货"）。 | 状态从售后对象（例如 `RETURN_OR_REFUND_REQUEST_PENDING`、`AWAITING_BUYER_SHIP`）获取并映射到卡片字段。 | 买家无需离开聊天即可了解下一步预期，减少重复联系和困惑。 |
### **典型的基于卡片发起场景（消息卡片对齐）：**

* **仅退款请求（无需退货）：**

买家报告商品未送达或无法使用。客服人员发送配置为**仅退款**的 `RETURN_REFUND_CARD`，ISV 调用 `Create Return`，然后调用 `Approve Return` 并设置 `decision: APPROVE_REFUND`。

* **退货退款请求：**

买家收到商品但不满意（例如尺码不对、有损坏）。卡片暴露**退货退款**选项。提交后，ISV 调用 `Create Return`，然后引导买家将商品寄回。

* **发货前订单取消：**

买家要求取消尚未发货的订单。客服人员发送取消相关的卡片（或带有**取消订单** CTA 的 `ORDER_CARD`），ISV 调用 `POST /return_refund/202309/cancellations` 创建取消请求。

* **部分退款或无需退货的退款：**

多行订单中仅部分商品有问题，或卖家选择对低价值商品发放**无需退货的退款**。`RETURN_REFUND_CARD` 允许买家或客服人员选择相关 SKU 和金额。ISV 调用 `Approve Return` 并设置 `decision: APPROVE_REFUND`，在适用情况下设置 `buyer_keep_item: true`。
## 聊天内操作与实时状态更新
售后请求创建后，客服人员应能在不离开聊天窗口的情况下审核和处理请求。ISV 在侧边栏面板和/或更新的消息卡片中展示请求，使**批准**、**拒绝**或**修改退款金额**等操作完全保持在上下文中。
| **阶段** | **参与者** | **聊天中的消息/卡片** | **后端操作/API** | **预期结果** |
| --- | --- | --- | --- | --- |
| 1. 请求展示给客服人员 | 系统 | 新的或更新的 `RETURN_REFUND_CARD` 出现，侧边栏显示当前 conversation 的售后摘要面板。 | ISV 监听 `RETURN_STATUS_CHANGED` / `CANCELLATION_STATUS_CHANGED` Webhooks 或轮询 `Search Returns` / `Search Cancellations`，然后将最新的售后记录绑定到 conversation。 | 客服人员立即看到哪些订单和商品正在审核中，无需在 Seller Center 中搜索。 |
| 2. 上下文审核 | 客服人员 | 客服人员检查卡片和侧边栏：订单详情（通过 `ORDER_CARD`）、物流信息（通过 `LOGISTICS_CARD`）以及买家消息/证据。 | ISV 通过 `Get Order Detail`、`Search Returns` 和相关物流 API 获取详情，以填充侧面板和卡片字段。 | 客服人员在单一视图中拥有所有必要的上下文（时间线、状态、之前的尝试）。 |
| 3. 操作选择 | 客服人员 | 客服人员从侧边栏或卡片中点击操作按钮，例如**批准**、**拒绝**、**仅退款**、**部分退款**或**取消订单**。 | ISV 调用相应的 endpoint，例如：`Approve Return`、`Reject Return`、`Approve Cancellation` 或 `Cancel Order`。写入调用包含幂等性 key 并在执行前验证资格。 | TikTok Shop 上的售后记录根据所选操作转换到下一个状态。 |
| 4. 在聊天中通知买家 | 系统 | 卡片和 conversation 中的消息更新以显示决定（例如"退货已批准 - 请寄送商品"、"退款已批准 - 无需退货"、"请求已拒绝，原因如下"）。 | Webhooks 触发 UI 刷新；ISV 更新 `RETURN_REFUND_CARD` 或通过 `Send Message` 发送新的系统消息。物流指引可通过 `LOGISTICS_CARD` 分享。 | 买家直接在聊天中收到即时的结构化更新和明确的下一步指引。 |
| 5. 案例关闭 | 系统 | 最终状态（例如"退款完成"、"取消完成"）在聊天和侧边栏的只读卡片中反映。 | 处理最终 Webhook（例如 `RETURN_OR_REFUND_REQUEST_COMPLETE`）；ISV 将案例标记为已解决并相应更新 UI。 | 客服人员可以关闭工单或 conversation，知道售后流程已成功完成。 |
### **典型的聊天内操作场景（消息卡片对齐）：**

* **标准退货退款批准：**

在侧边栏中，客服人员审核已送达订单的待处理 `RETURN_REFUND_CARD`，然后点击**批准退货**。ISV 调用 `Approve Return`（`decision: APPROVE_RETURN`），然后在包裹到达后调用 **Confirm goods received**（`decision: APPROVE_RECEIVED_PACKAGE`）。

* **仅退款或无需退货的退款批准：**

对于低价值或无需退回的商品，客服人员从卡片中选择**仅退款**。ISV 调用 `Approve Return` 并设置 `decision: APPROVE_REFUND`，可设置 `buyer_keep_item: true` 以实现无需退货的退款。

* **聊天中取消订单：**

对于 `AWAITING_SHIPMENT` 状态的订单，客服人员从订单相关卡片中触发**取消订单**。ISV 调用 `Cancel Order` 并使用 `CANCELLATION_STATUS_CHANGED` Webhooks 更新卡片并标记已取消的行项目。

* **多行订单的部分退款：**

当多商品订单中仅一个 SKU 有问题时，侧边栏允许客服人员选择受影响的行项目和退款金额。ISV 将选定的商品和金额传入 `Create Return` 和 `Approve Return` 调用，卡片高亮显示哪些商品已退款。

* **拒绝无效或滥用请求：**

如果资格检查失败（例如超出时间窗口、原因不正确），客服人员从卡片中点击**拒绝**，选择标准化的拒绝原因，ISV 调用 `Reject Return`。卡片变为只读状态并在 conversation 历史记录中记录决定。
## 使用的消息卡片（按用例）
**取消流程**
**概述**：取消卡片让卖家或聊天机器人为仍可取消的订单（通常为 `UNPAID`、`ON_HOLD`、`AWAITING_SHIPMENT` 状态）提供一键取消体验。卡片展示订单行和可选的取消原因，然后创建取消请求，并使用 `seller_im_order_cancellation_text_card`、`seller_im_order_cancellation_notification_card`、`seller_im_order_cancellation_voucher_card`、`seller_im_chatbot_cancel_order` 和 `seller_im_chatbot_cancel_order_result` 将最终决定展示回 conversation。
**相关 API：**

* `POST /return_refund/202309/cancellations` — 取消订单（卖家发起的取消，部分市场支持通过 `skus` 或 `order_line_item_ids` 进行部分取消）。
* `POST /return_refund/202309/cancellations/search` — 搜索取消记录（按订单、买家、状态或时间范围列出和筛选取消记录）。
* `POST /return_refund/202309/cancellations/{cancel_id}/approve` — 批准取消（卖家接受买家发起的取消请求）。
* `POST /return_refund/202309/cancellations/{cancel_id}/reject` — 拒绝取消（卖家以结构化原因拒绝买家发起的取消请求）。
* `GET /return_refund/202309/reject_reasons` — 获取拒绝原因（返回特定取消的有效拒绝原因的本地化文本）。

**资格检查：**

* `GET /return_refund/202512/orders/{order_id}/aftersale_eligibility`：
   * 在渲染 `seller_im_order_cancellation_text_card` 或 `seller_im_chatbot_cancel_order` 之前调用。
   * 将 `initiate_aftersale_user` 设为 `SELLER` 或 `BUYER`，并在 `request_types` 中包含 `CANCEL`。
   * 使用 `sku_eligibility[].line_item_eligibility[].eligible` 和 `available_reason_names` 决定哪些行项目仍可取消，以及要在卡片中展示哪些 `cancel_reason` 代码。
* `GET /return_refund/202601/decision_eligibility`：
   * 使用 `return_or_cancel_id = cancel_id` 和包含 `APPROVE_REQUEST_CANCEL` 及 `REJECT_REQUEST_CANCEL` 的 `check_decisions` 调用，然后在 `seller_im_order_cancellation_notification_card` 或 `seller_im_chatbot_cancel_order_result` 上显示批准/拒绝按钮。
   * 使用 `decisions[].eligible`、`ineligible_reason` 和 `available_reject_reasons` 启用/禁用操作并预填充拒绝原因选择器。

**操作 → 状态映射：**
| **操作** | **API 调用** | **下一状态标签** |
| --- | --- | --- |
| 创建卖家发起的取消 | `POST /return_refund/202309/cancellations` | `CANCELLATION_REQUEST_PENDING`（或立即处理时为 `CANCELLATION_REQUEST_SUCCESS`） |
| 批准买家取消请求 | `POST /return_refund/202309/cancellations/{cancel_id}/approve` | `CANCELLATION_REQUEST_SUCCESS` |
| 拒绝买家取消请求 | `POST /return_refund/202309/cancellations/{cancel_id}/reject` | `CANCELLATION_REQUEST_CANCEL` |
| 平台完成取消和退款 | Webhook + `Search Cancellations`（无直接写入 API） | `CANCELLATION_REQUEST_COMPLETE` |
**请求体要点：**

* 对于 `Cancel Order`（`POST /return_refund/202309/cancellations`）：
   * `order_id`（必填的 TikTok Shop 订单 ID）。
   * `skus[].sku_id`、`skus[].quantity` 或 `order_line_item_ids[]` 用于支持部分取消的市场。
   * `cancel_reason`（必填；使用取消原因表中与当前订单状态匹配的原因名称）。
   * 标准查询信封：`app_key`、`sign`、`timestamp`、`shop_cipher`。
   * 请求头：`x-tts-access-token`、`content-type: application/json`。
* 对于批准/拒绝取消：
   * `cancel_id`（路径参数）。
   * 对于拒绝：`reject_reason`（来自 `Get Reject Reasons`），可选 `comment`，可选 `images[].image_id` 及基本元数据。

**操作注意事项：**

* 在取消/批准/拒绝调用中使用 `idempotency_key` 来去重来自卡片点击或网络错误的重试。
* 将常见错误映射为卡片级别的消息：
   * `25001021 Reason not match order status` → 更新卡片告知客服人员此原因不再适用于当前订单状态。
   * `25001045` / `25001051` → 订单已发货或已完成，无法取消；引导客服人员改用退款/退货流程。
   * `25001011` → 取消或退货已在处理中；重新绑定现有案例而非创建新案例。
* 使用 `Search Cancellations` 驱动聊天内时间线并从遗漏的 Webhooks 中恢复；按 `cancel_status`、`cancel_types` 和时间范围筛选。
* 各 endpoint 未列出明确的速率限制；实施客户端限流和指数退避，并依赖平台文档获取任何全局限制。

**仅退款 / 无需退货的退款流程**
**概述**：仅退款和无需退货的退款卡片支持快速的货币补偿流程，无需强制买家退回商品。`seller_im_quick_refund_confirmation`、`seller_im_quick_refund_succeeded`、`seller_im_approve_refund_withdout_return` 和 `seller_im_chatbot_aftersales_check_status` 等卡片让客服人员可以提供全额或部分退款，对于无需退货的退款可选设置 `buyer_keep_item = true`。
**相关 API：**

* `POST /return_refund/202309/returns` — 创建退货（仅退款场景使用 `return_type = REFUND`，可选 `refund_total` 和 `currency`）。
* `POST /return_refund/202309/refunds/calculate` — 计算退款（在卡片上展示前预览每个订单/行的可退款金额）。
* `POST /return_refund/202309/returns/{return_id}/approve` — 批准退货（设置 `decision = APPROVE_REFUND`，可选 `buyer_keep_item = true` 和/或 `partial_refund` 金额）。
* `POST /return_refund/202309/returns/{return_id}/reject` — 拒绝退货（当仅退款请求无效时设置 `decision = REJECT_REFUND`）。
* `POST /return_refund/202309/returns/search` — 搜索退货（列出店铺或订单的退款案例及其状态）。
* `GET /return_refund/202309/returns/{return_id}/records` — 获取退货记录（用于丰富 `seller_im_chatbot_aftersales_check_status` 的时间线）。

**资格检查：**

* `GET /return_refund/202512/orders/{order_id}/aftersale_eligibility`：
   * 在显示快速退款选项之前，使用包含 `REFUND` 的 `request_types` 调用。
   * 使用 `sku_eligibility[].line_item_eligibility[].eligible` 将仅退款操作限制在符合条件的行，并驱动卡片中可预选的 SKU。
* `GET /return_refund/202601/decision_eligibility`：
   * 使用 `return_or_cancel_id = return_id` 和包含 `APPROVE_REFUND`、`DIRECT_REFUND`、`OFFER_PARTIAL_REFUND` 及 `REJECT_REFUND`（在支持的情况下）的 `check_decisions` 调用。
   * 使用响应启用或禁用 `seller_im_quick_refund_confirmation` 上的按钮，并在客服人员选择拒绝时获取 `available_reject_reasons`。

**操作 → 状态映射：**
| **操作** | **API 调用** | **下一状态标签** |
| --- | --- | --- |
| 创建仅退款请求（全额或部分） | `POST /return_refund/202309/returns`（`return_type = REFUND`） | `RETURN_OR_REFUND_REQUEST_PENDING` |
| 批准仅退款 / 无需退货的退款 | `POST /return_refund/202309/returns/{return_id}/approve`（`decision = APPROVE_REFUND`，可选 `buyer_keep_item`、`partial_refund`） | `RETURN_OR_REFUND_REQUEST_SUCCESS` |
| 平台完成退款支付 | Webhook + `Search Returns`（无直接写入 API） | `RETURN_OR_REFUND_REQUEST_COMPLETE` |
| 拒绝仅退款请求 | `POST /return_refund/202309/returns/{return_id}/reject`（`decision = REJECT_REFUND`） | `REFUND_OR_RETURN_REQUEST_REJECT` |
**请求体要点：**

* 对于 `Calculate Refund`：
   * `order_id`（必填）、`request_type`（`REFUND` 或 `CANCEL`）、`reason_name`（来自退款原因表），
   * `order_line_item_ids[]` 和/或 `skus[]`（每个包含 `sku_id`、`quantity`）以限定退款范围，
   * 可选的 `shipment_type` 和 `handover_method` 用于可能后续转为退货退款的场景。
* 对于 `Create Return`（仅退款）：
   * `order_id`、`return_type = REFUND`、`return_reason`（与退款原因表一致的原因名称），
   * 可选的 `refund_total` 和 `currency`（不得超过计算的可退款金额），
   * `order_line_item_ids[]` 和/或 `skus[]` 以支持部分退款。
* 对于 `Approve Return`（仅退款）：
   * `return_id`、`decision = APPROVE_REFUND`，
   * 可选的 `buyer_keep_item`（无需退货时为 true），
   * 可选的 `partial_refund.currency` 和 `partial_refund.amount` 用于部分退款。

**操作注意事项：**

* 在提交快速退款卡片之前始终调用 `Calculate Refund`，并向客服人员透明展示 `refund_total`、`refund_shipping_fee`、`refund_tax` 和其他组成部分。
* 如果 `Create Return` 调用时 `refund_total` 大于平台计算的可退款金额，API 返回 `25005005`；在卡片中展示此错误并从 `Calculate Refund` 重新同步金额。
* 仅在您的政策和 TikTok Shop 政策明确允许无需退货退款的情况下使用 `buyer_keep_item = true`；`seller_im_approve_refund_withdout_return` 等卡片应清楚告知买家可以保留商品。
* 对于多行订单的部分退款，保持 `order_line_item_ids` / `skus` 与 UI 行之间的映射，以便 `seller_im_quick_refund_succeeded` 可以准确高亮显示哪些商品已退款。
* 通过禁用确认按钮并要求客服人员调整选择来处理常见验证错误（`25001014`/`25001020` 未知或下线原因、`25005011` 行项目超限），而不是反复调用 API。

**退货退款流程**
**概述**：退货退款卡片处理完整的实物退货流程：卖家审核、买家发货、卖家检验和最终退款。`seller_im_seller_approve_return_request_card`、`seller_im_seller_reject_return_request_card` 和 `seller_im_chatbot_aftersales_check_status` 等卡片使买家和客服人员与 `AWAITING_BUYER_SHIP`、`BUYER_SHIPPED_ITEM` 和 `RETURN_OR_REFUND_REQUEST_COMPLETE` 等平台状态保持一致。
**相关 API：**

* `POST /return_refund/202309/returns` — 创建退货（标准退货使用 `return_type = RETURN_AND_REFUND`，实物商品退回）。
* `POST /return_refund/202309/returns/{return_id}/approve` — 批准退货：
   * 初次批准（`decision = APPROVE_RETURN`）将案例移至"等待买家发货"；
   * 后续批准（`decision = APPROVE_RECEIVED_PACKAGE`）确认退回包裹并触发退款。
* `POST /return_refund/202309/returns/{return_id}/reject` — 拒绝退货（根据卖家是拒绝请求本身还是拒绝收到的包裹，使用 `decision = REJECT_RETURN` 或 `REJECT_RECEIVED_PACKAGE`）。
* `POST /return_refund/202309/returns/search` — 搜索退货（退货状态、仲裁状态和卖家下一步操作的主要来源）。
* `GET /return_refund/202309/returns/{return_id}/records` — 获取退货记录（用于丰富状态检查卡片的时间事件日志）。
* `GET /return_refund/202309/reject_reasons` — 获取拒绝原因（用于退货）。

**资格检查：**

* `GET /return_refund/202512/orders/{order_id}/aftersale_eligibility`：
   * 在卡片上启用"退货退款"CTA 之前，使用包含 `RETURN_AND_REFUND` 的 `request_types` 调用。
   * 使用每个 SKU 的 `eligible` 标志和 `available_reason_names` 控制哪些行可以退货，以及在 `seller_im_seller_approve_return_request_card` 中展示哪些退货原因。
* `GET /return_refund/202601/decision_eligibility`：
   * 对于现有的 `return_id`，使用 `return_or_cancel_id = return_id` 和包含 `APPROVE_RETURN`、`APPROVE_RECEIVED_PACKAGE`、`REJECT_RETURN` 及 `REJECT_RECEIVED_PACKAGE` 的 `check_decisions` 调用。
   * 使用 `decisions[].eligible` 决定是否在卡片上显示或禁用当前状态的批准/拒绝按钮，并使用 `available_reject_reasons` 填充拒绝原因下拉菜单。

**操作 → 状态映射：**
| **操作** | **API 调用** | **下一状态标签** |
| --- | --- | --- |
| 创建退货退款请求 | `POST /return_refund/202309/returns`（`return_type = RETURN_AND_REFUND`） | `RETURN_OR_REFUND_REQUEST_PENDING` |
| 批准退货请求（要求买家发货） | `POST /return_refund/202309/returns/{return_id}/approve`（`decision = APPROVE_RETURN`） | `AWAITING_BUYER_SHIP` |
| 买家发货且物流更新状态 | 物流更新 → Webhook `RETURN_STATUS_CHANGED` 或 `Search Returns` | `BUYER_SHIPPED_ITEM` |
| 确认收货并通过检验 | `POST /return_refund/202309/returns/{return_id}/approve`（`decision = APPROVE_RECEIVED_PACKAGE`） | `RETURN_OR_REFUND_REQUEST_SUCCESS` |
| 平台完成退款支付 | Webhook + `Search Returns` | `RETURN_OR_REFUND_REQUEST_COMPLETE` |
| 拒绝请求或检验后拒绝包裹 | `POST /return_refund/202309/returns/{return_id}/reject`（`decision = REJECT_RETURN` 或 `REJECT_RECEIVED_PACKAGE`） | `REFUND_OR_RETURN_REQUEST_REJECT` 或 `REJECT_RECEIVE_PACKAGE` |
**请求体要点：**

* 对于 `Create Return`（退货退款）：
   * `order_id`（必填）、`return_type = RETURN_AND_REFUND`，
   * `return_reason`（来自退货原因表的原因名称，与订单状态和品类匹配），
   * `order_line_item_ids[]` 和/或 `skus[]`（`sku_id`、`quantity`）描述要退货的商品，
   * 可选的 `refund_total` 和 `currency`（必须在这些行的可退款金额范围内），
   * `shipment_type`（`PLATFORM` 或 `BUYER_ARRANGE`），当为 `PLATFORM` 时还需 `handover_method`（`DROP_OFF` 或 `PICKUP`）。
* 对于 `Approve Return` / `Reject Return`：
   * `return_id`（路径参数），
   * `decision` 匹配当前阶段（`APPROVE_RETURN`、`APPROVE_RECEIVED_PACKAGE`、`REJECT_RETURN`、`REJECT_RECEIVED_PACKAGE`），
   * 对于批准：可选的 `buyer_keep_item` 和 `partial_refund`（用于高级流程，如检验后的部分退款），
   * 对于拒绝：`reject_reason`（来自 `Get Reject Reasons`），可选 `comment`，可选 `images[]`。

**操作注意事项：**

* 在 `Create Return`、`Approve Return` 和 `Reject Return` 上使用 `idempotency_key`，防止在 `seller_im_seller_approve_return_request_card` 或 `seller_im_seller_reject_return_request_card` 上的重复点击。
* 在 UI 中优雅处理常见错误：
   * `25001010` / `25001011` 表示存在已完成或已完成的退货；不要静默失败操作，而是将卡片重新绑定到现有的 `return_id`。
   * `25005005` / `25005011` 表示无效的退款金额或商品数量；通过 `Calculate Refund` 刷新计算金额。
   * `25001014` / `25001020` 表示无效或下线的原因；从原因/资格 API 刷新原因列表。
* 将 Webhooks（`RETURN_STATUS_CHANGED`）与 `Search Returns` 和 `Get Return Records` 结合使用，使 `seller_im_chatbot_aftersales_check_status` 与权威平台状态保持同步，包括仲裁结果和包裹事件。

**物流与地址确认（主动通知）**
主动物流和地址卡片——`seller_im_proactive_confirm_address`、`seller_im_proactive_order_received` 和 `seller_im_proactive_abnormal_logistics`——主要是**通知展示面**。发送这些卡片本身不应触发订单、退货或取消 API 调用：后端将其视为只读状态或确认消息。只有当买家或客服人员点击卡片内的深度链接或 CTA（例如编辑收货地址或打开售后发起页面）时，ISV 才应调用相应的工作流 API（地址更新、物流索赔或售后发起）。这使得主动物流消息无副作用，同时仍允许深度链接操作在明确请求时启动完整的售后流程。
# 卖家工作台展示指引与文本回退
## 支持的消息类型与展示规则
使用 Message Types 规范中的 `content` / `data` / `plaintext` 三元组作为渲染基础：

* `content`：用于识别资源（订单、商品、优惠券、包裹等）的最小元数据。
* `data`：用于构建自定义 UI 的丰富业务数据载荷；仅在 `need_data = true` 时存在。
* `plaintext`：用于简单客户端或回退的预扁平化文本描述；仅在 `need_plaintext = true` 时存在。

在卖家工作台上，始终优先使用 `data` 进行丰富卡片渲染，并将 `plaintext` 作为回退。

* **文本（`TEXT`）**
   * **最小字段**：`content.content`（纯文本）。可选使用 `plaintext` 获取完整文本表示。
   * **展示**：渲染为多行左对齐文本；支持 URL 自动链接；保留换行和基本标点。默认不截断；如需截断，提供"展开更多"功能。
   * **无障碍**：确保足够的颜色对比度和可调整的字体大小；将完整文本暴露给屏幕阅读器。
* **图片/表情（`IMAGE` / emoticons）**
   * **最小字段**：`content.url`、`content.width`、`content.height`。
   * **展示**：显示保持宽高比的缩放缩略图并适应聊天宽度；点击缩略图应打开全尺寸预览。对于表情风格的图片，可在适当位置与文本内联渲染。
   * **无障碍**：如果 `plaintext` 存在，将其用作替代文本/无障碍标签。当图片加载失败时，显示带有相同替代文本的占位符，而非空白框。
* **视频（`VIDEO`）**
   * **最小字段**：`content.url` 和 `content.cover`；可用时还使用 `width`、`height`、`duration`。
   * **展示**：显示封面图片和清晰的播放图标。不在 conversation 列表中自动播放；点击时打开模态框或侧面板播放器。可用时在缩略图上标注时长。
   * **无障碍**：提供"视频消息"等无障碍标签并朗读时长；确保键盘焦点可以到达播放按钮。
* **订单卡片（`ORDER_CARD`）**
   * **最小字段**：`content.order_id`。丰富展示依赖 `data.order_status`、`data.product_name`、`data.product_image`、`data.paid_price`、`data.quantity`、`data.order_link`。
   * **展示**：渲染包含商品缩略图、标题、数量、订单状态和已付金额的紧凑卡片。主要 CTA 应为**查看订单详情**，使用 `data.order_link` 或内部深度链接到卖家的订单详情面板。
   * **无障碍**：使整个卡片可作为单一单元获得焦点，带有清晰标签（例如"订单卡片 – {product_name}，状态 {order_status}"）。确保 CTA 可通过键盘到达。
* **商品卡片（`PRODUCT_CARD`）**
   * **最小字段**：`content.product_id`。UI 使用 `data.product_name`、`data.product_image`、`data.product_lowest_price`、`data.product_highest_price`、`data.sold_quantity`、`data.product_link`。
   * **展示**：显示商品图片、名称、价格区间和关键销售信号（例如已售数量）。主要 CTA：**查看商品**（打开 `product_link` 或内部商品页面）。在主动物流流程中，可用于在配送延迟时推荐替代品或追加销售商品。
   * **无障碍**：提供"商品卡片 – {product_name}，价格从 {product_lowest_price} 起"等标签；确保卡片可通过键盘导航。
* **优惠券卡片（`COUPON_CARD`）**
   * **最小字段**：`content.coupon_id`。UI 使用 `data.coupon_title`、`data.discount`、`data.threshold`、`data.scope`、`data.start_time`、`data.end_time`、`data.coupon_link`。
   * **展示**：突出展示折扣金额或百分比，附带条件（门槛）和有效期。主要 CTA：**查看优惠券**或**使用优惠券**，引导至 `coupon_link` 或应用内优惠券面板。
   * **无障碍**：以纯文本形式播报折扣、门槛和到期时间，使屏幕阅读器能传达完整优惠信息。
* **物流卡片（`LOGISTICS_CARD`）**
   * **最小字段**：`content.order_id`、`content.package_id`。详细 UI 使用 `data.packages[*].product_name`、`product_image`、`quantity`、`tracking_number`、`shipping_provider_name`、`predict_delivery_time_*` 和 `tracking` 历史。
   * **展示**：在卡片头部摘要展示关键包裹信息（承运商、追踪单号、最新状态和时间戳），随后是商品缩略图和名称。主要 CTA：**追踪包裹**，打开从 `data.tracking` 构建的专用追踪视图或外部追踪链接。
   * **无障碍**：确保最新状态文本（例如"正在派送"）始终以文本形式存在，而不仅通过图标或颜色表示。
* **主动物流与地址卡片（`seller_im_proactive_confirm_address`、`seller_im_proactive_order_received`、`seller_im_proactive_abnormal_logistics`）**
   * **最小字段**：与 `LOGISTICS_CARD` 相同的结构基础（订单和包裹标识符）。存在时，还为 `seller_im_proactive_confirm_address` 展示买家收货姓名、电话和地址摘要，以及为 `seller_im_proactive_abnormal_logistics` 展示最新物流事件。
   * **展示**：
      * 在卡片标题中突出场景（例如"确认收货地址"、"我们已收到您的订单"、"您的配送有问题"）。
      * 每张卡片使用单一主要 CTA：**确认地址**、**追踪包裹**或**打开支持选项**，应深度链接到相应的地址编辑、追踪或售后发起流程。
      * 在卖家工作台中将卡片视为只读状态/通知；任何状态变更操作必须在用户与 CTA 明确交互后才发生。
   * **无障碍**：提供明确的文本描述，说明卡片要求买家做什么（确认、审核或联系支持），以便即使在纯文本或屏幕阅读器场景下意图仍然清晰。

## 文本回退机制
设计卖家工作台在丰富卡片渲染不可用时优雅降级。

* **何时回退**
   * `type` 未知或您的 UI 能力矩阵尚未支持。
   * `type` 已知但预期的 `data` 结构缺失或未通过验证。
   * 媒体资源（图片/视频 URL）无法加载或已过期。
   * 平台因速率限制、权限问题或策略/审核检查而拒绝卡片发送或更新。
* **回退优先级**
   1. **卡片 UI**：尽可能使用 `type` 和 `data` 渲染完整的交互式卡片。
   2. **富文本视图**：如果您不支持给定 `type` 的卡片组件，将 `data` 格式化为结构化文本块（例如订单摘要、物流状态、优惠券详情），并作为非交互式消息展示，保留关键值。
   3. **纯文本视图**：如果 `data` 不可用或解析失败，回退到 `plaintext`（存在时）或从 `content` 构建最小文本存根（例如"订单 {order_id} 的物流更新 – 追踪单号 {tracking_number}"）。
* **任何回退中必须保留的字段**
   * 订单标识符：`order_id`，以及适用时的 `sku_id` 或 `order_line_item_ids`。
   * 物流标识符：`package_id` 和/或 `tracking_number`。
   * 主要深度链接 URL：订单详情链接、追踪链接、售后发起链接、地址编辑链接。
   * 人类可读的状态文本（例如"等待发货"、"正在派送"、"配送异常"）。
* **文本模式下的 CTA 措辞**
   * 使用清晰的、面向操作的文本并附带明确链接，例如：
      * "查看订单详情：{order_link}"
      * "追踪包裹：{tracking_link}"
      * "确认收货地址：{address_link}"
      * "打开退货/退款页面：{aftersales_link}"
   * 避免在可见文本中暴露原始查询字符串参数或内部 ID；将技术细节保留在日志中，而非面向用户的 CTA 中。

## 实施检查清单

* **服务端类型检测**
   * 解析 Customer Service API 返回的每条消息的 `type`、`content`、`data` 和 `plaintext`。
   * 维护消息 `type`（以及适用时的特定卡片标识符，如 `seller_im_proactive_confirm_address`）到 UI 组件和支持操作的映射。
* **UI 能力矩阵**
   * 存储一个配置，描述对于每种消息类型，卖家工作台是否支持完整卡片渲染、卡片+操作，还是仅文本。
   * 在渲染时使用此矩阵决定使用原生卡片、富文本回退还是纯文本回退。
* **安全的文本和 HTML 渲染**
   * 将 `plaintext` 视为不可信文本：转义 HTML，不执行脚本，避免从 `data` 注入原始 HTML。
   * 在卖家工作台中仅允许最小格式集（换行、基本强调）；避免在卡片内嵌入 iframe 或第三方小部件。
* **深度链接验证**
   * 为深度链接设置域名白名单（例如 TikTok Shop 官方域名和您自己的 ISV 域名）。
   * 在导航前验证 URL scheme；在受控的 webview 或浏览器标签中打开链接，并优雅地处理错误（例如目标无法到达时显示"链接不可用"）。
* **错误展示与重试**
   * 当从卡片触发的操作（例如"确认地址"、"追踪包裹"）失败时，在卡片上显示内联错误状态，并记录失败信息及相关 `message_id`、`order_id` 和 API `request_id`。
   * 在服务端实施有界重试和幂等性 key；永远不要在 UI 上没有明确反馈的情况下多次重复发送同一操作。
* **审计日志与可观测性**
   * 记录消息接收、卡片渲染、用户交互（CTA 点击）和下游 API 调用，以便可以按 conversation 和订单进行关联。
   * 捕获足够的上下文（消息 `type`、标识符、状态转换），以在事件调查期间重建卖家和买家在工作台中看到的内容。
* **无障碍与国际化**
   * 确保所有卡片操作可通过键盘操作并向屏幕阅读器播报。
   * 不要仅在图片或颜色中编码业务关键信息；始终包含文本状态行。
   * 设计可容纳不同长度本地化字符串的布局，而不截断关键信息。

# API 解决方案设计
## 解决方案描述
此解决方案以 TikTok Shop **Customer Service API** 和 **Return/Refund/Cancel API** 的强大组合为核心。通过在 conversation 中发送的交互式消息卡片编排整个售后生命周期。
核心架构原则为：

* **展示层（消息卡片）**：所有售后操作和状态展示都在聊天 conversation 中渲染为结构化、交互式的消息卡片。这替代了非结构化的文本通信，减少歧义并提高效率。这些卡片的设计源自 `Message Types` 文档。
* **操作层（Customer Service 和 Post-Sales API）**：客服人员在消息卡片上的操作（例如点击"批准退款"）直接映射到特定的 API 调用。`Send Message` API 用于传递卡片，而 `Return/Refund/Cancel` API 用于执行业务逻辑。
* **状态管理层（Webhooks 和 API 轮询）**：系统主要依赖 Webhook 事件（例如 `RETURN_STATUS_CHANGED`、`CANCELLATION_STATUS_CHANGED`）进行实时状态同步。辅以轮询机制（例如 `Search Returns` API）用于数据对账和处理任何潜在的 Webhook 传递失败。
* **验证与资格层**：在向客服人员展示操作之前，系统使用资格 API（例如 `Get Aftersale Eligibility`）确保请求的操作对订单或退货的当前状态有效，防止错误并提供引导式的客服人员体验。

此设计创建了一个闭环系统，客服人员可以在其中自信地管理复杂的售后工作流，而无需离开其客服仪表板。


## 售后流程概述
以下图表展示了可通过消息卡片管理的三个主要售后工作流：

* **取消**：发生在订单发货之前。这是最简单的流程，通常只需要一个批准步骤。
* **仅退款**：用于买家无需退回商品的情况（例如商品未收到或严重损坏）。此流程的核心是卖家批准或拒绝退款。
* **退货退款**：最复杂的流程，涉及实物退货。包括多个阶段：卖家批准、买家发货、卖家收货检验，最后平台退款。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e7d2249422a1448ebd397407b93a1dd6~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/42ff652cb5c64ab7980e0fe5cf10f576~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/193dae825e6b4289831877e6e45cc712~tplv-k9wyc2ijk0-image.image)
这些流程中的每一步都可以用消息卡片更新或新的系统消息来表示，使买家和卖家都保持知情。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a8f8b60b2da94e42b79b4605ebb49f0a~tplv-k9wyc2ijk0-image.image)

此时序图详述了通过消息卡片发起和管理的典型**退货退款**流程的交互：

1. **基于卡片的发起**：客服人员向买家发送 `RETURN_REFUND_CARD`。买家填写并提交。
2. **API 操作**：ISV 应用接收卡片提交并调用 `Create Return` API。
3. **通过卡片进行卖家决策**：客服人员收到新卡片或显示待处理请求的更新视图。客服人员点击"批准"，触发 `Approve Return` API 调用。
4. **Webhook 驱动的状态同步**：TikTok Shop 平台处理批准并发送 `RETURN_STATUS_CHANGED` Webhook。ISV 应用消费此事件以更新其内部状态并刷新 UI（例如更新卡片显示"等待买家发货"）。
5. **流程完成**：后续步骤（如卖家确认收到退货商品）遵循相同的 API 调用和 Webhook 驱动更新模式，直到达到最终的"退款完成"状态。

此时序突出了集成的响应式特性，系统响应事件和 API 调用以引导工作流前进。
# 售后操作的卡片分类
清晰一致的卡片分类对于构建直观的客服人员体验至关重要。以下卡片源自官方 `Message Types` 文档，是售后工作流的基础。
| **卡片类型** | **用途** | **关键 `content` 字段** | **关键 `data` 字段（用于 UI 渲染）** |
| --- | --- | --- | --- |
| **RETURN_REFUND_CARD** | 发起或展示退货或退款请求的状态。这是售后操作的主要卡片。 | `order_id`、`sku_id` | `product_name`、`product_image`、`paid_price`、`quantity`、`return_status`、`return_reason`、`refund_amount` |
| **ORDER_CARD** | 提供与售后请求相关的原始订单上下文。 | `order_id` | `order_status`、`product_name`、`quantity`、`paid_price`、`order_link` |
| **LOGISTICS_CARD** | 展示退货物流信息，包括追踪单号和状态更新。 | `order_id`、`package_id` | `tracking_number`、`shipping_provider_name`、`tracking`（历史）、`delivery_option` |
| **PRODUCT_CARD** | 与买家分享替代商品或替换品。 | `product_id` | `product_name`、`product_image`、`product_highest_price`、`product_link` |
| **TEXT**、**IMAGE**、**VIDEO** | 用于补充通信，例如发送指引、向买家请求更多证据或确认操作。 | `content`（文本）或 `url`（媒体） | 不适用 |
## 载荷与验证
使用 `POST /customer_service/202309/conversations/{conversation_id}/messages` endpoint 发送卡片时，`body` 必须正确构造。
**示例：发送 `RETURN_REFUND_CARD`**
```JSON
{
  "type": "RETURN_REFUND_CARD",
  "content": "{\\"order_id\\":\\"580874485811283206\\",\\"sku_id\\":\\"7494560109732363423\\"}"
}
```

**验证规则：**

* `content` 字段必须是 JSON 序列化字符串。
* 对于 `RETURN_REFUND_CARD`，`order_id` 和 `sku_id` 都是必填的，用于识别售后过程中的特定商品。
* 在发送 `RETURN_REFUND_CARD` 之前，最佳实践是先调用 `GET /return_refund/.../aftersale_eligibility` endpoint 确保订单/商品符合退货或退款资格。这防止发送无法履行的操作卡片。

# 操作映射与状态编排
## API Endpoint 映射
以下表格将售后工作流中的关键客服人员操作映射到其对应的 API endpoint。
| **客服人员操作** | **HTTP 方法与 Endpoint** | **关键参数** | **注意事项与安全性** |
| --- | --- | --- | --- |
| **检查资格** | `GET /return_refund/202512/orders/{order_id}/aftersale_eligibility` | `request_types`（例如 REFUND、CANCEL） | 预防性使用，仅向客服人员展示有效的操作按钮。 |
| **批准请求** | `POST /return_refund/202309/returns/{return_id}/approve` | `decision`（例如 APPROVE_RETURN、APPROVE_REFUND） | 需要 `seller.return_refund.basic` 权限范围。使用 `Idempotency-Key` 防止重复批准。 |
| **拒绝请求** | `POST /return_refund/202309/returns/{return_id}/reject` | `decision`、`reject_reason`、`comment` | `reject_reason` 应从通过 `GET /return_refund/202309/reject_reasons` API 获取的列表中选择。 |
| **确认收货** | `POST /return_refund/202309/returns/{return_id}/approve` | `decision`（APPROVE_RECEIVED_PACKAGE） | 触发平台最终退款流程。此操作不可逆。 |
| **取消订单** | `POST /return_refund/202309/cancellations` | `order_id`、`cancel_reason` | 用于卖家发起的取消。先检查资格。使用 `order_line_item_ids` 进行部分取消。 |
| **批准取消** | `POST /return_refund/202309/cancellations/{cancel_id}/approve` | `cancel_id` | 批准买家发起的取消请求。 |
## 状态机与卡片更新（退货退款）
退货状态决定了可用操作和消息卡片的展示方式。
| 当前状态 | 允许的客服人员操作 | 下一状态（成功时） | 卡片更新策略 |
| --- | --- | --- | --- |
| `RETURN_OR_REFUND_REQUEST_PENDING` | 批准退货、批准退款（无需退货）、拒绝 | `AWAITING_BUYER_SHIP`、`REQUEST_SUCCESS`、`REQUEST_REJECTED` | 使用操作按钮更新卡片。操作后禁用按钮并显示"处理中..."。Webhook 确认后更新状态文本。 |
| `AWAITING_BUYER_SHIP` | （客服人员只读） | `BUYER_SHIPPED_ITEM` | 展示状态和退货收货地址/标签。监听 Webhook。 |
| `BUYER_SHIPPED_ITEM` | 确认收货、拒绝收货 | `REQUEST_SUCCESS`、`RECEIVE_REJECTED` | 使用新操作按钮更新卡片。Webhook 确认后更新为"退款处理中"。 |
| `REQUEST_SUCCESS` | （客服人员只读） | `RETURN_OR_REFUND_REQUEST_COMPLETE` | 展示状态"退款处理中"。最终 Webhook 后更新为"退款完成"。 |
| `REQUEST_REJECTED` | （客服人员只读） | 不适用 | 展示最终状态"请求已拒绝"及提供的原因。 |
| `RETURN_OR_REFUND_REQUEST_COMPLETE` | （客服人员只读） | 不适用 | 展示最终状态"已完成"。 |
**Webhook 与轮询**：始终优先使用 Webhook 集成进行实时状态更新。使用 API 轮询（`Search Returns`、`Search Cancellations`）作为回退机制，定期对账状态并从任何遗漏的事件中恢复。两者结合确保系统稳健且响应迅速。

# 实施指南与测试用例
## 分步集成流程

1. **认证与授权**：
   * 引导卖家授权您的应用，确保您请求 `seller.return_refund.basic` 和 `seller.customer_service` 权限范围。
   * 安全存储每个卖家的 `access-token` 和 `shop_cipher`。
2. **Webhook 订阅**：
   * 在 TikTok Shop Partner Center 的应用设置中，订阅 `RETURN_STATUS_CHANGED` 和 `CANCELLATION_STATUS_CHANGED` 事件。
   * 在后端实施公共 endpoint 以接收和验证这些 Webhook POST 请求。
3. **构建卡片发送逻辑**：
   * 集成 `POST /customer_service/202309/conversations/{conversation_id}/messages` endpoint。
   * 创建为每种卡片类型（例如 `ORDER_CARD`、`RETURN_REFUND_CARD`）构造 JSON `content` 字符串的服务。
4. **开发操作处理器**：
   * 创建后端服务，将来自 UI 的请求（例如客服人员点击"批准"）映射到正确的 Post-Sales API endpoint（例如 `Approve Return`）。
   * 此服务应处理参数构造、API 签名和错误处理。记得为所有写入操作实施 `Idempotency-Key`。
5. **设计 conversation UI**：
   * 在客服人员聊天界面中，创建基于消息 `type` 和 `data` 字段渲染消息卡片的机制。
   * 卡片上的可操作元素（按钮）应触发对后端操作处理器的调用。
6. **实施状态同步**：
   * Webhook endpoint 应解析传入事件并使用新的退货或取消状态更新本地数据库。
   * 使用实时通信渠道（例如 WebSockets）将这些更新推送到相关客服人员的 UI，确保卡片和状态信息始终是最新的。
7. **日志与审计**：
   * 记录每个 API 调用、其参数、响应以及任何关联的 `request_id`。
   * 记录每个传入的 Webhook 事件。这对于调试和审计整个售后工作流至关重要。

## 示例载荷
**发送订单卡片：**
```JSON
// POST /customer_service/202309/conversations/{conv_id}/messages
{
  "type": "ORDER_CARD",
  "content": "{\\"order_id\\":\\"576473917261320779\\"}"
}
```

**批准退货请求：**
```JSON
// POST /return_refund/202309/returns/4035319218955782461/approve
{
  "decision": "APPROVE_RETURN",
  "buyer_keep_item": false
}
```

## 端到端测试用例
**测试用例 1：全额退款（商品未收到）**

* **前提条件**：订单状态为 `IN_TRANSIT`。买家联系支持。
* **步骤**：
   1. 客服人员发送 `ORDER_CARD` 确认订单。
   1. 客服人员验证问题并决定退款。
   1. 客服人员使用 `Create Return` API 发起 `REFUND`。
   1. 客服人员立即使用 `Approve Return` API 批准，设置 `decision: APPROVE_REFUND`。
* **预期结果**：退货状态变为 `REQUEST_SUCCESS`。收到 Webhook。聊天中的卡片更新为"退款处理中"。

**测试用例 2：标准退货退款**

* **前提条件**：订单状态为 `DELIVERED`。买家想要退货。
* **步骤**：
   1. 客服人员发送 `RETURN_REFUND_CARD`。买家填写并提交。
   1. 客服人员在卡片上点击"批准"，调用 `Approve Return`（`decision: APPROVE_RETURN`）。
   1. （模拟）买家发货。收到 `BUYER_SHIPPED_ITEM` Webhook。
   1. 客服人员点击"确认收货"，调用 `Approve Return`（`decision: APPROVE_RECEIVED_PACKAGE`）。
* **预期结果**：状态从 `PENDING` -> `AWAITING_BUYER_SHIP` -> `BUYER_SHIPPED_ITEM` -> `REQUEST_SUCCESS` 推进。每次状态变更都在 UI 中反映。


**测试用例 3：拒绝无效退货请求**

* **前提条件**：订单已送达 30 天。买家以非质量原因申请退货。
* **步骤**：
   1. 客服人员检查资格，发现退货窗口已关闭。
   1. 客服人员发送 `TEXT` 消息说明政策。
   1. 如果买家坚持并创建请求，客服人员在卡片上点击"拒绝"。
   1. 客服人员选择原因（例如"超过退货期限"）并添加评论。
* **预期结果**：调用 `Reject Return` API。状态变为 `REQUEST_REJECTED`。卡片更新为最终的不可操作状态。

**测试用例 4：卖家发起的部分取消**

* **前提条件**：订单状态为 `AWAITING_SHIPMENT`。一件商品缺货。
* **步骤**：
   1. 客服人员通过 `TEXT` 消息通知买家。买家同意取消该商品。
   1. 客服人员使用调用 `Cancel Order` API 的 UI 功能，指定缺货商品的 `order_line_item_ids`。
* **预期结果**：创建取消记录。收到 `CANCELLATION_STATUS_CHANGED` Webhook。聊天中的 `ORDER_CARD` 更新为显示一件商品为"已取消"。
