# Agency应用开发与订阅权限

# 1. 概述
本功能指南说明TikTok Shop如何向已入驻的Agency授予API访问权限，以及Agency如何使用其TikTok Shop Agency身份构建自定义应用并为其合作的卖家订阅应用。借助此功能，卖家无需再由主账号手动完成每个步骤。
阅读本指南后，Agency将能够：

* 确认其已入驻的账号具有正确的Agency身份和权限范围。
* 在TikTok Shop Agency应用类别下创建Custom App并调用TikTok Shop Open API。
* 使用TSP Access进入已授权卖家的Seller Center并确认该卖家的App Subscription URL。
* 仅在**美国本地市场**有效，其他市场需要单独申请ISV类别。

# 2. 背景
此功能使Agency能够更快速、更简便地为其支持的卖家构建和推出基于API的工具。它简化了以往体验中的两个方面：

* **更简便的开发者访问。** 已入驻的Agency现在自动获得App Developer（ISV）身份，因此可以立即创建具有所需API范围的Custom App。此前，Agency需要单独的ISV应用类别审批才能调用TikTok Shop API。
* **代表卖家订阅。** 借助TSP Access，Agency现在可以直接代表已授权的卖家完成应用订阅确认。此前，每次安装和订阅确认都需要从卖家主账号完成，这在批量入驻卖家、准备直播上线和准备大促活动时增加了额外步骤。

这些更新共同为已入驻的Agency提供了更直接的应用开发路径：已入驻的Agency自动获得App Developer（ISV）身份并被分配到专属的TikTok Shop Agency应用类别，无需单独申请ISV。结合TSP Access，Agency可以直接为已授权的卖家完成订阅确认。
# 3. 前提条件

* 您的Agency入驻申请已获批准。
* 您可以使用入驻时的账号登录Partner Center。
* 至少有一个卖家通过标准TSP Access授权流程授权了您的TSP账号（第6节中代表卖家订阅步骤所需）。

App Developer（ISV）身份在入驻批准后可能需要最多一个工作日才能显示。如果在此时间内未显示，请参阅第8节的常见问题。

# 4. 功能运作方式
## 4.1 App Developer（ISV）身份
Agency入驻申请获批后，账号所有者将在左上角的身份切换器中看到新的App Developer（ISV）入口。此身份是进入TikTok Shop开发者控制台的入口，解锁创建和管理Custom App的能力。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/552823c3264049fda4647496a4c443c6~tplv-k9wyc2ijk0-image.image)
## 4.2 TikTok Shop Agency应用类别
在后台，平台将已批准的Agency分配到名为TikTok Shop Agency的专属应用类别。此类别定义了Agency应用可以申请的有效API范围，并管理这些应用的审核流程。Agency无需提交单独的ISV类别申请。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c6601c3b2060462188d7459d6116523f~tplv-k9wyc2ijk0-image.image)
## 4.3 构建Custom App
在TikTok Shop Agency应用类别下，Agency可以创建调用TikTok Shop Open API的Custom App。然后，Custom App可以在标准应用订阅流程下分发给Agency合作的卖家并由其安装。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5f104b535ef945c48f44a76ad7bc3dd0~tplv-k9wyc2ijk0-image.image)
## 4.4 TSP Access与App Subscription URL
在卖家已通过标准TSP Access流程授予授权的情况下，Agency可以进入卖家的Seller Center并打开App Subscription URL以完成该卖家的订阅确认。卖家的主账号不再需要为每个应用打开订阅界面。
管理此功能的具体权限点如下所示。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/6453cc542c7c475eabe24a32b91d4453~tplv-k9wyc2ijk0-image.image)
# 5. 权限点汇总
| 功能 | 所需身份 | 获取方式 | 适用范围 |
| --- | --- | --- | --- |
| 访问TikTok Shop开发者控制台 | App Developer（ISV） | Agency入驻成功后自动授予 | 左上角身份切换器 |
| 创建调用TikTok Shop Open API的Custom App | 具有TikTok Shop Agency应用类别的App Developer（ISV） | 应用类别设置为TikTok Shop Agency | 开发者控制台，创建应用 |
| 代表卖家进入Seller Center | 具有已授权卖家的TSP | TSP Access | Partner Center，卖家列表 |
| 打开App Subscription URL并确认卖家订阅 | 具有已授权卖家的TSP | TSP Access，应用订阅权限点（见图4） | Seller Center，App Subscription URL |
# 6. 分步指南
## 6.1 验证您的Agency身份

* 使用Agency入驻时的账号登录Partner Center。
* 打开左上角的身份切换器，确认App Developer（ISV）已列出。
* 如果身份缺失，请在入驻批准后等待最多一个工作日，然后验证您的Agency申请的入驻状态后再继续。

## 6.2 创建Custom App

* 切换到App Developer（ISV）身份。
* 进入TikTok Shop开发者控制台并选择创建应用。
* 选择TikTok Shop Agency作为应用类别。
* 完成应用元数据，申请所需的API范围，并提交审核。

## 6.3 入驻卖家并分发应用

* 确保卖家已通过标准TSP Access授权流程授权您的TSP账号。
* 与卖家分享应用的安装或订阅链接，或使用TSP Access直接进入Seller Center。

## 6.4 代表卖家订阅

* 在Partner Center中，找到已授权的卖家并使用TSP Access进入其Seller Center。
* 打开您的Custom App提供的App Subscription URL。
* 确认订阅。卖家的主账号不再需要完成此步骤。

# 7. 合规说明

* 所有API调用必须遵守应用审核时授予的API范围。申请超出TikTok Shop Agency应用类别的范围可能导致审核被拒。
* TSP Access仅在卖家授权有效期间有效。如果卖家撤销授权，TSP Access和代表卖家订阅的操作将立即被禁用。
* Agency对TSP Access下采取的操作负责，包括订阅确认。平台保留完整的审计日志以供合规审查。
* 不要对外分享App Developer（ISV）账号凭据。Custom App必须在已入驻的Agency实体下构建和维护。

# 8. 常见问题
## Q1. 我完成了Agency入驻但没有看到App Developer（ISV）身份。
请在入驻批准后等待最多一个工作日。如果身份仍未显示，请联系您的TikTok Shop客户经理，提供您的Partner ID和批准时间戳。
## Q2. 我还需要单独申请ISV应用类别吗？
不需要。已入驻的Agency自动归入TikTok Shop Agency应用类别。无需单独申请ISV。
## Q3. 我还需要卖家主账号来选择订阅按钮吗？
不需要。一旦TSP Access授权到位，您可以在卖家的Seller Center内打开App Subscription URL并代表卖家完成订阅确认。每次订阅不需要卖家主账号操作。
## Q4. 如果卖家撤销TSP Access会怎样？
所有TSP Access操作，包括进入Seller Center和代表卖家确认订阅，将立即被禁用。现有订阅保持有效，除非卖家从其自己的Seller Center取消。
