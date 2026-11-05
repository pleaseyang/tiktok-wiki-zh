# 查询商品危险品和保质期信息

# Path: /fbt/202603/goods/hazmat_and_expiration_info/search
# Method: [POST]
# 功能描述
通过 TikTok Shop SKU ID 查询商品的危险品和保质期信息。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| tts_sku_ids | []string | Y | ["723456789012345678"] | TikTok Shop 系统生成的 Stock Keeping Unit（SKU）标识符 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202603/goods/hazmat_and_expiration_info/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"tts_sku_ids":["723456789012345678"]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^hazmat_and_expiration_info | object |  | 每个 SKU 的危险品、批次控制和保质期管理结果的容器。 |
| ^^hazmat_and_expiration_dto_list | []object |  | 每个 SKU 的危险品、批次控制和保质期管理结果。使用 `tts_sku_id` 将每个条目与请求的 SKU 关联。 |
| ^^^tts_sku_id | string | 723456789012345678 | TikTok Shop 系统生成的 Stock Keeping Unit（SKU）标识符 |
| ^^^is_hazmat | bool | false | 表示产品是否根据 FBT 规则被分类为危险品。 |

* `true`: The product is classified as hazardous material. Provide the required hazmat declaration through `hazmat_info` when calling **Create FBT Goods** or **Update FBT Goods Info**.
* `false`: The product is not classified as hazardous material. |
   ^^^is_lot_code |bool |true |if the product requires lot management based on FBT category rule
   TRUE:this product requires lot control
   FALSE:this product does not require lot control
   |
   ^^^is_expiration_management |bool |true |Indicates whether the product requires expiration management based on the FBT category rule.
   TRUE: this product requires expiration management.
   FALSE: this product does not require expiration management. |
   ^^^exp_base_info |object | |Expiration-management thresholds for the product associated with the SKU when `is_expiration_management` is `true`. |
   ^^^^inbound_cutoff_days |int |90 |The period before a product's expiration date when the warehouse will stop accepting inbound shipments.For example, if the product expiration date is December 1, 2024, and the inbound cutoff days are 20 days, then the warehouse will stop accepting inbound shipments for this product after November 11, 2024 (20 days before expiration) |
   ^^^^expiration_alert_days |int |80 |The period of time before expiration in which the platform will send expiration alerts. |
   ^^^^sales_cutoff_days |int |70 |The period before a product's expiration date when the inventory will no longer be available for sale. For example, if the product expiration date is December 1, 2024, and the sales cutoff days are 20 days, then the inventory will stop being available for sale after November 11, 2024 (20 days before expiration). |

# 响应示例
```json
{"code":0,"data":{"hazmat_and_expiration_info":{"hazmat_and_expiration_dto_list":[{"tts_sku_id":"723456789012345678","is_hazmat":false,"is_lot_code":true,"is_expiration_management":true,"exp_base_info":{"inbound_cutoff_days":90,"expiration_alert_days":80,"sales_cutoff_days":70}}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

