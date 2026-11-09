# 获取商品

# 路径：/product/202309/products/{product_id}
# 方法：[GET]
# 功能描述
按商品 ID 获取商品详情，包括处于 `FREEZE` 或 `DELETED` 状态的商品。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求路径参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| product_id | string | Y | 1729592969712207008 | TikTok Shop 中的商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| return_under_review_version | bool | N | true | 用于指示当在线商品 (`ACTIVATE` 状态) 被编辑并重新提交供 TikTok Shop 审核时要获取哪些商品信息。 |

* True: 获取当前处于审核中的商品信息的最新版本。
* False: 检索在线生效的商品信息快照 (编辑前)。
   Default: False |
   return_draft_version |bool |N |true |用于指示当商品在 TikTok Shop 中存在草稿时要获取哪些商品信息。
* True: 获取商品信息的草稿版本。
* False: 获取最新商品信息。
   Default: False

**注意**：

* 仅当商品处于 `DRAFT`, `ACTIVATE`, `SELLER_DEACTIVATED`, 或 `PLATFORM_DEACTIVATED` 状态时适用。
* 此字段与 `return_under_review_version` 互斥。仅指定其中一个即可获取结果。 |
   locale |string |N |en-US |用于显示分类信息的 BCP-47 语言环境代码。
   Default: 您店铺的默认语言环境。
   可能的值：
* cs-CZ
* de-AT
* de-BE
* de-DE
* el-GR
* en-GB
* en-IE
* en-US
* es-ES
* es-MX
* fr-FR
* fr-BE
* hu-HU
* id-ID
* it-IT
* ja-JP
* ms-MY
* nl-NL
* nl-BE
* pl-PL
* pt-BR
* pt-PT
* th-TH
* vi-VN
* zh-CN |
   query_options |[]string |N |GET_PRODUCT_DETAIL_URL,GET_PRODUCT_DETAIL_URL |用于获取附加商品信息的选项。
   Currently supported:
* `GET_PRODUCT_DETAIL_URL` : 返回商品详情 URL, 支持通过深链启动 TikTok 客户端。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/1729592969712207008?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&return_under_review_version=true&return_draft_version=true&locale=en-US&query_options=GET_PRODUCT_DETAIL_URL,GET_PRODUCT_DETAIL_URL
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^audit | object |  | 商品审核信息。 |
| **注意**: 仅适用于在 TikTok Shop 上架的商品. 不适用于仅在 Tokopedia 上架的商品。 |  |  |  |
| ^^pre_approved_reasons | []string | ["KYC_PENDING"] | 商品获得预批准的原因。 |
| 仅当 `audit.status=PRE_APPROVED` 时适用，否则返回空数组。 |  |  |  |
可能的值：

* KYC_PENDING: 卖家的入驻(KYC - Know Your Customer 信息)不完整或待处理。
* RESTRICTED_CATEGORY_PENDING: 该商品属于受限类目，且类目审批仍在等待中。要申请访问权限，请通过 TikTok Shop Seller Center 上的 Qualification Center 提交申请。仅适用于美国市场。 |
   ^^status |string |AUDITING |商品审核状态。
   可能的值：
* NONE：商品不适用审核，因为它尚未提交在本平台上架，或处于草稿、冻结或已停用状态。
* AUDITING：商品正在审核中。
* FAILED: 商品审核未通过，或审核已被取消。
* PRE_APPROVED: 该商品已通过审核，但由于前置条件尚未满足而尚未上架。有关前置条件，请参阅 `pre_approved_reasons`。
* APPROVED: 商品已通过审核并在平台上架。 |
   ^^not_submitted_reasons |[]string |["SHOP_INACTIVE"] |商品未提交 TikTok Shop 审核的原因。
   仅当 `audit.status=NONE` 且因店铺未满足一项或多项上架前置条件而无法提交商品审核时适用；否则返回空数组。

可能的值：

* PAYMENT_ACCOUNT_NOT_LINKED: 店铺未关联支付账户。
* SHOP_INACTIVE: 店铺未激活。
* W8_NOT_CONFIGURED：尚未为店铺提供必需的 W-8 税务信息。仅适用于美国店铺。 |
   ^audit_failed_reasons |[]object | |TikTok Shop 审核失败信息。 |
   ^^listing_platform |string |TIKTOK_SHOP |上架商品的平台。
   可能的值：
* TIKTOK_SHOP
* TOKOPEDIA |
   ^^position |string |product |审核失败原因名称。 |
   ^^reasons |[]string |["violate listing rules"] |未通过 TikTok Shop 审核的简要原因。 |
   ^^suggestions |[]string |["The product violates TikTok Shopping listing rules, please check and resubmit."] |失败原因的详细说明。 |
   ^brand |object | |商品品牌信息。 |
   ^^id |string |7082427311584347905 |此商品的品牌 ID。 |
   ^^name |string |brand xxx aaa |该商品的品牌名称。 |
   ^category_chains |[]object | |商品类目树信息。 |
   ^^id |string |853000 |该商品所属类目的 ID。 |
   ^^is_leaf |bool |true |标识该分类是否为叶子分类的标志。

**注意**： 您只能创建或编辑属于叶子分类的商品。 |
^^local_name |string |Botol & Stoples Penyimpanan |请求语言环境中的分类名称。 |
^^parent_id |string |851848 |父分类 ID。
对于根分类，父 ID 为 `0`。 |
^certifications |[]object | |您的商品的认证列表。 |
^^expiration_date |int |1741235456 |此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。 |
^^files |[]object | |认证相关文件列表。 |
^^^format |string |PDF |认证文件的格式。 |
^^^id |string |v09ea0g40000cj91373c77u3mid3g1s0 |认证文件的 ID。 |
^^^name |string |CERT_X2.PDF |认证文件的名称。 |
^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] | 用于查看认证文件的 URL。 |
^^id |string |602362 |用于标识该商品所需认证类型的 ID。 |
^^images |[]object | |认证相关图片列表。 |
^^^height |int |600 |图片高度。
Unit: px |
^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] | 用于查看图片的 URL。 |
^^^width |int |600 |图片宽度。
Unit: px |
^^title |string |SNI Certificate |认证类型的标题。 |
^create_time |int |1234567890 |商品的创建时间，以秒为单位的 Unix 时间戳表示。 |
^delivery_options |[]object | |应用于此商品的自定义配送选项，会覆盖默认的仓库配送选项。
**说明**：直播后草稿不支持此字段，因此即使设置 `return_draft_version=true`，此处的取值也始终反映基础版本中的取值。 |
^^id |string |1729592969712203232 |配送选项 ID。 |
^^is_available |bool |true |指示该配送选项是否对此商品可用的标志。 |
^^name |string |SEND_BY_SELLER |配送选项名称。 |
^description |string |
购买前请将上述详细尺码与您的测量尺寸进行比较。


* M-Size
* XL-Size

![Image](https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627)
 |HTML 格式的商品描述。 | ^external_product_id |string |172959296971220002 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联商品。 | ^global_product_association |object | |The global product association established through global product publishing or manual binding.
**注意**：

* 适用于全球卖家和欧盟境内卖家。
* 不适用于使用 Global Product Replicate (GPR) 工具从其他市场同步商品的 EU 卖家。请改用 `global_listing_policy` 查找关联的源商品。 |
   ^^global_product_id |string |1729592969712207920 |TikTok Shop 中的全球商品 ID。 |
   ^^sku_mappings |[]object | |全球商品与本地商品之间的 SKU 映射列表。 |
   ^^^global_sku_id |string |1729592969712207234 |TikTok Shop 中的全局 SKU ID。 |
   ^^^local_sku_id |string |1729592969712207230 |TikTok Shop 中的本地 SKU ID。 |
   ^^^sales_attribute_mappings |[]object | |全球 SKU 与本地 SKU 之间的销售属性映射列表。 |
   ^^^^global_attribute_id |string |100000 |全局销售属性 ID。 |
   ^^^^global_value_id |string |1001064 |全局销售属性取值 ID。 |
   ^^^^local_attribute_id |string |100000 |本地销售属性 ID。 |
   ^^^^local_value_id |string |1001064 |本地销售属性取值 ID。 |
   ^has_draft |bool |true |指示商品是否有草稿的标志。
* true: 有草稿。
* false: 没有草稿。 |
   ^id |string |1729592969712207008 |TikTok Shop 生成的商品 ID。 |
   ^integrated_platform_statuses |[]object | |商品在与 TikTok Shop 原生集成的平台上的当前状态 (例如 TOKOPEDIA)。

**注意**： 对于印度尼西亚卖家，如果您在创建或编辑商品时未将上架平台设置为 `TOKOPEDIA`，则此字段将被省略。 |
^^platform |string |TOKOPEDIA |集成平台名称。
可能的值：

* TOKOPEDIA |
   ^^status |string |PLATFORM_DEACTIVATED |商品在集成平台中的状态。
   可能的值：
* UNKNOWN
* DRAFT
* PENDING
* FAILED
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED |
   ^is_cod_allowed |bool |true |标识是否在结账时显示货到付款（COD）付款选项的标志。
   仅适用于以下市场：
* 全球卖家: MY, PH, SA, TH, VN
* 本地卖家: ID, MY, PH, SA, TH, VN |
   ^is_not_for_sale |bool |true |用于指示商品是否非售卖、且仅通过购物赠品（GWP）促销活动提供的标志。此类商品不会出现在搜索或推荐中
   True：不出售
   False：在售 |
   ^is_pre_owned |bool |false |标识商品是否为二手商品的标志。
   仅当 TOKOPEDIA 是唯一上架平台时适用。

**说明**：TikTok Shop 平台上的二手商品通过 `category_id` 识别，该类目必须属于指定的二手商品类目之一（例如二手奢侈品包袋、箱包和配饰）。 |
^is_replicated |bool |false |用于指示该商品在其他本地市场是否包含副本（通过本地复制创建）的标志。 |
^key_product_features |[]string |["Breathable mesh upper", "Cushioned foam midsole"] |关键商品特性。 They will be displayed in the Product highlight module on the product detail page and will be used by search engines to increase your search weight for more traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500。 |
^listing_quality_tier |string |POOR |此商品上架的当前质量等级。 The quality tier of a product listing depends on the quality of the content in its product fields such as the title, image, attributes etc。
可能的值：

* POOR
* FAIR
* GOOD
* EXCELLENT

**注意**：仅适用于美国市场。 |
^main_images |[]object | |在商品图片库中展示的图片列表。 |
^^height |int |600 |图像高度。
Unit: px |
^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。
|
^^width |int |600 |图像宽度。
Unit: px |
^manufacturer_ids |[]string |["172959296971220002"] |制造商 ID 列表。
将此取值传入 [Search Manufacturers API](67066a580dcee902fa03ccf9) 中的 `manufacturer_id` 字段，以获取有关制造商的更多信息。
**注意**： 仅适用于欧盟市场 in certain categories |
^minimum_order_quantity |int |1 |商品的最低订购量。
有效范围： [1, 20]
仅适用于印尼市场及其他东南亚市场的部分卖家。如需了解如何获得此字段的访问权限，请联系您的客户经理。 |
^package_dimensions |object | |商品包裹的尺寸 |
^^height |string |10 |包裹高度。 |
^^length |string |10 |包裹长度。 |
^^unit |string |CENTIMETER |包裹尺寸的单位。 |
^^width |string |10 |包裹宽度。 |
^package_weight |object | |商品包装的重量。 |
^^unit |string |KILOGRAM |包装重量的单位。
可能的值：

* `KILOGRAM`
* `POUND` |
   ^^value |string |1.32 |包裹重量。 |
   ^pod_info |object | |MTO 商品的 POD 定制配置。此对象包含按需印刷商品可供消费者定制的模板、面和定制区域。 |
   ^^pod_templates |[]object | |POD 定制模板列表。每个模板代表一个定制方案，可与一个或多个 SKU 关联。 |
   ^^^pod_template_id |string |172959296971220002 |POD 定制模板的唯一标识符。 |
   ^^^remark |string |Front side customization template for basic tee |此定制模板的可选说明或指示。这些说明可用于在定制页面提醒消费者定制要求。 |
   ^^^sku_ids |[]string |["172959296971220002"] |与此定制模板关联的商品 SKU ID 列表。同一 SKU 不能关联多个模板。 |
   ^^^surfaces |[]object | |此模板下可定制商品面的列表，例如正面、背面、衣领或袖子。一个模板最多可包含 10 个面。 |
   ^^^^background_image |object | |可定制面的背景图。通常是用于配置定制区域的基础商品图。 |
   ^^^^^height |int |600 |背景图片的高度，以像素为单位。 |
   ^^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |背景图片的缩略图 URL 列表。 |
   ^^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |背景图片的 URI。
   通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CUSTOMIZATION_IMAGE` 获取此 URI。 |
   ^^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |背景图的 URL 列表。 |
   ^^^^^width |int |600 |背景图片的宽度，以像素为单位。 |
   ^^^^custom_areas |[]object | |该表面上可定制区域的列表。元素的顺序表示渲染最终定制预览时使用的图层顺序。一个表面最多可包含 10 个定制区域。 |
   ^^^^^area_name |string |logo area |可自定义区域的名称。 |
   ^^^^^area_placement |object | |表面上可定制区域的位置，尺寸，和旋转信息。 |
   ^^^^^^height |string |200 |可自定义区域的高度。
   支持两位小数。 |
   ^^^^^^rotate_degree |string |0 |可定制区域的旋转角度，以度为单位。
   支持两位小数。 |
   ^^^^^^width |string |200 |可定制区域的宽度。
   支持两位小数。 |
   ^^^^^^x_coordinate |string |0 |可定制区域在表面上的起始点的 X 坐标。
   支持两位小数。 |
   ^^^^^^y_coordinate |string |0 |可定制区域在表面上的起始点的 Y 坐标。
   支持两位小数。 |
   ^^^^^area_type |string |TEXT |可定制区域的类型。枚举值: `TEXT`、`IMAGE`。 |
   ^^^^^external_area_id |string |172959296971220002 |卖家自定义的定制区域外部标识符，用于与卖家自有系统映射。 |
   ^^^^^image_area |object | |图片类型定制区域的配置. 当 `area_type` 为 `IMAGE` 时返回此字段。 |
   ^^^^^^default_image |object | |此区域显示的可选默认图片。如果消费者未上传自定义图片，则可使用默认图片。 |
   ^^^^^^^height |int |600 |默认图片的高度，以像素为单位。 |
   ^^^^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |默认图片的缩略图 URL 列表。 |
   ^^^^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |默认图片的 URI。
   通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CUSTOMIZATION_IMAGE` 获取此 URI。 |
   ^^^^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |默认图的 URL 列表。 |
   ^^^^^^^width |int |600 |默认图片的宽度，以像素为单位。 |
   ^^^^^^min_height |int |300 |消费者上传图片所需的最小高度（以像素为单位）。 |
   ^^^^^^min_width |int |300 |消费者上传图片所需的最小宽度（以像素为单位）。 |
   ^^^^^is_required |bool |false |指定消费者是否必须为此区域提供定制内容。如果设为 `false`，可使用默认内容或基础商品版本。 |
   ^^^^^text_area |object | |文本类型定制区域的配置。当 `area_type` 为 `TEXT` 时返回此字段。 |
   ^^^^^^align_type |string |CENTER |文本对齐类型。枚举值: `LEFT`、`CENTER`、`RIGHT`。 |
   ^^^^^^colors |[]string |["#FFFFFF"] |供消费者选择的文字颜色列表，使用十六进制颜色值，例如 `#FFFFFF`。 |
   ^^^^^^default_text |string |Hello World |在此区域显示的可选默认文本。如果消费者未定制此区域，可使用默认文本。 |
   ^^^^^^fonts |[]string |["Roboto"] |消费者可选择的字体键列表，基于平台支持的字体库。 |
   ^^^^^^max_text_length |int |20 |消费者文本输入允许的最大字符数。 |
   ^^^^external_surface_id |string |172959296971220002 |卖家自定义的定制面外部标识符，用于与卖家自有系统映射。 |
   ^^^^mask_image |object | |置于定制区域之上的可选蒙版图片，用于支持不规则或镂空效果。 |
   ^^^^^height |int |600 |蒙版图片的高度，以像素为单位。 |
   ^^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |蒙版图片的缩略图 URL 列表。 |
   ^^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |蒙版图片的 URI。
   通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片并使用 `use_case=CUSTOMIZATION_IMAGE` 获取此 URI。 |
   ^^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |蒙版图片的 URL 列表。 |
   ^^^^^width |int |600 |蒙版图片的宽度，以像素为单位。 |
   ^^^^surface_name |string |Front Side |可定制表面的名称，例如，`Front Side` 或 `Back Side`。 |
   ^^^template_name |string |T-Shirt Front Print |定制模板的名称，供卖家用于内部管理。 |
   ^prescription_requirement |object | |商品的处方相关信息。
   **注意**： 仅适用于 Tokopedia. 对于所有药品商品返回此对象，对于非药品商品则省略。 |
   ^^needs_prescription |bool |false |用于指示购买该药品类商品是否需要处方的标志。 |
   ^primary_combined_product_id |string |1729592969712207008 |如果商品是虚拟组合商品，此值为组合中主商品的 ID。如果商品不是虚拟组合商品，则省略此值。 |
   ^product_attributes |[]object | |描述商品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。 |
   ^^id |string |100392 |商品属性的 ID。 |
   ^^name |string |Occasion |商品属性名称。 |
   ^^values |[]object | |商品属性的可选值列表。 |
   ^^^id |string |1001533 |商品属性取值 ID。 |
   ^^^name |string |Birthday |商品属性取值名称。 |
   ^^^metric_standard_info |object | |定义尺码模板信息，用于描述为商品配置的尺码标准和度量值。 |
   ^^^^id |string |7678592839487784712 |尺码模板的唯一 ID。使用此 ID 可确定该商品适用哪个尺码标准模板。 |
   ^^^^metric_value_module_infos |[]object | |尺码模板下的度量值条目列表。每个对象代表卖家为模板中特定度量项提交的取值。 |
   ^^^^^id |string |7678592839487784712 |尺码模板内度量项的唯一 ID。此 ID 标识提交的值属于哪个度量项。 |
   ^^^^^value |string |2026 |卖家为度量模板中的指定指标项提供的取值。 |
   ^^^^^unit_id |string |7678592839484720903 |指标值模块单位 ID。 |
   ^^^^^unit_name |string |piece |指标值模块单位名称。 |
   ^^^^^suffix |string |and |指标值后缀。 |
   ^^^^^prefix |string |daily |指标值前缀。 |
   ^product_families |[]object | |该商品所属的**在售**商品系列。商品系列是一组共享共同特征（如口味、版本或尺寸）的虚拟商品分组，使它们可以在商品页面上作为可选变体展示。
   **注意**：
* 仅适用于美国本地卖家。
* 如果该商品不属于任何商品系列，则省略。 |
   ^^id |string |1000592969712207000 |商品系列 ID。 |
   ^^products |[]object | |属于该商品系列的商品列表。 |
   ^^^id |string |1729592969712207008 |商品 ID。 |
   ^product_status |string |SELLER_DEACTIVATED |TikTok Shop 中与审核状态无关的商品状态。
   可能的值：
* INITIAL
* DRAFT
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED

**注意**： 对于印度尼西亚卖家，如果您在创建或编辑商品时未将上架平台设置为 `TIKTOK_SHOP`，则此字段将被省略。
|
^product_tags |[]string |["AUCTION"] |用于标识特殊类型商品的商品标签
可能的值： AUCTION |
^product_types |[]string |["COMBINED_PRODUCT"] |商品类型。
可能的值：

* COMBINED_PRODUCT: 表示这是虚拟组合商品。
* IN_COMBINED_PRODUCT: 表示此商品属于虚拟组合商品。
* GPR_TARGET_PRODUCT：表示此商品已同步到全局上架商品。仅适用于 EU 市场。 |
   ^recommended_categories |[]object | |基于商品标题、描述和图片为商品推荐的类目。 |
   ^^id |string |850003 |推荐类目的 ID。 |
   ^^local_name |string |
   Botol & Stoples Penyimpanan |请求的语言区域下推荐的类目名称。 |
   ^responsible_person_ids |[]string |["172959296971220003"] |负责人 ID 列表。
   将此值传入 [Search Responsible Persons API](67066a55f17b7d02f95d2fb1) 的 `responsible_person_id` 字段，以获取有关负责人的更多信息。

**注意**： 仅适用于欧盟市场 in certain categories |
^scheduled_sale |object | |商品的定时上架配置，包括是否启用定时上架以及定时上架时间。 |
^^is_enabled_scheduled_sale |bool |false |该商品是否启用了定时上架。 |
^^schedule_sale_time |int |1768899145000 |已存储的计划上架时间，以毫秒为单位的 Unix 时间戳表示。 |
^search_terms |[]string |["sneakers","running shoes","athletic"] |搜索词（ST 词）。 ST words will not be displayed to consumers; they are only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words are consistent with the product description, with a maximum of 15 terms and a total of no more than 250 characters。 |
^shipping_insurance_requirement |string |OPTIONAL |对买家施加的商品运输保险购买要求。
可能的值：

* REQUIRED: 运输保险为强制购买，买家无法取消。
* OPTIONAL: 买家可以选择通过平台购买运输保险。
* NOT_SUPPORTED: 商品不支持运输保险。
   Default: OPTIONAL

仅当上架平台包含 TOKOPEDIA 时适用。 |
^shipping_template_id |string |7552764259994699538 |绑定到该商品的配送模板的标识符 |
^size_chart |object | |商品的测量详情，帮助买家找到合适的尺码。 |
^^image |object | |尺码表的图片。 |
^^^height |int |600 |图片高度。
Unit: px |
^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] | 用于查看图片的 URL。 |
^^^width |int |600 |图片宽度。
Unit: px |
^^template |object | |由卖家中心 > 管理商品 > 批量操作 > 批量管理尺码表中的尺码表工具生成的 TikTok Shop 尺码表模板。 |
^^^id |string |7267563252536723205 |尺码表模板 ID。 |
^skus |[]object | |用于标识商品不同变体的 SKU（库存单位）列表。 |
^^combined_skus |[]object | |如果此 SKU 属于虚拟套装，此对象包含组成套装的单个 SKU 列表（如礼品篮、入门套装）。 |
^^^brand |object | |虚拟组合中包含的源商品的品牌信息。 |
^^^^id |string |7082427311584347905 |虚拟组合中包含的源商品品牌的 ID。 |
^^^^name |string |brand xxx aaa |虚拟组合中包含的源商品的品牌名称。 |
^^^categories |[]object | |虚拟组合中包含的源商品的类目树信息。 |
^^^^id |string |853000 |虚拟组合中包含的源商品所属类目的 ID。 |
^^^^is_leaf |bool |true |标识该分类是否为叶子分类的标志。 |
^^^^local_name |string |Botol & Stoples Penyimpanan |所请求语言区域下的源商品类目名称。 |
^^^^parent_id |string |851848 |虚拟组合中包含的来源商品的父类目 ID。 |
^^^combined_listing_not_live_reasons |[]string |["SUB_PRODUCT_DELETE"] |与虚拟组合装中包含的源商品相关联、导致虚拟组合装状态无法上架的原因。
可能的值：

* SUB_PRODUCT_DEACTIVATE: 表示源商品已被停用。
* SUB_PRODUCT_DELETE: 表示源商品已被删除。
* SUB_PRODUCT_FROZEN: 表示源商品已被冻结。
* SUB_SKU_DELETE: 表示来源 SKU 已被删除。
* SUB_PRODUCT_CATEGORY_FIRST_LEVEL_ERROR: 表示虚拟组合商品的一级类目与来源商品的一级类目不匹配。
* SUB_PRODUCT_CATEGORY_OVER_RESTRICTION: 表示来源商品的一级类目不在受限类目集合中。 |
   ^^^inventory |[]object | |来源 SKU 库存明细。 |
   ^^^^quantity |int |999 |源 SKU 所在仓库中的可用总量。 |
   ^^^^warehouse_id |string |6966568648651605766 |存放源 SKU 的仓库 ID。
   从 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/get-warehouse-list-202309) 获取仓库详情。 |
   ^^^price |object | |Source SKU 定价信息。 |
   ^^^^currency |string |USD |货币。
   基于地区的可能值：
* BRL: 巴西
* CZK: 捷克共和国
* EUR: 法国、德国、爱尔兰、意大利、西班牙、荷兰、比利时、奥地利、希腊、葡萄牙
* GBP: 英国
* HUF: 匈牙利
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* PLN: 波兰
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^^sale_price |string |117.5 |所有卖家
   商品页面上显示的源 SKU 在折扣前的本地展示价格。 |
   ^^^^tax_exclusive_price |string |110 |全球卖家
   源 SKU 的本地税前价格。其中不含任何适用费用，如跨境配送成本、税费及其他费用，因此不会显示在商品页面上。

Note: 不含税定价不适用于使用中国仓库的 JP 和 US 店铺，因此该取值与 sale_price 相同。 |
^^^product_id |string |1729582718312380123 |虚拟套装中包含的源商品 ID。 |
^^^product_main_image |object | |虚拟组合中包含的源商品的主图。 |
^^^^height |int |600 |图像高度。
Unit: px |
^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。 |
^^^^width |int |600 |图像宽度。
Unit: px |
^^^sales_attributes |[]object | |定义来源 SKU 的属性列表（如尺码、颜色、长度）。 |
^^^^id |string |100000 |销售属性 ID。 |
^^^^name |string |Color |销售属性名称。 |
^^^^sku_img |object | |The default/main image for each value (e.g. red) of the primary sales attribute (e.g. color) of the source product. This appears in the product options gallery on TikTok Shop. |
^^^^^height |int |100 |图片高度。
Unit: px |
^^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。 |
^^^^^width |int |100 |图像宽度。
Unit: px |
^^^^supplementary_sku_images |[]object | |A list of supplementary images for each value (e.g. red) of the primary sales attribute (e.g. color) to provide multiple views or details of the source product for that attribute value. These appear in the product options gallery on TikTok Shop.
仅适用于 US 市场。 |
^^^^^height |int |100 |图片高度。
Unit: px |
^^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。 |
^^^^^width |int |100 |图像宽度。
Unit: px |
^^^^value_id |string |100000 |销售属性取值 ID。 |
^^^^value_name |string |Red |销售属性取值名称。 |
^^^seller_sku |string |sku_name |用于管理来源 SKU 的内部编码/名称，买家不可见。 |
^^^sku_count |int |1 |虚拟套装中包含的源 SKU 数量。 |
^^^sku_id |string |1729582718312380123 |虚拟套装中包含的源 SKU ID。 |
^^^title |string |Short Boat Invisible Socks |虚拟组合中包含的来源商品的标题。 |
^^external_list_prices |[]object | |SKU 标价（如 MSRP、RRP）或外部电商平台上的原价信息。
仅适用于美国市场的部分卖家。
**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^^amount |string |1 |价格金额。 |
^^^currency |string |USD |货币。
可能的值： USD |
^^^source |string |SHOPIFY_COMPARE_AT_PRICE |价格来源的外部电商平台。
可能的值：

* SHOPIFY_COMPARE_AT_PRICE: Shopify 中的 compare_at_price。 |
   ^^external_sku_id |string |1729592969712207234 |在外部电商平台中使用的外部标识符。 这用于在 TikTok Shop 和外部电商平台之间关联 SKU。 |
   ^^external_urls |[]string |["https://example.com/path1", "https://example.com/path2"] |消费者可以下单的第三方商品上架页面 URL 列表。 |
   ^^extra_identifier_codes |[]string | ["00012345678905","9780596520687"] |如果 SKU 属于虚拟组合装（包含多个独立 SKU），则为最多 10 个附加标识符代码的列表。

**注意**： 仅适用于欧盟市场。 |
^^fees |[]object | |根据 TikTok Shop 政策该商品所需的费用。仅部分商品类目需要费用，请从 [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) 获取相关要求。 |
^^^additional_attribute |string |SINGLE_USE |Pfand 的可能值：

* SINGLE_USE
* REUSABLE
* NOT_APPLICABLE |
   ^^^amount |string |1.01 |费用金额。
   有效范围：
* PFAND: [0.00 - 6300.00] |
   ^^^type |string |PFAND |费用类型。
   可能的值：PFAND |
   ^^global_listing_policy |object | |当商品是同步目标时返回 Global Product Replicate (GPR) 相关信息。
   仅适用于欧盟市场。 |
   ^^^inventory_type |string |SHARED |要同步的库存类型。
   可能的值：
* SHARED: 库存区域共享
* EXCLUSIVE: 库存独占 |
   ^^^price_sync |bool |true |指示商品价格是否已同步的标志。 |
   ^^^replicate_source |object | |要从中同步的源全球上架商品。 |
   ^^^^product_id |string |1729592969712203232 |源商品的 ID。 |
   ^^^^shop_id |string |7295929697122032321 |源商品的店铺 ID。 |
   ^^^^sku_id |string |1729592969712203232 |源商品的 SKU ID。 |
   ^^id |string |10001 |由 TikTok Shop 生成的 SKU ID。 |
   ^^identifier_code |object | |根据国际标准化法规（如 GTIN）分配给商品的受管标识码，以确保商品在各种平台和系统中可普遍识别。 |
   ^^^code |string |10000000000010 |标识码。 |
   ^^^type |string |GTIN |标识码类型。
   可能的值：
* GTIN
* EAN
* UPC
* ISBN
* JAN |
   ^^inventory |[]object | |SKU 库存详情。
   **说明**：直播后草稿不支持此字段。因此，即使设置 `return_draft_version=true`，此处的取值也始终反映基础版本中的取值。 |
   ^^^backorder_quantity |int |888 |现货库存售罄后，`backorder_quantity` 将自动转换为 `quantity`。此库存的履约遵循下文指定的 `handling_time`。
   注意：按单生产（MTO）、预售和定制商品不支持缺货预订，因此与 backorder_quantity 不兼容。 |
   ^^^handling_time |int |5 |The estimated number of working days needed for a backorder to be shipped. Currently, different warehouses for the same SKU are not allowed to have different `handling_time` |
   ^^^quantity |int |999 |仓库中可用的 SKU 总数量。
   有效范围：[1, 99,999]

注意：此数量特指可以立即发货的有库存的库存量。 |
^^^warehouse_id |string |6966568648651605766 |SKU 存放仓库的 ID。
从 [Get Warehouse List API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6) 获取仓库详情。 |
^^list_price |object | |经审核团队验证为合规的 SKU 标价信息。相当于制造商建议零售价（MSRP）或建议零售价（RRP）。
仅适用于美国市场。
**注意**：

* 如果提交的价格未通过校验，此字段将为空或显示上次核验的价格。
* 该值可能作为划线价显示在商品页面上。但是，是否显示划线价以及显示的金额由审核团队根据各种定价信息审核并决定。 |
   ^^^amount |string |1 |价格金额。 |
   ^^^currency |string |USD |货币。
   可能的值： USD |
   ^^pre_sale |object | |SKU 预售信息，用于根据其预售类型将商品标记为预售商品。

如果未返回此项，表示该商品为普通的非预售商品。 |
^^^fulfillment_type |object | |关于预售订单履约类型及相应时间范围的信息。

* `handling_duration_days` 适用于延长时长的履约。
* `release_date` 用于在固定日期开始履约。 |
   ^^^^handling_duration_days |int |3 |处理预售订单并移交承运商所需的期望持续时间。

仅适用于以下地区和预售类型：
**US**

* `MADE_TO_ORDER`：工作日，3 至 14 天。
* `CUSTOM`：工作日，3 至 30 天。

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`：自然日，3 至 30 天。 |
   ^^^^release_date |int |1619611761 |商品转为普通商品并可供一般购买的日期。在此日期，订单处理也将开始，订单状态将变为 [AWAITING_SHIPMENT](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011)。

仅适用于美国的 `PRE_ORDER`。
**注意**: 此日期是基于卖家在 Seller Center 所选时区的 Unix 时间戳（秒）。
|
^^^type |string |PRE_ORDER |预售类型。
基于地区的可能值：
**US**

* `PRE_ORDER`：商品尚未上架或发布。可通过指定**发布日期**延长履约。
* `MADE_TO_ORDER`：商品仅在收到订单后生产。可通过指定**时长**延长履约。
* `CUSTOM`：因其他因素，商品所需的履约时限超出标准。可通过指定**时长**延长履约。

**英国、欧盟、东南亚、日本和拉丁美洲**

* `PRE_ORDER`：商品尚未上架或发布。可通过指定**时长**延长履约。 |
   ^^price |object | |SKU 定价信息。 |
   ^^^currency |string |USD |货币。
   基于地区的可能值：
* BRL: 巴西
* CZK: 捷克共和国
* EUR: 法国、德国、爱尔兰、意大利、西班牙、荷兰、比利时、奥地利、希腊、葡萄牙
* GBP: 英国
* HUF: 匈牙利
* IDR: 印度尼西亚
* JPY: 日本
* MXN: 墨西哥
* MYR: 马来西亚
* PHP: 菲律宾
* PLN: 波兰
* SGD: 新加坡
* THB: 泰国
* USD: 美国
* VND: 越南 |
   ^^^sale_price |string |117.5 |**所有卖家**
   SKU 在商品页面上折扣前显示的**本地展示价格**。 |
   ^^^starting_bid_price |string |2 |拍卖商品的起始竞价 |
   ^^^tax_exclusive_price |string |110 |**全球卖家**
   SKU 的**本地税前价格**。不含跨境配送费用、税费及其他适用费用等，因此不会显示在商品页面上。

**注意**： 不含税定价不适用于使用中国仓库的 JP 和 US 店铺，因此该取值与 `sale_price` 相同。 |
^^^unit_price |string |1 |SKU 的单价。
你可以展示单位价格，以便更便捷地比较不同商品与包装规格的价格。
仅适用于欧盟市场。
**注意**：

* 仅当您在创建商品时定义了用于计算此价格的要素时，此取值才可用。
* 单价 = 售价/(SKU 单位数量/基本单位数量) |
   ^^sales_attributes |[]object | |定义商品每个变体的属性列表（如尺寸、颜色、长度）。 |
   ^^^id |string |100000 |销售属性 ID。 |
   ^^^name |string |Color |销售属性名称。 |
   ^^^sku_img |object | |主要销售属性（如颜色）每个值（如红色）的默认/主图片。此图片显示在 TikTok Shop 的商品选项库中。 |
   ^^^^height |int |100 |图像高度。
   Unit: px |
   ^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
   ^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
   ^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。 |
   ^^^^width |int |100 |图像宽度。
   Unit: px |
   ^^^supplementary_sku_images |[]object | |主要销售属性（如颜色）每个值（如红色）的补充图片列表，用于提供该商品属性值的多角度视图或详情。这些图片显示在 TikTok Shop 的商品选项库中。

仅适用于 US 市场。 |
^^^^height |int |100 |图像高度。
Unit: px |
^^^^thumb_urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片缩略图的 URL。 |
^^^^uri |string |tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4 |图片的 URI。 |
^^^^urls |[]string |["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"] |用于查看图片的 URL。 |
^^^^width |int |100 |图像宽度。
Unit: px |
^^^value_id |string |100000 |销售属性取值 ID。 |
^^^value_name |string |Red |销售属性取值名称。 |
^^seller_sku |string |sku name |用于管理 SKU 的内部代码/名称，对买家不可见。 |
^^sku_dimensions |object | |SKU 的尺寸。
Note:

* 提供包装商品后测量的尺寸。
* 这些值会影响运费，因此确保尺寸准确很重要。任何测量差异都可能导致额外运费。
* ID、TH、VN 地区为可选。 |
   ^^^height |string |10 |包装高度。正整数。
   注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。 |
   ^^^length |string |10 |包装长度。正整数。
   注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。 |
   ^^^unit |string |CENTIMETER |SKU 尺寸的单位。
   基于地区的可能值：
* US: CENTIMETER, INCH
* 其他地区: CENTIMETER

说明：`sku_weight` 和 `sku_dimensions` 使用相同的计量单位制。例如，将 `KILOGRAM` 与 `CENTIMETER` 搭配使用。 |
^^^width |string |10 |包装宽度。正整数。
注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。 |
^^sku_unit_count |string |1.00 |SKU 代表的商品总量/体积。
例如，如果 SKU 代表 500 毫升水，则当单位类型定义为 ml 时，此值将为 500。
仅适用于欧盟市场。
**注意**：

* 这主要用于计算 SKU 的单价，仅当您希望展示单价以便于跨不同商品和包装尺寸进行价格比较时才需要。
* Unit price = Selling price/(SKU unit count/base unit count)。因此，如果要获取单位价格，还需要定义 "base unit count" 和 "unit type" 商品属性。可通过 [Get Attributes API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8) 获取这些商品属性的相关信息。 |
   ^^sku_weight |object | |SKU 的包装重量。 The returned `value` and `unit` use the same measurement system as `sku_dimensions`; for example, `KILOGRAM` is used with `CENTIMETER`. This weight can affect shipping fees, and it takes precedence over package dimensions when the fee calculated from weight is higher。 |
   ^^^unit |string |KILOGRAM |包装重量的单位。
   基于地区的可能值：
* US: KILOGRAM, POUND
* BR, JP, MX: KILOGRAM, GRAM
* 其他国家: KILOGRAM

说明：package_weight 和 package_dimensions 必须使用相同的计量单位制（公制或英制）。换言之，如果重量使用 KILOGRAM，则尺寸必须使用 CENTIMETER。 |
^^^value |string |1.32 |包装重量，必须是正数。
数字格式因单位而异：

* GRAM: 整数
* KILOGRAM: 最多 3 位小数
* POUND: 最多 2 位小数 |
   ^^status_info |object | |SKU 的状态信息。 |
   ^^^deactivation_source |string |PLATFORM |处于 `DEACTIVATED` 状态的 SKU 的停用来源。
   可能的值：
* SELLER: 表示卖家停用了该 SKU
* PLATFORM: 表示平台因违规原因停用了该 SKU
* COMBO_RELATION: 表示平台由于 sub-SKU 停用而停用了 bundle-SKU。 |
   ^^^status |string |DEACTIVATED |SKU 在 TikTok Shop 中的状态。
   可能的值：
* NORMAL
* DEACTIVATED |
   ^^purchase_order_quantity_limit |object | |该 SKU 的买家购买限制。`maximum_order_quantity` 是买家在单个订单中可购买的最大数量，`cumulative_order_quantity` 是限制生效期间买家在所有订单中可购买的最大数量。 |
   ^^^maximum_order_quantity |int |2 |每个订单的最大购买数量，针对每个
   商品款式（SKU）。
   例如：如果为含 5 个款式（SKU）的商品设置最大限购 2，则客户每个 SKU 最多可购买 2 件，每笔订单合计最多 10 件。 |
   ^^^cumulative_order_quantity |int |20 |· 客户可购买某商品的总数量
   限购生效期间，跨所有订单的款式（SKU）数量。清除限购将重置其历史购买量，允许其按新限购再次购买；若未设置限购，则不受限制。
   • 例如，如果为含 5 个款式（SKU）的商品设置总限购 2，则客户每个 SKU 最多可购买 2 件，多次购买合计最多 10 件。之后，除非清除限购，否则无法继续购买。总限购必须大于或等于最大值
   limit. |
   ^status |string |SELLER_DEACTIVATED |商品在 TikTok Shop 中的状态。此状态同时涵盖商品状态和审核状态。
   可能的值：
* DRAFT
* PENDING
* FAILED
* ACTIVATE
* SELLER_DEACTIVATED
* PLATFORM_DEACTIVATED
* FREEZE
* DELETED
* SCHEDULED

**注意**： 对于印度尼西亚卖家，如果您在创建或编辑商品时未将上架平台设置为 `TIKTOK_SHOP`，则此字段将被省略。 |
^subscribe_info |object | |与指定商品关联的所有 Save and Subscribe 促销信息。 |
^^subscribe_discount_details |[]object | |所有 Save and Subscribe 优惠详情。 |
^^^discount_level |string |REGULAR |表示折扣类型的枚举:

* REGULAR
* FIRST_ORDER
* RETENTION |
   ^^^discount_value |int |10 |折扣的取值。取值为 10 表示 10% 的折扣。 |
   ^^subscribe_promotion_config |[]object | |特定于卖家的订阅配置。其中列明了可供使用的不同推广类型及相关约束。 |
   ^^^discount_level |string |REGULAR |表示折扣类型的枚举:
* REGULAR
* FIRST_ORDER
* RETENTION |
   ^^^discount_options |[]int |[5, 10, 15, 20] |卖家在给定折扣层级下可用的折扣选项。 |
   ^^^max_discount |int |90 |卖家可为关联折扣档位设置的最大折扣。 |
   ^^^min_discount |int |5 |卖家可为关联折扣档位设置的最小折扣。 |
   ^^subscribe_status |string |ENABLED |用于说明指定商品是否存在生效中的 Subscribe and Save 促销活动的枚举：
* ENABLED
* NOT_ENABLED |
   ^^support_subscribe |bool |false |用于说明卖家和指定商品是否支持 Subscribe and Save 促销活动的标志。 |
   ^title |string |Short Boat Invisible Socks |商品标题。 |
   ^update_time |int |1234567899 |商品最近一次更新的时间，以秒为单位的 Unix 时间戳表示。 |
   ^video |object | |商品视频信息。 |
   ^^cover_url |string |https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036 |用于查看视频封面图的 URL。 |
   ^^format |string |MP4 |视频格式。 |
   ^^height |int |480 |视频高度。
   Unit: px |
   ^^id |string |v09ea0g40000cj91373c77u3mid3g1s0 |视频 ID。 |
   ^^size |int |1000 |视频原始文件大小。
   Unit: MB |
   ^^url |string |https://v16m-default.akamaized.net/bbae7099581b26cd340beaa7821b2d8c/64de6020/video/tos/alisg/tos-alisg-v-f466fc-sg/oMne9QuzIBN3fIDN7bFCCMbBKuGigg12ghDC8k/?a=0&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=2212&bt=1106&cs=0&ds=3&ft=dl9~j-Inz7TKnfsfiyq8Z&mime_type=video_mp4&qs=13&rc=anR4Ojk6ZmYzbTMzODRmNEBpanR4Ojk6ZmYzbTMzODRmNEBsYWFwcjRva2NgLS1kLy1zYSNsYWFwcjRva2NgLS1kLy1zcw%3D%3D&l=202308171159498F7B108584E58B010932&btag=e00048000 |用于查看视频的 URL。 |
   ^^width |int |1280 |视频宽度。
   Unit: px |
   ^selling_format |string |FIXED_PRICE |The product's sale format. 可能的值： FIXED_PRICE, LIVE_AUCTION, FIXED_PRICE_AND_LIVE_AUCTION。 |
   ^is_blind_box |bool |false |该商品是否为盲盒或福袋。例如: PopMart |
   ^product_detail_url |string |detail_url |支持深链以唤起 TikTok 客户端的商品详情 URL。需在 query_options 参数中添加 GET_PRODUCT_DETAIL_URL。 |

# 响应示例
```json
{"code":0,"data":{"audit":{"pre_approved_reasons":["KYC_PENDING"],"status":"AUDITING","not_submitted_reasons":["SHOP_INACTIVE"]},"audit_failed_reasons":[{"listing_platform":"TIKTOK_SHOP","position":"product","reasons":["violate listing rules"],"suggestions":["The product violates TikTok Shopping listing rules, please check and resubmit."]}],"brand":{"id":"7082427311584347905","name":"brand xxx aaa"},"category_chains":[{"id":"853000","is_leaf":true,"local_name":"Botol \u0026 Stoples Penyimpanan","parent_id":"851848"}],"certifications":[{"expiration_date":1741235456,"files":[{"format":"PDF","id":"v09ea0g40000cj91373c77u3mid3g1s0","name":"CERT_X2.PDF","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"]}],"id":"602362","images":[{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600}],"title":"SNI Certificate"}],"create_time":1234567890,"delivery_options":[{"id":"1729592969712203232","is_available":true,"name":"SEND_BY_SELLER"}],"description":"\u003cp\u003ePlease compare above detailed size with your measurement before purchase.\u003c/p\u003e\n\u003cul\u003e \n  \u003cli\u003eM-Size\u003c/li\u003e\n  \u003cli\u003eXL-Size\u003c/li\u003e\n\u003c/ul\u003e \n\u003cimg src=\"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/181595ea7d26489284b5667488d708c1~tplv-o3syd03w52-origin-jpeg.jpeg?from=1432613627\" /\u003e\n","external_product_id":"172959296971220002","global_product_association":{"global_product_id":"1729592969712207920","sku_mappings":[{"global_sku_id":"1729592969712207234","local_sku_id":"1729592969712207230","sales_attribute_mappings":[{"global_attribute_id":"100000","global_value_id":"1001064","local_attribute_id":"100000","local_value_id":"1001064"}]}]},"has_draft":true,"id":"1729592969712207008","integrated_platform_statuses":[{"platform":"TOKOPEDIA","status":"PLATFORM_DEACTIVATED"}],"is_cod_allowed":true,"is_not_for_sale":true,"is_pre_owned":false,"is_replicated":false,"key_product_features":["Breathable mesh upper","Cushioned foam midsole"],"listing_quality_tier":"POOR","main_images":[{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600}],"manufacturer_ids":["172959296971220002"],"minimum_order_quantity":1,"package_dimensions":{"height":"10","length":"10","unit":"CENTIMETER","width":"10"},"package_weight":{"unit":"KILOGRAM","value":"1.32"},"pod_info":{"pod_templates":[{"pod_template_id":"172959296971220002","remark":"Front side customization template for basic tee","sku_ids":["172959296971220002"],"surfaces":[{"background_image":{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600},"custom_areas":[{"area_name":"logo area","area_placement":{"height":"200","rotate_degree":"0","width":"200","x_coordinate":"0","y_coordinate":"0"},"area_type":"TEXT","external_area_id":"172959296971220002","image_area":{"default_image":{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600},"min_height":300,"min_width":300},"is_required":false,"text_area":{"align_type":"CENTER","colors":["#FFFFFF"],"default_text":"Hello World","fonts":["Roboto"],"max_text_length":20}}],"external_surface_id":"172959296971220002","mask_image":{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600},"surface_name":"Front Side"}],"template_name":"T-Shirt Front Print"}]},"prescription_requirement":{"needs_prescription":false},"primary_combined_product_id":"1729592969712207008","product_attributes":[{"id":"100392","name":"Occasion","values":[{"id":"1001533","name":"Birthday","metric_standard_info":{"id":"7678592839487784712","metric_value_module_infos":[{"id":"7678592839487784712","value":"2026","unit_id":"7678592839484720903","unit_name":"piece","suffix":"and","prefix":"daily"}]}}]}],"product_families":[{"id":"1000592969712207000","products":[{"id":"1729592969712207008"}]}],"product_status":"SELLER_DEACTIVATED","product_tags":["AUCTION"],"product_types":["COMBINED_PRODUCT"],"recommended_categories":[{"id":"850003","local_name":"\t\nBotol \u0026 Stoples Penyimpanan"}],"responsible_person_ids":["172959296971220003"],"scheduled_sale":{"is_enabled_scheduled_sale":false,"schedule_sale_time":1768899145000},"search_terms":["sneakers","running shoes","athletic"],"shipping_insurance_requirement":"OPTIONAL","shipping_template_id":"7552764259994699538","size_chart":{"image":{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600},"template":{"id":"7267563252536723205"}},"skus":[{"combined_skus":[{"brand":{"id":"7082427311584347905","name":"brand xxx aaa"},"categories":[{"id":"853000","is_leaf":true,"local_name":"Botol \u0026 Stoples Penyimpanan","parent_id":"851848"}],"combined_listing_not_live_reasons":["SUB_PRODUCT_DELETE"],"inventory":[{"quantity":999,"warehouse_id":"6966568648651605766"}],"price":{"currency":"USD","sale_price":"117.5","tax_exclusive_price":"110"},"product_id":"1729582718312380123","product_main_image":{"height":600,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":600},"sales_attributes":[{"id":"100000","name":"Color","sku_img":{"height":100,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":100},"supplementary_sku_images":[{"height":100,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":100}],"value_id":"100000","value_name":"Red"}],"seller_sku":"sku_name","sku_count":1,"sku_id":"1729582718312380123","title":"Short Boat Invisible Socks"}],"external_list_prices":[{"amount":"1","currency":"USD","source":"SHOPIFY_COMPARE_AT_PRICE"}],"external_sku_id":"1729592969712207234","external_urls":["https://example.com/path1","https://example.com/path2"],"extra_identifier_codes":["00012345678905","9780596520687"],"fees":[{"additional_attribute":"SINGLE_USE","amount":"1.01","type":"PFAND"}],"global_listing_policy":{"inventory_type":"SHARED","price_sync":true,"replicate_source":{"product_id":"1729592969712203232","shop_id":"7295929697122032321","sku_id":"1729592969712203232"}},"id":"10001","identifier_code":{"code":"10000000000010","type":"GTIN"},"inventory":[{"backorder_quantity":888,"handling_time":5,"quantity":999,"warehouse_id":"6966568648651605766"}],"list_price":{"amount":"1","currency":"USD"},"pre_sale":{"fulfillment_type":{"handling_duration_days":3,"release_date":1619611761},"type":"PRE_ORDER"},"price":{"currency":"USD","sale_price":"117.5","starting_bid_price":"2","tax_exclusive_price":"110","unit_price":"1"},"sales_attributes":[{"id":"100000","name":"Color","sku_img":{"height":100,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":100},"supplementary_sku_images":[{"height":100,"thumb_urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"uri":"tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036"],"width":100}],"value_id":"100000","value_name":"Red"}],"seller_sku":"sku name","sku_dimensions":{"height":"10","length":"10","unit":"CENTIMETER","width":"10"},"sku_unit_count":"1.00","sku_weight":{"unit":"KILOGRAM","value":"1.32"},"status_info":{"deactivation_source":"PLATFORM","status":"DEACTIVATED"},"purchase_order_quantity_limit":{"maximum_order_quantity":2,"cumulative_order_quantity":20}}],"status":"SELLER_DEACTIVATED","subscribe_info":{"subscribe_discount_details":[{"discount_level":"REGULAR","discount_value":10}],"subscribe_promotion_config":[{"discount_level":"REGULAR","discount_options":[5,10,15,20],"max_discount":90,"min_discount":5}],"subscribe_status":"ENABLED","support_subscribe":false},"title":"Short Boat Invisible Socks","update_time":1234567899,"video":{"cover_url":"https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/6c8519a3663a4d728c4e3c131dc914b4~tplv-o3syd03w52-resize-jpeg:300:300.jpeg?from=522366036","format":"MP4","height":480,"id":"v09ea0g40000cj91373c77u3mid3g1s0","size":1000,"url":"https://v16m-default.akamaized.net/bbae7099581b26cd340beaa7821b2d8c/64de6020/video/tos/alisg/tos-alisg-v-f466fc-sg/oMne9QuzIBN3fIDN7bFCCMbBKuGigg12ghDC8k/?a=0\u0026ch=0\u0026cr=0\u0026dr=0\u0026er=0\u0026lr=default\u0026cd=0%7C0%7C0%7C0\u0026br=2212\u0026bt=1106\u0026cs=0\u0026ds=3\u0026ft=dl9~j-Inz7TKnfsfiyq8Z\u0026mime_type=video_mp4\u0026qs=13\u0026rc=anR4Ojk6ZmYzbTMzODRmNEBpanR4Ojk6ZmYzbTMzODRmNEBsYWFwcjRva2NgLS1kLy1zYSNsYWFwcjRva2NgLS1kLy1zcw%3D%3D\u0026l=202308171159498F7B108584E58B010932\u0026btag=e00048000","width":1280},"selling_format":"FIXED_PRICE","is_blind_box":false,"product_detail_url":"detail_url"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019150 | 商品 ID 不存在。 |
| 12052032 | 商品不存在 |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052260 | 商品 ID 不存在 |
| 12052547 | 该商品没有处于审核中的版本。请获取线上版本。 |
| 12052704 | 卖家 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |

