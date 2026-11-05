# 获取品牌

# Path: /product/202309/brands
# Method: [GET]
# 功能描述
获取您店铺的品牌，包括内置品牌和使用 [Create Custom Brands API](650a0926f1fd3102b91bbfb0) 创建的任何自定义品牌。在创建或编辑产品时传递返回的品牌 ID，以将品牌与产品关联。

* To check if a brand is fully authorized for use in a specific product category, specify the **category ID**.
* To obtain the full list of brands that your shop can potentially use and their authorization status, omit the category ID. We recommend that you specify the **brand name** to narrow down the list of brands returned.
   **Key concept**
   您是否可以选择和显示品牌取决于品牌的授权状态、品牌被授权的分类，以及品牌是否被归类为 T1（需要事先品牌授权的国际知名品牌）。
   **- Brand selection rules**: You can only select the following types of brands during product creation/editing.
   * Authorized brands which contain the desired category (`authorized_status=AUTHORIZED` and `brand_status=AVAILABLE`)
   * Unauthorized non-T1 brands (`authorized_status=UNAUTHORIEZD` and `is_t1_brand=false`)
      **- Brand display rules**: Note however that brands will only appear on the product display page if the brand is authorized (`authorized_status=AUTHORIZED`) and available in the desired category (`brand_status=AVAILABLE`). This means that you need to obtain brand authorization for unauthorized non-T1 brands before they can be displayed. Obtain brand authorization or add categories to an authorized brand through TikTok Shop Seller Center > Qualification Center > Brand qualification.
      **For Tokopedia sellers**: You can select and display any returned brand on Tokopedia regardless of these rules.


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_id | string | N | 600006 | 指定分类 ID 以显示 **authorized brands** in the category. |
| **Note**: Specify this value to obtain an accurate list of brands that you can use in a category. |  |  |  |  |
| is_authorized | bool | N | false | 按品牌授权状态过滤结果。 |
| Possible values: |  |  |  |  |

* 1: Returns only authorized brands
* 0: Returns all brands |
   brand_name |string |N |Teas |过滤结果以包含以指定值开头的品牌名称。 |
   page_size |int |Y |100 |每页返回的结果数量。
   Valid range: [1-100] |
   page_token |string |N |cGFnZV9udW1iZXI9Mg== |用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
   category_version |string |N |v1 |按分类树版本过滤分类。Possible values based on region:
* US, EU and SEA: v2, represents the 7-level category tree.
   Important: For US, EU and SEA shops, you must pass v2 when using this API.
* Other regions: v1, represents the 3-level category tree.Default: v1 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/brands?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&category_id=600006&is_authorized=false&brand_name=Teas&page_size=100&page_token=cGFnZV9udW1iZXI9Mg==&category_version=v1
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^brands | []object |  | 符合查询条件的品牌列表。 |
| ^^id | string | 7082427311584347905 | 品牌 ID。 |
| ^^name | string | Teas | 品牌名称。 |
| ^^authorized_status | string | AUTHORIZED | 标识卖家是否已获得事先授权销售带有品牌商标、名称或标志的商品的状态。 |
| Possible values: |  |  |  |

* UNAUTHORIEZD
* AUTHORIZED

**Note**: If the brand is unauthorized, check `is_t1_brand` to determine if you can use it during product creation. |
^^is_t1_brand |bool |true |标识该品牌是否为 T1 品牌的标志，T1 品牌是指可能存在合规风险并要求卖家获得品牌授权的国际知名品牌。
**Note**:

* You cannot create products with unauthorized T1 brands.
* You can create products with unauthorized non-T1 brands, **but** the brand information will not appear on the product display page.
   You can obtain authorization by submitting the required qualifications through TikTok Shop Seller Center > Qualification Center > Brand qualification. |
   ^^brand_status |string |AVAILABLE |The availability of an **authorized brand** in the requested category.
   Possible values:
* AVAILABLE
* UNAVAILABLE

**Note**: Not applicable if you did not specify the category ID, or the brand is unauthorized. |
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
| 12052023 | 分类 does not exist |
| 12052217 | All region shops must use V2 categories. Check the documentation for further details. |
| 12052230 | 分类 version and categoryID are not matched. |
| 12052700 | The seller is inactive. |
| 12052704 | seller id not exist |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |

