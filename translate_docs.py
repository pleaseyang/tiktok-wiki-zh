#!/usr/bin/env python3
"""Translate TikTok Shop API documentation from English to Chinese."""

import os
import re
import json

# ============================================================
# Translation dictionaries
# ============================================================

# Exact header translations (line-level, stripped)
HEADER_MAP = {
    "# Products API overview": "# Products API 概览",
    "# Context": "# 背景",
    "# Important Concepts": "# 重要概念",
    "# TikTok Shop Marketplace Policies": "# TikTok Shop 市场政策",
    "# Frequently Asked Questions": "# 常见问题",
    "# Listing quality diagnosis": "# 上架质量诊断",
    "# Product pricing": "# 产品定价",
    "# Common mistakes": "# 常见错误",
    "# Sales Attributes": "# 销售属性",
    "# Function Description": "# 功能描述",
    "# Common Parameters": "# 通用参数",
    "# Request Query Parameters": "# 请求查询参数",
    "# Request Body Parameters": "# 请求体参数",
    "# Request Path Parameters": "# 请求路径参数",
    "# Request Sample": "# 请求示例",
    "# Response Parameters": "# 响应参数",
    "# Response Sample": "# 响应示例",
    "# Error Code": "# 错误码",
    "# Diagnosis results and recommendations": "# 诊断结果和建议",
    "# United States": "# 美国",
    "# Rest of World": "# 世界其他地区",
    "# Currency precision": "# 货币精度",
    "# Local sellers": "# 本地卖家",
    "# Intra-EU sellers": "# 欧盟内部卖家",
    "# Global sellers": "# 全球卖家",
    "# Sellers with local warehouses": "# 拥有本地仓库的卖家",
    "# Sellers with cross-border warehouses": "# 拥有跨境仓库的卖家",
    "# Notes": "# 注意事项",
    "# Duplicated sales attributes in 1 SKU": "# 单个 SKU 中的重复销售属性",
    "# Duplicated sales attribute values across SKUs": "# 跨 SKU 的重复销售属性值",
    "# Sales attribute count mismatch across SKUs": "# 跨 SKU 的销售属性数量不匹配",
    "# Incorrect usage": "# 错误用法",
    "# Correct usage": "# 正确用法",
    "# Incorrect usage - 1 attribute": "# 错误用法 - 1 个属性",
    "# Correct usage - 1 attribute": "# 正确用法 - 1 个属性",
    "# Incorrect usage - Multiple attributes": "# 错误用法 - 多个属性",
    "# Correct usage - Multiple attributes": "# 正确用法 - 多个属性",
    "# Check Listing Prerequisites": "# 检查上架前提条件",
    "# Get Categories": "# 获取分类",
    "# Recommend Category": "# 推荐分类",
    "# Get Category Rules": "# 获取分类规则",
    "# Get Category Attributes": "# 获取分类属性",
    "# Create Custom Brands": "# 创建自定义品牌",
    "# Get Brands": "# 获取品牌",
    "# Check Product Listing": "# 检查产品上架",
    "# Upload Product Image": "# 上传产品图片",
    "# Upload Product File": "# 上传产品文件",
    "# Search Size Charts": "# 搜索尺码表",
    "# Activate Products": "# 激活产品",
    "# Create Product": "# 创建产品",
    "# Deactivate Products": "# 下架产品",
    "# Delete Products": "# 删除产品",
    "# Recover Products": "# 恢复产品",
    "# Get Product": "# 获取产品",
    "# Search Products": "# 搜索产品",
    "# Update Price": "# 更新价格",
    "# Update Inventory": "# 更新库存",
    "# Inventory Search": "# 库存搜索",
    "# Diagnose and Optimize Product": "# 诊断和优化产品",
    "# Get Product Diagnoses": "# 获取产品诊断结果",
    "# Get Products SEO Words": "# 获取产品 SEO 关键词",
    "# Get Recommended Product Title And Description": "# 获取推荐产品标题和描述",
    "# Optimize Images": "# 优化图片",
    "# Create Image Translation Tasks": "# 创建图片翻译任务",
    "# Get Image Translation Tasks": "# 获取图片翻译任务",
    "# Get Global Listing Rules": "# 获取全球上架规则",
    "# Replicate Product": "# 复制产品",
    "# Get Global Replicated Products": "# 获取全球复制产品",
    "# Edit Product": "# 编辑产品",
    "# Partial Edit Product": "# 部分编辑产品",
    "# Partial Edit Global Product": "# 部分编辑全球产品",
    "# Search Products for Compliance Auditing": "# 搜索合规审核产品",
    "# Get Product Package Recommendations": "# 获取产品包装建议",
    "# Get Opportunity Detail": "# 获取商机详情",
    "# List Opportunities": "# 列出商机",
    "# Get Submission Records": "# 获取提交记录",
    "# Submit Product via Opportunity": "# 通过商机提交产品",
    "# Create GPA Upgrade Task": "# 创建 GPA 升级任务",
    "# Submit Size Chart Appeal": "# 提交尺码表申诉",
    "# List Product SKPP Statuses": "# 列出产品 SKPP 状态",
    "# Get Product SKPP Detail": "# 获取产品 SKPP 详情",
    "# Get Shop SKPP Summary": "# 获取店铺 SKPP 摘要",
    "# Update Stock Operation Settings": "# 更新库存操作设置",
    "# Suggest Brands": "# 建议品牌",
    "# Create Category Upgrade Task": "# 创建分类升级任务",
    "# Get Global Categories": "# 获取全球分类",
    "# Recommend Global Categories": "# 推荐全球分类",
    "# Get Global Attributes": "# 获取全球属性",
    "# Create Global Product": "# 创建全球产品",
    "# Publish Global Product": "# 发布全球产品",
    "# Edit Global Product": "# 编辑全球产品",
    "# Delete Global Products": "# 删除全球产品",
    "# Get Global Product": "# 获取全球产品",
    "# Search Global Products": "# 搜索全球产品",
    "# Update Global Inventory": "# 更新全球库存",
    "# Get Global Category Rules": "# 获取全球分类规则",
    "# Create Manufacturer": "# 创建制造商",
    "# Partial Edit Manufacturer": "# 部分编辑制造商",
    "# Search Manufacturers": "# 搜索制造商",
    "# Create Responsible Person": "# 创建负责人",
    "# Partial Edit Responsible Person": "# 部分编辑负责人",
    "# Search Responsible Persons": "# 搜索负责人",
}

# Sub-header translations (## level)
SUBHEADER_MAP = {
    "Duplicated sales attributes in 1 SKU": "单个 SKU 中的重复销售属性",
    "Duplicated sales attribute values across SKUs": "跨 SKU 的重复销售属性值",
    "Sales attribute count mismatch across SKUs": "跨 SKU 的销售属性数量不匹配",
    "Incorrect usage": "错误用法",
    "Correct usage": "正确用法",
    "Incorrect usage - 1 attribute": "错误用法 - 1 个属性",
    "Correct usage - 1 attribute": "正确用法 - 1 个属性",
    "Incorrect usage - Multiple attributes": "错误用法 - 多个属性",
    "Correct usage - Multiple attributes": "正确用法 - 多个属性",
    "Currency precision": "货币精度",
    "Local sellers": "本地卖家",
    "Intra-EU sellers": "欧盟内部卖家",
    "Global sellers": "全球卖家",
    "Sellers with local warehouses": "拥有本地仓库的卖家",
    "Sellers with cross-border warehouses": "拥有跨境仓库的卖家",
    "Notes": "注意事项",
}

# Full paragraph translations (exact match on stripped line)
PARA_MAP = {
    "The Product API helps sellers manage their product catalog at scale. Using the Product API, a seller can create, edit, delete products, and retrieve product details, as well as sync them into Tiktok Shop from an external DTC/OMS/ERP system (such as Shopify) for sales on TikTok Shop.":
        "Product API 帮助卖家大规模管理产品目录。使用 Product API，卖家可以创建、编辑、删除产品，检索产品详情，以及将它们从外部 DTC/OMS/ERP 系统（如 Shopify）同步到 TikTok Shop 进行销售。",
    "A product can be created either as a live product or a draft via Create Product API.":
        "产品可以通过 Create Product API 创建为上架产品或草稿。",
    "The steps to create a product varies based on the location of the shop.":
        "创建产品的步骤因店铺所在地区而异。",
    "**For EU countries**": "**对于欧盟国家**",
    "**For other regions**": "**对于其他地区**",
    "Products may be deactivated or frozen by TikTok for various policy violations. You can obtain the real-time review result of the product via the Product webhook.":
        "产品可能因各种政策违规被 TikTok 下架或冻结。您可以通过 Product webhook 获取产品的实时审核结果。",
    "Product details can be retrieved via the Get Product List API and the Get Product Detail API. Product details include product basic information and sales terms. Basic information includes item titles, description, inventory, images, etc. Sales terms include price and inventory, etc.":
        "产品详情可以通过 Get Product List API 和 Get Product Detail API 获取。产品详情包括产品基本信息和销售条款。基本信息包括商品标题、描述、库存、图片等。销售条款包括价格和库存等。",
    "A product will be reviewed by TikTok after the product is created or edited. If a live product fails the review after being edited, the live version remains the snapshot of the product before the editing. To retrieve the after-editing version being reviewed, specify True for the need_audit_version parameter field when calling the Get Product Detail API.":
        "产品在创建或编辑后将由 TikTok 审核。如果上架产品在编辑后未通过审核，上架版本将保持编辑前的产品快照。要获取正在审核的编辑后版本，在调用 Get Product Detail API 时将 need_audit_version 参数字段指定为 True。",
    "**Product:** A product is an item that a seller lists on TikTok for sale.  A product is identified by its unique product ID.":
        "**产品：**产品是卖家在 TikTok 上架销售的商品。产品由其唯一的产品 ID 标识。",
    "**Category:** Products on TikTok are grouped into categories predefined by TikTok.  All products must belong to a category.  Categories are organized in a tree structure.  You can retrieve all available categories via Get Category API.":
        "**分类：**TikTok 上的产品被分组到 TikTok 预定义的分类中。所有产品必须属于一个分类。分类以树形结构组织。您可以通过 Get Category API 获取所有可用的分类。",
    "**Attribute**: Attributes are supplementary content of product information. Attributes are associated with categories.  For a particular category, some attributes are required while others are optional. Attributes can be further divided into product attributes and sales attributes.":
        "**属性**：属性是产品信息的补充内容。属性与分类关联。对于特定分类，某些属性是必填的，而其他属性是可选的。属性可以进一步分为产品属性和销售属性。",
    "* **Product attributes** are general attributes such as manufacturer, country of origin, materials used)":
        "* **产品属性**是一般属性，如制造商、原产国、使用材料等）",
    "* **Sales attributes** are attributes that are specific to the variant (aka SKU) of a product such as size, color, length.":
        "* **销售属性**是特定于产品变体（即 SKU）的属性，如尺寸、颜色、长度。",
    "* **Custom attributes** are attributes that a seller can optionally create to supplement the product information. For example, weight is generally a generic product attribute, which is primarily used for shipping calculations. However, if your product is an extremely lightweight product for example performance outdoor clothing, you can list the weight as a custom attribute.":
        "* **自定义属性**是卖家可以选择创建的属性，用于补充产品信息。例如，重量通常是一个通用产品属性，主要用于运费计算。但是，如果您的产品是超轻产品（例如高性能户外服装），您可以将重量列为自定义属性。",
    "**Product Status**: A product has the following statuses:":
        "**产品状态**：产品具有以下状态：",
    "**Brand authorization**: TikTok requires the seller of a product to provide brand authorization for certain brands either as the direct manufacturer or an authorized reseller.  Branded products without valid brand authorization cannot be listed on TikTok for sale.  To verify whether the seller has authorization for a particular brand, use the Get Brand API.":
        "**品牌授权**：TikTok 要求产品卖家为某些品牌提供品牌授权，无论是作为直接制造商还是授权经销商。没有有效品牌授权的品牌产品不能在 TikTok 上架销售。要验证卖家是否拥有特定品牌的授权，请使用 Get Brand API。",
    "**Product certification**: For certain categories, product certification is required to prove the authenticity of the product. These certifications are meant to comply with local laws. Some examples include ingredients in beauty or consumable products.":
        "**产品认证**：对于某些分类，需要产品认证来证明产品的真实性。这些认证旨在符合当地法律。例如，包括美容或消耗品中的成分。",
    "**Product upload limit**: To assist new sellers with order fulfillment, **all** **new shops (both individual and corporate)** on TikTok Shop are subject to a **probation period** that limits the number of daily orders sellers can accept and the number of product uploads sellers can list per day.":
        "**产品上传限制**：为帮助新卖家处理订单履约，TikTok Shop 上的**所有****新店铺（包括个人和企业）**都需要经过**试用期**，限制卖家每天可以接受的订单数量和每天可以上架的产品上传数量。",
    "* New individual sellers are limited to 100 orders per day.": "* 新个人卖家每天限制 100 个订单。",
    "* New corporate sellers are limited to 200 orders per day.": "* 新企业卖家每天限制 200 个订单。",
    "* All new sellers are limited to 100 product uploads per day.": "* 所有新卖家每天限制 100 个产品上传。",
    "Once sellers graduate from probation, sellers are not subject to order limits but are limited to 1,000 product uploads per day.":
        "卖家通过试用期后，不再受订单限制，但每天限制 1,000 个产品上传。",
    "High-quality product listings are essential for improving visibility and building customer trust.":
        "高质量的产品上架对于提高可见性和建立客户信任至关重要。",
    "TikTok Shop provides APIs that diagnose product content and offer recommendations for optimization, covering areas such as text, image, and search engine optimization (SEO).":
        "TikTok Shop 提供诊断产品内容并提供优化建议的 API，涵盖文本、图片和搜索引擎优化（SEO）等领域。",
    "**For unlisted new products**": "**对于未上架的新产品**",
    "**For existing products**": "**对于现有产品**",
    "Prices on TikTok Shop are set at the SKU level. The allowable price range varies based on the destination market and the seller operation mode.":
        "TikTok Shop 上的价格在 SKU 级别设置。允许的价格范围因目标市场和卖家运营模式而异。",
    "Some markets also require specific currency precision. For Indonesia, Japan, and Vietnam, prices must be integers because these currencies do not support decimal places.":
        "某些市场还要求特定的货币精度。对于印度尼西亚、日本和越南，价格必须是整数，因为这些货币不支持小数位。",
    "When integrating with TikTok Shop Products APIs, it's essential to understand the correct structure and usage of each parameter to ensure smooth API interactions. In this article, we highlight common mistakes developers make when calling the APIs, particularly for complex parameters, and provide guidance on how to avoid them.":
        "在集成 TikTok Shop Products API 时，了解每个参数的正确结构和用法对于确保顺畅的 API 交互至关重要。在本文中，我们重点介绍了开发者在调用 API 时常犯的错误，特别是对于复杂参数，并提供了如何避免这些错误的指导。",
    "First, it's important to understand what sales attributes are and their relationship to SKUs.":
        "首先，了解什么是销售属性及其与 SKU 的关系很重要。",
    '**Sales attributes** are variations specific to an SKU, such as size, color, and material, while an **SKU** represents a **unique** combination of these attributes, creating distinct versions of a product. For example, a sweater with color "Red" and material "Cotton" would be one SKU, while a sweater with color "Blue" and material "Wool" would be a different SKU.':
        '**销售属性**是特定于 SKU 的变体，如尺寸、颜色和材料，而 **SKU** 代表这些属性的**唯一**组合，创建产品的不同版本。例如，颜色为"红色"、材料为"棉"的毛衣是一个 SKU，而颜色为"蓝色"、材料为"羊毛"的毛衣是另一个 SKU。',
    "This section focuses on how to avoid common mistakes when defining sales attributes during product listing through practical examples.":
        "本节重点介绍如何通过实际示例避免在上架产品时定义销售属性的常见错误。",
    'Each SKU can only **define each sales attribute ID/name once**. In practical terms, this means an SKU can\'t have two different colors at the same time.':
        '每个 SKU 只能**定义每个销售属性 ID/名称一次**。实际上，这意味着一个 SKU 不能同时拥有两种不同的颜色。',
    "Each SKU must represent a **unique combination of sales attribute value ID/names.** In practical terms, this means you can't have two SKUs with the same combination of attributes and attribute values. For example, you can have two SKUs for red sweaters, but they must differ by another attribute, such as size or material.":
        "每个 SKU 必须代表**销售属性值 ID/名称的唯一组合。**实际上，这意味着不能有两个具有相同属性和属性值组合的 SKU。例如，可以有两个红色毛衣的 SKU，但它们必须在另一个属性上有所不同，如尺寸或材料。",
    "All SKUs must define the **same set of sales attribute ID/names**. In practical terms, this means if one SKU is defined by 2 sales attributes, such as color and material, then every other SKU for the same product must also include both attributes. Alternatively, remove the redundant attribute.":
        "所有 SKU 必须定义**相同的销售属性 ID/名称集合**。实际上，这意味着如果一个 SKU 由 2 个销售属性定义（如颜色和材料），则同一产品的每个其他 SKU 也必须包含这两个属性。或者，删除多余的属性。",
    "Check if a TikTok shop is ready to list products.":
        "检查 TikTok 店铺是否准备好上架产品。",
    "Each shop needs to satisfy a series of TikTok Shop requirements before you can start listing products. Before you proceed to list products, use this API to check if your shop has satisfied all requirements.":
        "每个店铺在开始上架产品之前需要满足一系列 TikTok Shop 要求。在上架产品之前，使用此 API 检查您的店铺是否已满足所有要求。",
    "Retrieve the list of product categories available for your shop.":
        "获取您的店铺可用的产品分类列表。",
    "Product categories are updated frequently, so it's recommended to call the API in real time to ensure you are using the latest category data. Caching category data locally may result in using outdated information, leading to errors when creating products.":
        "产品分类经常更新，因此建议实时调用 API 以确保使用最新的分类数据。在本地缓存分类数据可能导致使用过时的信息，从而在创建产品时导致错误。",
    "Retrieve the recommended category for a candidate product based on its title, description, and images.":
        "根据候选产品的标题、描述和图片获取推荐的分类。",
    "If you are syncing product catalogs from an external system to TikTok Shop, use this API to facilitate product categorization.":
        "如果您正在将产品目录从外部系统同步到 TikTok Shop，请使用此 API 来促进产品分类。",
    "Retrieve the additional requirements (beyond mandatory product attributes) for listing a product in a particular category based on your shop's location. Requirements may include product certifications, size charts, dimensions and more.":
        "根据您店铺的位置，获取在特定分类中上架产品的额外要求（除必填产品属性外）。要求可能包括产品认证、尺码表、尺寸等。",
    "Use this API to determine the supporting information that you must prepare before listing a product.":
        "使用此 API 确定在上架产品之前必须准备的辅助信息。",
    "Retrieve the standard built-in product and sales attributes for listing a product in a particular category based on your shop's location.":
        "根据您店铺的位置，获取在特定分类中上架产品的标准内置产品属性和销售属性。",
    "Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is associated with a standard set of product attributes and sales attributes.":
        "TikTok Shop 上的产品被分组到 TikTok Shop 预定义的分类中，每个分类都关联一组标准的产品属性和销售属性。",
    "Use this API to determine the mandatory and optional attributes before listing a product.":
        "使用此 API 确定在上架产品之前的必填和可选属性。",
    "Create custom brands for your own use across all markets.":
        "创建自定义品牌，供您在所有市场中使用。",
    "Authorization is not required when creating a brand. You can create the brand first and obtain brand authorization later through the Qualification Center in TikTok Shop Seller Center.":
        "创建品牌时不需要授权。您可以先创建品牌，然后稍后通过 TikTok Shop 卖家中心的资质中心获得品牌授权。",
    "Retrieve brands for your shop, including the built-in brands and any custom brands created using the [Create Custom Brands API](650a0926f1fd3102b91bbfb0). Pass the returned brand ID when creating or editing a product to associate the brand with the product.":
        "获取您店铺的品牌，包括内置品牌和使用 [Create Custom Brands API](650a0926f1fd3102b91bbfb0) 创建的任何自定义品牌。在创建或编辑产品时传递返回的品牌 ID，以将品牌与产品关联。",
    "Identify any issues with your product properties in advance to ensure your product is ready for listing.":
        "提前识别产品属性的任何问题，确保您的产品准备好上架。",
    "Every product must meet TikTok Shop requirements before it can be listed. Before listing, you can submit all relevant product information to this API to check whether a listing meets these requirements. You'll receive a list of issues to resolve before listing. This process helps reduce the risk of failure when creating products.":
        "每个产品在上架前必须满足 TikTok Shop 的要求。在上架之前，您可以将所有相关产品信息提交到此 API，以检查上架是否满足这些要求。您将收到一个需要在上架前解决的问题列表。此过程有助于降低创建产品时失败的风险。",
    "Upload a local image to TikTok Shop for use as a product image, variant image, size chart, certification image, or another supported image use case.":
        "将本地图片上传到 TikTok Shop，用作产品图片、变体图片、尺码表、认证图片或支持的其他图片用例。",
    "Upload non-image files, such as PDF or video to TikTok Shop.":
        "将非图片文件（如 PDF 或视频）上传到 TikTok Shop。",
    "Use this API when you need to add videos to your product to improve the shopping experience, or submit certifications or reports to meet TikTok Shop requirements for listing restricted products.":
        "当您需要为产品添加视频以改善购物体验，或提交认证或报告以满足 TikTok Shop 上架受限产品的要求时，使用此 API。",
    "Retrieve size charts that a seller has created.":
        "获取卖家已创建的尺码表。",
    "Activate hidden products that are in the `Seller_deactivated` or `Platform_deactivated` status and display them in the TikTok Shop catalog.":
        "激活处于 `Seller_deactivated` 或 `Platform_deactivated` 状态的隐藏产品，并在 TikTok Shop 目录中展示它们。",
    "After submitting the activation request, the products will be sent to TikTok Shop for auditing and their status will change to `Pending`. If a product passes the audit, its status will change back to `Activate`. You can use the [Product status change webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) to monitor the audit status.":
        "提交激活请求后，产品将被发送到 TikTok Shop 进行审核，其状态将变为 `Pending`。如果产品通过审核，其状态将变回 `Activate`。您可以使用[产品状态变更 webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) 来监控审核状态。",
    "Create and list products intended for sale exclusively in local shops.":
        "创建并上架仅在本地店铺销售的产品。",
    "Create global products to be sold in one or multiple shops outside of the seller's base country.":
        "创建全球产品，在卖家所在国家/地区以外的一个或多个店铺中销售。",
    "Add a manufacturer for a seller. The provided information will be automatically translated into all EU languages supported by TikTok Shop.":
        "为卖家添加制造商。提供的信息将自动翻译成 TikTok Shop 支持的所有欧盟语言。",
    "For common parameters, refer to [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)":
        "通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)",
    "For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)":
        "常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)",
}

# FAQ translations
FAQ_MAP = {
    "**-** **I can't get my product to list. What is going on?**":
        "**-** **我无法上架产品。怎么回事？**",
    "* There are several reasons for this. Please check the following:":
    "* 可能有几个原因。请检查以下事项：",
    "* Your product has all the required attributes.":
        "* 您的产品具有所有必填属性。",
    "* Your product has all the required certifications, based on the category it is assigned.":
        "* 根据您的产品分配的分类，您的产品具有所有必需的认证。",
    "* You have reached your 100 product upload limit per day, as a new Seller. Please try again the next day.":
        "* 作为新卖家，您已达到每天 100 个产品上传的限制。请第二天再试。",
    "**-** **How do I overcome the Product Upload limit?**":
        "**-** **如何突破产品上传限制？**",
    "* New sellers are limited to 100 products per day. If you would like to overcome this limit and graduate from new seller probation, please reach out to your TikTok account manager.":
        "* 新卖家每天限制 100 个产品。如果您想突破此限制并从新卖家试用期中毕业，请联系您的 TikTok 客户经理。",
    "**-** **My product continuously fails TikTok reviews. Help!**":
        "**-** **我的产品持续未通过 TikTok 审核。求助！**",
    "* Check that your images are high quality.":
        "* 检查您的图片是否为高质量。",
    "* Check that your category or product is allowed for sale in the region.":
        "* 检查您的分类或产品是否允许在该地区销售。",
    "* Check that you have filled in all required product attributes.":
        "* 检查您是否已填写所有必填的产品属性。",
    "* If the above is not resolved, please reach out to your TikTok Account Manager.":
        "* 如果以上问题未解决，请联系您的 TikTok 客户经理。",
    "**-** **What is the difference between Deactivate and Delete?**":
        "**-** **下架和删除有什么区别？**",
    "* Deactivate will temporarily remove your product off the shelf. All back-end data, including sales, reports, product description, will persist. You can reactivate this product at any time, when you receive more inventory etc.":
        "* 下架将暂时把您的产品从货架上移除。所有后端数据，包括销售、报告、产品描述，都将保留。您可以在收到更多库存时随时重新激活此产品。",
    "* Deleting a product will remove the product from your catalog forever. This also removes historical sales data, financial settlements...etc. Only do this if you have tied up all your accounting and reporting matters, and are fully committed to removing the product from your catalog forever.":
        "* 删除产品将永久从您的目录中移除该产品。这还会删除历史销售数据、财务结算等。只有在您处理完所有会计和报告事务，并完全致力于永久从目录中移除该产品时，才执行此操作。",
}

# Inline phrase replacements (substring-level)
INLINE_MAP = {
    "The success or failure status code returned in API response.": "API 响应中返回的成功或失败状态码。",
    "The success or failure messages returned in API response. Reasons of failure will be described in the message.": "API 响应中返回的成功或失败消息。失败原因将在消息中描述。",
    "Request log": "请求日志",
    "Specific return information": "具体返回信息",
    "Use this property to pass shop information in requesting the API. Failure in passing the correct value when requesting the API for cross-border shops will return incorrect response.": "使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。",
    "Every single app will have a unique key. Please use the specific key assigned to your app.": "每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。",
    "Signature generated by gen algorithm. When you send API requests to TTS, you must sign them so that TTS can identify the senders.": "由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。",
    "Unix timestamp GMT (UTC+00:00). This timestamp is used across all API requests. Developers can use this convert to local time.": "Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。",
    "Allowed type: application/json": "允许类型：application/json",
    "Allowed type: multipart/form-data": "允许类型：multipart/form-data",
    "The language used in text fields such as descriptions and titles must align with the target market's language (e.g. don't use Chinese).": "描述和标题等文本字段中使用的语言必须与目标市场的语言一致（例如，不要使用中文）。",
    "The language used in the product content must align with the target market's language (e.g. don't use Chinese), otherwise the listing will fail or be rejected.": "产品内容中使用的语言必须与目标市场的语言一致（例如，不要使用中文），否则上架将失败或被拒绝。",
    "The diagnosis is performed on the following product fields:": "对以下产品字段执行诊断：",
    "Refer to the following region-based tables for the diagnosis results/codes returned in the APIs and the actionable recommendations to optimize your listings effectively.": "请参考以下基于地区的表格，了解 API 中返回的诊断结果/代码以及可有效优化上架的可操作建议。",
    'Codes marked as "**Retired**" indicate that they are no longer recommended and will not appear anymore.': '标记为"**已停用**"的代码表示不再推荐使用，将不再出现。',
    "In the US, product listings are evaluated based on a tiered system that includes listing quality tiers such as": "在美国，产品上架基于分层系统评估，包括上架质量等级，如",
    'Each diagnosis code corresponds to a specific recommendation and is assigned a quality tier, such as "FAIR" or "GOOD". Implementing the recommendations can help your listing progress through these tiers to achieve better quality and visibility. For example, a product will reach the "GOOD" tier once all "FAIR" and "GOOD" recommendations are addressed or implemented.': '每个诊断代码对应一个具体建议，并被分配一个质量等级，如"FAIR"或"GOOD"。实施这些建议可以帮助您的上架逐步提升等级，获得更好的质量和可见性。例如，一旦所有"FAIR"和"GOOD"建议都得到解决或实施，产品将达到"GOOD"等级。',
    "For more information about the listing quality tiers and criteria, refer to": "有关上架质量等级和标准的更多信息，请参考",
    "For regions outside the US, product listings are evaluated based on key recommendations. The following table provides the list of diagnosis codes along with actionable recommendations to improve your product listing's overall quality and visibility.": "对于美国以外的地区，产品上架基于关键建议进行评估。以下表格提供了诊断代码列表以及可改善产品上架整体质量和可见性的可操作建议。",
    "The product title (API property:": "产品标题（API 属性：",
    "The product description (API property:": "产品描述（API 属性：",
    "The product attributes (API property:": "产品属性（API 属性：",
    "The size chart image (API property:": "尺码表图片（API 属性：",
    "The product images displayed in the image gallery (API property:": "在图片库中展示的产品图片（API 属性：",
    "The product description in HTML format.": "HTML 格式的产品描述。",
    "The URI of the image. Retrieve the URI from the [Upload Product Image API]": "图片的 URI。从 [Upload Product Image API] 获取 URI",
    "The URI of the image.": "图片的 URI。",
    "The URL to access and view the image.": "访问和查看图片的 URL。",
    "The local image file to be uploaded.": "要上传的本地图片文件。",
    "The local file to be uploaded.": "要上传的本地文件。",
    "The usage scenario of the image.": "图片的使用场景。",
    "The name of the file, including the file extension": "文件名称，包括文件扩展名",
    "The height of the image after aspect ratio adjustment.": "调整宽高比后的图片高度。",
    "The width of the image after aspect ratio adjustment.": "调整宽高比后的图片宽度。",
    "The usage scenario specified during upload.": "上传时指定的使用场景。",
    "Pass this value when creating or editing a product to associate the image with the product.": "在创建或编辑产品时传递此值，以将图片与产品关联。",
    "Pass this value when creating or editing a product to associate the file with the product.": "在创建或编辑产品时传递此值，以将文件与产品关联。",
    "The product IDs to activate.": "要激活的产品 ID。",
    "The errors for individual products that could not be activated. Check this list even when the top-level": "无法激活的单个产品的错误。即使顶级",
    "The main error code.": "主要错误代码。",
    "The main error message.": "主要错误消息。",
    "The details of the main error.": "主要错误的详细信息。",
    "The ID of the product that could not be activated.": "无法激活的产品 ID。",
    "A list of further nested errors or issues related to the main error.": "与主要错误相关的进一步嵌套错误或问题列表。",
    "The secondary error code.": "次要错误代码。",
    "The secondary error message.": "次要错误消息。",
    "The listing platforms where the product will be activated.": "产品将被激活的上架平台。",
    "The number of results to be returned per page.": "每页返回的结果数量。",
    "An opaque token used to retrieve the next page of a paginated result set. Retrieve this value from the result of the": "用于获取分页结果集下一页的不透明 token。从上一次响应的",
    "from a previous response. It is not needed for the first page.": "结果中获取此值。第一页不需要此值。",
    "The total count of brands that meet the query conditions.": "符合查询条件的品牌总数。",
    "An opaque token used to retrieve the next page of a paginated result set. If this value is non-empty, pass it in the": "用于获取分页结果集下一页的不透明 token。如果此值非空，请将其传递给下一个请求的",
    "parameter of the next request. An empty value means there are no more results.": "参数。空值表示没有更多结果。",
    "The list of brands that meet the query conditions.": "符合查询条件的品牌列表。",
    "The list of categories that meet the query conditions.": "符合查询条件的分类列表。",
    "The category ID.": "分类 ID。",
    "The parent category ID.": "父分类 ID。",
    "The category name in the requested locale. If": "请求语言环境中的分类名称。如果",
    "is omitted, the default locale of your shop is used.": "被省略，则使用您店铺的默认语言环境。",
    "A flag to indicate if the category is a leaf category.": "标识该分类是否为叶子分类的标志。",
    "You can only create or edit products that belong to a leaf category.": "您只能创建或编辑属于叶子分类的产品。",
    "The shop's permission statuses for this category.": "该店铺的此分类权限状态。",
    "The shop's permission status for this category.": "该店铺的此分类权限状态。",
    "The category hierarchy for the recommended leaf category, ordered from the top-level category to the leaf category.": "推荐叶子分类的分类层级，从顶级分类到叶子分类排序。",
    "The recommended category ID. This is always a leaf category.": "推荐的分类 ID。这始终是叶子分类。",
    "The category level.": "分类级别。",
    "The category name.": "分类名称。",
    "Filter categories by this keyword in": "使用此关键词过滤分类",
    "Filter categories by the category tree version.": "按分类树版本过滤分类。",
    "Filter categories by the specified platform.": "按指定平台过滤分类。",
    "A flag to indicate whether to include categories that are prohibited on TikTok Shop.": "标识是否包含 TikTok Shop 禁止的分类。",
    "The BCP-47 locale codes for displaying category information.": "用于显示分类信息的 BCP-47 语言环境代码。",
    "The BCP-47 locale codes for displaying the size charts.": "用于显示尺码表的 BCP-47 语言环境代码。",
    "The default locale of your shop.": "您店铺的默认语言环境。",
    "The ID of the brand of this product.": "此产品的品牌 ID。",
    "A list of Stock Keeping Units (SKUs) used to identify distinct variants of the product.": "用于标识产品不同变体的 SKU（库存单位）列表。",
    "A list of attributes (e.g. size, color, length) that define each variant of a product.": "定义产品每个变体的属性列表（如尺寸、颜色、长度）。",
    "The ID of a built-in sales attribute, retrieved from": "内置销售属性的 ID，从",
    "A self-defined custom sales attribute name to validate when the built-in attributes do not satisfy your needs.": "当内置属性不满足需求时，用于验证的自定义销售属性名称。",
    "The ID of a built-in sales attribute value, retrieved from the": "内置销售属性值的 ID，从",
    "A self-defined custom sales attribute value to validate when the built-in values do not satisfy your needs.": "当内置值不满足需求时，用于验证的自定义销售属性值。",
    "No duplicates allowed under the same attribute.": "同一属性下不允许重复。",
    "An internal code/name for managing SKUs, not visible to buyers.": "用于管理 SKU 的内部代码/名称，对买家不可见。",
    "SKU pricing information.": "SKU 定价信息。",
    "SKU inventory information.": "SKU 库存信息。",
    "The ID of the warehouse where the SKU is stored.": "SKU 存放仓库的 ID。",
    "Retrieve the list of warehouses available for your shop from the": "从以下位置获取您的店铺可用仓库列表",
    "The total SKU quantity available in the warehouse.": "仓库中可用的 SKU 总数量。",
    "The product title.": "产品标题。",
    "Title length:": "标题长度：",
    "A flag indicating whether to show the Cash On Delivery (COD) payment option during checkout.": "标识是否在结账时显示货到付款（COD）付款选项的标志。",
    "The list of certifications for your product.": "您的产品的认证列表。",
    "The ID to identify the type of certification required for the product category.": "用于标识产品分类所需认证类型的 ID。",
    "A list of certification related images.": "认证相关图片列表。",
    "A list of certification related files.": "认证相关文件列表。",
    "The ID of the certification file.": "认证文件的 ID。",
    "The name of the certification file, including the file extension.": "认证文件的名称，包括文件扩展名。",
    "The format of the certification file. Only PDF is supported.": "认证文件的格式。仅支持 PDF。",
    "The expiration date of this certification expressed in unix timestamp (seconds) UTC+0.": "此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。",
    "The weight of the product package.": "产品包装的重量。",
    "The package weight, which must be a positive number.": "包装重量，必须是正数。",
    "The unit for the package weight.": "包装重量的单位。",
    "The unit for the SKU weight.": "SKU 重量的单位。",
    "The unit for the SKU dimensions.": "SKU 尺寸的单位。",
    "The package length. A positive whole number.": "包装长度。正整数。",
    "The package width. A positive whole number.": "包装宽度。正整数。",
    "The package height. A positive whole number.": "包装高度。正整数。",
    "The dimensions of the sku.": "SKU 的尺寸。",
    "The packaged weight of the SKU.": "SKU 的包装重量。",
    "A list of general attributes (e.g. manufacturer, country of origin, materials used) that describe the product as a whole, regardless of variant.": "描述产品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。",
    "The ID of the product attribute, retrieved from the": "产品属性的 ID，从",
    "A list of selectable values for the product attribute.": "产品属性的可选值列表。",
    "The ID of a built-in product attribute value, retrieved from the": "内置产品属性值的 ID，从",
    "A self-defined custom product attribute value if the built-in values do not satisfy your needs. The system will auto-generate an ID after listing.": "如果内置值不满足需求，可自定义产品属性值。系统将在上架后自动生成 ID。",
    "The measurement details of the product to help buyers find the right size.": "产品的测量详情，帮助买家找到合适的尺码。",
    "An image of the size chart.": "尺码表的图片。",
    "The URI of the size chart image.": "尺码表图片的 URI。",
    "The dimensions of the product package.": "产品包装的尺寸。",
    "A product introduction or promotion video to display for your product.": "用于展示产品的产品介绍或推广视频。",
    "The ID of the product video.": "产品视频的 ID。",
    "A list of manufacturer IDs. Retrieve the IDs from the": "制造商 ID 列表。从",
    "A list of responsible person IDs. Retrieve the IDs from the": "负责人 ID 列表。从",
    "The result of the product diagnosis (PASS, FAILED).": "产品诊断的结果（PASS, FAILED）。",
    "Warning information that the API caller needs to pay special attention to.": "API 调用者需要特别关注的警告信息。",
    "The built-in attribute.": "内置属性。",
    "The name of the built-in attribute.": "内置属性的名称。",
    "The attribute type.": "属性类型。",
    "A flag to indicate if the product attribute is always required when creating or editing a product.": "标识在创建或编辑产品时是否始终需要该产品属性的标志。",
    "Certification related rules.": "认证相关规则。",
    "Size chart related rules.": "尺码表相关规则。",
    "A flag to indicate whether size charts are supported.": "标识是否支持尺码表的标志。",
    "A flag to indicate whether a size chart is required.": "标识是否需要尺码表的标志。",
    "Cash on Delivery (COD) related rules.": "货到付款（COD）相关规则。",
    "A flag to indicate whether COD is supported.": "标识是否支持 COD 的标志。",
    "Package dimension related rules.": "包装尺寸相关规则。",
    "A flag to indicate whether package dimensions are required.": "标识是否需要包装尺寸的标志。",
    "Extended Producer Responsibility (EPR) related rules.": "生产者延伸责任（EPR）相关规则。",
    "A flag to indicate whether EPR is required.": "标识是否需要 EPR 的标志。",
    "Responsible person (RP) related rules. Applicable only for the EU market.": "负责人（RP）相关规则。仅适用于欧盟市场。",
    "A flag to indicate whether the responsible person information is required.": "标识是否需要负责人信息的标志。",
    "Manufacturer related rules. Applicable only for the EU market.": "制造商相关规则。仅适用于欧盟市场。",
    "A flag to indicate whether the manufacturer information is required.": "标识是否需要制造商信息的标志。",
    "The list of standard built-in product and sales attributes that are bound to the specified category, based on your shop's location.": "根据您店铺的位置，绑定到指定分类的标准内置产品属性和销售属性列表。",
    "The ID of the built-in attribute.": "内置属性的 ID。",
    "The ID of the built-in attribute value.": "内置属性值的 ID。",
    "The name of the built-in attribute value.": "内置属性值的名称。",
    "A list of selectable values for the attribute.": "属性的可选值列表。",
    "A flag indicating whether sellers can enter a custom value for the attribute when creating or editing a product.": "标识卖家在创建或编辑产品时是否可以为属性输入自定义值的标志。",
    "A flag indicating whether sellers can select multiple values for the attribute when creating or editing a product.": "标识卖家在创建或编辑产品时是否可以为属性选择多个值的标志。",
    "The data format for a free-form attribute value.": "自由格式属性值的数据格式。",
    "Certification expiration date related rules.": "认证到期日期相关规则。",
    "A flag to indicate whether an expiration date is required for this certification.": "标识此认证是否需要到期日期的标志。",
    "The type of condition.": "条件的类型。",
    "The ID of the product attribute that is being evaluated by the condition.": "被条件评估的产品属性的 ID。",
    "The ID of the product attribute value that must match the seller's input for the condition to be true.": "必须与卖家输入匹配才能使条件为真的产品属性值的 ID。",
    "Details about the certification documents that you must submit, including the content, format, and any other guidelines.": "您必须提交的认证文件的详细信息，包括内容、格式和任何其他指南。",
    "The URL to view an image of the sample certification document.": "查看示例认证文件图片的 URL。",
    "A unique ID that identifies the brand in TikTok Shop.": "在 TikTok Shop 中标识品牌的唯一 ID。",
    "A status to indicate whether the seller has obtained prior authorization to sell goods bearing the brand's trademark, name, or logo.": "标识卖家是否已获得事先授权销售带有品牌商标、名称或标志的商品的状态。",
    "A flag to indicate whether the brand is a T1 brand, which refers to internationally renowned brands that may have compliance risks and require sellers to obtain brand authorization.": "标识该品牌是否为 T1 品牌的标志，T1 品牌是指可能存在合规风险并要求卖家获得品牌授权的国际知名品牌。",
    "The product type defined on the source platform.": "在源平台上定义的产品类型。",
    "The product vendor or brand name on the source platform.": "源平台上的产品供应商或品牌名称。",
    "Tags associated with the product on the source platform.": "与源平台上产品关联的标签。",
    "Category information assigned to the product on the source platform.": "在源平台上分配给产品的分类信息。",
    "The category ID on the source platform.": "源平台上的分类 ID。",
    "The category name on the source platform.": "源平台上的分类名称。",
    "The full category path or full category name on the source platform.": "源平台上的完整分类路径或完整分类名称。",
    "Whether the category is a leaf category.": "该分类是否为叶子分类。",
    "Whether the category is a root category.": "该分类是否为根分类。",
    "Additional product metadata provided by the source platform.": "源平台提供的额外产品元数据。",
    "A list of product metadata attributes and their values.": "产品元数据属性及其值的列表。",
    "The metadata attribute name.": "元数据属性名称。",
    "The values associated with the metadata attribute.": "与元数据属性关联的值。",
    "Filter size charts by size chart template IDs.": "按尺码表模板 ID 过滤尺码表。",
    "Filter size charts by size chart template name or by key words in the template name.": "按尺码表模板名称或模板名称中的关键词过滤尺码表。",
    "Filter size charts by usage mode.": "按使用模式过滤尺码表。",
    "The list of size charts that meet the query conditions.": "符合查询条件的尺码表列表。",
    "The size chart template name.": "尺码表模板名称。",
    "The list of images included in a size chart.": "尺码表中包含的图片列表。",
    "Leaf category IDs applicable to this size chart.": "适用于此尺码表的叶子分类 ID。",
    "Localized structured size chart data.": "本地化的结构化尺码表数据。",
    "Structured size chart data for the specified locale.": "指定语言环境的结构化尺码表数据。",
    "The language of the size chart table.": "尺码表表格的语言。",
    "The language of the size chart image.": "尺码表图片的语言。",
    "Structured table containing headers and rows.": "包含表头和行的结构化表格。",
    "Ordered header definitions.": "有序的表头定义。",
    "Header display name.": "表头显示名称。",
    "Standard size-system ID or measurement key.": "标准尺码体系 ID 或测量键。",
    "Rows of the size chart.": "尺码表的行。",
    "Cells aligned by index with table.headers.": "按索引与 table.headers 对齐的单元格。",
    "Cell value.": "单元格值。",
    "Additional size chart description.": "额外的尺码表描述。",
    "Whether this is a one-size chart.": "是否为均码表。",
    "The number of size charts that meet the query conditions.": "符合查询条件的尺码表数量。",
    "The currency.": "货币。",
    "The currency.Possible values based on the region:": "货币。基于地区的可能值：",
    "Product fees related rules.": "产品费用相关规则。",
    "The type of fee.": "费用类型。",
    "A flag to indicate whether information about the fee is required.": "标识是否需要费用信息的标志。",
    "The list of special product types, excluding regular products, that your shop is allowed to list in this category.": "您的店铺允许在此分类中上架的特殊产品类型列表（不包括常规产品）。",
    "The brand name.": "品牌名称。",
    "Specify a category ID to show the availability of": "指定分类 ID 以显示",
    "Filter results by the brand authorization status.": "按品牌授权状态过滤结果。",
    "Filter results to include brand names that begin with the specified value.": "过滤结果以包含以指定值开头的品牌名称。",
    "Whether you can select and display a brand depends on the brand's authorization status, the categories authorized for the brand, and whether the brand is classified as T1 (internationally renowned brands that require prior brand authorization).": "您是否可以选择和显示品牌取决于品牌的授权状态、品牌被授权的分类，以及品牌是否被归类为 T1（需要事先品牌授权的国际知名品牌）。",
    "A requirement that the shop needs to satisfy.": "店铺需要满足的要求。",
    "The specific reasons for failing a certain": "未通过特定",
    "The name of the brand.": "品牌名称。",
    "The brand ID.": "品牌 ID。",
    "The product ID.": "产品 ID。",
    "The product field being diagnosed.": "被诊断的产品字段。",
    "The diagnosis results.": "诊断结果。",
    "Product optimization diagnosis information.": "产品优化诊断信息。",
    "Improvement suggestions.": "改进建议。",
    "The suggested SEO keyword text.": "建议的 SEO 关键词文本。",
    "The intelligent text suggestions for titles and descriptions.": "标题和描述的智能文本建议。",
    "The suggested intelligent text.": "建议的智能文本。",
    "The optimized main image. Only the first image in the main image set will be optimized.": "优化后的主图。仅优化主图组中的第一张图片。",
    "The original URI of the image.": "图片的原始 URI。",
    "The original URL of the image.": "图片的原始 URL。",
    "The URI of the image after optimization.": "优化后图片的 URI。",
    "The URL of the image after optimization.": "优化后图片的 URL。",
    "The image height after optimization.": "优化后的图片高度。",
    "The image width after optimization.": "优化后的图片宽度。",
    "The current quality tier of this product listing.": "此产品上架的当前质量等级。",
    "Product listing quality information.": "产品上架质量信息。",
    "Warning information that needs attention.": "需要注意的警告信息。",
    "The listing quality tier you can reach by implementing the recommendation.": "通过实施建议可以达到的上架质量等级。",
    "The recommendation for resolving the identified issue, returned in the default locale language of the shop.": "解决已识别问题的建议，以店铺的默认语言返回。",
    "A machine-readable code that represents an identified issue.": "代表已识别问题的机器可读代码。",
    "A machine-readable code that represents the failure reason.": "代表失败原因的机器可读代码。",
    "A detailed reason for the failure.": "详细的失败原因。",
    "The size chart template ID.": "尺码表模板 ID。",
    "Retrieve the IDs from the": "获取 ID，从",
    "The ID of the category. It must be a leaf category.": "分类 ID。必须是叶子分类。",
    "The ID of the category of this product. It must be a leaf category.": "此产品的分类 ID。必须是叶子分类。",
    "A list of URLs for third-party product listing pages where consumers can place orders.": "消费者可以下单的第三方产品上架页面 URL 列表。",
    "An external identifier used in an external ecommerce platform.": "在外部电商平台中使用的外部标识符。",
    "Max length: 999 characters": "最大长度：999 个字符",
    "The platforms for listing the product.": "产品上架的平台。",
    "The shipping insurance purchase requirement imposed on buyers for the product.": "对买家施加的产品运输保险购买要求。",
    "A flag to indicate if the product is pre-owned.": "标识产品是否为二手产品的标志。",
    "The minimum order quantity for the product.": "产品的最低订购量。",
    "Identifier of the shipping template that will be bound to the product": "将绑定到产品的运费模板的标识符",
    "Options for asynchronous product information verification.": "异步产品信息验证的选项。",
    "Search terms (ST words).": "搜索词（ST 词）。",
    "Key Product Features.": "关键产品特性。",
    "The product title.\nTitle length:": "产品标题。\n标题长度：",
    "A flag indicating whether the shop has failed a": "标识店铺是否未通过",
    "The product IDs to activate.": "要激活的产品 ID。",
    "Max number of IDs: 20": "最大 ID 数量：20",
}

# Table header translations
TABLE_HEADER_MAP = {
    "| Properties ": "| 属性 ",
    "| Location ": "| 位置 ",
    "| Type ": "| 类型 ",
    "| Require ": "| 必填 ",
    "| Sample ": "| 示例 ",
    "| Properties description ": "| 属性描述 ",
    "| Code ": "| 代码 ",
    "| Message ": "| 消息 ",
    "| Quality tier": "| 质量等级",
    "| Category": "| 分类",
    "| Diagnosis code": "| 诊断代码",
    "| Recommendations": "| 建议",
    "| Region": "| 地区",
    "| Diagnosis result": "| 诊断结果",
    "| Country": "| 国家",
    "| Currency": "| 货币",
    "| Currency name": "| 货币名称",
    "| Decimal places": "| 小数位数",
    "| Allowable Price Range": "| 允许价格范围",
    "| Status": "| 状态",
    "| Definition": "| 定义",
    "| Notes": "| 注意事项",
}

# Code comment translations
CODE_COMMENT_MAP = {
    "// Product": "// 产品",
    "// SKU 1": "// SKU 1",
    "// SKU 2": "// SKU 2",
    "// SKU 1 - Red sweater": "// SKU 1 - 红色毛衣",
    "// SKU 2 - Blue sweater": "// SKU 2 - 蓝色毛衣",
    "// SKU 1 - Sweater with red on the outside and blue on the inside": "// SKU 1 - 外面红色里面蓝色的毛衣",
    "// SKU 1 - Red cotton sweater": "// SKU 1 - 红色棉质毛衣",
    "// SKU 2 - Red wool sweater": "// SKU 2 - 红色羊毛毛衣",
    "// SKU 2 - Blue cotton sweater": "// SKU 2 - 蓝色棉质毛衣",
    "// variation A": "// 变体 A",
    "// variation B": "// 变体 B",
    "// added SKU 2 - Blue sweater": "// 添加 SKU 2 - 蓝色毛衣",
    "// added variation B": "// 添加变体 B",
    "// duplicated value": "// 重复值",
    "// unique value": "// 唯一值",
    "// missing variation B": "// 缺少变体 B",
}


def translate_code_comment(line):
    """Translate code comments within code blocks."""
    for eng, chn in CODE_COMMENT_MAP.items():
        if eng in line:
            line = line.replace(eng, chn)
    return line


def translate_table_line(line):
    """Translate table header cells."""
    for eng, chn in TABLE_HEADER_MAP.items():
        if eng in line:
            line = line.replace(eng, chn)
    return line


def translate_line(line, in_code_block):
    """Translate a single line."""
    if in_code_block:
        return translate_code_comment(line)

    stripped = line.strip()

    # Skip empty lines
    if not stripped:
        return line

    # Skip lines that are purely HTML/img/svg/base64
    if stripped.startswith('<img ') or 'from="flow-chart"' in stripped or 'payload=' in stripped:
        return line
    if stripped.startswith('data:image') or stripped.startswith('<br><br>'):
        return line

    # Exact header match
    if stripped in HEADER_MAP:
        return HEADER_MAP[stripped]

    # Sub-header match (## level)
    m = re.match(r'^(#{2,6})\s+(.+)$', stripped)
    if m:
        hashes, title = m.group(1), m.group(2)
        if title in SUBHEADER_MAP:
            indent = len(line) - len(line.lstrip())
            return ' ' * indent + f"{hashes} {SUBHEADER_MAP[title]}"
        if title in HEADER_MAP:
            translated = HEADER_MAP[title].lstrip('#').strip()
            indent = len(line) - len(line.lstrip())
            return ' ' * indent + f"{hashes} {translated}"

    # Exact paragraph match
    if stripped in PARA_MAP:
        indent = len(line) - len(line.lstrip())
        return ' ' * indent + PARA_MAP[stripped]

    # FAQ match
    if stripped in FAQ_MAP:
        indent = len(line) - len(line.lstrip())
        return ' ' * indent + FAQ_MAP[stripped]

    # Table line - translate headers
    if '|' in stripped and stripped.startswith('|'):
        line = translate_table_line(line)

    # Apply inline replacements (longest first to avoid partial matches)
    result = line
    # Sort by length descending to avoid partial replacements
    sorted_inline = sorted(INLINE_MAP.items(), key=lambda x: -len(x[0]))
    for eng, chn in sorted_inline:
        if eng in result:
            result = result.replace(eng, chn)

    return result


def translate_file(filepath):
    """Translate a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []
    in_code_block = False

    for line in lines:
        # Track code blocks
        stripped = line.rstrip('\n')
        if stripped.strip().startswith('```'):
            in_code_block = not in_code_block
            translated_lines.append(stripped)
            continue

        translated = translate_line(stripped, in_code_block)
        translated_lines.append(translated)

    result = '\n'.join(translated_lines)
    # Ensure file ends with newline if original did
    if lines and lines[-1].endswith('\n'):
        result += '\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)


def main():
    directories = [
        "D:/tiktok/tiktok-docs/zh/API_Reference/Products",
        "D:/tiktok/tiktok-docs/zh/API_Reference/Products_Global_Products",
        "D:/tiktok/tiktok-docs/zh/API_Reference/Products_Compliance",
    ]

    files = []
    for d in directories:
        if os.path.exists(d):
            for f in sorted(os.listdir(d)):
                if f.endswith('.md'):
                    files.append(os.path.join(d, f))

    print(f"Found {len(files)} files to translate")

    for i, f in enumerate(files):
        basename = os.path.basename(f)
        print(f"[{i+1}/{len(files)}] Translating: {basename}")
        translate_file(f)

    print(f"\nDone! Translated {len(files)} files.")


if __name__ == "__main__":
    main()
