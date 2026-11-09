# 获取品牌

# 路径：/product/202309/brands
# 方法：[GET]
# 功能描述
获取您店铺的品牌，包括内置品牌和使用 [Create Custom Brands API](650a0926f1fd3102b91bbfb0) 创建的任何自定义品牌。在创建或编辑商品时传递返回的品牌 ID，以将品牌与商品关联。

* 要检查品牌是否在特定商品类目中已完全授权，请指定**类目 ID**。
* 要获取店铺可能使用的全部品牌及其授权状态，请省略类目 ID。建议指定**品牌名称**以缩小返回的品牌列表范围。
   **Key concept**
   您是否可以选择和显示品牌取决于品牌的授权状态、品牌被授权的分类，以及品牌是否被归类为 T1（需要事先品牌授权的国际知名品牌）。
   **- 品牌选择规则**: 创建/编辑商品时只能选择以下类型的品牌。
   * 包含所需类目的已授权品牌（`authorized_status=AUTHORIZED` 且 `brand_status=AVAILABLE`）
   * 未授权的非 T1 品牌（`authorized_status=UNAUTHORIEZD` 且 `is_t1_brand=false`）
      **- 品牌展示规则**: 但请注意，只有当品牌已授权（`authorized_status=AUTHORIZED`）且在所需类目中可用（`brand_status=AVAILABLE`）时，品牌才会显示在商品展示页上。这意味着需要先为未授权的非 T1 品牌获取品牌授权，才能展示它们。可通过 TikTok Shop Seller Center > Qualification Center > Brand qualification 获取品牌授权或为已授权品牌添加类目。
      **针对 Tokopedia 卖家**: 无论这些规则如何，您都可以在 Tokopedia 上选择并展示任何返回的品牌。


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
| category_id | string | N | 600006 | 指定分类 ID 以显示 **authorized brands** in the category。 |
| **注意**: 指定此值可获取可在某一类目中使用的品牌的准确列表。 |  |  |  |  |
| is_authorized | bool | N | false | 按品牌授权状态过滤结果。 |
| 可能的值： |  |  |  |  |

* 1: 仅返回已授权品牌
* 0: 返回所有品牌 |
   brand_name |string |N |Teas |过滤结果以包含以指定值开头的品牌名称。 |
   page_size |int |Y |100 |每页返回的结果数量。
   有效范围： [1-100] |
   page_token |string |N |cGFnZV9udW1iZXI9Mg== |用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
   category_version |string |N |v1 |按分类树版本过滤分类。基于地区的可能值：
* US、EU 和 SEA: v2，代表 7 级分类树。
   重要提示：对于 US、EU 和 SEA 店铺，使用此 API 时必须传递 v2。
* 其他地区: v1，代表 3 级分类树。默认值：v1 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/brands?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&category_id=600006&is_authorized=false&brand_name=Teas&page_size=100&page_token=cGFnZV9udW1iZXI9Mg==&category_version=v1
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^brands | []object |  | 符合查询条件的品牌列表。 |
| ^^id | string | 7082427311584347905 | 品牌 ID。 |
| ^^name | string | Teas | 品牌名称。 |
| ^^authorized_status | string | AUTHORIZED | 标识卖家是否已获得事先授权销售带有品牌商标、名称或标志的商品的状态。 |
| 可能的值： |  |  |  |

* UNAUTHORIEZD
* AUTHORIZED

**注意**: 如果品牌未授权，请检查 `is_t1_brand` 以确定是否可在创建商品时使用。 |
^^is_t1_brand |bool |true |标识该品牌是否为 T1 品牌的标志，T1 品牌是指可能存在合规风险并要求卖家获得品牌授权的国际知名品牌。
**注意**：

* 不能使用未授权的 T1 品牌创建商品。
* 可以使用未授权的非 T1 品牌创建商品，**但**品牌信息不会显示在商品展示页上。
   可通过 TikTok Shop Seller Center > Qualification Center > Brand qualification 提交所需资质来获取授权。 |
   ^^brand_status |string |AVAILABLE |**已授权品牌**在请求类目中的可用性。
   可能的值：
* AVAILABLE
* UNAVAILABLE

**注意**: 如果未指定类目 ID，或品牌未授权，则不适用。 |
^total_count |int |10000 |符合查询条件的品牌总数。 |
^next_page_token |string |cGFnZV9udW1iZXI9Mg== |用于获取分页结果集下一页的不透明 token。如果此值非空，请将其传递给下一个请求的 `page_token` 参数。空值表示没有更多结果。 |
# 响应示例
```json
{"code":0,"data":{"brands":[{"id":"7082427311584347905","name":"Teas","authorized_status":"AUTHORIZED","is_t1_brand":true,"brand_status":"AVAILABLE"}],"total_count":10000,"next_page_token":"cGFnZV9udW1iZXI9Mg=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019108 | page number is invalid |
| 12019109 | page size is invalid |
| 12019123 | product of pageSize and pageNumber exceeds the maximum limit |
| 12019124 | pageSize and pageNumber need to be used together |
| 12052023 | 分类不存在 |
| 12052217 | 所有地区的店铺必须使用 V2 分类。请查看文档了解更多详情。 |
| 12052230 | 分类版本与 categoryID 不匹配。 |
| 12052700 | 卖家不活跃。 |
| 12052704 | 卖家 ID 不存在 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

