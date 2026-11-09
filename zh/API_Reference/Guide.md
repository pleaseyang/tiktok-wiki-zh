# 合作伙伴授权指南

# 合作伙伴授权的作用是什么？
完成合作伙伴授权后，应用即可在该合作伙伴授予的权限范围内调用 **Affiliate Partner** 接口。
合作伙伴授权用于访问合作伙伴自有的业务类目数据。目前 TikTok Shop 合作伙伴中心仅对 **Seller and Scalable Creator Match-Up (TAP)** 这一合作伙伴类目支持该授权流程。有关支持的端点，请参阅 **Affiliate Partner** API 参考。
# 授权域名概览
TikTok Shop 针对卖家、达人和合作伙伴授权使用不同的授权入口域名。请根据你要申请授权的数据归属方，选择对应的授权指南。
| 授权类型 | 数据归属方 | 美国授权入口 | ROW 授权入口 | 说明 |
| --- | --- | --- | --- | --- |
| 卖家授权 | 卖家 / 店铺 | `https://services.us.tiktokshop.com/open/authorize` | `https://services.tiktokshop.com/open/authorize` | 用于卖家自有的店铺数据及卖家 API 权限范围。 |
| 达人授权 | 达人 | `https://shop.tiktok.com/alliance` | `https://shop.tiktok.com/alliance` | 用于达人授权流程。完整路径与参数请遵循达人授权指南。 |
| 合作伙伴授权 | 合作伙伴 | `https://partner.us.tiktokshop.com/open/authorize` | `https://partner.tiktokshop.com/open/authorize` | 用于 Affiliate Partner 接口及合作伙伴 API 权限范围。 |
# 前置要求

1. 若应用仍在开发中，只能接受应用所有者的授权；应用上线后，才能接受其他合作伙伴的授权。
2. 应用必须启用合作伙伴 API 权限范围，即 scope key 中以 `partner` 开头的权限：

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/dec0b1025fc14dec8878e93266569436~tplv-k9wyc2ijk0-image.image)
# 授权链接
可通过 **Copy authorization link**（复制授权链接）按钮获取基础授权链接。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1700c2b084de4d4fac238f4a74de20b9~tplv-k9wyc2ijk0-image.image)
若应用仍在开发中，开发者需使用应用的 `service_id` 手动生成授权链接。`service_id` 可在 **合作伙伴中心 > App & Service > 选择应用/服务 > Basic Information > Service ID** 中找到：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b919a650b24046c481b58fedf505d340~tplv-k9wyc2ijk0-image.image)
请使用与合作伙伴所在地区相匹配的授权域名：
| 合作伙伴地区 | 授权链接 |
| --- | --- |
| 美国 | `https://partner.us.tiktokshop.com/open/authorize?service_id={service_id}` |
| 其他市场（ROW） | `https://partner.tiktokshop.com/open/authorize?service_id={service_id}` |
建议添加 `state` 参数，但合作伙伴授权并不强制要求。创建与校验 `state` 的示例参见 [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect#createxsrftoken) 文档。
# 获取与刷新令牌
合作伙伴同意授权后，TikTok Shop 会携带授权码将其重定向回应用配置的回调 URL。调用 Affiliate Partner 接口前，请先用该授权码换取访问令牌。

1. 从回调 URL 中获取授权码。
2. 在后端服务中调用令牌接口：

```HTTP
GET https://auth.tiktok-shops.com/api/v2/token/get?app_key={app_key}&app_secret={app_secret}&auth_code={auth_code}&grant_type=authorized_code
```

成功响应包含 `access_token`、`access_token_expire_in`、`refresh_token`、`refresh_token_expire_in` 和 `granted_scopes`。请在服务端安全存储令牌，不要在前端代码中暴露 `app_secret`、`access_token` 或 `refresh_token`。
调用 Affiliate Partner 接口时，请在 `x-tts-access-token` 请求头中传入 `access_token`。调用合作伙伴类目接口前，需先调用 **Get Authorized Category Assets** 确认已授权的业务类目并获取类目资产 cipher：
```HTTP
GET /authorization/202405/category_assets
Header: x-tts-access-token: {access_token}
```

返回的 `category_assets[].cipher` 用于标识已授权的合作伙伴类目资产，并作为 Affiliate Partner 接口的入参。
访问令牌过期时，使用刷新令牌进行刷新：
```HTTP
GET https://auth.tiktok-shops.com/api/v2/token/refresh?app_key={app_key}&app_secret={app_secret}&refresh_token={refresh_token}&grant_type=refresh_token
```

若刷新令牌已过期，或合作伙伴取消了授权，请让合作伙伴重新授权应用。
# 合作伙伴要求
合作伙伴授权仅允许访问该合作伙伴已授权、且应用已获批准访问的业务类目数据。目前合作伙伴中心仅为 **Seller and Scalable Creator Match-Up (TAP)** 类目提供合作伙伴授权，不会授予无关的合作伙伴业务数据访问权限。
合作伙伴必须已成功入驻 **Seller and Scalable Creator Match-Up (TAP)**：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/445e0f8141aa4417b224109f48263772~tplv-k9wyc2ijk0-image.image)
请确认用户在授权页面上选择了 **Seller and Scalable Creator Match-Up (TAP)**。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/ffeba3cb3bd74f029a7e4f9d537441e6~tplv-k9wyc2ijk0-image.image)
# 取消授权
合作伙伴可在 **My account > My authorizations** 中取消授权。
取消授权后，应用应停止为该合作伙伴调用合作伙伴接口，将已有令牌视为无效；若仍需访问，请让合作伙伴重新授权。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/46cf0e4a4a7647e0a811101fec97367b~tplv-k9wyc2ijk0-image.image)
