# Developer Dashboard

# Dashboard 简介
Developer Dashboard 帮助开发者监控 TikTok Shop 对账检查发现的订单质量事件。它旨在回答三个问题：

1. 哪些订单已因超过发货 SLA 而被取消？
2. 哪些活跃订单有可能超过发货 SLA 或存在不一致的履约数据？
3. 哪个规则触发了每个事件，以便开发者修复集成并使用正确的原因关闭事件？

将此 Dashboard 与你的订单、履约和物流跟踪集成结合使用。目标是防止卖家收入损失、减少迟发取消，并保持良好的事件关闭率。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/6a2c9069067a46fc9dd43fa4c3aa5eae~tplv-k9wyc2ijk0-image.image)
# 如何使用 Dashboard

1. 优先查看 A-LOC 事件。这些订单已因超过发货 SLA 而被系统取消。
2. 在 SLA 到期之前查看风险订单事件。如果及时更正订单、履约或物流跟踪数据，这些订单可能仍可挽救。
3. 使用规则 ID 识别可能的集成问题。例如，缺少外部订单指向订单同步失败，而外部有物流跟踪但 TikTok Shop 中缺少则指向履约同步失败。
4. 在外部系统或集成工作流中修复根本原因。
5. 提交事件反馈并使用正确的原因码关闭事件。

# 集成边界
Quality Engine 是 TikTok Shop 的对账系统。开发者不直接操作对账逻辑。面向开发者的集成通过 Developer Dashboard、事件记录和 Quality Engine 数据交换 API 进行。
开发者负责保持外部平台数据与 TikTok Shop 对齐，包括：

* 订单创建和订单状态
* 包裹和履约状态
* 物流跟踪号和承运商更新
* 事件反馈和关闭原因

TikTok Shop 负责计算事件规则、暴露事件记录和展示 Dashboard 指标。有关 API 详情，请参阅 [Quality Engine 订单数据交换 API 文档](https://bytedance.sg.larkoffice.com/docx/A6qMdwPC5oESvkxLuffcAVMbnLc)。
# 术语
| 术语 | 含义 |
| --- | --- |
| TikTok Shop / TTS | TikTok Shop 订单和履约数据。 |
| 外部平台 / DTC 平台 | 接收 TikTok Shop 订单并处理下游履约的开发者、卖家、ERP、OMS、WMS 或 DTC 系统。 |
| Quality Engine | TikTok Shop 的对账系统，将 TikTok Shop 订单数据与外部平台数据进行比较，并展示面向开发者的事件。 |
| SLA | 服务等级协议。在此上下文中，指订单必须发货或更新的最晚时间。 |
| `shipping_due_time` | 订单的发货截止时间。如果订单在此截止时间前未发货或更新，可能会被系统取消。请参阅 [Orders API 中的 SLA 信息](https://partner.tiktokshop.com/docv2/page/sla-information-now-available-in-orders-api)。 |
| `tts_sla` | TikTok Shop 维护的 SLA 截止时间，用于风险订单规则。 |
| 物流跟踪号 | 存储在 TikTok Shop 或外部平台中的包裹物流跟踪号。 |
| `system_cancel_order_reason_shipping_timeout` | 当 TikTok Shop 因超过发货 SLA 而系统取消订单时使用的取消原因。 |
| FC-101 至 FC-105 | Quality Engine 原因码，用于在外部平台中因已识别原因未找到订单的情况。请在事件原因码文档中确认确切的原因定义。 |
| 事件关闭率 | 开发者已审核、解决并通过反馈关闭的事件百分比。 |
# 指标
## A-LOC 比率
A-LOC 代表 App Caused Late Dispatch（应用导致的迟发率）。它衡量因应用或集成问题导致超过发货 SLA 而被取消的 TikTok Shop 订单。
文本公式：
```Plain Text
A-LOC 比率 = A-LOC 订单数 / 所选时间段内符合条件的 TikTok Shop 订单数 * 100%
```

服务商目标：将 A-LOC 比率保持在 `0.01%` 以下。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/52b653121bf04dae9b2b53f4cb532447~tplv-k9wyc2ijk0-image.image)
## 风险订单比率
风险订单是可能超过发货 SLA 或在 TikTok Shop 与外部平台之间存在不一致的订单、履约或物流跟踪数据的活跃 TikTok Shop 订单。这些事件应在 SLA 到期之前处理。
文本公式：
```Plain Text
风险订单比率 = 风险订单事件数 / 所选时间段内千符合条件的 TikTok Shop 订单数 * 100%
```

如果 Dashboard 导出或 API 响应为某个指标提供了更具体的分母，请使用该来源返回的分母。
# A-LOC 事件统计
A-LOC 事件是已取消的订单。它们表明 TikTok Shop 在 `shipping_due_time` 之前未收到所需的发货更新，订单已被系统以 `system_cancel_order_reason_shipping_timeout` 原因取消。
A-LOC 规则表比较三个数据点：

* TikTok Shop 订单状态和取消原因
* 订单是否存在于外部平台中
* TikTok Shop 和外部平台中是否存在物流跟踪信息

| 规则 ID | TikTok Shop 订单状态 | TikTok Shop 取消原因 | TikTok Shop 物流跟踪号 | 外部平台订单状态 | 外部平台物流跟踪号 | 含义/可能的问题 |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | 已取消 | `system_cancel_order_reason_shipping_timeout` | 空 | 未找到订单 | 不适用 | 订单在创建或同步到外部平台之前就被取消了。检查订单接入和重试逻辑。 |
| A2 | 已取消 | `system_cancel_order_reason_shipping_timeout` | 空 | 订单存在 | 空 | 订单已到达外部平台，但在发货截止时间前没有可用的物流跟踪信息。检查履约处理。 |
| A3 | 已取消 | `system_cancel_order_reason_shipping_timeout` | 空 | 订单存在 | 有 | 外部平台有物流跟踪信息，但在超时之前未同步回 TikTok Shop。检查履约状态和物流跟踪同步。 |
| A4 | 已取消 | `system_cancel_order_reason_shipping_timeout` | 有 | 订单存在 | 有 | 双方都有物流跟踪信息，但订单仍被取消。检查更新时间、SLA 计算和跨系统数据一致性。 |
# 风险订单事件统计
风险订单事件是需要采取行动的活跃订单，以防止它们变成 A-LOC 取消。它们通常由缺少外部订单、缺少物流跟踪、物流跟踪同步延迟或 SLA 截止时间风险引起。
使用规则组确定行动优先级：

* R0、R5 和 R6：外部存在物流跟踪但 TikTok Shop 中缺失或未对齐。
* R1 和 R2：订单在外部平台中缺失。
* R3、R4 和 R7：订单接近或已超过其 SLA 阈值。

| 规则 ID | TikTok Shop 订单状态 | TikTok Shop 物流跟踪号 | 外部平台订单状态 | 外部平台物流跟踪号 | SLA 条件 | 含义/建议操作 |
| --- | --- | --- | --- | --- | --- | --- |
| R0 | On hold | 空 | 订单存在 | 有 | 不适用 | 外部有物流跟踪但 TikTok Shop 仍无物流跟踪。确认是否应将物流跟踪推送到 TikTok Shop。 |
| R1 | 等待发货 | 不适用 | 无相关订单 | 不适用 | Not-existing reason 为空或为 FC-101 至 FC-105 之一 | 订单在外部平台中缺失。检查订单同步失败以及 not-existing reason 是否有效。 |
| R2 | 部分发货 | 不适用 | 无相关订单 | 不适用 | Not-existing reason 为空或为 FC-101 至 FC-105 之一 | 部分发货订单在外部平台中缺失。检查部分履约和订单同步逻辑。 |
| R3 | 等待发货 | 空 | 订单存在 | 空 | 当前时间晚于 `tts_sla - 1 天`，且 `tts_sla` 不为 `0` | SLA 前剩余不到一天，且双方都没有物流跟踪。优先处理履约和物流跟踪创建。 |
| R4 | 部分发货 | 空 | 订单存在 | 空 | 当前时间晚于 `tts_sla - 1 天`，且 `tts_sla` 不为 `0` | 部分发货订单接近 SLA 且没有物流跟踪。优先处理剩余包裹的履约。 |
| R5 | 等待发货 | 空 | 订单存在 | 有 | 不适用 | 外部有物流跟踪但未同步到 TikTok Shop。推送物流跟踪并验证履约状态同步。 |
| R6 | 部分发货 | 空 | 订单存在 | 有 | 不适用 | 部分发货订单在外部有物流跟踪但 TikTok Shop 中缺失。检查包裹级别的物流跟踪同步。 |
| R7 | 等待揽收 | 有 | 订单存在 | 有 | 当前时间晚于 TikTok Shop 订单 SLA | 双方都有物流跟踪，但订单已超过预期的 SLA 进度。检查承运商交接、揽收状态和状态同步时间。 |
# 事件反馈和关闭流程
在修复根本原因后，在 Developer Dashboard 中或通过相关 Quality Engine 工作流提交事件反馈并关闭事件。
使用规则 ID、订单详情和根本原因选择正确的关闭原因。请参阅 [Quality Engine 事件原因码](https://partner.tiktokshop.com/docv2/page/660bf931cf5cc502e03007ca)参考文档。
# 开发者检查清单

* 确认所有 TikTok Shop 订单已及时创建在外部平台中。
* 确认履约和物流跟踪更新在 `shipping_due_time` 之前推送回 TikTok Shop。
* 每日监控风险订单事件，在它们变成 A-LOC 取消之前解决。
* 使用 A-LOC 事件进行根本原因分析和集成可靠性改进。
* 在补救后使用准确的反馈和原因码关闭事件。
