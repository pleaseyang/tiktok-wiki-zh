# 更新价格

# 路径：/product/202309/products/{product_id}/prices/update
# 方法：[POST]
# 功能描述
更新处于 `ACTIVATE` 状态且未参与任何进行中促销活动的商品下多个 SKU 的价格。
**注意**: 由于没有额外的响应数据，`data` 响应字段始终为空。

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
| product_id | string | Y | 1729592969712207008 | TikTok Shop 生成的商品 ID。 |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| skus | []object | Y |  | 用于标识商品不同变体的 SKU（库存单位）列表。 |
| ^id | string | Y | 1729592969712207013 | TikTok Shop 生成的 SKU ID。一个商品可包含多个 SKU ID。 |
**注意**：

* 该 SKU ID 必须属于具有 `ACTIVATE` 状态的商品。
* 如果要更新多个 SKU, 所有 SKU ID 必须属于同一商品。 |
   ^price |object |Y | |SKU 定价信息。 |
   ^^amount |string |N |1.32 |**本地卖家/欧盟内部卖家**
   SKU 在商品页面上折扣前显示的**本地展示价格**。 Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

**全球卖家**
SKU 的**本地税前价格**。不含跨境配送费用、税费及其他适用费用等，因此不会显示在商品页面上。
Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

* **注意**：不适用于使用中国仓库的 JP 和 US 店铺，请改用 `price.sale_price`。 |
   ^^currency |string |Y |USD |货币。
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
   ^^sale_price |string |N |1.32 |**全球卖家**
   SKU 在商品页面上折扣前显示的**本地展示价格**。
   Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) 了解各市场允许的价格范围。

**注意**：

* 仅适用于全球卖家。
* 使用中国仓库的 JP 和 US 店铺必填，其他店铺可选。
* 这是商品页面上显示的最终确定价格，所有其他价格将被忽略。 |
   ^list_price |object |N | |SKU 的标价信息。这等同于制造商建议零售价（MSRP）或建议零售价（RRP）。
   仅适用于美国市场。

**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^amount |string |Y |1 |价格金额。
有效范围：[0.01, 7600]
**注意**：

* 该值必须等于或大于 `skus.price.amount`。否则将被丢弃。
* 如果该值经审核团队核实为合规，将被保存并在 [Get Product API](6509d85b4a0bb702c057fdda) 中返回。 |
   ^^currency |string |Y |USD |货币。
   可能的值： USD |
   ^external_list_prices |[]object |N | |SKU 标价（如 MSRP、RRP）或外部电商平台上的原价信息。
   仅适用于美国市场的部分卖家。

**注意**：此值可能显示为商品页面上的划线价。但是，是否显示划线价以及显示的金额需经审核团队根据各种定价信息审核决定。 |
^^source |string |Y |SHOPIFY_COMPARE_AT_PRICE |价格来源的外部电商平台。
可能的值：

* SHOPIFY_COMPARE_AT_PRICE: Shopify 中的 compare_at_price。 |
   ^^amount |string |Y |1 |价格金额。
   有效范围：[0.01, 7600] |
   ^^currency |string |Y |USD |货币。
   可能的值： USD |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/products/1729592969712207008/prices/update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"skus":[{"id":"1729592969712207013","price":{"amount":"1.32","currency":"USD","sale_price":"1.32"},"list_price":{"amount":"1","currency":"USD"},"external_list_prices":[{"source":"SHOPIFY_COMPARE_AT_PRICE","amount":"1","currency":"USD"}]}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
# 响应示例
```json
{"code":0,"data":{},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019022 | SKU 必须包含有效仓库。 |
| 12019045 | price is locked |
| 12019059 | seller sku is invalid |
| 12019113 | product status is invalid |
| 12052012 | Incorrect price format |
| 12052023 | 分类不存在 |
| 12052032 | 商品不存在 |
| 12052038 | Product price locked due to ongoing promotion. |
| 12052048 | 您无法编辑指定商品，因为它未在您的账户或店铺中上架。 |
| 12052073 | The product price is invalid |
| 12052084 | 所提供的货币不适用于该店铺/地区。 |
| 12052092 | product sale price is invalid |
| 12052096 | Unable to update the price for SKUs with no warehouse. Assign a warehouse and try again. |
| 12052097 | The warehouse does not exist |
| 12052163 | The gift product are not allowed to be edited |
| 12052260 | 商品 ID 不存在 |
| 12052308 | 当前存在进行中的申诉。如需编辑商品详情，请先撤销该申诉。 |
| 12052371 | Auction product is bidding when it is not supported to change product info |
| 12052376 | list price not support |
| 12052383 | product list price exceed limit |
| 12052424 | Missing 'sale price' value |
| 12052531 | The warehouse is disabled. |
| 12052553 | Sku id duplicate |
| 12052557 | The SKU ID does not belong to the product. |
| 12052570 | product price exceed limit |
| 12052572 | the sale price is invalid |
| 12052700 | 卖家不活跃。 |
| 12052703 | 卖家税号无效 |
| 12052704 | 卖家 ID 不存在 |
| 12052861 | The price of combined SKU cannot exceed the sum of the prices of the sub-SKUs. |
| 12052881 | identity 内部错误 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12052901 | 商品当前状态不支持此操作。请更改商品状态后重试。 |
| 12052902 | The SKU list is empty. Either omit the list entirely, or provide all required details. |
| 12052910 | 输入参数无效。请参阅 API 文档了解详情。 |

