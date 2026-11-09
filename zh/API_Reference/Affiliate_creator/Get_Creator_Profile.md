# 获取达人资料

# 路径：/affiliate_creator/202508/profiles
# 方法：[GET]
# 功能描述
获取与 access token 关联的达人的资料信息。达人必须已配置销售区域；否则，请求将因前提条件错误而失败。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop APIs - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202508/profiles?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^avatar | object |  | 与 TikTok 达人个人资料头像相关的数据。 |
| ^^width | int | 100 | 头像图片宽度（像素）。 |
| ^^height | int | 100 | 头像图片高度（像素）。 |
| ^^url | string | https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d76b8cc1b598de90ad5048df46e672b3~c5_100x100.webp?x-expires=1691895600&x-signature=oAT9KOL7aCN3Did9U%2FoKEsbBDj0%3D | TikTok 达人头像图片文件的 URL。 |
| ^username | string | abc123 | TikTok 用户名。 |
| ^selection_region | string | US | 达人有资格在橱窗、视频和直播中推广商品的区域。 |
| ^register_region | string | US | 达人的 TikTok 账户注册区域。 |
| ^seller_type | string | LOCAL | 如果达人同时拥有 TikTok Shop 卖家账户，则为达人的卖家类型。这是枚举类型，取值如下： |

* CROSS_BORDER
* LOCAL |
   ^permissions |[]string |["LIVE_STREAM_PERMISSION","SELF_SALE_PERMISSION","ADD_AFFILIATE_PERMISSION"] |达人的商品推广权限列表。该列表可以包含零个或多个以下权限：
* LIVE_STREAM_PERMISSION
* SELF_SALE_PERMISSION
* ADD_AFFILIATE_PERMISSION
* PHOTO_SHOPPABLE_PERMISSION_PRODUCT
* PHOTO_SHOPPABLE_PERMISSION_SHOP |
   ^user_type |string |TIKTOK_SHOP_OFFICIAL_ACCOUNT |达人的用户类型。这是枚举类型，取值如下：
* TIKTOK_SHOP_OFFICIAL_ACCOUNT
* TIKTOK_MARKETING_ACCOUNT
* TIKTOK_SHOP_CREATOR |
   ^creator_user_open_id |string |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |Creator Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |

# 响应示例
```json
{"code":0,"data":{"avatar":{"width":100,"height":100,"url":"https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d76b8cc1b598de90ad5048df46e672b3~c5_100x100.webp?x-expires=1691895600\u0026x-signature=oAT9KOL7aCN3Did9U%2FoKEsbBDj0%3D"},"username":"abc123","selection_region":"US","register_region":"US","seller_type":"LOCAL","permissions":["LIVE_STREAM_PERMISSION","SELF_SALE_PERMISSION","ADD_AFFILIATE_PERMISSION"],"user_type":"TIKTOK_SHOP_OFFICIAL_ACCOUNT","creator_user_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop APIs - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
| 16015006 | 该达人当前没有选择区域。请联系达人并确保其当前拥有电商权限。 |
| 16015007 | 无销售区域错误；详情：达人没有销售区域。 |
| 16501011 | 用户没有权限访问此 API。请检查达人的认证信息。 |
| 16504002 | 查询达人信息失败。请检查达人的电商权限是否可用。 |
| 36009002 | 请求过多。您在短时间内发送了过多请求。 |

