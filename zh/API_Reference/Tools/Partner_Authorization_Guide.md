# 合作伙伴授权指南

# 合作伙伴授权的作用
合作伙伴授权后，应用可以使用合作伙伴授予的权限调用 **Affiliate Partner** API。
合作伙伴授权用于合作伙伴拥有的业务品类数据。目前，TikTok Shop Partner Center 仅支持 **Seller and Scalable Creator Match-Up (TAP)** 合作伙伴品类的此流程。有关支持的 endpoint 的更多信息，请参阅 **Affiliate Partner** API 参考文档。
# 授权域名概览
TikTok Shop 为卖家、达人和合作伙伴授权使用不同的授权入口域名。请使用与您要请求授权的数据所有者相匹配的授权指南。
| 授权类型 | 数据所有者 | 美国授权入口 | 其他地区授权入口 | 备注 |
| --- | --- | --- | --- | --- |
| 卖家授权 | 卖家 / 店铺 | `https://services.us.tiktokshop.com/open/authorize` | `https://services.tiktokshop.com/open/authorize` | 用于卖家拥有的店铺数据和卖家 API scope。 |
| 达人授权 | 达人 | `https://shop.tiktok.com/alliance` | `https://shop.tiktok.com/alliance` | 用于达人授权流程。完整路径和参数请遵循达人授权指南。 |
| 合作伙伴授权 | 合作伙伴 | `https://partner.us.tiktokshop.com/open/authorize` | `https://partner.tiktokshop.com/open/authorize` | 用于 Affiliate Partner API 和合作伙伴 API scope。 |
# 前提条件

1. 如果应用仍处于开发中，则应用只能接受应用所有者的授权。上线后，应用可以接受其他合作伙伴的授权。
2. 应用必须启用合作伙伴 API scope，即 scope key 中以 `partner` 开头的那些：

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/dec0b1025fc14dec8878e93266569436~tplv-k9wyc2ijk0-image.image)
# 授权链接
基本授权链接可以通过 **Copy authorization link** 按钮获取。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1700c2b084de4d4fac238f4a74de20b9~tplv-k9wyc2ijk0-image.image)
如果应用处于开发中，开发者需要使用应用的 `service_id` 手动生成授权链接。您可以在 **Partner Center > App & Service > 选择应用/服务 > Basic Information > Service ID** 中找到 `service_id`：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b919a650b24046c481b58fedf505d340~tplv-k9wyc2ijk0-image.image)
使用与合作伙伴所在地区匹配的授权域名：
| 合作伙伴地区 | 授权链接 |
| --- | --- |
| 美国 | `https://partner.us.tiktokshop.com/open/authorize?service_id={service_id}` |
| 其他地区 (ROW) | `https://partner.tiktokshop.com/open/authorize?service_id={service_id}` |
建议添加 `state` 参数，但合作伙伴授权不强制要求。请参阅 [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect#createxsrftoken) 文档以了解如何创建和确认 `state` 的示例。
# 获取和刷新 Token
合作伙伴批准授权后，TikTok Shop 会将合作伙伴重定向回应用配置的重定向 URL，并附带授权码。在调用 Affiliate Partner API 之前，请将此授权码换取 access token。

1. 从重定向 URL 接收授权码。
2. 从您的后端服务调用 token API：

```HTTP
# 使用授权码获取 access token
GET https://auth.tiktok-shops.com/api/v2/token/get?app_key={app_key}&app_secret={app_secret}&auth_code={auth_code}&grant_type=authorized_code
```

成功响应包含 `access_token`、`access_token_expire_in`、`refresh_token`、`refresh_token_expire_in` 和 `granted_scopes`。请在服务端安全存储 token。不要在前端代码中暴露 `app_secret`、`access_token` 或 `refresh_token`。
在调用 Affiliate Partner API 时，在 `x-tts-access-token` 请求 header 中使用 `access_token`。在调用合作伙伴品类 API 之前，请先调用 **Get Authorized Category Assets** 以确认已授权的业务品类并获取品类资产 cipher：
```HTTP
# 获取已授权的品类资产
GET /authorization/202405/category_assets
Header: x-tts-access-token: {access_token}
```

返回的 `category_assets[].cipher` 标识已授权的合作伙伴品类资产，用作 Affiliate Partner API 的输入参数。
当 access token 过期时，使用 refresh token 刷新它：
```HTTP
# 使用 refresh token 刷新 access token
GET https://auth.tiktok-shops.com/api/v2/token/refresh?app_key={app_key}&app_secret={app_secret}&refresh_token={refresh_token}&grant_type=refresh_token
```

如果 refresh token 过期或合作伙伴取消了授权，请要求合作伙伴重新授权应用。
# 合作伙伴要求
合作伙伴授权仅授予访问合作伙伴所授权且应用被批准访问的业务品类数据的权限。目前，Partner Center 仅公开 **Seller and Scalable Creator Match-Up (TAP)** 品类的合作伙伴授权；它不授予访问不相关的合作伙伴业务数据的权限。
合作伙伴必须已成功加入 **Seller and Scalable Creator Match-Up (TAP)**：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/445e0f8141aa4417b224109f48263772~tplv-k9wyc2ijk0-image.image)
确保用户在授权页面上选择 **Seller and Scalable Creator Match-Up (TAP)**。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/ffeba3cb3bd74f029a7e4f9d537441e6~tplv-k9wyc2ijk0-image.image)
# 取消授权
合作伙伴可以从 **My account > My authorizations** 取消授权。
取消后，应用应停止为该合作伙伴调用合作伙伴 API，将现有 token 视为无效，如果仍需要访问则要求合作伙伴重新授权。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/46cf0e4a4a7647e0a811101fec97367b~tplv-k9wyc2ijk0-image.image)
