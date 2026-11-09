# 可购物视频集成解决方案

**重要通知**
API 结构将保持不变，但部分字段名称可能会修改。
请持续关注文档更新。
建议开发者定期查看 **Changelog** 获取最新更新和变更。

🌟 **测试可购物视频**：[【外部】使用你自己的 TikTok 账号测试联盟集成](https://bytedance.sg.larkoffice.com/docx/OB5Zdr0y2oyiikxNZnVlhZNcgCb)


# 简介
本方案面向 **第三方应用和卖家开发者**，涵盖从达人授权 → 获取可带货商品 → 素材制作与上传 → 视频预审与发布（绑定商品锚点）→ 视频数据表现的端到端流程。
> 本方案面向 **3P App / 自研卖家**，提供从达人授权 → 获取可带货商品 → 素材制作与上传 → 视频预审与发布（绑定商品锚点）→ 数据回收的集成解决方案。


# 业务目标

* 让开发者基于稳定的 **Shoppable Content Posting APIs**，为卖家/达人持续产出可挂车视频，提升发布量与转化。
* 支持**批量发布**与**发布**失败原因回传，并为后续广告投放和素材优化提供帮助。
> * 让开发者基于稳定的 **Shoppable Content Posting APIs**，为卖家/达人持续产出可挂车视频，提升发布量与转化。
> * 支持**批量发布**与**发布**失败原因回传，并为后续广告投放和素材优化提供帮助。

# 术语表
| 术语 | 定义 |
| --- | --- |
| 应用需求文档（ARD） | 本文档概述了卖家通过电商平台连接器管理 TikTok Shop 所需的各种使用场景。 |
| 集成流程 | 集成流程是与特定使用场景相关的开发指南。 |
| TTS | TikTok Shop 的缩写。 |
| 买家 | 在 TikTok Shop 上购买商品的买家。 |
| 卖家 | TikTok Shop 卖家 |
| 达人 | 所有内容达人，包括卖家。 |
| 内容 | 达人可以上传到 TikTok Shop 的**所有**可用媒体形式，包括商品展示、视频和直播。还包括所有元数据、字幕和个人资料信息。 |
| 可购物短视频 <br/>  | **可购物短视频**的创建格式与你在 TikTok 上创建任何短视频相同。普通 TikTok 视频与可购物短视频的区别在于，可购物短视频包含一个嵌入式锚点链接，可将观众引导至你要推广的商品。我们发现，精心制作的视频在连接潜在客户和销售方面可以产生巨大影响。**短视频**是吸引观众注意力、激发他们采取行动并推动购买的关键。 |
| 营销账号 <br/>  | 营销账号（最多 4 个）：用于扩大卖家覆盖范围和营销能力的附加账号。营销账号可以销售关联卖家和联盟的商品。 |
| 官方账号 | 官方账号（必填，每店 1 个）：卖家在 TikTok Shop 上的主要品牌展示，拥有专属店铺页面。官方账号只能销售关联卖家账号的商品。 |
| TikTok Shop 短视频官方指南 | https://seller-us.tiktok.com/university/essay?knowledge_id=7096334743553838&from=new-and-updated&role=1&identity=1 |
| TikTok 社区规范 | https://www.tiktok.com/community-guidelines/en/overview |
| Seller Center | TTS 卖家管理店铺、商品、订单、退货/退款等的卖家门户。 |
| 模块 | 模块是电商销售生命周期的子组件。 |
| 功能 | 功能是模块的子组件。功能是产品中一组允许卖家完成一组任务或操作的功能。你如何设计功能将决定最终用户的整体体验。 |
| 使用场景 | 使用场景是卖家或买家可能使用应用的特定情况。 |
| UI 建议 | 开发者在开发阶段需要考虑的具体 UI 建议，以确保应用易于使用。 |
| 应用开发者 | 正在构建应用的合作伙伴/开发者。 |
| 应用审核员 | 应用开发完成后，团队成员将根据你填写的 ARD 审核和测试应用。 |
| Beta 测试员 | 内部审核完成后，我们将邀请卖家对你的应用进行 beta 测试。这些卖家就是 beta 测试员。 |

# 集成流程概览

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e6c0245787624e76a8f208fcd23acbf1~tplv-k9wyc2ijk0-image.image)
# API / Webhook 概览
| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Access Token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) <br/>  | RESTful API | 使用此 API 请求 `access_token` 和 `refresh_token` |
| [Get Creator Profile](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) | RESTful API | 使用此 API 获取达人的个人资料信息。 |
| [Get Shop Products](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Fu3idMqnqoqwTixg2lklALotgSG) <br/>  | RESTful API | 开发者可使用此 API 搜索和获取特定达人绑定的店铺商品信息，支持关键词搜索。 |
| [Get Showcase Products](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405#Back%20To%20Top) <br/>  | RESTful API | 此 API 列出达人橱窗中的商品，按指定页面大小分页，并通过 page token 遍历页面，最多支持橱窗中的 **2000 个商品**。通常在达人希望查看橱窗中的商品时使用此 API。平台将返回橱窗中的商品详情，以及达人正在直播时的直播袋中的商品。 |
| [Upload Shoppable Video File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-EEPudRjSEorRmIxMSX6lFIL8gih) | RESTful API <br/>  | 使用此 API 在发布到 TikTok 之前上传视频 <br/>  |
| [Post Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-U6Sud9fdBodmjwxLRKml4GAfgib) | RESTful API | 使用此 API 发布视频。请求支持 `video_info.is_ai_generated` 字段来标识 AI 生成内容；省略时该字段默认为 `false`。当存在内容发布配额限制时，响应可能包含 `data.video.quota`。 |
| [Get Shoppable Video Status](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-J9uCdO4Ulo3RAjxscIUlKib1gGf) | RESTful API | 使用此 API 获取视频发布结果 |
| [Pre-check Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-GEyCdCNhGoAZ5TxbVetli7SbgLc) | RESTful API <br/>  | 使用此 API 预审视频和可购物内容锚点是否存在违规 <br/>  |
| [Get Shoppable Video Pre-check Result](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-WYbCdyN1ToT52TxtU3ClrUuHgkc) | RESTful API | 使用此 API 获取视频预审结果 |
| [Shoppable Video Precheck Result](https://partner.tiktokshop.com/docv2/page/arpnre1g) <br/>  | Webhook | 当调用 Precheck Video Content API 时触发视频预审结果 webhook，提供视频质量评估和违规检查的结果。 |
| [Get Shop Video Performance List](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-list-202409) <br/>  | RESTful API <br/>  | 返回店铺下所有视频的整体表现指标。此 API 目前仅提供在美国、英国、新加坡、越南和泰国注册的店铺数据。 |
| [Get Shop Video Performance Detail](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-details-202409) | RESTful API | 返回（请求的）视频的详细表现指标。此 API 目前仅提供在美国、英国、新加坡、越南和泰国注册的店铺数据。 |
| [Get Creator Video Performance Detail](https://bytedance.sg.larkoffice.com/docx/VkfxdgvBCoL4gMxpZJslZ8xmgcg) | RESTful API | 这是目前仅限美国达人的 API。用于获取 TikTok 电商视频指标（包括 anchor_display_rate、ctr、orders、items_sold、gmv）进行分析。 |
# 建议的集成流程
| **模块** | **功能** | **使用场景** | 集成流程 |
| --- | --- | --- | --- |
| 可购物视频 <br/>  | 达人授权与取消授权 <br/>  | [UC-161111](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-CikMddDSIozcWSxwJ0Kl8LX7gxe)：支持达人完成对开发者应用的授权或取消授权。 <br/> > 支持达人可以完成达人授权或者解除授权。 | IF-161111.V1 |
|  | 获取达人类型和商品信息 <br/> > 获取达人类型与可带货商品 <br/>  <br/>  | [UC-161121](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Xjf7dGbxeo6WVQxX3rSlolSqgmd)：获取达人类型。 <br/> > 获取达人类型。 | IF-161121.V1 |
|  |  | [UC-161122：](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Xjf7dGbxeo6WVQxX3rSlolSqgmd)获取对应达人类型可带货的商品（含主图、标题、SKU）。 <br/> > 获取对应达人类型可带货的商品（含主图、标题、SKU） | IF-161122.V1 |
|  | 上传视频 <br/>  <br/>  | [UC-161131](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-E9SldzIRGotErGx6W4Vl6Vaqgtc)：卖家使用商品图片/信息生成短视频。 <br/> > 卖家使用商品图片/信息生成短视频 | IF-161131.V1 |
|  |  | [UC-161132](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-HfpGdkpvYoySwOxjdTElavyFgzc)：上传视频至 TikTok Shop。 <br/> > 上传视频至 TikTok Shop | IF-161132.V1 |
|  | 预审并发布可购物视频（绑定锚点） <br/> > 预审并发布Shoppable Video <br/>  <br/>  | [UC-161141](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-TrtBdldZgo9zoCxrdt4lrx6lgCX)：卖家提交视频进行预审。 <br/> > 卖家提交视频进行预审。 | IF-161141.V1 |
|  |  | [UC-161142](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-JqH1dpyXVogxiKxQREllX0p1gPh)：发布挂车视频，绑定商品锚点。 <br/> > 发布挂车视频，绑定商品锚点 | IF-161142.V1 |
|  |  | [UC-161143](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Rt3CdlJzXoIzzZxJvAZl7Ym4g2b)：获取挂车视频发布最终结果，若失败，获取失败原因并提示修改/重试。 <br/> > 获取挂车视频发布最终结果，若失败，获取失败原因并提示修改/重试。 | IF-161143.V1 |
|  |  | [UC-161144](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Nj6GdD2FIowNqXxyYP2ltjaBgff)：获取预审结果。如果预审失败，服务商必须在系统中阻断发布操作，防止卖家上传不合规内容。 <br/> > 获取precheck结果。如果预审失败，服务商必须禁止卖家发对应的挂车视频。 | IF-161144.V1 |
|  |  | [UC-161145](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#V7rMdNcugo8irwxnaFTlBb3JgJh)：获取优质检查结果。帮助卖家提前了解视频是否被视为高质量内容，如不是则提供可执行的优化建议。即使返回了建议，视频仍可发布；此检查不应阻断发布流程。 <br/>  | IF-161145.V1 <br/>  |
|  | 店铺视频数据表现 <br/> > 视频数据分析 <br/>  <br/>  | [UC-161151](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Y4grdqZ36oHiHdxkFtulzMgRgph)：获取店铺下的视频表现数据。 <br/> > 获取店铺下的视频表现数据 | IF-161151.V1 |
|  | 视频关联音乐和设置封面 <br/> > 视频关联音乐和设置封面 | [UC-161161](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-KrJJdRN0XoHR5AxYiBIlpQHkgub)：可购物视频发布支持视频封面图片。 | IF-161161.V1 <br/>  |
|  |  | [US-161162](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-C505denogolCDCxOG2dlq6A1gnf)：搜索音乐 | IF-161161.V1 |
|  |  | [UC-161163](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Bi0adv0ZPoWE3cxgJPPl2CNVgXg)：可购物视频发布支持绑定音乐。 | IF-161162.V1 |

## 达人授权与取消授权
### **IF-161111.V1 支持达人完成对开发者应用的授权或取消授权**

1. 在开发者应用中，卖家登录自己的达人账号完成授权，可通过网页端或移动端完成账号登录与授权确认。
2. 同时，根据合规要求，开发者应用必须支持达人在任何时间撤销授权。开发者需在系统中提供便捷的"取消授权"功能入口，确保达人可自主管理其授权状态。
3. 更多如何支持达人授权的详细说明，请参考：[https://partner.tiktokshop.com/docv2/page/creator-authorization-guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide)
> 1. 开发者应用中，卖家登录自己的达人账号完成授权，可通过网页端或移动端完成账号登录与授权确认。
> 2. 同时，根据合规要求，开发者应用必须支持达人在任何时间撤销授权。开发者需在系统中提供便捷的"取消授权"功能入口，确保达人可自主管理其授权状态。
> 3. 更多如何支持达人授权的详细说明，请参考：https://partner.tiktokshop.com/docv2/page/creator-authorization-guide

UI 建议：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5e8fde9a94ba43b5b8be4439279d38eb~tplv-k9wyc2ijk0-image.image)


| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Access Token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) | RESTful API | 使用此 API 请求 `access_token` 和 `refresh_token` |
## 获取达人类型和商品信息
### **IF-161121.V1 获取达人类型**

1. 卖家可在开发者的应用内选择需要授权的达人并展示达人对应的类型，不同类型的达人可以带货的商品范围是不同的。
2. 可以通过 Get 达人 Profile 中 user_type 的出参来支持卖家筛选达人类型：
   * `TIKTOK_SHOP_OFFICIAL_ACCOUNT` 代表卖家官方号
   * `TIKTOK_MARKETING_ACCOUNT` 代表卖家渠道号
   * `TIKTOK_SHOP_CREATOR` 代表联盟达人
> 1. 卖家可在开发者的应用内选择需要授权的达人并展示达人对应的类型，不同类型的达人可以带货的商品范围是不同的。
> 2. 可以通过Get 达人 Profile 中 user_type的出参来支持卖家筛选达人类型
>    * TIKTOK_SHOP_OFFICIAL_ACCOUNT代表卖家官方号
>    * TIKTOK_MARKETING_ACCOUNT代表卖家渠道号
>    * TIKTOK_SHOP_CREATOR代表联盟达人


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/23f5f2fedf3a4338ac8f149765afc190~tplv-k9wyc2ijk0-image.image)
API/通知概览
| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Creator Profile](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) | RESTful API | 使用此 API 获取达人的个人资料信息。 |
### **IF-161122.V1 获取对应达人类型可带货的商品（含主图、标题、SKU）**

1. 支持卖家选择达人对应类型可带货的商品：
   * 如果是 `TIKTOK_MARKETING_ACCOUNT`/`TIKTOK_SHOP_OFFICIAL_ACCOUNT`，则需要通过调用 **Get Shop Products** API 获取该达人可以带货的商品信息。
   * 如果是 `TIKTOK_SHOP_CREATOR`，则需要调用 **Get 橱窗 Products** API 获取该达人橱窗中的商品信息。
2. 可在应用中通过接口返回的商品信息对应展示商品的基础信息（例如商品名称、主图等），提升卖家选择商品的效率和体验。
> 1. 支持卖家选择达人对应类型可带货的商品
>    * 如果是`TIKTOK_MARKETING_ACCOUNT`/`TIKTOK_SHOP_OFFICIAL_ACCOUNTT`，则需要通过调用Get Shop Products接口获取该达人可以带货的商品信息。
>    * 如果是TIKTOK_SHOP_CREATOR，则需要调用Get 橱窗 Products接口获取该达人橱窗橱窗内的商品信息，如果added_status不是ADDED则代表商品未加入到橱窗，可以通过调用Add 橱窗 Products接口将商品添加到橱窗。
> 2. 可在应用中通过接口返回的商品信息对应展示商品的基础信息例如商品名称、主图等，提升卖家选择商品的效率和体验


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/71b39d864a314d9abed26f8b8f2c5d26~tplv-k9wyc2ijk0-image.image)
注意

1. 在 **Get 橱窗 Products** 中，请关注商品的状态满足以下条件：
* `inventory_status`: `IN_STOCK`
* `review_status`: `"APPROVED"`
* `is_hidden`: `false`
* `added_status`: `ADDED`
> 1. 在Get 橱窗 Products中，请关注商品的状态满足以下条件：
>    *  inventory_status: IN_STOCK,
>    *  review_status: "APPROVED",
>    *  is_hidden: false,
>    *  added_status: ADDED
> 2. 在Get Shop Products，请关注商品的状态，请关注商品的状态满足以下条件：
>    * added_status：ADDED

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Shop Products](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Fu3idMqnqoqwTixg2lklALotgSG) | RESTful API | 开发者可使用此 API 搜索和获取特定达人绑定的店铺商品信息，支持关键词搜索。 |
| [Get Showcase Products](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405#Back%20To%20Top) | RESTful API <br/>  | 此 API 列出达人橱窗中的商品，按指定页面大小分页，并通过 page token 遍历页面，最多支持橱窗中的 2000 个商品。通常在达人希望查看橱窗中的商品时使用此 API。平台将返回橱窗中的商品详情，以及达人正在直播时的直播袋中的商品。 |

## 上传视频
### **IF-161131.V1 卖家使用商品图片/信息生成短视频**

1. 卖家可通过开发者的应用基于商品的主图、标题、SKU 等信息自动化或半自动化生成短视频内容。
2. 在视频生成过程中需遵守 TikTok 社区规范和 TikTokShop 短视频官方指南，请确保素材内容合规并且符合平台优质视频规范。生成的视频将在后续通过 Shoppable Video API 上传并发布。
> 1. 卖家可通过开发者的应用基于商品的主图、标题、SKU 等信息自动化或半自动化生成短视频内容
> 2. 在视频生成过程中需遵守 TikTok社区规范 和 TikTokShop 短视频官方指南，请确保素材内容合规并且符合平台优质视频规范。生成的视频将在后续通过 Shoppable Video API 上传并发布。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b5c1fd06ad234d94839509f6d57a2323~tplv-k9wyc2ijk0-image.image)
备注

1. 视频格式规范
   * 支持格式：MP4、MOV、MKV、WMV、WEBM、AVI、3GP、FLV、MPEG
   * 最大文件大小：100 MB
   * 视频宽高比：9:16 至 16:9
   * 分辨率：HD 720p 及以上
   * 时长：>30 秒
> 1. 视频格式规范
>    * 支持格式：MP4、MOV、MKV、WMV、WEBM、AVI、3GP、FLV、MPEG
>    * 最大文件大小：100 MB
>    * 视频宽高比：9:16 至 16:9（推荐 9:16）
>    * 视频时长：建议 >30 秒
>    * 分辨率：推荐 720p 及以上


| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Creator Profile](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) | RESTful API | 使用此 API 获取达人的个人资料信息。 |
| [Get Shop Products](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Fu3idMqnqoqwTixg2lklALotgSG) | RESTful API | 开发者可使用此 API 搜索和获取特定达人绑定的店铺商品信息，支持关键词搜索。 |
| [Get Showcase Products](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405#Back%20To%20Top) | RESTful API <br/>  | 此 API 列出达人橱窗中的商品，按指定页面大小分页，并通过 page token 遍历页面，最多支持橱窗中的 2000 个商品。通常在达人希望查看橱窗中的商品时使用此 API。平台将返回橱窗中的商品详情，以及达人正在直播时的直播袋中的商品。 |
### **IF-161132.V1 上传视频至 TikTok Shop**

1. 在卖家正式发布挂车视频之前，必须先调用 **Upload Video File** 接口，将视频文件上传至 TikTok Shop 平台，并获取一个唯一的 `file_id`。该 `file_id` 将作为后续**视频发布的**必要入参。
2. 目前上传接口不支持对已上传的视频进行修改，如需调整视频内容，必须重新生成并再次上传。
> 1. 在卖家正式发布挂车视频之前，必须先调用 Upload Video File 接口，将视频文件上传至 TikTok Shop 平台，并获取一个唯一的 `file_id`。该 `file_id` 将作为后续 **视频发布的**必要入参。
> 2. 目前上传接口不支持对已上传的视频进行修改，如需调整视频内容，必须重新生成并再次上传。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/bece427c7d684f1fbab16edf1d3ff634~tplv-k9wyc2ijk0-image.image)
**注意**

1. 上传视频文件成功**不代表**一定能发布挂车视频，如不符合平台规范仍会在挂车视频审核环节失败。
2. 上传接口返回结果中包含 `video_file.md5` 字段（上传文件的 MD5 校验值）。服务商系统可在上传前自行计算本地文件的 MD5，与返回值比对，用于：
   * 确认上传文件与本地文件一致，避免因网络抖动导致的文件损坏。
   * 做断点续传/幂等上传时的文件唯一性校验。
> 1. 上传视频文件成功不代表一定能发布挂车视频，如不符合平台规范仍会在挂车视频审核环节失败。
> 2. 上传接口返回结果中包含 `video_file.md5` 字段（上传文件的 md5 校验值）。服务商系统可在上传前自行计算本地文件的 md5，与返回值比对。用于：
>    * 确认上传文件与本地文件一致，避免因网络抖动导致的文件损坏；
>    * 做断点续传/幂等上传时的文件唯一性校验。

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Upload Shoppable Video File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-EEPudRjSEorRmIxMSX6lFIL8gih) <br/> <br/> **注意**：使用 [Upload Shoppable Video File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-EEPudRjSEorRmIxMSX6lFIL8gih) API 时，<br/> 如果视频 >= 10MB，必须遵循 [可购物视频大文件上传方案](https://bytedance.sg.larkoffice.com/docx/WTMvdfbTBo30Fex0r9YlYstGg0d?from=from_parent_docx) | RESTful API | 使用此 API 在发布到 TikTok 之前上传视频 <br/>  |
## 预审并发布可购物视频（绑定锚点）
### **IF-161141.V1 卖家提交视频进行预审**

1. 在卖家发布挂车视频之前，服务商需确保视频内容满足以下要求：
   * [底线原则] **TikTok 社区规范**：视频必须符合平台的社区规则，否则将作出对应违规处罚。
   * [底线原则] **TTS 电商平台治理规则**：视频不得涉及违规商品、违规展示或其他违反电商治理的内容，否则将作出对应违规处罚。——**✅API 已支持**
   * [强烈推荐] **优质视频规则**：平台鼓励视频满足优质视频标准，优质视频将会获得更多的 GMV 收益。
2. **预审接口**

 我们现已提供 **预审接口（Pre-check API）**，支持 ISV 在视频发布前调用接口，验证视频内容是否符合 **TTS 电商治理规则（TTS E-commerce Governance Rules）**。接口会帮助卖家在视频发布前识别违规风险，防止内容违规。

   * **预审接口的配额管理**：
      * 每个达人账号每日拥有 **50 次预审配额**。预审的配额在 API 渠道和非 API 渠道**独立配置**，互不影响。例如，如果达人今天在非 API 渠道有 **50 个预审配额**，那么在 API 渠道也会有**单独的 50 个配额**。两个渠道之间的配额**不会互相抵扣或影响**。
      * 当日配额使用完毕后，将无法发起新的预审任务。
      * 每一次成功创建**预审任务（precheck task）**的 API 调用会消耗一次配额。如同一个视频（file_id）被多次预审，将生成多个任务，每次调用都会消耗一次配额。

⚠️ **重要提示**

* 预审接口**不会**判断视频是否**高质量**，也不会验证是否符合 **TikTok 社区规范**。
3. 服务商在系统中需要设计必要的预审检查能力，以便在平台校验之外，进一步保障视频合规性与内容质量。
> 1. 在卖家发布挂车视频之前，服务商需确保视频内容满足以下要求：
>    * **[底线原则] TikTok Community Guidelines（TikTok 社区规范）**：视频必须符合平台的社区规则，否则将作出对应违规处罚
>    * **[底线原则] TTS 电商平台治理规则**：视频不得涉及违规商品、违规展示或其他违反电商治理的内容，否则将作出对应违规处罚。
>    * **[强烈推荐] 优质视频规则**：平台鼓励视频满足优质视频标准，优质视频将会获得更多的GMV收益。
> 2. **预审接口已提供**

> 我们现已提供 **预审接口（Pre-check API）**，支持 ISV 在视频发布前调用接口，验证视频内容是否符合 **TTS 电商治理规则（TTS E-commerce Governance Rules）**。接口会帮助卖家在视频发布前识别违规风险，防止内容违规。

> * **预审接口的配额管理**：
>    * 每个达人账号每日拥有50次预审配额。预审的配额在API渠道和非API渠道独立配置，互不影响。例如，如果达人今天在非API渠道有50个配额，那么在API渠道也会有50个配额，两个渠道之间的配额 **不会互相抵扣或影响。**
>    * 当日配额使用完毕后，将无法发起新的预审任务。建议在系统中做好必要提示。
>    * 每一次成功创建 **预审任务（precheck task）** 的 API 调用会消耗一次配额。如同一个视频（`file_id`）被多次预审，将生成多个任务，每次调用都会消耗一次配额。
> 3. 服务商在系统中需要设计必要的预审检查能力，以便在平台校验之外，进一步保障视频合规性与内容质量。

>
> 请参阅以下三份文档了解更多详情：

> 1. **[底线原则] TikTok 社区规范**：[Community Guidelines](https://www.tiktok.com/community-guidelines/en/overview)
> 2. **[底线原则] TTS 电商平台治理规则：**[✨Creator Policy Pulse (August 2025)✨](https://seller-us.tiktok.com/university/essay?knowledge_id=7096334743553838&from=new-and-updated&role=1&identity=1)
> 3. **[强烈推荐] 优质视频规则**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/59eb6d23a22f4af89e65ce6b4759f08e~tplv-k9wyc2ijk0-image.image)

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| 预检可购物视频  | RESTful API | 使用此 API 预审视频和可购物内容锚点是否存在违规 |
| 获取可购物视频预检结果  | RESTful API | 使用此 API 获取视频预审结果 |
| 可购物视频预检结果 | Webhook | 通知开发者视频预审结果 |
### **IF-161142.V1 发布挂车视频，绑定商品锚点**

1. 卖家在发布挂车视频前，开发者应用需要支持卖家在应用中填写以下信息，完成后才可以提交发布挂车视频。
   * **视频文案（`caption`）**：作为视频的标题与说明，支持包含话题标签 `#` 和用户提及 `@`，有助于视频分发与曝光。
   * **视频文件 ID（`file_id`）**：来自于上传接口返回结果，是视频的唯一标识。
   * **关联商品（`product_id`）**：从「Get Shop Products」或「Get 橱窗 Products」接口获取，用于将商品锚点绑定到视频中。
   * **商品锚点文案（`anchor_title`）**：展示在挂车位的标题，帮助用户快速理解商品卖点。
   * **AI 生成内容标识（`video_info.is_ai_generated`）**：可选布尔字段，用于声明提交的视频是否由 AI 生成。AI 生成内容应传 `true`，发布后的帖子会展示 AI-generated 标签；字段省略时默认为 `false`。
> 1. 卖家在发布挂车视频前，开发者应用需要支持卖家在应用中填写以下信息，完成后才可以提交发布挂车视频。
>    * **视频文案（caption）**：作为视频的标题与说明，支持包含话题标签 `#` 和用户提及 `@`，有助于视频分发与曝光。
>    * **视频文件 ID（file_id）**：来自于上传接口返回结果，是视频的唯一标识。
>    * **关联商品（product_id）**：从「Get Shop Products」或「Get 橱窗 Products」接口获取，用于将商品锚点绑定到视频中。
>    * **商品锚点文案（anchor_title）**：展示在挂车位的标题，帮助用户快速理解商品卖点。
>    * **AI 生成内容标识（video_info.is_ai_generated）**：可选布尔字段，用于声明提交的视频是否由 AI 生成。AI 生成内容应传 `true`，发布后的帖子会展示 AI-generated 标签；字段省略时默认为 `false`。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fa92ac11f0294846aad91e23da902f6f~tplv-k9wyc2ijk0-image.image)
调用 `Post Shoppable Video` 后，接口可能随 `data.video.id` 返回 `data.video.quota`，用于提示达人当前内容发布配额。字段存在时建议展示友好提示；字段未返回时表示当前无适用配额限制，不应按错误处理。
> 调用 `Post Shoppable Video` 后，接口可能随 `data.video.id` 返回 `data.video.quota`，用于提示达人当前内容发布配额。字段存在时建议展示友好提示；字段未返回时表示当前无适用配额限制，不应按错误处理。


注意

1. **挂车视频必填字段**
   * **`video_info.file_id`**：上传接口返回的文件 ID。
   * **`video_info.title`**：视频标题/文案，最长 4000 个字符，支持 `#` 和 `@`。
   * **`tts_anchor_info.product_id`**：需要挂载的商品 ID。
   * **`tts_anchor_info.title`**：商品锚点展示文案，不超 30 个字符，不能带标点和 emoji。
2. **内容合规**
   * 视频文案与锚点文案需符合 **TikTok 社区规范**和 **TikTok Shop 视频政策**。
   * 商品必须是可带货商品，且与视频内容保持相关性。
3. **挂车短视频发布量限制**
   * 不同账号有不同的限制。请阅读卖家大学的政策，例如[美国本地商家政策](https://seller-us.tiktok.com/university/essay?knowledge_id=6939143037667118#posting-limits-for-shoppable-content-us-)
> 1. **挂车视频必填字段**
> * `video_info.file_id`：上传接口返回的文件 ID。
> * `video_info.title`：视频标题/文案，最长 4000 个字符，支持 `#` 和 `@`。
> * `tts_anchor_info.product_id`：需要挂载的商品 ID。
> * `tts_anchor_info.title`：商品锚点展示文案，不超30个字符，不能带标点和emoji。
> 2. **内容合规**
> * 视频文案与锚点文案需符合 TikTok 平台社区规范和电商视频规范
> * 商品必须是可带货商品，且与视频内容保持相关性。
> 3. **挂车短视频发布量限制**
> * 不同账号有不同的限制。请阅读卖家大学的政策，以[美国跨境商家大学的政策](https://seller.tiktokshopglobalselling.com/university/essay?knowledge_id=2564695663953681&shop_region=us&identity=1&anchor_link=EC4200CA)为例

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Post Shoppable Video](https://partner.tiktokshop.com/docv2/page/post-shoppable-video-202607#Back%20To%20Top) <br/>  | RESTful API | 使用此 API 发布视频。适用时设置 `video_info.is_ai_generated`；省略时默认为 `false`。响应可能包含 `data.video.quota`。 |
### **IF-161143.V1 获取挂车视频发布最终结果，若失败，获取失败原因并提示修改/重试**

1. 卖家通过 **Post Shoppable Video API** 提交发布后，会获得一个 `video_id`。最终的发布状态（成功/失败/处理中）可以通过以下两种方式获取：
   * **主动查询（GET）**：开发者应用可定期调用查询接口，根据 `video_id` 获取最新状态。该接口仅返回视频的发布结果。
   * **Webhook 推送**：当视频发布状态发生变更时，平台会向开发者应用配置的回调地址推送事件。该 webhook 不仅包含视频发布结果，还会返回失败原因的枚举值。开发者可根据返回的结果和失败原因，引导卖家修改视频并重新提交。
> 1. 卖家通过 Post Shoppable Video API 提交发布后，会获得一个 `video_id`。最终的发布状态（成功 / 失败 / 处理中）可以通过以下两种方式获取：
>    * **主动查询（GET）**：开发者应用可定期调用查询接口，根据 `video_id` 获取最新状态。该接口仅返回视频的发布结果。
>    * **Webhook 推送**：当视频发布状态发生变更时，平台会向开发者应用配置的回调地址推送事件。该 webhook 不仅包含视频发布结果，还会返回失败原因的枚举值。开发者可根据返回的结果和失败原因，引导卖家修改视频并重新提交。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/510cb271f1014bc49ba32f3b9de7d28c~tplv-k9wyc2ijk0-image.image)
**注意**

1. 当调用了发布接口，代表 `file_id` 已被消费不能再次使用。
> 1. 当调用了发布接口，代表 `file_id` 已被消费不能再次使用。

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Shoppable Video Status](https://partner.tiktokshop.com/docv2/page/get-shoppable-video-status-202509) | RESTful API | 使用此 API 获取视频发布结果 |
| ~~视频发布结果~~ | ~~Webhook~~ | ~~通知开发者视频发布结果及失败原因~~ |
### **IF-161144.V1 获取预审结果。如果预审失败，服务商必须在系统中阻断发布操作，防止卖家上传不合规内容。**

* **强阻断逻辑**：当预审未通过时，服务商**必须在系统中阻断**卖家的发文操作，防止卖家上传不合规的视频。系统需清晰展示预审结果，包括 **result**、**risk**、**suggestions**。
* 预审接口仅会返回视频是否符合 **TTS 电商治理规则（TTS e-commerce governance rules）** 的结果，**无法完全保证**视频始终符合平台的所有合规政策要求，因为 **TTS 的治理规则和内容政策会动态更新**。



> * **强阻断逻辑**：当预审未通过时，ISV **必须在系统中阻断** 卖家的发文操作，防止卖家上传不合规的视频。

>  系统需清晰展示预审结果，包括 **result**、**risk**、**suggestions**，并提示警告信息，例如："您的视频不符合平台规范，无法发布"

> * 预审接口仅会返回视频是否符合 **TTS 电商治理规则（TTS e-commerce governance rules）** 的结果，

> **无法完全保证** 视频始终符合平台的所有合规政策要求，因为 **TTS 的治理规则和内容政策会动态更新**。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fa399a54e62b41eabe59bc1409570437~tplv-k9wyc2ijk0-image.image)
| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Pre-check Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-GEyCdCNhGoAZ5TxbVetli7SbgLc) | RESTful API | 使用此 API 预审视频和可购物内容锚点是否存在违规 |
| [Get Shoppable Video Pre-check Result](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-WYbCdyN1ToT52TxtU3ClrUuHgkc) | RESTful API | 使用此 API 获取视频预审结果 |
| [Shoppable Video Precheck Result](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-NdUqdt1ACoNmxvx5VdYlYr7xgUf) | Webhook | 通知开发者视频预审结果 |
### IF-161145.V1 获取优质检查结果
**免责声明**
预检查结果仅供参考，无法保证公开视频后的最终审核结果。最终结果还可能受到 TikTok Shop 平台政策、账号状态及其他因素的影响。平台的建议内容可能会随着政策调整而实时更新，请以最新返回的结果为准。
> **免责声明**
> 预检查结果仅供参考，无法保证公开视频后的最终审核结果。最终结果还可能受到 TikTok Shop 平台政策、账号状态及其他因素的影响。平台的建议内容可能会随着政策调整而实时更新，请以最新返回的结果为准。


1. ISV 可以调用 **Get Shoppable Video Pre-check Result API** 并订阅 **Shoppable Video Precheck Result webhook** 来获取「**优质检查（good quality check）**」结果。

 这可以帮助卖家提前了解其视频是否被认为是高质量内容；如果未通过，也会返回可执行的优化建议。即使返回了建议，视频**仍然可以发布**，该检查**不应阻塞发布流程**。

2. **调用时机**：

 该 API **仅应在视频文件上传完成（已获得 `file_id`）之后、执行 "post shoppable video" 操作之前调用**，以避免在其他场景下被误用。

3. **配额管理**：
   1. 「**优质检查（Good quality check）**」对每个达人账号**每日最多支持 50 次检查，并且次数与合格检查共享**。
   2. 当超出配额时，API 将返回错误信息：`The creator account has reached the daily limit for pre-checks. Please try again tomorrow` 开发者应对此进行处理，并向用户提供**友好的提示信息**。
4. **适用范围**：
   1. 「优质检查（Good quality check）」目前**仅在 US 地区生效**，其他地区暂不支持。
   2. 该能力适用于**卖家达人账号及联盟达人账号发布的视频**。
> 1. ISV 可以调用 **Get Shoppable Video Pre-check Result API** 并订阅 **Shoppable Video Precheck Result webhook** 来获取「**优质检查（good quality check）**」结果。

>  这可以帮助卖家提前了解其视频是否被认为是高质量内容；如果未通过，也会返回可执行的优化建议。即使返回了建议，视频**仍然可以发布**，该检查**不应阻塞发布流程**。

> 2. **调用时机**：

>  该 API **仅应在视频文件上传完成（已获得** **`file_id`）之后、执行 "post shoppable video" 操作之前调用**，以避免在其他场景下被误用。

> 3. **配额管理**：
>    1. 「**优质检查（Good quality check）**」对每个达人账号**每日最多支持 50 次检查，并且次数与合格检查共享**。
>    2.  当超出配额时，API 将返回错误信息：`The creator account has reached the daily limit for pre-checks. Please try again tomorrow`开发者应对此进行处理，并向用户提供**友好的提示信息**。
> 4. **适用范围：**
>    1. 「优质检查（Good quality check）」目前**仅在 US 地区生效**，其他地区暂不支持。
>    2. 该能力适用于**卖家达人账号及联盟达人账号发布的视频**；


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/33a8d0d2810b479db28bbd21f3185a95~tplv-k9wyc2ijk0-image.image)
**API/通知概览**
| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Precheck Video Content](https://partner.tiktokshop.com/docv2/page/precheck-video-content-202511) | RESTful API | 使用此 API 预审视频和可购物内容锚点是否存在违规 |
| [Get Shoppable Video Pre-check Result](https://partner.tiktokshop.com/docv2/page/get-shoppable-video-precheck-result-202601) | RESTful API | 使用此 API 获取视频预审结果，包括优质检查结果。 |
| [Shoppable Video Precheck Result](https://partner.tiktokshop.com/docv2/page/arpnre1g) | Webhook <br/>  | 通知开发者视频预审结果，包括优质检查结果。 |
## 店铺视频数据表现
### IF-161151.V1 获取店铺下的视频表现数据

1. 需要支持卖家完成店铺数据授权，和 posting shoppable video 的接口的授权类型不同。[查看如何进行卖家授权](https://partner.tiktokshop.com/docv2/page/seller-authorization-guide#Authorization%20in%20development%20stage)
2. 支持卖家在应用中查看视频表现数据。卖家可以查看店铺所有视频或某个特定视频的表现，包括核心经营指标和互动数据，帮助评估视频效果和用户参与度。
3. 支持的数据：
   1. **核心经营指标**：
      * `gmv.amount`
      * `click_through_rate`
      * `daily_avg_buyers`
      * `views`
   2. **互动数据**：
      * `likes`
      * `shares`
      * `xcomments`
      * `views`
> 1. 需要支持卖家完成店铺数据授权，和posting shoppable video的接口的授权类型不同。[Check how to do seller auth](https://partner.tiktokshop.com/docv2/page/seller-authorization-guide#Authorization%20in%20development%20stage)
> 2. 支持卖家在应用中查看视频表现数据。卖家可以查看店铺所有视频或某个特定视频的表现，包括核心经营指标和互动数据，帮助评估视频效果和用户参与度。
> 3. **支持的数据**
>    1. **核心经营指标**：
>       * GMV（成交金额）；
>       * CTR（点击率）；
>       * 日均买家数（daily_avg_buyers）；
>       * 观看量（views）。
>    2. **互动数据**：
>       * 点赞总数（likes）；
>       * 分享总数（shares）；
>       * 评论总数（comments）；
>       * 播放总数（views）。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e3bc9599ea649799a885363becc8f69~tplv-k9wyc2ijk0-image.image)
注意：

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Get Shop Video Performance List](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-list-202409) <br/>  | RESTful API <br/>  | 返回店铺下所有视频的整体表现指标。此 API 目前仅提供在美国、英国、新加坡、越南和泰国注册的店铺数据。 |
| [Get Shop Video Performance Detail](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-details-202409) | RESTful API | 返回（请求的）视频的详细表现指标。此 API 目前仅提供在美国、英国、新加坡、越南和泰国注册的店铺数据。 |
| [Get Creator Video Performance Detail](https://bytedance.sg.larkoffice.com/docx/VkfxdgvBCoL4gMxpZJslZ8xmgcg) | RESTful API | 这是目前仅限美国达人的 API。用于获取 TikTok 电商视频指标（包括 anchor_display_rate、ctr、orders、items_sold、gmv）进行分析。 |
## 视频关联音乐和设置封面
### IF-161162.V1 可购物视频发布支持视频封面图片

1. 在开发者应用中，卖家发布可购物视频（Shoppable Video）时需要能够设置视频的封面，以提升内容的吸引力。为满足此需求，卖家在调用接口时可提供以下任一信息：
   * **封面图片 URI（`cover_uri`）**：通过 `Upload Shoppable Photo File` 接口预先上传一张图片，并将其返回的 `uri` 作为视频封面。
   * **封面时间戳（`cover_timestamp_ms`）**：指定视频中的一个具体时间点（以毫秒为单位），系统将截取该时间点的视频帧作为封面。
2. 开发者应用需明确告知卖家两种设置方式的优先级：
   * 如果同时提供了 `cover_uri` 和 `cover_timestamp_ms`，系统将优先采用 `cover_uri` 作为封面。
   * 如果两者均未提供，系统将默认使用已上传视频的第一帧作为封面。
> 1. 在开发者应用中，卖家发布可购物视频（Shoppable Video）时需要能够设置视频的封面，以提升内容的吸引力。为满足此需求，卖家在调用接口时可提供以下任一信息：
>    * **封面图片 URI (`cover_uri`)**：通过 `Upload Shoppable Photo File` 接口预先上传一张图片，并将其返回的 `uri` 作为视频封面。
>    * **封面时间戳 (`cover_timestamp_ms`)**：指定视频中的一个具体时间点（以毫秒为单位），系统将截取该时间点的视频帧作为封面。
> 2. 开发者应用需明确告知卖家两种设置方式的优先级：
>    * 如果同时提供了 `cover_uri` 和 `cover_timestamp_ms`，系统将优先采用 `cover_uri` 作为封面。
>    * 如果两者均未提供，系统将默认使用已上传视频的第一帧作为封面。
> * 封面内容（无论是上传的图片还是视频截图）必须遵守 **TikTok 社区规范**与 **TikTok Shop 电商视频政策**。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/112607dc28ec43ce9b4fb555050f4a56~tplv-k9wyc2ijk0-image.image)
| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Post Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-TV8qdaPDLo49yxxamEblRomKgMh) | RESTful API | 使用此 API 发布带有指定封面的视频。 |
| [Upload Shoppable Photo File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#IGBzdu65Ao0Urdxqj00lPH69gPo) | RESTful API | 使用此 API 上传图片文件并获取其 URI 用于封面。 |
### IF-161161.V1 搜索音乐
在卖家发布挂车内容前，开发者应用可以支持卖家在应用中通过输入**关键词**搜索音乐，搜索到的音乐支持播放，可以在后续挂车步骤中直接使用。**接口查询获取的音乐均为有电商权限的音乐，可直接使用，无违规风险。**

* **音乐 ID（music_id）**：搜索到的音乐关联的唯一 ID，在后续挂车步骤中可直接使用。
* **关键词（keyword）**：用户输入的搜索词，用于匹配音乐名称或作者。
* **语言（language）**：支持定义返回语言，例如英语等。
* **播放链接（play_url）**：返回的播放链接，支持播放音乐。

> 在卖家发布挂车内容前，开发者应用可以支持卖家在应用中通过输入关键词搜索音乐，搜索到的音乐支持播放，可以在后续挂车步骤中直接使用。**接口查询获取的音乐均为有电商权限的音乐，可直接使用，无违规风险。**

> * **音乐 ID (music_id)**：搜索到的音乐关联的唯一 ID，在后续挂车步骤中可直接使用。
> * **关键词 (keyword)**：用户输入的搜索词，用于匹配音乐名称或作者。
> * **语言 （language）**：支持定义返回语言，例如英语等。
> * **播放链接(play_url)**:返回的播放链接，支持播放音乐。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/53d2c47d70314806ae59cb6745faeb1e~tplv-k9wyc2ijk0-image.image)
| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Search Music](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Spk6d6AHuoE3Oix24Nslptczgkb) | RESTful API | 基于关键词推荐音乐信息。Search Music 在全球所有受支持的 TikTok Shop 市场可用。使用 `region` 和 `language` 查询参数来本地化结果。 |
### IF-161163.V1 可购物视频发布支持绑定音乐

1. 在开发者应用中，卖家发布可购物视频（Shoppable Video）时，可以为视频关联一段背景音乐（BGM），以增强视频的趣味性和传播效果。
   * 卖家需要在应用内通过 `music_id` 来指定所需的音乐。
   * **如果视频关联音乐，那么视频原声（包含口播）会被音乐覆盖**
> 1. 在开发者应用中，卖家发布可购物视频（Shoppable Video）时，可以为视频关联一段背景音乐（BGM），以增强视频的趣味性和传播效果。
>    * 卖家需要在应用内通过 `music_id` 来指定所需的音乐。
>    * **如果视频关联音乐，那么视频原声（包含口播）会被音乐覆盖**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/bf901f4209bd46f4a0d82b493ff3cb7a~tplv-k9wyc2ijk0-image.image)

| **API/通知名称** | **类型** | **描述** |
| --- | --- | --- |
| [Post Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-TV8qdaPDLo49yxxamEblRomKgMh) | RESTful API | 使用此 API 发布带有指定背景音乐的视频。 |
| [Search Music](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Spk6d6AHuoE3Oix24Nslptczgkb) | RESTful API <br/>  | 使用此 API 搜索已授权音乐并获取有效的 `music_id`。Search Music 在全球所有受支持的 TikTok Shop 市场可用；使用 `region` 和 `language` 查询参数来本地化结果。 |
# 附录
# **常见问题**
| 即使视频预审 API 在发布前未发现问题，发布后是否仍可能收到违规警告？ | 是的，有可能。预检查结果仅供参考，不保证发布后的最终结果。 |
| --- | --- |
| 如果视频通过了预审，是否保证良好的表现？ | 不，预检查结果仅供参考，不保证发布后的最终结果。视频表现受多种因素影响，包括 TikTok Shop 内容政策、账号状态、内容质量等。 |
| 卖家每天通过 API 可以进行多少次预审？ | 卖家每天至少有 2 次预审机会。可用预审次数可能因卖家表现而异。 |
| 如果 Get 达人 Profile API 响应中达人的账号类型同时是 Marketing Account 和 Affiliate 达人，该怎么办？ | 在达人的账号类型同时为 Marketing Account 和 Affiliate 达人的情况下，Get 达人 Profile API 将在 `type` 字段返回 `Marketing Account`。 |
| 如果账号 A 上传了视频并获得了 file_id，这个 file_id 能否用于通过账号 B 发布视频？ | 不能，账号 A 的 Upload Video API 返回的 file_id 不能被账号 B 用于发布视频。file_id 特定于上传视频的账号。每个账号都有自己唯一的视频上传会话，生成的 file_id 与该会话绑定。 |
| [TikTok Shop 官方账号有什么功能？](https://seller-us.tiktok.com/university/essay?knowledge_id=5643789953599275&identity=1&anchor_link=EBCE00CE) | 一旦 TikTok 账号被关联为 TikTok Shop 的官方账号，它将成为你店铺在 TikTok 上的主要代表。你店铺中的商品将自动同步到店铺页面。店铺页面也将作为商品展示和促销的中心页面。 <br/> <br/> * **积累店铺粉丝，提高复购率** <br/>    * 绑定店铺官方 TikTok 账号后，可以打通官方账号与店铺的粉丝用户群。用户关注你的店铺官方 TikTok 账号后，可以通过账号主页轻松找到你的店铺入口，帮助店铺引流并提高复购率。 <br/> * **提高店铺曝光，沉淀流量** <br/>    * 用户可以通过 TikTok 的搜索功能轻松搜索你店铺中的商品，并在直播间为整个销售链路新增店铺页面入口，帮助你的商品和店铺在 TikTok 上获得更多曝光。 |
| [TikTok Shop 官方账号有什么规则？](https://seller-us.tiktok.com/university/essay?knowledge_id=5643789953599275&identity=1&anchor_link=EBEB00CD) | * 每个店铺只能绑定一个官方账号。 <br/> * 升级后店铺名称与绑定的官方账号名称需保持一致，当修改店铺名称时，官方账号名称将同步更改。修改店铺名称时请谨慎操作。 <br/> * 官方账号在**绑定成功 24 小时后可以解绑。请注意官方账号只能解绑 3 次**； <br/> * 账号地区需与店铺地区相同。 <br/> * 同一账号不能同时绑定为同一店铺的官方账号和营销账号。 <br/> * 该账号只能销售自己店铺的商品，无法参与联盟计划。如果卖家想参与联盟，可以使用营销账号或达人账号申请权限。 |
| [如何绑定 TikTok Shop 官方账号？](https://seller-us.tiktok.com/university/essay?knowledge_id=5643789953599275&identity=1&anchor_link=EC0800CC) | 查看链接中的详细信息 |
# API
## [GET] 获取店铺商品
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 获取店铺商品 |
| API 版本 | 202509 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/shop_products |
| API 方法 | GET |
| API 功能描述 | 开发者可使用此 API 搜索和获取特定达人绑定的店铺商品信息，支持关键词搜索。 |
### 请求参数
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一密钥。请使用分配给你的应用的特定密钥。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。当你向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int64 | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| title_keyword | string | 否 | apple | 你希望搜索的商品标题关键词。 |
| sort_field | string | 否 | PRODUCT_ID | 排序字段包括 PRODUCT_ID、PRICE 和 SALE。如果 sort_field 为空或无效，将默认设置为 PRODUCT_ID。 |
| sort_order | string | 否 | DESC | 排序顺序包括 DESC 和 ASC。如果排序顺序为空或无效，将默认设置为 DESC。 |
| page_size | int32 <br/>  | 是 | 20 | 分页数量决定发送请求后你将获得多少商品。推荐值为 20。 <br/> 有效范围：[1-20] |
| page_token | string | 否 | b2Zmc2V0PTAK | 分页偏移量，决定从哪里开始搜索。如果是第一次请求，此字段为空。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | 是 | 29a39d | 来自 [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的达人 access_token 值，当 user_type = 1 时。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | 是 | application/json | 允许类型：application/json |
#### Body（GET/DELETE 不适用）
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
**请求体示例：**
```JSON
{}
```

### 响应参数
| 字段 |  |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- | --- |
| code |  |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  |  | object |  | 具体返回信息 |
| > | products |  |  | []object |  | 搜索到的商品列表。当没有搜索结果时将为空。 |
| > | > | id |  | string | 1729592969712207012 | TikTok 商品 ID。 |
| > | > | title |  | string | testcase autotest Live Product | 商品名称。 |
| > | > | price |  | object |  | 商品价格，以两位小数和货币显示。 |
| > | > | > | amount | string | 56.00 | 商品价格，两位小数。 |
| > | > | > | currency | string | USD | 商品价格货币，基于达人可以销售的地区。 |
| > | > | added_status |  | string | ADDABLE | 橱窗添加状态，可能的值： <br/> - ADDABLE <br/> - ADDED <br/> - REJECTED |
| > | > | brand_name |  | string | Apple | 卖家为商品设置的品牌名称。 |
| > | > | images |  | []object |  | 商品的图片。 |
| > | > | > | url | string | https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/982dd6b4e46a6a24203b00611a474cca~c5_1080x1080.webp | 商品图片的 URL。 |
| > | > | > | width | int32 | 200 | 商品图片的宽度。 |
| > | > | > | height | int32 | 200 | 商品图片的高度。 |
| > | > | sales_count |  | int32 | 33 | 已售出的商品数量。 |
| > | total_count |  |  | int32 | 300 | 符合查询条件的商品总数。 |
| > | next_page_token |  |  | string | b2Zmc2V0PTAK | 分页 token 是用于分页的游标。token 在上一次分页查询中返回，用于确定当前位置。当没有更多商品可搜索时将为空。 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "data": {
      "products": {
        "id": "1729592969712207012",
        "title": "testcase autotest Live Product",
        "price": {
          "amount": "56.00",
          "currency": "USD"
        },
        "added_status": "ADDABLE\n",
        "brand_name": "Apple",
        "images": {
          "url": "https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/982dd6b4e46a6a24203b00611a474cca~c5_1080x1080.webp",
          "width": 200,
          "height": 200
        },
        "sales_count": 33
      },
      "total_count": 300,
      "next_page_token": "b2Zmc2V0PTAK"
  },
  "message": "success",
  "request_id": "202410011116276C0AA9039F31B70430A0"
}
```

### 代码示例
### Curl
```Bash
curl -X GET \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202509/shop_products?timestamp=1623812664&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&sort_order=DESC&page_size=20&app_key=29a39d&title_keyword=apple&sort_field=PRODUCT_ID&page_token=b2Zmc2V0PTAK' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |

## **[POST] 上传可购物视频**
 如果视频文件超过 10 MB，请参考[可购物视频大文件上传方案](https://bytedance.sg.larkoffice.com/docx/WTMvdfbTBo30Fex0r9YlYstGg0d)
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 上传可购物视频文件 |
| API 版本 | 202505 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/videos/video_files |
| API 方法 | POST |
| API 功能描述 | 使用此 API 在发布到 TikTok 之前上传视频文件 |
### 请求参数
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 来自[获取 Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的 creator_access_token 值，user_type = 1。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | true | multipart/form-data | 允许类型：multipart/form-data |
#### Body
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| data | binary | true |  | 要上传的本地文件。 <br/> 注意： <br/> - 支持格式：MP4、MOV、MKV、WMV、WEBM、AVI、3GP、FLV、MPEG <br/> - 最大视频大小：100 MB <br/> - 视频宽高比：9:16 至 16:9 <br/> 商品视频建议： <br/> - 分辨率：720p 或更高 <br/> - 时长：> 30 秒 |
**请求体示例：**
```JSON
{
  "data": ""
}
```

### 响应参数
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  | object |  | 具体返回信息 |
| > | video_file |  | object |  | 视频文件信息。 |
| > | > | id | string | 123123123123 | 上传视频文件的 ID。 |
| > | > | md5 | string | D41D8CD98F00B204E9800998ECF8427E | 上传文件的 MD5 校验和 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "data": {
      "video_file": {
        "id": "123123123123",
        "md5": "D41D8CD98F00B204E9800998ECF8427E"
      }
  },
  "message": "success",
  "request_id": "202410011116276C0AA9039F31B70430A0"
}
```

### 代码示例
### Curl
```Bash
curl -X POST \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202505/videos/video_files?timestamp=1623812664&app_key=29a39d&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: multipart/form-data' \
-F 'data=@"file"'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |

## [POST] 上传可购物图片文件
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 上传可购物图片文件 |
| API 版本 | 202511 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/photos/photo_files |
| API 方法 | POST |
| API 功能描述 | 使用此 API 在视频发布之前上传图片。返回每个上传图片的 photo_file_uri |
### 请求参数
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 来自[获取 Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的 creator_access_token 值，user_type = 1。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | true | multipart/form-data | 允许类型：multipart/form-data |
#### Body
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| data | binary | true |  | 要上传的本地图片文件。 <br/> <br/> 注意： <br/> - 支持格式：JPG、JPEG、PNG、WEBP、HEIC、BMP <br/> - 最大大小：10MB <br/> <br/> - 宽高比：9:16 至 16:9 |
**请求体示例：**
```JSON
{
  "data": ""
}
```

### 响应参数
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  | object |  | 具体返回信息 |
| > | photo_file |  | object |  | 图片信息 |
| > | > | photo_uri | string | skldjfskdlfjlskdfs000023423s | 在[发布可购物视频]中，使用此图片 URI 填充 cover_uri 字段 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "photo_file": {
      "photo_uri": "skldjfskdlfjlskdfs000023423s"
    }
  }
}
```

### 代码示例
### Curl
```Bash
curl -X POST \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202511/photos/photo_files?sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664&app_key=29a39d' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: multipart/form-data' \
-F 'data=@"file"'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次重试后问题仍然存在，请联系平台支持。 |

## **[POST] 发布可购物视频**
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 发布可购物视频 |
| API 版本 | 202607 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/videos |
| API 方法 | POST |
| API 功能描述 | 使用此 API 发布可购物视频。 |
### 请求参数
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key <br/>  | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 来自[获取 Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的 creator_access_token 值，user_type = 1。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | true | application/json | 允许类型：application/json |
#### Body
| 字段 |  | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| video_info |  | object | true |  | 视频信息 |
| > | file_id | string | true | v12d00gd0024d3nfqr7og65 | 来自[上传可购物视频文件]的 video file_id |
| > | title | string | true | Sample video title | 视频标题。 <br/> 最大长度为 4000 个 UTF-16 字符。 <br/> 如果未指定，发布的帖子将不包含任何标题。 |
| > | cover_uri | string | false | v12d00gd0024d3nfqr7og65oooiuuyy | 视频封面图片 URI，通过上传可购物图片文件 API 上传图片后返回。 |
| > | cover_timestamp_ms | int32 | false | 1000 | 输入参数为时间戳，指定视频中的某一特定时刻。该时刻的帧将被用作视频封面。如果 cover_uri 和 cover_timestamp_ms 均未提供，封面将默认为上传视频的第一帧。cover_uri 和 cover_timestamp_ms 只能提供其中一个。如果两个参数都传入，cover_uri 将优先生效。 |
| > | music_id <br/>  | string | false | 717294069642063456 | 视频背景音乐的 music ID。如果未提供，视频将不关联音乐。music ID 必须通过搜索音乐库获取。 |
| > | is_ai_generated | bool | false | true | 表示提交的视频内容是否为 AI 生成。设置为 `true` 将在发布的帖子上显示 AI 生成标签。省略时默认为 `false`。 |
| product_link_info |  | object | true |  | 商品链接信息 |
| > | product_id | string | true | 17294069642063424 | 使用 product_id 将商品与视频绑定。 <br/> product_id 来自[获取店铺商品]或[获取橱窗商品] |
| > | title | string | true | 样品商品锚点标题 | 显示在商品锚点上的标题。锚点标题应少于 30 个字符。 |
**请求体示例：**
```JSON
{
  "video_info": {
    "file_id": "v12d00gd0024d3nfqr7og65",
    "title": "Sample video title",
    "cover_uri": "v12d00gd0024d3nfqr7og65oooiuuyy",
    "cover_timestamp_ms": 1000,
    "music_id": "717294069642063456",
    "is_ai_generated": true
  },
  "product_link_info": {
    "product_id": "17294069642063424",
    "title": "Sample product anchor title"
  }
}
```

### 响应参数
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  | object |  | 具体返回信息 |
| > | video |  | object |  | 已发布的视频信息 |
| > | > | id | string | 7548431509997292816 | 视频 ID，使用此 ID 查询视频发布状态。 |
| > | > | quota | string | 3/day | 达人的内容发布配额。发布成功时返回；发布失败时包含在错误消息中；如果没有配额限制则省略。 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "video": {
      "id": "7548431509997292816",
      "quota": "3/day"
    }
  }
}
```

### 代码示例
### Curl
```Bash
curl -X POST \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202607/videos?app_key=29a39d&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664' \
-H 'content-type: application/json' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-d '{
  "product_link_info": {
    "product_id": "17294069642063424",
    "title": "Sample product anchor title"
  },
  "video_info": {
    "cover_timestamp_ms": 1000,
    "cover_uri": "v12d00gd0024d3nfqr7og65oooiuuyy",
    "file_id": "v12d00gd0024d3nfqr7og65",
    "music_id": "717294069642063456",
    "title": "Sample video title",
    "is_ai_generated": true
  }
}'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |
| 16011007 | 商品链接标题不应超过 30 个字符。 |
| 16011009 | 商品链接标题包含不当用语。 |
| 16011069 | 商品链接标题包含标点符号或表情符号。 |
| 36009003 | 内部错误。请重试。如果多次重试后问题仍然存在，请联系平台支持。 |
| 38007001 | 系统错误 |
| 170001002 | 达人 TikTok Shop 权限检查失败。 |
| 170001003 | 达人 TikTok Shop 权限暂时被封禁。 |
| 170001004 | 达人 TikTok Shop 权限被永久封禁。 |
| 170001005 | 达人未签署服务条款。请联系 TikTok 了解更多详情。 |
| 170001006 | 未签署 GKA 条款。请在签署 GKA 条款后重试。 |
| 170001007 | 达人未签署欧盟数据共享协议。 |
| 170001008 | 达人年龄验证失败。请先完成年龄验证。 |
| 170001009 | 该商品属于不支持的类目。 |
| 170001010 | 佣金计划获取失败或被拒绝。 |
| 170001011 | 该商品不存在。 |
| 170001012 | 该商品不可用。 |
| 170001013 | 橱窗 SPU 超出限制。 |
| 170001014 | 被垃圾信息检查拦截。 |
| 170001015 | 被 TikTok Shop 风控拦截。 |
| 170001018 | 获取达人支付账户错误。请先验证支付账户。 |
| 170001020 | 您已超过发布电商短视频的频率。请休息片刻。 |
| 170001024 | cover_timestamp_ms 必须是非负整数且在视频时长范围内。 |
| 170001025 | cover_timestamp_ms 超出视频时长。 |
| 170001030 | 达人账号被封禁。请联系 TikTok 处理您的账号。 |
| 170001031 | 达人被禁止发布内容。 |
| 170001040 | 请使用有效的视频文件 ID 发布 TikTok Shop 短视频。 |
| 170001050 | 视频发布流程中出现错误。请重试或联系 TikTok。 |

## **[GET] 获取可购物视频状态**
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 获取可购物视频状态 |
| API 版本 | 202509 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/videos/:video_id/status |
| API 方法 | GET |
| API 功能描述 | 使用此 API 获取可购物视频发布结果。 |
### 请求参数
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| video_id | string | true | 7548431509997292816 | 来自[发布可购物视频]的视频 ID |
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 来自[获取 Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的 creator_access_token 值，user_type = 1。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | true | application/json | 允许类型：application/json |
#### Body（GET/DELETE 请求不适用）
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
**请求体示例：**
```JSON
{}
```

### 响应参数
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  | object |  | 具体返回信息 |
| > | video |  | object |  | 返回的视频信息 |
| > | > | id | string | 7493990579714164574 | 视频 ID |
| > | > | post_status | string | FAIL | 视频发布状态，可能的值： <br/> - SUCCESS <br/> - FAIL <br/> - PROCESSING |
| > | > | post_time | int64 | 1685548800 | 视频成功发布时返回，即 `posting_status = SUCCESS`。 <br/> 以秒为单位。 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "video": {
      "id": "7493990579714164574",
      "post_status": "FAIL",
      "post_time": 1685548800
    }
  }
}
```

### 代码示例
### Curl
```Bash
curl -X GET \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202509/videos/7548431509997292816/status?sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664&app_key=29a39d' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |
| 38007001 | 系统错误 |
| 170001016 | 该视频不属于此达人。请检查有效的视频状态。 |

## **[POST] 预审可购物视频**
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 预审视频内容 |
| API 版本 | 202511 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/videos/precheck_task |
| API 方法 | POST |
| API 功能描述 | 使用此 API 预审视频和可购物内容锚点是否存在违规 |
### 请求参数
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 来自[获取 Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的 creator_access_token 值，user_type = 1。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | true | application/json | 允许类型：application/json |
#### Body
| 字段 |  | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| video_info |  | object | true |  | 视频信息 |
| > | file_id | string | true | v12d00gd0024d3nfqr7og65 | 来自[上传可购物视频文件](https://api/affiliate_creator/202505/videos/video_files)的 video file_id |
| product_link_info |  | object | true |  | 商品链接信息 |
| > | product_id | string | true | 17294069642063424 | 使用 product_id 将商品与视频绑定。 <br/> product_id 来自[获取店铺商品](https://api/affiliate_creator/202509/shop_products)或[获取橱窗商品](https://api/affiliate_creator/202405/showcases/products) |
| > | title | string | true | 样品商品锚点标题 | 显示在商品锚点上的标题。锚点标题应少于 30 个字符。 |
**请求体示例：**
```JSON
{
  "video_info": {
    "file_id": "v12d00gd0024d3nfqr7og65"
  },
  "product_link_info": {
    "product_id": "17294069642063424",
    "title": "Sample product anchor title"
  }
}
```

### 响应参数
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  | object |  | 具体返回信息 |
| > | precheck |  | object |  | 视频内容预审任务结果 |
| > | > | task_id | string | 1123123123 | 预审任务 ID |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "precheck": {
      "task_id": "1123123123"
    }
  }
}
```

### 代码示例
### Curl
```Bash
curl -X POST \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202511/videos/precheck_task?app_key=29a39d&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json' \
-d '{
  "product_link_info": {
    "product_id": "17294069642063424",
    "title": "Sample product anchor title"
  },
  "video_info": {
    "file_id": "v12d00gd0024d3nfqr7og65"
  }
}'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |
| 16011007 | 商品链接标题不应超过 30 个字符。 |
| 16011009 | 商品链接标题包含不当用语。 |
| 16011069 | 商品链接标题包含标点符号或表情符号。 |
| 36009003 | 内部错误。请重试。如果多次重试后问题仍然存在，请联系平台支持。 |
| 170001002 | 达人 TikTok Shop 权限检查失败。 |
| 170001005 | 达人未签署服务条款。请联系 TikTok 了解更多详情。 |
| 170001006 | 未签署 GKA 条款。请在签署 GKA 条款后重试。 |
| 170001007 | 达人未签署欧盟数据共享协议。 |
| 170001008 | 达人年龄验证失败。请先完成年龄验证。 |
| 170001009 | 该商品属于不支持的类目。 |
| 170001010 | 佣金计划获取失败或被拒绝。 |
| 170001011 | 该商品不存在。 |
| 170001012 | 该商品不可用。 |
| 170001013 | 橱窗 SPU 超出限制。 |
| 170001014 | 被垃圾信息检查拦截。 |
| 170001015 | 被 TikTok Shop 风控拦截。 |
| 170001018 | 获取达人支付账户错误。请先验证支付账户。 |
| 170001019 | 用户已超过分配的每日预审资源配额 |

## **[GET] 获取可购物视频预审结果**
### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 获取可购物视频预审结果 |
| API 版本 | 202511 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/videos/precheck_tasks/:task_id |
| API 方法 | GET |
| API 功能描述 | 使用此 API 获取视频预审结果 |
### 请求参数
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| task_id | string | true | 7493990579714164574 | 来自[预审视频内容](https://api/affiliate_creator/202511/videos/precheck_task)的任务 ID |
#### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
#### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 来自[获取 Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API) 的 creator_access_token 值，user_type = 1。按照此[指南](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c)获取达人 access_token。 |
| content-type | string | true | application/json | 允许类型：application/json |
#### Body（GET/DELETE 请求不适用）
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
**请求体示例：**
```JSON
{}
```

### 响应参数
| 字段 |  |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- | --- |
| code |  |  |  | int32 | 0 | API 响应中返回的成功或失败状态码。 |
| message |  |  |  | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id |  |  |  | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data |  |  |  | object |  | 具体返回信息 |
| > | precheck_task |  |  | object |  | 视频预审任务 |
| > | > | id |  | string | 7493990579714164574 | 视频预审任务的 ID。 |
| > | > | result |  | string | FAIL | SUCCESS：预审任务通过检查 <br/> FAIL：预审任务因违规而失败。请查看 'issues' 字段了解详情。 <br/> PROCESSING：预审任务仍在进行中 |
| > | > | issues |  | []object |  | 任务失败时返回的策略违规详情列表 |
| > | > | > | risk | string | Pirated Content | 策略违规类型 |
| > | > | > | suggestions | string | 您的视频可能包含非原创内容。创作原创内容是脱颖而出的关键。 | 解决检测到的违规问题的详细指导。 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "precheck_task": {
      "id": "7493990579714164574",
      "result": "FAIL",
      "issues": [
        "risk": "Pirated Content",
        "suggestions": "Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."
      ]
    }
  }
}
```

### 代码示例
### Curl
```Bash
curl -X GET \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202511/videos/precheck_tasks/7493990579714164574?app_key=29a39d&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```

### 错误码
| 错误码 | 错误消息 |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次重试后问题仍然存在，请联系平台支持。 |

## [GET] 搜索音乐
#### 概述
| 类型 | 值 |
| --- | --- |
| API 名称 | 搜索音乐 |
| API 版本 | 202602 |
| API URI（所有 API 固定） | 主机: open-api.tiktokglobalshop.com <br/> 协议: HTTPS |
| API 路径 | /affiliate_creator/:version/music/search |
| API 方法 | GET |
| API 功能描述 | 使用此 API 获取音乐信息。搜索音乐在全球支持的 TikTok Shop 市场中可用；使用 `region` 和 `language` 查询参数来定位结果。 |
#### 请求参数
##### Path
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
##### Query
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int64 | true | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可将其转换为本地时间。 |
| keyword | string | true | love | 搜索关键词 |
| search_id | string | false | 2026021821534288157A7F308E8C81359B | 第一页时，search_id 留空，响应将返回一个 search_id。从第 2 页开始（即 page_token > 0 时），在每个请求中包含相同的 search_id 以继续翻页；否则分页可能失败。 |
| page_token | string | false | 40 | 第一页：留空。 <br/> 下一页：将上一次响应中的 next_page_token 复制到这里 |
| page_size | string | false | 20 | 每页大小 |
| region | string | false | US | 区域代码（ISO 3166-1 alpha-2） |
| language | string | false | en-US | 语言标签（BCP-47） |
##### Headers
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | 卖家 access_token |
| content-type | string | true | application/json | 允许类型：application/json |
##### Body（GET/DELETE 请求不适用）
| 字段 | 类型 | 必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
**请求体示例**
```JSON
{}
```

#### 响应参数
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| music |  |  | []object |  | 音乐列表 |
| > | id |  | string | 717294069642063456 | 音乐 ID |
| > | title |  | string | Love Story | 音乐标题 |
| > | author |  | string | Taylor Swift | 艺人名称 |
| > | cover_thumb |  | object |  | 封面图片 |
| > | > | url_list | []string | ["https://example.com/music/cover/love_story_1.jpg"] | 封面图片 URL 列表 |
| > | duration |  | string | 235 | 时长（秒） |
| > | play_url |  | object |  | 播放 URL |
| > | > | url_list | []string | ["https://example.com/music/play/love_story.mp3"] | URL 列表 |
| next_page_token |  |  | string | 40 | 用作下一次请求的 page_token，仅在 has_more=true 时有意义。 |
| has_more |  |  | bool | false | 是否有下一页。 |
| search_id |  |  | string | 2026021821534288157A7F308E8C81359B | 同一搜索的所有后续页面使用相同的 search_id。 |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "music": {
    "id": "717294069642063456",
    "title": "Love Story",
    "author": "Taylor Swift",
    "cover_thumb": {
      "url_list": [
        "https://example.com/music/cover/love_story_1.jpg"
      ]
    },
    "duration": "235",
    "play_url": {
      "url_list": [
        "https://example.com/music/play/love_story.mp3"
      ]
    }
  },
  "next_page_token": "40",
  "has_more": false,
  "search_id": "2026021821534288157A7F308E8C81359B"
}
```

#### 错误码
| **错误码** | **错误消息** |
| --- | --- |
|  |  |
| 36009003 | 内部错误。请重试。如果多次重试后问题仍然存在，请联系平台支持。 |
## 可购物视频预审结果（webhook）
#### Webhook 负载
| 字段 |  |  | 类型 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| type |  |  | int | 55 | webhook 类型的 ID。 |
| tts_notification_id |  |  | string | 7327112393057371910 | 通知的 ID。 |
| creator_open_id <br/>  |  |  | string | VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw | 达人的 open_id。获取该值请参阅[授权概述](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75)。 <br/>  |
| timestamp |  |  | int | 1644412885 | 此 webhook 触发时的 UNIX 时间戳。 |
| data |  |  | object |  |  |
| > | precheck_task_id <br/>  |  | string <br/>  | 7493990579714164574 |  <br/>  |
| > | result <br/>  |  | string | "FAIL" <br/>  | PASS <br/> FAIL |
| > | issues <br/>  |  | []object <br/>  |  | 仅当 "result" 为 "FAIL" 时返回 |
| > | > | risk | string | "Pirated Content" | 风险类型。 |
| > | > | suggestion <br/>  | string <br/>  | "您的视频可能包含非原创内容。创作原创内容是脱颖而出的关键。" | 如何解决此风险。 <br/>  |
注意：以 ">" 开头的参数表示该参数是子对象。
```JSON
{
  "type": 55,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id": "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "precheck_task_id": "7493990579714164574",
    "result": "FAIL",
    "issues": [
      {
        "risk": "Pirated Content",
        "suggestion": "Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."
      }
    ]
  }
}
```
