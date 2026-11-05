# Shoppable video Integration Solutions

**Important Notice**
The API structure will remain unchanged, but certain field names may be modified. 
Please keep an eye 👁👁 on the documentation for updates.
Developers are encouraged to regularly check the **Changelog** for the latest updates and changes.

🌟 **Test Shoppable Video**: [【External】Test Affiliate Integration with your own TikTok Account](https://bytedance.sg.larkoffice.com/docx/OB5Zdr0y2oyiikxNZnVlhZNcgCb)


# Introduction
This solution targets **third-party apps and seller developer sellers**, covering the end-to-end flow—from creator authorization → fetching eligible products → asset creation and upload → video precheck and publishing (with product anchors) →video data perfomance.
> 本方案面向 **3P App / 自研商家**，提供从达人授权 → 获取可带货商品 → 素材制作与上传 → 视频预审与发布（绑定商品锚点）→ 数据回收的集成解决方案。


# Business Goal

* Enable developers to build on reliable **Shoppable Content Posting APIs** to continuously produce shoppable videos for sellers/creators, increasing publishing volume and conversions.
* Support bulk publishing and detailed failure feedback, paving the way for subsequent ad campaigns and creative optimization.
> * 让开发者基于稳定的 **Shoppable Content Posting APIs**，为商家/达人持续产出可挂车视频，提升发布量与转化。
> * 支持**批量发布**与**发布**失败原因回传，并为后续广告投放和素材优化提供帮助。

# Glossary
| Term | Definition  |
| --- | --- |
| Application Requirement Document (ARD) | This document gives you an overview of the various use cases that a seller needs, in order to manage their shop on TikTok via an ecommerce platform connector.  |
| Integration Flow | An integration flow is a development guide related to the specific use case. |
| TTS | Acronym for TikTok Shop.  |
| Buyer | Buyer purchases product(s) on TikTok Shop.  |
| Seller | A TikTok Shop seller  |
| Creator | All users, including sellers, who create content. |
| content | **All** available forms of media that can be uploaded by creators to TikTok Shop, including your Product Showcase, videos, and live streams. This also includes all metadata, captions, and profile information. |
| Shoppable short video <br/>  | **Shoppable short video** is created in the same format that you would create any short video on TikTok. The difference between your typical TikTok video and a shoppable short video is that a shoppable short video includes an embedded anchor link that directs your audience to the product that you want to promote. We've found that a well-executed video can make a big difference when it comes to connecting with potential customers and selling. **Short videos** are key in capturing audience attention, inspiring them to take action, and driving them to purchase. |
| Marketing account  <br/>  | Marketing account (up to 4): Additional accounts to expand seller reach and marketing capabilities. Marketing accounts can sell both linked sellers' and affiliates' products. |
| Official account | Official account (Required, 1 per shop): seller's primary brand presence on TikTok Shop with a dedicated shop page. An official account can only sell products from the linked seller account. |
| TikTok Shop Short Video Official Guidelines | https://seller-us.tiktok.com/university/essay?knowledge_id=7096334743553838&from=new-and-updated&role=1&identity=1 |
| TikTok Community Guideline | https://www.tiktok.com/community-guidelines/en/overview |
| Seller Center | A seller portal for TTS sellers to manage their shop, products, orders, returns/refunds, and more.  |
| Module  | A module is a subcomponent of the ecommerce selling lifecycle.  |
| Feature | A feature is a subcomponent of module. Features are a set of functionalities in a product that will allow the seller to complete a set of tasks or actions. How you design the feature will determine the overall experience of the end user. |
| Use Case | A use case is a specific situation in which an app could potentially be used by a seller or buyer.  |
| UI Suggestions  | Specific UI suggestions for developers to consider during development phase to ensure an easy-to-use experience on the app.  |
| App Developer | Partners/developers who are building the app.  |
| App Reviewer | Once the app development is complete, a team member will review and test the app based on the ARD you filled out.  |
| Beta Testers | Once internal review is done, we will invite sellers to beta test your app. The sellers are beta testers.  |

#  Integration flow Overview

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e6c0245787624e76a8f208fcd23acbf1~tplv-k9wyc2ijk0-image.image)
# API / Webhook Overview 
| **API/Notification name** | **Type** | **Description** |
| --- | --- | --- |
| [Get Access Token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) <br/>  | RESTful API | Use this API to request an `access_token` and `refresh_token` |
| [Get Creator Profile](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) | RESTful API | Use this API to get the creator's profile information. |
| [Get Shop Products](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Fu3idMqnqoqwTixg2lklALotgSG) <br/>  | RESTful API | Developers can utilize this API to search and retrieve product information of shops which is bound by a specific creator with specific keywords. |
| [Get Showcase Products](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405#Back%20To%20Top) <br/>  | RESTful API | This API lists the products in the creator's showcase, paginated by specified page size and iterated through pages by page token for up to **2000 products** in the showcase. This API is generally used when a creator would like to view the products in the showcase. The platform will return the product details in the showcase, as well as the products in the livebag if the creator is live streaming. |
| [Upload Shoppable Video File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-EEPudRjSEorRmIxMSX6lFIL8gih) | RESTful API <br/>  | Use this API to upload the video before posting to TikTok <br/>  |
| [Post Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-U6Sud9fdBodmjwxLRKml4GAfgib) | RESTful API | Use this API to publish the video. The request supports `video_info.is_ai_generated` to indicate AI-generated content; the field defaults to `false` when omitted. The response may include `data.video.quota` when a content posting quota restriction applies. |
| [Get Shoppable Video Status](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-J9uCdO4Ulo3RAjxscIUlKib1gGf) | RESTful API | Use this API to get video publish result |
| [Pre-check Shoppable Video ](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-GEyCdCNhGoAZ5TxbVetli7SbgLc) | RESTful API <br/>  | Use this API to pre-check if there's any violation in the video and the shoppable content anchor |
| [Get Shoppable Video Pre-check Result ](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-WYbCdyN1ToT52TxtU3ClrUuHgkc) | RESTful API | Use this API to get video pre-check result |
| [Shoppable Video Precheck Result](https://partner.tiktokshop.com/docv2/page/arpnre1g) <br/>  | Webhook | The Video Precheck Result webhook is triggered when the Precheck Video Content API is called, and provides the results of the video’s quality assessment and violation checks. |
| [Get Shop Video Performance List](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-list-202409) <br/>  | RESTful API <br/>  | Returns overall performance metrics for all videos under a shop. This API currently provides data only for shops registered in the United States, United Kingdom, Singapore, Vietnam, and Thailand. |
| [Get Shop Video Performance Detail](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-details-202409) | RESTful API | Returns detailed performance metrics for a (requested) video. This API currently provides data only for shops registered in the United States, United Kingdom, Singapore, Vietnam, and Thailand. |
| [Get Creator Video Performance Detail ](https://bytedance.sg.larkoffice.com/docx/VkfxdgvBCoL4gMxpZJslZ8xmgcg) | RESTful API | This is a US-creator-only API for now. And it is for getting Tiktok E-commerce video metrics(including anchor_display_rate, ctr, orders, items_sold, gmv) to analysis. |
# Proposed Integration Flows 
| **Module** | **Feature** | **Use Case** | Integration Flow |
| --- | --- | --- | --- |
| Shoppable Video <br/>  | Creator Auth and deauth <br/> > 达人授权与取消授权 | [UC-161111](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-CikMddDSIozcWSxwJ0Kl8LX7gxe)：Support creators to complete authorization or deauth for the developer's app. <br/> > 支持达人可以完成达人授权或者解除授权。 | IF-161111.V1 |
|  | Get creator type and product info <br/> > 获取达人类型与可带货商品 <br/>  <br/>  | [UC-161121](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Xjf7dGbxeo6WVQxX3rSlolSqgmd)： Retrieve creator type. <br/> > 获取达人类型。 | IF-161121.V1 |
|  |  | [UC-161122：](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Xjf7dGbxeo6WVQxX3rSlolSqgmd)Retrieve products that can be promoted by the corresponding creator type (including main image, title, SKU). <br/> > 获取对应达人类型可带货的商品（含主图、标题、SKU） | IF-161122.V1 |
|  | Upload Video  <br/> > 上传视频 <br/>  <br/>  | [UC-161131](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-E9SldzIRGotErGx6W4Vl6Vaqgtc)：Seller uses product images/information to generate short videos. <br/> > 商家使用商品图片/信息生成短视频 | IF-161131.V1 |
|  |  | [UC-161132](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-HfpGdkpvYoySwOxjdTElavyFgzc)：Upload video to TikTok Shop. <br/> > 上传视频至 TikTok Shop | IF-161132.V1 |
|  | Precheck and Publish Shoppable Videos with anchors <br/> > 预审并发布Shoppable Video <br/>  <br/>  | [UC-161141](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-TrtBdldZgo9zoCxrdt4lrx6lgCX)：Seller submits video for precheck . <br/> > 商家提交视频进行预审. | IF-161141.V1 |
|  |  | [UC-161142](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-JqH1dpyXVogxiKxQREllX0p1gPh)：Publish shoppable video and bind product anchor. <br/> > 发布挂车视频，绑定商品锚点 | IF-161142.V1 |
|  |  | [UC-161143](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Rt3CdlJzXoIzzZxJvAZl7Ym4g2b)：Retrieve final result of shoppable video publishing. If it fails, obtain failure reason and provide suggestions for modification/retry. <br/> > 获取挂车视频发布最终结果，若失败，获取失败原因并提示修改/重试。 | IF-161143.V1 |
|  |  |  [UC-161144](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Nj6GdD2FIowNqXxyYP2ltjaBgff): Retrieve result of precheck. If the precheck fails, ISVs must block the posting action in their system to prevent the seller from uploading non-compliant content. <br/> > 获取precheck结果。如果预审失败，服务商必须禁止商家发对应的挂车视频。 |  IF-161144.V1  |
|  |  | [UC-161145](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#V7rMdNcugo8irwxnaFTlBb3JgJh): Retrieve result of good quality check. This allows sellers to know in advance whether their video is considered high-quality and provides actionable suggestions for improvement if it is not. Even if suggestions are returned, the video can still be published; this check should not block the posting process. <br/>  | IF-161145.V1 <br/>  |
|  | Shop Video performance data <br/> > 视频数据分析 <br/>  <br/>  | [UC-161151](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Y4grdqZ36oHiHdxkFtulzMgRgph)：Retrieve video performance data under the shop <br/> > 获取店铺下的视频表现数据 | IF-161151.V1 |
|  | Associate music with the Shoppable Videos and set a cover <br/> > 视频关联音乐和设置封面 | [UC-161161](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-KrJJdRN0XoHR5AxYiBIlpQHkgub): The Shoppable Video publishing supports video cover images. | IF-161161.V1 <br/>  |
|  |  | [US-161162](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-C505denogolCDCxOG2dlq6A1gnf): Search music ****  | IF-161161.V1 |
|  |  | [UC-161163](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Bi0adv0ZPoWE3cxgJPPl2CNVgXg): The Shoppable Video publishing supports to bind music. | IF-161162.V1 |

## Creator Auth and deauth
### **IF-161111.V1 Support creators to complete authorization or** **deauth for the developer's app.**

1. In the developer application, the seller can login to the creator account and complete the creator authorization either the web or mobile app.
2. Additionally, in compliance with regulations, the developer application must support the creator’s ability to revoke authorization at any time. Developers must provide an easy-to-use “revoke authorization” feature in the system, ensuring that the creator can manage their authorization status independently.
3. For more detailed instructions on how to support creator authorization, please refer to: [https://partner.tiktokshop.com/docv2/page/creator-authorization-guide](https://partner.tiktokshop.com/docv2/page/creator-authorization-guide)
> 1. 开发者应用中，商家登录自己的达人账号完成授权，可通过网页端或移动端完成账号登录与授权确认。
> 2. 同时，根据合规要求，开发者应用必须支持达人在任何时间撤销授权。开发者需在系统中提供便捷的“取消授权”功能入口，确保达人可自主管理其授权状态。
> 3. 更多如何支持达人授权的详细说明，请参考：https://partner.tiktokshop.com/docv2/page/creator-authorization-guide

UI suggestions：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5e8fde9a94ba43b5b8be4439279d38eb~tplv-k9wyc2ijk0-image.image)


| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Get Access Token](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) | RESTful API | Use this API to request an `access_token` and `refresh_token` |
## Get creator type and product info
### **IF-161121.V1 Retrieve Creator Type**

1. The seller can select the creator to be authorized within the developer’s application and display the corresponding creator type. The range of products a creator can promote varies based on their type.
2. The seller can use the `user_type` field in the **Get Creator Profile** response to filter creators by type:
   * `TIKTOK_SHOP_OFFICIAL_ACCOUNT` represents the seller's official account
   * `TIKTOK_MARKETING_ACCOUNT` represents the seller's marketing account
   * `TIKTOK_SHOP_CREATOR` represents the affiliate creator
> 1. 商家可在开发者的应用内选择需要授权的达人并展示达人对应的类型，不同类型的达人可以带货的商品范围是不同的。
> 2. 可以通过Get Creator Profile 中 user_type的出参来支持商家筛选达人类型
>    * TIKTOK_SHOP_OFFICIAL_ACCOUNT代表商家官方号
>    * TIKTOK_MARKETING_ACCOUNT代表商家渠道号
>    * TIKTOK_SHOP_CREATOR代表联盟达人


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/23f5f2fedf3a4338ac8f149765afc190~tplv-k9wyc2ijk0-image.image)
API/Notification Overview
| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Get Creator Profile](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) | RESTful API | Use this API to get the creator's profile information. |
### **IF-161122.V1 Retrieve products that can be promoted by the corresponding creator type (including main image, title, SKU)**

1. Support the seller in selecting products that can be promoted by the corresponding creator type:
   * If the creator is a `TIKTOK_MARKETING_ACCOUNT`/, `TIKTOK_SHOP_OFFICIAL_ACCOUNT`the seller needs to call the **Get Shop Products** API to retrieve the product information that the creator can promote.
   * If the creator is a `TIKTOK_SHOP_CREATOR`, the seller needs to call the **Get Showcase Products** API to retrieve the product information from the creator's showcase.
2. The application can display the basic product information, such as product name, main image, etc., based on the product information returned by the API. This enhances the efficiency and experience for the seller when selecting products.
> 1. 支持商家选择达人对应类型可带货的商品
>    * 如果是`TIKTOK_MARKETING_ACCOUNT`/, `TIKTOK_SHOP_OFFICIAL_ACCOUNTT`，则需要通过调用Get Shop Products接口获取该达人可以带货的商品信息。
>    * 如果是TIKTOK_SHOP_CREATOR，则需要调用Get Showcase Products接口获取该达人showcase橱窗内的商品信息，如果added_status不是ADDED则代表商品未加入到橱窗，可以通过调用Add Showcase Products接口将商品添加到橱窗。
> 2. 可在应用中通过接口返回的商品信息对应展示商品的基础信息例如商品名称、主图等，提升商家选择商品的效率和体验


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/71b39d864a314d9abed26f8b8f2c5d26~tplv-k9wyc2ijk0-image.image)
Note

1. In **Get Showcase Products**, please ensure the product status meets the following conditions:
* `inventory_status`: `IN_STOCK`
* `review_status`: `"APPROVED"`
* `is_hidden`: `false`
* `added_status`: `ADDED`
> 1. 在Get Showcase Products中，请关注商品的状态满足以下条件：
>    *  inventory_status: IN_STOCK,
>    *  review_status: "APPROVED",
>    *  is_hidden: false,
>    *  added_status: ADDED
> 2. 在Get Shop Products，请关注商品的状态，请关注商品的状态满足以下条件：
>    * added_status：ADDED

| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Get Shop Products](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Fu3idMqnqoqwTixg2lklALotgSG) | RESTful API | Developers can utilize this API to search and retrieve product information of shops which is bound by a specific creator with specific keywords. |
| [Get Showcase Products](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405#Back%20To%20Top) | RESTful API <br/>  | This API lists the products in the creator's showcase, paginated by specified page size and iterated through pages by page token for up to 2000 products in the showcase. This API is generally used when a creator would like to view the products in the showcase. The platform will return the product details in the showcase, as well as the products in the livebag if the creator is live streaming. |

## Upload Video 
### **IF-161131.V1 Seller uses product images/information to generate short videos**

1. The seller can use the developer's application to automatically or semi-automatically generate short video content based on the product’s main image, title, SKU, and other information.
2. During the video generation process, it is necessary to comply with TikTok Community Guidelines and the TikTok Shop Short Video Official Guidelines. Please ensure that the content is compliant and meets the platform's quality video standards. The generated video will later be uploaded and published through the Post Shoppable Video API.
> 1. 商家可通过开发者的应用基于商品的主图、标题、SKU 等信息自动化或半自动化生成短视频内容
> 2. 在视频生成过程中需遵守 TikTok社区规范 和 TikTokShop 短视频官方指南，请确保素材内容合规并且符合平台优质视频规范。生成的视频将在后续通过 Shoppable Video API 上传并发布。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b5c1fd06ad234d94839509f6d57a2323~tplv-k9wyc2ijk0-image.image)
Notes

1. Video specifications
   * Supported formats: MP4, MOV, MKV, WMV, WEBM, AVI, 3GP, FLV, MPEG
   * Max video size: 100 MB
   * Video aspect ratio: 9:16 to 16:9
   * Resolution: HD 720p or higher
   * Duration: >30 seconds
> 1. 视频格式规范
>    * 支持格式：MP4、MOV、MKV、WMV、WEBM、AVI、3GP、FLV、MPEG
>    * 最大文件大小：100 MB
>    * 视频宽高比：9:16 至 16:9（推荐 9:16）
>    * 视频时长：建议 >30 秒
>    * 分辨率：推荐 720p 及以上


| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Get Creator Profile](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) | RESTful API | Use this API to get the creator's profile information. |
| [Get Shop Products](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Fu3idMqnqoqwTixg2lklALotgSG) | RESTful API | Developers can utilize this API to search and retrieve product information of shops which is bound by a specific creator with specific keywords. |
| [Get Showcase Products](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405#Back%20To%20Top) | RESTful API <br/>  | This API lists the products in the creator's showcase, paginated by specified page size and iterated through pages by page token for up to 2000 products in the showcase. This API is generally used when a creator would like to view the products in the showcase. The platform will return the product details in the showcase, as well as the products in the livebag if the creator is live streaming. |
###  **IF-161132.V1 Upload video to TikTok Shop.**

1. Before the seller officially publishes the shoppable video, they MUST first call the **Upload Video File** API to upload the video file to the TikTok Shop platform and obtain a unique `file_id`. This `file_id` will be a required parameter for subsequent video publishing.
2. The current upload API does not support modifying an already uploaded video. If the video content needs to be adjusted, it must be regenerated and re-uploaded.
> 1. 在商家正式发布挂车视频之前，必须先调用 Upload Video File 接口，将视频文件上传至 TikTok Shop 平台，并获取一个唯一的 `file_id`。该 `file_id` 将作为后续 **视频发布的**必要入参。
> 2. 目前上传接口不支持对已上传的视频进行修改，如需调整视频内容，必须重新生成并再次上传。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/bece427c7d684f1fbab16edf1d3ff634~tplv-k9wyc2ijk0-image.image)
**Note**

1. Successfully uploading a video file does **not** guarantee that the shoppable video will be published. If the video does not comply with platform policies, it may still fail during the shoppable video review stage.
2. The upload API response includes the field `video_file.md5` (the MD5 checksum of the uploaded file). The developer’s system can calculate the MD5 of the local file before uploading and compare it with the returned value to:
   * Verify that the uploaded file is identical to the local file, preventing file corruption caused by network instability.
   * Ensure file uniqueness when implementing resumable uploads or idempotent uploads.
> 1. 上传视频文件成功不代表一定能发布挂车视频，如不符合平台规范仍会在挂车视频审核环节失败。
> 2. 上传接口返回结果中包含 `video_file.md5` 字段（上传文件的 md5 校验值）。服务商系统可在上传前自行计算本地文件的 md5，与返回值比对。用于：
>    * 确认上传文件与本地文件一致，避免因网络抖动导致的文件损坏；
>    * 做断点续传/幂等上传时的文件唯一性校验。

| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Upload Shoppable Video File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-EEPudRjSEorRmIxMSX6lFIL8gih) <br/>  <br/> **Note**: When using [Upload Shoppable Video File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-EEPudRjSEorRmIxMSX6lFIL8gih) API, <br/> if video ≥ 10mb, must follow [Shoppable Video Large File Upload Solution](https://bytedance.sg.larkoffice.com/docx/WTMvdfbTBo30Fex0r9YlYstGg0d?from=from_parent_docx) | RESTful API | Use this API to upload the video before posting to TikTok <br/>  |
## Precheck and Publish Shoppable Videos with anchors
### **IF-161141.V1 Seller submits video for precheck** 

1. Before the seller publishes the shoppable video, the service provider must ensure the video content meets the following requirements:
   * [Baseline Principle] **TikTok Community Guidelines**: The video must comply with the platform's community rules, otherwise corresponding penalties for violations will be applied.
   * [Baseline Principle] **TTS E-commerce Platform Governance Rules**: The video must not involve prohibited products, improper displays, or any content that violates e-commerce governance rules, otherwise corresponding penalties for violations will be applied.——**✅API supported**
   * [Strong Recommendation] **High-Quality Video Guidelines**: The platform encourages videos to meet high-quality video standards. High-quality videos will receive more GMV benefits.
2. **Precheck API**

 We now provide the capability to support ISVs call the **Pre-check API** to verify whether the video content complies with **TTS E-commerce Governance Rules**. This helps prevent policy violations before posting.

   * We have **Quota Management** of  **Pre-check API**：
      * Each creator account has a **50/daily precheck quota limit.** Quota management for the Pre-check API is **configured independently** from non-API channels.For example, if a creator has **50 precheck quotas** available today for non-API channels (e.g., Seller Center or App posting), they will have a **separate 50 quota as** for API-based prechecks. Usage in one channel does **not affect** the quota in the other channel.
      * Once the quota is exhausted, no new precheck tasks can be initiated.
      * Each API call that successfully creates a **precheck task** consumes one quota. If the same video (file_id) is prechecked multiple times, multiple tasks will be generated — each consuming one quota.

⚠️ **Important Notes**

* It will **not** determine whether the video is **high-quality**, nor verify compliance with **TikTok Community Guidelines**.
3. ISVs need to design the necessary precheck capabilities in the system to further ensure video compliance and content quality beyond the platform's checks.
> 1. 在商家发布挂车视频之前，服务商需确保视频内容满足以下要求：
>    * **[底线原则] TikTok Community Guidelines（TikTok 社区规范）**：视频必须符合平台的社区规则，否则将作出对应违规处罚
>    * **[底线原则] TTS 电商平台治理规则**：视频不得涉及违规商品、违规展示或其他违反电商治理的内容，否则将作出对应违规处罚。
>    * **[强烈推荐] 优质视频规则**：平台鼓励视频满足优质视频标准，优质视频将会获得更多的GMV收益。
> 2. **预审接口已提供**

> 我们现已提供 **预审接口（Pre-check API）**，支持 ISV 在视频发布前调用接口，验证视频内容是否符合 **TTS 电商治理规则（TTS E-commerce Governance Rules）**。接口会帮助商家在视频发布前识别违规风险，防止内容违规。

> * **预审接口的配额管理**：
>    * 每个创作者账号每日拥有50次预审配额。预审的配额在API渠道和非API渠道独立配置，互不影响。例如，如果创作者今天在非API渠道有50个配额，那么在API渠道也会有50个配额，两个渠道之间的配额 **不会互相抵扣或影响。**
>    * 当日配额使用完毕后，将无法发起新的预审任务。建议在系统中做好必要提示。
>    * 每一次成功创建 **预审任务（precheck task）** 的 API 调用会消耗一次配额。如同一个视频（`file_id`）被多次预审，将生成多个任务，每次调用都会消耗一次配额。
> 3. 服务商在系统中需要设计必要的预审检查能力，以便在平台校验之外，进一步保障视频合规性与内容质量。

> 
> Please refer to the following three documents for more details:

> 1. **[Baseline Principle] TikTok Community Guidelines**: [Community Guidelines](https://www.tiktok.com/community-guidelines/en/overview)
> 2. **[Baseline Principle] TTS 电商平台治理规则：**[✨Creator Policy Pulse (August 2025)✨](https://seller-us.tiktok.com/university/essay?knowledge_id=7096334743553838&from=new-and-updated&role=1&identity=1)
> 3. **[Strong Recommendation] High-Quality Video Guidelines**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/59eb6d23a22f4af89e65ce6b4759f08e~tplv-k9wyc2ijk0-image.image)

| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| Pre-check Shoppable Video  | RESTful API | Use this API to pre-check if there's any violation in the video and the shoppable content anchor |
| Get Shoppable Video Pre-check Result  | RESTful API | Use this API to get video pre-check result |
| Shoppable Video Precheck Result | Webhook | Notice the developer about the video pre-check result |
### **IF-161142.V1 Publish shoppable video and bind product anchor**

1. Before the seller can publish a shoppable video, the developer's application must support the seller in providing the following information within the app. Only after completing these fields can the video be submitted for publishing: 
   * **Caption (`caption`):** The video's title and description. Supports hashtags `#` and user mentions `@` to help improve video distribution and exposure.
   * **Video File ID (`file_id`):** Returned from the **Upload Video File** API, serving as the unique identifier for the video.
   * **Associated Product (`product_id`):** Retrieved via the **Get Shop Products** or **Get Showcase Products** API, used to bind the product anchor to the video.
   * **Anchor Title (`anchor_title`):** The text displayed in the shoppable anchor position, helping users quickly understand the product's key selling point.
   * **AI-generated Flag (`video_info.is_ai_generated`):** Optional boolean indicating whether the submitted video is AI generated. Set it to `true` for AI-generated content so the published post displays an AI-generated label. If omitted, it defaults to `false`.
> 1. 商家在发布挂车视频前，开发者应用需要支持商家在应用中填写以下信息，完成后才可以提交发布挂车视频。 
>    * **视频文案（caption）**：作为视频的标题与说明，支持包含话题标签 `#` 和用户提及 `@`，有助于视频分发与曝光。
>    * **视频文件 ID（file_id）**：来自于上传接口返回结果，是视频的唯一标识。
>    * **关联商品（product_id）**：从「Get Shop Products」或「Get Showcase Products」接口获取，用于将商品锚点绑定到视频中。
>    * **商品锚点文案（anchor title���**：展示在挂车位的标题，帮助用户快速理解商品卖点。
>    * **AI 生成内容标识（video_info.is_ai_generated）**：可选布尔字段，用于声明提交的视频是否由 AI 生成。AI 生成内容应传 `true`，发布后的帖子会展示 AI-generated 标签；字段省略时默认为 `false`。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fa92ac11f0294846aad91e23da902f6f~tplv-k9wyc2ijk0-image.image)
After calling `Post Shoppable Video`, the API may return `data.video.quota` together with `data.video.id`. Developers should parse `quota` when present and display a friendly content-posting quota message. If `quota` is omitted, no quota restriction applies and the omission should not be treated as an error.
> 调用 `Post Shoppable Video` 后，接口可能随 `data.video.id` 返回 `data.video.quota`，用于提示创作者当前内容发布配额。字段存在时建议展示友好提示；字段未返回时表示当前无适用配额限制，不应按错误处理。


Note

1. **Required Fields for Shoppable Video**
   * **`video_info.file_id`**: The file ID returned from the upload API.
   * **`video_info.title`**: The video caption/title, up to 4000 characters. Supports hashtags `#` and user mentions `@`.
   * **`tts_anchor_info.product_id`**: The product ID that needs to be anchored to the video.
   * **`tts_anchor_info.title`**: The product anchor displays title, no more than 30 characters, and cannot contain punctuation or emojis.
2. **Content Compliance**
   * Both the video caption and anchor title must comply with the **TikTok Community Guidelines** and **TikTok Shop Video Policies**.
   * The product must be an eligible product for promotion and must remain relevant to the video content.
3. **Quota for the number of shoppable videos that can be posted**
   * Different TikTok accounts have different quotas. Please read the policy seller academy. For example, [US local sellers' policy](https://seller-us.tiktok.com/university/essay?knowledge_id=6939143037667118#posting-limits-for-shoppable-content-us-)
> 1. **挂车视频必填字段**
> * `video_info.file_id`：上传接口返回的文件 ID。
> * `video_info.title`：视频标题/文案，最长 4000 个字符，支持 `#` 和 `@`。
> * `tts_anchor_info.product_id`：需要挂载的商品 ID。
> * `tts_anchor_info.title`：商品锚点展示文案，不超30个字符，不能带标点和emoji。
> 2. **内容合规**
> * 视频文案与锚点文案需符合 TikTok 平台社区规范和电商视频规范
> * 商品必须是可带货商品，且与视频内容保持相关性。
> 3. **挂车短视频发布量限制**
> * 不同账号有不同的限制。请阅读商家大学的政策，以[美国跨境商家大学的政策](https://seller.tiktokshopglobalselling.com/university/essay?knowledge_id=2564695663953681&shop_region=us&identity=1&anchor_link=EC4200CA)为例

| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Post Shoppable Video](https://partner.tiktokshop.com/docv2/page/post-shoppable-video-202607#Back%20To%20Top) <br/>  | RESTful API | Use this API to publish the video. Set `video_info.is_ai_generated` when applicable; it defaults to `false` when omitted. The response may include `data.video.quota`. |
### **IF-161143.V1 Retrieve final result of shoppable video publishing. If it fails, obtain failure reason and provide suggestions for modification/retry.**

1. After the seller submits a shoppable video via the **Post Shoppable Video API**, a `video_id` will be returned. The final publishing status (success / failure / processing) can be obtained in two ways:
   * **Active Query (GET)**: The developer application can periodically call the query API with the `video_id` to retrieve the latest status. This API only returns the publishing result of the video.
   * **Webhook Push**: When the publishing status changes, the platform will send an event to the callback URL configured by the developer application. The webhook provides both the publishing result and a set of failure reason enums. Developers can then guide the seller to modify the video and retry based on the returned result and failure reason.
> 1. 商家通过 Post Shoppable Video **** API **** 提交发布后，会获得一个 `video_id`。最终的发布状态（成功 / 失败 / 处理中）可以通过以下两种方式获取：
>    * **主动查询（GET）**：开发者应用可定期调用查询接口，根据 `video_id` 获取最新状态。该接口仅返回视频的发布结果。
>    * **Webhook 推送**：当视频发布状态发生变更时，平台会向开发者应用配置的回调地址推送事件。该 webhook 不仅包含视频发布结果，还会返回失败原因的枚举值。开发者可根据返回的结果和失败原因，引导商家修改视频并重新提交。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/510cb271f1014bc49ba32f3b9de7d28c~tplv-k9wyc2ijk0-image.image)
**Note**

1. Once the publish API is called, the `file_id` is consumed and cannot be reused, even if the video is not successfully published.
> 1. 当调用了发布接口，代表 `file_id` 已被消费不能再次使用。

| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Get Shoppable Video Status](https://partner.tiktokshop.com/docv2/page/get-shoppable-video-status-202509) | RESTful API | Use this API to get video publish result |
| ~~Video Publish Result~~ | ~~Webhook~~ | ~~Notice the developer about the video publishing result and fail reasons~~ |
###  **IF-161144.V1 Retrieve result of precheck. If the precheck fails, ISVs must block the posting action in their system to prevent the seller from uploading non-compliant content.**

* **Strong Block Logic: If** the precheck fails, ISVs **must block** the posting action in their system to prevent the seller from uploading non-compliant content. The system should clearly display the precheck result — including **result, risk , suggestions.**
* The precheck API will only return the result of whether the video complies with **TTS e-commerce governance rules and** cannot fully guarantee that the video will always comply with platform policies, as **TTS governance and content policies are subject to dynamic updates**



> * **强阻断逻辑**：当预审未通过时，ISV **必须在系统中阻断** 商家的发文操作，防止商家上传不合规的视频。

>  系统需清晰展示预审结果，包括 **result**、**risk**、**suggestions**，并提示警告信息，例如：“您的视频不符合平台规范，无法发布”

> * 预审接口仅会返回视频是否符合 **TTS 电商治理规则（TTS e-commerce governance rules）** 的结果，

> **无法完全保证** 视频始终符合平台的所有合规政策要求，因为 **TTS 的治理规则和内容政策会动态更新**。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fa399a54e62b41eabe59bc1409570437~tplv-k9wyc2ijk0-image.image)
| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Pre-check Shoppable Video ](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-GEyCdCNhGoAZ5TxbVetli7SbgLc) | RESTful API | Use this API to pre-check if there's any violation in the video and the shoppable content anchor |
| [Get Shoppable Video Pre-check Result ](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-WYbCdyN1ToT52TxtU3ClrUuHgkc) | RESTful API | Use this API to get video pre-check result |
| [Shoppable Video Precheck Result](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-NdUqdt1ACoNmxvx5VdYlYr7xgUf) | Webhook | Notice the developer about the video pre-check result |
###  IF-161145.V1 Retrieve result of good quality check
**Disclaimer**
Pre-check results are for reference only guarantee the final outcome after public performance is also affected by TikTok Shop policies, account status,and other factors. The platform's suggested content may be updated in real-time as policies adjust, so please refer to the latest returned results.
> **免责声明**
> 预检查结果仅供参考，无法保证公开视频后的最终审核结果。最终结果还可能受到 TikTok Shop 平台政策、账号状态及其他因素的影响。平台的建议内容可能会随着政策调整而实时更新，请以最新返回的结果为准。


1. ISV can call the **Get Shoppable Video Pre-check Result** API and subscribe to the **Shoppable Video Precheck Result** webhook to obtain the "good quality check" result. This allows sellers to know in advance whether their video is considered **high-quality** and **provides actionable suggestions for improvement** if it is not. Even if suggestions are returned, the video can still be published; this check should not block the publishing process.
2. **Timing**: This API should only be called after uploading the video file (obtaining a `file_id`) and before executing the "post shoppable video" action. This avoids misuse in other scenarios.
3. **Quota Management**:
   1. The **Good Quality Check** supports up to **50 checks per creator account per day**, and this quota is shared with qualified checks.
   2. If the quota is exceeded, the API will return an error. Error will be：`The creator account has reached the daily limit for pre-checks. Please try again tomorrow`Developers should handle this by providing a user-friendly prompt.
4. **Applicability**
   1. The Good quality check is currently available **only for the US region**. 
   2. It applies to videos published by **seller official accounts and affiliate creator accounts**.
> 1. ISV 可以调用 **Get Shoppable Video Pre-check Result API** 并订阅 **Shoppable Video Precheck Result webhook** 来获取「**优质检查（good quality check）​**」结果。

>  这可以帮助卖家提前了解其视频是否被认为是高质量内容；如果未通过，也会返回可执行的优化建议。即使返回了建议，视频**仍然可以发布**，该检查**不应阻塞发布流程**。

> 2. **调用时机**：

>  该 API **仅应在视频文件上传完成（已获得** **`file_id`）之后、执行 “post shoppable video” 操作之前调用**，以避免在其他场景下被误用。

> 3. **配额管理**：
>    1. 「**优质检查（Good quality check）​**」对每个创作者账号**每日最多支持 50 次检查，并且次数与合格检查共享**。
>    2.  当超出配额时，API 将返回错误信息：`The creator account has reached the daily limit for pre-checks. Please try again tomorrow`开发者应对此进行处理，并向用户提供**友好的提示信息**。
> 4. **适用范围：**
>    1. 「优质检查（Good quality check）」目前**仅在 US 地区生效**，其他地区暂不支持。
>    2. 该能力适用于**商家达人账号及联盟达人账号发布的视频**；


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/33a8d0d2810b479db28bbd21f3185a95~tplv-k9wyc2ijk0-image.image)
**API/Notification Overview**
| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Precheck Video Content](https://partner.tiktokshop.com/docv2/page/precheck-video-content-202511) | RESTful API | Use this API to pre-check if there's any violation in the video and the shoppable content anchor |
| [Get Shoppable Video Pre-check Result ](https://partner.tiktokshop.com/docv2/page/get-shoppable-video-precheck-result-202601) | RESTful API | Use this API to get video pre-check results, including the good quality check outcome. |
| [Shoppable Video Precheck Result](https://partner.tiktokshop.com/docv2/page/arpnre1g) | Webhook <br/>  | Notice the developer about the video pre-check result, including the good quality check outcome. |
## Shop Video performance data
### IF-161151.V1 Retrieve video performance data under the shop

1. It is necessary to support the seller in completing shop data authorization, and the authorization type for posting shoppable videos is different. [Check how to do seller auth](https://partner.tiktokshop.com/docv2/page/seller-authorization-guide#Authorization%20in%20development%20stage)
2. Supports the seller in viewing video performance data within the application. The seller can view the performance of all videos in the shop or a specific video, including core business metrics and engagement data, to help evaluate the video’s effectiveness and user engagement.
3. Supported Data:
   1. **Core Business Metrics**:
      * `gmv.amount` 
      * `click_through_rate` 
      * `daily_avg_buyers` 
      * `views` 
   2. **Engagement Data**:
      * `likes`
      * `shares` 
      * `xcomments` 
      * `views` 
> 1. 需要支持商家完成店铺数据授权，和posting shoppable video的接口的授权类型不同。[Check how to do seller auth](https://partner.tiktokshop.com/docv2/page/seller-authorization-guide#Authorization%20in%20development%20stage)
> 2. 支持商家在应用中查看视频表现数据。商家可以查看店铺所有视频或某个特定视频的表现，包括核心经营指标和互动数据，帮助评估视频效果和用户参与度。
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
Note：

| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Get Shop Video Performance List](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-list-202409) <br/>  | RESTful API <br/>  | Returns overall performance metrics for all videos under a shop. This API currently provides data only for shops registered in the United States, United Kingdom, Singapore, Vietnam, and Thailand. |
| [Get Shop Video Performance Detail](https://partner.tiktokshop.com/docv2/page/get-shop-video-performance-details-202409) | RESTful API | Returns detailed performance metrics for a (requested) video. This API currently provides data only for shops registered in the United States, United Kingdom, Singapore, Vietnam, and Thailand. |
| [Get Creator Video Performance Detail ](https://bytedance.sg.larkoffice.com/docx/VkfxdgvBCoL4gMxpZJslZ8xmgcg) | RESTful API | This is a US-creator-only API for now. And it is for getting Tiktok E-commerce video metrics(including anchor_display_rate, ctr, orders, items_sold, gmv) to analyze. |
## Associate music with the Shoppable Videos and set a cover
### IF-161162.V1 The Shoppable Video publishing supports video cover images.

1. When publishing a shoppable video, merchants can set a custom cover to improve content attractiveness. To do this, developers can provide one of the following when calling the API:
   * **Cover Image URI (`cover_uri`)**: Pre-upload an image using the `Upload Shoppable Photo File` API and use the returned `uri` as the video cover.
   * **Cover Timestamp (`cover_timestamp_ms`)**: Specify a timestamp (in milliseconds) in the video. The system will capture the frame at this exact moment to use as the cover.
2. Developer applications must clearly inform merchants of the priority for these two options:
   * If both `cover_uri` and `cover_timestamp_ms` are provided, the system will prioritize `cover_uri` for the cover.
   * If neither is provided, the system will default to using the first frame of the uploaded video as the cover.
> 1. 在开发者应用中，商家发布可购物视频（Shoppable Video）时需要能够设置视频的封面，以提升内容的吸引力。为满足此需求，商家在调用接口时可提供以下任一信息：
>    * **封面图片 URI (`cover_uri`)**：通过 `Upload Shoppable Photo File` 接口预先上传一张图片，并将其返回的 `uri` 作为视频封面。
>    * **封面时间戳 (`cover_timestamp_ms`)**：指定视频中的一个具体时间点（以毫秒为��位），系统将截取该时间点的视频帧作为封面。
> 2. 开发者应用需明确告知商家两种设置方式的优先级：
>    * 如果同时提供了 `cover_uri` 和 `cover_timestamp_ms`，系统将优先采用 `cover_uri` 作为封面。
>    * 如果两者均未提供，系统将默认使用已上传视频的第一帧作为封面。
> * 封面内容（无论是上传的图片还是视频截图）必须遵守 **TikTok 社区规范**与 **TikTok Shop 电商视频政策**。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/112607dc28ec43ce9b4fb555050f4a56~tplv-k9wyc2ijk0-image.image)
| **API/Notification name** | **Type** | **Description** |
| --- | --- | --- |
| [Post Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-TV8qdaPDLo49yxxamEblRomKgMh) | RESTful API | Use this API to publish the video with a specified cover. |
| [Upload Shoppable Photo File](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#IGBzdu65Ao0Urdxqj00lPH69gPo) | RESTful API | Use this API to upload a photo file and get its URI for the cover. |
### IF-161161.V1 Search music **** 
Before merchants publish shoppable video content, developer applications can support merchants in searching for music by entering **keywords** within the app. The searched music can be played and directly used in subsequent shoppable posting steps. **All music retrieved through the API query is authorized for E-commerce use and can be directly applied without risk of violation.**

* **Music ID (music_id)**: The unique ID associated with the searched music, which can be directly used in subsequent shoppable posting steps.
* **Keyword (keyword)**: The search term entered by the user, used to match music titles or authors.
* **Language (language)**: Supports defining the response language, such as English.
* **Play URL (play_url)**: The returned playback URL, which supports playing the music.

> 在商家发布挂车内容前，开发者应用可以支持商家在应用中通过输入关键词搜索音乐，搜索到的音乐支持播放，可以在后续挂车步骤中直接使用。**接口查询获取的音乐均为有电商权限的音乐，可直接使用，无违规风险。**

> * **音乐 ID (music_id)**：搜索到的音乐关联的唯一 ID，在后续挂车步骤中可直接使用。
> * **关键词 (keyword)**：用户输入的搜索词，用于匹配音乐名称或作者。
> * **语言 （language）**：支持定义返回语言，例如英语等。
> * **播放链接(play_url)**:返回的播放链接，支持播放音乐。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/53d2c47d70314806ae59cb6745faeb1e~tplv-k9wyc2ijk0-image.image)
| **API/Notification name** | **type** | **description** |
| --- | --- | --- |
| [Search Music](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Spk6d6AHuoE3Oix24Nslptczgkb) | RESTful API | Recommend music information based on keywords. Search Music is available globally across supported TikTok Shop markets. Use the `region` and `language` query parameters to localize results. |
### IF-161163.V1 The Shoppable Video publishing supports Binding music.

1. When publishing a shoppable video, merchants can add background music (BGM) to enhance the video's appeal and engagement.
   * Merchants must specify the desired music using a `music_id` within the application.
   * If the video is linked to background music, the original video audio will be overridden by the music.
> 1. 在开发者应用中，商家发布可购物视频（Shoppable Video）时，可以为视频关联一段背景音乐（BGM），以增强视频的趣味性和传播效果。
>    * 商家需要在应用内通过 `music_id` 来指定所需的音乐。
>    * **如果视频关联音乐，那么视频原声（包含口播）会被音乐覆盖**


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/bf901f4209bd46f4a0d82b493ff3cb7a~tplv-k9wyc2ijk0-image.image)

| **API/Notification name** | **Type** | **Description** |
| --- | --- | --- |
| [Post Shoppable Video](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-TV8qdaPDLo49yxxamEblRomKgMh) | RESTful API | Use this API to publish the video with specified background music. |
| [Search Music](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f#share-Spk6d6AHuoE3Oix24Nslptczgkb) | RESTful API <br/>  | Use this API to search for licensed music and obtain a valid `music_id`. Search Music is available globally across supported TikTok Shop markets; use the `region` and `language` query parameters to localize results. |
# Appendix
# **FAQs**
| Can a video still receive violation warnings after publishing, even if the Video pre-check API found no issues before posting? | Yes, it is possible. Pre-check results are for reference only and do not guarantee the final outcome after publication.  |
| --- | --- |
| If a video passes the Video pre-check review, does it guarantee good performance? | No, pre-check results are for reference only and do not guarantee the final outcome after publication. Video performance is affected by multiple factors, including TikTok Shop content policies, account status, content quality and more.  |
| How many pre-checks can seller conduct per day via API? | Sellers have at least 2 pre-checks per day. The number of pre-checks available may vary based on seller performance.  |
| What happens if a creator’s account type is both Marketing Account and Affiliate Creator in the Get Creator Profile API response? | In cases where a creator's account type is both Marketing Account and Affiliate Creator, the Get Creator Profile API will return `Marketing Account` to the `type` field.  |
| If account A uploads a video and receives a file_id, can this file_id be used to publish the video through account B? | No, the file_id returned by the Upload Video API for account A cannot be used by account B to publish the video. The file_id is specific to the account under which the video was uploaded. Each account has its own unique session for video uploads, and the file_id generated is tied to that session. |
| [What are the functions of TikTok Shop official account?](https://seller-us.tiktok.com/university/essay?knowledge_id=5643789953599275&identity=1&anchor_link=EBCE00CE) | Once the TikTok account is linked as the TikTok shop's official account, it will be the main representative of your shop on TikTok. The products in your shop will be automatically synchronized to the Shop Page. The Shop Page will also act as the central page for product display and promotions. <br/>  <br/> * **Accumulate store fans and increase repurchase rate** <br/>    * After binding the store's official TikTok account, the official account and the store's fan user group can be connected. After users follow your store's official TikTok account, they can easily find your store's entrance on the account's profile page through the store's official TikTok account, helping the store to attract traffic and increase the repurchase rate. <br/> * **Improve store exposure and precipitate traffic** <br/>    * Users can easily search for products in your store through TikTok's search function, and add a new store page entry for the whole link of sales in the live broadcast room to help your products and stores gain more exposure on TikTok. |
| [What are the rules for the official TikTok Shop account?](https://seller-us.tiktok.com/university/essay?knowledge_id=5643789953599275&identity=1&anchor_link=EBEB00CD) | * Each shop can only be bound to one official account. <br/> * The shop name and the bound official account's name must be consistent after upgrade, and when the store name is modified, the official account name will be changed simultaneously. Please be careful when changing the shop name. <br/> * The official account can be unbound once **24 hours after the official account is successfully bound. Please note official account can only be unlinked 3 times**； <br/> * The account region needs to be the same as the shop region. <br/> * The same account cannot be bound as the official account and marketing account of the same store at the same time. <br/> * The account can only sell the product from their own shop and fail to participate in the affiliate program. If sellers want to participate in affiliate, they can use their marketing account or creator account to apply for permission.  |
| [How to bind TikTok Shop official account?](https://seller-us.tiktok.com/university/essay?knowledge_id=5643789953599275&identity=1&anchor_link=EC0800CC) | Check details in the link |
# APIs
## [GET] Get Shop Products
### Summary
| Type | Value |
| --- | --- |
| API Name | Get Shop Products |
| API Version | 202509 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/shop_products |
| API Method | GET |
| API Function Description | Developer can utilize this API to search and retrieve products information of shop which is bound by a specific creator with specific keywords. |
### Request Parameters
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
| title_keyword | string | false | apple | The title keyword of the product you wish to search by. |
| sort_field | string | false | PRODUCT_ID | Sort fields include PRODUCT_ID, PRICE and SALE. If sort_field is empty or invalid, PRODUCT_ID will be set as default. |
| sort_order | string | false | DESC | Sort orders include DESC and ASC. If sort order is empty or invalid, DESC will be set as default. |
| page_size | int32 <br/>  | true | 20 | Pagination count determines how many products you'll get after sending the request. 20 is a recommended number. <br/> Valid Range: [1-20] |
| page_token | string | false | b2Zmc2V0PTAK | The pagination offset that determines where you begin your search. If you are making your first request, this will be empty. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | application/json | Allowed type: application/json |
#### Body(Not applicable for GET/DELETE)
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
**Request body example:**
```JSON
{}
```

### Response Parameters
| Properties |  |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- | --- |
| code |  |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  |  | object |  | Specific return information |
| > | products |  |  | []object |  | The searched product list. It will be empty when there are no search results. |
| > | > | id |  | string | 1729592969712207012 | TikTok product ID. |
| > | > | title |  | string | testcase autotest Live Product | Product name. |
| > | > | price |  | object |  | Product price shown with two decimal places and currency. |
| > | > | > | amount | string | 56.00 | Product price with two decimal places. |
| > | > | > | currency | string | USD | Product price currency, based on region where creators can sell. |
| > | > | added_status |  | string | ADDABLE | Showcase add status with possible values: <br/> - ADDABLE <br/> - ADDED <br/> - REJECTED |
| > | > | brand_name |  | string | Apple | The brand name a seller has set for a product. |
| > | > | images |  | []object |  | Images of a product. |
| > | > | > | url | string | https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/982dd6b4e46a6a24203b00611a474cca~c5_1080x1080.webp | The URL of the product image. |
| > | > | > | width | int32 | 200 | The width of the product image. |
| > | > | > | height | int32 | 200 | The height of the product image. |
| > | > | sales_count |  | int32 | 33 | The number of products that have been sold. |
| > | total_count |  |  | int32 | 300 | The total number of products that meet the query conditions. |
| > | next_page_token |  |  | string | b2Zmc2V0PTAK | The pagination token is a cursor used for pagination. The token is returned in the previous pagination query to determine the current position. It will be empty when there aren't any products to search for. |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
### Curl
```Bash
curl -X GET \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202509/shop_products?timestamp=1623812664&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&sort_order=DESC&page_size=20&app_key=29a39d&title_keyword=apple&sort_field=PRODUCT_ID&page_token=b2Zmc2V0PTAK' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```

### Error Codes
| Error Code | Error Message |
| --- | --- |

## **[POST] Upload Shoppable Video**
 If the video size exceeds 10 MB, please follow [Shoppable Video Large File Upload Solution](https://bytedance.sg.larkoffice.com/docx/WTMvdfbTBo30Fex0r9YlYstGg0d)
### Summary
| Type | Value |
| --- | --- |
| API Name | Upload Shoppable Video File |
| API Version | 202505 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/videos/video_files |
| API Method | POST |
| API Function Description | Use this API to upload the video before posting to TikTok |
### Request Parameters
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | multipart/form-data | Allowed type: multipart/form-data |
#### Body
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| data | binary | true |  | The local file to be uploaded. <br/> Note： <br/> - Supported formats: MP4, MOV, MKV, WMV, WEBM, AVI, 3GP, FLV, MPEG <br/> - Max video size: 100 MB <br/> - Video aspect ratio: 9:16 to 16:9 <br/> Recommendations for product videos: <br/> - Resolution: 720p or higher <br/> - Duration: > 30 seconds |
**Request body example:**
```JSON
{
  "data": ""
}
```

### Response Parameters
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  | object |  | Specific return information |
| > | video_file |  | object |  | Video file information. |
| > | > | id | string | 123123123123 | The id from of the uploaded video file. |
| > | > | md5 | string | D41D8CD98F00B204E9800998ECF8427E | Upload file md5 checksum |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
### Curl
```Bash
curl -X POST \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202505/videos/video_files?timestamp=1623812664&app_key=29a39d&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: multipart/form-data' \
-F 'data=@"file"'
```

### Error Codes
| Error Code | Error Message |
| --- | --- |
## [POST] Upload Shoppable Photo File
### Summary
| Type | Value |
| --- | --- |
| API Name | Upload Shoppable Photo File |
| API Version | 202511 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/photos/photo_files |
| API Method | POST |
| API Function Description | Use this API to upload the photos before video posting. It returns the photo_file_uri for each uploaded image |
### Request Parameters
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | multipart/form-data | Allowed type: multipart/form-data |
#### Body(Not applicable for GET/DELETE)
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| data | binary | true |  | The local file to be uploaded. <br/> The local image file to be uploaded. <br/>  <br/> Note: <br/> - Supported formats: JPG, JPEG, PNG, WEBP, HEIC, BMP <br/> - Max size: 10MB <br/>  <br/> - aspect ratio: 9:16 to 16:9 |
**Request body example:**
```JSON
{
  "data": ""
}
```

### Response Parameters
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  | object |  | Specific return information |
| > | photo_file |  | object |  | Photo Info |
| > | > | photo_uri | string | skldjfskdlfjlskdfs000023423s | In [Post Shoppable Video], use this photo URI to fill cover_uri field |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
### Curl
```Bash
curl -X POST \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202511/photos/photo_files?sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664&app_key=29a39d' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: multipart/form-data' \
-F 'data=@"file"'
```

### Error Codes
| Error Code | Error Message |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
## **[POST] Post Shoppable Video**
### Summary
| Type | Value |
| --- | --- |
| API Name | Post Shoppable Video |
| API Version | 202607 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/videos |
| API Method | POST |
| API Function Description | Use this API to post the shoppable video. |
### Request Parameters
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key <br/>  | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | application/json | Allowed type: application/json |
#### Body(Not applicable for GET/DELETE)
| Properties |  | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| video_info |  | object | true |  | Video information |
| > | file_id | string | true | v12d00gd0024d3nfqr7og65 | Video file_id from [Upload Shoppable Video File] |
| > | title | string | true | Sample video title | The video caption. <br/> The maximum length is 4000 in UTF-16 runes. <br/> If not specified, the ticket post will not have any captions. |
| > | cover_uri | string | false | v12d00gd0024d3nfqr7og65oooiuuyy | Video cover image URI, which is returned after uploading the image via the Upload Shoppable Photo File API. |
| > | cover_timestamp_ms | int32 | false | 1000 | The input parameter is a timestamp, which specifies a particular moment in the video. The frame at that timestamp will be used as the video cover. If cover_uri and cover_timestamp_ms are both not provided, the cover will default to the first frame of the uploaded video. Only one of cover_uri or cover_timestamp_ms can be provided. If both parameters are passed, cover_uri will take precedence. |
| > | music_id <br/>  | string | false | 717294069642063456 | The music ID for the video BGM. If not provided, no music will be associated with the video. The music ID must be obtained via Search Music Library. |
| > | is_ai_generated | bool | false | true | Indicates whether the submitted video content is AI generated. Set to `true` to display an AI-generated label on the published post. Defaults to `false` when omitted. |
| product_link_info |  | object | true |  | Product link information |
| > | product_id | string | true | 17294069642063424 | Use product_id to bind the product with the video. <br/> The product_id from [Get Shop Products] or [Get Showcase Products] |
| > | title | string | true | Sample product anchor title | The title to be shown on the product anchor. Anchor title should be shorter than 30 characters. |
**Request body example:**
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

### Response Parameters
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  | object |  | Specific return information |
| > | video |  | object |  | Published video information |
| > | > | id | string | 7548431509997292816 | The video id, use this id to query video publish status. |
| > | > | quota | string | 3/day | Content posting quota for the creator. Returned on successful publish; included in the error message on failure; omitted if no quota restriction applies. |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
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

### Error Codes
| Error Code | Error Message |
| --- | --- |
| 16011007 | Product link title should be no longer than 30 characters. |
| 16011009 | Product link title contains offensive language. |
| 16011069 | Product link title contains punctuation or emoji. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 38007001 | System Error |
| 170001002 | Creator TikTok Shop permission check failed. |
| 170001003 | Creator Tiktok Shop permission temporarily banned. |
| 170001004 | Creator TikTok Shop permission is permanently banned. |
| 170001005 | Creator terms of service not signed. Please contact TikTok for more details. |
| 170001006 | GKA terms not signed. Please try again after signing GKA term. |
| 170001007 | Creator did not sign the EU data share agreement. |
| 170001008 | Creator Age verification failed. Please verify age first. |
| 170001009 | The product belongs to unsupported category. |
| 170001010 | The commission plan gets failed or rejected. |
| 170001011 | The product doesn't exist. |
| 170001012 | The product is not available. |
| 170001013 | Showcase SPU exceeds limit. |
| 170001014 | Blocked by spam check. |
| 170001015 | Blocked by TikTok Shop risk control. |
| 170001018 | Get creator pay account error. Please verify the pay account first. |
| 170001020 | You have exceeded the frequency to post EC short videos. Please take a rest. |
| 170001024 | cover_timestamp_ms must be a non-negative integer within the video duration. |
| 170001025 | cover_timestamp_ms exceeds the video duration. |
| 170001030 | Creator account banned. Please contact TikTok agent for your account. |
| 170001031 | Creator forbidden to post content. |
| 170001040 | Please use valid video file id to post TikTok Shop short video. |
| 170001050 | Getting errors during video posting workflow. Please try again or contact TikTok. |
## **[GET] Get Shoppable Video Status**
### Summary
| Type | Value |
| --- | --- |
| API Name | Get Shoppable Video Status |
| API Version | 202509 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/videos/:video_id/status |
| API Method | GET |
| API Function Description | Use this API to get shoppable video posting results. |
### Request Parameters
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| video_id | string | true | 7548431509997292816 | The video id from [Publish Shoppable Video] |
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | application/json | Allowed type: application/json |
#### Body(Not applicable for GET/DELETE)
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
**Request body example:**
```JSON
{}
```

### Response Parameters
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  | object |  | Specific return information |
| > | video |  | object |  | returned video info |
| > | > | id | string | 7493990579714164574 | Video id |
| > | > | post_status | string | FAIL | Video posting status, possible values: <br/> - SUCCESS <br/> - FAIL <br/> - PROCESSING |
| > | > | post_time | int64 | 1685548800 | Returned if the video has been successfully posted, i.e. `posting_status = SUCCESS`. <br/> Represented in seconds. |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
### Curl
```Bash
curl -X GET \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202509/videos/7548431509997292816/status?sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664&app_key=29a39d' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```

### Error Codes
| Error Code | Error Message |
| --- | --- |
| 38007001 | System Error |
| 170001016 | The video does not belong to the creator. Please check valid video status. |

## **[POST] Pre-check Shoppable Video** 
### Summary
| Type | Value |
| --- | --- |
| API Name | Precheck Video Content |
| API Version | 202511 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/videos/precheck_task |
| API Method | POST |
| API Function Description | Use this API to pre-check if there's any violation in the video and the shoppable content anchor |
### Request Parameters
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | application/json | Allowed type: application/json |
#### Body(Not applicable for GET/DELETE)
| Properties |  | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| video_info |  | object | true |  | Video information |
| > | file_id | string | true | v12d00gd0024d3nfqr7og65 | Video file_id from [Upload Shoppable Video File](https://api/affiliate_creator/202505/videos/video_files) |
| product_link_info |  | object | true |  | Product link information |
| > | product_id | string | true | 17294069642063424 | Use product_id to bind the product with the video. <br/> The product_id from [Get Shop Products](https://api/affiliate_creator/202509/shop_products) or [Get Showcase Products](https://api/affiliate_creator/202405/showcases/products) |
| > | title | string | true | Sample product anchor title | The title to be shown on the product anchor. Anchor title should be shorter than 30 characters. |
**Request body example:**
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

### Response Parameters
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  | object |  | Specific return information |
| > | precheck |  | object |  | Video content pre-check task result |
| > | > | task_id | string | 1123123123 | pre-check task id |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
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

### Error Codes
| Error Code | Error Message |
| --- | --- |
| 16011007 | Product link title should be no longer than 30 characters. |
| 16011009 | Product link title contains offensive language. |
| 16011069 | Product link title contains punctuation or emoji. |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 170001002 | Creator TikTok Shop permission check failed. |
| 170001005 | Creator terms of service not signed. Please contact TikTok for more details. |
| 170001006 | GKA terms not signed. Please try again after signing GKA term. |
| 170001007 | Creator did not sign the EU data share agreement. |
| 170001008 | Creator Age verification failed. Please verify age first. |
| 170001009 | The product belongs to unsupported category. |
| 170001010 | The commission plan gets failed or rejected. |
| 170001011 | The product doesn't exist. |
| 170001012 | The product is not available. |
| 170001013 | Showcase SPU exceeds limit. |
| 170001014 | Blocked by spam check. |
| 170001015 | Blocked by TikTok Shop risk control. |
| 170001018 | Get creator pay account error. Please verify the pay account first. |
| 170001019 | The user has exceeded allocated daily quota for precheck resource |

## **[Get] Get Shoppable Video Pre-check Result** 
### Summary
| Type | Value |
| --- | --- |
| API Name | Get Shoppable Video Precheck Result  |
| API Version | 202511 |
| API URI ( Fixed for all APIs ) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path | /affiliate_creator/:version/videos/precheck_tasks/:task_id |
| API Method | GET |
| API Function Description | Use this API to get video pre-check result |
### Request Parameters
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| task_id | string | true | 7493990579714164574 | task id from [Precheck Video Content](https://api/affiliate_creator/202511/videos/precheck_task) |
#### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
#### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | The creator access_token value from [Get Access Token](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75#Get%20Access%20Token%20API), when user_type = 1. Follow this [guide](https://partner.tiktokshop.com/docv2/page/678e3a362dccb8030ea6f98c) to get creator access_token. |
| content-type | string | true | application/json | Allowed type: application/json |
#### Body(Not applicable for GET/DELETE)
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
**Request body example:**
```JSON
{}
```

### Response Parameters
| Properties |  |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- | --- |
| code |  |  |  | int32 | 0 | The success or failure status code returned in API response. |
| message |  |  |  | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id |  |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  |  | object |  | Specific return information |
| > | precheck_task |  |  | object |  | Video pre-check task |
| > | > | id |  | string | 7493990579714164574 | The id of the video pre-check task. |
| > | > | result |  | string | FAIL | SUCCESS: The precheck task passed checks <br/> FAIL: The precheck task has failed due to violations. Check the 'issues' field for details. <br/> PROCESSING: The precheck task is still in progress |
| > | > | issues |  | []object |  | A list of policy violation details returned when the task fails |
| > | > | > | risk | string | Pirated Content | Policy violation |
| > | > | > | suggestions | string | Your video may include unoriginal content. Creating original content is essential for standing out from the crowd. | Detailed guidance to resolve the detected violation. |
Note: parameter preceded by ">" means the parameter is a subobject.
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

### Code Sample
### Curl
```Bash
curl -X GET \
 'https://open-api.tiktokglobalshop.com/affiliate_creator/202511/videos/precheck_tasks/7493990579714164574?app_key=29a39d&sign=bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290&timestamp=1623812664' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```

### Error Codes
| Error Code | Error Message |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
## [Get] **** Search Music 
#### Overview | 基础定义
| Type \| 类型 | Value \| 值 |
| --- | --- |
| API Name \| API 名称 | Search Music |
| API Version \| API 版本 | 202602 |
| API URI \| API 统一资源标识 (所有 API 固定) | Host: open-api.tiktokglobalshop.com <br/> Schemes: HTTPS |
| API Path \| API 访问路径 | /affiliate_creator/:version/music/search |
| API Method \| API 方法 | GET |
| API Function Description \| API 功能描述 | Use this API to get music information. Search Music is available globally across supported TikTok Shop markets; use the `region` and `language` query parameters to localize results. |
#### Request Parameters | 入参定义
##### Path
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
##### Query
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| app_key | string | true | 38abcd | Every single app will have a unique key. Please use the specific key assigned to your app. |
| sign | string | true | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.  |
| timestamp | int64 | true | 1623812664 | Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time. |
| keyword | string | true | love | Search keyword |
| search_id | string | false | 2026021821534288157A7F308E8C81359B | For the first page, leave search_id empty, the response will return a search_id. Starting from page 2 (i.e., when page_token > 0), include that same search_id in every request to continue paging; otherwise, pagination may fail. |
| page_token | string | false | 40 | First page: leave empty.  <br/> Next page: copy the next_page_token from the previous response and fill it here |
| page_size | string | false | 20 | Page size |
| region | string | false | US | Region code (ISO 3166-1 alpha-2) |
| language | string | false | en-US | Language tag (BCP-47) |
##### Headers
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
| x-tts-access-token | string | true | 29a39d | Seller access_token |
| content-type | string | true | application/json | Allowed type: application/json |
##### Body(Not applicable for GET/DELETE | GET/DELETE请求不适用)
| Properties | Type | Required | Example | Properties description |
| --- | --- | --- | --- | --- |
**Request Body Example**
```JSON
{}
```

#### Response Parameters ｜ 出参定义
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| music |  |  | []object |  | Music list |
| > | id |  | string | 717294069642063456 | Music id |
| > | title |  | string | Love Story | Music title |
| > | author |  | string | Taylor Swift | Artist name |
| > | cover_thumb |  | object |  | Cover image |
| > | > | url_list | []string | ["https://example.com/music/cover/love_story_1.jpg"] | Cover image URL list |
| > | duration |  | string | 235 | Duration in seconds |
| > | play_url |  | object |  | Play URL |
| > | > | url_list | []string | ["https://example.com/music/play/love_story.mp3"] | URL list |
| next_page_token |  |  | string | 40 | use this as the next request’s page_token, only meaningful when has_more=true. |
| has_more |  |  | bool | false | Whether there is another page. |
| search_id |  |  | string | 2026021821534288157A7F308E8C81359B | Use the same search_id for all subsequent pages of the same search. |
Note: parameter preceded by ">" means the parameter is a subobject.
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

#### Error Codes | 错误码定义
| **Error Code** | **Error Message** |
| --- | --- |
|  |  |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
## Shoppable Video Precheck Result(webhook)
#### Webhook payload 
| Properties |  |  | Type | Example | Properties description |
| --- | --- | --- | --- | --- | --- |
| type |  |  | int | 55 | The ID of the webhook type. |
| tts_notification_id |  |  | string | 7327112393057371910 | The ID of the notification. |
| creator_open_id <br/>  |  |  | string | VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw | The open_id of the creator. To get the value, see [Authorization overview](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75). <br/>  |
| timestamp |  |  | int | 1644412885 | The UNIX timestamp when this webhook was triggered. |
| data |  |  | object |  |  |
| > | precheck_task_id <br/>  |  | string <br/>  | 7493990579714164574 |  <br/>  |
| > | result <br/>  |  | string | "FAIL" <br/>  | PASS <br/> FAIL |
| > | issues <br/>  |  | []object <br/>  |  | Only if the "result" is "FAIL" |
| > | > | risk | string | "Pirated Content" | Risk type. |
| > | > | ~~todo~~ <br/> suggestion <br/>  <br/>  | string <br/>  | "Your video may include unoriginal content. Creating original content is essential for standing out from the crowd." | How to fix this risk. <br/>  |
Note: parameter preceded by ">" means the parameter is a subobject.
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

