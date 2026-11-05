# 获取已授权类目资产

# Path: /authorization/202405/category_assets
# Method: [GET]
# 功能描述
获取合作方为应用授权的商业类目资产列表。
在应用访问合作方数据之前，需要获得合作方的授权，该授权基于商业类目授予。使用此 API 可以查看当前为应用授权的商业类目资产，并获取相应的类目资产 cipher，用作 affiliate 合作方相关 API 的输入参数。
有关合作方授权的更多信息，请参阅[合作方授权指南](678e3a3978f4c20311b8b555)。
目标合作方：所有

---


# 公共参数
有关公共参数，请参阅[如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | 是 | application/json | 允许类型：application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/authorization/202405/category_assets?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^category_assets | []object |  | 合作方为应用授权的商业类目资产列表。 |
| ^^cipher | string | TTP_XF90igAAAABh0sddwer0qsWgt233vOiG | 此已授权商业类目及目标市场的加密类目资产 cipher。将其用作 affiliate 合作方相关 API 的输入参数；您无需对其进行解密。 |
| ^^target_market | string | US | 与此已授权商业类目及其类目资产 cipher 关联的目标市场。 |
| ^^category | object |  | 商业类目信息。 |
| ^^^id | int | 3 | 商业类目的 ID。使用此字段验证合作方是否已授权正确的类目。否则，请参阅[合作方授权指南](https://partner.tiktokshop.com/docv2/page/669a301bd92cd602fd403ff9)向合作方请求重新授权。 |
| ^^^name | string | Customer Support | 商业类目的名称。此名称可能会更改。 |
# 响应示例
```json
{"code":0,"data":{"category_assets":[{"cipher":"TTP_XF90igAAAABh0sddwer0qsWgt233vOiG","target_market":"US","category":{"id":3,"name":"Customer Support"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅[如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |


