# 获取店铺组及相关店铺

# 路径：/卖家/202601/shop_groups
# 方法：[GET]
# 功能描述
获取已认证店铺的商品互通组及相关店铺。例如，一个组可以包含一家美国店铺和一家墨西哥店铺。

---


# 公共参数
有关公共参数，请参阅[如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | 是 | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/seller/202601/shop_groups?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^shop_group_data | object |  | 商品互通组信息 |
| ^^shop_group | object |  | 商品互通组的基本信息。当已认证店铺不属于任何组时，此对象将被省略。 |
| ^^^source | string | 1 | 用于区分商品互通组的创建来源。 |
| 如果是由美国本地卖家开设墨西哥店铺形成的商品互通组，枚举值为：'1 -> US_MX_ONBOARD' |  |  |  |
| 如果是由中国跨境卖家开设墨西哥店铺形成的商品互通组，枚举值为：'2 -> GS_POP'。 |  |  |  |
| ^^^shop_group_name | string | 店铺分组名称 A | 代表商品互通组的唯一名称 |
| ^^shops | []object |  | 商品互通组中的店铺。如果 `shop_group` 被省略，则列出与已认证店铺属于同一全球卖家的店铺。 |
| ^^^shop_id | string | 36123502970007 | 店铺的 ID。 |
| ^^^seller_id | string | 74901234567890 | 与店铺关联的全球卖家 ID。 |
| ^^^shop_name | string | 店铺名称 A | 店铺的名称。 |
| ^^^shop_region | string | US | 店铺运营所在区域 |
# 响应示例
```json
{"code":0,"data":{"shop_group_data":{"shop_group":{"source":"1","shop_group_name":"shop group name A"},"shops":[{"shop_id":"36123502970007","seller_id":"74901234567890","shop_name":"shop name A","shop_region":"US"}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅[如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 98001004 | 参数 {param_name} 无效。原因：{reason}。预期值：{expected_value} |


