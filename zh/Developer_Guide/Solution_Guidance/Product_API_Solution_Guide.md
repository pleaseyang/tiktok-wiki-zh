# 商品 API 解决方案指南

**集成原则：API 是数据源；webhook 是变更触发器。** 商品创建、编辑、价格、库存、特殊上架和目录维护操作应通过当前 Product Open API 契约写入，然后通过 Get Product 或相关搜索 API 验证平台状态。Webhook 应触发对账，而不是替代写后读或定时轮询。

# 目的与受众
本指南面向希望直接集成 TikTok Shop 商品 API（而非依赖 1P 连接器路径进行商品上架和日常目录维护）的卖家、ISV、PIM 系统、连接器应用和自研卖家系统。
**这是一份参考集成指南，而非产品需求文档。** 它将当前商品领域的集成模式转化为面向卖家的架构：上架前需要做什么准备、调用哪些商品操作 API、如何处理审核和上架状态，以及如何安全地消费商品 webhook。
起草时使用的主要参考：[TikTok Shop Products API 概览](https://partner.tiktokshop.com/docv2/page/products-api-overview)、[TikTok Shop 开发者指南](https://partner.tiktokshop.com/docv2/page/tts-developer-guide)、[Create Product API](https://partner.tiktokshop.com/docv2/page/create-product-202309)、[Edit Product API](https://partner.tiktokshop.com/docv2/page/edit-product-202509)、[Update Price API](https://partner.tiktokshop.com/docv2/page/update-price-202309)、[Update Inventory API](https://partner.tiktokshop.com/docv2/page/update-inventory-202309)、[Partial Edit Product API](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309)、[Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405)、[商品状态变更 webhook](https://partner.tiktokshop.com/docv2/page/5-product-status-change)、[库存状态变更 webhook](https://partner.tiktokshop.com/docv2/page/27-inventory-status-change)、[商品审核状态变更 webhook](https://partner.tiktokshop.com/docv2/page/37-product-audit-status-change)、[组合商品变更 webhook](https://partner.tiktokshop.com/docv2/page/42-combined-listing-change) 以及 [组合商品 - 合并为变体功能指南](https://seller-us.tiktok.com/university/essay?knowledge_id=1016792318773006&role=1&course_type=1&from=search)、[[外部] TikTok Shop 目录集成解决方案 V2023.Q2.01](https://bytedance.sg.larkoffice.com/docx/GYCFd9SVXomiNhxfaQMcYLIznkf)
# 术语
| 术语 | 在本指南中的含义 |
| --- | --- |
| **卖家系统** | 卖家的 PIM、ERP、OMS、商务平台或中间件，负责管理源目录并调用 TikTok Shop API。 |
| **TikTok 商品** | 在 TikTok Shop 中创建的上架实体。它具有商品级内容、SKU 级商业数据、平台状态和审核状态。 |
| **SKU** | 商品下的可售变体。价格、库存、卖家 SKU 和 SKU 状态在 SKU 级别维护。 |
| **全量编辑** | 重新提交整个商品对象的商品更新。省略的字段可能被视为已删除，除非文档中明确说明的例外（如价格和库存）。 |
| **部分编辑** | 针对选定属性的定向商品更新。当卖家系统有意只修改上架内容的部分时使用。 |
| **关联/组合上架** | TikTok Shop 中的一种商品关系，将多个相关商品 ID 分组，使消费者可以在商品详情页之间切换。这与虚拟套装不同。 |
| **GWP / 非可售** | 买赠礼品。在 Create Product API 中标记为 `non_sellable: true` 的商品。这些被视为赠品，不能单独购买。 |
| **幂等性** | 创建请求可以重试而不会产生重复商品的特性。在本指南中，`external_product_id` 被视为 Create Product 的幂等键。 |
# 集成架构
卖家的目录、OMS 和 WMS 应通过一个集成层调用 TikTok Shop，该集成层负责验证商品 payload、签署 API 请求、存储映射关系并处理 webhook 触发的对账。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e47ffdd9b7384a36bc6816af30d1b98c~tplv-k9wyc2ijk0-image.image)
**推荐状态模型。** 存储外部商品 ID、TikTok 商品 ID、SKU ID、卖家 SKU、类目 ID、TikTok 属性 ID、卖家属性映射、仓库 ID、各仓库库存数量、各 SKU 价格、上架状态、审核状态、拒绝原因、webhook 事件时间戳、最近成功的 API 请求 ID 以及最近一次 TikTok 更新时间。
# 上架前的前置条件
商品上架失败最常见的原因是卖家系统在店铺、类目、品牌、仓库、物流和合规数据就绪之前就开始构建商品 payload。在接入时以及卖家变更市场、类目、品牌、仓库或物流模板时，都需要运行这些检查。
| 领域 | 卖家操作 | 为什么重要 | 测试指南 |
| --- | --- | --- | --- |
| 开发者应用就绪 | 按照 [TikTok Shop 开发者指南](https://partner.tiktokshop.com/docv2/page/tts-developer-guide) 准备应用、授权、请求签名、token 刷新和 webhook 回调配置。 | 在卖家应用能够签署请求、安全刷新 token 并接收授权店铺的 webhook 回调之前，不应开始调用商品 API。 |  |
| 店铺授权 | 确认店铺已授权且处于活跃状态；按租户存储 shop cipher / shop ID。 | 商品写入 API 需要有效的卖家授权上下文和活跃的店铺。 |  |
| 上架前置条件 | 在构建批量创建或编辑 payload 之前调用 `GET /product/202309/prerequisites`。 | 使用响应来识别缺失的设置，例如类目资格、店铺就绪度、品牌、仓库、物流或其他商品上架要求，然后再提交 Create Product。 |  |
| KYC 和资格 | 确认卖家已完成市场接入并可以在目标区域上架。 | Edit Product API 文档将已完成 KYC 的活跃卖家/店铺列为适用条件。 |  |
| 类目映射 | 将外部类目体系映射到 TikTok 类目 ID，并在创建 payload 之前获取类目规则/属性。 | 必填属性、认证、包装尺寸和变体规则因类目而异。 |  |
| 品牌和合规 | 在上架受监管或受限类目之前，解决品牌授权和所需认证。 | 缺少品牌或合规数据通常会导致商品进入拒绝或审核循环。 | 测试时，当卖家处于开发阶段，可以使用"No brand"，无需任何品牌授权。 |
| 仓库和物流 | 将每个外部仓库映射到 TikTok 仓库 ID 并确认物流设置。 | 创建和库存操作需要仓库级别的库存数据和有效的物流配置。 |  |
| 媒体资源就绪 | 上传图片和文件，确保商品媒体在提交前符合平台规则。 | 图片或文件问题可能阻止上架，且在批量上传进入审核后难以修复。 |  |
# 商品生命周期流程
直接集成应将商品同步建模为一小组稳定状态。创建和内容/SKU 更新可能进入审核；价格和库存更新通常保持线上上架的正常运营。在 TikTok 确认批准或拒绝之前，将上一个线上版本与提交版本分开保存。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/937037440e324d1c97420c2cf4db71d7~tplv-k9wyc2ijk0-image.image)
## 商品状态参考
使用商品状态来决定卖家系统接下来可以做什么。生命周期图使用简化状态；卖家 UI 和集成日志应分别保存 TikTok 商品状态、审核状态、拒绝原因和最近提交的版本。
| 状态组 | 对卖家的含义 | 集成处理方式 |
| --- | --- | --- |
| **草稿** | 商品已保存但对消费者不可见。 | 允许卖家在激活或提交之前补全缺失的商品数据、媒体、类目规则、物流输入或合规字段。 |
| **待审核 / 审核中** | 创建或编辑请求正在由 TikTok Shop 审核。 | 保持上一个线上版本和 SKU 映射处于活跃状态。使用商品状态和审核 webhook 来获知提交版本是被批准还是被拒绝。 |
| **失败 / 被拒绝** | 提交的上架版本未通过审核。 | 向卖家展示拒绝原因，保持上一个线上版本不变，让卖家修复 payload 后通过 Create Product、Edit Product 或 Partial Edit Product 重新提交。 |
| **线上** | 商品可见，如果 SKU、价格、库存和店铺条件允许则可以销售。 | 允许通过专用 API 进行正常的价格和库存维护。当卖家系统需要权威线上商品快照时使用 Get Product。 |
| **已停用** | 由于卖家或上架控制主动停用，该上架不再活跃销售。 | 当卖家有意更改销售可用性时，使用文档中记录的 Activate Product 或 Deactivate Products API 流程。 |
| **暂停 / 冻结** | 由于平台侧政策、风控或合规处理，该上架被阻止。 | 不要将其视为正常的卖家停用操作。存储状态原因，展示所需卖家操作，并在问题解决后通过 Get Product 或相关状态 webhook 刷新。 |
| **已删除** | 商品已被移除。 | 停止对该 `product_id` 的价格和库存推送。在确认删除后，卖家可以根据需要重用相同的 `external_product_id` 发起新的 Create Product 请求。 |

商品状态和审核状态相关但不相同。商品状态告知上架是草稿、线上、未激活、暂停还是已删除；审核状态告知提交的创建或编辑版本是仍在审核中、已批准还是已拒绝。
## 操作路由流程

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c451f893c7f24b979a8ce739aae24ff7~tplv-k9wyc2ijk0-image.image)

**路由摘要。** 该流程按卖家试图更改的内容区分商品领域的变更，因为每个操作都有不同的 API 契约、审核行为和对账需求。

* **创建路径变更：** 对新上架和仅限创建的上架属性（如 GWP/非可售、定时上架、拍卖、预售和支持的虚拟套装字段）使用 Create Product。提交后，存储 `product_id`、`sku_id`、提交版本和请求 ID，然后通过商品状态和审核 webhook 跟踪审批。
* **内容和 SKU 模型变更：** 对少量已记录字段子集使用 Partial Edit，当卖家更改完整上架 payload 或 SKU 模型时使用全量 Edit。如果在审核期间添加、删除或重新映射 SKU，在 TikTok 确认批准状态之前保持上一个线上商品/SKU 映射活跃。
* **商业操作变更：** 将纯价格和纯库存变更路由到其专用 API，而非 Edit Product。存储每个 SKU 和仓库发送的最新价格和库存值。使用 webhook 和定期搜索/获取 API 确认 TikTok Shop 反映了卖家系统预期的状态。
* **关系和特殊上架变更：** 使用相关功能部分列出的特定 API 路径或 Create/Edit Product 字段。例如，通过 `non_sellable` 路由 GWP，通过 `product_tag_operations.product_tag = AUCTION` 路由拍卖，通过 `scheduled_sale` 路由定时上架，通过 `subscribe_info` / `subscribe_info_edit` 路由 SNS，通过 `primary_combined_product_id` 和 `combined_skus` 路由支持的虚拟套装创建。
* **写后读规则：** Webhook 应触发后续处理，但它们不是最终的数据源。当卖家系统需要权威的上架状态、审核结果、拒绝原因或最终 SKU 映射时，请调用 Get Product。

## 创建和更新商品
典型的 Create Product 集成应按顺序完成授权、上架前置条件、类目元数据、媒体、物流输入、商品创建和审批跟踪。这使 Create Product payload 专注于提交，而不是用 Create Product 来发现缺失的设置。
### 典型创建商品流程

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b17484ebce884c8f9fa62c6387265e96~tplv-k9wyc2ijk0-image.image)

Create Product 和 Product Edit 遵循相同的集成规范：构建完整的商品模型，验证类目和市场要求，存储 TikTok ID，并在将提交版本视为线上之前处理审核状态。
| 操作 | 使用的 API / 字段 | 面向卖家的指南 |
| --- | --- | --- |
| 创建商品 | `POST /product/202309/products`（[Create Product API](https://partner.tiktokshop.com/docv2/page/create-product-202309)） | 当尚不存在 TikTok 商品时使用。发送完整的商品对象并存储返回的 `product_id` 和 `sku_id`。 |
| 全量编辑 | `PUT /product/202309/products/{product_id}`（[Edit Product API](https://partner.tiktokshop.com/docv2/page/edit-product-202509#Back%20To%20Top)） | 当更改商品对象或 SKU 模型时使用。先获取最新商品，合并预期变更，提交，然后等待审核/状态结果后再替换线上映射。 <br/> Edit Product 响应可以返回 `audit_status`。将 `AUDITING` 视为待审核，`APPROVED` 视为已接受，`NONE` 视为不适用于审核（商品可能处于草稿、冻结、停用或其他未提交上架的状态）。 |
| 部分编辑 | `PATCH /product/202309/products/{product_id}/partial_edit`（[Partial Edit Product API](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309)） | 用于定向商品内容编辑。不要用于纯价格或纯库存变更。 |
| 获取商品 | `GET /product/202309/products/{product_id}`（[Get Product API](https://partner.tiktokshop.com/docv2/page/get-product)） | 当集成在 webhook 通知、审核完成、错误恢复或定期对账后需要权威状态时使用。 |
```JSON
{
  "save_mode": "LISTING",
  "title": "示例纯棉T恤",
  "description": "HTML 商品描述",
  "category_id": "123456",
  "brand_id": "987654",
  "non_sellable": false,
  "scheduled_sale": {"start_time": 1790000000},
  "pre_sale": {"type": "PRE_ORDER"},
  "product_tag_operations": [{"operation": "ADD", "tag": "AUCTION"}],
  "main_images": [{"uri": "tos-image-uri"}],
  "skus": [{
    "seller_sku": "TSHIRT-BLACK-M",
    "price": {"amount": "19.99", "currency": "USD"},
    "inventory": [{"warehouse_id": "7000714532876273410", "quantity": 100}]
  }]
}
```


### 类目推荐
在构建创建或编辑 payload 之前解析 TikTok 类目。卖家可以浏览类目树，向平台请求推荐类目，然后获取所选类目的属性和规则。
| 步骤 | 使用的 API / 字段 | 卖家使用方式 |
| --- | --- | --- |
| 浏览/选择类目 | `GET /product/202309/categories`（[Get Categories API](https://partner.tiktokshop.com/docv2/page/get-categories-202309)） | 当卖家 UI 允许卖家从可用类目树中选择 TikTok 类目时使用。 |
| 推荐类目 | `POST /product/202309/categories/recommend`（[Recommend Category API](https://partner.tiktokshop.com/docv2/page/recommend-category-202309)） | 当卖家不确定最佳类目时使用自动推荐；发送标题、描述和商品信号，然后请卖家确认所选类目。 |
| 确认规则 | `GET /product/202309/categories/{category_id}/rules`（[Get Category Rules API](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309)） | 用于验证类目约束、认证、包装尺寸、尺码表和其他上架要求。提供成功商品上架所需满足的必填属性/条件。 |

### 仓库映射
在商品创建和商品更新之前存储仓库映射。卖家的仓库代码应映射到创建/编辑 payload 和后续库存维护中使用的 TikTok `warehouse_id`。

* 拒绝有库存但没有映射到 TikTok 仓库的上架行。

### 属性映射
使用 `GET /product/202309/categories/{category_id}/attributes`（[Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8)）为所选类目构建商品模板。这些属性包含成功提交上架所需填充的必填字段。
**存储 TikTok Attribute ID，而不仅仅是显示名称。** 属性名称和值标签可能因市场、语言或类目版本而异。持久化 TikTok 属性 ID 使卖家系统能够重建编辑 payload 并对账商品状态，而无需从翻译后的标签中猜测。

### 媒体、尺码表和物流资源
在调用 Create Product 或 Edit Product 之前上传或解析所有资源 ID。创建/编辑 payload 应引用商品媒体 API 返回的 TikTok Shop 资源标识符，而非卖家本地文件路径或外部图片 URL。
| 资源/设置需求 | 使用的 API / 参考 | 卖家使用方式 |
| --- | --- | --- |
| 商品图片 | `POST /product/202309/images/upload`（[Upload Product Image API](https://partner.tiktokshop.com/docv2/page/upload-product-image-202309)） | 在创建/编辑之前上传主商品图片、详情图片和其他上架图片。存储返回的图片 URI 并在商品图片字段中引用。 |
| 商品文件 | `POST /product/202309/files/upload`（[Upload Product File API](https://partner.tiktokshop.com/docv2/page/upload-product-file-202309)） | 上传所选类目或市场要求的商品文件，如证书、合规文件、标签或 Product API 接受的其他文件资源。存储返回的文件标识符用于创建/编辑 payload。 |
| 已有尺码表 | [Search Size Charts API](https://partner.tiktokshop.com/docv2/page/search-size-charts-202407) | 当类目规则要求尺码表且卖家可能已有尺码表时使用。存储所选尺码表 ID 并在上架 payload 中需要的地方引用。 |
| 新建或更新尺码表 | [Create Size Chart API](https://partner.tiktokshop.com/docv2/page/create-size-chart-202608) 和 [Edit Size Charts API](https://partner.tiktokshop.com/docv2/page/edit-size-charts-202608) | 在上架提交之前创建或更新卖家尺码表，然后将生成的尺码表 ID 附加到需要尺码指导的类目商品。 |
| 图片优化 | [Optimized Images API](https://partner.tiktokshop.com/docv2/page/optimized-images-202404) | 当卖家希望使用平台生成的图片改进时使用。仅在卖家审核和批准后在创建/编辑 payload 中引用优化后的图片。 |
| 图片翻译 | [Create Image Translation Tasks API](https://partner.tiktokshop.com/docv2/page/create-image-translation-tasks-202505) 和 [Get Image Translation Tasks API](https://partner.tiktokshop.com/docv2/page/get-image-translation-tasks-202506) | 用于跨市场销售时的图片文字翻译工作流。轮询任务结果，让卖家审核翻译后的资源，然后在创建/编辑中使用已批准的图片 URI。 |
| 物流和运费输入 | `GET /product/202309/prerequisites` 和类目规则 | 在提交之前解析所需的包装尺寸、物流设置、物流选项 ID 和市场特定的上架输入。这些是设置标识符，不是媒体上传。 |

### 最佳实践
| 主题 | 存储内容 | 最佳实践 |
| --- | --- | --- |
| 商品映射 | product_id、商品状态 | 创建/更新后，存储商品的 product id 和 sku id 信息以及商品状态信息。使用这些信息支持后续的商品编辑。 |
| SKU 映射 | `product_id`、`sku_id`、卖家 SKU、线上状态、提交版本、待删除标记 | 在编辑审核期间，同时保留当前线上 SKU 集合和已提交 SKU 集合的映射。如果线上 SKU 为 A、B、C，卖家提交了 B、C、D，在 TikTok 确认新版本线上之前保持 SKU A 映射为待删除。审核期间仍可对 SKU A 下单。 |
| 幂等键 | `external_product_id` 以及店铺详情或任何有助于避免重复创建商品的信息 | 在前一个商品未被删除时，相同的键不能创建另一个商品。该商品被删除后，卖家可以使用相同的键创建新商品。使用此幂等键避免重复创建商品。 |
| 类目映射 | 外部类目到 TikTok 类目的映射 | 为卖家提供工具，允许他们将外部类目映射到 TikTok 类目。这将有助于上架商品，并帮助避免卖家重新选择 TikTok 类目，同时促进自动映射类目。 |
| 属性映射 | 外部属性到 TikTok 属性的映射 | 提供工具允许卖家将外部系统的商品属性映射到 TikTok 属性和值。这将有助于上架商品，卖家无需手动重新添加所有属性信息。属性 ID 根据类目变化。 |
| 审批跟踪 | `product_id`、`sku_id`、提交版本、请求 ID、审核状态、商品状态 | 在 Create Product 之后，等待商品状态变更和商品审核事件，再将上架显示为线上。使用 webhook 事件作为触发器，当卖家系统需要最终批准状态、拒绝原因或 SKU 映射确认时调用 Get Product。 |
| 审核处理 | 已提交商品版本、线上商品版本、审核状态、拒绝原因 | 在商品状态/审核 webhook 或 Get Product 确认提交版本已上线之前，不要替换线上映射、SKU 可用性或面向卖家的可售状态。你也可以存储多个版本的 SKU 映射——一个用于线上，一个用于审核中。该映射对履约订单很有帮助。 |

### 高级功能
| 功能 | 使用的 API / 字段 | 面向卖家的指南 |
| --- | --- | --- |
| 定时发布 | `POST /product/202309/products` 中的 `scheduled_sale` | 在卖家系统中存储预期计划，并通过商品状态 webhook 和 Get Product 验证最终线上状态。 |
| 创建前优化 | [Diagnose and Optimize Product API](https://partner.tiktokshop.com/docv2/page/diagnose-and-optimize-product-202411#Back%20To%20Top) | 在商品拥有 TikTok `product_id` 之前使用。向卖家展示建议，仅提交卖家批准的内容。 |
| 创建后标题/描述优化 | [Get Recommended Product Title and Description API](https://partner.tiktokshop.com/docv2/page/get-recommended-product-title-and-description-202405#Back%20To%20Top) | 仅在商品创建后使用；此 API 需要 `product_id`。通过 Edit Product 或 Partial Edit Product 应用已批准的变更。 |
| 图片优化 | [Optimized Images API](https://partner.tiktokshop.com/docv2/page/optimized-images-202404) | 在支持的地方使用以改进商品图片，然后在 Create Product、Edit Product 或 Partial Edit Product 中引用卖家批准的图片 URI。 |
## 更新价格
使用 `POST /product/202309/products/{product_id}/prices/update`（[Update Price API](https://partner.tiktokshop.com/docv2/page/update-price-202309)）进行 SKU 级别的价格维护。除非有意重建商品 payload，否则不要将纯价格变更纳入全量商品编辑流程。
```JSON
{
  "skus": [{
    "id": "1729382476852921560",
    "price": {"amount": "19.99", "currency": "USD"}
  }]
}
```

**价格更新处理：** 对每个 SKU，发送应显示在 TikTok Shop 上的最终价格。存储每个 `product_id` + `sku_id` 的预期价格、卖家端价格更新时间、请求 ID 和 TikTok 响应状态。使用此记录安全地重试相同的价格更新，忽略较新价格变更后的旧重试，并将 TikTok Shop 的当前价格与卖家系统的最新预期价格进行对账。
## 更新库存
使用 `POST /product/202309/products/{product_id}/inventory/update`（[Update Inventory API](https://partner.tiktokshop.com/docv2/page/update-inventory-202309)）进行仓库级别的 SKU 库存管理。使用 `POST /product/202309/inventory/search`（[Inventory Search API](https://partner.tiktokshop.com/docv2/page/inventory-search-202309)）进行定期对账和回填。
```JSON
{
  "skus": [{
    "id": "1729382476852921560",
    "inventory": [{"warehouse_id": "7000714532876273410", "quantity": 80}]
  }]
}
```

### 库存最佳实践

* 按 SKU 和仓库发送最终可用数量；除非目标市场的 API 参考文档明确支持增量行为，否则不要发送源增量。
* 对于正常量级，卖家可以将每个源库存变更直接推送到 Update Inventory。
* 对于高订单量、高库存变更频率或超卖风险，卖家可以选择在调用 Update Inventory 之前使用聚合/受控节奏。聚合层应将快速的源变更合并为最新的安全数量。
* 为现有 SKU 添加新仓库时，包含应保留在该 SKU 上的所有仓库。如果更新现有仓库的数量，直接只传递该仓库和数量。
* 使用 Inventory Search 进行定期对账，确保遗漏的 webhook、失败的推送或手动 Seller Center 编辑不会导致库存过时。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2c9f2a30402b47f8b7c75cd82c4141a0~tplv-k9wyc2ijk0-image.image)

## Webhook 策略
在卖家的应用上注册商品领域的 webhook，并将每个事件路由到同一个对账队列。Webhook payload 应标识变更内容；卖家系统应在做出下游决策之前拉取商品状态。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/eda4611ca8e044ffac7bea70457f5bfc~tplv-k9wyc2ijk0-image.image)

| Webhook | 主要 payload 字段 | 卖家使用方式 |
| --- | --- | --- |
| 商品状态变更 | `product_id`、`status`、`suspended_reason`、`update_time` | 更新卖家商品状态，展示商品是否线上/未激活/已删除/已暂停，并在需要权威状态时触发 Get Product。 |
| 商品审核状态变更 | `product_id`、审核状态、原因字段、`update_time` | 在提交的创建/编辑通过或未通过审核时通知卖家。批准时，完成提交的映射变更。拒绝时，保持上一个线上映射并提供修复指导。 |
| 商品信息变更 | `product_id`、`changed_fields`、`change_source` | 检测在 Seller Center 或其他应用中直接进行的编辑。拉取商品并决定卖家源目录还是 TikTok 状态对每个字段胜出。 |
| SKU 状态变更 | `product_id`、包含 `sku_id` 和 `status` 的 SKU 列表 | 更新变体可用性，防止未来的价格/库存更新在没有卖家审核的情况下针对已停用的 SKU。 |
| 库存状态变更 | 库存状态、可用数量信号、商品/SKU 引用 | 在低库存或缺货时提醒卖家，并可选地在发送修正更新之前触发库存对账。 |
| 组合商品变更 | `combined_listing_id`、商品、状态、`change_type` | 在组合商品被创建、更新、停用或删除时保持分组上架展示状态同步。 |

# 特殊上架场景
特殊上架功能应在卖家可以提交 payload 之前按市场、类目和卖家资格进行功能门控。如果某个功能在该卖家场景下无法通过 Product API 使用，请描述受支持的卖家工作流，而不是发送不受支持的字段。
| 场景 | 使用的 API / 字段 | 面向卖家的指南 | 建议流程 |
| --- | --- | --- | --- |
| SKU 级虚拟套装 | `POST /product/202309/products` 配合 `primary_combined_product_id` 和 SKU 级 `combined_skus` | 仅在组件商品和 SKU 已上线并映射后创建套装。存储套装 PID、套装 SKU、组件 `product_id` / `sku_id` 和组件数量。仅在目标 API 版本文档记录了相同字段的更新支持时使用编辑。这仅建立 SKU 级套装。 <br/> <br/> 对于**商品级套装**，目前没有 API，卖家必须直接在 Seller Center 中修改。https://seller-us.tiktok.com/university/essay?knowledge_id=894944353240878&role=1&course_type=1&from=search |  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/55ad19e1fdc94f12852ce0ccee0277b0~tplv-k9wyc2ijk0-image.image) <br/>  <br/>  |
| 组合上架/关联 | `POST /product/202506/combined_listing_recommendations/search`（[Products API 概览](https://partner.tiktokshop.com/docv2/page/products-api-overview)） <br/>  | 仅使用此 API 获取可合并为组合上架的推荐商品组，基于颜色、款式、口味或类似变体维度等共享选项属性。请求接收商品 ID，例如 `{"product_ids":["123423536575","123423536576"]}`，响应返回推荐组，如 `option_name`、商品 `id`、`option_value`、`next_page_token` 和 `total_count`。此 API 不创建组合上架、不提交 Seller Center 合并不执行子 SKU 映射。对于实际的合并为变体流程，卖家应在 Manage Products -> Combined Listings -> Merge products 下使用 Seller Center。关系建立后，存储主商品、子商品、生成的变体映射、子 SKU 到组合上架 SKU 的映射以及组合上架状态，因为更改所选商品或删除变体维度可能会重置生成的 SKU 映射。 |  |
| 买赠（GWP） | `POST /product/202309/products` 中的 `non_sellable: true` | 将 GWP 类型视为创建时不可变。要在 GWP 和可售之间转换，先删除上架，等待删除确认，然后重新创建。同一幂等键仅在上一个商品被删除后才能重用。 |  |
| 拍卖上架 | Create Product 中的 `product_tag_operations.product_tag = AUCTION` | 在向卖家展示拍卖之前验证市场和类目资格。在允许创建后拍卖标签维护之前单独确认 Edit Product 支持。 |  |
| 预售 | 类目和市场支持时的 `pre_sale` | 在提交前验证类目规则，并保持卖家 UI 文案明确预售与定时上架不同。 |  |
| SNS | `POST /product/202502/products/search` 配合 `sns_filter`；`GET /product/202309/products/{product_id}` 返回 `subscribe_info`；`PUT /product/202309/products/{product_id}` 或 `POST /product/202309/products/{product_id}/partial_edit` 配合 `subscribe_info_edit` | 假设 SNS 指订阅并节省，卖家可以使用 `sns_filter` 发现 SNS 商品：对已配置 SNS 的商品使用 `CONFIGURED`，对符合 SNS 资格的商品使用 `ELIGIBLE`。使用 Get Product 读取 `subscribe_info`，包括 `support_subscribe`、`subscribe_status`、折扣详情和可用折扣约束。通过 Edit Product 或 Partial Edit Product 启用、禁用或更新 SNS，发送 `subscribe_info_edit.subscribe_status` 为 `ENABLED` 或 `NOT_ENABLED` 配合 `discount_details`。实际配置仍取决于 `support_subscribe` 显示的卖家和商品资格。 |  |
# 卖家白名单和上架资格控制
[卖家商品上架白名单和资格指南](https://bytedance.us.larkoffice.com/docx/FMjjdgUTroFxuixUFShu9H9Wsdd)
# 市场要求
不同市场的商品 payload 并不相同。卖家系统应在创建或编辑之前为目标店铺解析类目规则、合规字段、仓库配置和上架功能。
| 市场/场景 | 所需卖家准备 | 实施指南 |
| --- | --- | --- |
| 欧盟 GPSR | 准备制造商和责任人记录，然后为适用类目传递 `manufacturer_ids` 和 `responsible_person_ids`。 | 在卖家选择所需记录之前阻止上架提交。不要静默省略这些字段，因为商品可能无法通过合规验证或审核。 |
| 类目特定合规 | 获取认证、安全标签、包装尺寸、商品属性和邀请制类目的类目规则。 | 维护按市场的类目规则缓存并在批量上架前刷新。即使外部类目相同，美国、英国、欧盟、东南亚和拉美市场的规则也可能不同。 |
| 仓库和库存 | 将卖家仓库映射到 TikTok 仓库 ID 并验证仓库级别的库存字段。 | 库存更新应针对 SKU + 仓库。拒绝有库存但没有映射到 TikTok 仓库的上架行。 |
| 上架功能 | 检查拍卖、预售、定时销售、临时上架、SNS、GWP 和虚拟套装是否对卖家的市场和类目启用。 | 在卖家 UI 中对不受支持的字段进行功能门控，使不受支持的功能不会产生审核失败或静默无操作。 |
# 全球商品和市场扩展
当一个卖家希望通过多个英国或欧盟店铺提供相同商品时使用此流程。每个店铺是一个独立市场：它有自己的 Shop ID、商品 ID、SKU ID、上架规则、价格、库存和合规要求。
## 使用本地复制
对于新集成，在一个本地店铺中创建商品并使用 Replicate Product 将其复制到每个目标市场。TikTok Shop 维护商品之间的关系，同时每个目标店铺获得自己的商品 ID 和 SKU ID。
| 方法 | 功能 | 使用时机 |
| --- | --- | --- |
| 本地复制 | 将商品从一个本地店铺复制到另一个受支持市场并保持商品关联。 | 用于所有新的 Direct API 集成。 |
| Seller Center 全球上架 | 通过 Seller Center 规则创建和管理关联市场上架。 | 你的集成可以读取关系，但不应在不检查当前商品数据的情况下重建或覆盖它。 |
| 旧版全球商品 API | 使用全球商品记录的旧版跨市场商品方法。 | 仅用于迁移现有旧版商品。不要用于新商品。 |
## 市场扩展的公开 API
Product API 参考文档是请求字段、权限、受支持市场和当前限制的权威来源。
| API 或事件 | 功能 | 使用时机 |
| --- | --- | --- |
| [Get Global Listing Rules](https://partner.tiktokshop.com/docv2/page/get-global-listing-rules-202507) | 返回店铺可用的全球上架方法和库存规则。 | 在展示或启动"跨欧盟销售"流程之前调用。仅在本地复制受支持时继续。 |
| [Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309) | 在选定的源店铺中创建商品。 | 当商品尚不存在于源店铺时使用。 |
| [Replicate Product](https://partner.tiktokshop.com/docv2/page/replicate-product-202507) | 启动从源店铺到受支持目标市场的异步复制。 | 在源商品就绪且目标市场要求已检查后使用。 |
| 全球复制状态变更事件 | 在复制请求完成或需要关注时通知你的应用。 | 使用此事件而非反复发送 Replicate Product 或将提交视为最终成功。 |
| [Get Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) | 返回一个本地商品的最新商品数据和复制信息。 | 在事件之后、对账期间以及重试更新之前使用。 |
| [Partial Edit Product](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309) | 在本地商品上添加或更正选定字段。 | 当复制创建了需要市场特定信息的目标店铺草稿时使用。 |
| [Get Global Replicated Products](https://partner.tiktokshop.com/docv2/page/get-global-replicated-products-202507) | 返回通过复制关联的本地商品。 | 用于现有商品接入、映射修复和定期对账。 |
| [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | 查找店铺中已存在的商品。 | 在创建或复制之前使用，当卖家可能已有匹配商品时。 |

完整的公开 API 列表请参阅 [Products API 概览](https://partner.tiktokshop.com/docv2/page/products-api-overview) 和 [TikTok Shop API 参考文档](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) 的商品部分。
## 实施流程
此流程展示了推荐的卖家旅程。复制是异步的：接受请求是处理的开始，而非目标上架已就绪的确认。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/34008b80ce4943c3ae1fdff7ca4a1c06~tplv-k9wyc2ijk0-image.image)

*如果不支持本地复制，将商品保留为该市场的本地上架。如果复制创建了草稿或失败，更新现有目标商品并在重试前确认其最新状态。*
## Direct API 流程

1. **授权每个店铺。** 获取源店铺和每个目标店铺的访问权限。确认应用具有所需的 Product API 权限范围。
2. **检查店铺就绪度。** 获取卖家的授权店铺，并为每个将创建或接收商品的店铺调用 Get Listing Prerequisites。
3. **检查上架方式。** 调用 Get Global Listing Rules。仅在响应允许对目标市场和库存模型使用本地复制时继续。
4. **准备每个目标市场。** 获取目标店铺的类目、属性、类目规则和授权类目资源。即使实体商品相同，要求也可能因国家/地区而异。
5. **创建源商品。** 在选定的本地店铺中使用 Create Product。保存其本地商品 ID 和 SKU ID。
6. **启动复制。** 对每个受支持的目标市场调用 Replicate Product。成功的 API 响应意味着 TikTok Shop 接受了请求；并不意味着目标上架已准备好销售。
7. **等待结果。** 订阅全球复制状态变更事件。当事件到达时，调用 Get Product 读取最新的目标店铺状态。
8. **完成草稿或修复失败。** 当目标市场需要额外数据时，复制可能创建草稿。使用 Get Product 查找缺失字段，然后使用 Partial Edit Product 或相关的价格和库存 API 进行修正后重新提交。
9. **保存市场映射。** 将 Shopify 商品和变体 ID 与每个市场的 Shop ID、国家、本地商品 ID 和本地 SKU ID 一起存储。

## 实施最佳实践
这些实践描述了安全的集成方法，无需卖家复制 TikTok Shop 的内部设计。
### 商品身份和映射

* 使用卖家自己的稳定商品和变体标识符作为映射的起点。
* 为每个店铺存储单独的记录。包括 Shop ID、国家、本地商品 ID 和本地 SKU ID。
* 永远不要假设同一商品在两个市场中具有相同的商品或 SKU ID。
* 在创建或复制之前，搜索目标店铺并检查保存的映射以避免重复。

### 异步处理和安全重试

* 将 Replicate Product 视为异步请求。向卖家展示处理已开始，然后等待全球复制状态变更事件。
* 使用每个事件作为调用 Get Product 的信号。最新的商品响应应决定下一步操作。
* 对同一源商品和目标店铺只允许一个活跃的复制请求。
* 在重试之前，检查 TikTok Shop 是否已创建线上商品或草稿。更新现有草稿而非创建另一个商品。
* 对临时错误使用延迟重试。不要在短时间内反复调用 API。

### 市场特定数据

* 为每个目标店铺验证类目、属性、资质、认证、制造商、责任人、价格、仓库和库存。
* 将商品内容、价格和库存更新保持为独立操作。这使失败更易于解释和重试。
* 仅当 Get Global Listing Rules 确认市场和仓库支持共享库存时才使用。
* 当目标上架需要本地信息时，仅收集缺失字段并更新该市场的商品。

### 监控和卖家体验

* 使用 Search Products、Get Product 和 Get Global Replicated Products 进行定期对账。Webhook 可能延迟或丢失。
* 保留源商品、目标店铺、请求时间、最新结果和所需卖家操作的审计跟踪。
* 以卖家友好的语言展示错误，例如："法国需要认证"，而不是仅显示 API 错误码。
* 先推出一两个目标市场。在启用更多市场之前确认映射、webhook、合规处理、价格和库存。

**推荐的卖家状态：** 处理中、需要操作和就绪。将详细的 API 状态保留在集成日志中，而卖家以通俗语言看到下一步操作。

## 现有商品
不要仅因为你的应用没有创建就假设商品无关。Seller Center 或其他集成可能已经创建了市场关系。

* 使用 Search Products 查找每个店铺中已存在的商品。
* 使用 Get Product 并检查 `is_replicated` 以查看本地商品是否来自复制。
* 读取 `global_product_association` 以匹配跨店铺的关联 SKU。
* 使用 Get Global Replicated Products 查找完整的关联本地商品集合。
* 如果 Get Product 返回 `global_listing_policy`，保留 Seller Center 全球上架关系并遵循其策略。

## 市场数据和库存
复制尽可能复用商品信息，但不消除本地上架要求。为每个目标店铺验证以下内容：

* 类目和必填商品属性
* 品牌或类目授权
* 认证和支持文件
* 所需的制造商和责任人信息
* 目标市场价格、税务设置、仓库和库存

仅当 Get Global Listing Rules 允许对选定市场和仓库使用共享库存时才使用。否则，为每个店铺分别维护库存。
## 重试和重复预防

* 在创建或复制之前，搜索目标店铺并检查你保存的映射。
* 发送 Replicate Product 后，保存请求上下文并等待状态事件。
* 在重试之前，调用 Get Product 或 Get Global Replicated Products 确认目标商品或草稿是否已存在。
* 如果草稿存在，更新该草稿。不要创建另一个副本。
* 如果一个店铺中已存在两个线上商品，在更改映射或删除上架之前询问卖家保留哪个。

## 旧版商品迁移
本地复制白名单已于 2026 年 6 月 30 日移除。新集成应使用本地复制而无需白名单依赖。
旧版全球商品 API 计划于 2026 年 10 月 30 日停用。对于仍使用旧版方式的商品，请按照[迁移公告](https://partner.tiktokshop.com/docv2/page/6z874qqu)，使用 [Create GPA Upgrade Task](https://partner.tiktokshop.com/docv2/page/create-gpa-upgrade-task-202604) 启动迁移，并订阅 [Global Listing Method Change](https://partner.tiktokshop.com/docv2/page/g2wnrb57) 事件。此迁移流程仅适用于现有旧版商品。
## 卖家和合作伙伴清单

* 仅使用 Partner Center 中记录的公开 TikTok Shop Open API。
* 对新跨市场商品使用本地复制。
* 为每个店铺分别存储商品和 SKU ID。
* 等待复制事件并在重试前确认最新商品状态。
* 完成目标市场合规、价格、仓库和库存数据。
* 不要依赖 `global_product_id` 或任何内部服务。

# API 操作索引
| 操作 | 公开 API 或参考 | 使用时机 |
| --- | --- | --- |
| 获取上架前置条件 | `GET /product/202309/prerequisites` | 检查店铺是否准备好创建或接收上架。 |
| 获取类目 | [Get Categories](https://partner.tiktokshop.com/docv2/page/get-categories-202309) | 向卖家展示所选店铺中可用的类目。 |
| 推荐类目 | [Recommend Category](https://partner.tiktokshop.com/docv2/page/recommend-category-202309) | 当卖家不确定选择哪个类目时推荐类目。 |
| 获取属性 | [Get Attributes](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) | 查找所选类目的必填和选填属性。 |
| 获取类目规则 | [Get Category Rules](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309) | 检查认证、包装尺寸、尺码表和其他类目规则。 |
| 获取授权类目资源 | [Get Authorized Category Assets](https://partner.tiktokshop.com/docv2/page/get-authorized-category-assets-202405) | 检查哪些卖家或类目资质可用于上架。 |
| 上传商品图片 | [Upload Product Image](https://partner.tiktokshop.com/docv2/page/upload-product-image-202309) | 在创建或编辑请求中使用返回的引用之前上传图片。 |
| 上传商品文件 | [Upload Product File](https://partner.tiktokshop.com/docv2/page/upload-product-file-202309) | 上传尺码表、标签、证书和其他商品文件。 |
| 创建前优化 | [Diagnose and Optimize Product](https://partner.tiktokshop.com/docv2/page/diagnose-and-optimize-product-202411#Back%20To%20Top) | 在商品拥有 TikTok Shop 商品 ID 之前检查商品 payload。 |
| 创建后优化 | [Get Recommended Product Title and Description](https://partner.tiktokshop.com/docv2/page/get-recommended-product-title-and-description-202405#Back%20To%20Top) | 在商品创建后改进标题或描述。 |
| 获取全球上架规则 | [Get Global Listing Rules](https://partner.tiktokshop.com/docv2/page/get-global-listing-rules-202507) | 检查店铺是否支持本地复制和共享库存方式。 |
| 创建商品 | [Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309) | 在所选本地店铺的所需数据就绪后创建商品。 |
| 跨市场复制商品 | [Replicate Product](https://partner.tiktokshop.com/docv2/page/replicate-product-202507) | 启动到另一个受支持市场的异步复制。每个目标店铺获得自己的商品和 SKU ID。 |
| 跟踪复制结果 | 全球复制状态变更事件 | 等待事件，然后调用 Get Product。不要将请求接受视为最终上架成功。 |
| 获取商品 | [Get Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) | 在事件之后、对账期间以及重试之前读取最新商品状态。 |
| 全量编辑 | [Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202509) | 先获取最新商品，然后发送完整的预期状态。 |
| 部分编辑 | [Partial Edit Product](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309) | 添加或更正选定的商品字段，包括复制草稿中缺失的字段。 |
| 更新价格 | [Update Price](https://partner.tiktokshop.com/docv2/page/update-price-202309) | 维护一个店铺中本地 SKU 的价格。 |
| 更新库存 | [Update Inventory](https://partner.tiktokshop.com/docv2/page/update-inventory-202309) | 按本地 SKU 和仓库维护库存。 |
| 搜索库存 | [Inventory Search](https://partner.tiktokshop.com/docv2/page/inventory-search-202309) | 对账库存、检查低库存商品或在接入期间回填库存。 |
| 搜索商品 | [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | 在创建或复制之前查找现有商品，并对账店铺中已有的商品。 |
| 获取关联市场商品 | [Get Global Replicated Products](https://partner.tiktokshop.com/docv2/page/get-global-replicated-products-202507) | 查找通过复制关联的本地商品并修复跨市场映射。 |
| 迁移旧版全球商品 | [Create GPA Upgrade Task](https://partner.tiktokshop.com/docv2/page/create-gpa-upgrade-task-202604) | 仅用于仍使用旧版全球商品 API 方式的商品。 |
| 订阅商品事件 | [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) | 订阅受支持的商品、SKU、审核、库存和复制事件。 |
