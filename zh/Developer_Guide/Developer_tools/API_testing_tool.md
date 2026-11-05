# API 测试工具

API 测试工具帮助开发者在 Partner Center 中测试 TikTok Shop Open API。它允许你选择 API、填写请求参数、发送测试请求、检查响应，以及在使用自己的 app key 测试时复制生成的示例代码。
# 功能更新
功能更新说明维护在[更新日志](https://partner.tiktokshop.com/docv2/changelog)中。请勿将本页上的 dated 示例视为工具的最新状态。请使用更新日志和实时的 API 测试工具 UI 作为新发布的测试功能、支持的 API 版本和工具行为变更的真实来源。
# 在调用任何 API 之前
> **重要提示：** 大多数 API 测试工具失败是由缺少 API scope 或缺少商家/店铺授权导致的。在使用你自己的 app key 进行测试之前，请确保应用已拥有所需的 API scope，并且商家或测试店铺已授权该 scope。

调用前检查清单：

1. 打开 endpoint 参考页面，确认所需的 API scope。
2. 在 Partner Center Console 中，前往你的应用的 **App & Service > Manage > Manage API**。
3. 确认所需的 scope 已为应用启用或批准。
4. 完成应用对商家/测试店铺的授权。
5. 如果你手动获取 access token，确认 token 响应的 `granted_scopes` 包含所需的 scope。
6. 在 API 测试工具中，使用正确的 app key 并在请求 token 字段中填入 access token，通常是 `202309` 及更高版本 API 的 `x-tts-access-token` 请求头字段。

常见授权和 scope 错误：
| 症状或错误码 | 可能原因 | 检查内容 |
| --- | --- | --- |
| `105005 Access denied` | 应用或 access token 不包含所需的 API scope。 | 检查 **App & Service > Manage > Manage API**，然后比较 token 的 `granted_scopes` 与 endpoint 所需的 scope。 |
| `105002 Expired credentials` | Access token 已过期。 | 刷新 token 或重新授权。 |
| `36009004 Invalid credentials`，附带 `access_token` 或 `x-tts-access-token` 消息 | Token 无效、复制错误或属于错误的授权主体。 | 生成新 token 并粘贴到正确的 token/请求头字段中。 |
| 测试店铺 API 时店铺为空或缺失 | 应用尚未获得目标商家或测试店铺的授权。 | 使用工具的授权功能或按照授权指南为应用授权。 |
更多故障排除信息，请参阅常见错误和访问权限范围。
# 什么是 API 测试工具？
API 测试工具使开发者能够直接在 Partner Center 中测试 TikTok Shop Open API。
你可以使用它来：

* 选择工具支持的 API 和版本；
* 填写 query、header、path 和 body 参数；
* 发送请求并检查响应；
* 验证你的 app key、scope、授权、token 和请求参数是否正确；
* 在使用自己的 app key 时，复制生成的示例代码，例如 `curl` 请求。

API 测试工具适用于手动验证和调试。对于生产集成，请继续在你自己的后端实现签名、token 刷新、重试、日志记录和错误处理。
# 入口
使用统一的命名规范：
**Partner Center Console > Development Kits > API Testing Tool**
你也可以直接打开入口：
[API 测试工具](https://partner.tiktokshop.com/dev/api-testing-tool)
请勿将工具入口与应用配置混淆：
| 任务 | Partner Center 路径 |
| --- | --- |
| 打开 API 测试工具 | **Development Kits > API Testing Tool** |
| 查找你的 app key | **App & Service > Manage > App details** |
| 配置 API scope | **App & Service > Manage > Manage API** |
| 授权测试店铺或商家 | 使用 API 测试工具授权流程，或遵循授权指南。 |
如果旧截图不一致地使用 **Partner Console**、**Partner Center**、**Development** 或 **Development Kits**，请以 **Partner Center Console** 作为产品区域名称，以 **Development Kits > API Testing Tool** 作为工具入口。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/43e04e10d604411197ee5440c10497b3~tplv-k9wyc2ijk0-image.image)
# 选择 app key 模式
| 模式 | 适用场景 | 支持内容 | 限制 |
| --- | --- | --- | --- |
| 平台 app key | 在创建或选择自己的应用之前进行快速探索。 | 平台 key 支持的基本只读 `GET` API 测试。 | 不代表你的应用的 scope、授权或市场访问权限。工具可能不为该模式提供生成的请求示例代码。 |
| 你自己的 app key | 真实的应用调试和集成验证。 | 应用特定的 API scope、商家/测试店铺授权、access token 和生成的示例代码。 | 需要在调用成功之前完成应用设置、scope 配置和授权。 |
# 使用平台 app key
平台 app key 是 API 测试工具中的内置选项，用于基本的 API 探索。它允许开发者在选择自己的 app key 之前尝试支持的只读 API。
仅将其用于快速检查。它不能证明你自己的应用有权访问同一 endpoint。对于应用特定的测试，请使用你自己的 app key。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2eb30f87ee764689a1d6f4dddabe875f~tplv-k9wyc2ijk0-image.image)
# 使用你自己的 app key
当你需要验证实际应用配置、商家/测试店铺授权、请求参数和生成的示例代码时，请使用你自己的 app key。
## 设置步骤

1. 登录 [TikTok Shop Partner Center Console](https://partner-sso.tiktok.com/account/login)。
2. 前往 **App & Service > Manage > App details**，复制你的 **App Key**。
3. 前往 **App & Service > Manage > Manage API**，启用或申请所需的 API scope。
4. 为应用授权商家或测试店铺。
5. 打开 **Development Kits > API Testing Tool**。
6. 选择 **Use your own app key**，选择或粘贴你的 app key。
7. 选择你要测试的 API 和 API 版本。
8. 填写所需的 query、path、header 和 body 参数。
9. 在工具显示的 token/请求头字段中填入 access token。对于 `202309` 及更高版本的 API，通常是 `x-tts-access-token` 请求头。
10. 发送请求并检查响应。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/124df2df16f1473ebacf959a88505e8d~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/99352b7e4739481e8f0d955583f64bf4~tplv-k9wyc2ijk0-image.image)
## 授权和 access token 选项
你自己的 app key 必须经过授权后才能测试需要商家、店铺、达人或服务商数据的 API。
你有两个选项：
| 选项 | 工作方式 | 使用时机 |
| --- | --- | --- |
| 工具授权流程 | 使用 API 测试工具中提供的授权功能来授权测试店铺或商家，然后继续在工具中测试。 | 基于工具的手动测试的最快路径。 |
| 手动授权流程 | 遵循授权指南，获取 `access_token`，并将其粘贴到 API 测试工具的 token/请求头字段中。 | 当你需要复现真实的 OAuth 流程或调试 token 交换时使用。 |
手动回填 token 时，将 `access_token` 粘贴到 API 测试工具显示的请求 token 字段中。对于 `202309` 及更高版本的 API，这对应 `x-tts-access-token` 请求头。请勿将 refresh token 粘贴到请求 token 字段中。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5fc05b9d5fbb4fe09944fbb4980e8be9~tplv-k9wyc2ijk0-image.image)
# API 测试工具使用技巧
| 技巧 | 使用方式 | 演示 |
| --- | --- | --- |
| 文档引导 | 选择 API 时，使用文档引导从测试工具跳转到 endpoint 参考文档。当出现 API 错误时，使用错误文档引导识别可能的问题和下一步操作。 | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/427ca078185944a6ae2cbed42e7af561~tplv-k9wyc2ijk0-image.image) <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3bf3df94b13e449a9a164015cb817b63~tplv-k9wyc2ijk0-image.image) |
| 示例代码 | 使用你自己的 app key 时，复制生成的请求示例（如 `curl`），在终端中运行以在 Partner Center 之外复现相同请求。这对于比较工具行为与你的后端实现非常有用。 | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b9883c37938b4d119ffd120c85d9352b~tplv-k9wyc2ijk0-image.image) <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5ac394c4c7544b30bed4d4bfedea3d09~tplv-k9wyc2ijk0-image.image) |
# 快速故障排除流程

1. 确认你使用的是正确的 app key。
2. 确认 endpoint 所需的 API scope。
3. 确认该 scope 已在 **App & Service > Manage > Manage API** 中启用或批准。
4. 确认商家或测试店铺已在 scope 启用后对应用进行了授权。
5. 确认 access token 已粘贴到正确的请求 token/请求头字段中。
6. 确认请求方法、路径、API 版本、查询参数、请求体以及 `shop_cipher` 等必需标识符与 endpoint 参考文档一致。
7. 如果同一请求在 API 测试工具中有效但在你的后端中失败，请将生成的示例代码与你的后端签名、请求头、token 和请求体序列化进行比较。
