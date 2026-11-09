# 获取 Widget Token

# 概述
使用 **Get Widget Token** 生成用于 TikTok Shop Widget SDK 集成的短期 `widget_token`。
Token 流程如下：
| 步骤 | 角色 | Token 或接口 | 目的 |
| --- | --- | --- | --- |
| 1 | 卖家和开发者后端 | `access_token` | 卖家授权应用，开发者后端通过 TikTok Shop 授权流程获取 access token。 |
| 2 | 开发者后端 | `GET /authorization/202401/widget_token` | 后端使用签名查询参数和 `x-tts-access-token` 头调用此 Open API。 |
| 3 | TikTok Shop Open API | `widget_token` | API 返回短期 widget token。通常约 5 分钟后过期。 |
| 4 | 开发者后端和前端 | 开发者自有的 token 端点，例如 `/api/widget-token` | 后端将 widget token 返回给前端。不要将卖家 `access_token` 或 App Secret 暴露给前端代码。 |
| 5 | 前端 Widget SDK | `getToken` 回调 | 前端 SDK 使用 widget token 加载和调用 widget 服务。 |

`access_token` 和 `widget_token` 是不同的凭证。`access_token` 由开发者后端用于调用 TikTok Shop Open API。`widget_token` 是传递给 Widget SDK 的短期 token。
# API 端点
| 项目 | 值 |
| --- | --- |
| API 名称 | 获取 Widget 令牌 |
| API 版本 | `202401` |
| Host | `https://open-api.tiktokglobalshop.com` |
| Method | `GET` |
| Path | `/authorization/202401/widget_token` |
| 请求体 | 无 |
| 认证 | 签名通用查询参数加 `x-tts-access-token` 头 |
# 域名与接口范围
为集成的各部分使用正确的域名或接口。
| 域名或接口 | 用途 | 调用方 |
| --- | --- | --- |
| `https://open-api.tiktokglobalshop.com` | TikTok Shop Open API 资源服务器。使用此 host 调用 `GET /authorization/202401/widget_token`。 | 开发者后端 |
| `https://partner.tiktokshop.com` 和 `https://partner.us.tiktokshop.com` | Partner Center、文档、应用配置、卖家授权入口、API Testing Tool 和支持工单。 | 浏览器中的开发者 / 授权流程 |
| `/api/v1/seller/widget/get` | Widget SDK 指南和 SDK 故障排除中提到的 Widget SDK 端接口。不要将其用作生成 widget token 的 Open API 端点。 | Widget 运行时 / SDK 端服务 |
# 请求头
| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `x-tts-access-token` | string | 是 | 通过 TikTok Shop 授权流程获取的卖家 access token。此 token 必须属于将使用 widget 的卖家/店铺。 |
| `Content-Type` | string | 是 | 使用 `application/json`。 |
# 查询参数
此 API 没有必需的业务请求参数。正常调用仅使用通用签名查询参数。
| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `app_key` | string | 是 | 在 Partner Center 中分配给您的应用的唯一密钥。 |
| `timestamp` | int64 | 是 | Unix 时间戳（秒）。生成 `sign` 时必须使用相同的 timestamp 值。 |
| `sign` | string | 是 | 由请求路径、查询参数、请求体（如有）和 App Secret 生成的签名。参见 [签名您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。 |
| `shop_id` | int64 | 否 | API 模式中为可选，正常调用不需要。卖家/店铺上下文从 `x-tts-access-token` 解析。除非 TikTok Shop 支持或 API Testing Tool 明确要求，否则不要传递此参数。 |
# 请求示例
```Bash
curl --location --request GET 'https://open-api.tiktokglobalshop.com/authorization/202401/widget_token?app_key=<your_app_key>&timestamp=<unix_timestamp>&sign=<signature>' \
  --header 'Content-Type: application/json' \
  --header 'x-tts-access-token: <seller_access_token>'
```

# 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `code` | int32 | 是 | API 响应中返回的成功或失败状态码。 |
| `message` | string | 是 | 成功消息或失败原因。 |
| `request_id` | string | 是 | 请求日志 ID。联系技术支持时请提供此值。 |
| `data` | object | 否 | 响应数据。 |
| `data.widget_token` | object | 否 | Widget token 信息。 |
| `data.widget_token.token` | string | 否 | 传递给 Widget SDK 的短期 token。 |
| `data.widget_token.expire_at` | int64 | 否 | Widget token 的过期时间戳。Widget token 通常约 5 分钟后过期。 |
# 响应示例
```JSON
{
  "code": 0,
  "data": {
    "widget_token": {
      "token": "<widget_token>",
      "expire_at": 1703100448
    }
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

# 前端 SDK 交接
您的前端应调用自己的后端端点获取 widget token。后端应调用 TikTok Shop Open API 并仅返回短期 widget token 信息。
```TypeScript
async function getWidgetToken() {
  const response = await fetch('/api/widget-token', {
    method: 'GET',
    credentials: 'include'
  });
  const result = await response.json();

  if (result.code !== 0) {
    throw new Error(result.message || '获取 widget token 失败');
  }

  return result.data.widget_token;
}
```

配置 `@tiktokshop/widget-kit` 或 `@tiktokshop/widget-kit-react` 时，将此函数传递给 SDK 的 `getToken` 字段。前端 SDK 应收到包含 `token` 和 `expire_at` 的值。
# 错误码
| 错误码 | 错误消息 | 含义 | 建议操作 |
| --- | --- | --- | --- |
| `98001001` | `internal error` | 服务无法获取授权或店铺上下文。 | 使用指数退避重试。如果错误持续，联系 TikTok Shop 技术支持并提供 `request_id`、app key、市场、时间戳和完整响应。 |
| `98001004` | `Invalid param` | 必需的查询参数或头缺失、无效或与生成的签名不一致。 | 检查 `app_key`、`timestamp`、`sign`、`x-tts-access-token`、`Content-Type`、端点路径和 API 版本。确认确切请求 URL 后重新生成签名。 |
| `13002013` | `Seller does not exist` | access token 未映射到此 API 调用的有效授权卖家/店铺。 | 确认卖家已授权应用，使用正确的卖家 `access_token`，必要时刷新或重新授权，并使用 Get Authorized Shops 验证授权店铺映射。 |

Widget SDK 错误与此 Open API 响应分开处理。例如，`/api/v1/seller/widget/get` 的错误（如域名白名单不匹配、widget token 过期、widget token 无效、app key 不匹配或店铺/地区不匹配）应在 Widget SDK 集成层进行调试。
# 测试
您可以在 [API Testing Tool](https://partner.tiktokshop.com/docv2/page/api-testing-tool) 或使用 cURL 等命令行客户端测试此 API。
测试前：

1. 确认应用已创建且 App Key 正确。
2. 完成卖家授权并获取有效的卖家 `access_token`。
3. 使用确切的请求路径和查询参数生成 `sign` 值。
4. 在请求头中传递 `x-tts-access-token`。
5. 收到 `widget_token` 后，验证前端 SDK 的 `getToken` 回调返回包含 `token` 和 `expire_at` 的对象。

# 相关页面
| 页面 | 用途 |
| --- | --- |
| [授权指南](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) | 卖家授权和 access token 流程。 |
| [签名您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | 签名生成规则。 |
| [API Testing Tool](https://partner.tiktokshop.com/docv2/page/api-testing-tool) | 在 Partner Center 中测试 Open API 请求。 |
| [Widget SDK 用户指南](https://partner.tiktokshop.com/docv2/page/widget-sdk-user-guide) | 前端 SDK 集成和 `getToken` 回调使用。 |
