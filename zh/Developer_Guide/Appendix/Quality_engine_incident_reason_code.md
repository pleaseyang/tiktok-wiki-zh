# Quality Engine 事件原因码

# 概述
当你的应用需要通过 Quality Engine 订单数据交换 API 将 Quality Engine 事件原因同步到 TikTok Shop 时，请使用本页面。
Quality Engine 使用原因码来了解订单对账事件发生的原因。发送本页列出的原因码之一，将其与适用的规则 ID 匹配，并保持 enum 值与所列内容完全一致。不在列表中的原因码可能会被 Quality Engine 拒绝。
最后审核日期：2026 年 7 月 6 日，依据 Data Reconciliation OpenAPI 参考文档和 Developer Dashboard 规则表。
# 关键术语
| 术语 | 含义 |
| --- | --- |
| Quality Engine | TikTok Shop 的订单和履约对账系统。它将 TikTok Shop 的订单和履约数据与卖家同步或履行订单的外部平台进行比较。 |
| A-LOC | App Caused-Late Dispatch Rate TikTok Shipping Cancel Order Count。在 Developer Dashboard 中，A-LOC 事件是指因超过 `shipping_due_time` SLA 而被系统取消的 TikTok Shop 订单，取消原因为 `system_cancel_order_reason_shipping_timeout`。 |
| Risk Order（风险订单） | 由于 TikTok Shop 与外部平台之间的订单或履约数据不一致，可能导致无法按时完成 TikTok Shop 发货 SLA 的订单。 |
| Orphan Order（孤儿订单） | TikTok Shop 订单在 DTC 渠道或外部平台中没有相关订单的事件。 |
| Pre-RTS | 在本页面中，Pre-RTS 事件是指订单在 DTC 渠道中已发货或有物流跟踪信息，但对应的 TikTok Shop 订单尚未在 TikTok Shop 中发货或履约。RTS 指的是 ready-to-ship 履约阶段。 |
| DTC 渠道 | Direct-to-Consumer 渠道，例如 Shopify、WooCommerce、BigCommerce 或 Magento。在本页面中，"DTC 渠道"、"渠道平台"和"外部平台"均指卖家的外部商务系统。 |
| 4PL 连接器 | 四方物流连接器或履约集成，可以在卖家的履约系统与 TikTok Shop 之间交换订单、包裹、承运商或物流跟踪数据。 |
| TTS | TikTok Shop。在面向用户的文本中使用"TikTok Shop"，除非引用 API 字段或现有规则名称。 |
| `shipping_due_time` / `tts_sla` | TikTok Shop 的发货截止时间，Developer Dashboard 规则表用于检测 A-LOC 和风险订单事件。 |
# 规则对照
本页的原因码列表使用 [Developer Dashboard](https://partner.tiktokshop.com/docv2/page/developer-dashboard) 中的 R/A 规则 ID 体系。不应与某些 Dashboard 备注中仍保留的旧版 FC-101 至 FC-105 措辞混淆。
| 规则 ID | 事件类型 | Dashboard 定义 | 本页中的原因码类别 |
| --- | --- | --- | --- |
| [A1](https://partner.tiktokshop.com/docv2/page/developer-dashboard#a--loc-incident-statistics) | A-LOC | TikTok Shop 订单因发货超时而取消，且订单不存在或未发送至外部平台。 | Orphan Order |
| A2 | A-LOC | TikTok Shop 订单因发货超时而取消；订单存在于 DTC 渠道中，但 DTC 物流跟踪号为空。 | 当前原因码表未涵盖。请勿自行编造原因码。 |
| A3 | A-LOC | TikTok Shop 订单因发货超时而取消；订单存在于 DTC 渠道中且 DTC 物流跟踪号不为空。 | Pre-RTS |
| A4 | A-LOC | TikTok Shop 订单因发货超时而取消；TikTok Shop 和 DTC 的物流跟踪号均不为空。 | 当前原因码表未涵盖。请勿自行编造原因码。 |
| R0 | Risk Order | TikTok Shop 订单处于 on hold 状态；DTC 订单存在且有物流跟踪信息。 | 当前原因码表未涵盖。 |
| R1 | Risk Order | TikTok Shop 订单等待发货，且不存在相关 DTC 订单。 | Orphan Order |
| R2 | Risk Order | TikTok Shop 订单部分发货，且不存在相关 DTC 订单。 | Orphan Order |
| R3 / R4 | Risk Order | 针对等待发货或部分发货订单的短期内置规则，DTC 订单存在但在 SLA 截止时间附近物流跟踪号为空。 | 当前原因码表未涵盖。 |
| R5 | Risk Order | TikTok Shop 订单等待发货；DTC 订单存在且 DTC 物流跟踪号不为空。 | Pre-RTS |
| R6 | Risk Order | TikTok Shop 订单部分发货；DTC 订单存在且 DTC 物流跟踪号不为空。 | Pre-RTS |
| R7 | Risk Order | TikTok Shop 订单等待揽收；TikTok Shop 和 DTC 物流跟踪号在 TikTok Shop SLA 之后均不为空。 | 当前原因码表未涵盖。 |
Developer Dashboard 表格中的 FC-101 至 FC-105 仅作为旧版"Not Existing Reason"措辞保留。这些 FC 码未在本页列为有效原因码。除非 API 参考文档明确为你的应用版本列出了 FC-101 至 FC-105，否则不要在 `issue_reason` 中发送这些码。
# API 使用方法
使用 [Quality Factory Order Data Import API](https://partner.tiktokshop.com/docv2/page/quality-factory-order-data-import-api-202401) 同步订单数据和事件原因码。
| 项目 | 值 |
| --- | --- |
| 方法和路径 | `POST /data_reconciliation/202401/orders/import` |
| 查询参数 | 在需要店铺上下文时提供 `shop_cipher`。从已授权店铺数据中获取。 |
| 必需请求头 | `x-tts-access-token`、`Content-Type: application/json` |
| 原因码请求字段 | `orders[].issue_reason` |
| 原因码格式 | 大写 enum 字符串，与本页所列内容完全一致。 |
| 相关 API 文档 | [Quality Engine 订单数据交换 API](https://bytedance.sg.larkoffice.com/docx/A6qMdwPC5oESvkxLuffcAVMbnLc)、[原因码参考](https://partner.tiktokshop.com/docv2/page/660bf931cf5cc502e03007ca) |
版本说明：`POST /data_reconciliation/202309/orders/sync` 和 `POST /data_reconciliation/202310/orders/import` 使用 `orders[].not_exist_reason`。202401 API 使用 `orders[].issue_reason`。请使用你调用的 endpoint 版本对应的字段名。
最小请求示例：
```JSON
{
  "orders": [
    {
      "order_id": "7021436810468230477",
      "channel_type": "SHOPIFY",
      "channel_order_id": "8021436810468230477",
      "channel_order_status": "OPEN",
      "channel_financial_status": "PAID",
      "channel_fulfillment_status": "FULFILLED",
      "channel_order_update_time": "1692163668",
      "issue_reason": "SELLER_TIKTOKSHOP_AUTHORIZATION_REVOKED",
      "packages": [
        {
          "package_id": "RN141567632MY",
          "shipping_provider_name": "UPS",
          "tracking_number": "LX542261779US"
        }
      ]
    }
  ]
}
```

`channel_order_update_time` 是 DTC 渠道上的订单更新时间戳，而非 API 调用时间。它必须是 10 位 Unix 时间戳（以秒为单位），且必须早于当前时间戳。
# 原因码快速指南
| 原因类别 | 适用规则 | 原因码 | API 字段 |
| --- | --- | --- | --- |
| Orphan Order | R1 / R2 / A1 | 使用下方 Orphan Order 原因码表。 | `issue_reason` |
| Pre-RTS | A3 / R5 / R6 | 使用下方 Pre-RTS 原因码表。 | `issue_reason` |
# Orphan Order 原因码
当 DTC 渠道中没有相关订单时使用这些码。
| 原因类别 | 适用规则 | 原因码 | 描述 |
| --- | --- | --- | --- |
| Orphan Order | R1 / R2 / A1 | `SELLER_TIKTOKSHOP_AUTHORIZATION_REVOKED` | 卖家撤销了应用对 TikTok Shop 的授权。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_UNINSTALLED_DTC_APP` | 卖家从 DTC 渠道平台卸载了该应用。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_NOT_GRANT_DTC_PERMISSION` | 卖家未向应用授予相应的 DTC 渠道 API 权限。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_DTC_STORE_UNAVAILABLE` | 卖家的 DTC 渠道店铺不可用。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_TIKTOKSHOP_STORE_INACTIVE` | 卖家的 TikTok Shop 店铺处于非活跃状态。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_DTC_NO_SKU` | 未找到卖家 DTC 渠道产品的对应 SKU。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_DTC_ABNORMAL_PRODUCT_STATUS` | 卖家 DTC 渠道平台上的产品状态异常。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_DTC_PRODUCT_OUT_OF_STOCK` | 卖家 DTC 渠道平台上的产品缺货。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_TIKTOKSHOP_ORDER_AMOUNT_ZERO` | 卖家 TikTok Shop 订单中的订单金额为 0。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_APP_OWE_FEE` | 卖家使用了应用但未续费，或卖家配额已用完。 |
| Orphan Order | R1 / R2 / A1 | `SELLER_ABANDON_SYNC_TIKTOKSHOP_ORDER` | 卖家选择不同步 TikTok Shop 订单。 |
| Orphan Order | R1 / R2 / A1 | `APP_MISSED_WEBHOOK` | 应用错过了 TikTok Shop 订单 webhook。 |
| Orphan Order | R1 / R2 / A1 | `APP_ORDER_RETRIEVE_API_FAILED` | 应用通过调用 TikTok Shop API 检索订单失败。 |
| Orphan Order | R1 / R2 / A1 | `APP_ORDER_RETRIEVE_API_NOT_MATCH_DTC_FIELD` | 应用从 TikTok Shop API 检索的订单信息不完整或与 DTC 渠道字段映射不匹配。 |
| Orphan Order | R1 / R2 / A1 | `APP_CALL_DTC_CREATE_ORDER_API_FAILED` | 应用通过调用 DTC 渠道 API 创建订单失败。 |
| Orphan Order | R1 / R2 / A1 | `OTHER` | 仅在所列 Orphan Order 原因码均不匹配该事件时使用。 |
# Pre-RTS 原因码
当订单在 DTC 渠道中已发货但在 TikTok Shop 中未发货时使用这些码。
| 原因类别 | 适用规则 | 原因码 | 描述 |
| --- | --- | --- | --- |
| Pre-RTS | A3 / R5 / R6 | `INVALID_TRACKING_NUMBER` | DTC 渠道中输入了无效的物流跟踪号。示例：物流跟踪号包含多余的空格或制表符，或物流跟踪号不正确但被 DTC 渠道接受。TikTok Shop 拒绝此履约。 |
| Pre-RTS | A3 / R5 / R6 | `UNSUPPORTED_CARRIER_TRACKING_NUMBER` | 承运商被 DTC 渠道支持但不被 TikTok Shop 支持。TikTok Shop 拒绝此履约。 |
| Pre-RTS | A3 / R5 / R6 | `ORDER_NOT_ELIGIBLE_FOR_FULFILLMENT` | 包裹在 DTC 渠道中已发货但未在 TikTok Shop 中发货，因为 TikTok Shop 对该订单有取消或退款请求。TikTok Shop 拒绝此履约。 |
| Pre-RTS | A3 / R5 / R6 | `FULFILL_UNIT_OR_ORDER_NUMBER_NOT_COMBINED_CORRECTLY` | 包裹或订单履约调用 TikTok Shop 失败，因为物流跟踪号被用于另一个订单且未正确合并订单。 |
| Pre-RTS | A3 / R5 / R6 | `FULFILL_UNIT_OR_ORDER_NUMBER_NOT_FOUND` | 包裹或订单履约调用 TikTok Shop 失败，因为卖家在履约前在 TikTok Shop 或 DTC 渠道中合并或拆分了订单。TikTok Shop 拒绝此履约。 |
| Pre-RTS | A3 / R5 / R6 | `FULFILLMENT_FAILURE_DUE_TO_RATE_LIMIT` | 包裹或订单履约调用 TikTok Shop 失败，因为应用超出了速率限制且未进行重试。 |
| Pre-RTS | A3 / R5 / R6 | `FULFILLMENT_FAILURE_DUE_TO_NO_RETRY_LOGIC` | 应用调用了订单履约，但 TikTok Shop 返回了临时内部错误且应用未进行重试。 |
| Pre-RTS | A3 / R5 / R6 | `FULFILLMENT_FAILURE_DUE_TO_NO_API_CALL` | 连接器应用未对此订单进行订单履约调用。 |
当前 Pre-RTS 列表未定义 `OTHER` 码。除非较新的 endpoint 参考文档明确添加了该码，否则不要为 Pre-RTS 事件发送 `OTHER`。如果某个事件不匹配任何已列出的 Pre-RTS 原因码，请通过最新的 Quality Engine 规则定义或 Partner Center 支持确认预期的原因码。
# 验证清单
在同步原因码之前：

1. 确认事件类别：Orphan Order 或 Pre-RTS。
2. 确认 Developer Dashboard 中的规则 ID：Orphan Order 对应 R1 / R2 / A1，Pre-RTS 对应 A3 / R5 / R6。
3. 从相应表格中选择最具体的原因码。
4. 对于 202401 API，按照 `orders[].issue_reason` 中所列内容完全一致地发送原因码。
5. 不要发送 FC-101 至 FC-105、小写 enum 值或来自其他类别的原因码，除非 endpoint 参考文档明确支持。

# 相关页面
| 页面 | 用途 |
| --- | --- |
| [Developer Dashboard](https://partner.tiktokshop.com/docv2/page/developer-dashboard) | A-LOC 和风险订单事件的规则定义。 |
| [Quality Engine 订单数据交换 API](https://bytedance.sg.larkoffice.com/docx/A6qMdwPC5oESvkxLuffcAVMbnLc) | 与 Quality Engine 交换订单数据的 API 级别集成指南。 |
| [Quality Factory Order Data Import API 202401](https://partner.tiktokshop.com/docv2/page/quality-factory-order-data-import-api-202401) | `POST /data_reconciliation/202401/orders/import` 的 endpoint 参考文档。 |
| [原因码参考](https://partner.tiktokshop.com/docv2/page/660bf931cf5cc502e03007ca) | 已发布的原因码页面。 |
| [Order API 概述](https://partner.tiktokshop.com/docv2/page/order-api-overview) | 对账中使用的 TikTok Shop 订单数据。 |
| [Fulfillment API 概述](https://partner.tiktokshop.com/docv2/page/fulfillment-api-overview) | 对账中使用的 TikTok Shop 履约数据。 |
| [shipping_due_time SLA 参考](https://partner.tiktokshop.com/docv2/page/sla-information-now-available-in-orders-api) | Quality Engine 和 Developer Dashboard 事件使用的 SLA 字段。 |
