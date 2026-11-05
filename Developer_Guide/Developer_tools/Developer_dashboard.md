# Developer dashboard

# What this dashboard is
The Developer Dashboard helps developers monitor order-quality incidents found by TikTok Shop reconciliation checks. It is intended to answer three questions:

1. Which orders have already been cancelled because the shipping SLA was missed?
2. Which active orders are at risk of missing the shipping SLA or have inconsistent fulfillment data?
3. Which rule triggered each incident, so the developer can repair the integration and close the incident with the correct reason?

Use this dashboard together with your order, fulfillment, and tracking integrations. The goal is to prevent seller revenue loss, reduce late-dispatch cancellations, and keep incident close rate healthy.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/6a2c9069067a46fc9dd43fa4c3aa5eae~tplv-k9wyc2ijk0-image.image)
# How to use the dashboard

1. Review A-LOC incidents first. These orders have already been system-cancelled because the shipping SLA was missed.
2. Review Risk Order incidents before the SLA expires. These orders may still be recoverable if the order, fulfillment, or tracking data is corrected in time.
3. Use the rule ID to identify the likely integration issue. For example, a missing external order points to order-sync failure, while tracking present externally but missing in TikTok Shop points to fulfillment-sync failure.
4. Fix the root cause in the external system or integration workflow.
5. Submit incident feedback and close the incident with the correct reason code.

# Integration boundary
Quality Engine is TikTok Shop's reconciliation system. Developers do not operate the reconciliation logic directly. Developer-facing integration happens through the Developer Dashboard, incident records, and Quality Engine data exchange APIs.
Developers are responsible for keeping the external platform data aligned with TikTok Shop, including:

* order creation and order status
* package and fulfillment status
* tracking number and carrier updates
* incident feedback and closure reason

TikTok Shop is responsible for calculating incident rules, exposing incident records, and showing dashboard metrics. For API details, refer to the [Quality Engine Order Data Exchange API documentation](https://bytedance.sg.larkoffice.com/docx/A6qMdwPC5oESvkxLuffcAVMbnLc).
# Terminology
| Term | Meaning |
| --- | --- |
| TikTok Shop / TTS | TikTok Shop order and fulfillment data. |
| External platform / DTC platform | The developer, merchant, ERP, OMS, WMS, or DTC system that receives TikTok Shop orders and handles downstream fulfillment. |
| Quality Engine | TikTok Shop's reconciliation system that compares TikTok Shop order data with external platform data and surfaces developer-facing incidents. |
| SLA | Service level agreement. In this context, it is the latest time by which an order must be shipped or updated. |
| `shipping_due_time` | The shipping deadline for an order. If the order is not shipped or updated before this deadline, it may be cancelled by the system. See [SLA information in Orders API](https://partner.tiktokshop.com/docv2/page/sla-information-now-available-in-orders-api). |
| `tts_sla` | The SLA deadline maintained by TikTok Shop and used in risk-order rules. |
| Tracking number | The package tracking number stored in TikTok Shop or in the external platform. |
| `system_cancel_order_reason_shipping_timeout` | Cancellation reason used when TikTok Shop system-cancels an order because the shipping SLA was missed. |
| FC-101 to FC-105 | Quality Engine reason codes used when an order is not found in the external platform for a recognized reason. Confirm the exact reason definition in the incident reason-code documentation. |
| Incident close rate | The percentage of incidents that the developer has reviewed, resolved, and closed with feedback. |
# Metrics
## A-LOC rate
A-LOC stands for App Caused Late Dispatch. It measures TikTok Shop orders that were cancelled because the shipping SLA was missed due to an app or integration issue.
Text formula:
```Plain Text
A-LOC rate = A-LOC order count / eligible TikTok Shop order count in the selected period * 100%
```

Partner target: keep A-LOC rate below `0.01%`.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/52b653121bf04dae9b2b53f4cb532447~tplv-k9wyc2ijk0-image.image)
## Risk Order rate
Risk Orders are active TikTok Shop orders that may miss the shipping SLA or have inconsistent order, fulfillment, or tracking data between TikTok Shop and the external platform. These incidents should be handled before the SLA expires.
Text formula:
```Plain Text
Risk Order rate = Risk Order incident count / eligible TikTok Shop order count in the selected period * 100%
```

If a dashboard export or API response provides a more specific denominator for a metric, use the denominator returned by that source.
# A-LOC incident statistics
A-LOC incidents are already cancelled orders. They indicate that TikTok Shop did not receive the required shipping update before `shipping_due_time`, and the order was system-cancelled with `system_cancel_order_reason_shipping_timeout`.
The A-LOC rule table compares three data points:

* TikTok Shop order status and cancellation reason
* whether the order exists in the external platform
* whether tracking exists in TikTok Shop and in the external platform

| Rule ID | TikTok Shop order status | TikTok Shop cancel reason | TikTok Shop tracking number | External platform order status | External platform tracking number | Meaning / likely issue |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Cancelled | `system_cancel_order_reason_shipping_timeout` | Empty | Order not found | N/A | The order was cancelled before it was created or synced to the external platform. Check order ingestion and retry logic. |
| A2 | Cancelled | `system_cancel_order_reason_shipping_timeout` | Empty | Order exists | Empty | The order reached the external platform, but no tracking was available before the shipping deadline. Check fulfillment processing. |
| A3 | Cancelled | `system_cancel_order_reason_shipping_timeout` | Empty | Order exists | Present | The external platform had tracking, but tracking was not synced back to TikTok Shop before timeout. Check fulfillment-status and tracking sync. |
| A4 | Cancelled | `system_cancel_order_reason_shipping_timeout` | Present | Order exists | Present | Both sides have tracking, but the order was still cancelled. Check update timing, SLA calculation, and data consistency across systems. |
# Risk Order incident statistics
Risk Order incidents are active orders that need action before they become A-LOC cancellations. They are usually caused by missing external orders, missing tracking, tracking-sync delay, or SLA deadline risk.
Use the rule group to prioritize action:

* R0, R5, and R6: tracking exists externally but is missing or not aligned in TikTok Shop.
* R1 and R2: the order is missing in the external platform.
* R3, R4, and R7: the order is close to or past its SLA threshold.

| Rule ID | TikTok Shop order status | TikTok Shop tracking number | External platform order status | External platform tracking number | SLA condition | Meaning / recommended action |
| --- | --- | --- | --- | --- | --- | --- |
| R0 | On hold | Empty | Order exists | Present | N/A | External tracking exists while TikTok Shop still has no tracking. Confirm whether tracking should be pushed to TikTok Shop. |
| R1 | Awaiting shipment | N/A | No related order | N/A | Not-existing reason is empty or one of FC-101 to FC-105 | The order is missing in the external platform. Check order-sync failures and whether the not-existing reason is valid. |
| R2 | Partially shipping | N/A | No related order | N/A | Not-existing reason is empty or one of FC-101 to FC-105 | A partial-shipment order is missing in the external platform. Check partial fulfillment and order-sync logic. |
| R3 | Awaiting shipment | Empty | Order exists | Empty | Current time is later than `tts_sla - 1 day`, and `tts_sla` is not `0` | Less than one day remains before SLA, and no tracking exists on either side. Prioritize fulfillment and tracking creation. |
| R4 | Partially shipping | Empty | Order exists | Empty | Current time is later than `tts_sla - 1 day`, and `tts_sla` is not `0` | A partially shipped order is close to SLA and has no tracking. Prioritize remaining package fulfillment. |
| R5 | Awaiting shipment | Empty | Order exists | Present | N/A | External tracking exists but was not synced to TikTok Shop. Push tracking and verify fulfillment-status sync. |
| R6 | Partially shipping | Empty | Order exists | Present | N/A | External tracking exists for a partially shipped order but is missing in TikTok Shop. Check package-level tracking sync. |
| R7 | Awaiting collection | Present | Order exists | Present | Current time is later than the TikTok Shop order SLA | Tracking exists on both sides, but the order has missed the expected SLA progress. Check carrier handoff, collection status, and status-sync timing. |
# Incident feedback and close process
After fixing the root cause, submit incident feedback and close the incident in the Developer Dashboard or through the relevant Quality Engine workflow.
Use the rule ID, order details, and root cause to select the correct close reason. See the [Quality Engine Incident Reason Code](https://partner.tiktokshop.com/docv2/page/660bf931cf5cc502e03007ca) reference.
# Developer checklist

* Confirm that all TikTok Shop orders are created in the external platform on time.
* Confirm that fulfillment and tracking updates are pushed back to TikTok Shop before `shipping_due_time`.
* Monitor Risk Order incidents daily and resolve them before they become A-LOC cancellations.
* Use A-LOC incidents for root-cause analysis and integration reliability improvements.
* Close incidents with accurate feedback and reason codes after remediation.
