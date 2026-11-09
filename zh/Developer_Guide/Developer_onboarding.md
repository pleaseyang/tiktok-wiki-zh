# 开发者入驻

成为 TikTok Shop 开发者有 **三个** 主要步骤：

1. 在 TikTok Shop Partner Center **创建账户**。
2. **注册为开发者**（卖家开发者或应用开发者 / ISV）。
3. **启动合规和法律审查**——美国和英国合作伙伴必须完成（其他地区视情况而定）。此步骤可能需要 **三周或更长时间**，请尽早规划。

> ⏱️ **规划完整时间线。** 步骤 1-2 很快完成，但步骤 3 中的合规和法律审查是关键耗时环节。如果你是英国或美国合作伙伴，请在完全上线前预留 3 周以上时间。

## 步骤 1：在 Partner Center 创建账户
如果你还没有账户，请使用 TikTok Shop 合作伙伴控制台创建账户：

* **美国** 地区账户 → [partner.us.tiktokshop.com/account/sign-up](https://partner.us.tiktokshop.com/account/sign-up)
* **非美国** 地区账户 → [partner.tiktokshop.com/account/sign-up](https://partner.tiktokshop.com/account/sign-up)

> **我应该使用哪个域名？** 美国地区账户使用 `partner.us.tiktokshop.com`，全球/其他地区账户使用 `partner.tiktokshop.com`。美国跨境卖家开发者使用全球入口。之后，当你进行 API 调用时，还会遇到 `auth.tiktok-shops.com`（token endpoint）和区域授权域名（`services.us.tiktokshop.com` / `services.tiktokshop.com`）。每个市场/用途都有自己的域名——完整映射请参见授权指南。

两个流程相同。在 **Log In** 对话框中，选择 **Sign Up**，然后提供你的电子邮件地址和（可选）手机号码。请保持你的 Partner Center 电子邮件为最新状态——它对于接收关键平台更新至关重要。
**为什么我被重定向到美国站点？**
使用美国 VPN 或代理可能导致 Partner Center 根据你的公网 IP 将你重定向到美国站点。如需访问全球/其他地区，请检查你的 IP 位置，断开美国 VPN 或使用非美国出口，然后重新打开 [Global Partner Center](https://partner.tiktokshop.com/)。
你的账户区域也可能在登录后导致重定向。如果切换网络无法解决问题，请注销并在隐私窗口中重试，然后确认站点与你的账户区域匹配。
> ⚠️ 为你的开发者类型使用正确的电子邮件。如果你想注册为应用开发者或系统集成商（ISV），请勿使用与你的 TikTok Shop 卖家账户关联的电子邮件。如果你使用 Shop 账户电子邮件注册，系统会将你识别为卖家，你只能注册为卖家开发者。

**注意：** TikTok Shop 合作伙伴 Platform 和 Open Platform 已于 2022 年底合并为 TikTok Shop Partner Center。如果你有现有的合作伙伴 Platform 或 Open Platform 账户，可以使用这些凭据登录 Partner Center。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b28cc21e222f476c95281075a679196e~tplv-k9wyc2ijk0-image.image)
## 步骤 2：注册为开发者
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e669291d30f4b67bd48cadb951ed878~tplv-k9wyc2ijk0-image.image)
## 开始之前：确定你的开发者类型
注册时，你需要选择以下两种开发者类型之一：

1. **TikTok Shop 卖家开发者** —— 构建访问 **自己** 卖家数据的 **custom** 应用。
2. **应用开发者或系统集成商（ISV）** —— 构建 **public** 应用，可以申请授权访问 TikTok Shop 上 **其他卖家** 的数据。

> ✅ **卖家开发者前提条件（开始前请阅读）：**

> * 你必须在注册为开发者之前 **拥有已激活的 TikTok Shop 账户并绑定了 Account Manager**。
> * 你用于验证的电子邮件 **应与** 注册 TikTok Shop 时使用的电子邮件相同。

> 这两个约束是卖家开发者注册失败的最常见原因。

## 注册为应用开发者或系统集成商（ISV）

1. **开始你的合作伙伴注册申请。** 在业务指南对话框中，选择 **For app developers（ISV）**，然后点击 **Start Business**。

> 如果你的账户因电子邮件错误（**使用了 Shop 账户电子邮件**）需要加入白名单，请在继续注册流程之前提交工单或联系你的 Account Manager（AM）申请白名单。

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b13be7a323f042d693ae5b22cc619072~tplv-k9wyc2ijk0-image.image" width="1280px" /></div>


2. 点击 **Start Business** 开始你的合作伙伴申请。

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/906a33e285db45fd942596b714ac5e64~tplv-k9wyc2ijk0-image.image" width="1052px" /></div>


3. **指定你的注册区域、目标市场和业务类别：**

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a0b1d2a2200c40f7b16eace530df6034~tplv-k9wyc2ijk0-image.image" width="3812px" /></div>


   * **注册区域：** 必须与你公司的商业认证一致。
   * **目标市场：** 跨境合作伙伴（注册区域为中国和/或中国香港）可选择英国、马来西亚、越南、泰国、菲律宾或新加坡；本地合作伙伴（本地市场实体）应仅选择其本地市场。
   * **业务类别：** 选择你的业务类别。📌 可用类别可能因注册区域和目标市场而异。
4. **指定你的公司名称和联系信息，** 并提供额外的业务详情以便团队为你提供支持。

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c4f7dc5ccb9d453595656649704cdcc2~tplv-k9wyc2ijk0-image.image" width="3816px" /></div>


5. **上传你公司的营业执照和注册信息。**

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/53c321e8ce844441bbd2d0c67c5e9654~tplv-k9wyc2ijk0-image.image" width="3810px" /></div>


   * 如果你尚未准备好这些材料，请选择 **Save for later**；然后你可以前往 *Back to profile* 或 *Create app or service*。（如果你现在创建应用，在认证完成之前无法发布。）

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4f9839cc656a4d37bdf20715c2eb2e3e~tplv-k9wyc2ijk0-image.image" width="3806px" /></div>


   * 否则，选择 **Submit** 开始认证审查。

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fd21258fe5b8436abd226db7c4d21320~tplv-k9wyc2ijk0-image.image" width="3812px" /></div>

在 **My Account > My category & market** 下查看你的申请状态。一旦批准，**under review** 消息将消失。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1fcbb9ff22994e46ab601438ec9767d4~tplv-k9wyc2ijk0-image.image)
## 入驻后添加其他市场
如果你已有 ISV 应用并希望扩展它，可以从该应用的 **+ Add market（Seller type）** 对话框开始。完整流程请参见 [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) 中的 **Add markets to an existing app**。
你也可以从你的个人资料开始：

1. 打开你的个人资料，选择添加类别或市场的选项。
2. 选择目标市场和业务类别，然后点击 **Next**。
3. 查看 **合作伙伴 info** 表单并填写所需信息。如果你在该类别中已有应用，点击 **Submit** 保存草稿。
4. 在成功页面上，选择你希望继续的方式：
   * **Add to an existing App** 将打开 **App & Service**，并筛选到相关类别。选择一个应用并点击 **Manage**，然后使用 **+ Add market（Seller type）** 选择可用市场，完成卖家设置并 **Save**。如果在市场可用之前需要资格审查，请先完成该审查。
   * **Create a new App** 将打开应用创建流程，并自动带入所选类别。选择 **Public** 或 **Custom**，查看应用详情并完成创建。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/925f6c7c17fc4a0db5572c2b0aa9a415~tplv-k9wyc2ijk0-image.image)

如果你在所选类别中没有应用，请继续按照 Partner Center 中显示的应用创建流程操作。
> **检查最后一步。** 成功页面确认你的草稿信息已保存。这并不意味着资格审查已开始、市场已添加到应用、或应用已在该市场上架。

### 找到你要扩展的应用
**Category** 筛选器将匹配的 Public 和 Custom 类别归在一个选项下。如果你只想查看 Public 或仅 Custom 应用，请使用单独的 **Type** 筛选器。
当你从 **Add to an existing App** 进入时，Partner Center 会显示选择应用的提示。关闭此提示后，类别筛选器仍然保留。
## 注册为卖家开发者
> 详细指南请参阅：https://partner.tiktokshop.com/docv2/page/seller-developer-onboarding-onepager


* 在申请开发者账户的目标市场时，选择类别 **卖家 inhouse developer / TikTok Shop 卖家**，并在下一步中 **关联已激活的 TikTok Shop 账户**。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f9513f71b0d84bcab0ad458aa7d7f8f0~tplv-k9wyc2ijk0-image.image)

📌 **注意**：请确保你输入的卖家账户信息真实有效。

## 步骤 3：启动合规和法律审查
注册为开发者合作伙伴后，启动合规和法律审查。这可能需要 **三周或更长时间**。某些合作伙伴视情况需要审查，但 **美国和英国合作伙伴始终需要审查**。
联系你所辖市场的合作伙伴 Development & Management 团队索取尽职调查问卷：

* 美国：[partner.us@tiktokshop.com](mailto:partner.us@tiktokshop.com)
* 英国：[partner.uk@tiktokshop.com](mailto:partner.uk@tiktokshop.com)
* 其他：[partner@tiktokshop.com](mailto:partner@tiktokshop.com)

**何时开始：** 注册完成后立即启动此审查，以便 3 周以上的时间线与你的开发工作并行进行。提前准备你的尽职调查问卷和支持性商业文件。详情请参见合规和法律审查。
## 后续步骤
现在你已拥有合作伙伴开发者账户，可以开始 [进行你的第一次 TikTok Shop API 调用](https://partner.tiktokshop.com/docv2/page/make-your-first-api-call-overview)。

