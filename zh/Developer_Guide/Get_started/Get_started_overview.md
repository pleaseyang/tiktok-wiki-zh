# 入门概述

本页面介绍 **TikTok Shop 开发者类型**，并指引你了解入门路径的其余部分。在下方确定你的开发者类型后，继续前往开发者入门、授权，最后完成首次 API 调用。
## 三种开发者类型
| 开发者类型 | 构建内容 | 是否存储卖家 OAuth 凭据？ | 数据访问 | 典型场景 |
| --- | --- | --- | --- | --- |
| **电商平台插件 / 连接器开发者** | Public 应用 | 通常不存储 | 有限的、特定场景的数据 | 为 Shopify、WooCommerce、Magento 添加 TikTok Shop 支持的插件 |
| **电商系统集成商 / SaaS 开发者** | Public 应用 | 是（可信存储 bearer 和 refresh token） | 直接访问已授权卖家的数据 | 为众多卖家管理广告、促销、营销和运营的 SaaS |
| **TikTok Shop 卖家开发者** | Custom 应用 | 仅存储自有凭据 | 仅限自有店铺数据 | 卖家为自己的店铺构建集成 |
## 电商平台开发者
为 Shopify、WooCommerce 或 Adobe Magento 等热门电商平台创建插件的开发者。这些插件扩展平台以支持 TikTok Shop 等特定市场。此类型通常**不需要**存储卖家 OAuth 凭据或数据。
## 电商系统集成商
构建系统以代表卖家和商户客户管理广告、产品推广、营销和其他业务功能的开发者。有些是带有用户界面的 SaaS 产品；有些则直接管理运营。此类型通常需要**直接访问**卖家数据，并被信任存储和生成 OAuth 凭据（如 bearer token 和 refresh token）。
## TikTok Shop 卖家开发者
拥有活跃店铺并希望为自己的店铺需求构建集成的 TikTok Shop 卖家。此类型仅可访问**自有**的 OAuth 凭据和数据。
## 开发者类型如何映射到 `user_type`
当用户授权你的应用时，token 响应包含 `user_type` 字段。平台/集成商开发者代表 **卖家**（`user_type=0`）操作；为 affiliate 达人构建的应用接收 **达人**（`user_type=1`）；affiliate 合作伙伴（TAP）应用接收 **合作伙伴**（`user_type=3`）。完整枚举请参阅授权概述。
> **不熟悉 OAuth 术语？** *OAuth 凭据*是你的应用代表用户操作所需的凭证。*Bearer token（access token）* 授权每次 API 调用；*refresh token* 允许你在无需重新授权的情况下获取新的 access token。完整流程请参阅授权概述。

## 后续步骤
你的完整入门路径：

1. [开发者入门](https://partner.tiktokshop.com/docv2/page/developer-onboarding) — 创建账户并注册为开发者。
2. [授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407) — 了解应用如何获取用户数据访问权限。
3. [首次 API 调用概述](https://partner.tiktokshop.com/docv2/page/make-your-first-api-call-overview) — 签名并发送你的第一个请求。


