# 联盟 API 解决方案指南

# 背景
TikTok Shop 很高兴推出一类新的 API，专注于 TikTok Shop 的联盟营销。
这些 API 将为卖家、达人联盟和 TikTok Shop 合作伙伴提供更高效的方式来创建、管理、匹配、跟踪、变现和协作 TikTok Shop 联盟合作和合作伙伴活动。

**联盟 API 默认未激活，合作伙伴/ISV 必须申请访问权限，需要您的客户经理或合作伙伴经理批准才能激活 API 以构建应用。**
## 合作伙伴账户设置

1. 参考 [注册为服务合作伙伴](tsp-onboarding) 进行注册。确保在注册时选择以下值。
   * **业务指南**：应用开发者（ISV）
   * **类别**：应用开发者 > 客户互动 > 联盟
      ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/partner_account_setup1.png?x-resource-account=public)
2. 进入 **应用与服务** 并创建以下应用：
   * Affiliate（公开）：用于在 TikTok Shop 应用店铺上架官方应用。
   * Affiliate（自定义）：用于测试目的。
   * Connector（自定义）：用于获取非联盟 API 的必要访问权限。
3. 参考 [发布并上架公开应用](publish-and-list-public-app) 对 **Affiliate（公开）** 应用发起合规审查。
4. 提供您的 **app key**（14 位字符的密钥，不是 App ID 或合作伙伴 ID）给您的合作伙伴经理，以便我们为您列出达人授权。达人授权是访问达人 API 的必要条件。
5. API 访问权限授予后，开始集成开发。

## 开发店铺设置
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/development_shop_setup2.png?x-resource-account=public)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/development_shop_setup1.png?x-resource-account=public)
## 开发店铺卖家中心设置
### 税务信息
提供虚拟信息以满足此要求。
导航到 [卖家中心](https://seller-us.tiktok.com/homepage)，应该会看到类似以下的横幅：
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/seller_center_banner.png?x-resource-account=public)
点击横幅上的 **立即验证**，您将看到如下所示的税务表单。您可以使用本示例中的相同值。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/seller_center_tax_information.png?x-resource-account=public)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/seller_center_tax_information2.png?x-resource-account=public)
点击 **提交** 后，系统会弹出确认框，要求您签名。这可能看起来很严格，但这只是测试账户，我们只需满足一些要求即可。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/seller_center_tax_signature.png?x-resource-account=public)

<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：您可能需要设置发货仓和退货仓，并设置物流模板。请参考以下支持文章配置仓库和物流模板：</span>

* [物流模板](https://seller-us.tiktok.com/university/essay?knowledge_id=6837882170099457&role=1&course_type=1&from=search&identity=1&anchor_link=EC4200CA)
* [仓库](https://seller-us.tiktok.com/university/essay?knowledge_id=6837882170099457&role=1&course_type=1&from=search&identity=1&anchor_link=EBCE00CE)

提交税务信息后，开发店铺设置即完成，可以接受商品上架了。
### 商品上架示例
举例来说，假设我们有一个商品希望达人展示。他们需要一个联盟链接来与粉丝分享以购买此商品。这有助于简化购买流程，并跟踪达人或商品类别的销售情况。以下是一些示例截图，展示如何通过卖家中心上架商品。您也可以使用 API 创建它们。
<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：如果通过卖家中心创建，建议选择 </span><span style="color: orange"><strong>No Brand</strong></span><span style="color: orange">。</span>
**商品 1**
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/product_listing_example1.png?x-resource-account=public)
**商品 2**
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/product_listing_example2.png?x-resource-account=public)
商品创建后，审核通过后您应该看到它们的状态为 **上架中**。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/product_listing_live.png?x-resource-account=public)
恭喜！商品现在可以添加到开放合作中了！点击左侧的 **联盟** 进入联盟中心。向下滚动并点击 **前往 TikTok Shop 联盟首页**。这将在新标签页中打开联盟中心。您也可以使用[此链接](https://affiliate-us.tiktok.com/errorpage?)，它应该会自动登录。
## 卖家入驻
需要卖家中心授权才能获取卖家所有在售商品的信息。卖家可以设置开放合作（任何达人都可以加入），或设置与特定合作伙伴的定向合作。要通过 API 实现这些功能，卖家必须连接其 TikTok 卖家中心账户，以便您可以管理其联盟、商品和订单。
要了解授权应用的所有步骤，请参考合作伙伴中心的[卖家授权指南](seller-authorization-guide)。授权后，您应该：

* 通过调用 [获取授权店铺 API](get-authorized-shops) 验证连接，并将响应与卖家中心的值进行比较。
* 调用 [搜索商品 API](search-products) 获取商品列表及其对应的商品 ID，以供后续 API 调用使用。

## 达人入驻
在发送定向合作或邀请达人参加活动之前，您需要让达人将其 TikTok 账户与您的应用连接。

* 请他们使用您的达人授权链接登录 TikTok。链接格式为：
   `shop.tiktok.com/alliance/creator/auth?app_key=<app_key>&state=<state>`

<span style="color: red">❗ </span><span style="color: red"><strong>重要</strong></span><span style="color: red">：</span><span style="color: red"><strong>state</strong></span><span style="color: red"> 参数是达人授权链接的必填项。</span>

* 这将提示达人使用其 TikTok 账户登录。
* 登录成功后，他们将看到类似以下的界面：
   ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/creator_onboarding1.jpg?x-resource-account=public)
* 当他们点击 **授权** 按钮时，TikTok Shop 将把您重定向到应用设置中指定的重定向链接。例如，如果重定向链接是 `http://localhost:8000`，则重定向 URL 将类似：`http://localhost:8000?code=<redacted>&state=<state>&app_key=<app_key>`。
* 使用重定向 URL 中的 code 调用 **GET Access Token** 端点，这将授予您调用联盟达人端点的权限。

<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：此过程与获取卖家中心账户的 access token 相同，但有两个不同的 access token，一个用于卖家账户，一个用于达人账户。</span>

* **GET 达人 Profile** 端点将返回成功调用创建定向合作 API 所需的 `creator_user_id`。

请参考 TikTok Shop 合作伙伴中心的[创作者授权指南](creator-authorization-guide)，了解如何连接这些账户的详细信息。
## API 范围映射
<span style="color: green">💡 </span><span style="color: green"><strong>提示</strong></span><span style="color: green">：您可以直接在 </span><span style="color: green"><strong>管理 API</strong></span><span style="color: green"> 弹窗中搜索 API 名称，点击 </span><span style="color: green"><strong>Scope Name</strong></span><span style="color: green"> 旁边的下拉菜单，从 </span><span style="color: green"><strong>API Names</strong></span><span style="color: green"> 列下的列表中选择一项。</span>
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/api_scope_mapping.png?x-resource-account=public)
| Scope ID | Scope 名称 | API 名称 |
| --- | --- | --- |
| 434372 | 联盟信息 | * 检查主播内容 <br/> * 检查主播前置条件 <br/> * 获取达人资料 <br/> * 获取直播间信息 <br/> * 获取店铺商品 |
| 733764 | 读取卖家联盟合作 | * 搜索卖家联盟订单 <br/> * 卖家搜索联盟开放协作商品 |
| 890884 | 管理卖家联盟合作 | * 创建开放协作 <br/> * 创建定向协作 <br/> * 编辑开放协作设置 <br/> * 生成联盟商品推广链接 <br/> * 从协作中移除联盟达人 |
| 1021508 | 读取达人联盟合作 | * 达人搜索开放协作商品 <br/> * 搜索达人联盟订单 <br/> * 搜索达人定向协作 |
| 733508 | 读取联盟合作伙伴活动 | * 获取 Affiliate Partner 活动详情 <br/> * 获取 Affiliate Partner 活动列表 <br/> * 获取 Affiliate Partner 活动商品列表 |
| 733444 | 管理联盟合作伙伴活动 | * 创建 Affiliate Partner 活动 <br/> * 编辑 Affiliate Partner 活动 <br/> * 发布 Affiliate Partner 活动 |
| 733572 | 管理联盟合作伙伴活动商品 | * 审核 Affiliate Partner 活动商品 |

# 使用场景
## 生成联盟商品推广链接
对于已上架的商品，您可以通过调用[生成联盟商品推广链接 API](generate-affiliate-product-promotion-link)生成商品推广链接。每次 API 调用只能创建一个推广链接，因为商品 ID 是路径参数的一部分。
```curl
curl --location --globoff --request POST 'https://open-api.tiktokglobalshop.com/affiliate_seller/202405/products/1729570313535393936/promotion_link/generate?app_key=6d0ut2ttps2io&shop_cipher=TTP_YaVduQAAAACwxSc13yKds1NldAZaPw34&sign=c2a149d480ae59b6eaf0ceebe1173d7fbb831a4227406a9008c0565535b42ebe&timestamp=1723135734' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: <token>' \
--data ''

{
    "code": 0,
    "data": {
        "product_promotion_link": "https://www.tiktok.com/t/ZTNgEQFGa/"
    },
    "message": "Success",
    "request_id": "20240808165018109CFA6CCA917E04CBAD"
}
```

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/open_collaboration1.png?x-resource-account=public)
<span style="color: red">❗ </span><span style="color: red"><strong>重要</strong></span><span style="color: red">：每个开放合作只能添加</span><span style="color: red"><strong>一个</strong></span><span style="color: red">商品。</span>

要创建开放合作，请按以下步骤操作：

* 通过调用[创建开放合作 API](create-open-collaboration)，使用商品 ID 和佣金比例（例如 1234）将商品添加到开放合作中。
   * 如果成功，响应应包含生效时间、ID（开放合作 ID 87620110221）和合作中的商品 ID。
   * 如果您想编辑佣金比例或审批达人开关，只需使用新设置再次调用 API。ID 不会改变。

<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：免费样品无法通过 API 添加到开放合作，必须在卖家中心完成。</span>

* 您可以通过调用[卖家搜索联盟开放合作 API](seller-search-affiliate-open-collaboration-product)验证创建是否成功：

```curl
curl --location --globoff 'https://open-api.tiktokglobalshop.com/affiliate_seller/202405/open_collaborations/products/search?app_key=6d0ut2ttps2io&shop_cipher=TTP_YaVduQAAAACwxSc13yKds1NldAZaPw34&sign=30ce092ba485c189a6c30f856ce771c55c4acddda11c957ecababd5c07435a2d&timestamp=1723136505&page_size=10' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: <token>' \
--data '{
    "category": {
        "id": "601755"
    },
    "title_keywords": [
        "Open Collaboration Pink"
    ],
    "sales_price_range": {
        "amount_ge": "3.99",
        "amount_lt": "4.99"
    },
    "commission_rate_range": {
        "rate_ge": 1233,
        "rate_lt": 1235
    }
}'

{
    "code": 0,
    "data": {
        "next_page_token": "",
        "products": [
            {
                "category_chains": [
                    {
                        "id": "601755",
                        "is_leaf": false,
                        "local_name": "Computers & Office Equipment",
                        "parent_id": "0"
                    },
                    {
                        "id": "831112",
                        "is_leaf": false,
                        "local_name": "Office Stationery & Supplies",
                        "parent_id": "601755"
                    },
                    {
                        "id": "855560",
                        "is_leaf": true,
                        "local_name": "Cards",
                        "parent_id": "831112"
                    }
                ],
                "commission": {
                    "amount": "0.4319",
                    "currency": "USD",
                    "rate": 1234
                },
                "detail_link": "https://shop.tiktok.com/view/product/1729570313535393936?region=US&local=en",
                "has_inventory": true,
                "id": "1729570313535393936",
                "main_image_url": "https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/c9052b2b9d5248c1a552d5fe15a892d5~tplv-omjb5zjo8w-origin-webp.webp?from=1695864008",
                "original_price": {
                    "currency": "USD",
                    "maximum_amount": "4.19",
                    "minimum_amount": "4.19"
                },
                "sale_region": "US",
                "sales_price": {
                    "currency": "USD",
                    "maximum_amount": "3.5",
                    "minimum_amount": "3.5"
                },
                "shop": {
                    "name": "SANDBOX7398293016815273770"
                },
                "title": "Open Collaboration Coffee Pink Color Meme Card Smiling Lady",
                "units_sold": 5
            }
        ],
        "total_count": 1
    },
    "message": "Success",
    "request_id": "20240808170145A205E014C8878404D59C"
}
```

<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：您可能需要调整参数来过滤结果，特别是当参数太宽泛时。在上面的示例中，标题关键词为 "Open Collaboration Pink"，销售价格范围在 3.99 到 4.99 之间，佣金比例在 1233 到 1235 之间。</span>

* 您也可以在联盟中心验证：

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/open_collaboration2.png?x-resource-account=public)
### 达人操作
已完成上述入驻步骤的达人可以使用您的应用查找开放合作。要启用此功能，您必须集成[创作者搜索开放合作商品 API](creator-search-open-collaboration-product)（cURL 如下）。该 API 接受商品标题搜索、商品价格、商品类别以及合作佣金，并返回该卖家发布的开放合作列表，达人可以自由加入。其中一些有筛选流程，卖家需要在审核后批准达人。
```curl
curl --location --globoff 'https://open-api.tiktokglobalshop.com/affiliate_seller/202405/open_collaborations/products/search?app_key=6d0ut2ttps2io&shop_cipher=TTP_bCWokAAAAAA6xm9rY_B9wYFY2QltXcs9&sign={{sign}}&timestamp={{timestamp}}&page_size=10' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: <redacted>' \
--data '{
    "category": {
        "id": "601755"
    },
    "title_keywords": [
        "Open Collaboration Pink"
    ],
    "sales_price_range": {
        "amount_ge": "3.99",
        "amount_lt": "4.99"
    },
    "commission_rate_range": {
        "rate_ge": 1233,
        "rate_lt": 1235
    }
}'

{
    "code": 0,
    "data": {
        "next_page_token": "",
        "products": [
            {
                "category_chains": [
                    {
                        "id": "601755",
                        "is_leaf": false,
                        "local_name": "Computers & Office Equipment",
                        "parent_id": "0"
                    },
                    {
                        "id": "831112",
                        "is_leaf": false,
                        "local_name": "Office Stationery & Supplies",
                        "parent_id": "601755"
                    },
                    {
                        "id": "855560",
                        "is_leaf": true,
                        "local_name": "Cards",
                        "parent_id": "831112"
                    }
                ],
                "commission": {
                    "amount": "0.4319",
                    "currency": "USD",
                    "rate": 1234
                },
                "detail_link": "https://shop.tiktok.com/view/product/1729570313535393936?region=US&local=en",
                "has_inventory": true,
                "id": "1729570313535393936",
                "main_image_url": "https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/c9052b2b9d5248c1a552d5fe15a892d5~tplv-omjb5zjo8w-origin-webp.webp?from=1695864008",
                "original_price": {
                    "currency": "USD",
                    "maximum_amount": "4.19",
                    "minimum_amount": "4.19"
                },
                "sale_region": "US",
                "sales_price": {
                    "currency": "USD",
                    "maximum_amount": "3.5",
                    "minimum_amount": "3.5"
                },
                "shop": {
                    "name": "SANDBOX7398293016815273770"
                },
                "title": "Open Collaboration Coffee Pink Color Meme Card Smiling Lady",
                "units_sold": 5
            }
        ],
        "total_count": 1
    },
    "message": "Success",
    "request_id": "202408081849481CCE26F7477A910041E1"
}
```

如果达人在手机上点击任何商品下的 `detail_link`，它会打开 TikTok 应用并显示商品展示页面（PDP），下方显示合作详情。在下面的示例中，是 **购买按钮** 上方的“每售出一件商品赚取 0.52”文字。


点击此按钮会展开菜单，包含申请免费样品或可购物视频（如适用）的选项，以及将商品添加到展示柜的主要行动号召。例如，一个时尚达人可以使用此 API 搜索生产高质量 T 恤的卖家的开放合作。达人可以通过将所需佣金比例和 T 恤风格传入商品标题搜索来设定。
|  |  |  |
| --- | --- | --- |
| ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/open_collaboration3.PNG?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/open_collaboration4.PNG?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/open_collaboration5.PNG?x-resource-account=public) <br/>  |

### 从合作中移除达人
如果您希望从开放合作中移除达人，可以调用[从合作中移除创作者联盟 API](remove-creator-from-open-collaboration)。
<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：在当前 API 版本中，这将移除达人但不会阻止他们通过联盟链接重新加入。</span>
```curl
curl --location --globoff 'https://open-api.tiktokglobalshop.com/affiliate_seller/202405/open_collaborations/129916503437/remove_creator?app_key=6d0ut2ttps2io&shop_cipher=TTP_bCWokAAAAAA6xm9rY_B9wYFY2QltXcs9&sign=b61b7a13d73cf242f95d9f8ff8f0d46689af5ceba70749f5a267dac54c370869&timestamp=1723143673' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: <redacted' \
--data '{
    "creator_user_id": "7400230764149244970",
    "product_id": "1729568997216587962"
}'

{
    "code": 0,
    "data": {},
    "message": "Success",
    "request_id": "20240808190113870E01A8EAB8AF006987"
}
```

## 创建定向合作
要成功邀请达人参加定向合作，您需要一个达人用户 ID 列表，每次 API 调用最多可以邀请 50 个达人。这意味着您需要按照[创作者授权指南](creator-authorization-guide)中的步骤让达人授权，并拥有修改达人 TikTok 账户的唯一 access token。
要创建定向合作，请按以下步骤操作：

* 使用达人 access token 调用[获取创作者资料 API](get-creator-profile)获取达人用户 ID（如果您的数据库中没有存储）：

```curl
curl --location --globoff 'https://open-api.tiktokglobalshop.com/affiliate_creator/202405/profiles?app_key=6d0ut2ttps2io&sign=4ba5a9531b4c2196cdefde923c270259363398d3fcd05074c0c9302e07f77576&timestamp=1723144188' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: <creator_token>' \
--data ''

{
    "code": 0,
    "data": {
        "avatar": {
            "url": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1594805258216454~c5_100x100.webp?lk3s=a5d48078&nonce=51354&refresh_token=4cda6b090dcbd9854fe8aa7ec2297662&x-expires=1723312800&x-signature=y9Z7uqPuxLEtzus5m7PBg5CeqH4%3D&shp=a5d48078&shcp=2c5759a5"
        },
        "creator_user_id": "7400230764149244970",
        "permissions": [
            "LIVE_STREAM_PERMISSION",
            "ADD_AFFILIATE_PERMISSION"
        ],
        "register_region": "US",
        "selection_region": "US",
        "seller_type": "UNKNOWN",
        "user_type": "TIKTOK_SHOP_CREATOR",
        "username": "testdziwjtmwbq"
    },
    "message": "Success",
    "request_id": "202408081837124EF0047357C9480005DB"
}
```


* [调用创建定向合作 API](create-target-collaboration)：

```curl
curl --location --globoff 'https://open-api.tiktokglobalshop.com/affiliate_seller/202405/target_collaborations?app_key=6d0ut2ttps2io&shop_cipher=TTP_bCWokAAAAAA6xm9rY_B9wYFY2QltXcs9&sign=5ddb3f519b3da61f2f959df81fc42b77441df06626f070ae423e3112a932111a&timestamp=1723144047' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: <redacted>' \
--data-raw '{
    "name": "API Target Collaboration",
    "message": "Created via Postman",
    "end_time": "1723194000",
    "products": [
        {
            "id": "1729569362021748922",
            "target_commission_rate": 2001
        }
    ],
    "creator_user_ids": [
        "7400230764149244970"
    ],
    "seller_contact_info": {
        "email": "test@tiktokshop.com"
    },
    "free_sample_rule": {
        "has_free_sample": true,
        "is_sample_approval_exempt": false
    }
}'

{
    "code": 0,
    "data": {
        "target_collaboration": {
            "id": "7400846837790361387"
        },
        "target_collaboration_conflicts": []
    },
    "message": "Success",
    "request_id": "202408081907271D8F70256ABB65008443"
}
```


* 建议 `end_time` 至少设置为几天后。
* 有时 API 可能在响应中返回 `target_collaboration_conflicts`。这意味着定向合作**未**创建成功。
* 如果成功，应该有一个 `target_collaboration` 对象，包含定向合作 ID。
   * 常见错误包括：
      * `invalid_params`：请检查 `end_time`。
      * `test account and non test account can not cross invite`：如果您邀请多个达人，其中一个或多个与店铺环境不匹配，请从达人列表中移除他们。

### 达人操作
达人可以通过进入 **个人资料 > TikTok Studio > TikTok Shop for 达人**（在变现部分下）**>** 向下滚动到 **TikTok Shop Toolkit > Collab invites** 查找合作邀请。

* 当达人选择感兴趣的合作时，将显示此邀请中的所有商品，他们可以选择将想要推广的商品添加到展示柜。
* 他们可以选择 **全部添加** 或点击单个商品添加。

|  |  |  |  |
| --- | --- | --- | --- |
| ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/target_collaboration1.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/target_collaboration2.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/target_collaboration3.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/target_collaboration4.png?x-resource-account=public) <br/>  |

[搜索创作者定向合作 API](search-creator-target-collaborations) 允许应用搜索达人与特定店铺的所有定向合作。此店铺需要一个 shop ID，可以通过调用[获取授权店铺 API](get-authorized-shops)获取，如上述卖家入驻步骤所述。
```curl
curl --location --globoff 'https://open-api.tiktokglobalshop.com/affiliate_creator/202405/target_collaborations/search?app_key=6d0ut2ttps2io&sign={{sign}}&timestamp={{timestamp}}&page_size=20' \
--header 'content-type: application/json' \
--header 'x-tts-access-token: TTP_VfWnMAAAAADpPV2NiWO2_60_59-jq0QxV6beCG1eHCnsQGa3Znh6huRfzsNsfAjCx3sexUeCzQ35Fi8SZfHTTwVnm-dQD_vk_Jh0YTSdfpp2tmWllFw_4g' \
--data '{
    "shop_id": "7495792013947799738"
}'

{
    "code": 0,
    "data": {
        "next_page_token": "",
        "target_collaborations": [
            {
                "id": "7400846837790361387",
                "name": "API Target Collaboration",
                "products": [
                    {
                        "commission": {
                            "amount": "1.0005",
                            "currency": "USD",
                            "rate": 2001
                        },
                        "id": "1729569362021748922",
                        "main_image_url": "tos-useast5-i-omjb5zjo8w-tx/b22252c5634c4cf58ab44fd630945cc0",
                        "title": "I Got A Bridge To Sell You Model Concrete Test Prod"
                    }
                ],
                "status": "LIVE"
            }
        ],
        "total_count": 1
    },
    "message": "Success",
    "request_id": "202408081923125F67CB063F3DF300AF19"
}
```

## 展示柜交互
### 达人使用 TikTok 应用
当达人在移动设备上点击商品推广链接时，会打开 TikTok 应用并显示 PDP，提示达人将商品添加到展示柜。此提示还会让达人订购免费样品（如果在开放合作中启用），或提示他们制作可购物视频（如果是定向合作）。
### 合作伙伴/卖家使用 API
要调用 API 参考中 **联盟达人** 下列出的任何 API，您需要让达人授权您的应用。按照[此链接中的创作者授权流程](creator-authorization-guide)操作。以下步骤假设您已拥有对其 TikTok 账户进行更改的 token。出于测试目的，如果您尚未拥有 TikTok 达人账户凭证，可以使用上文提供的凭证。


要将商品添加到达人的展示柜，商品必须已作为合作的一部分存在。如果商品合作链接不存在，您可能会收到要求联系 TikTok 的错误。请参考上文了解如何创建定向合作。


要将商品添加到达人的展示柜，您可以调用[添加展示柜商品 API](add-showcase-products)。建议添加可按上述用例生成的联盟链接。


商品添加到展示柜后，达人可以申请免费样品（如果已启用）。
### 达人使用 API
与 TikTok API 集成的应用可以通过调用 Get 橱窗 Products 显示特定达人账户中当前列出的商品。
## 达人免费样品
### 启用免费样品
免费样品只能在联盟中心启用。点击 **未创建** 打开一个模态窗口，允许您指定免费样品规则。唯一必填字段是数量，您可以根据需要调整其他设置。启用免费样品后，您需要生成可与达人分享的商品推广链接。


请参考上述部分：**生成联盟商品推广链接**、**创建开放合作** 和 **创建定向合作**，了解如何生成达人可以申请样品的链接。


<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：如果商品未添加到开放合作，则只生成链接。</span>


将此链接分享给达人，以便他们可以按下图所示添加到展示柜。
### 申请免费样品
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample1.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample2.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample3.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample4.png?x-resource-account=public) <br/>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample5.png?x-resource-account=public) <br/>  |

### 履约免费样品
当达人将商品添加到展示柜时，他们还可以选择申请免费样品（如果可用）。这些样品的申请会显示在联盟中心的[样品申请页面](https://affiliate-us.tiktok.com/product/sample-request?shop_region=US)。如果 auto-approved 设置为 false，卖家可以批准或拒绝这些申请。


批准后，将创建一个样品订单，并应在卖家中心显示。像处理其他订单一样履约此订单。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample6.png?x-resource-account=public)
 ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample7.png?x-resource-account=public)
 ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample8.png?x-resource-account=public)
<span style="color: orange">📌 </span><span style="color: orange"><strong>注意</strong></span><span style="color: orange">：免费样品订单没有暂留期。一旦在卖家中心提供了物流跟踪号（无论是通过 TikTok Shipping 还是卖家 Shipping），状态将从</span><span style="color: orange"><strong>准备发货</strong></span><span style="color: orange">（卖家中心的等待发货）变为</span><span style="color: orange"><strong>已发货</strong></span><span style="color: orange">（卖家中心的等待收取）。</span>
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/free_sample9.png?x-resource-account=public)
达人可以通过进入 **个人资料 > 您的订单 > 样品 > 订单** 查看其样品订单。
## 联盟订单
### TikTok 应用购买流程
<video controls><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/aff1.mp4?x-resource-account=public" type="video/mp4"></video>
<video controls><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/aff2.mp4?x-resource-account=public" type="video/mp4"></video>
### 卖家中心订单
当商品通过联盟流程购买（通过链接或可购物视频）时，它们会出现在[联盟订单部分](https://affiliate-us.tiktok.com/product/order?shop_region=US)。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/seller_center_orders1.png?x-resource-account=public)
这些订单也会在卖家中心创建，并在高亮区域链接。点击订单 ID 将在新窗口中打开卖家中心的订单。这些订单默认有一小时的暂留期。
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Affiliate%20Integration/seller_center_orders2.png?x-resource-account=public)
这些订单也可以通过调用[搜索卖家联盟订单 API](search-seller-affiliate-orders)找到。
### 达人订单
要查找达人生成的订单，您可以调用[搜索创作者联盟订单 API](search-creator-affiliate-orders)。合作伙伴可以检索达人的联盟订单列表，并可以使用订单 ID 来衡量达人产生的转化。
