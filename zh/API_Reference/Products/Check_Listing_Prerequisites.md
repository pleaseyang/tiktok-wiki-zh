# 检查上架前提条件

# 路径：/product/202312/prerequisites
# 方法：[GET]
# 功能描述
检查 TikTok 店铺是否准备好上架商品。
每个店铺在开始上架商品之前需要满足一系列 TikTok Shop 要求。在上架商品之前，使用此 API 检查您的店铺是否已满足所有要求。
**提示**：我们建议您在进行任何批量更新之前先运行此检查，以避免上架问题。例如，卖家可能将配送选项改为 "Shipped by 卖家"，却未添加配送模板，从而导致店铺无法上架商品。在这种情况下，接口会对 `SHIPPING_TEMPLATE` 检查项返回 `is_failed=true`，您可以提示卖家修复该问题。

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
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202312/prerequisites?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^check_results | []object |  | 检查店铺是否满足 TikTok Shop 要求的结果列表。 |
| ^^check_item | string | RETURN_WAREHOUSE | 店铺需要满足的要求。 |
| 可能的值： |  |  |  |

* SHOP_STATUS
* SHOP_TAX
* PICKUP_WAREHOUSE
* RETURN_WAREHOUSE
* DELIVERY_OPTION
* SHIPPING_TEMPLATE
* PRODUCT_QUANTITY_LIMIT
* EXTENDED_PRODUCER_RESPONSIBILITY
* BANk_ACCOUNT
* CONTACT_INFO
   |
   ^^is_failed |bool |true |标识店铺是否未通过 `check_item`。 |
   ^^fail_reasons |[]string |["Couldn't publish this product as you haven't set the return 仓库 for your shop. Add the return 仓库 information on TikTok Shop Seller Center first and try again."] |未通过特定 `check_item`。 |

# 响应示例
```json
{"code":0,"data":{"check_results":[{"check_item":"RETURN_WAREHOUSE","is_failed":true,"fail_reasons":["Couldn't publish this product as you haven't set the return warehouse for your shop. Add the return warehouse information on TikTok Shop Seller Center first and try again."]}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 33001002 | 内部错误 |

