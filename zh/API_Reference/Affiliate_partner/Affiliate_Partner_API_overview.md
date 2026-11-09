# Affiliate Partner API 概览

<div style="border: #fed4a4 solid 1px; background-color: #fff5eb; border-style: solid; padding: 1px 10px; border-radius: 10px;">
<p>📌 <b>注意</b>：Affiliate API 目前在<b>英国</b>和<b>欧盟</b>市场<b>不可</b>用。
</p>
<p>应用只能使用其所属类别可用的 API 权限范围。要使用 Affiliate API，请打开该 API 的文档页面，点击底部的<b>View app categories</b>，查看哪些类别支持您的注册地区和目标市场。然后在支持的类别下创建应用。如果没有显示结果，则表示该 API 尚未在所选地区或市场开放。
</p>
</div>

# 背景
开发合作伙伴可以通过集成 TikTok Shop Affiliate API，帮助 TikTok Shop 的利益相关方在 TikTok Shop Affiliate 协作和合作伙伴活动中进行创建、管理、匹配、追踪、变现和协作。在 TikTok Shop App Store 中上架集成了 Affiliate API 的应用，将为开发合作伙伴带来诸多优势：

* **支持现有客户**：满足并支持已经在使用 TikTok Shop 或即将加入的现有客户。
* **增加曝光度**：在 App Store 中获取正在寻找 affiliate 解决方案的 TikTok Shop 卖家的关注。
* **营销机会**：受益于与 TikTok Shop App Store 相关的营销活动。
* **竞争优势**：与未集成 TikTok Shop 的竞争对手形成差异化。
* **增强收入生成**：提供下游可衡量的解决方案，专注于效果和收入生成，而不仅仅是上游的知名度和互动营销。


---


## Affiliate API 的类型
Affiliate 管理共有 3 种类型的 API：

* **Affiliate 卖家 API**：帮助卖家通过开放和定向的 TikTok Shop Creator Affiliate 协作来最大化商品曝光，促进无缝商品推广，并追踪其 affiliate 营销活动的整体转化。
* **Affiliate 达人 API**：帮助 TikTok Shop Creator Affiliate 管理其在 TikTok Shop 上的协作和商品展示，同时追踪其营销活动的转化效果。
* **Affiliate Partner API**：帮助 TikTok Affiliate Partner (TAP) 有效管理将卖家与 TikTok Shop Creator Affiliate 进行匹配的活动，为卖家优化商品推广，同时为 TikTok Shop Creator Affiliate 提供更多变现机会。


开发合作伙伴可以组合使用这些 API 来：

* 将卖家商品目录注册到开放协作中
* 创建开放协作
* 创建定向协作
* 创建合作伙伴活动
* 帮助卖家寻找达人
* 以及更多..。


---


# 重要概念
## TikTok Shop Affiliate 计划
TikTok Shop Affiliate 计划由 **Affiliate Collaboration** 和 **Affiliate Partner 活动** 组成，两者都允许卖家和 TikTok Shop Creator Affiliate 基于 TikTok 上的互动购物内容进行协作，共同构建社交电商的下一个时代。


* **TikTok Shop Creator Affiliate** 是有资格在 TikTok Shop 上销售电商商品的达人。要获得资格，达人需要满足以下要求：
   * 在美国、英国和东南亚注册
   * 美国：1K+ 粉丝
   * 英国、东南亚：5K+ 粉丝
   * 18 岁以上
   * 账户违规不超过 3 次

 达人可以在此[申请](https://business.tiktokshop.com/us/creator/)加入 affiliate 计划。
（此后，TikTok Shop Creator Affiliate 将统称为达人。）

<div style="border: #fed4a4 solid 1px; background-color: #fff5eb; border-style: solid; padding: 1px 10px; border-radius: 10px;">
<p>📌 <b>注意</b>：目前外部合作伙伴无法以编程方式帮助达人入驻或审核。我们将在未来的迭代中改进此功能，但目前您可以通过以下 2 种方式检查达人是否为 TikTok Shop Creator Affiliate：

* 达人的个人资料上有"橱窗"图标
* 达人能够成功授权合作伙伴

</p>
<p>请注意，TikTok Shop Creator 授权目前与 TikTok for Business 或 TikTok for Developers 是分开的。
</p>
</div>
<br/>


* 在 TikTok Shop 的语境中，**可购物内容**指的是达人创建的互动 TikTok 视频，他们在视频中标记卖家商品并嵌入原生锚点链接，允许最终用户直接在达人的内容上进行购物。基于可购物内容的电商的关键特征：
   * 与传统电商 affiliate（链接、优惠码、社交媒体跳转）不同，这种类型的内容消除了归因和 cookie 有效期的问题，因为用户无需离开应用即可完成互动和购买。
   * 它实现了直接且基于效果的变现模式，消除了传统营销方法中常见的模糊性。达人通过直接推动的购买（无浏览归因）赚取佣金（由卖家决定），而卖家在扣除税费后从销售中获得剩余收益。


<div style="border:#bacefd solid 1px; background-color: #f0f4ff; border-style: solid; padding: 1px 10px; border-radius: 10px;">
<p>💡<b>这对利益相关方意味着什么？</b>

* **买家**（TikTok App 用户）通过受信赖的达人接触商品，并享受直接的购买路径。
* **卖家**受益于通过达人制作的互动 TikTok 风格可购物内容和按效果付费的模式，无需大量前期成本。
* **达人**受益于基于效果的高潜力报酬以及与卖家多样化的协作推广商品的机会。

</p>
</div>

---


## Affiliate Collaboration
通过 affiliate 变现的最基本方式之一是卖家和达人之间的直接 affiliate 协作。TikTok Shop Affiliate 计划中有 2 种协作模式：

* **开放协作 (Open Collaboration)**
   开放协作是指卖家将商品注册到开放计划中，使**商品对所有 TikTok Shop Creator Affiliate 可见**，可在 Creator Marketplace 上查看。
   您可以将开放协作想象为一个对达人开放的俱乐部，唯一的要求是达人已注册并被批准为 TikTok Shop Creator Affiliate。
   在某些情况下，卖家可以要求对开放协作进行审批。这意味着开放协作对达人可见，但他们必须申请并通过卖家审批才能参与。您可以将其想象为俱乐部门卫对派对参与者进行快速审核。

* **定向协作 (Target Collaboration)**
   定向协作是指卖家将商品注册到定向计划中，使**商品仅对被卖家明确邀请的 TikTok Shop Creator Affiliate 可见**。
   您可以将定向协作想象为一个仅限邀请的俱乐部。达人只有在被卖家邀请后才能进入俱乐部。进入后，达人必须遵守俱乐部的规则，并且可以随时被移除。
   定向协作是卖家在 TikTok 上寻找适合其独特风格的达人的绝佳方式，通常涉及那些通过历史表现证明自己或拥有强大内容组合的达人，通常带有更高的佣金率。


<div style="border:#bacefd solid 1px; background-color: #f0f4ff; border-style: solid; padding: 1px 10px; border-radius: 10px;">
<p>💡<b>这对利益相关方意味着什么？</b>
开发合作伙伴可以通过向卖家或达人收取 SaaS 费用，或通过与卖家或达人直接在 TikTok Shop 平台之外从匹配工作中抽取分成来利用这些协作。
</p>
</div>

---


## Affiliate Partner 活动
Affiliate Partner 活动是一种协作模式，其中 TikTok Affiliate Partner (TAP) 帮助卖家和达人更高效地进行匹配。这种模式与传统 affiliate 营销领域的子 affiliate 非常相似，TAP 充当子 affiliate，将最合适的达人推荐给卖家。
延续上面关于俱乐部的类比，您可以将 TAP 想象为俱乐部推广人——一个知道哪个俱乐部最适合谁的人。俱乐部推广人对当地俱乐部场景有敏锐的感知，包括年龄群体、DJ、音乐类型、趋势和整体氛围。
在 TikTok Shop 的语境中，TAP 可以推荐病毒式 TikTok 趋势、商品，并帮助卖家和达人在社交电商时代成功创建内容。TAP 计划的一些示例包括达人变现应用、达人或影响者营销平台、子 affiliate 等。

Affiliate Partner 活动的性质因地区略有不同。

* **美国/EMEA**：一(TAP)对一(卖家)的活动是常态。这与开放或定向协作没有区别，只是 TAP 促进了匹配过程，从而从佣金中抽取分成。您可以将 TAP 视为一个子 affiliate 网络。



* **其他地区**：一对多的活动是常态。TAP 通常设计的活动允许在一个更广泛的活动计划下与多个 TikTok Shop 卖家和达人协作。这些活动旨在支持 TAP 同时服务多个品牌，并在佣金结构方面提供灵活性：
   * 支持第三方佣金分成（销售后同时向 TAP 和达人支付）
   * 围绕佣金的不同自定义杠杆

尽管存在差异，佣金分成是所有 Affiliate Partner 活动的通用特性。这是 TAP 变现其工作的关键。


<div style="border:#bacefd solid 1px; background-color: #f0f4ff; border-style: solid; padding: 1px 10px; border-radius: 10px;">
<p>💡<b>这对利益相关方意味着什么？</b>
已启用 API 的 TikTok Affiliate Partner (TAP) 现在可以通过使用这些 API 以自动化方式高效管理 Affiliate Partner 活动。
本质上，Affiliate Partner 活动的功能类似于开放或定向协作，只是 TAP 可以直接从交易中变现。如果您是更倾向于通过 SaaS 费用或其他方式变现的合作伙伴，我们建议您利用开放或定向协作模式。
</p>
</div>

---


# **TikTok Shop Partner Center 政策**
https://partner.tiktokshop.com/docv2/page/6506bbf2de672602b7bc0697
