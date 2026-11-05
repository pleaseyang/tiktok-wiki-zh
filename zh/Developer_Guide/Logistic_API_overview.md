# 物流 API 概述

# 背景
物流 API 帮助您获取物流资源信息，包括：

* 获取仓库列表
* 获取已订阅的配送选项
* 获取物流服务商
* 获取全球仓库列表


当卖家创建/发布商品时，他们可能需要：

* 获取仓库列表
* 获取全球仓库列表

更多详情，请参阅 ["商品 API" 概述](https://partner.tiktokshop.com/docv2/page/650b23eef1fd3102b93d2326)。

当卖家履约订单时，他们可能需要：

* 获取已订阅的配送选项
* 获取物流服务商

更多详情，请参阅 ["履约 API" 概述](https://partner.tiktokshop.com/docv2/page/650b2044f1fd3102b93c9178)。
# 重要概念
## 仓库
仓库是卖家在创建 TikTok Shop 账号时设置的。这是订单需要发货时包裹发出的地方。
一个卖家可以有多个全球仓库。
一个卖家可以为一个店铺拥有多个仓库。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/54149c6a76d3475b8f50e2dc02ff442a~tplv-k9wyc2ijk0-image.image)
当卖家想创建全球商品时，他们需要基于全球仓库明确库存（[获取全球仓库列表 API](https://partner.tiktokshop.com/docv2/page/650aa3f0defece02be6e5ffb?external_id=650aa3f0defece02be6e5ffb#Back%20To%20Top)）。
当卖家想发布全球商品时，他们需要基于仓库明确库存（[获取仓库列表 API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6)）。
## 配送选项
配送选项是协助卖家将商品交付给客户的物流方案。
配送选项包含一组物流服务商和物流服务。
卖家需要在配送选项要求下履约订单，包括物流服务商、物流服务、尺寸、重量等。
配送选项由买家在 TikTok 下单时选择。配送选项的示例包括 Seller Shipping 的"Express shipping"、TikTok Shipping 的"Economy Shipping"等。
请注意，Seller Shipping 的 Express Shipping 和 TikTok Shipping 的 Express Shipping 实际上是两个不同的配送选项。
### 配送类型
配送类型是卖家发货的方式。它是配送选项的一个属性。
TikTok 支持多种配送类型：

* Platform - 卖家通过 TikTok 与物流服务商连接。
* Seller - 卖家通过自己的渠道与物流服务商连接，然后将物流单号上传到 TikTok 进行后续跟踪。

对于不同地区，TikTok 提供不同的配送服务，包括购买面单、安排配送等。
## 物流服务（美国）
物流服务是由一个服务商提供的具体物流解决方案。
不同的配送选项有不同的可用物流服务。
物流服务的示例包括"USPS Ground"、"DHL eCommerce SM parcel"。
## 物流服务商
物流服务商是提供物流服务的服务商。
不同的配送选项有不同的可用物流服务商。
对于使用"seller shipping"类型配送选项的订单，卖家需要在履约过程中更新物流服务商和物流单号。
物流服务商的示例包括"USPS"、"DHL eCommerce"。
重要提示："DHL"和"DHL eCommerce"是两个不同的服务商。

下图概述了配送选项、物流服务商和物流服务之间的关系。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/dcefc31a473646bca211ab30380158e2~tplv-k9wyc2ijk0-image.image)

# 常见问题

* 卖家和店铺之间的关系是什么？

一个卖家可以在多个地区经营业务。
对于每个地区，一个卖家可以拥有一个 TikTok 店铺。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/46c96cf5ec98442894d42cf2814ecf94~tplv-k9wyc2ijk0-image.image)

* 全球仓库和仓库之间的关系是什么？

当存在全球仓库时，对于每个地区，都有一个仓库实际上指向该全球仓库。

* 仓库和配送选项之间的关系是什么？

一个仓库可以订阅多个配送选项。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5574a789943f4a55b9bec9904dad5324~tplv-k9wyc2ijk0-image.image)

* 不同配送选项之间有什么区别？

订单详情中有以下几条履约信息：

* 配送选项 ID
* 履约类型：表示商品将从 TikTok 仓库还是卖家仓库发出
      * FULFILLMENT_BY_TIKTOK
      * FULFILLMENT_BY_SELLER
* 配送方式：表示包裹将通过 TikTok 购买面单还是通过卖家自己的渠道发货。
      * TikTok
      * Seller

对于履约类型 - FULFILLMENT_BY_TIKTOK，TikTok 将自动代表卖家处理订单。卖家不需要管理履约流程。
对于履约类型 - FULFILLMENT_BY_SELLER，卖家需要使用履约 API 处理订单。
有关履约流程的更多详情，请参阅 [履约 API 概述](https://partner.tiktokshop.com/docv2/page/650b2044f1fd3102b93c9178)。

