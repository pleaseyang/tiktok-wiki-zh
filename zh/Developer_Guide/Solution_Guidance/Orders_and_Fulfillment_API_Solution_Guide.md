# 订单与履约 API 解决方案指南

本文档是作为外部物流合作伙伴（包括 3PL 仓库运营商、4PL 协调方或 ISV）集成 TikTok Shop 订单与履约功能的指南。
它涵盖一个领域：接收和履行订单。包括订单同步、订单生命周期、两种物流模式下的面单购买和发货报告、多包裹订单，以及平台驱动的包裹集重组。
从这里开始，找到与你问题匹配的文档，然后深入阅读。本页面本身不包含技术细节。
# 文档列表
| **文档** | **受众** | **涵盖内容** |
| --- | --- | --- |
| [订单同步指南](https://bytedance.us.larkoffice.com/docx/GTgMdfok5oXd4fxLqQNucRAgs7d) | 工程团队 <br/>  | 订单如何到达你：Mode A（webhook + 轮询）和 Mode B（仅轮询），订单记录和状态生命周期（包括 ON_HOLD 窗口），对账扫描，以及存储每个订单并标记为待履行状态的步骤。请首先阅读。 |
| [履约指南](https://bytedance.us.larkoffice.com/docx/FYBrdmGO4oUr0ux2tjAu8BY4s3c) | 工程团队 <br/>  | 收到待处理订单后你需要做什么：两条端到端履约通道——Lane A TikTok Shipping（4PL）和 Lane B 卖家 Shipping（3PL），发货计划，平台对包裹集的重组，包裹合并，包裹状态参考，以及履约错误码。 |
| [市场变体（配套指南）](https://bytedance.us.larkoffice.com/docx/RLORdDtEyom8HLxDCXEu5aLMszg) | 工程团队 | 与默认流程不同的内容：东南亚和拉美地区的交接与发货报告，发货前合并，巴西发票上传，以及英国注意事项。每个章节都会注明它所替代的指南步骤。 |
| [利益相关方概览](https://bytedance.us.larkoffice.com/docx/Z5f8dYDBcoqdzvxPTLHuVMKnsUc) | 解决方案架构师、业务方、商务方 | 非技术视角：用通俗语言详细介绍两种履约模式，按能力分组的 API 接入清单，分阶段工作量框架，以及影响运营的一些业务规则。没有 payload，没有复杂图表。 |
# 我应该从哪个指南开始？
两个指南按方向划分一个集成。订单同步指南负责将信息从 TikTok Shop 传递给你：它以两种模式之一接收订单、存储订单并标记为待处理。履约指南负责将信息从你传递回 TikTok Shop：它通过两条通道之一发货。两者都描述了美国、英国、EMEA 和日本的默认流程；其他市场请参阅市场变体指南。
从**订单同步指南**开始。如果你可以托管公共 HTTPS endpoint，请构建 Mode A：webhook 是主要触发方式，步骤 1.5 到 1.8 添加了每个 webhook 集成都需要的对账扫描作为安全网。
如果入站 HTTPS 不可行——例如由于网络策略、缺少公共 endpoint 或面向批处理的中间件——请改为构建同一指南的 Mode B：一个具有自身操作规范的纯拉取引擎。然后继续阅读**履约指南**，两种模式共用同一份履约指南。
为一个模式完成的工作可以复用到另一个模式。
# 读者路径
| **如果你需要...** | **请前往** |
| --- | --- |
| 在 Mode A（webhook + 轮询）和 Mode B（仅轮询）之间做选择 | 订单同步指南："同步策略：选择你的模式" |
| 了解 3PL 与 4PL 以及订单属于哪条通道 | 履约指南："履约模式：3PL 与 4PL" |
| 查看订单生命周期、ON_HOLD 窗口以及值得存储的订单数据 | 订单同步指南："订单数据与状态生命周期" |
| 端到端实现履约流程 | 履约指南：第 1 和第 2 部分 |
| 构建轮询引擎（扫描、游标、确认） | 订单同步指南：第 2 部分（Mode B） |
| 检测并处理平台对包裹集的重组 | 履约指南：第 3 部分 |
| 将多个订单合并为一个包裹，或使用拆单功能预先拆分 | 履约指南："相邻能力" |
| 在东南亚、拉美或巴西发货，或查看英国差异 | [市场变体指南](https://bytedance.us.larkoffice.com/docx/RLORdDtEyom8HLxDCXEu5aLMszg) |
| 查找 endpoint、method 或路径 | 任一指南："附录 A - Endpoint 索引"（订单同步中查找订单 endpoint，履约中查找履约和物流 endpoint） |
| 实现 webhook 接收、签名验证和重试处理 | 订单同步指南："附录 B - Webhook 交付契约和主题" |
| 查找轮询上限、过滤器和窗口语义 | 订单同步指南："附录 C - 轮询参考卡" |
| 处理 rate limit 和错误码 | 任一指南："Rate Limits 和 Errors" |
| 在上线前规划验证 | 任一指南："建议的上线前验证" |
| 为非技术受众评估集成范围 | [利益相关方概览](https://bytedance.us.larkoffice.com/docx/Z5f8dYDBcoqdzvxPTLHuVMKnsUc) |
| 在上线前设置沙盒店铺和测试卖家账号 | TikTok Partner Center：[测试你的 App](https://partner.tiktokshop.com/docv2/page/64f1998564ed2e0295f3d87d)、[创建测试卖家账号](https://partner.tiktokshop.com/docv2/page/686da7797cac2a04985d83a1) |
# 范围与相邻领域
本中心仅涵盖**订单与履约**领域。
两个相邻领域在其他地方管理：

* **合作伙伴接入** — Partner Center 应用创建、卖家授权、token 生命周期和请求签名由接入领域负责。
* **逆向流程** — 取消、退货和退款由逆向领域负责。当这些指南涉及逆向流程时，会指向配套的**RMA/退货设计**。

随着更多领域上线，本中心可以为每个领域扩展专属章节。
