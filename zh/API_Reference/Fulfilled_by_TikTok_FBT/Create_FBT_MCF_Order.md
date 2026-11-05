# 创建 FBT MCF 订单

# Path: /fbt/202607/mcf_outbound_orders
# Method: [POST]
# 功能描述
对于在其他销售渠道创建的需要通过 FBT 进行履约的订单，此 API 允许您创建相应的订单（以下简称 MCF 订单）。MCF 订单创建成功后，将自动提交至 FBT 系统进行履约。

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
| external_order_id | string | Y | shopify202208291503530001100220033 | 您 OMS 中对应的订单 ID。最大 UTF-8 长度：127 字节。它必须在同一商家的活跃 MCF 订单中唯一。重用活跃订单的 `external_order_id` 将被视为重复请求而被拒绝，不会作为幂等重试处理。 |
| goods | []object | Y |  | 订单中包含的商品 ID 和数量。数组必须至少包含一个商品，且每个商品必须在 FBT 系统中管理。`goods` 中所有条目的 `quantity` 之和不得超过 50。 |
| ^id | string | Y | 1234567 | Fulfilled by TikTok 系统生成的商品 ID。值必须为正整数的十进制字符串。 |
| ^quantity | int | Y | 1 | 此商品的数量。必须大于 0。 |
| consignee | object | Y |  | 收货人联系信息 |
| ^name | string | Y | username | 收货人姓名。不得超过 128 个 UTF-8 字节。 |
| ^phone_number | string | Y | (+1)1211223910 | 收货人电话号码 |
| ^email | string | Y | username@example.com | 收货人电子邮箱 |
| ^address | object | Y |  | 收货人地址必须是有效地址；如果地址验证失败，将不会创建订单。 |
| ^^country_code | string | Y | US | 收货人地址的国家代码，采用两位字符的 ISO 3166-1 alpha-2 格式。仅接受 `US`。 |
| ^^state_or_region | string | Y | Alabama | 收货人地址的州或地区 |
| ^^district_or_county | string | N | Baldwin | 收货人地址的区或县 |
| ^^city | string | Y | Bay Minette | 收货人地址的城市 |
| ^^address_line_1 | string | Y | 312 Courthouse Square | 详细地址行 1 |
| ^^address_line_2 | string | N | Suite 10 | 详细地址行 2 |
| ^^postal_code | string | N | 36507 | 收货人地址的 5 位美国 ZIP 代码。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202607/mcf_outbound_orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"external_order_id":"shopify202208291503530001100220033","goods":[{"id":"1234567","quantity":1}],"consignee":{"name":"username","phone_number":"(+1)1211223910","email":"username@example.com","address":{"country_code":"US","state_or_region":"Alabama","district_or_county":"Baldwin","city":"Bay Minette","address_line_1":"312 Courthouse Square","address_line_2":"Suite 10","postal_code":"36507"}}}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^mcf_order | object |  | 成功创建的 MCF 订单信息。在成功响应中，此对象包含 `mcf_order_id`、`external_order_id` 和 `create_time`。 |
| ^^external_order_id | string | shopify202208291503530001100220033 | 您 OMS 中对应的订单 ID。 |
| ^^mcf_order_id | string | 7136104329798256386 | 用于标识不同 MCF 订单的唯一 ID |
| ^^create_time | int | 1661756811 | MCF 订单创建时的 Unix 时间戳（秒）。 |
# 响应示例
```json
{"code":0,"data":{"mcf_order":{"external_order_id":"shopify202208291503530001100220033","mcf_order_id":"7136104329798256386","create_time":1661756811}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 177001001 | 缺少参数或参数格式不正确 |
| 177001002 | 商品数据在 FBT 系统中不存在。您必须提供有效的商品 ID；否则 FBT 系统无法履约该订单。 |
| 177001003 | 地址信息验证失败。请检查地址的有效性，确保您的地址准确，可通过 USPS ZIP 查询工具验证地址。 |
| 177001004 | inventory 不足，无法履约该订单。请补充 inventory 或通过其他方式安排配送。 |
| 177001006 | 商家没有创建外部订单的权限；请检查您的权限或联系平台。 |
| 177001007 | external_order_number 已与一个活跃的 MCF 订单关联。FBT 系统正在处理该订单的配送，不允许重复创建订单。 |
| 177001008 | 订单创建频率已超过限制；请降低调用频率或稍后重试。 |
| 177001009 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 177001010 | 无法通过您提供的 mcf_order_id 检索订单信息；请检查您的 ID 是否正确。 |
| 177001011 | 地址无法送达 |
| 177001012 | 订单已推送至履约系统，无法再次推送 |
| 177001013 | 无权限，请先支付 FBT 账单 |
| 177001014 | 邮政编码有误 |
| 177001015 | 新商品尚未到达 warehouse |
| 177001016 | 每个订单的最大商品数量不能超过 99 |

