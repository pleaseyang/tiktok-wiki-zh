# 上架质量诊断

高质量的商品上架对于提高可见性和建立客户信任至关重要。
TikTok Shop 提供诊断商品内容并提供优化建议的 API，涵盖文本、图片和搜索引擎优化（SEO）等领域。

**对于未上架的新商品**
- [Check Product Listing API (v202309)](https://partner.tiktokshop.com/docv2/page/650a0ee8f1fd3102b91c6493)：使用此接口在上架前预先诊断新商品。
<br/>
**对于现有商品**
- [Product Information Issue Diagnosis API (v202405)](https://partner.tiktokshop.com/docv2/page/665048f380b6b302e73917d9)：使用此接口诊断店铺商品目录中已上架的在售商品。
<br/>

**说明**：对于服务美国市场的开发者，可以先使用 [Search Products API (v202312)](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda?external_id=65854ffb8f559302d8a6acda) 获取属于某个上架质量层级的商品，再运行 [Product Information Issue Diagnosis API (v202405)](https://partner.tiktokshop.com/docv2/page/665048f380b6b302e73917d9) 以识别建议。之后，可以使用 [Get Product API (v202309)](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda?external_id=6509d85b4a0bb702c057fdda) 获取商品现有的属性值（包括其上架质量层级），并找出需要编辑的属性值。
# 诊断结果和建议
对以下商品字段执行诊断：
**-** **Title**: 商品标题（API 属性： `title`)
**-** **Description**: 商品描述（API 属性： `description`)
**-** **Attributes**: 商品属性（API 属性： `product_attributes` or `skus.sales_attributes`)
**-** **Size chart**: 尺码表图片（API 属性： `size_chart`)
**-** **Product images**: 在图片库中展示的商品图片（API 属性： `main_images`)

请参考以下基于地区的表格，了解 API 中返回的诊断结果/代码以及可有效优化上架的可操作建议。
**注意**： 标记为"**已停用**"的代码表示不再推荐使用，将不再出现。

# 美国
在美国，商品上架基于分层系统评估，包括上架质量等级，如 "POOR", FAIR", and "GOOD". 每个诊断代码对应一个具体建议，并被分配一个质量等级，如"FAIR"或"GOOD"。实施这些建议可以帮助您的上架逐步提升等级，获得更好的质量和可见性。例如，一旦所有"FAIR"和"GOOD"建议都得到解决或实施，商品将达到"GOOD"等级。
有关上架质量等级和标准的更多信息，请参考 [Listing Quality Guidelines](https://seller-us.tiktok.com/university/essay?from=feature_guide&identity=1&knowledge_id=481891871868714&role=1)。
| **Quality tier**  <!-- width:100px --> | **Category**  <!-- width:130px --> | **Diagnosis code (`diagnosis_results.code`）**<!-- width:440px --> | **Recommendations** |
| --- | --- | --- | --- |
| FAIR | Description | DESCRIPTION_CHARACTERS_LESS_THAN_80_CHARS | 提供至少 80 个字符的描述和/或添加图片。 |
| FAIR | Description | DESCRIPTION_INVALID | 避免仅提供链接。请详细描述商品。 |
| FAIR | Product images  | MAIN_IMG_DUPLICATE <br/>  | 移除重复图片。 |
| FAIR | Product images  | MAIN_IMG_FIRST_IMG_LOW_QUALITY | 首图: 图片分辨率必须至少为 600*600px。 |
| FAIR | Product images  | MAIN_IMG_FIRST_IMG_MISSING_PRODUCT_SUBSTANCE <br/>  | 首图：使用商品突出且易于辨识的图片。避免使用过度放大的图片、没有实际商品照片的图片，或商品过小的图片。 |
| FAIR | Product images | MAIN_IMG_FIRST_IMG_PRODUCT_SUBJECT_NOT_COMPLETE | 首图: 使用完整展示商品且未被裁剪的图片。 |
| FAIR | Product images | MAIN_IMG_FIRST_IMG_TEXT_OVERLOAD | 首张图片: 使用不包含徽标，水印，图形和文字的图片。 |
| FAIR | Product images | MAIN_IMG_FIRSTIMG_LOW_QUALITY_BACKGROUND | 首图：使用简洁的纯色背景以突出商品。 |
| FAIR | Product images | MAIN_IMG_FIRSTIMG_WATERMARK | 首张图片：使用不含水印的图片。 |
| FAIR | Product images | **(新增)** MAIN_IMG_FIRST_IMG_SPLICED_PICTURE | 首图: 使用完整，独立的商品图片，而非拼图。 |
| FAIR | Product images | MAIN_IMG_INVALID | 使用展示商品或其特性的真实图片。避免使用与商品本身无关的占位插图。 |
| FAIR | Product images | MAIN_IMG_LOW_QUALITY_SHOT | 确保商品图片清晰对焦且未被过度拉伸。 |
| FAIR | Product images | MAIN_IMG_OBFUSCATION | 确保图片未被修改以遮挡商品的任何部分。 |
| FAIR | Product images | **(已废弃)** MAIN_IMG_SPLICED_PICTURE | 使用完整，独立的商品图片而非拼图。 |
| FAIR | Product images | **(新增)** MAIN_IMG_PROMOTION_IMAGE <br/>  | 使用不包含任何营销或促销贴纸的图片，例如 "free shipping" 或 "best sale"。 |
| FAIR | Title | TITLE_INCLUDE_ADVERTISE | 移除诸如 "Last unit"、"50% discount" 或 "Limited time only" 之类的促销用语。 |
| FAIR | Title | TITLE_NOT_INCLUDE_PRODUCT_SUBJECT_WORDS | 加入能够标识该商品的词。例如，"Tshirt"、"Smartphone" 或 "Sneakers"。 |
| FAIR | Title | TITLE_NOT_INCLUDE_VARIETY_WORDS | 移除任何关于库存可用性的提及，以及对颜色、尺寸、数量、口味和类似商品类型的重复提及。不当短语示例："red/blue/green", "5 colors", "plus size, plus size set", "set of 4, set of 6", "sweatpants, lounge pants, workout pants", "low stock"。 |
| FAIR | Title | TITLE_REPETITIVE | 避免任何词重复超过 4 次。 |
| GOOD <br/>  | Attributes | **(已废弃)** ATTRIBUTE_MISSING_SHOPPING_GUIDE_ITEM | 提供额外的属性以帮助买家决策。 |
| GOOD | Description | DESCRIPTION_HAVE_TOO_LONG_PARAGRAPH | 段落保持在 400 个字符以内。 |
| GOOD | Description | DESCRIPTION_INCLUDE_INVALID_IMAGE | 移除任何重复，样机，或占位图片。 |
| GOOD | Description | DESCRIPTION_INCLUDE_LESS_THAN_3_IMAGES | 如果选择不提供文字描述，请至少添加 3 张图片。 |
| GOOD | Description | DESCRIPTION_NOT_PROPER_CAPITALIZATION | 使用句首字母大写，避免全大写。 |
| GOOD | Description | PRD_NOT_INCLUDE_APPLICABLE_SCOPE | 指定目标用户群体，例如护肤品的肤质 (如干性，中性，油性), 或婴儿/宠物用品的年龄段。 |
| GOOD | Description | PRD_NOT_INCLUDE_CATALOG | 为图书提供目录，或为音乐提供曲目列表。 |
| GOOD | Description | PRD_NOT_INCLUDE_FRAGRANCE_NOTES | 为香水添加香调，包括前调、中调和后调的详细信息。 |
| GOOD | Description | PRD_NOT_INCLUDE_INGREDIENTS | 提供商品的主要成分。 |
| GOOD | Description | PRD_NOT_INCLUDE_INGREDIENTS_LIST | 提供商品成分的完整列表。 |
| GOOD | Description | **(已废弃)** PRD_NOT_INCLUDE_KEY_PARAMETER_LIST | 为电子商品提供 4 项或更多关键规格 (例如智能手机的屏幕分辨率，电池容量，处理器类型，RAM)。 |
| GOOD | Description | PRD_NOT_INCLUDE_MATERIAL_DETAILS | 提供材质信息 (e.g. 棉混纺: 80% 棉，20% 聚酯纤维)。 |
| GOOD | Description | PRD_NOT_INCLUDE_NUTRITION_FACT | 添加营养成分信息。 |
| GOOD | Description | **(已废弃)** PRD_NOT_INCLUDE_PACKAGE_LIST | 提供包裹内所含物品的完整列表。 |
| GOOD | Description | PRD_NOT_INCLUDE_PRD_BENEFITS | 添加清晰的商品卖点。例如，该商品可强韧发丝、修护损伤并防止断裂。 |
| GOOD | Description | PRD_NOT_INCLUDE_SPECIFICATIONS | 提供商品尺寸，体积或重量等测量信息。 |
| GOOD | Description | PRD_NOT_INCLUDE_MULTI_ANGLE_OR_DETAIL_DISPLAY | 添加多角度或细节图片以完整展示商品 |
| GOOD | Product images | MAIN_IMG_FIRST_IMG_BACKGROUND_UNTIDY | 首图：使用简洁的纯色背景以突出商品。 |
| GOOD | Product images | MAIN_IMG_FIRST_IMG_BLACK_BORDER | 首图：去除彩色边框。 |
| GOOD | Product images | MAIN_IMG_FIRST_IMG_FAKE_MODEL | 首图: 使用真人或动物来展示你的商品。 |
| GOOD | Product images | MAIN_IMG_FIRST_IMG_NOT_CLEAR | 首图: 使用对焦清晰，不模糊的商品图片. <br/>  |
| GOOD | Product images | MAIN_IMG_FIRST_IMG_WHITE_BORDER | 首图：去除彩色边框。 |
| GOOD | Product images | MAIN_IMG_LESS_THAN_5_IMAGES | 提供 5 张或更多商品图片。 |
| GOOD | Product images | MAIN_IMAGE_COUNT_NOT_MEET_STANDARD | 请上传更多主图以确保商品展示效果更佳。所需图片数量因类目而异（例如至少 1、3、4 或 5 张图片）。详情请参阅诊断结果中的建议。 |
| GOOD | Size chart | **(已停用)** SIZE_CHART_NOT_INCLUDE_STANDARDIZED_SIZE_INFO | 提供包含所有相关测量值的完整尺码表. <br/>  |
| GOOD <br/>  | Size chart | **(新增)** SIZE_CHART_NOT_INCLUDE_SIZE_INFO <br/>  | 请至少提供 1 个尺码变体（如 S、M 或 L）和 1 个尺码维度（如胸围、腰围或臀围） |
| GOOD | Title | **(已废弃)** TITLE_LESS_THAN_25_CHARS | 使用至少 25 个字符的商品名称。 |

# 世界其他地区
对于美国以外的地区，商品上架基于关键建议进行评估。以下表格提供了诊断代码列表以及可改善商品上架整体质量和可见性的可操作建议。
| **Category** <br/> <!-- width:130px --> | **Region** <br/> <!-- width:130px --> | **Diagnosis result (`diagnosis_results.code`）** | **Recommendations** |
| --- | --- | --- | --- |
| Description | 除 JP 外的所有市场 | DESC_LESS_THAN_FIVE_HUNDRED_CHARS | 将商品描述扩展至至少 500 个字符。 |
| Description | JP | **(新增)** DESC_LESS_THAN_FIFTY_CHARS | 将商品描述扩展至至少 50 个字符。 |
| Description | All | DESC_NO_NEW_LINE | 在商品描述中添加换行，以增强可读性和结构。 |
| Product images | All | MAIN_IMG_DUPLICATE | 移除重复图片。 |
| Product images | All | MAIN_IMG_FIRST_IMG_BACKGROUND_UNTIDY | 首图：使用简洁的纯色背景以突出商品。 |
| Product images | All | MAIN_IMG_FIRST_IMG_BLACK_BORDER | 首图：去除彩色边框。 |
| Product images | All | MAIN_IMG_FIRST_IMG_FAKE_MODEL | 首图: 使用真人或动物来展示你的商品。 |
| Product images | All | MAIN_IMG_FIRST_IMG_INCLUDE_NON_LOCAL_LANGUAGE | 首图：仅使用当地语言。 |
| Product images | All | MAIN_IMG_FIRST_IMG_LOW_QUALITY | 首图: 图片分辨率必须至少为 600*600px。 |
| Product images | All | MAIN_IMG_FIRST_IMG_MISSING_PRODUCT_SUBSTANCE | 首图：使用商品突出且易于辨识的图片。避免使用过度放大的图片、没有实际商品照片的图片，或商品过小的图片。 |
| Product images | All | MAIN_IMG_FIRST_IMG_NOT_CLEAR | 首图：使用对焦清晰、不模糊的商品图片。 |
| Product images | All | MAIN_IMG_FIRST_IMG_PRODUCT_SUBJECT_NOT_COMPLETE | 首图: 使用完整展示商品且未被裁剪的图片。 |
| Product images | All | MAIN_IMG_FIRST_IMG_SPLICED_PICTURE | 首图: 使用完整，独立的图片，而非拼图。 |
| Product images | All | MAIN_IMG_FIRST_IMG_TEXT_OVERLOAD | 首张图片: 使用不包含徽标，水印，图形和文字的图片。 |
| Product images | All | MAIN_IMG_FIRST_IMG_WHITE_BORDER | 首图：去除彩色边框。 |
| Product images | 除 JP 外的所有市场 | MAIN_IMG_NUMBER_LESS_THAN_FIVE | 提供 5 张或更多商品图片。 |
| Title | 除 JP 外的所有市场 | TITLE_LESS_THAN_40_CHARACTERS | 将标题扩展至至少 40 个字符。 |
| Title | JP | **(新增)** TITLE_LESS_THAN_25_CHARACTERS | 将标题扩展至至少 25 个字符。 |
| Title | All | SEO_DIAGNOSTIC_ITEM | 添加更多 SEO 关键词。你可以参考 `suggestion.seo_words` 中建议的 SEO 关键词。 |
| Size chart | EU, JP, UK | **(新增)** SIZE_CHART_NOT_INCLUDE_SIZE_INFO <br/>  | 请至少提供 1 个尺码变体（如 S、M 或 L）和 1 个尺码维度（如胸围、腰围或臀围） |

