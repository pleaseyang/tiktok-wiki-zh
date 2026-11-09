# Seller Center 开发店铺

Seller Center 开发店铺允许开发者为 TikTok Shop API 开发创建 Seller Center 测试账号。这些测试账号在 Partner Center 账号下创建，与生产环境的卖家账号分开。开发店铺不会在生产环境的 TikTok 应用中被普通 TikTok 用户发现。
使用本指南选择合适的测试账号类型、创建测试店铺、授权您的应用，以及生成测试商品和订单数据。
# 快速入门
使用当前 Partner Center 路径：
**Partner Center 控制台 > 开发工具包 > 开发店铺**
| 任务 | 路径 |
| --- | --- |
| 创建 Core Function 或 Full Function 测试账号 | **开发工具包 > 开发店铺 > 管理账号 > 创建测试账号** |
| 进入测试店铺或授权应用 | **开发工具包 > 开发店铺 > 管理账号**  |
| 关联客户（买家）测试 TikTok 账号 | **开发工具包 > 开发店铺 > 管理账号 > 设置 (按钮)** |

较旧的截图或文档可能显示 **Development Kits > Development Shops**。将 **Development Shops** 视为 Sandbox 测试账号区域的前一个菜单名称。

## **创建测试卖家账号**
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4e741e5e315348c8beb9377ad1f05881~tplv-k9wyc2ijk0-image.image)

## **授权应用**
> 注意：您的应用市场必须包含 Sandbox 所在市场以及卖家类型；否则授权将失败。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/81521c8a370b4535bb99dee5479786f0~tplv-k9wyc2ijk0-image.image)

## **关联客户（买家）测试账号**
> 注意：此操作是不可逆的。一旦 TikTok 账号在开发店铺中关联，它将永久转变为测试账号。未来取消关联也不会恢复此账号。您必须使用新创建的 TikTok 账号进行关联。测试账号不能关联到生产环境的 Seller Center 账号。尝试这样做可能会严重影响您的业务运营。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c0c3bd107e434d5b90acabb7b8edeaac~tplv-k9wyc2ijk0-image.image)

# Core Function 与 Full Function 账号
| 问题 | 选择 Core Function 账号 | 选择 Full Function 账号 |
| --- | --- | --- |
| 主要目标 | 使用生成的测试数据进行商品、订单、履约、取消和退货 API 测试。 | 更接近生产环境 Seller Center 和 TikTok 应用买家行为的全流程测试。 |
| 商业/KYC 信息 | 基本设置不需要。 | 需要。商业和 KYC 信息必须有效，可能会接受审核。 |
| TikTok 账号设置 | 不需要。 |  Official Test TikTok Account 和 Buyer Test TikTok Account 场景需要。 |
| 支付 | 不需要真实支付或信用卡。测试订单在 Buyer View 中创建。 | 可以使用 Buyer Test TikTok Account 和支付方式测试真实买家结账流程。使用非常低的测试价格，例如 `$0.01`。 |
| TikTok 应用商品发现 | 不支持通过普通买家账号。 | 仅支持通过关联的测试 TikTok 账号。 |
| 财务、结算、客服及完整的生产级流程 | 不支持或不适用。 | Full Function 设置完成后可支持测试。 |
| 最适用于 | 商品上架、订单更新、履约、取消和退货的 API 集成测试。 | 测试买家体验、商品发现、支付、结算、客服及端到端流程。 |
决策指南：

1. 如果您只需要商品、订单、履约、取消或退货测试而无需真实支付，使用 **Core Function Account**。
2. 如果您需要 TikTok 应用发现、买家结账、真实支付、结算、客服或生产级验证，使用 **Full Function Account**。
3. 如果您无法提供商业/KYC 信息或区域匹配的 TikTok 测试账号，请先使用 **Core Function Account**。
4. 如果问题仅在 TikTok 应用买家流程中复现，请使用关联了测试 TikTok 账号的 **Full Function Account**。

> **Core Function 重要限制：** 在 **Core Function Account** 模式下，Sandbox 提供内置工具直接推进正向和逆向订单状态。由于这些工具模拟状态变更，某些流程可能与生产环境不一致或不完全对齐。使用 Core Function 模式进行核心 API 功能测试。使用 Full Function 模式进行全流程或细节级别的验证。


# 设置前常见问题
本节涵盖常见的 Sandbox 和开发者工具支持问题：测试账号创建、不可逆的 TikTok 账号转换，以及地区、SIM 卡或 VPN 限制。
## 我可以在生产和测试中使用同一个 TikTok 账号吗？
不要将生产或个人 TikTok 账号用于 Full Function 测试。一旦 TikTok 账号作为 Official Test TikTok Account 或 Buyer Test TikTok Account 关联，它将被转变为测试账号。此操作是永久性的，无法撤销。该账号不能再在 TikTok 应用或 TikTok Shop 生产环境中正常使用。
## 为什么关联 TikTok 账号会失败？
TikTok 账号地区必须与测试店铺地区匹配。创建或关联 TikTok 账号时，您的物理位置应与测试店铺所在国家或地区匹配。如果您无法 physically 位于该区域，请从设备中取出 SIM 卡，并使用具有测试店铺地区 IP 地址的 VPN，然后再创建或关联 TikTok 账号。
## 为什么在 TikTok 应用中找不到测试商品？
这适用于 Full Function 测试。请使用关联的 Buyer Test TikTok Account 搜索，而不是普通 TikTok 账号。还需检查商品是否已发布、不包含违禁或随机测试关键词，以及设备位置是否与店铺地区匹配。
## 为什么结账显示"Something went wrong"等错误？
对于 Full Function 订单，请检查买家测试账号是否正确关联、买家设备地区是否与店铺地区匹配，以及支付方式是否可用。如果您无法 physically 与店铺在同一地区，请取出 SIM 卡并使用具有该地区 IP 地址的 VPN。
# 您可以测试的内容
| 功能 | Core Function 账号 | Full Function 账号 |
| --- | --- | --- |
| 创建商品 | 是 | 是 |
| 无需支付创建测试订单 | 是，通过 Buyer View | 否，请改用买家结账流程 |
| 使用真实支付下单 | 否 | 是，通过关联的 Buyer Test TikTok Account |
| 履约订单 | 是 | 是 |
| 处理退货和退款 | 是 | 是 |
| TikTok 应用中的商品发现 | 否 | 是，通过关联的测试 TikTok 账号 |
| 财务报表和结算 | 否 | 是 |
| 客户消息服务 | 否 | 是 |
# 支持的市场和卖家类型
卖家开发店铺适用于跨境和本地店铺。
**注意：** 表格反映的是 Core Function 账号支持的区域。对于 Full Function 账号，支持的本地区域与 Core Function 账号相同，而跨境卖家支持目前不可用。
| 国家/地区 | 国家代码 | 跨境 | 本地 |
| --- | --- | --- | --- |
| 奥地利 | AT (40) | 是 | 是 |
| 比利时 | BE (56) | 是 | 是 |
| 巴西 | BR (76) | 否 | 是 |
| 捷克 | CZ (203) | 是 | 是 |
| 法国 | FR (250) | 是 | 是 |
| 德国 | DE (276) | 是 | 是 |
| 希腊 | GR (300) | 是 | 是 |
| 匈牙利 | HU (348) | 是 | 是 |
| 印度尼西亚 | ID (360) | 否 | 是 |
| 爱尔兰 | IE (372) | 是 | 是 |
| 意大利 | IT (380) | 是 | 是 |
| 日本 | JP (392) | 是 | 是 |
| 马来西亚 | MY (458) | 是 | 是 |
| 墨西哥 | MX (484) | 是 | 是 |
| 荷兰 | NL (528) | 是 | 是 |
| 菲律宾 | PH (608) | 是 | 是 |
| 波兰 | PL (616) | 是 | 是 |
| 葡萄牙 | PT (620) | 是 | 是 |
| 新加坡 | SG (702) | 是 | 是 |
| 越南 | VN (704) | 是 | 是 |
| 西班牙 | ES (724) | 是 | 是 |
| 泰国 | TH (764) | 是 | 是 |
| 英国 | GB (826) | 是 | 是 |
| 美国 | US (840) | 是 | 是 |
# 术语
| 术语 | 定义 |
| --- | --- |
| Seller Center 开发账号 | 在 Partner Center 下创建的用于开发和测试的 Seller Center 测试账号。开发账号中的事件和数据不会影响生产卖家账号。有两种类型：Core Function Account 和 Full Function Account。 |
| 核心功能账号 | 一种轻量级测试账号，不需要真实商业信息、TikTok 账号设置或信用卡信息。主要用于 Partner Center 内的商品、订单和履约测试。不支持真实买家结账、财务、结算或客服场景。 |
| 全功能账号 | 一种类生产环境的测试账号，需要商业和 KYC 信息。它支持 Core Account 功能以及关联的 Official Test TikTok Account 和 Buyer Test TikTok Account。用于买家结账、商品发现、财务、结算、客服和全流程测试。 |
| TikTok Account | 在 TikTok 应用中通过邮箱或手机号创建的账号。对于测试，请创建新的 TikTok 账号，不要使用生产账号。 |
| 官方测试 TikTok 账号 | 作为店铺官方账号关联到 Full Function 测试店铺的 TikTok 账号。关联后，该账号被转变为测试账号，无法恢复为生产用途。 |
| 买家测试 TikTok 账号 | 在 Partner Center 中关联的用于买家侧测试的 TikTok 账号。它可以在 Full Function 场景中搜索测试店铺、查看商品和下达测试订单。关联后，它永久转变为测试账号。 |
| 店铺类型 | 测试店铺的卖家模式和市场类型，例如 **Local** 或 **Cross-border**。本地店铺在一个本地市场运营。跨境店铺代表支持地区的跨境卖家场景。 |
| 入驻类型 | 设置期间使用的账号实体类型，例如 **Individual** 或 **Business**。对于 Core Function 测试，这不会改变可用功能。对于 Full Function 测试，商业/KYC 要求可能因市场和账号上下文而异。 |
# 设置概述
大多数 API 集成测试需要商品数据和订单数据。要创建这些数据，请使用以下设置之一：
| 设置 | 所需资源 |
| --- | --- |
| Core Function 测试 | Seller Center 核心功能账号 |
| Full Function 测试 | Seller Center Full Function Account、Official Test TikTok Account 和 Buyer Test TikTok Account |
设置完成后，使用测试店铺授权您的应用、创建商品、创建或下达订单，然后根据生成的测试数据验证 API 行为。
# Core Function Account 设置
## Core Function 功能
核心功能账号：

* 需要最少的设置信息；
* 不需要 TikTok Official 或 Buyer Test TikTok Account；
* 不需要支付方式或信用卡；
* 支持商品上架、订单更新、履约、取消和退货的核心测试；
* 不应用于财务、结算、客服、真实结账或类生产环境的买家流程验证。

## 创建 Core Function Account

1. 在 Partner Center Console 中，进入 **Development Kits > Sandbox > 卖家 test accounts**。
2. 点击 **Create test account**。
3. 选择 **Core Function**。
4. 根据目标卖家场景选择 **Shop Type**，例如 **Local**。
5. 提供 **Account Nickname**。
6. 选择 **Onboarding Type**，例如 **Individual** 或 **Business**。
7. 等待 Seller Center 测试账号设置完成。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e58d92b9830a4cc8b0a9dbddfa2e61ff~tplv-k9wyc2ijk0-image.image)
## 使用 Core Function 测试店铺授权您的应用

1. 进入 **Development Kits > Sandbox > 卖家 test accounts**。
2. 在卖家测试账号区域，点击 **Authorize app**。
3. 选择要与此店铺一起测试的应用。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/854f31907af145ae9c20070ca8459c40~tplv-k9wyc2ijk0-image.image)
## 添加和管理商品
通过在 Core Function 测试账号中输入所需的 TikTok Shop 商品信息并点击 **Submit for review** 来创建商品。您也可以使用 Create Product API 为开发店铺创建商品。
商品创建后，从 Core Function Seller Center 内的 **Products** 标签页管理和验证商品。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a3b85f88ba644df79426a97e4bccde0b~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/cacd3bc3ac9b4c7096887d2f5042c755~tplv-k9wyc2ijk0-image.image)
只有处于 **Active** 状态的商品才能用于 Core Function 测试订单。
## 添加卖家发货的运费模板
**注意：** 本节截图以美国为例。菜单选项可能因市场而异。

1. 在 Core Function Account 中，进入 **Orders > Shipping Options**。
2. 选择 TikTok Shipping 或卖家 Shipping。
3. 如果选择了卖家 Shipping，进入 **Orders > Shipping Templates** 并设置包含所需买家地区的运费模板。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4961c665fe8a44198437732d9f968854~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e9ac605b68e4ffd894c68bfe33d0e78~tplv-k9wyc2ijk0-image.image)
更多信息，请参阅 [TikTok Shipping 和 Seller Shipping 设置](https://seller-us.tiktok.com/university/essay?knowledge_id=2921116620719915&role=1&course_type=1&from=search&identity=1)。
## 使用 Buyer View 创建 Core Function 测试订单
Buyer View 让您无需真实买家支付即可触发测试订单。

1. 在 Buyer View 中点击 **Create test order**。
2. 选择测试订单的商品。一个测试订单最多可包含 3 个商品。
3. 选择订单的配送方式。
4. 测试订单创建后，它将出现在 Buyer View 中，状态为 **On Hold**。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3d2c9357a0ee4e21ac552129468f0adb~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a77d72556fa54e089cb763def0e6213f~tplv-k9wyc2ijk0-image.image)
## 测试取消、退货和履约
Buyer View 支持对受支持订单状态的模拟买家操作：
| 测试操作 | 要求 |
| --- | --- |
| 取消订单 | 订单必须处于 **On Hold** 或 **Awaiting Shipment** 状态。 |
| 申请退款或退货 | 订单必须处于受支持的状态，例如 **Awaiting Collection**、**In Transit** 或 **Delivered**。 |
开发者可以通过 API 或通过 **Orders > Manage Returns** 响应退货请求。
有关订单管理指南，请参阅：

* [管理订单](https://seller-us.tiktok.com/university/essay?knowledge_id=7774796412471041&role=1&course_type=1&from=search&identity=1)
* [管理退货](https://seller-us.tiktok.com/university/essay?knowledge_id=6837901778454274&role=1&course_type=1&from=search&identity=1)

# Full Function Account 设置
## Full Function 功能
全功能账号：

* 包含 Core Function 测试功能；
* 需要有效的商业和 KYC 信息；
* 在测试类生产环境流程之前需要完成完整的 Seller Center 设置；
* 可以关联 Official Test TikTok Account 和 Buyer Test TikTok Account；
* 支持通过关联的测试账号在 TikTok 应用中进行商品发现和买家结账；
* 支持真实支付测试订单、财务、结算、客服及其他全流程 API 测试。

## 创建 Full Function 账号前的要求
在创建 Full Function Account 之前，请准备所需的商业和 KYC 信息以及测试账号。您不需要提前创建应用。

* 提供有效的商业和 KYC 信息。
* 注册至少两个新的 TikTok 账号用于测试：一个用于 Official Test TikTok Account，一个用于 Buyer Test TikTok Account。
* 使用测试邮箱地址。不要使用个人、生产或高价值的 TikTok 账号。
* 为 TikTok 账号创建和关联准备区域匹配的设备/网络条件。

如果您无法提供所需的信息或区域匹配的 TikTok 账号，请先使用 Core Function Account。
## 创建 Full Function Account

1. 在 Partner Center Console 中，进入 **Development Kits > Sandbox > 卖家 test accounts**。
2. 点击 **Create test account**。
3. 选择 **Full Function**。
4. 根据目标卖家场景选择 **Shop Type**，例如 **Local**。
5. 提供 **Account Nickname**。
6. 点击 **Go to Seller Center** 并完成 [Seller Center 入驻](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10013682&role=1&identity=1)。

如果您是卖家开发者，并且已有与 Partner Center 账号关联的 TikTok Shop，则可能看不到 Seller Center 入驻步骤。
对于美国和英国的 Seller Center 测试账号：

* 美国：要在测试店铺中发布新商品，请在 Seller Center 中提供所需的税务信息。
* 英国：要接收来自 TikTok Shop 的付款，请填写 Seller Center 测试账号的税务信息。
* 创建测试店铺后，默认取货仓库会自动设置。您仍需设置运费模板。请参阅 [设置配送](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10012875&role=1&identity=1)。

## 关联 Official Test TikTok Account

1. 在 TikTok 应用中创建一个新的 TikTok 账号。使用测试邮箱地址。
2. 不要使用生产环境的 TikTok 账号。
3. 将该 TikTok 账号关联为测试店铺的 Official TikTok Account。
4. 有关账号关联详情，请参阅 [如何关联 TikTok Shop 官方账号](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10012412&role=1&identity=1)。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b471be6835d449b7ba92cf0f09dd6be8~tplv-k9wyc2ijk0-image.image)
**不要将账号关联为 Marketing Account 进行应用测试。** Marketing Account 对商品和店铺可见性有额外限制。
## 关联 Buyer Test TikTok Account

1. 在 TikTok 应用中创建第二个新的 TikTok 账号。使用测试邮箱地址。
2. 使用要作为买家测试账号的账号登录 TikTok 应用。
3. 在 Partner Center 中，进入 **Development Kits > Sandbox > Buyer test accounts**。
4. 点击 **Link account**。
5. 在 **Link TikTok account as buyer account** 页面使用 TikTok 应用扫描二维码。
6. 在 TikTok 应用中按照 **Authorize TikTok Partner Center** 流程操作。
7. 在买家账号关联页面点击 **Link the account**。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/08010af0a24a4e6792370acb942fbc6c~tplv-k9wyc2ijk0-image.image)
## 地区和账号转换规则
以下规则适用于 Official Test TikTok Account 和 Buyer Test TikTok Account：

* TikTok 账号地区必须与测试店铺地区匹配。
* 在创建和关联 TikTok 账号时，您的物理位置应与测试店铺地区匹配。
* 如果您无法 physically 位于同一地区，请从设备中取出 SIM 卡，并使用具有测试店铺地区 IP 地址的 VPN，然后再创建或关联 TikTok 账号。
* TikTok 账号在 Sandbox 中关联后，将永久转变为测试账号。
* 转变后的测试账号不能在 TikTok 应用或 TikTok Shop 生产环境中正常使用。
* 使用新的测试邮箱地址，并将 Official Test TikTok Account 与 Buyer Test TikTok Account 分开。

# 使用 Full Function Account 测试您的应用
## 授权您的应用

1. 进入 **Development Kits > Sandbox > 卖家 test accounts**。
2. 在卖家测试账号区域，点击 **Authorize app**。
3. 选择要安装并与测试店铺一起测试的应用。

## 添加和发布商品
按照生产规则添加和发布商品。对于美国测试店铺，必须在提交税务信息后才能发布商品。
不要在商品标题中使用随机字符串、"test"一词或违禁关键词。商品可能会被标记，即使它们在 Seller Center 中显示为已发布。
## 在 TikTok 中查找商品
使用关联的 Buyer Test TikTok Account 在 TikTok 应用中搜索 Official Test TikTok Account。只有关联的测试账号才能找到并与测试店铺的商品互动。普通 TikTok 账号无法找到开发店铺。
如果商品未出现：

* 确认商品已发布；
* 检查标题或内容是否被标记；
* 确认买家账号已正确关联；
* 确认设备地区与店铺地区匹配。

## 使用真实支付创建订单
Full Function 测试订单通过 TikTok 应用买家流程下达。

1. 为 Buyer Test TikTok Account 添加支付方式。
2. 设置非常低的商品价格，例如 `$0.01`。
3. 使用 Buyer Test TikTok Account 登录 TikTok 应用。
4. 搜索测试店铺的 Official Test TikTok Account。
5. 从账号主页打开 **Shop** 标签页。
6. 选择测试商品并完成购买。

如果结账失败，请检查买家账号关联状态、设备地区、SIM 卡、VPN、支付方式和商品发布状态。
## 管理订单
支付完成后，在 **Seller Center > Orders > Manage orders** 中管理订单。您可以根据应用的测试用例通过 API 履约订单。
更多详情，请参阅：

* [管理订单](https://seller-us.tiktok.com/university/essay?knowledge_id=7774796412471041&identity=1)
* [管理卖家自行配送](https://seller-us.tiktok.com/university/essay?knowledge_id=6837882170099457&identity=1)
* [管理 TikTok Shop 物流配送](https://seller-us.tiktok.com/university/essay?knowledge_id=8706274700117762&identity=1)

如果您需要测试订单结算、收入分成或其他财务相关功能，请使用 **Full Function Account**。
# 限制

1. 您最多可以创建 10 个 Seller Center 测试账号（包括 Full Function 和 Core Function Account）。
2. Seller Center 开发店铺在 180 天后过期，但可以在 Partner Center 中重新激活。
3. 您最多可以将 10 个 TikTok 账号作为 Buyer Test TikTok Account 关联到一个 Partner Center 账号。
4. 关联到 Partner Center 账号的 Buyer Test TikTok Account 可以与您在 Sandbox 中创建的任何测试店铺一起使用。
5. Full Function 测试至少需要两个真实的 TikTok 账号：一个 Official Test TikTok Account 和一个 Buyer Test TikTok Account。
6. 您不能将同一个 TikTok 账号同时用作 Official Test TikTok Account 和 Buyer Test TikTok Account。
7. 沙盒店铺的 API 调用配额为 QPH < 18,000，超过此限制将导致限流错误。


