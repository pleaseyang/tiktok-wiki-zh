# 获取分类

# 路径：/product/202309/categories
# 方法：[GET]
# 功能描述
获取您的店铺可用的商品分类列表。
商品分类经常更新，因此建议实时调用 API 以确保使用最新的分类数据。在本地缓存分类数据可能导致使用过时的信息，从而在创建商品时导致错误。
**针对印度尼西亚市场**：要在 TikTok Shop 和 Tokopedia 同时上架商品，请仅使用两个平台都支持的类目。调用此接口一次并将 `listing_platform` 设为 `TIKTOK_SHOP`，再调用一次将其设为 `TOKOPEDIA`，然后确定两次调用返回的类目。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| locale | string | N | en-US | 用于显示分类信息的 BCP-47 语言环境代码。 |
| Default: 您店铺的默认语言环境。 |  |  |  |  |
| 可能的值： |  |  |  |  |

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
   keyword |string |N |electronics |使用此关键词过滤分类 `local_name`。 |
   category_version |string |N |v1 |按分类树版本过滤分类。基于地区的可能值：
* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |
   listing_platform |string |N |TIKTOK_SHOP |按指定平台过滤分类。
   可能的值：
* TIKTOK_SHOP
* TOKOPEDIA
   默认值：TIKTOK_SHOP

仅适用于从 Tokopedia 迁移的卖家。 |
include_prohibited_categories |bool |N |false |标识是否包含 TikTok Shop 禁止的分类。 Set this to `true` to identify which are the product categories that you can't list on TikTok Shop in any circumstances。
仅适用于 BR、MX、EU 和 SEA 市场。 |
is_live_quick |bool |N |false |false — 常规商品
true — LIVE_QUICK 商品。只有具有所需权限的卖家才能创建 LIVE_QUICK 商品。
默认值：false |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/categories?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&keyword=electronics&category_version=v1&listing_platform=TIKTOK_SHOP&include_prohibited_categories=false&is_live_quick=false
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^categories | []object |  | 符合查询条件的分类列表。 |
| ^^id | string | 600002 | 分类 ID。 |
| ^^parent_id | string | 600001 | 父分类 ID。 |
| 对于根分类，父 ID 为 `0`。 |  |  |  |
| ^^local_name | string | Home Supplies | 请求语言环境中的分类名称。如果 `locale` 被省略，则使用您店铺的默认语言环境。 |
| ^^is_leaf | bool | false | 标识该分类是否为叶子分类的标志。 |
**注意**： 您只能创建或编辑属于叶子分类的商品。 |
^^permission_statuses |[]string |["INVITE_ONLY", "NON_MAIN_CATEGORY"] |该店铺的此分类权限状态。
可能的值：

* `AVAILABLE`: 下列类目权限限制均不适用于该类目。要在该类目中创建或编辑商品，`is_leaf` 必须为 `true`。
* `INVITE_ONLY`: 这是受限类目，您无权使用。请通过 TikTok Shop Seller Center 上的 Qualification Center 提交申请以获取权限。在 Seller Center 中，`INVITE_ONLY` 也称为 "restricted"。
* `NON_MAIN_CATEGORY`: 该类目不在本店铺经营范围内，您无权使用。请联系您的客户经理寻求帮助。
* `PROHIBITED`：该类目在 TikTok Shop 上被禁止。请勿尝试在此类目下上架商品，因为它们将在审核中被拒绝。仅适用于 BR, MX, EU 和 SEA 市场。 |

# 响应示例
```json
{"code":0,"data":{"categories":[{"id":"600002","parent_id":"600001","local_name":"Home Supplies","is_leaf":false,"permission_statuses":["INVITE_ONLY","NON_MAIN_CATEGORY"]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019210 | 发布参数无效 |
| 12052023 | 分类不存在 |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052700 | 卖家不活跃。 |
| 12052704 | 卖家 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

