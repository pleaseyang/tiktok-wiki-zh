# 更新 Package 配送状态

# 路径：/fulfillment/202309/packages/deliver
# 方法：[POST]
# 功能描述
使用此 API 报告 SOF（卖家 Own Fleet）package 的配送结果或确认 O2O（门店自提）package 的配送。对于 SOF，使用 `DELIVERY_SUCCESS`、`DELIVERY_FAILED` 或 `UPDATE_POD`。对于 O2O，使用 `DELIVERY_SUCCESS` 并提供取货验证码。仅使用 SOF 或 O2O 的卖家可以使用此 API。此 API 仅在东南亚地区可用。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| packages | []object | Y |  | 要更新的 package。至少提供一个 package。 |
| ^id | string | Y | 11529598723402 | Package ID。 |
| ^delivery_type | string | Y | DELIVERY_SUCCESS | Package 的配送状态。 |
| 门店自提的可能值： |  |  |  |  |

* `DELIVERY_SUCCESS`：package 已成功送达。
   SOF（卖家 Own Fleet）的可能值：
* `DELIVERY_SUCCESS`：package 已成功送达。
* `DELIVERY_FAILED`：package 无法成功送达。
* `UPDATE_POD`：更新已送达 package 的附件。 |
   ^fail_delivery_reason |string |N |INVALID_ADDRESS |配送失败原因。

当 `delivery_type = DELIVERY_FAILED` 时，此字段必填。对于其他配送类型，此字段不必填。
可能的值：

* `INVALID_ADDRESS`：买家 shipping 地址无效。
* `UNABLE_RECEIVE`：买家目前无法接收配送。
* `UNABLE_CONTACT_BUYER`：无法联系买家。
* `BUYER_REFUSED`：买家拒绝接收商品。
* `DELAY_DELIVERY`：配送延迟。
* `PACKAGE_LOST`：package 丢失。
* `PACKAGE_DAMAGE`：package 损坏。
* `FORCE_MAJEURE`：发生了不可预见的不可抗力事件。
* `OTHER`：其他原因。
   |
   ^file_type |string |N |IMG |附件类型：
* `IMG`
* `PDF` |
   ^file_url |string |N |https://tiktok.shopcenter.cn/file/CWvBsBZ9mhbMiHtmbZecKshon6f?table=tblTW |附件 URL。
   卖家可以使用 [Upload Delivery File](https://partner.tiktokshop.com/docv2/page/650aa6e04a0bb702c06dcd34?external_id=650aa6e04a0bb702c06dcd34#Back%20To%20Top) 和 [Upload Delivery Image](https://partner.tiktokshop.com/docv2/page/650aa70d0fcef602bf32772f?external_id=650aa70d0fcef602bf32772f) API 生成 URL。附件将由 TikTok Shop 用于验证 package 配送。 |
   ^verification_code |string |N |123456 |订单取货所需的验证码。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/deliver?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"packages":[{"id":"11529598723402","delivery_type":"DELIVERY_SUCCESS","fail_delivery_reason":"INVALID_ADDRESS","file_type":"IMG","file_url":"https://tiktok.shopcenter.cn/file/CWvBsBZ9mhbMiHtmbZecKshon6f?table=tblTW","verification_code":"123456"}]}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^errors | []object |  | 批量请求中的 package 级别失败。每个条目标识受影响的 package 并包含返回的失败代码和消息字段。即使顶级响应 code 为 `0`，也请检查此列表。 |
| ^^code | int | 10007014 | 失败原因代码。 |
| ^^message | string | order not in sof service | Fulfillment 失败原因。 |
| ^^detail | object |  | 错误详情。 |
| ^^^package_id | string | 1231231231231 | Package ID。 |
# 响应示例
```json
{"code":0,"data":{"errors":[{"code":10007014,"message":"order not in sof service","detail":{"package_id":"1231231231231"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 21001011 | 系统处理错误，请稍后重试。 |
| 21011028 | 该 package 不属于当前店铺。请确保您提供了正确的 package ID 和/或 shop cipher。 |
| 21042247 | 您输入的验证码不正确。请重试。 |
| 21042248 | 已达到最大尝试次数。请在 30 分钟后重试。 |
| 21042252 | 订单状态异常，无法更新配送状态，请稍后重试。 |

