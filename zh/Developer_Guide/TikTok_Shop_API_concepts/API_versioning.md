# API 版本管理

API 版本管理使 TikTok Shop 能够在 API 不断发展的同时持续改进和扩展 API 功能，并保持无缝的集成体验。
当 TikTok Shop API 引入破坏性变更时，这些变更将通过新的 API 版本发布。破坏性变更可能是改进功能、引入新能力或增强安全性所必需的。为了保持集成稳定并利用更新的功能，开发者应定期查看受支持的版本并在需要时进行升级。
有关非破坏性变更和破坏性变更的示例，请以 [变更日志](https://partner.tiktokshop.com/docv2/changelog) 为准，而不是依赖本页中的固定示例。变更日志条目会随时间更新，可能包括 API 更新、新端点发布、字段新增、迁移通知、破坏性变更和退役通知等类别。
# API 发布计划和版本命名
新的 API 版本通常按月发布，但并非每个 API 每月都会更新。
API 版本名称（如 `202303`）由该 API 版本发布的年份和月份衍生而来。
# 在 API 参考文档中选择 API 版本
API 版本在 API 级别分配，这意味着不同 API 在同一时间可能支持不同的版本列表。不要使用硬编码的示例来决定 API 的最新版本。
API 参考页面默认显示该 API 最新支持的版本。使用参考页面上的版本下拉菜单确认您正在调用的 API 当前支持哪些版本。通过点击下拉菜单中的版本名称，您可以访问该特定 API 版本的参考文档。
不同版本的不同 API 通常可以一起使用，但集成应经过全面测试。在大多数情况下，对每个端点使用 API 参考页面上显示的最新受支持版本。如果您的集成依赖多个相关 API，请在发布前测试版本组合。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fdd7aa43e905434bbca6f2d5b67b6a6d~tplv-k9wyc2ijk0-image.image)
# 调用 API 时指定 API 版本
从 `202309` API 风格开始，API 版本是请求路径的一部分。有关更多迁移详情，请参阅升级到 202309 以及方法和端点。
生成请求签名时，请完全按照 API 参考页面上显示的端点路径使用。
| API 风格 | URI 模式 | 版本位置 |
| --- | --- | --- |
| 旧版 API 风格 | `https://open-api.tiktokglobalshop.com/{legacy_resource}?version={version}&app_key={app_key}&timestamp={timestamp}&sign={sign}` | 查询参数 |
| `202309` 及更高版本 API 风格 | `https://open-api.tiktokglobalshop.com/{category}/{version}/{resource}?app_key={app_key}&timestamp={timestamp}&sign={sign}` | 路径段 |
`202309` 及更高版本 API 风格示例：
```HTTP
GET https://open-api.tiktokglobalshop.com/authorization/202309/shops?app_key={app_key}&timestamp={timestamp}&sign={sign}
```

计算 `202309` 及更高版本 API 的签名时，请包含主机后的完整路径，包括类别、版本和资源段，例如 `/authorization/202309/shops`。
# 升级到新的 API 版本
在升级到新的 API 版本之前，请阅读目标版本的变更日志和 API 参考文档。检查路径、方法、请求头、查询参数、请求体、响应体、错误码、字段含义、市场可用性和授权范围要求的变化。
使用 API 参考页面上的版本下拉菜单比较同一 API 的受支持版本。如果有单独的迁移指南（如升级到 202309），请将该指南与端点参考页面一起参考。
# API 版本退役
在新的 API 版本发布后，旧版本至少保持 2 个月的可用期。这是从新版本发布之日起计算的最短可用时间窗口。
当一个 API 版本计划永久退役时，退役公告将在永久退役日期前至少 2 个月通过 [变更日志](https://partner.tiktokshop.com/docv2/changelog) 发布。这是从永久退役日期倒推的退役通知窗口。
这两个 2 个月的时间窗口描述了不同的生命周期检查点。应按以下时间线理解：
| 时间线节点 | 发生事项 | 时间规则 |
| --- | --- | --- |
| 1. 新版本发布 | 更新的 API 版本在 API 参考页面上可用。 | 新版本生命周期的开始。 |
| 2. 旧版本最短可用期 | 旧版本在新版本发布后仍可调用。 | 新版本发布后至少 2 个月。 |
| 3. 退役公告 | 如果旧版本计划永久退役，将发布变更日志通知。 | 永久退役前至少 2 个月。 |
| 4. 永久退役 | 退役版本不再受支持。对该版本的调用可能会失败。 | 在变更日志中声明的退役日期生效。 |
如果您使用已退役或无效的版本，API 可能返回表示不支持该 API 版本的错误。
```JSON
{
  // 错误码表示版本名称无效
  "code": 36009014,
  "data": null,
  "message": "The version name is invalid, please check and retry."
}
```

一些常见的网关或旧版示例可能会出现 `36009004` 和 `Invalid API version` 消息，表示相同的一般情况。在运行时行为在文档和端点之间完全对齐之前，通过检查响应 `code` 和 `message` 文本来处理无效版本故障，并记录 `request_id` 以便排查问题。这应与常见错误保持一致。
# 保持更新
## 变更日志
[变更日志](https://partner.tiktokshop.com/docv2/changelog) 是 API 变更的主要来源，包括新版本、新端点、非破坏性更新、迁移通知、破坏性变更和退役通知。定期查看变更日志有助于您提前规划升级，避免调用已退役的版本。
