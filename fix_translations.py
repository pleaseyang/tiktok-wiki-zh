#!/usr/bin/env python3
"""Fix remaining untranslated English content in translated docs."""
import os
import re

# ============================================================
# PHASE 1: Inline substring replacements (for mixed Chinese/English lines)
# Applied to ALL non-code lines, longest first
# ============================================================
INLINE_FIXES = [
    # Table header fix (appears in all 69 files)
    ("属性 description", "属性描述"),
    ("分类 does not exist", "分类不存在"),
    ("分类 version and categoryID are not matched.", "分类版本与 categoryID 不匹配。"),
    ("分类 is not final category", "分类不是最终分类"),

    # Common mixed-content phrases in table cells
    ("Use the [Get Categories API]", "使用 [Get Categories API]"),
    ("Use the [Get Brands API]", "使用 [Get Brands API]"),
    ("Use the [Get Category Rules API]", "使用 [Get Category Rules API]"),
    ("Use the [Upload Product File API]", "使用 [Upload Product File API]"),
    ("Use the [Upload Product Image API]", "使用 [Upload Product Image API]"),
    ("Use the [Optimize Images API]", "使用 [Optimize Images API]"),
    ("Use the [Get Attributes API]", "使用 [Get Attributes API]"),
    ("Use the [Get Warehouse List API]", "使用 [Get Warehouse List API]"),
    ("Refer to [Product Pricing]", "参考 [Product Pricing]"),
    ("Refer to TikTok Shop Academy", "参考 TikTok Shop Academy"),

    ("Obtain this URI by uploading the images through the [Upload Product Image API]",
     "通过 [Upload Product Image API] 上传图片获取此 URI"),
    ("Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload the files first and obtain the corresponding file ID.",
     "先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传文件获取相应的文件 ID。"),
    ("to get the list of available brands for a shop.", "获取店铺可用品牌列表。"),
    ("to check if COD is supported for your product category.", "检查您的产品分类是否支持 COD。"),
    ("to check the requirements.", "检查要求。"),
    ("to obtain the available categories.", "获取可用分类。"),
    ("Retrieve this value from the [Get Category Rules API]", "从 [Get Category Rules API] 获取此值"),
    ("Retrieve the IDs from the", "获取 ID，从"),

    # "Get by API" line
    ("Get by API [Get Authorization Shop]", "通过 API 获取 [Get Authorization Shop]"),

    # Common phrases
    ("Possible values:", "可能的值："),
    ("Possible values based on region:", "基于地区的可能值："),
    ("Possible values based on the region:", "基于地区的可能值："),
    ("Possible values for Pfand:", "Pfand 的可能值："),
    ("Default: TIKTOK_SHOP", "默认值：TIKTOK_SHOP"),
    ("Default: false", "默认值：false"),
    ("Default: true", "默认值：true"),
    ("Default: v1", "默认值：v1"),
    ("Default: LISTING", "默认值：LISTING"),

    # Applicable phrases
    ("Applicable only for sellers that migrated from Tokopedia.", "仅适用于从 Tokopedia 迁移的卖家。"),
    ("Applicable only for the EU market.", "仅适用于欧盟市场。"),
    ("Applicable only for global sellers.", "仅适用于全球卖家。"),
    ("Applicable only for US local sellers.", "仅适用于美国本地卖家。"),
    ("Applicable only for selected local sellers in the US market.", "仅适用于美国市场选定的本地卖家。"),
    ("Applicable only for the Indonesia market and selected sellers in other SEA markets.", "仅适用于印度尼西亚市场和东南亚其他市场的选定卖家。"),
    ("Applicable only for the following markets:", "仅适用于以下市场："),
    ("Applicable only for the following regions and pre-sale type:", "仅适用于以下地区和预售类型："),
    ("Applicable only if `allowed_special_product_types`", "仅当 `allowed_special_product_types`"),
    ("Applicable only if TOKOPEDIA is the sole listing platform.", "仅当 TOKOPEDIA 是唯一上架平台时适用。"),
    ("Applicable only if the listing platforms include TOKOPEDIA.", "仅当上架平台包含 TOKOPEDIA 时适用。"),

    # Note/Recommendation/Format/Important/Tip labels
    ("**Note**:", "**注意**："),
    ("**Note**: ", "**注意**："),
    ("Note:", "注意："),
    ("**Recommendations**:", "**建议**："),
    ("**Recommendations**: ", "**建议**："),
    ("**Format**:", "**格式**："),
    ("**Format**: ", "**格式**："),
    ("Format:", "格式："),
    ("**Important**:", "**重要**："),
    ("**Important**: ", "**重要**："),
    ("**Tip**:", "**提示**："),
    ("**Tip**: ", "**提示**："),
    ("**Rules for the US market**:", "**美国市场规则**："),
    ("**UK, EU, SEA, JP, and LATAM**", "**英国、欧盟、东南亚、日本和拉丁美洲**"),
    ("**US**", "**美国**"),

    # Deprecated field notice
    ("(**Deprecated**: This field is deprecated and will be removed in a future API version. Use [Diagnose and Optimize Product]",
     "（**已弃用**：此字段已弃用，将在未来的 API 版本中移除。请使用 [Diagnose and Optimize Product]"),
    ("API instead to get listing quality related information.)",
     "API 获取上架质量相关信息。）"),

    # Query/Body labels
    ("**Query**", "**查询**"),
    ("**Body**", "**正文**"),

    # Common inline descriptions
    ("The price amount.", "价格金额。"),
    ("The fee amount.", "费用金额。"),
    ("starting bid price for auction product", "拍卖产品的起始竞价"),
    ("The type of pre-sale.", "预售类型。"),
    ("The type of fee.", "费用类型。"),
    ("The type of identifier code.", "标识码类型。"),
    ("The identifier code.", "标识码。"),
    ("The external ecommerce platform from which the price is sourced.", "价格来源的外部电商平台。"),
    ("An optional attribute that provides additional context for the fee. The accepted values may vary by fee type and market.",
     "提供费用附加上下文的可选属性。接受的值可能因费用类型和市场而异。"),

    # Country names in bullet lists
    ("* DE: Germany", "* DE: 德国"),
    ("* ES: Spain", "* ES: 西班牙"),
    ("* FR: France", "* FR: 法国"),
    ("* IE: Ireland", "* IE: 爱尔兰"),
    ("* IT: Italy", "* IT: 意大利"),
    ("* GB: United Kingdom", "* GB: 英国"),
    ("* AT: Austria", "* AT: 奥地利"),
    ("* GR: Greece", "* GR: 希腊"),
    ("* ID: Indonesia", "* ID: 印度尼西亚"),
    ("* JP: Japan", "* JP: 日本"),
    ("* MY: Malaysia", "* MY: 马来西亚"),
    ("* PH: Philippines", "* PH: 菲律宾"),
    ("* SG: Singapore", "* SG: 新加坡"),
    ("* TH: Thailand", "* TH: 泰国"),
    ("* US: United States", "* US: 美国"),
    ("* VN: Vietnam", "* VN: 越南"),
    ("* MX: Mexico", "* MX: 墨西哥"),
    ("* BR: Brazil", "* BR: 巴西"),
    ("* PL: Poland", "* PL: 波兰"),
    ("* PT: Portugal", "* PT: 葡萄牙"),
    ("* HU: Hungary", "* HU: 匈牙利"),
    ("* CZ: Czech Republic", "* CZ: 捷克共和国"),
    ("* NL: Netherlands", "* NL: 荷兰"),
    ("* BE: Belgium", "* BE: 比利时"),
    ("* SA: Saudi Arabia", "* SA: 沙特阿拉伯"),

    # Currency names
    ("* BRL: Brazil", "* BRL: 巴西"),
    ("* CZK: Czech Republic", "* CZK: 捷克共和国"),
    ("* EUR: France, Germany, Ireland, Italy, Spain, Netherlands, Belgium, Austria, Greece, Portugal",
     "* EUR: 法国、德国、爱尔兰、意大利、西班牙、荷兰、比利时、奥地利、希腊、葡萄牙"),
    ("* GBP: United Kingdom", "* GBP: 英国"),
    ("* HUF: Hungary", "* HUF: 匈牙利"),
    ("* IDR: Indonesia", "* IDR: 印度尼西亚"),
    ("* JPY: Japan", "* JPY: 日本"),
    ("* MXN: Mexico", "* MXN: 墨西哥"),
    ("* MYR: Malaysia", "* MYR: 马来西亚"),
    ("* PHP: Philippines", "* PHP: 菲律宾"),
    ("* PLN: Poland", "* PLN: 波兰"),
    ("* SGD: Singapore", "* SGD: 新加坡"),
    ("* THB: Thailand", "* THB: 泰国"),
    ("* USD: United States", "* USD: 美国"),
    ("* VND: Vietnam", "* VND: 越南"),

    # Common error messages
    ("The seller is inactive.", "卖家不活跃。"),
    ("seller id not exist", "卖家 ID 不存在"),
    ("The check failed.", "检查失败。"),
    ("Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support.",
     "内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。"),
    ("internal error", "内部错误"),
    ("The number of provided product IDs exceeds the limit.", "提供的产品 ID 数量超过限制。"),
    ("You cannot edit the specified product(s) as it isn't listed in your account or shop.",
     "您无法编辑指定产品，因为它未在您的账户或店铺中上架。"),
    ("Exceeded the product listing limit for the seller.", "超过卖家的产品上架限制。"),
    ("product is not supported to list in designated sale platform", "产品不支持在指定销售平台上架"),
    ("The seller center is locked during shop integration, only editing stock and price is allowed",
     "店铺集成期间卖家中心被锁定，仅允许编辑库存和价格"),
    ("The product in its current status is not available for this operation. Change the product status and try again.",
     "产品当前状态不支持此操作。请更改产品状态后重试。"),
    ("Invalid input parameters. Refer to the API documentation for details.",
     "输入参数无效。请参阅 API 文档了解详情。"),
    ("SKU must contain a valid warehouse.", "SKU 必须包含有效仓库。"),
    ("The product ID does not exist", "产品 ID 不存在"),
    ("The product does not exist", "产品不存在"),
    ("publish param invalid", "发布参数无效"),
    ("All region shops must use V2 categories. Check the documentation for further details.",
     "所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。"),
    ("Batch activate business error.", "批量激活业务错误。"),
    ("You can't edit other sellers' products", "您无法编辑其他卖家的产品"),

    # Common validation/range descriptions
    ("Max length: 500 characters", "最大长度：500 个字符"),
    ("Max length: 999 characters", "最大长度：999 个字符"),
    ("Max length: 10,000 characters.", "最大长度：10,000 个字符。"),
    ("Max length: 20 characters", "最大长度：20 个字符"),
    ("Max length: 50 characters.", "最大长度：50 个字符。"),
    ("Max length: 2000 characters", "最大长度：2000 个字符"),
    ("Max count: 9", "最大数量：9"),
    ("Max count: 10", "最大数量：10"),
    ("Max number of IDs: 20", "最大 ID 数量：20"),
    ("Max number of image URIs: 8.", "最大图片 URI 数量：8。"),
    ("Max SKUs for BR, EU, JP, MX, UK, US: 300", "BR、EU、JP、MX、UK、US 的最大 SKU 数量：300"),
    ("Max SKUs for other regions: 100", "其他地区的最大 SKU 数量：100"),
    ("Valid range: [1, 99,999]", "有效范围：[1, 99,999]"),
    ("Valid range: [0.01, 99,999.9999]", "有效范围：[0.01, 99,999.9999]"),
    ("Valid range: [0.01, 7600]", "有效范围：[0.01, 7600]"),
    ("Valid range:", "有效范围："),
    ("Valid length:", "有效长度："),
    ("Supports two decimal places.", "支持两位小数。"),

    # Length validations
    ("* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 characters",
     "* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 个字符"),
    ("* Other regions: 1-50 characters", "* 其他地区: 1-50 个字符"),
    ("* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: Use alphabets, numbers, hyphens (-), or underscores (_) only",
     "* DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 仅使用字母、数字、连字符 (-) 或下划线 (_)"),
    ("* Other regions: Text without spaces", "* 其他地区: 不含空格的文本"),
    ("* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]", "* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]"),
    ("* BR, MX: [1, 300]", "* BR, MX: [1, 300]"),
    ("* Other regions: [25, 255]", "* 其他地区: [25, 255]"),
    ("* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]", "* DE, ES, FR, IE, IT, JP, UK, US: [1, 255]"),

    # Region-based values
    ("* US: CENTIMETER, INCH", "* US: CENTIMETER, INCH"),
    ("* Other regions: CENTIMETER", "* 其他地区: CENTIMETER"),
    ("* US: KILOGRAM, POUND", "* US: KILOGRAM, POUND"),
    ("* BR, JP, MX: KILOGRAM, GRAM", "* BR, JP, MX: KILOGRAM, GRAM"),
    ("* US: `KILOGRAM`, `POUND`", "* US: `KILOGRAM`, `POUND`"),
    ("* BR, JP, MX: `KILOGRAM`, `GRAM`", "* BR, JP, MX: `KILOGRAM`, `GRAM`"),
    ("* Other countries: KILOGRAM", "* 其他国家: KILOGRAM"),
    ("* Other countries: `KILOGRAM`", "* 其他国家: `KILOGRAM`"),
    ("* Other regions: v1, represents the 3-level category tree.Default: v1",
     "* 其他地区: v1，代表 3 级分类树。默认值：v1"),
    ("* US, EU and SEA: v2, represents the 7-level category tree.",
     "* US、EU 和 SEA: v2，代表 7 级分类树。"),
    ("Important: For US, EU and SEA shops, you must pass v2 when using this API.",
     "重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。"),

    # COD markets
    ("* Global sellers: MY, PH, SA, TH, VN", "* 全球卖家: MY, PH, SA, TH, VN"),
    ("* Local sellers: ID, MY, PH, SA, TH, VN", "* 本地卖家: ID, MY, PH, SA, TH, VN"),

    # Number format descriptions
    ("The number format varies based on the unit:", "数字格式因单位而异："),
    ("The number format varies based on the `unit`:", "数字格式因 `unit` 而异："),
    ("* GRAM: integer", "* GRAM: 整数"),
    ("* `GRAM`: integer", "* `GRAM`: 整数"),
    ("* KILOGRAM: up to 3 decimal places", "* KILOGRAM: 最多 3 位小数"),
    ("* `KILOGRAM`: up to 3 decimal places", "* `KILOGRAM`: 最多 3 位小数"),
    ("* POUND: up to 2 decimal places", "* POUND: 最多 2 位小数"),
    ("* `POUND`: up to 2 decimal places", "* `POUND`: 最多 2 位小数"),

    # GTIN format
    ("* GTIN: 14 digits", "* GTIN: 14 位数字"),
    ("GTIN: 14 digits", "GTIN: 14 位数字"),
    ("* EAN: 8, 13, or 14 digits", "* EAN: 8、13 或 14 位数字"),
    ("EAN: 8, 13, or 14 digits", "EAN: 8、13 或 14 位数字"),
    ("* UPC: 12 digits", "* UPC: 12 位数字"),
    ("UPC: 12 digits", "UPC: 12 位数字"),
    ("* ISBN: 13 digits, or 9 digits ending in capital `X`", "* ISBN: 13 位数字，或以大写 `X` 结尾的 9 位数字"),
    ("ISBN: 13 digits, or 9 digits ending in capital `X`", "ISBN: 13 位数字，或以大写 `X` 结尾的 9 位数字"),
    ("* JAN: 8 or 13 digits", "* JAN: 8 或 13 位数字"),

    # Pre-sale type descriptions
    ("* `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a release date.",
     "* `PRE_ORDER`: 产品尚未上市或发布。可以通过指定发布日期来延长履约时间。"),
    ("* `MADE_TO_ORDER`: The product is produced only after the order is received. Fulfillment can be extended by specifying a duration.",
     "* `MADE_TO_ORDER`: 产品在收到订单后才生产。可以通过指定持续时间来延长履约时间。"),
    ("* `CUSTOM`: The product requires a fulfillment timeline that exceeds the standard due to other factors. Fulfillment can be extended by specifying a duration.",
     "* `CUSTOM`: 由于其他因素，产品需要超出标准的履约时间线。可以通过指定持续时间来延长履约时间。"),
    ("* `PRE_ORDER`: The product is not yet available or released. Fulfillment can be extended by specifying a duration.",
     "* `PRE_ORDER`: 产品尚未上市或发布。可以通过指定持续时间来延长履约时间。"),
    ("* `MADE_TO_ORDER`: Business days, from 3 to 14 days.",
     "* `MADE_TO_ORDER`: 工作日，3 到 14 天。"),
    ("* `CUSTOM`: Business days, from 3 to 30 days.",
     "* `CUSTOM`: 工作日，3 到 30 天。"),
    ("* `PRE_ORDER`: Calendar days, from 3 to 30 days.",
     "* `PRE_ORDER`: 日历日，3 到 30 天。"),

    # AS_DRAFT/LISTING
    ("* AS_DRAFT: Save the product as a draft for future editing.",
     "* AS_DRAFT: 将产品保存为草稿以便将来编辑。"),
    ("* LISTING: Immediately list the product in the shop.",
     "* LISTING: 立即在店铺中上架产品。"),

    # TOKOPEDIA/TIKTOK_SHOP values
    ("* TOKOPEDIA", "* TOKOPEDIA"),
    ("* TIKTOK_SHOP", "* TIKTOK_SHOP"),

    # Fee attribute values
    ("* SINGLE_USE", "* SINGLE_USE"),
    ("* REUSABLE", "* REUSABLE"),
    ("* NOT_APPLICABLE", "* NOT_APPLICABLE"),
    ("Possible values: PFAND", "可能的值：PFAND"),

    # Check item values
    ("* SHOP_STATUS", "* SHOP_STATUS"),
    ("* SHOP_TAX", "* SHOP_TAX"),
    ("* PICKUP_WAREHOUSE", "* PICKUP_WAREHOUSE"),
    ("* RETURN_WAREHOUSE", "* RETURN_WAREHOUSE"),
    ("* DELIVERY_OPTION", "* DELIVERY_OPTION"),
    ("* SHIPPING_TEMPLATE", "* SHIPPING_TEMPLATE"),
    ("* PRODUCT_QUANTITY_LIMIT", "* PRODUCT_QUANTITY_LIMIT"),
    ("* EXTENDED_PRODUCER_RESPONSIBILITY", "* EXTENDED_PRODUCER_RESPONSIBILITY"),
    ("* BANk_ACCOUNT", "* BANk_ACCOUNT"),
    ("* CONTACT_INFO", "* CONTACT_INFO"),

    # Shipping insurance
    ("* REQUIRED: Shipping insurance is mandatory and buyers can't opt out.",
     "* REQUIRED: 运输保险为强制购买，买家无法取消。"),
    ("* OPTIONAL: Buyers can choose to purchase shipping insurance through the platform.",
     "* OPTIONAL: 买家可以选择通过平台购买运输保险。"),
    ("* NOT_SUPPORTED: Shipping insurance is not supported for the product.",
     "* NOT_SUPPORTED: 产品不支持运输保险。"),

    # SHOPIFY_COMPARE_AT_PRICE
    ("* SHOPIFY_COMPARE_AT_PRICE: The compare_at_price in Shopify.",
     "* SHOPIFY_COMPARE_AT_PRICE: Shopify 中的 compare_at_price。"),

    # PFAND range
    ("* PFAND: [0.00 - 6300.00]", "* PFAND: [0.00 - 6300.00]"),

    # Common bullet points
    ("* Provide the dimensions measured after packing the product.", "* 提供包装产品后测量的尺寸。"),
    ("* These values impact the shipping cost, so it is important to ensure that dimensions are accurate. Any discrepancies in measurements may lead to additional shipping fees.",
     "* 这些值会影响运费，因此确保尺寸准确很重要。任何测量差异都可能导致额外运费。"),
    ("* Optional for ID, TH, VN regions.", "* ID、TH、VN 地区为可选。"),
    ("* Provide the weight measured after packing the SKU.", "* 提供包装 SKU 后测量的重量。"),
    ("* Provide the weight measured after packing the product.", "* 提供包装产品后测量的重量。"),
    ("* Use the same measurement system for `sku_weight` and `sku_dimensions`; for example, use `KILOGRAM` with `CENTIMETER`.",
     "* `sku_weight` 和 `sku_dimensions` 使用相同的度量系统；例如，`KILOGRAM` 搭配 `CENTIMETER`。"),
    ("* Weight and dimensions can affect shipping costs, so ensure both are accurate. Shipping fees may use the higher of the actual weight and the volumetric weight calculated from the dimensions.",
     "* 重量和尺寸会影响运费，因此请确保两者准确。运费可能使用实际重量和根据尺寸计算的体积重量中的较高者。"),
    ("* Arrange your image URIs in the sequence that they should appear on TikTok Shop.",
     "* 按图片在 TikTok Shop 上的展示顺序排列图片 URI。"),
    ("* Applicable only for the US market.", "* 仅适用于美国市场。"),
    ("* Applicable only for the EU market.", "* 仅适用于欧盟市场。"),
    ("* The content must conform to the [HTML syntax]", "* 内容必须符合 [HTML 语法]"),
    ("* Max length: 10,000 characters.", "* 最大长度：10,000 个字符。"),
    ("* Image guidelines: You must use [TikTok Shop image URLs]", "* 图片指南：必须使用 [TikTok Shop 图片 URL]"),
    ("* If you are syncing a pre-existing description from another platform, include the full HTML source description here.",
     "* 如果您正在从其他平台同步预先存在的描述，请在此处包含完整的 HTML 源代码描述。"),
    ("* Provide a detailed description, ideally over 300 characters.", "* 提供详细描述，最好超过 300 个字符。"),
    ("* Include 3-5 key selling points, each under 250 characters, with supporting images.",
     "* 包含 3-5 个关键卖点，每个不超过 250 个字符，并附带支持图片。"),
    ("* Use 1600x1600 px for the image dimensions.", "* 图片尺寸使用 1600x1600 像素。"),
    ("* Use a minimum of 5 images.", "* 至少使用 5 张图片。"),
    ("* The first image should have a white background.", "* 第一张图片应有白色背景。"),
    ("* Do not include sensitive characters.", "* 不要包含敏感字符。"),
    ("* This is mainly used to calculate the unit price of the SKU", "* 这主要用于计算 SKU 的单价"),
    ("* This is the definitive final price shown on the product page, all other prices will be ignored.",
     "* 这是产品页面上显示的最终确定价格，所有其他价格将被忽略。"),
    ("* Required for JP and US shops using China warehouses, optional for others.",
     "* 对于使用中国仓库的 JP 和 US 店铺为必填，其他为可选。"),
    ("* All the products package weight is **mandatory by default**", "* 所有产品包装重量**默认为必填**"),
    ("* This value impacts the shipping cost, so it is important to ensure that the weight is accurate. Any discrepancies in measurements may lead to additional shipping fees.",
     "* 此值会影响运费，因此确保重量准确很重要。任何测量差异都可能导致额外运费。"),
    ("* The package weight will take precedence over package dimensions in fee calculation if the fee based on weight is higher.",
     "* 如果基于重量的费用更高，则包装重量将在费用计算中优先于包装尺寸。"),
    ("* Max number of image URIs: 8.", "* 最大图片 URI 数量：8。"),

    # Longer paragraph translations
    ("This is used to associate the SKU between TikTok Shop and the external ecommerce platform.",
     "这用于在 TikTok Shop 和外部电商平台之间关联 SKU。"),
    ("This is used to associate the product between TikTok Shop and the external ecommerce platform.",
     "这用于在 TikTok Shop 和外部电商平台之间关联产品。"),
    ("Add this property if you have products listed on third-party sites other than TikTok Shop and would like to map them.",
     "如果您在 TikTok Shop 以外的第三方网站上架了产品并希望进行映射，请添加此属性。"),
    ("Provide this field as a JSON array of URL strings.", "将此字段作为 URL 字符串的 JSON 数组提供。"),
    ("Max string length: 500", "最大字符串长度：500"),

    # Note blocks
    ("Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the nearest whole number.",
     "注意：对于 BR 市场，也接受使用 . 或 , 作为分隔符的十进制值，但将四舍五入到最接近的整数。"),
    ("**Note**: For the BR market, decimal values using `.` or `,` as separators are also accepted but will be rounded to the nearest whole number.",
     "**注意**：对于 BR 市场，也接受使用 `.` 或 `,` 作为分隔符的十进制值，但将四舍五入到最接近的整数。"),
    ("Note: Use the same measurement system (metric or imperial) for `sku_weight` and `sku_dimensions`. For example, use `KILOGRAM` with `CENTIMETER`.",
     "注意：`sku_weight` 和 `sku_dimensions` 使用相同的度量系统（公制或英制）。例如，`KILOGRAM` 搭配 `CENTIMETER`。"),
    ("Note: This quantity specifically refers to the in-stock inventory that can be shipped immediately.",
     "注意：此数量特指可以立即发货的有库存的库存量。"),

    # Strikethrough price note
    ("**Note**: This value may appear as the strikethrough price on the product page. However, whether the strikethrough price is shown and the amount shown are subject to the audit team's review and decision based on various pricing information.",
     "**注意**：此值可能显示为产品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。"),

    # Various longer descriptions
    ("The SKU's **local display price** shown on the product page before any discounts.",
     "SKU 在产品页面上折扣前显示的**本地展示价格**。"),
    ("The SKU's **local display price** shown on the product page before any discounts. Refer to [Product Pricing]",
     "SKU 在产品页面上折扣前显示的**本地展示价格**。参考 [Product Pricing]"),
    ("for the allowed price ranges in each market.", "了解各市场允许的价格范围。"),

    ("A list of results from checking whether a shop satisfies TikTok Shop requirements.",
     "检查店铺是否满足 TikTok Shop 要求的结果列表。"),
    ("A regulated identifier code assigned to a product based on international standardized regulations (e.g. GTIN) to ensure the product is universally identifiable across various platforms and systems.",
     "根据国际标准化法规（如 GTIN）分配给产品的受管标识码，以确保产品在各种平台和系统中可普遍识别。"),
    ("If this SKU belongs to a virtual bundle, this object contains the list of individual SKUs that form the bundle (e.g. gift basket, starter pack).",
     "如果此 SKU 属于虚拟套装，此对象包含组成套装的单个 SKU 列表（如礼品篮、入门套装）。"),
    ("If this SKU belongs to a virtual bundle (containing multiple individual SKUs), you can add up to 10 additional identifier codes here for the SKUs included in the bundle.",
     "如果此 SKU 属于虚拟套装（包含多个单独 SKU），您可以在此处为套装中包含的 SKU 添加最多 10 个额外标识码。"),
    ("The ID of the source product included in the virtual bundle.", "虚拟套装中包含的源产品 ID。"),
    ("The ID of the source SKU included in the virtual bundle.", "虚拟套装中包含的源 SKU ID。"),
    ("The quantity of the source SKU included in the virtual bundle.", "虚拟套装中包含的源 SKU 数量。"),
    ("The total quantity/volume of the product represented by the SKU.", "SKU 代表的产品总量/体积。"),
    ("For example, if the SKU represents 500ml of water, this value would be 500 if the unit type is defined as ml.",
     "例如，如果 SKU 代表 500 毫升水，则当单位类型定义为 ml 时，此值将为 500。"),

    # Pre-sale descriptions
    ("SKU presale information, used to tag a product as a presale product based on its presale type. Omit this object if the product is a regular item.",
     "SKU 预售信息，用于根据预售类型将产品标记为预售产品。如果产品是常规商品，请省略此对象。"),
    ("Information about the type of pre-sale order fulfillment and the corresponding timeframe.",
     "关于预售订单履约类型及相应时间范围的信息。"),
    ("* `handling_duration_days` is for fulfillment with an extended duration.",
     "* `handling_duration_days` 用于延长持续时间的履约。"),
    ("* `handling_duration_days` is for starting fulfillment on a fixed date.",
     "* `handling_duration_days` 用于在固定日期开始履约。"),
    ("* `release_date` is for starting fulfillment on a fixed date.",
     "* `release_date` 用于在固定日期开始履约。"),

    # Release date description
    ("The date on which the product gets converted into a regular product and becomes available for general purchase. On this date, order handling will also start, changing the status of the order to [AWAITING_SHIPMENT]",
     "产品转换为常规产品并可公开购买的日期。在此日期，订单处理也将开始，将订单状态更改为 [AWAITING_SHIPMENT]"),
    ("The desired duration for handling a pre-sale order and handing it over to a shipping carrier.",
     "处理预售订单并移交承运商所需的期望持续时间。"),

    # List price descriptions
    ("The SKU's list price information. This is equivalent to the manufacturer's suggested retail price (MSRP), or the recommended retail price (RRP).",
     "SKU 的标价信息。这等同于制造商建议零售价（MSRP）或建议零售价（RRP）。"),
    ("The SKU list price (e.g. MSRP, RRP) or original price information on external ecommerce platforms.",
     "SKU 标价（如 MSRP、RRP）或外部电商平台上的原价信息。"),

    # Fee descriptions
    ("The fees required for this product based on TikTok Shop policies. Fees are required only for certain product categories, retrieve the requirements from the [Get Category Rules API]",
     "根据 TikTok Shop 政策此产品所需的费用。仅某些产品分类需要费用，从 [Get Category Rules API] 获取要求"),

    # Category descriptions
    ("The ID of the category of this product. It must be a leaf category that corresponds to the category tree type specified in the `category_version` property.",
     "此产品的分类 ID。必须是与 `category_version` 属性中指定的分类树类型对应的叶子分类。"),
    ("The ID of a leaf category for this product.", "此产品的叶子分类 ID。"),

    # Image descriptions
    ("A list of images to display in the product image gallery.", "在产品图片库中展示的图片列表。"),
    ("The default/main image for each value (e.g. red) of the primary sales attribute (e.g. color). This appears in the product options gallery on TikTok Shop.",
     "主要销售属性（如颜色）每个值（如红色）的默认/主图片。此图片显示在 TikTok Shop 的产品选项库中。"),
    ("A list of supplementary images for each value (e.g. red) of the primary sales attribute (e.g. color) to provide multiple views or details of the product for that attribute value. These appear in the product options gallery on TikTok Shop.",
     "主要销售属性（如颜色）每个值（如红色）的补充图片列表，用于提供该产品属性值的多角度视图或详情。这些图片显示在 TikTok Shop 的产品选项库中。"),
    ("You can attach images to only 1 type of sales attribute, which will serve as the primary attribute for display. An image must be provided for each value of the primary attribute.",
     "您只能将图片附加到 1 种类型的销售属性上，该属性将作为展示的主要属性。必须为主要属性的每个值提供图片。"),
    ("An image must be provided for each value of the primary attribute. For example, if a product has 2 colors and 3 sizes, you can choose to attach images to the Color attribute, in which case an image must be provided for each of the 2 color values.",
     "必须为主要属性的每个值提供图片。例如，如果产品有 2 种颜色和 3 种尺码，您可以选择将图片附加到颜色属性，在这种情况下，必须为 2 个颜色值各提供一张图片。"),

    # Size chart descriptions
    ("A TikTok Shop size chart template generated by the size chart tool in Seller Center > Manage Products > Bulk action > Batch manage size charts.",
     "由卖家中心 > 管理产品 > 批量操作 > 批量管理尺码表中的尺码表工具生成的 TikTok Shop 尺码表模板。"),

    # Product description notes
    ("All HTML tags are accepted but to optimize display on the TikTok Shop product detail page, the system will automatically convert certain tags into alternative formats, such as rendering",
     "所有 HTML 标签都被接受，但为了优化在 TikTok Shop 产品详情页上的展示，系统会自动将某些标签转换为替代格式，例如将"),
    ("tags as images.", "标签渲染为图片。"),
    ("tags into alternative formats, such as rendering `<table>` tags as images.", "标签转换为替代格式，例如将 `<table>` 标签渲染为图片。"),

    # Category restriction notes
    ("Refer to TikTok Shop Academy for information on product category restrictions.", "有关产品分类限制的信息，请参考 TikTok Shop Academy。"),
    ("Unauthorized brands won't be displayed on TikTok Shop.", "未经授权的品牌不会在 TikTok Shop 上显示。"),

    # Main image notes
    ("Use the [Optimize Images API]", "使用 [Optimize Images API]"),
    ("to change the background to white.", "将背景更改为白色。"),
    ("to change the background to white", "将背景更改为白色"),

    # Sales attributes notes
    ("You can omit this object if there is only 1 SKU. Otherwise, this is **required**.",
     "如果只有 1 个 SKU，则可以省略此对象。否则为**必填**。"),
    ("You can only have up to 3 types of sales attributes per product.", "每个产品最多只能有 3 种销售属性类型。"),
    ("Each SKU must include the same number and type of sales attributes.", "每个 SKU 必须包含相同数量和类型的销售属性。"),
    ("Provide either a built-in ID or a custom name; if both are provided, the ID takes priority.",
     "提供内置 ID 或自定义名称；如果同时提供，则 ID 优先。"),

    # Identifier code notes
    ("**Note**: The identifier code must be unique for each SKU, with no repetition allowed.",
     "**注意**：标识码必须在每个 SKU 中唯一，不允许重复。"),
    ("* The identifier code must be unique for each SKU, with no repetition allowed.",
     "* 标识码必须在每个 SKU 中唯一，不允许重复。"),
    ("The identifier code must be unique for each SKU, with no repetition allowed.",
     "标识码必须在每个 SKU 中唯一，不允许重复。"),

    # COD notes
    ("**Note**: If COD is not supported, the listing will fail if you set this to `true`.",
     "**注意**：如果不支持 COD，将此设置为 `true` 将导致上架失败。"),

    # Size chart notes
    ("* For certain product categories, size charts may be required or not supported.",
     "* 对于某些产品分类，可能需要或不支持尺码表。"),
    ("* If size charts are not supported, even if you provide a size chart here, the size chart will not be saved.",
     "* 如果不支持尺码表，即使您在此处提供尺码表，也不会保存。"),
    ("* Provide either a TikTok Shop size chart template ID or a size chart image; if both are provided, the ID takes priority.",
     "* 提供 TikTok Shop 尺码表模板 ID 或尺码表图片；如果同时提供，则 ID 优先。"),

    # Package weight notes
    ("except for products under **Virtual Products** categories.", "（**虚拟产品**分类下的产品除外）。"),
    ("e.g **Digital Games**.", "例如**数字游戏**。"),

    # Measurement system notes
    ("**Note**: You must use the same system of measurement (metric system or imperial system) for `package_weight` and `package_dimensions`. In other words, if you are using `KILOGRAM` for the weight, you must use `CENTIMETER` for the dimensions.",
     "**注意**：`package_weight` 和 `package_dimensions` 必须使用相同的度量系统（公制或英制）。换言之，如果重量使用 `KILOGRAM`，则尺寸必须使用 `CENTIMETER`。"),

    # Attributes note
    ("**Important**: The attributes available for use are determined by the system based on the product's assigned category, with some being mandatory.",
     "**重要**：可用的属性由系统根据产品分配的分类确定，其中一些是必填的。"),
    ("You must provide the product attributes marked as `is_required` in the response of the [Get Attributes API]",
     "您必须提供 [Get Attributes API] 响应中标记为 `is_required` 的产品属性"),

    # Pre-sale notes
    ("**Note**: Provide either the `handling_duration_days` or the `release_date`, depending on the value of `pre_sale.type` and your shop's region.",
     "**注意**：根据 `pre_sale.type` 的值和您店铺所在的地区，提供 `handling_duration_days` 或 `release_date`。"),
    ("Applicable only for `PRE_ORDER` in the US.", "仅适用于美国的 `PRE_ORDER`。"),
    ("* Regular / Preorder product: Once the product goes live, you cannot change the product type.",
     "* 常规/预售产品：产品上架后，您无法更改产品类型。"),
    ("* Made-to-order product: You can change it to a regular product at any time.",
     "* 按需生产产品：您可以随时将其更改为常规产品。"),

    # Release date notes
    ("* Valid range: The date must fall within 3 - 60 days from the current date.",
     "* 有效范围：日期必须在当前日期的 3 到 60 天内。"),
    ("* This date is a unix timestamp (seconds) based on the seller-selected timezone in Seller Center.",
     "* 此日期是基于卖家中心中卖家选择的时区的 Unix 时间戳（秒）。"),
    ("* This date cannot be modified once the product goes live.",
     "* 产品上架后无法修改此日期。"),

    # List price notes
    ("**Note**: The value must be equal to or greater than `skus.price.amount`. Otherwise, it will be discarded.",
     "**注意**：该值必须等于或大于 `skus.price.amount`。否则将被丢弃。"),

    # Backorder notes
    ("* For non-virtual product categories, provide `backorder_quantity` and `handling_time` together.",
     "* 对于非虚拟产品分类，请同时提供 `backorder_quantity` 和 `handling_time`。"),
    ("* Made-to-order (MTO), pre-order, and custom products cannot be backordered and are incompatible with `backorder_quantity`.",
     "* 按需生产（MTO）、预售和定制产品不支持缺货订购，且不兼容 `backorder_quantity`。"),

    # External URLs description
    ("The seller center is locked during shop integration, only editing stock and price is allowed",
     "店铺集成期间卖家中心被锁定，仅允许编辑库存和价格"),

    # Certification descriptions
    ("As per TikTok Shop guidelines, certifications are required for certain restricted product categories.",
     "根据 TikTok Shop 指南，某些受限产品分类需要认证。"),
    ("Retrieve the certification requirements for your", "获取您的"),
    ("This field may be required for certain certifications.", "某些认证可能需要此字段。"),

    # Product description recommendations
    ("**Note**:", "**注意**："),

    # Size chart image recommendations
    ("* Resolution: Minimum 1024px on the shorter side", "* 分辨率：较短边最小 1024 像素"),
    ("* Content: Include key measurement dimensions (e.g., bust, waist, hips, inseam), the more the better.",
     "* 内容：包含关键测量尺寸（如胸围、腰围、臀围、内缝），越多越好。"),
    ("* Format: Use a table with distinct columns and row.", "* 格式：使用具有明显列和行的表格。"),
    ("* Use only one table per product and image.", "* 每个产品和图片仅使用一个表格。"),
    ("* Display each dimension in a separate row.", "* 在单独的行中显示每个尺寸。"),
    ("* Display units in column headers.", "* 在列标题中显示单位。"),

    # Permission statuses
    ("* `AVAILABLE`: None of the category-permission restrictions listed below applies to this category.",
     "* `AVAILABLE`: 下面列出的分类权限限制均不适用于此分类。"),
    ("* `INVITE_ONLY`: This is a restricted category and you do not have permission to use it.",
     "* `INVITE_ONLY`: 这是受限分类，您没有使用权限。"),
    ("* `NON_MAIN_CATEGORY`: This category is out of scope for this shop, and you do not have permission to use it.",
     "* `NON_MAIN_CATEGORY`: 此分类超出此店铺的范围，您没有使用权限。"),
    ("* `PROHIBITED`: This category is prohibited on TikTok Shop.",
     "* `PROHIBITED`: 此分类在 TikTok Shop 上被禁止。"),

    # Various "to" phrases
    ("to obtain the unit price, you would also need to define the", "要获取单价，您还需要定义"),
    ("and the", "和"),
    ("product attributes.", "产品属性。"),
    ("Retrieve the relevant information for these pro", "获取这些产品属性的相关信息"),

    # External product ID description
    ("The SKU's **local display price** shown on the product page before any discounts", "SKU 在产品页面上折扣前显示的**本地展示价格**"),

    # For the root category
    ("For the root category, the parent ID is `0`.", "对于根分类，父 ID 为 `0`。"),

    # Indicates how the product should be saved
    ("Indicates how the product should be saved.", "指示产品应如何保存。"),

    # For Indonesia market
    ("**For the Indonesia market**: To list a product on both TikTok Shop and Tokopedia, use only categories available on both platforms.",
     "**对于印度尼西亚市场**：要在 TikTok Shop 和 Tokopedia 上架产品，请仅使用两个平台上都可用的分类。"),
    ("Call this API once with `listing_platform` set to `TIKTOK_SHOP` and once with it set to `TOKOPEDIA`, then identify the categories returned by both calls.",
     "将此 API 调用一次，`listing_platform` 设置为 `TIKTOK_SHOP`，再调用一次，设置为 `TOKOPEDIA`，然后识别两次调用返回的共同分类。"),

    # is_live_quick descriptions
    ("false — NORMAL products", "false — 常规产品"),
    ("true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.",
     "true — LIVE_QUICK 产品。只有具有所需权限的卖家才能创建 LIVE_QUICK 产品。"),

    # Set this to true
    ("Set this to `true` to identify which are the product categories that you can't list on TikTok Shop in any circumstances.",
     "将其设置为 `true` 以识别在任何情况下都无法在 TikTok Shop 上架的产品分类。"),

    # include_prohibited_categories
    ("Applicable only for BR, MX, EU and SEA markets.", "仅适用于 BR、MX、EU 和 SEA 市场。"),

    # For the US market
    ("For the US market, if you are creating products in `INVITE_ONLY` categories, you must submit a separate application through the Qualification Center on TikTok Shop Seller Center to gain access.",
     "对于美国市场，如果您正在 `INVITE_ONLY` 分类中创建产品，您必须通过 TikTok Shop 卖家中心的资质中心提交单独的申请以获得访问权限。"),
    ("Otherwise, even if the product audit is passed, the product will not be listed and made available to buyers.",
     "否则，即使产品审核通过，产品也不会被上架并可供买家购买。"),
    ("(The product status will be `PENDING` and the audit status will be `PRE_APPROVED`)",
     "（产品状态将为 `PENDING`，审核状态将为 `PRE_APPROVED`）"),

    # For the Indonesia market (longer)
    ("For the Indonesia market, to list a product on both TikTok Shop and Tokopedia, you must use only categories that are available on both platforms.",
     "对于印度尼西亚市场，要在 TikTok Shop 和 Tokopedia 上架产品，您必须仅使用两个平台上都可用的分类。"),

    # Note about product content language
    ("The language used in the product content must align with the target market's language", "产品内容中使用的语言必须与目标市场的语言一致"),

    # Tip about running check
    ("We recommend that you run this check before any bulk updates to avoid listing issues.",
     "我们建议您在任何批量更新之前运行此检查，以避免上架问题。"),
    ("For example, sellers may change the delivery option to", "例如，卖家可能将配送选项更改为"),
    ("but fail to add a shipping template, thus blocking the shop from listing products.",
     "但未添加运费模板，从而阻止店铺上架产品。"),

    # Additional common phrases
    ("The custom delivery option IDs to apply to this product if you want to override the default warehouse delivery options.",
     "如果您想覆盖默认仓库配送选项，则应用于此产品的自定义配送选项 ID。"),
    ("To retrieve the available options, use the", "要获取可用选项，请使用"),
    ("Leave this field blank to inherit the default delivery options configured for the warehouse.",
     "将此字段留空以继承为仓库配置的默认配送选项。"),
    ("If this product is associated with a virtual bundle, this value is the ID of the primary",
     "如果此产品关联虚拟套装，此值是主要"),
    ("product in the bundle.", "套装中的产品 ID。"),
    ("Required only for virtual bundle products.", "仅虚拟套装产品需要。"),
    ("Applicable only for the EU market in certain categories.", "仅适用于欧盟市场的特定分类。"),
    ("Use the [Get Category Rules API]", "使用 [Get Category Rules API]"),
    ("to check the requirements.", "检查要求。"),

    # Note about same measurement system
    ("You must use the same system of measurement (metric system or imperial system)", "您必须使用相同的度量系统（公制或英制）"),

    # Product description guidelines
    ("Please check the measurements before purchase.", "请在购买前检查尺寸。"),

    # Additional image guidelines
    ("Max 30 `<img>` tags, each under 4000px with `src`, `width`, and `height` attributes.",
     "最多 30 个 `<img>` 标签，每个不超过 4000px，带有 `src`、`width` 和 `height` 属性。"),

    # Use case descriptions
    ("with `use_case=MAIN_IMAGE`.", "使用 `use_case=MAIN_IMAGE`。"),
    ("with `use_case=ATTRIBUTE_IMAGE`.", "使用 `use_case=ATTRIBUTE_IMAGE`。"),
    ("with `use_case=CERTIFICATION_IMAGE`.", "使用 `use_case=CERTIFICATION_IMAGE`。"),
    ("with `use_case=SIZE_CHART_IMAGE`.", "使用 `use_case=SIZE_CHART_IMAGE`。"),
    ("You can use the returned URI directly, or process it through the", "您可以直接使用返回的 URI，或者通过"),
    ("first and use the resulting URI.", "处理后再使用生成的 URI。"),

    # External identifier code
    ("An external identifier used in an external ecommerce platform.", "在外部电商平台中使用的外部标识符。"),

    # Set this field to true together with
    ("Set this field to `true` together with a nonempty `gne_async_check_session_id` to start new asynchronous checks.",
     "将此字段设置为 `true` 并与非空的 `gne_async_check_session_id` 一起使用以启动新的异步检查。"),
    ("To retry retrieval with the same session ID without creating new asynchronous tasks, set this field to `false`; any completed findings are returned in",
     "要在不创建新异步任务的情况下使用相同会话 ID 重试检索，请将此字段设置为 `false`；任何已完成的发现将在"),
    ("Whether to trigger asynchronous product information verification. This asynchronous workflow is availab",
     "是否触发异步产品信息验证。此异步工作流可用"),

    # For the root category note
    ("For the root category, the parent ID is", "对于根分类，父 ID 为"),

    # Various "Applicable only" variations
    ("Applicable only for sellers that migrated from Tokopedia", "仅适用于从 Tokopedia 迁移的卖家"),
    ("Applicable only for the EU market", "仅适用于欧盟市场"),
    ("Applicable only for global sellers", "仅适用于全球卖家"),
    ("Applicable only for US local sellers", "仅适用于美国本地卖家"),
    ("Applicable only for the Indonesia market", "仅适用于印度尼西亚市场"),

    # The `id/name` and `value_id/value_name` pairs
    ("The `id/name` and `value_id/value_name` pairs must be unique in each SKU.",
     "`id/name` 和 `value_id/value_name` 对在每個 SKU 中必须唯一。"),
    ("For example, you cannot have one SKU that has only a Color attribute, while another SKU has both Color and Size attributes.",
     "例如，不能一个 SKU 只有颜色属性，而另一个 SKU 同时有颜色和尺码属性。"),
    ("For example, you cannot repeat", "例如，不能重复"),
    ("in different SKUs.", "在不同的 SKU 中。"),

    # Unit price note
    ("and is required only if you wish to display the unit price to facilitate easier price comparisons across different products and packaging sizes.",
     "仅当您希望展示单价以便于跨不同产品和包装尺寸进行价格比较时才需要。"),
    ("Unit price = Selling price/(SKU unit count/base unit count). Therefore if you want to obtain the unit price, you would also need to define the",
     "单价 = 售价/(SKU 单位数量/基本单位数量)。因此，如果要获取单价，您还需要定义"),
    ("and the", "和"),
    ("product attributes. Retrieve the relevant information for these properties from the",
     "产品属性。从以下位置获取这些属性的相关信息"),

    # Various additional descriptions
    ("The estimated number of working days needed for a backorder to be shipped.", "缺货订购发货所需的预计工作日数。"),
    ("For non-virtual product categories, provide `handling_time` and `backorder_quantity` together.",
     "对于非虚拟产品分类，请同时提供 `handling_time` 和 `backorder_quantity`。"),
    ("All warehouses for the same SKU must use the same `handling_time`.",
     "同一 SKU 的所有仓库必须使用相同的 `handling_time`。"),
    ("The `backorder_quantity` will automatically be converted to `quantity` once in-stock inventory is sold out.",
     "一旦有库存售罄，`backorder_quantity` 将自动转换为 `quantity`。"),
    ("The fulfillment of this inventory follows the `handling_time` specified below.",
     "此库存的履约遵循以下指定的 `handling_time`。"),

    # A flag to indicate whether to return
    ("A flag to indicate whether to return the listing quality information (US only) and optimization diagnosis results for the product.",
     "标识是否返回产品的上架质量信息（仅限美国）和优化诊断结果的标志。"),
    ("If this is set to `false`, the response body will exclude the `listing_quality` and `diagnoses` objects.",
     "如果设置为 `false`，响应体将排除 `listing_quality` 和 `diagnoses` 对象。"),

    # Set this field to true
    ("Set this field to `true` to enable the listing quality diagnosis.",
     "将此字段设置为 `true` 以启用上架质量诊断。"),

    # Note about pre-owned products
    ("To list pre-owned products on the TikTok Shop platform, please specify the ID of one of the designated pre-owned product categories",
     "要在 TikTok Shop 平台上架二手产品，请指定指定二手产品分类之一的 ID"),

    # Additional phrases
    ("The URI of the image. Retrieve the URI from the [Upload Product Image API]", "图片的 URI。从 [Upload Product Image API] 获取 URI"),
    ("The URI of the image. Retrieve the URI from the", "图片的 URI。从以下位置获取 URI"),
    ("Upload Product Image API", "Upload Product Image API"),
    ("to get the list of available warehouses for your shop.", "获取您店铺的可用仓库列表。"),

    # For more info
    ("For more information", "有关更多信息"),
    ("for the allowed price ranges", "了解允许的价格范围"),
    ("in each market.", "在各市场中。"),

    # Additional common patterns
    ("This appears in the product options gallery on TikTok Shop.", "此图片显示在 TikTok Shop 的产品选项库中。"),
    ("These appear in the product options gallery on TikTok Shop.", "这些图片显示在 TikTok Shop 的产品选项库中。"),
    ("These appear in the product", "这些显示在产品"),

    # Use the Optimize Images API to
    ("Use the [Optimize Images API](665692b35d39dc02deb49a97) to", "使用 [Optimize Images API](665692b35d39dc02deb49a97)"),

    # Image dimension notes
    ("Image dimensions: [300x300 px, 4000x4000 px]", "图片尺寸：[300x300 像素, 4000x4000 像素]"),

    # Obtain this URI by uploading
    ("Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22)",
     "通过 [Upload Product Image API](6509df95defece02be598a22) 上传图片获取此 URI"),
    ("Obtain this URI by uploading the images through the [Upload Product Image API]",
     "通过 [Upload Product Image API] 上传图片获取此 URI"),

    # Use the Upload Product Image API to upload
    ("Use the [Upload Product Image API](6509df95defece02be598a22) to upload the video first and obtain the corresponding",
     "先使用 [Upload Product Image API](6509df95defece02be598a22) 上传视频获取相应的"),
    ("Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload the video first and obtain the corresponding",
     "先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传视频获取相应的"),
    ("Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload the files first and obtain the corresponding",
     "先使用 [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) 上传文件获取相应的"),

    # Obtain this URI by uploading the images
    ("Obtain this URI by uploading", "通过上传获取此 URI"),

    # For example
    ("For example, if a product has 2 colors and 3 sizes, you can choose to attach images to the Color attribute, in which case an image must be provided for each of the 2 color values.",
     "例如，如果产品有 2 种颜色和 3 种尺码，您可以选择将图片附加到颜色属性，在这种情况下，必须为 2 个颜色值各提供一张图片。"),
    ("For example, use", "例如，使用"),

    # The product title
    ("The product title.", "产品标题。"),
    ("Title length:", "标题长度："),

    # Various additional patterns
    ("The URI of the size chart image.", "尺码表图片的 URI。"),
    ("The URI of the certification image.", "认证图片的 URI。"),

    # Additional inline fixes
    ("You can use the returned URI directly, or process it through the [Optimize Images API]",
     "您可以直接使用返回的 URI，或通过 [Optimize Images API]"),
    ("first and use the resulting URI.", "处理后再使用生成的 URI。"),

    # "corresponding" translations
    ("and obtain the corresponding image URI.", "并获取相应的图片 URI。"),
    ("and obtain the corresponding file ID.", "并获取相应的文件 ID。"),
    ("and obtain the corresponding", "并获取相应的"),

    # Product description field
    ("The product description in HTML format.", "HTML 格式的产品描述。"),
    ("HTML 格式的产品描述。", "HTML 格式的产品描述。"),

    # Various remaining patterns
    ("The usage scenario of the image.", "图片的使用场景。"),
    ("The name of the file, including the file extension", "文件名称，包括文件扩展名"),
    ("The local image file to be uploaded.", "要上传的本地图片文件。"),
    ("The local file to be uploaded.", "要上传的本地文件。"),

    # The height/width of the image
    ("The height of the image after aspect ratio adjustment.", "调整宽高比后的图片高度。"),
    ("The width of the image after aspect ratio adjustment.", "调整宽高比后的图片宽度。"),
    ("The usage scenario specified during upload.", "上传时指定的使用场景。"),

    # Pass this value
    ("Pass this value when creating or editing a product to associate the image with the product.",
     "在创建或编辑产品时传递此值以将图片与产品关联。"),
    ("Pass this value when creating or editing a product to associate the file with the product.",
     "在创建或编辑产品时传递此值以将文件与产品关联。"),

    # The URI of the image
    ("The URI of the image.", "图片的 URI。"),
    ("The URL to access and view the image.", "访问和查看图片的 URL。"),
    ("The URL of the image.", "图片的 URL。"),
    ("The original URI of the image.", "图片的原始 URI。"),
    ("The original URL of the image.", "图片的原始 URL。"),

    # Additional inline patterns
    ("The ID of the product that could not be activated.", "无法激活的产品 ID。"),
    ("The errors for individual products that could not be activated.", "无法激活的单个产品的错误。"),
    ("Check this list even when the top-level", "即使顶级"),
    ("is `0`.", "为 `0` 也请检查此列表。"),

    # The main error
    ("The main error code.", "主要错误代码。"),
    ("The main error message.", "主要错误消息。"),
    ("The details of the main error.", "主要错误的详细信息。"),
    ("A list of further nested errors or issues related to the main error.", "与主要错误相关的进一步嵌套错误或问题列表。"),
    ("The secondary error code.", "次要错误代码。"),
    ("The secondary error message.", "次要错误消息。"),

    # The success or failure
    ("The success or failure status code returned in API response.", "API 响应中返回的成功或失败状态码。"),
    ("The success or failure messages returned in API response. Reasons of failure will be described in the message.",
     "API 响应中返回的成功或失败消息。失败原因将在消息中描述。"),

    # Request log
    ("Request log", "请求日志"),
    ("Specific return information", "具体返回信息"),

    # Allowed type
    ("Allowed type: application/json", "允许类型：application/json"),
    ("Allowed type: multipart/form-data", "允许类型：multipart/form-data"),

    # Additional remaining phrases
    ("The listing platforms where the product will be activated.", "产品将被激活的上架平台。"),
    ("The product IDs to activate.", "要激活的产品 ID。"),
    ("The number of results to be returned per page.", "每页返回的结果数量。"),

    # An opaque token
    ("An opaque token used to retrieve the next page of a paginated result set.",
     "用于获取分页结果集下一页的不透明 token。"),
    ("Retrieve this value from the result of the", "从上一次响应的"),
    ("from a previous response. It is not needed for the first page.", "结果中获取此值。第一页不需要此值。"),
    ("If this value is non-empty, pass it in the", "如果此值非空，请将其传递给下一个请求的"),
    ("parameter of the next request. An empty value means there are no more results.", "参数。空值表示没有更多结果。"),

    # Brand related
    ("The total count of brands that meet the query conditions.", "符合查询条件的品牌总数。"),
    ("The list of brands that meet the query conditions.", "符合查询条件的品牌列表。"),
    ("The list of categories that meet the query conditions.", "符合查询条件的分类列表。"),
    ("The category ID.", "分类 ID。"),
    ("The parent category ID.", "父分类 ID。"),
    ("The category name in the requested locale.", "请求语言环境中的分类名称。"),
    ("If omitted, the default locale of your shop is used.", "如果被省略，则使用您店铺的默认语言环境。"),
    ("A flag to indicate if the category is a leaf category.", "标识该分类是否为叶子分类的标志。"),
    ("You can only create or edit products that belong to a leaf category.", "您只能创建或编辑属于叶子分类的产品。"),
    ("The shop's permission statuses for this category.", "该店铺的此分类权限状态。"),
    ("The shop's permission status for this category.", "该店铺的此分类权限状态。"),

    # Category hierarchy
    ("The category hierarchy for the recommended leaf category, ordered from the top-level category to the leaf category.",
     "推荐叶子分类的分类层级，从顶级分类到叶子分类排序。"),
    ("The recommended category ID. This is always a leaf category.", "推荐的分类 ID。这始终是叶子分类。"),
    ("The category level.", "分类级别。"),
    ("The category name.", "分类名称。"),

    # Filter categories
    ("Filter categories by this keyword in", "使用此关键词过滤分类"),
    ("Filter categories by the category tree version.", "按分类树版本过滤分类。"),
    ("Filter categories by the specified platform.", "按指定平台过滤分类。"),
    ("A flag to indicate whether to include categories that are prohibited on TikTok Shop.",
     "标识是否包含 TikTok Shop 禁止的分类。"),
    ("The BCP-47 locale codes for displaying category information.", "用于显示分类信息的 BCP-47 语言环境代码。"),
    ("The BCP-47 locale codes for displaying the size charts.", "用于显示尺码表的 BCP-47 语言环境代码。"),
    ("The default locale of your shop.", "您店铺的默认语言环境。"),

    # Brand
    ("The ID of the brand of this product.", "此产品的品牌 ID。"),
    ("The brand name.", "品牌名称。"),
    ("The name of the brand.", "品牌名称。"),
    ("The brand ID.", "品牌 ID。"),
    ("A unique ID that identifies the brand in TikTok Shop.", "在 TikTok Shop 中标识品牌的唯一 ID。"),
    ("A status to indicate whether the seller has obtained prior authorization to sell goods bearing the brand's trademark, name, or logo.",
     "标识卖家是否已获得事先授权销售带有品牌商标、名称或标志的商品的状态。"),
    ("A flag to indicate whether the brand is a T1 brand", "标识该品牌是否为 T1 品牌的标志"),
    ("which refers to internationally renowned brands that may have compliance risks and require sellers to obtain brand authorization.",
     "T1 品牌是指可能存在合规风险并要求卖家获得品牌授权的国际知名品牌。"),

    # Product type/vendor/tags
    ("The product type defined on the source platform.", "在源平台上定义的产品类型。"),
    ("The product vendor or brand name on the source platform.", "源平台上的产品供应商或品牌名称。"),
    ("Tags associated with the product on the source platform.", "与源平台上产品关联的标签。"),
    ("Category information assigned to the product on the source platform.", "在源平台上分配给产品的分类信息。"),
    ("The category ID on the source platform.", "源平台上的分类 ID。"),
    ("The category name on the source platform.", "源平台上的分类名称。"),
    ("The full category path or full category name on the source platform.", "源平台上的完整分类路径或完整分类名称。"),
    ("Whether the category is a leaf category.", "该分类是否为叶子分类。"),
    ("Whether the category is a root category.", "该分类是否为根分类。"),
    ("Additional product metadata provided by the source platform.", "源平台提供的额外产品元数据。"),
    ("A list of product metadata attributes and their values.", "产品元数据属性及其值的列表。"),
    ("The metadata attribute name.", "元数据属性名称。"),
    ("The values associated with the metadata attribute.", "与元数据属性关联的值。"),

    # Size chart
    ("Filter size charts by size chart template IDs.", "按尺码表模板 ID 过滤尺码表。"),
    ("Filter size charts by size chart template name or by key words in the template name.",
     "按尺码表模板名称或模板名称中的关键词过滤尺码表。"),
    ("Filter size charts by usage mode.", "按使用模式过滤尺码表。"),
    ("The list of size charts that meet the query conditions.", "符合查询条件的尺码表列表。"),
    ("The size chart template name.", "尺码表模板名称。"),
    ("The list of images included in a size chart.", "尺码表中包含的图片列表。"),
    ("Leaf category IDs applicable to this size chart.", "适用于此尺码表的叶子分类 ID。"),
    ("Localized structured size chart data.", "本地化的结构化尺码表数据。"),
    ("Structured size chart data for the specified locale.", "指定语言环境的结构化尺码表数据。"),
    ("The language of the size chart table.", "尺码表表格的语言。"),
    ("The language of the size chart image.", "尺码表图片的语言。"),
    ("Structured table containing headers and rows.", "包含表头和行的结构化表格。"),
    ("Ordered header definitions.", "有序的表头定义。"),
    ("Header display name.", "表头显示名称。"),
    ("Standard size-system ID or measurement key.", "标准尺码体系 ID 或测量键。"),
    ("Rows of the size chart.", "尺码表的行。"),
    ("Cells aligned by index with table.headers.", "按索引与 table.headers 对齐的单元格。"),
    ("Cell value.", "单元格值。"),
    ("Additional size chart description.", "额外的尺码表描述。"),
    ("Whether this is a one-size chart.", "是否为均码表。"),
    ("The number of size charts that meet the query conditions.", "符合查询条件的尺码表数量。"),
    ("The size chart template ID.", "尺码表模板 ID。"),

    # Currency
    ("The currency.", "货币。"),
    ("The currency.Possible values based on the region:", "货币。基于地区的可能值："),

    # Product fees
    ("Product fees related rules.", "产品费用相关规则。"),
    ("A flag to indicate whether information about the fee is required.", "标识是否需要费用信息的标志。"),
    ("The list of special product types, excluding regular products, that your shop is allowed to list in this category.",
     "您的店铺允许在此分类中上架的特殊产品类型列表（不包括常规产品）。"),

    # Specify a category
    ("Specify a category ID to show the availability of", "指定分类 ID 以显示"),
    ("Filter results by the brand authorization status.", "按品牌授权状态过滤结果。"),
    ("Filter results to include brand names that begin with the specified value.", "过滤结果以包含以指定值开头的品牌名称。"),
    ("Whether you can select and display a brand depends on the brand's authorization status",
     "您是否可以选择和显示品牌取决于品牌的授权状态"),
    ("the categories authorized for the brand", "品牌被授权的分类"),
    ("and whether the brand is classified as T1 (internationally renowned brands that require prior brand authorization).",
     "以及品牌是否被归类为 T1（需要事先品牌授权的国际知名品牌）。"),
    ("A requirement that the shop needs to satisfy.", "店铺需要满足的要求。"),
    ("The specific reasons for failing a certain", "未通过特定"),

    # Product ID
    ("The product ID.", "产品 ID。"),
    ("The product field being diagnosed.", "被诊断的产品字段。"),
    ("The diagnosis results.", "诊断结果。"),
    ("Product optimization diagnosis information.", "产品优化诊断信息。"),
    ("Improvement suggestions.", "改进建议。"),
    ("The suggested SEO keyword text.", "建议的 SEO 关键词文本。"),
    ("The intelligent text suggestions for titles and descriptions.", "标题和描述的智能文本建议。"),
    ("The suggested intelligent text.", "建议的智能文本。"),
    ("The optimized main image. Only the first image in the main image set will be optimized.",
     "优化后的主图。仅优化主图组中的第一张图片。"),
    ("The URI of the image after optimization.", "优化后图片的 URI。"),
    ("The URL of the image after optimization.", "优化后图片的 URL。"),
    ("The image height after optimization.", "优化后的图片高度。"),
    ("The image width after optimization.", "优化后的图片宽度。"),
    ("The current quality tier of this product listing.", "此产品上架的当前质量等级。"),
    ("Product listing quality information.", "产品上架质量信息。"),
    ("Warning information that needs attention.", "需要注意的警告信息。"),
    ("The listing quality tier you can reach by implementing the recommendation.", "通过实施建议可以达到的上架质量等级。"),
    ("The recommendation for resolving the identified issue, returned in the default locale language of the shop.",
     "解决已识别问题的建议，以店铺的默认语言返回。"),
    ("A machine-readable code that represents an identified issue.", "代表已识别问题的机器可读代码。"),
    ("A machine-readable code that represents the failure reason.", "代表失败原因的机器可读代码。"),
    ("A detailed reason for the failure.", "详细的失败原因。"),

    # Built-in attribute
    ("The built-in attribute.", "内置属性。"),
    ("The name of the built-in attribute.", "内置属性的名称。"),
    ("The attribute type.", "属性类型。"),
    ("A flag to indicate if the product attribute is always required when creating or editing a product.",
     "标识在创建或编辑产品时是否始终需要该产品属性的标志。"),
    ("Certification related rules.", "认证相关规则。"),
    ("Size chart related rules.", "尺码表相关规则。"),
    ("A flag to indicate whether size charts are supported.", "标识是否支持尺码表的标志。"),
    ("A flag to indicate whether a size chart is required.", "标识是否需要尺码表的标志。"),
    ("Cash on Delivery (COD) related rules.", "货到付款（COD）相关规则。"),
    ("A flag to indicate whether COD is supported.", "标识是否支持 COD 的标志。"),
    ("Package dimension related rules.", "包装尺寸相关规则。"),
    ("A flag to indicate whether package dimensions are required.", "标识是否需要包装尺寸的标志。"),
    ("Extended Producer Responsibility (EPR) related rules.", "生产者延伸责任（EPR）相关规则。"),
    ("A flag to indicate whether EPR is required.", "标识是否需要 EPR 的标志。"),
    ("Responsible person (RP) related rules. Applicable only for the EU market.", "负责人（RP）相关规则。仅适用于欧盟市场。"),
    ("A flag to indicate whether the responsible person information is required.", "标识是否需要负责人信息的标志。"),
    ("Manufacturer related rules. Applicable only for the EU market.", "制造商相关规则。仅适用于欧盟市场。"),
    ("A flag to indicate whether the manufacturer information is required.", "标识是否需要制造商信息的标志。"),
    ("The list of standard built-in product and sales attributes that are bound to the specified category, based on your shop's location.",
     "根据您店铺的位置，绑定到指定分类的标准内置产品属性和销售属性列表。"),
    ("The ID of the built-in attribute.", "内置属性的 ID。"),
    ("The ID of the built-in attribute value.", "内置属性值的 ID。"),
    ("The name of the built-in attribute value.", "内置属性值的名称。"),
    ("A list of selectable values for the attribute.", "属性的可选值列表。"),
    ("A flag indicating whether sellers can enter a custom value for the attribute when creating or editing a product.",
     "标识卖家在创建或编辑产品时是否可以为属性输入自定义值的标志。"),
    ("A flag indicating whether sellers can select multiple values for the attribute when creating or editing a product.",
     "标识卖家在创建或编辑产品时是否可以为属性选择多个值的标志。"),
    ("The data format for a free-form attribute value.", "自由格式属性值的数据格式。"),
    ("Certification expiration date related rules.", "认证到期日期相关规则。"),
    ("A flag to indicate whether an expiration date is required for this certification.", "标识此认证是否需要到期日期的标志。"),
    ("The type of condition.", "条件的类型。"),
    ("The ID of the product attribute that is being evaluated by the condition.", "被条件评估的产品属性的 ID。"),
    ("The ID of the product attribute value that must match the seller's input for the condition to be true.",
     "必须与卖家输入匹配才能使条件为真的产品属性值的 ID。"),
    ("Details about the certification documents that you must submit, including the content, format, and any other guidelines.",
     "您必须提交的认证文件的详细信息，包括内容、格式和任何其他指南。"),
    ("The URL to view an image of the sample certification document.", "查看示例认证文件图片的 URL。"),

    # Product status
    ("The platforms for listing the product.", "产品上架的平台。"),
    ("The shipping insurance purchase requirement imposed on buyers for the product.", "对买家施加的产品运输保险购买要求。"),
    ("A flag to indicate if the product is pre-owned.", "标识产品是否为二手产品的标志。"),
    ("The minimum order quantity for the product.", "产品的最低订购量。"),
    ("Identifier of the shipping template that will be bound to the product", "将绑定到产品的运费模板的标识符"),
    ("Options for asynchronous product information verification.", "异步产品信息验证的选项。"),
    ("Search terms (ST words).", "搜索词（ST 词）。"),
    ("Key Product Features.", "关键产品特性。"),

    # A list of URLs
    ("A list of URLs for third-party product listing pages where consumers can place orders.",
     "消费者可以下单的第三方产品上架页面 URL 列表。"),

    # Various remaining descriptions
    ("Warning information that the API caller needs to pay special attention to.", "API 调用者需要特别关注的警告信息。"),
    ("The result of the product diagnosis (PASS, FAILED).", "产品诊断的结果（PASS, FAILED）。"),

    # SKU descriptions
    ("A list of Stock Keeping Units (SKUs) used to identify distinct variants of the product.",
     "用于标识产品不同变体的 SKU（库存单位）列表。"),
    ("A list of attributes (e.g. size, color, length) that define each variant of a product.",
     "定义产品每个变体的属性列表（如尺寸、颜色、长度）。"),
    ("The ID of a built-in sales attribute, retrieved from", "内置销售属性的 ID，从"),
    ("A self-defined custom sales attribute name to validate when the built-in attributes do not satisfy your needs.",
     "当内置属性不满足需求时，用于验证的自定义销售属性名称。"),
    ("The ID of a built-in sales attribute value, retrieved from the", "内置销售属性值的 ID，从"),
    ("A self-defined custom sales attribute value to validate when the built-in values do not satisfy your needs.",
     "当内置值不满足需求时，用于验证的自定义销售属性值。"),
    ("No duplicates allowed under the same attribute.", "同一属性下不允许重复。"),
    ("An internal code/name for managing SKUs, not visible to buyers.", "用于管理 SKU 的内部代码/名称，对买家不可见。"),
    ("SKU pricing information.", "SKU 定价信息。"),
    ("SKU inventory information.", "SKU 库存信息。"),
    ("The ID of the warehouse where the SKU is stored.", "SKU 存放仓库的 ID。"),
    ("Retrieve the list of warehouses available for your shop from the", "从以下位置获取您的店铺可用仓库列表"),
    ("The total SKU quantity available in the warehouse.", "仓库中可用的 SKU 总数量。"),

    # Product title/description
    ("The product title.", "产品标题。"),
    ("Title length:", "标题长度："),
    ("A flag indicating whether to show the Cash On Delivery (COD) payment option during checkout.",
     "标识是否在结账时显示货到付款（COD）付款选项的标志。"),
    ("The list of certifications for your product.", "您的产品的认证列表。"),
    ("The ID to identify the type of certification required for the product category.", "用于标识产品分类所需认证类型的 ID。"),
    ("A list of certification related images.", "认证相关图片列表。"),
    ("A list of certification related files.", "认证相关文件列表。"),
    ("The ID of the certification file.", "认证文件的 ID。"),
    ("The name of the certification file, including the file extension.", "认证文件的名称，包括文件扩展名。"),
    ("The format of the certification file. Only PDF is supported.", "认证文件的格式。仅支持 PDF。"),
    ("The expiration date of this certification expressed in unix timestamp (seconds) UTC+0.",
     "此认证的到期日，以 Unix 时间戳（秒）UTC+0 表示。"),

    # Package weight/dimensions
    ("The weight of the product package.", "产品包装的重量。"),
    ("The package weight, which must be a positive number.", "包装重量，必须是正数。"),
    ("The unit for the package weight.", "包装重量的单位。"),
    ("The unit for the SKU weight.", "SKU 重量的单位。"),
    ("The unit for the SKU dimensions.", "SKU 尺寸的单位。"),
    ("The package length. A positive whole number.", "包装长度。正整数。"),
    ("The package width. A positive whole number.", "包装宽度。正整数。"),
    ("The package height. A positive whole number.", "包装高度。正整数。"),
    ("The dimensions of the sku.", "SKU 的尺寸。"),
    ("The packaged weight of the SKU.", "SKU 的包装重量。"),
    ("The dimensions of the product package.", "产品包装的尺寸。"),

    # Product attributes
    ("A list of general attributes (e.g. manufacturer, country of origin, materials used) that describe the product as a whole, regardless of variant.",
     "描述产品整体（不考虑变体）的一般属性列表（如制造商、原产国、使用材料）。"),
    ("The ID of the product attribute, retrieved from the", "产品属性的 ID，从"),
    ("A list of selectable values for the product attribute.", "产品属性的可选值列表。"),
    ("The ID of a built-in product attribute value, retrieved from the", "内置产品属性值的 ID，从"),
    ("A self-defined custom product attribute value if the built-in values do not satisfy your needs. The system will auto-generate an ID after listing.",
     "如果内置值不满足需求，可自定义产品属性值。系统将在上架后自动生成 ID。"),

    # Size chart
    ("The measurement details of the product to help buyers find the right size.", "产品的测量详情，帮助买家找到合适的尺码。"),
    ("An image of the size chart.", "尺码表的图片。"),

    # Product video
    ("A product introduction or promotion video to display for your product.", "用于展示产品的产品介绍或推广视频。"),
    ("The ID of the product video.", "产品视频的 ID。"),

    # Manufacturer/responsible person
    ("A list of manufacturer IDs. Retrieve the IDs from the", "制造商 ID 列表。从"),
    ("A list of responsible person IDs. Retrieve the IDs from the", "负责人 ID 列表。从"),

    # Retrieve the IDs from the
    ("Retrieve the IDs from the", "获取 ID，从"),
    ("Retrieve the IDs from", "获取 ID，从"),

    # The ID of the category. It must be a leaf category.
    ("The ID of the category. It must be a leaf category.", "分类 ID。必须是叶子分类。"),
    ("The ID of the category of this product. It must be a leaf category.", "此产品的分类 ID。必须是叶子分类。"),

    # For certain categories
    ("For certain categories, size charts may be required.", "对于某些分类，可能需要尺码表。"),

    # A flag indicating whether
    ("A flag indicating whether the shop has failed a", "标识店铺是否未通过"),

    # Max number of IDs
    ("Max number of IDs: 20", "最大 ID 数量：20"),

    # The product IDs to activate
    ("The product IDs to activate.", "要激活的产品 ID。"),

    # The language used in text fields
    ("The language used in text fields such as descriptions and titles must align with the target market's language (e.g. don't use Chinese).",
     "描述和标题等文本字段中使用的语言必须与目标市场的语言一致（例如，不要使用中文）。"),

    # The diagnosis is performed
    ("The diagnosis is performed on the following product fields:", "对以下产品字段执行诊断："),

    # Refer to the following region-based tables
    ("Refer to the following region-based tables for the diagnosis results/codes returned in the APIs and the actionable recommendations to optimize your listings effectively.",
     "请参考以下基于地区的表格，了解 API 中返回的诊断结果/代码以及可有效优化上架的可操作建议。"),

    # Codes marked as Retired
    ('Codes marked as "**Retired**" indicate that they are no longer recommended and will not appear anymore.',
     '标记为"**已停用**"的代码表示不再推荐使用，将不再出现。'),

    # In the US, product listings
    ("In the US, product listings are evaluated based on a tiered system that includes listing quality tiers such as",
     "在美国，产品上架基于分层系统评估，包括上架质量等级，如"),

    # Each diagnosis code
    ('Each diagnosis code corresponds to a specific recommendation and is assigned a quality tier, such as "FAIR" or "GOOD".',
     '每个诊断代码对应一个具体建议，并被分配一个质量等级，如"FAIR"或"GOOD"。'),
    ("Implementing the recommendations can help your listing progress through these tiers to achieve better quality and visibility.",
     "实施这些建议可以帮助您的上架逐步提升等级，获得更好的质量和可见性。"),
    ('For example, a product will reach the "GOOD" tier once all "FAIR" and "GOOD" recommendations are addressed or implemented.',
     '例如，一旦所有"FAIR"和"GOOD"建议都得到解决或实施，产品将达到"GOOD"等级。'),

    # For more information about the listing quality tiers
    ("For more information about the listing quality tiers and criteria, refer to",
     "有关上架质量等级和标准的更多信息，请参考"),

    # For regions outside the US
    ("For regions outside the US, product listings are evaluated based on key recommendations.",
     "对于美国以外的地区，产品上架基于关键建议进行评估。"),
    ("The following table provides the list of diagnosis codes along with actionable recommendations to improve your product listing's overall quality and visibility.",
     "以下表格提供了诊断代码列表以及可改善产品上架整体质量和可见性的可操作建议。"),

    # The product title/description/attributes/size chart image/product images (API property)
    ("The product title (API property:", "产品标题（API 属性："),
    ("The product description (API property:", "产品描述（API 属性："),
    ("The product attributes (API property:", "产品属性（API 属性："),
    ("The size chart image (API property:", "尺码表图片（API 属性："),
    ("The product images displayed in the image gallery (API property:", "在图片库中展示的产品图片（API 属性："),

    # Every single app
    ("Every single app will have a unique key. Please use the specific key assigned to your app.",
     "每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。"),

    # Signature
    ("Signature generated by gen algorithm.", "由 gen 算法生成的签名。"),
    ("When you send API requests to TTS, you must sign them so that TTS can identify the senders.",
     "当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。"),

    # Unix timestamp
    ("Unix timestamp GMT (UTC+00:00).", "Unix 时间戳 GMT（UTC+00:00）。"),
    ("This timestamp is used across all API requests.", "此时间戳用于所有 API 请求。"),
    ("Developers can use this convert to local time.", "开发者可以将其转换为本地时间。"),

    # Use this property
    ("Use this property to pass shop information in requesting the API.", "使用此属性在请求 API 时传递店铺信息。"),
    ("Failure in passing the correct value when requesting the API for cross-border shops will return incorrect response.",
     "在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。"),

    # The product title\nTitle length
    ("The product title.\\nTitle length:", "产品标题。\\n标题长度："),

    # Additional remaining descriptions
    ("The product title.\\nTitle length:", "产品标题。\\n标题长度："),
]


# ============================================================
# PHASE 2: Full-line replacements (exact match on stripped line)
# ============================================================
FULL_LINE_MAP = {
    "# Path:": "# 路径：",
    "# Method: [POST]": "# 方法：[POST]",
    "# Method: [GET]": "# 方法：[GET]",
    "# Method: [PUT]": "# 方法：[PUT]",
    "# Method: [DELETE]": "# 方法：[DELETE]",
    "Possible values:": "可能的值：",
    "Possible values based on region:": "基于地区的可能值：",
    "Possible values based on the region:": "基于地区的可能值：",
    "**Note**:": "**注意**：",
    "**Note**: ": "**注意**：",
    "**Recommendations**:": "**建议**：",
    "**Format**:": "**格式**：",
    "**Important**:": "**重要**：",
    "**Query**": "**查询**",
    "**Body**": "**正文**",
    "**US**": "**美国**",
    "**UK, EU, SEA, JP, and LATAM**": "**英国、欧盟、东南亚、日本和拉丁美洲**",
    "Note:": "注意：",
    "Valid range:": "有效范围：",
    "Valid length:": "有效长度：",
    "Supports two decimal places.": "支持两位小数。",
    "---": "---",
    "* TIKTOK_SHOP": "* TIKTOK_SHOP",
    "* TOKOPEDIA": "* TOKOPEDIA",
    "* SINGLE_USE": "* SINGLE_USE",
    "* REUSABLE": "* REUSABLE",
    "* NOT_APPLICABLE": "* NOT_APPLICABLE",
    "* GTIN": "* GTIN",
    "* EAN": "* EAN",
    "* UPC": "* UPC",
    "* ISBN": "* ISBN",
    "* JAN": "* JAN",
    "* SHOP_STATUS": "* SHOP_STATUS",
    "* SHOP_TAX": "* SHOP_TAX",
    "* PICKUP_WAREHOUSE": "* PICKUP_WAREHOUSE",
    "* RETURN_WAREHOUSE": "* RETURN_WAREHOUSE",
    "* DELIVERY_OPTION": "* DELIVERY_OPTION",
    "* SHIPPING_TEMPLATE": "* SHIPPING_TEMPLATE",
    "* PRODUCT_QUANTITY_LIMIT": "* PRODUCT_QUANTITY_LIMIT",
    "* EXTENDED_PRODUCER_RESPONSIBILITY": "* EXTENDED_PRODUCER_RESPONSIBILITY",
    "* BANk_ACCOUNT": "* BANk_ACCOUNT",
    "* CONTACT_INFO": "* CONTACT_INFO",
    "Default: TIKTOK_SHOP": "默认值：TIKTOK_SHOP",
    "Default: false": "默认值：false",
    "Default: true": "默认值：true",
    "Default: v1": "默认值：v1",
    "Default: LISTING": "默认值：LISTING",
}


def translate_path_method(line):
    """Translate # Path: and # Method: headers."""
    m = re.match(r'^# Path:\s*(.+)$', line)
    if m:
        return f"# 路径：{m.group(1)}"
    m = re.match(r'^# Method:\s*(.+)$', line)
    if m:
        return f"# 方法：{m.group(1)}"
    return None


def fix_file(filepath):
    """Apply all fixes to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result_lines = []
    in_code_block = False

    for line in lines:
        raw = line.rstrip('\n')
        stripped = raw.strip()

        # Track code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result_lines.append(raw)
            continue

        if in_code_block:
            result_lines.append(raw)
            continue

        # Skip empty lines
        if not stripped:
            result_lines.append(raw)
            continue

        # Skip horizontal rules
        if stripped == '---':
            result_lines.append(raw)
            continue

        # Skip pure HTML/img/svg/base64
        if stripped.startswith('<img ') or 'from="flow-chart"' in stripped or 'payload=' in stripped:
            result_lines.append(raw)
            continue
        if stripped.startswith('data:image') or stripped.startswith('<br><br>'):
            result_lines.append(raw)
            continue

        # Skip lines that are just locale codes or enum values in bullet lists
        if re.match(r'^[*\s]*`?[a-z]{2}[-_][A-Z]{2}`?\s*\|?$', stripped):
            result_lines.append(raw)
            continue

        # Try Path/Method translation
        pm = translate_path_method(stripped)
        if pm is not None:
            indent = len(raw) - len(raw.lstrip())
            result_lines.append(' ' * indent + pm)
            continue

        # Try full-line match
        if stripped in FULL_LINE_MAP:
            indent = len(raw) - len(raw.lstrip())
            result_lines.append(' ' * indent + FULL_LINE_MAP[stripped])
            continue

        # Apply inline fixes (longest first)
        result = raw
        sorted_fixes = sorted(INLINE_FIXES, key=lambda x: -len(x[0]))
        for eng, chn in sorted_fixes:
            if eng in result:
                result = result.replace(eng, chn)

        result_lines.append(result)

    # Write back
    output = '\n'.join(result_lines)
    if lines and lines[-1].endswith('\n'):
        output += '\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output)


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

    print(f"Found {len(files)} files to fix")

    for i, f in enumerate(files):
        basename = os.path.basename(f)
        print(f"[{i+1}/{len(files)}] Fixing: {basename}")
        fix_file(f)

    print(f"\nDone! Fixed {len(files)} files.")


if __name__ == "__main__":
    main()
