# Fulfillment API 概述

# 背景
Fulfillment API 允许卖家履行 TikTok Shop 订单。
TikTok Shop 提供两种履约类型：

1. TikTok 履约（FULFILLMENT_BY_TIKTOK）：TikTok 将自动代表卖家处理订单。卖家无需管理履约流程。
2. 卖家履约（FULFILLMENT_BY_SELLER）：在此履约类型下，有两种配送类型：

a) TikTok 配送（TIKTOK）：有时也称为"平台配送"或"通过平台发货"。使用此配送类型时，卖家通过 TikTok Shop 购买面单，并安排 TikTok Shop 物流商上门取件，或将包裹送到 TikTok Shop 物流商的投递点。卖家可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0) 或 [Get Order List](https://partner.tiktokshop.com/docv2/page/650aa8094a0bb702c06df242) 获取配送类型。
b) 卖家配送（SELLER）：有时也称为"通过卖家发货"。卖家通过自有渠道管理配送。使用此配送类型时，卖家调用 Fulfillment API 将配送详情回传给 TikTok Shop。卖家可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0) 或 [Get Order List](https://partner.tiktokshop.com/docv2/page/650aa8094a0bb702c06df242) 获取配送类型。
Fulfillment API 还提供拆包发货和合包发货（有时也称为合并包裹）选项，以支持更灵活的配送需求。卖家可以从 [Get Order Detail](https://partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0) 或 [Get Order List](https://partner.tiktokshop.com/docv2/page/650aa8094a0bb702c06df242) 获取履约类型。
# API 概述
## TikTok 配送
使用平台配送时，根据具体市场，卖家可以通过从 TikTok 购买面单或安排与 TikTok 物流商的包裹交接来发货。
### 购买面单（美国、英国、EMEA 和日本）

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/ee9e1ae6578e47028d0c0606aaff3883~tplv-k9wyc2ijk0-image.image)


### 预约发货（东南亚和拉美）

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5a146a17252244d89f7343fb26b44e8d~tplv-k9wyc2ijk0-image.image)


**从 TikTok 购买面单（美国、英国、EMEA 和日本）**
卖家可以根据包裹的尺寸和重量从 TikTok 购买面单。

1. 使用 [Get Eligible Shipping Service](https://partner.tiktokshop.com/docv2/page/650aa6b2bace3e02b75dda4e?external_id=650aa6b2bace3e02b75dda4e) API 获取可用的物流服务（美国和日本）；
2. 使用 [Create Package](https://partner.tiktokshop.com/docv2/page/650aa132bace3e02b75d40d8?external_id=650aa132bace3e02b75d40d8) API 购买物流服务并创建面单。
3. 使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取面单。

**注意：**
在调用 [Create Package](https://partner.tiktokshop.com/docv2/page/650aa132bace3e02b75d40d8?external_id=650aa132bace3e02b75d40d8#Back%20To%20Top) API 之前，请确保订单未被取消且没有待卖家审批的取消请求。

1. 在冷静期（订单支付后 1 小时内），买家可以无需卖家批准取消订单。
2. 冷静期过后，买家可以请求取消订单，需等待卖家批准。

请确保在调用 [Create Package](https://partner.tiktokshop.com/docv2/page/650aa132bace3e02b75d40d8?external_id=650aa132bace3e02b75d40d8#Back%20To%20Top) API 成功完成面单购买后，再使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取面单。
英国市场在包裹尺寸不可用时也可以使用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1?external_id=650aa4f1defece02be6e7cb1) API。

**从 TikTok 预约发货（东南亚、拉美）**
卖家可以与物流服务商预约包裹交接时间和方式。

1. 使用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1?external_id=650aa4f1defece02be6e7cb1) API 预约包裹交接时间和方式。
2. 使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取面单。

**注意：**
在调用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 发货之前，请确保订单未被取消或有待处理的取消请求。

1. 在冷静期（订单支付后 1 小时内），买家可以无需卖家批准取消订单。
2. 冷静期过后，买家可以请求取消订单，需等待卖家批准。
3. **巴西**市场特有，卖家必须在发货前上传发票文件。请使用 [POST Upload Invoice](https://partner.tiktokshop.com/docv2/page/67b542559a140004b343984f?external_id=67b542559a140004b343984f#Back%20To%20Top) endpoint。通过 webhook [invoice status change] 获取发票上传成功信息后，即可发货。

请确保在调用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 成功预约发货后，再使用 [Get Package Shipping Document](https://partner.tiktokshop.com/docv2/page/650aa5fac16ffe02b8f112ca?external_id=650aa5fac16ffe02b8f112ca) API 获取面单。

## 卖家配送
使用卖家配送时，卖家直接与物流商安排配送，并上传配送跟踪号通知 TikTok 包裹已发出。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4a56b2fa1505407488165cc0a6e74301~tplv-k9wyc2ijk0-image.image)



**美国和 EMEA 市场流程：**

1. 卖家发货并从物流商处获取跟踪号。
2. 使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) endpoint 通过 delivery_option_id 获取 TikTok Shop 支持的物流服务商 ID（卖家可以从 Get Order Detail API / Get Order List API 获取 delivery_option_id）。
3. 使用 [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/6503c95456e2bb0289ee4e81?external_id=6503c95456e2bb0289ee4e81) endpoint 上传跟踪号和物流服务商 ID。

**东南亚和拉美市场流程：**

1. 卖家发货并从物流商处获取跟踪号。
2. 使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) endpoint 通过 delivery_option_id 获取 TikTok Shop 支持的物流服务商 ID（卖家可以从 Get Order Detail API / Get Order List API 获取 delivery_option_id）。
3. 使用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) endpoint 上传跟踪号和物流服务商 ID。

**注意：**
在调用 [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/6503c95456e2bb0289ee4e81?external_id=6503c95456e2bb0289ee4e81)/[Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 发货之前，请确保订单未被取消或有待处理的取消请求。

1. 在冷静期（订单支付后 1 小时内），买家可以无需卖家批准取消订单。
2. 冷静期过后，买家可以请求取消订单，需等待卖家批准。

为保障买家的购物和服务体验，TikTok 基于跟踪号衡量配送服务水平。当 TikTok 无法验证跟踪号或发货处理时间超过 TikTok 的服务水平协议时，TikTok 可能会取消订单并为买家退款。为防止订单被 TikTok 取消，请验证物流服务商是否受 TikTok 支持。
## 拆包履约

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3f8d829ae6814f53ab0580a551a5fe80~tplv-k9wyc2ijk0-image.image)

## 合包履约
### 发货前合包（东南亚和拉美）

1. 调用 [Search Combinable Packages](https://partner.tiktokshop.com/docv2/page/650aa481bace3e02b75d9e32?external_id=650aa481bace3e02b75d9e32) API 获取可合包的订单。
2. 调用 [Combine Package](https://partner.tiktokshop.com/docv2/page/650aa99adefece02be6f07c9?external_id=650aa99adefece02be6f07c9) API 确认合包。
3. （可选）：如果你想移除已合包的订单，请使用 [Uncombine Packages](https://partner.tiktokshop.com/docv2/page/650aa960f1fd3102b92ceb0e?external_id=650aa960f1fd3102b92ceb0e) API 移除特定订单。
4. 调用 [Ship Package](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) API 发货。

### 配送中合包

1. 卖家合并订单，并使用现有配送流程发货。
2. 对于 4PL 订单（美国、英国和日本）：调用 Create Packages API 在发货时合并。
3. 对于 3PL 订单（美国、EMEA 和日本）：调用 [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/6503c95456e2bb0289ee4e81?external_id=6503c95456e2bb0289ee4e81) API 为每个已合并的订单上传跟踪号。

# TikTok Shop 市场政策
## 拆包履约政策

对于东南亚市场，订单不能拆分为低于订单行级别（也称为 SKU 级别）。例如，如果买家购买了两条牛仔裤和一件衬衫，两条牛仔裤必须在同一个包裹中发货，而衬衫可以拆分为单独的包裹。

对于美国、EMEA、拉美和日本市场，没有限制。订单中的所有商品可以任意拆分为不同的包裹。
## 合包履约政策


1. 使用相同跟踪号发货的所有订单必须具有相同的收件人姓名和配送地址。
2. 单个跟踪号最多可用于合包发货 20 个订单。


## 跟踪号验证政策
如果卖家使用卖家配送模式，TikTok 将验证跟踪号。

1. 卖家使用的物流服务商必须受 TikTok 支持。请使用 [Get Shipping Providers](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd) API 获取可用的物流服务商。
2. TikTok 将验证跟踪号是否与所选物流服务商匹配。如果跟踪号未被所选物流服务商验证，将返回错误。

# 常见问题

1. 我可以使用平台列表之外的物流服务商吗？
   * 不可以。这将导致 TikTok 无法获取配送跟踪信息。如果 TikTok 在 cancel_sla_time 指定的时间内无法获取配送跟踪信息，订单可能会被 TikTok 取消。
2. 对于"FULFILL_BY_TIKTOK"的订单，我需要处理发货操作吗？
   * 不需要。TikTok 将负责履行订单。
3. 我可以随时从 TikTok 获取面单吗？
   * 不可以。面单仅在包裹安排好发货后、包裹交给物流商之前可用。
4. 如果我已经将包裹交给物流服务商，但平台上的订单状态尚未更新为"IN_TRANSIT"，该怎么办？
   * 首先，你需要确认你使用的物流服务商受平台支持。如果确认受支持，请联系物流服务商确保包裹已被扫描录入其系统。如果你已在物流官方网站上跟踪到跟踪信息但平台仍未显示任何跟踪详情，请联系 TikTok 寻求帮助。


