# Fulfillment API 概述

# 背景
Fulfillment API 允许卖家履行 TikTok Shop 订单。
TikTok Shop 提供两种 fulfillment 类型：

1. Fulfilled by TikTok（FULFILLMENT_BY_TIKTOK）：TikTok 将自动代表卖家处理订单。卖家无需管理 fulfillment 流程。
2. Fulfilled by Seller（FULFILLMENT_BY_SELLER）：在此 fulfillment 类型下，有两种 shipping 类型：

a) TikTok shipping（TIKTOK）：有时也称为"平台 shipping"或"通过平台发货"。在此 shipping 类型下，卖家通过 TikTok Shop 购买 shipping label，并安排 TikTok Shop carrier 上门取件，或将包裹送至 TikTok Shop carrier 的投递点。卖家可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0) 或 [Get Order List](https://partner.tiktokshop.com/docv2/page/650aa8094a0bb702c06df242) 获取 shipping 类型。
b) Seller shipping（SELLER）：有时也称为"通过卖家发货"。卖家通过自己的渠道管理 shipping。在此 shipping 类型下，卖家调用 Fulfillment API 将 shipping 详情回传给 TikTok Shop。卖家可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0) 或 [Get Order List](https://partner.tiktokshop.com/docv2/page/650aa8094a0bb702c06df242) 获取 shipping 类型。
Fulfillment API 还提供拆包发货（split-package）和合包发货（consolidated-package，有时也称为 combined package）的 shipment 选项，以支持更灵活的 shipping 需求。卖家可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0) 或 [Get Order List](https://partner.tiktokshop.com/docv2/page/650aa8094a0bb702c06df242) 获取 fulfillment 类型。
# API 概述
## TikTok shipping
使用平台 shipping 时，根据具体市场，卖家可以通过从 TikTok 购买 shipping label，或安排与 TikTok carrier 的包裹交接来进行 shipment。
### 购买 shipping（美国、英国、EMEA 和日本）

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/ee9e1ae6578e47028d0c0606aaff3883~tplv-k9wyc2ijk0-image.image)


### 安排 shipping（东南亚和拉丁美洲）

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5a146a17252244d89f7343fb26b44e8d~tplv-k9wyc2ijk0-image.image)


**从 TikTok 购买 shipping（美国、英国、EMEA 和日本）**
卖家可以根据包裹的尺寸和重量要求从 TikTok 购买 label。

1. 使用 [Get Eligible Shipping Service](https://partner.tiktokshop.com/docv2/page/650aa6b2bace3e02b75dda4e?external_id=650aa6b2bace3e02b75dda4e) API 获取可用的 shipping service（美国和日本）；
2. 使用 [Create Package](https://partner.tiktokshop.com/docv2/page/650aa132bace3e02b75d40d8?external_id=650aa132bace3e02b75d40d8) API 购买 shipping service 并创建 shipping label。
3. 使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取 shipping label。

**注意：**
在调用 [Create Package](https://partner.tiktokshop.com/docv2/page/650aa132bace3e02b75d40d8?external_id=650aa132bace3e02b75d40d8#Back%20To%20Top) API 之前，请确保订单未被取消，且没有待卖家审批的取消请求。

1. 在冷静期（订单支付后 1 小时内），买家可以无需卖家批准即可取消订单。
2. 冷静期过后，买家可以请求取消订单，需等待卖家批准。

请确保在调用 [Create Package](https://partner.tiktokshop.com/docv2/page/650aa132bace3e02b75d40d8?external_id=650aa132bace3e02b75d40d8#Back%20To%20Top) API 成功完成 label 购买后，再使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取 shipping label。
英国市场在包裹尺寸不可用时也可以使用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1?external_id=650aa4f1defece02be6e7cb1) API

**从 TikTok 安排 shipping（东南亚、拉丁美洲）**
卖家可以与 shipping 提供商安排包裹交接时间和方式。

1. 使用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1?external_id=650aa4f1defece02be6e7cb1) API 安排包裹交接时间和方式。
2. 使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取 shipping label。

**注意：**
在调用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 发货之前，请确保订单未被取消或有待响应的取消请求。

1. 在冷静期（订单支付后 1 小时内），买家可以无需卖家批准即可取消订单。
2. 冷静期过后，买家可以请求取消订单，需等待卖家批准。
3. 针对**巴西**市场，卖家必须在发货前上传发票文件。请使用 [POST Upload Invoice](https://partner.tiktokshop.com/docv2/page/67b542559a140004b343984f?external_id=67b542559a140004b343984f#Back%20To%20Top) endpoint。在通过 webhook [invoice status change] 获取发票上传成功的信息后，即可发货。

请确保在调用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 成功安排 shipment 后，再使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取 shipping label。

## Seller shipping
使用卖家 shipping 时，卖家直接与 shipping carrier 安排 shipment，并上传 shipment tracking number 以通知 TikTok 包裹已发货。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4a56b2fa1505407488165cc0a6e74301~tplv-k9wyc2ijk0-image.image)



**美国和 EMEA 市场流程：**

1. 卖家发货并从 shipping carrier 获取 shipment tracking number。
2. 使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) endpoint 通过 delivery_option_id 获取 TikTok Shop 支持的 shipping service provider ID（卖家可以在 Get Order Detail API / Get Order List API 中获取 delivery_option_id）。
3. 使用 [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/6503c95456e2bb0289ee4e81?external_id=6503c95456e2bb0289ee4e81) endpoint 上传 shipment tracking number 和 shipping provider ID。

**东南亚和拉丁美洲市场流程：**

1. 卖家发货并从 shipping carrier 获取 shipment tracking number。
2. 使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) endpoint 通过 delivery_option_id 获取 TikTok Shop 支持的 shipping service provider ID（卖家可以在 Get Order Detail API / Get Order List API 中获取 delivery_option_id）。
3. 使用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) endpoint 上传 shipment tracking number 和 shipping provider ID。

**注意：**
在调用 [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/6503c95456e2bb0289ee4e81?external_id=6503c95456e2bb0289ee4e81)/[Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 发货之前，请确保订单未被取消或有待响应的取消请求。

1. 在冷静期（订单支付后 1 小时内），买家可以无需卖家批准即可取消订单。
2. 冷静期过后，买家可以请求取消订单，需等待卖家批准。

为确保买家的购物体验和服务质量，TikTok 通过基于 tracking number 的 shipment tracking 信息来衡量 shipping 服务水平。当 TikTok 无法验证 tracking number，或包裹处理时间超过 TikTok 的服务水平协议时，TikTok 可能会取消订单并退款给买家。为防止订单被 TikTok 取消，请验证 shipping provider 是否受到 TikTok 支持。
## 拆单 fulfillment

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3f8d829ae6814f53ab0580a551a5fe80~tplv-k9wyc2ijk0-image.image)

## 合单 fulfillment
### 发货前合包（东南亚和拉丁美洲）

1. 调用 [Search Combinable Packages](https://partner.tiktokshop.com/docv2/page/650aa481bace3e02b75d9e32?external_id=650aa481bace3e02b75d9e32) API 获取可以合单的订单。
2. 调用 [Combine Package](https://partner.tiktokshop.com/docv2/page/650aa99adefece02be6f07c9?external_id=650aa99adefece02be6f07c9) API 确认合单。
3. （可选）：如果您想移除已经合单的订单，请使用 [Uncombine Packages](https://partner.tiktokshop.com/docv2/page/650aa960f1fd3102b92ceb0e?external_id=650aa960f1fd3102b92ceb0e) API 移除特定订单。
4. 调用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 发货。

### 发货中合包

1. 卖家合并订单，并使用其现有的 shipping 流程发货。
2. 对于 4PL 订单（美国、英国和日本）：调用 Create Packages API 在发货时进行合包。
3. 对于 3PL 订单（美国、EMEA 和日本）：调用 [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/6503c95456e2bb0289ee4e81?external_id=6503c95456e2bb0289ee4e81) API 上传每个已合包订单的 tracking number。

# TikTok Shop 市场政策
## 拆单 fulfillment 政策

对于东南亚市场，订单不能在订单行级别（也称为 SKU 级别）以下进行拆分。例如，如果买家购买了两条牛仔裤和一件衬衫，两条牛仔裤必须装在同一个 package 中，而衬衫可以拆分到单独的 package 中。

对于美国、EMEA、拉丁美洲和日本，没有限制。订单中的所有商品可以任意拆分到不同的 package 中。
## 合单 fulfillment 政策


1. 使用相同 tracking number 发货的所有订单必须具有相同的收件人姓名和 shipping 地址。
2. 一个 tracking number 最多可用于合包发货的 20 个订单。


## Tracking number 验证政策
如果卖家使用卖家 shipping 模式，TikTok 将验证 tracking number。

1. 商家使用的 shipping service provider 必须受到 TikTok 支持。请使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) API 获取可用的 shipping provider。
2. TikTok 将验证 tracking number 是否与所选的 shipping service provider 匹配。如果 tracking number 未被所选 shipping provider 验证通过，将返回错误。

# 常见问题

1. 我可以使用平台列表之外的 shipping service provider 吗？
   * 不可以。这将导致 TikTok 无法获取 shipment tracking 信息。如果 TikTok 在 cancel_sla_time 指定的时间内无法获取 shipment tracking 信息，订单可能会被 TikTok 取消。
2. 对于标记为 'FULFILL_BY_TIKTOK' 的订单，我需要处理 shipping 操作吗？
   * 不需要。TikTok 将负责履行该订单。
3. 我可以随时从 TikTok 获取 shipping label 吗？
   * 不可以。只有在为 package 安排了 shipping 之后、且在 package 交给 carrier 之前，shipping label 才可用。
4. 如果我已经将 package 交给了 shipping service provider，但平台上的订单状态尚未更新为 'IN_TRANSIT'，我该怎么办？
   * 首先，您需要确认您使用的 shipping service provider 是否受到平台支持。如果确认受支持，请联系 shipping service provider 确保 package 已被扫描录入其系统。如果您已在官方物流网站上追踪到 tracking 信息，但平台仍未显示任何 tracking 详情，请联系 TikTok 寻求帮助。


