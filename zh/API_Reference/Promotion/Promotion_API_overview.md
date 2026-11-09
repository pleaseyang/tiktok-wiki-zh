# Promotion API 概述

TikTok Shop 为您提供多种促销活动，您可以利用这些活动为 TikTok 用户打造丰富的购物体验。
您可以使用 Promotion API 在 TikTok Shop 上创建和管理三种促销活动：

* Product Discount（商品折扣）
* Flash Deal（限时特卖）
* Coupon（美国地区）/ Voucher（其他地区）（您无法使用 OpenAPI 创建 coupon 活动。）

> 注意事项：

> * 以上三种活动均为卖家促销活动，由 TikTok Shop 上的卖家 100% 出资。
> * 当一个商品同时参与 flash deal 活动和 product discount 活动时，仅 flash deal 价格生效。
> * 当一个商品同时参与 flash deal 和 TikTok 活动时，活动价格始终生效。
> * 无论商品是否参与其他促销活动或 TikTok 活动，coupon 始终适用。

### Product Discount（商品折扣）
您可以使用 Product Discount 活动为特定商品创建折扣。折扣后的价格会与原价格一起展示，原价格以删除线标示。示例如下：
<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/40b6766f105c4916a78027cd85465bbe~tplv-k9wyc2ijk0-image.image" width="200px" /></div>


您可以将此活动应用于商品详情页、直播和橱窗。视觉效果在这些场景中基本相同。
有两种折扣类型：

* Fixed Price（固定价格）：指定折扣后的最终价格。
* Percentage Off（百分比折扣）：指定扣除金额占原价格的比例。


### Flash Deal（限时特卖）
您可以使用 Flash Deal 活动为特定商品创建折扣。参与 flash deal 的商品将以限时倒计时的方式突出展示。示例如下：
<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/ed42ed826f6d41b6bf858aa24f0f5c57~tplv-k9wyc2ijk0-image.image" width="300px" /></div>

每个商品的 deal 价格需要等于或低于过去 30 天内客户支付的价格。
### Coupon / 卖家 Voucher（优惠券/卖家优惠券）
您可以在美国使用 coupon 活动，在其他地区使用卖家 voucher 活动，并与其他促销活动组合使用。您可以在 Seller Center 中进行设置，coupon 的视觉效果取决于您的设置。
您无法使用 OpenAPI 进行设置，但可以搜索和获取现有 coupon 活动的详细信息。

## API 列表
您可以在 Seller Center 和卖家 App 中创建和管理促销活动；也可以通过 Promotion API 来完成。以下是 Promotion API 列表：

* 管理 product discount 或 flash deal 活动，请参考：
   * [创建活动](650c33c155bc3202b762b507)；
   * [搜索活动](650acfbaf1fd3102b9315a3a)；
   * [获取活动](650acd920fcef602bf36ee2b)；
   * [更新活动](650c584d82c3a602befa4ab8)；
   * [停用活动](650acf9adefece02be7380cf)。
* 更新 product discount 或 flash deal 活动中包含的商品，请参考：
   * [更新活动商品](650d32c42aaa3602b86ccb5c)；
   * [移除活动商品](650acfd84a0bb702c072b4eb)。
* 搜索和获取 coupon 活动的详细信息，请参考：
   * [搜索优惠券](6699dcdf115ebe02f841e4cd)；
   * [获取优惠券](6699dce0de15e502ed219e37)。
