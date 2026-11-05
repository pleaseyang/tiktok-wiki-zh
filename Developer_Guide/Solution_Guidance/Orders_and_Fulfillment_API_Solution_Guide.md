# Orders and Fulfillment API Solution Guide

This document is a guide for integrating TikTok Shop orders and fulfillment as an external logistics partner, including a 3PL warehouse operator, 4PL orchestrator, or ISV building on their behalf.
It covers one domain: receiving and fulfilling orders. This includes order sync, the order lifecycle, label purchase and shipment reporting across both shipping models, multi-shipment orders, and platform-driven re-shapes of the package set.
Start here, find the document that matches your question, and go deeper there. This page contains no technical details of its own.
# The Documents
| **Document** | **Audience** | **What it covers** |
| --- | --- | --- |
| [Order Sync guide](https://bytedance.us.larkoffice.com/docx/GTgMdfok5oXd4fxLqQNucRAgs7d) | Engineering <br/>  | How orders reach you: Mode A (webhook plus poll) and Mode B (poll only), the order record and status lifecycle with the ON_HOLD window, the reconciliation sweep, and the step that stores each order and marks it ready for fulfillment. Read it first. |
| [Fulfillment guide](https://bytedance.us.larkoffice.com/docx/FYBrdmGO4oUr0ux2tjAu8BY4s3c) | Engineering <br/>  | What you do with a ready order: both fulfillment lanes end to end, Lane A TikTok Shipping (4PL) and Lane B Seller Shipping (3PL), shipment planning, platform re-shapes of the package set, package consolidation, the package state reference, and the fulfillment error codes. |
| [Market Variants (companion guide)](https://bytedance.us.larkoffice.com/docx/RLORdDtEyom8HLxDCXEu5aLMszg) | Engineering | What changes outside the default flow: SEA and LATAM handover and shipment reporting, pre-shipping consolidation, the Brazil invoice upload, and UK notes. Each section names the guide step it replaces. |
| [Stakeholder overview](https://bytedance.us.larkoffice.com/docx/Z5f8dYDBcoqdzvxPTLHuVMKnsUc) | Solution architects, business, commercial | The non-technical view: it provides details of the two fulfillment models in plain words, the API onboarding inventory grouped by capability, phased effort framing, and the handful of business rules that affect operations. No payloads, no dense diagrams. |
# Which Guide Do I Start With?
The two guides split one integration by direction. The Order Sync guide moves information from TikTok Shop to you: it receives orders in one of two modes, stores them, and marks them ready. The Fulfillment guide moves information from you to TikTok Shop: it ships ready orders through one of two lanes. Both describe the default flow for the US, UK, EMEA and JP; the Market Variants guide covers the other markets.
Start with the **Order Sync guide**. If you can host a public HTTPS endpoint, build Mode A: webhooks are the primary trigger, and Steps 1.5 to 1.8 add the reconciliation sweep that every webhook integration needs as a safety net.
If inbound HTTPS is impractical - for example, because of network policy, the lack of a public endpoint, or batch-oriented middleware - build Mode B of the same guide instead: a pull-only engine with its own operational disciplines. Then continue with the **Fulfillment guide**, which is the same for both modes.
Work completed for one mode carries over to the other.
# Reader Paths
| **If you need to...** | **Go to** |
| --- | --- |
| Decide between Mode A (webhook plus poll) and Mode B (poll only) | Order Sync guide: "Sync Strategy: Select Your Mode" |
| Understand 3PL vs 4PL and which lane an order is in | Fulfillment guide: "Fulfillment Models: 3PL vs 4PL" |
| See the order lifecycle, the ON_HOLD window, and the order data worth storing | Order Sync guide: "Order Data and the Status Lifecycle" |
| Implement the fulfillment flow end to end | Fulfillment guide: Parts 1 and 2 |
| Build the polling engine (sweeps, cursors, acknowledgments) | Order Sync guide: Part 2 (Mode B) |
| Detect and absorb platform re-shapes of the package set | Fulfillment guide: Part 3 |
| Combine orders into one package, or pre-split with Split Orders | Fulfillment guide: "Adjacent Capabilities" |
| Ship in SEA, LATAM or Brazil, or check UK differences | [Market Variants guide](https://bytedance.us.larkoffice.com/docx/RLORdDtEyom8HLxDCXEu5aLMszg) |
| Look up an endpoint, method, or path | Either guide: "Appendix A - Endpoint Index" (order endpoints in Order Sync, fulfillment and logistics endpoints in Fulfillment) |
| Implement webhook receipt, signature verification, and retry handling | Order Sync guide: "Appendix B - Webhook Delivery Contract and Topics" |
| Look up poll caps, filters, and window semantics | Order Sync guide: "Appendix C - Polling Reference Card" |
| Handle rate limits and error codes | Either guide: "Rate Limits and Errors" |
| Plan validation before go-live | Either guide: "Suggested Validation Before Go-Live" |
| Scope the integration for a non-technical audience | [Stakeholder overview](https://bytedance.us.larkoffice.com/docx/Z5f8dYDBcoqdzvxPTLHuVMKnsUc) |
| Set up a sandbox shop and a test seller account before go-live | TikTok Partner Center: [Test your App](https://partner.tiktokshop.com/docv2/page/64f1998564ed2e0295f3d87d), [Create a test seller account](https://partner.tiktokshop.com/docv2/page/686da7797cac2a04985d83a1) |
# Scope and Adjacent Domains
This hub covers the **orders and fulfillment** domain only.
Two adjacent domains are managed elsewhere:

* **Partner onboarding** — Partner Center app creation, seller authorization, token lifecycle, and request signing are owned by the onboarding domain.
* **Reverse flows** — Cancellations, returns, and refunds are owned by the reverse domain. Where these guides touch on those flows, they point to the companion **RMA/returns design**.

As additional domains come online, this hub can expand with a dedicated section for each domain.
