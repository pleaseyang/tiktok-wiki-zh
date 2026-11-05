# Widget SDK 用户指南

# SDK 版本与更新日志
本指南涵盖 TikTok Shop Widget SDK 的以下包：
| 包名 | 适用场景 | 最新 npm 版本 | 最新 npm 发布时间 |
| --- | --- | --- | --- |
| [@tiktokshop/widget-kit](https://www.npmjs.com/package/@tiktokshop/widget-kit) | 原生 JavaScript 集成 | `1.0.4` | 2026-04-27 07:38:24 UTC |
| [@tiktokshop/widget-kit-react](https://www.npmjs.com/package/@tiktokshop/widget-kit-react) | React 组件集成 | `1.0.4` | 2026-04-27 08:54:08 UTC |
以上最新版本于 2026-07-06 在 npm 注册表中核实。新集成应安装 `latest` dist-tag，除非您的 TikTok Shop 对接联系人要求您固定特定版本。
```Bash
npm install @tiktokshop/widget-kit-react@latest
npm install @tiktokshop/widget-kit@latest
```

| 版本 | 包名 | 发布日期 | 说明 |
| --- | --- | --- | --- |
| `1.0.4` | `@tiktokshop/widget-kit` | 2026-04-27 | 最新 npm 发布版本。用于新的原生 JavaScript 集成。源文档中未包含详细发布说明。 |
| `1.0.4` | `@tiktokshop/widget-kit-react` | 2026-04-27 | 最新 npm 发布版本。用于新的 React 集成。源文档中未包含详细发布说明。 |
| `1.0.3` | 两个包 | 2024-04-08 | 在 npm 上发布。源文档中未包含详细发布说明。 |
| `1.0.2` | `@tiktokshop/widget-kit` | 2024-02-19 | 修复问题。 |
| `1.0.2` | `@tiktokshop/widget-kit-react` | 2024-02-19 | 新增 `WidgetConfigProvider` 和 `RemoteWidget`，用于 React 组件集成。 |
| `1.0.0` | `@tiktokshop/widget-kit` | 2023-12-22 | 初始原生 JavaScript SDK，包含 `init`、`loadWidget`、`update` 和 `preloadWidget`。 |
| `1.0.0` | `@tiktokshop/widget-kit-react` | 2023-12-22 | 初始 React SDK 版本。 |
# 选择集成方式
如果您的应用使用 React 构建，请使用 React 包。它将 SDK 初始化、配置更新、预加载和渲染封装在组件中。
如果您的应用不使用 React 构建，或者您需要将 widget 手动挂载到 DOM 节点，请使用原生 JavaScript 包。
| 场景 | 推荐包 | 主要 API |
| --- | --- | --- |
| React 应用 | `@tiktokshop/widget-kit-react` | `WidgetConfigProvider`、`RemoteWidget` |
| 非 React 应用 | `@tiktokshop/widget-kit` | `init`、`preloadWidget`、`loadWidget`、`update` |
# 前提条件
在集成 Widget SDK 之前：

1. 在您的系统中构建一个后端 endpoint，用于向前端返回短期有效的 widget token。您的后端应调用 [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token)，对应 OpenAPI 路径 `GET /authorization/202401/widget_token`。
2. 在 TikTok Shop 开放平台配置 widget 域名白名单。Widget 页面存在跨域限制，因此托管前端的浏览器域名必须加入白名单。
3. 确认您的应用已启用的 widget 名称。SDK 不会自动发现 widget 名称。widget 名称列表在您的 widget 集成文档中提供，或在 widget 启用时由 TikTok Shop 开放平台提供。
4. 将 TikTok Shop OpenAPI 凭证和卖家 access token 保留在后端。不要在浏览器中暴露 app secret、卖家 access token 或签名逻辑。

# 配置字段
使用来自 Partner Center、卖家授权数据和 widget 启用材料的明确值。不要在生产代码中保留 `xxx` 等占位符字符串。
| 字段 | 是否必填 | 示例 | 获取方式 |
| --- | --- | --- | --- |
| `config.shopId` | 是 | `7493990753256900486` | 应用后端中已授权的 TikTok Shop 卖家/店铺 ID。必须与用于请求 widget token 的卖家 access token 匹配。 |
| `config.oecRegion` | 是 | `US` | 来自已授权店铺上下文的卖家市场或区域代码，如 `US`、`GB` 或 `ID`。 |
| `config.appKey` | 是 | `6amm4vuh5fo1g` | Partner Center 应用详情。这是您的 TikTok Shop 应用的 app key/client key。 |
| `config.isvInfo.name` | 是 | `OPEN_PLATFORM` | 您在 Partner Center 或 TikTok Shop 共享的集成资料中的 ISV 或开发者展示名称。 |
| `getToken` | 初始化时必填 | `getWidgetToken` | 前端回调函数，调用您的后端 token endpoint 并返回 `{ token, expire_at }`。 |
| `remotes[].name` | 是 | `@tiktokshop-widget/product:optimizer` | TikTok Shop 开放平台为您的应用启用的 widget 场景提供的 widget 名称。 |
| `preloadWidgetNames` | 否 | `["@tiktokshop-widget/product:optimizer"]` | 应在渲染前预加载的 widget 名称。仅使用 `remotes` 中包含的名称。 |
# Token 流程
前端不得直接调用 TikTok Shop OpenAPI。请使用以下流程：

1. 前端调用您的后端 endpoint，例如 `GET /api/widget-token?shopId=7493990753256900486`。
2. 您的后端验证卖家会话并获取卖家的 TikTok Shop `access_token`。
3. 您的后端调用 TikTok Shop OpenAPI `GET /authorization/202401/widget_token`，并携带必需的 `x-tts-access-token` header。
4. TikTok Shop 返回 `data.widget_token.token` 和 `data.widget_token.expire_at`。
5. 您的后端向前端返回 `{ "token": "...", "expire_at": 1703100448 }`。
6. SDK 在需要有效 widget token 时调用 `getToken`。

内部请求路径 `/api/v1/seller/widget/get` 可能出现在浏览器错误或截图中，因为托管的 widget 页面会调用内部 widget 服务。开发者不应直接调用该内部接口。请实现您自己的 `getToken` 回调和后端 endpoint，并由后端调用公开的 [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) OpenAPI。
# 后端 token endpoint 示例
以下示例展示后端 endpoint 的结构。请将 `getSellerAccessToken` 和 `callTikTokShopOpenAPI` 替换为您现有的 OpenAPI 签名和 token 处理逻辑。
```TypeScript
import express from "express";

const app = express();

async function getSellerAccessToken(shopId: string): Promise<string> {
  // 从您的授权存储中读取卖家 access token。
  // 不要将此 token 暴露给浏览器。
  return "";
}

async function callTikTokShopOpenAPI(path: string, accessToken: string) {
  // 使用您的后端用于其他 TikTok Shop OpenAPI 调用的
  // 相同 OpenAPI base URL、签名、时间戳和应用凭证。
  const response = await fetch(`${process.env.TTS_OPEN_API_BASE_URL}${path}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "x-tts-access-token": accessToken,
    },
  });

  return response.json();
}

app.get("/api/widget-token", async (req, res) => {
  const shopId = String(req.query.shopId ?? "");

  if (!shopId) {
    res.status(400).json({ message: "shopId is required" });
    return;
  }

  const accessToken = await getSellerAccessToken(shopId);
  const body = await callTikTokShopOpenAPI(
    `/authorization/202401/widget_token?shop_id=${encodeURIComponent(shopId)}`,
    accessToken,
  );

  const widgetToken = body?.data?.widget_token;
  if (body?.code !== 0 || !widgetToken?.token || !widgetToken?.expire_at) {
    res.status(502).json({
      message: "Failed to get widget token",
      request_id: body?.request_id,
      code: body?.code,
    });
    return;
  }

  res.json({
    token: widgetToken.token,
    expire_at: widgetToken.expire_at,
  });
});
```

# React 快速入门
在 React 应用顶部附近使用一次 `WidgetConfigProvider`。在需要渲染 widget 的位置使用 `RemoteWidget`。
```TypeScript
import { WidgetConfigProvider, RemoteWidget } from "@tiktokshop/widget-kit-react";

const widgetName = "@tiktokshop-widget/product:optimizer";

const widgetConfig = {
  shopId: "7493990753256900486",
  oecRegion: "US",
  appKey: import.meta.env.VITE_TTS_APP_KEY,
  isvInfo: {
    name: "OPEN_PLATFORM",
  },
};

async function getWidgetToken() {
  const response = await fetch(`/api/widget-token?shopId=${widgetConfig.shopId}`);
  if (!response.ok) {
    throw new Error("Failed to request widget token");
  }

  const data = await response.json();
  return {
    token: data.token,
    expire_at: data.expire_at,
  };
}

export function App() {
  return (
    <WidgetConfigProvider
      config={widgetConfig}
      getToken={getWidgetToken}
      remotes={[{ name: widgetName }]}
      preloadWidgetNames={[widgetName]}
    >
      <RemoteWidget
        name={widgetName}
        className="widget-preview-container"
        options={{}}
      />
    </WidgetConfigProvider>
  );
}
```

# 原生 JavaScript 快速入门
在调用 `preloadWidget`、`loadWidget` 或 `update` 之前，先调用一次 `init`。
```TypeScript
import { init, preloadWidget, loadWidget, type WidgetComponent } from "@tiktokshop/widget-kit";

const widgetName = "@tiktokshop-widget/product:optimizer";

const widgetConfig = {
  shopId: "7493990753256900486",
  oecRegion: "US",
  appKey: import.meta.env.VITE_TTS_APP_KEY,
  isvInfo: {
    name: "OPEN_PLATFORM",
  },
};

async function getWidgetToken() {
  const response = await fetch(`/api/widget-token?shopId=${widgetConfig.shopId}`);
  if (!response.ok) {
    throw new Error("Failed to request widget token");
  }

  const data = await response.json();
  return {
    token: data.token,
    expire_at: data.expire_at,
  };
}

init({
  config: widgetConfig,
  getToken: getWidgetToken,
  remotes: [{ name: widgetName }],
});

await preloadWidget([widgetName]);

const component: WidgetComponent = await loadWidget(widgetName);
const view = component.create(document.getElementById("widget-preview-container")!);
await view.render({});
```

```HTML
<div class="widget-preview-container" id="widget-preview-container"></div>
```

# 预加载 Widget
预加载是可选的。当 widget 不在首屏显示，且您希望提前加载资源时使用。
对于 React，将 `preloadWidgetNames` 传递给 `WidgetConfigProvider`。
```TypeScript
<WidgetConfigProvider
  config={widgetConfig}
  getToken={getWidgetToken}
  remotes={[{ name: widgetName }]}
  preloadWidgetNames={[widgetName]}
>
  <RemoteWidget name={widgetName} options={{}} />
</WidgetConfigProvider>
```

对于原生 JavaScript，在 `init` 之后调用 `preloadWidget`。
```TypeScript
import { preloadWidget } from "@tiktokshop/widget-kit";

await preloadWidget(["@tiktokshop-widget/product:optimizer"]);
```

# 加载 Widget
对于 React，使用 `RemoteWidget`。
```TypeScript
import { RemoteWidget } from "@tiktokshop/widget-kit-react";

export function ProductOptimizerWidget() {
  return (
    <RemoteWidget
      name="@tiktokshop-widget/product:optimizer"
      className="widget-preview-container"
      options={{}}
    />
  );
}
```

对于原生 JavaScript，在 `init` 之后调用 `loadWidget`。
```TypeScript
import { loadWidget, type WidgetComponent } from "@tiktokshop/widget-kit";

const component: WidgetComponent = await loadWidget("@tiktokshop-widget/product:optimizer");
const view = component.create(document.getElementById("widget-preview-container")!);
await view.render({});
```

# 更新 Widget 配置
当初始化后当前卖家或店铺上下文发生变化时，使用 `update`。
对于 React，更新传递给 `WidgetConfigProvider` 的 props。
对于原生 JavaScript，调用 `update`。`getToken` 在初始化时是必需的。在 `update` 中，仅当 token 回调发生变化时才传递 `getToken`。
```TypeScript
import { update } from "@tiktokshop/widget-kit";

await update({
  config: {
    shopId: "7493990753256900486",
    oecRegion: "US",
    appKey: import.meta.env.VITE_TTS_APP_KEY,
    isvInfo: {
      name: "OPEN_PLATFORM",
    },
  },
  getToken: getWidgetToken,
});
```

# 参考 API - init
`init` 存在于 `@tiktokshop/widget-kit` 中。在加载或预加载 widget 之前调用一次。
| 属性 | 类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| `config` | `WidgetConfig` | 是 |  | 基础 widget 配置。 |
| `config.shopId` | `string` | 是 | `"7493990753256900486"` | 用于路由和事件追踪的卖家或店铺 ID。 |
| `config.oecRegion` | `string` | 是 | `"US"` | 卖家区域或市场代码。 |
| `config.appKey` | `string` | 是 | `"6amm4vuh5fo1g"` | 来自 Partner Center 的 app key/client key。 |
| `config.isvInfo` | `object` | 是 |  | ISV 信息。 |
| `config.isvInfo.name` | `string` | 是 | `"OPEN_PLATFORM"` | ISV 或开发者展示名称。 |
| `getToken` | `() => Promise<WidgetToken>` | 是 | `getWidgetToken` | 返回短期有效 widget token 的回调函数。 |
| `remotes` | `Array<{ name: string }>` | 是 | `[{ name: "@tiktokshop-widget/product:optimizer" }]` | 为您的应用启用的 widget 名称。 |
# 参考 API - WidgetToken
`getToken` 必须解析为 SDK 所需的 token 对象。
| 属性 | 类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| `token` | `string` | 是 | `"eyJhbGciOiJIUzUxMi..."` | widget 页面使用的 token。 |
| `expire_at` | `number` | 是 | `1703100448` | 过期时间戳。OpenAPI 响应将 widget token 描述为短期有效，通常约 5 分钟。 |
# 参考 API - loadWidget
`loadWidget` 按名称加载一个 widget。
| 包名 | 输入 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `@tiktokshop/widget-kit-react` | `name: string` | React 组件 | React 集成推荐使用 `RemoteWidget`。 |
| `@tiktokshop/widget-kit` | `name: string` | `Promise<WidgetComponent>` | 使用返回的 view 调用 `create`，然后调用 `render`、`update` 或 `unmount`。 |
```TypeScript
const component = await loadWidget("@tiktokshop-widget/product:optimizer");
const view = component.create(document.getElementById("widget-preview-container")!);
await view.render({});
```

# 参考 API - update
`update` 存在于 `@tiktokshop/widget-kit` 中。用于在初始化后更新 widget 配置。
| 属性 | 类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| `config` | `WidgetConfig` | 否 |  | 新的 widget 配置。当您要更改店铺、区域、app key 或 ISV 信息时必填。 |
| `getToken` | `() => Promise<WidgetToken>` | 否 | `getWidgetToken` | 如果回调未变化，`update` 时为可选。初始设置时必填。 |
# 参考 API - preloadWidget
`preloadWidget` 存在于 `@tiktokshop/widget-kit` 中。
| 属性 | 类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| `names` | `string[]` | 是 | `["@tiktokshop-widget/product:optimizer"]` | 要预加载的 widget 名称。 |
# 参考 API - WidgetConfigProvider
`WidgetConfigProvider` 存在于 `@tiktokshop/widget-kit-react` 中。将其放置在渲染远程 widget 的 React 组件之上。
| 属性 | 类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| `config` | `WidgetConfig` | 是 |  | 基础 widget 配置。 |
| `getToken` | `() => Promise<WidgetToken>` | 是 | `getWidgetToken` | 返回短期有效 widget token 的回调函数。 |
| `remotes` | `Array<{ name: string }>` | 是 | `[{ name: "@tiktokshop-widget/product:optimizer" }]` | 为您的应用启用的 widget 名称。 |
| `preloadWidgetNames` | `string[]` | 否 | `["@tiktokshop-widget/product:optimizer"]` | 要预加载的 widget 名称。 |
# 参考 API - RemoteWidget
`RemoteWidget` 存在于 `@tiktokshop/widget-kit-react` 中。用于渲染一个已启用的 widget。
| 属性 | 类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| `name` | `string` | 是 | `"@tiktokshop-widget/product:optimizer"` | 为您的应用启用的 widget 名称。 |
| `className` | `string` | 否 | `"widget-preview-container"` | widget 容器的 CSS 类名。 |
| `style` | `CSSProperties` | 否 | `{ width: 100 }` | widget 容器的内联样式。 |
| `options` | `Record<string, any>` | 否 | `{}` | 传递给远程 widget 的 props/配置。 |
# 参考 API - WidgetComponent 和 WidgetView
以下接口适用于原生 JavaScript 集成。
```TypeScript
export interface WidgetComponent {
  create: (el: HTMLElement) => WidgetView;
}

export interface WidgetView {
  render: (props: Record<string, any>) => Promise<void>;
  unmount: () => Promise<void>;
  update: (props: Record<string, any>) => Promise<void>;
}
```

# 错误信息列表
| 错误信息 | 描述 | 修复方法 |
| --- | --- | --- |
| `Please call init first` | 在 SDK 初始化之前调用了 `preloadWidget`、`loadWidget` 或 `update`。 | 原生 JavaScript 请先调用 `init`，React 请在 `WidgetConfigProvider` 内渲染 widget。 |
| `Current name configuration not found` | widget 名称未在 `remotes` 中配置，或名称与您的应用已启用的 widget 不匹配。 | 检查集成文档中提供的 widget 名称，确保其包含在 `remotes` 中。 |
# 常见问题
# 常见问题 - Widget 页面加载失败且 token 请求反复执行
症状：浏览器反复请求 widget token，widget 页面始终无法完成加载。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9150f60428264983bc2309ad7c27af76~tplv-k9wyc2ijk0-image.image)
最常见原因：

* `getToken` 未返回 `{ token, expire_at }`。
* 后端返回了完整的 OpenAPI 响应，而非 `data.widget_token`。
* token 已过期。
* `shopId`、`oecRegion`、`appKey` 或卖家 access token 不匹配。
* 前端域名未加入 widget 白名单。

前端 `getToken` 回调应仅返回 widget token 对象：
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9991f878fabd45a4990736d4694b8c46~tplv-k9wyc2ijk0-image.image)
```TypeScript
async function getWidgetToken() {
  const response = await fetch(`/api/widget-token?shopId=${widgetConfig.shopId}`);
  const data = await response.json();

  return {
    token: data.token,
    expire_at: data.expire_at,
  };
}
```

# 常见问题 - 为什么错误中会出现 `/api/v1/seller/widget/get`？
`/api/v1/seller/widget/get` 是托管 widget 页面发起的内部 widget 服务请求。它不是开发者应调用的公开 API。
开发者应从后端调用公开 OpenAPI：
| 用途 | API |
| --- | --- |
| 开发者用于生成 widget token 的公开 API | `GET /authorization/202401/widget_token` |
| 可能出现在浏览器错误中的内部 widget 页面请求 | `/api/v1/seller/widget/get` |
如果内部请求失败，请首先排查您的公开 token 流程：`getToken` 输出结构、token 过期时间、app key、shop ID、region、卖家 access token 和域名白名单。
常见内部 widget 错误码：
| 错误码 | 错误信息 | 原因 |
| --- | --- | --- |
| `36017010` | `Widget domain not match` | 白名单域名与实际前端域名不匹配。 |
| `36017005` | `Widget Token Is Expired` | widget token 已过期。 |
| `36017006` | `Widget token is invalid` | widget token 缺失、格式错误或未被 widget 服务接受。 |
| `36017008` | `app_key is not match` | app key 与 token 或 widget 配置不匹配。 |
| `36017009` | `Widget Token Shop Not Match` | 配置中的 `shopId` 与 widget token 中的店铺信息不匹配。 |
| `36004003` | `invalid client_key` | app key 白名单未配置。请向 TikTok Shop 开放平台提供域名和 app key 以配置白名单。 |
| `I01008` | `Traffic is invalid` | 店铺区域与机房不匹配。通常由 `shopId` 和 `oecRegion` 不匹配导致。 |
# 常见问题 - widget 名称错误
症状：SDK 报告 `Current name configuration not found` 或无法找到 widget 页面。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8a5f75bbb3c3452e9e10b7fe0a8b9a39~tplv-k9wyc2ijk0-image.image)
请检查为您的应用共享的集成文档中的 widget 名称，然后验证：

* 相同的 widget 名称出现在 `remotes` 中。
* `RemoteWidget.name`、`preloadWidgetNames` 和 `loadWidget(name)` 使用完全相同的字符串。
* widget 场景已由 TikTok Shop 开放平台为您的应用启用。

# 相关链接
| 链接 | 用途 |
| --- | --- |
| [@tiktokshop/widget-kit on npm](https://www.npmjs.com/package/@tiktokshop/widget-kit) | 原生 JavaScript 包版本和包元数据。 |
| [@tiktokshop/widget-kit-react on npm](https://www.npmjs.com/package/@tiktokshop/widget-kit-react) | React 包版本和包元数据。 |
| [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) | 您的后端用于生成 widget token 的公开 OpenAPI。 |
