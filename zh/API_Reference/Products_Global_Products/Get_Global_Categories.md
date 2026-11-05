# 获取全球分类

# Path: /product/202309/global_categories
# Method: [GET]
# 功能描述
Retrieve all available product categories, regardless of market variations.
Product categories are updated frequently, so it's recommended to call the API in real time to ensure you are using the latest category data. Caching category data locally may result in using outdated information, leading to errors when creating global products.

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| locale | string | N | en-GB | 用于显示分类信息的 BCP-47 语言环境代码。 |
| Default: 您店铺的默认语言环境。 |  |  |  |  |
| Possible values: |  |  |  |  |

* `cs-CZ`
* `de-AT`
* `de-BE`
* `de-DE`
* `el-GR`
* `en-GB`
* `en-IE`
* `en-US`
* `es-ES`
* `es-MX`
* `fr-FR`
* `fr-BE`
* `hu-HU`
* `id-ID`
* `it-IT`
* `ja-JP`
* `ms-MY`
* `nl-NL`
* `nl-BE`
* `pl-PL`
* `pt-BR`
* `pt-PT`
* `th-TH`
* `vi-VN`
* `zh-CN` |
   keyword |string |N |electronics |使用此关键词过滤分类 `local_name`. |
   category_version |string |N |v1 |按分类树版本过滤分类。Possible values based on region:
* US, EU and SEA: v2, represents the 7-level category tree.
   Important: For US, EU and SEA shops, you must pass v2 when using this API.
* Other regions: v1, represents the 3-level category tree.Default: v1 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/global_categories?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&locale=en-GB&keyword=electronics&category_version=v1
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^categories | []object |  | 符合查询条件的分类列表。 |
| ^^id | string | 600001 | 分类 ID。 |
| ^^parent_id | string | 0 | 父分类 ID。 |
| For the root category, the parent ID is `0`. |  |  |  |
| ^^local_name | string | Home Supplies | The name of the category. |
| ^^is_leaf | bool | false | 标识该分类是否为叶子分类的标志。 |
| **Note**: 您只能创建或编辑属于叶子分类的产品。 |  |  |  |
| ^^permission_statuses | []string | ["AVAILABLE"] |  |
| 该店铺的此分类权限状态。 |  |  |  |
| Possible values: |  |  |  |

* AVAILABLE: You have the permission to create products in this category.
* NON_MAIN_CATEGORY: This category is out of scope for this seller, and you do not have permission to use it. Contact your account manager for assistance. |

# 响应示例
```json
{"code":0,"data":{"categories":[{"id":"600001","parent_id":"0","local_name":"Home Supplies","is_leaf":false,"permission_statuses":["AVAILABLE"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12052023 | 分类 does not exist |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052700 | The seller is inactive. |
| 12052704 | seller id not exist |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

