# Widget SDK user guide

# SDK version and changelog
This guide covers the TikTok Shop Widget SDK packages:
| Package | Use case | Latest npm version | Latest npm publish time |
| --- | --- | --- | --- |
| [@tiktokshop/widget-kit](https://www.npmjs.com/package/@tiktokshop/widget-kit) | Native JavaScript integration | `1.0.4` | 2026-04-27 07:38:24 UTC |
| [@tiktokshop/widget-kit-react](https://www.npmjs.com/package/@tiktokshop/widget-kit-react) | React component integration | `1.0.4` | 2026-04-27 08:54:08 UTC |
The latest versions above were checked against the npm registry on 2026-07-06. New integrations should install the `latest` dist-tag unless your TikTok Shop integration contact asks you to pin a specific version.
```Bash
npm install @tiktokshop/widget-kit-react@latest
npm install @tiktokshop/widget-kit@latest
```

| Version | Package | Publish date | Notes |
| --- | --- | --- | --- |
| `1.0.4` | `@tiktokshop/widget-kit` | 2026-04-27 | Latest npm release. Use for new native JavaScript integrations. Detailed release notes were not included in the source document. |
| `1.0.4` | `@tiktokshop/widget-kit-react` | 2026-04-27 | Latest npm release. Use for new React integrations. Detailed release notes were not included in the source document. |
| `1.0.3` | both packages | 2024-04-08 | Published on npm. Detailed release notes were not included in the source document. |
| `1.0.2` | `@tiktokshop/widget-kit` | 2024-02-19 | Fixed issues. |
| `1.0.2` | `@tiktokshop/widget-kit-react` | 2024-02-19 | Added `WidgetConfigProvider` and `RemoteWidget` for React component integration. |
| `1.0.0` | `@tiktokshop/widget-kit` | 2023-12-22 | Initial native JavaScript SDK with `init`, `loadWidget`, `update`, and `preloadWidget`. |
| `1.0.0` | `@tiktokshop/widget-kit-react` | 2023-12-22 | Initial React SDK version. |
# Choose an integration method
Use the React package if your app is built with React. It wraps SDK initialization, config updates, preloading, and rendering in components.
Use the native JavaScript package if your app is not built with React or if you need to mount the widget manually into a DOM node.
| Scenario | Recommended package | Main APIs |
| --- | --- | --- |
| React app | `@tiktokshop/widget-kit-react` | `WidgetConfigProvider`, `RemoteWidget` |
| Non-React app | `@tiktokshop/widget-kit` | `init`, `preloadWidget`, `loadWidget`, `update` |
# Preconditions
Before integrating the Widget SDK:

1. Build a backend endpoint in your system that returns a short-lived widget token to your frontend. Your backend should call [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token), which maps to the OpenAPI path `GET /authorization/202401/widget_token`.
2. Configure your widget domain allowlist with TikTok Shop Open Platform. Widget pages have cross-origin restrictions, so the browser domain that hosts your frontend must be allowlisted.
3. Confirm the widget names enabled for your app. The SDK does not discover widget names automatically. The widget name list is provided in your widget integration documentation or by TikTok Shop Open Platform during widget enablement.
4. Keep TikTok Shop OpenAPI credentials and seller access tokens on your backend. Do not expose app secrets, seller access tokens, or signing logic in the browser.

# Configuration fields
Use explicit values from Partner Center, your seller authorization data, and your widget enablement materials. Do not leave placeholder strings such as `xxx` in production code.
| Field | Required | Example | Where to get it |
| --- | --- | --- | --- |
| `config.shopId` | Yes | `7493990753256900486` | The authorized TikTok Shop seller/shop ID in your app backend. It must match the seller access token used to request the widget token. |
| `config.oecRegion` | Yes | `US` | The seller market or region code from the authorized shop context, such as `US`, `GB`, or `ID`. |
| `config.appKey` | Yes | `6amm4vuh5fo1g` | Partner Center app details. This is the app key/client key for your TikTok Shop app. |
| `config.isvInfo.name` | Yes | `OPEN_PLATFORM` | Your ISV or developer display name in Partner Center or the integration profile shared with TikTok Shop. |
| `getToken` | Yes for initialization | `getWidgetToken` | A frontend callback that calls your backend token endpoint and returns `{ token, expire_at }`. |
| `remotes[].name` | Yes | `@tiktokshop-widget/product:optimizer` | The widget name provided by TikTok Shop Open Platform for the widget scenario enabled for your app. |
| `preloadWidgetNames` | No | `["@tiktokshop-widget/product:optimizer"]` | Widget names that should be preloaded before rendering. Use only names included in `remotes`. |
# Token flow
The frontend must not call TikTok Shop OpenAPI directly. Use this flow:

1. The frontend calls your backend endpoint, for example `GET /api/widget-token?shopId=7493990753256900486`.
2. Your backend verifies the seller session and retrieves the seller's TikTok Shop `access_token`.
3. Your backend calls TikTok Shop OpenAPI `GET /authorization/202401/widget_token` with the required `x-tts-access-token` header.
4. TikTok Shop returns `data.widget_token.token` and `data.widget_token.expire_at`.
5. Your backend returns `{ "token": "...", "expire_at": 1703100448 }` to the frontend.
6. The SDK calls `getToken` whenever it needs a valid widget token.

The internal request path `/api/v1/seller/widget/get` may appear in browser errors or screenshots because the hosted widget page calls an internal widget service. Developers should not call that internal interface directly. Implement your own `getToken` callback and backend endpoint, and have the backend call the public [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) OpenAPI.
# Backend token endpoint example
The following example shows the shape of a backend endpoint. Replace `getSellerAccessToken` and `callTikTokShopOpenAPI` with your existing OpenAPI signing and token handling logic.
```TypeScript
import express from "express";

const app = express();

async function getSellerAccessToken(shopId: string): Promise<string> {
  // Read the seller access token from your authorization storage.
  // Do not expose this token to the browser.
  return "";
}

async function callTikTokShopOpenAPI(path: string, accessToken: string) {
  // Use the same OpenAPI base URL, signing, timestamp, and app credentials
  // that your backend uses for other TikTok Shop OpenAPI calls.
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

# React quick start
Use `WidgetConfigProvider` once near the top of your React app. Use `RemoteWidget` where the widget should render.
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

# Native JavaScript quick start
Call `init` once before calling `preloadWidget`, `loadWidget`, or `update`.
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

# Preload widget
Preloading is optional. Use it when the widget is not displayed on the first screen and you want to load resources earlier.
For React, pass `preloadWidgetNames` to `WidgetConfigProvider`.
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

For native JavaScript, call `preloadWidget` after `init`.
```TypeScript
import { preloadWidget } from "@tiktokshop/widget-kit";

await preloadWidget(["@tiktokshop-widget/product:optimizer"]);
```

# Load widget
For React, use `RemoteWidget`.
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

For native JavaScript, call `loadWidget` after `init`.
```TypeScript
import { loadWidget, type WidgetComponent } from "@tiktokshop/widget-kit";

const component: WidgetComponent = await loadWidget("@tiktokshop-widget/product:optimizer");
const view = component.create(document.getElementById("widget-preview-container")!);
await view.render({});
```

# Update widget config
Use `update` when the current seller or shop context changes after initialization.
For React, update the props passed to `WidgetConfigProvider`.
For native JavaScript, call `update`. `getToken` is required during initialization. In `update`, pass `getToken` only if the token callback has changed.
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

# Reference API - init
`init` exists in `@tiktokshop/widget-kit`. Call it once before loading or preloading widgets.
| Property | Type | Required | Sample | Description |
| --- | --- | --- | --- | --- |
| `config` | `WidgetConfig` | Yes |  | Basic widget configuration. |
| `config.shopId` | `string` | Yes | `"7493990753256900486"` | Seller or shop ID used for routing and event tracking. |
| `config.oecRegion` | `string` | Yes | `"US"` | Seller region or market code. |
| `config.appKey` | `string` | Yes | `"6amm4vuh5fo1g"` | App key/client key from Partner Center. |
| `config.isvInfo` | `object` | Yes |  | ISV information. |
| `config.isvInfo.name` | `string` | Yes | `"OPEN_PLATFORM"` | ISV or developer display name. |
| `getToken` | `() => Promise<WidgetToken>` | Yes | `getWidgetToken` | Callback that returns a short-lived widget token. |
| `remotes` | `Array<{ name: string }>` | Yes | `[{ name: "@tiktokshop-widget/product:optimizer" }]` | Widget names enabled for your app. |
# Reference API - WidgetToken
`getToken` must resolve to the token object expected by the SDK.
| Property | Type | Required | Sample | Description |
| --- | --- | --- | --- | --- |
| `token` | `string` | Yes | `"eyJhbGciOiJIUzUxMi..."` | Token used by the widget page. |
| `expire_at` | `number` | Yes | `1703100448` | Expiration timestamp. The OpenAPI response describes widget tokens as short-lived, usually about 5 minutes. |
# Reference API - loadWidget
`loadWidget` loads one widget by name.
| Package | Input | Return value | Notes |
| --- | --- | --- | --- |
| `@tiktokshop/widget-kit-react` | `name: string` | React component | Prefer `RemoteWidget` for React integrations. |
| `@tiktokshop/widget-kit` | `name: string` | `Promise<WidgetComponent>` | Use `create`, then `render`, `update`, or `unmount` on the returned view. |
```TypeScript
const component = await loadWidget("@tiktokshop-widget/product:optimizer");
const view = component.create(document.getElementById("widget-preview-container")!);
await view.render({});
```

# Reference API - update
`update` exists in `@tiktokshop/widget-kit`. Use it to update widget configuration after initialization.
| Property | Type | Required | Sample | Description |
| --- | --- | --- | --- | --- |
| `config` | `WidgetConfig` | No |  | New widget config. Required if you are changing shop, region, app key, or ISV info. |
| `getToken` | `() => Promise<WidgetToken>` | No | `getWidgetToken` | Optional for `update` if the callback has not changed. Required during initial setup. |
# Reference API - preloadWidget
`preloadWidget` exists in `@tiktokshop/widget-kit`.
| Property | Type | Required | Sample | Description |
| --- | --- | --- | --- | --- |
| `names` | `string[]` | Yes | `["@tiktokshop-widget/product:optimizer"]` | Widget names to preload. |
# Reference API - WidgetConfigProvider
`WidgetConfigProvider` exists in `@tiktokshop/widget-kit-react`. Place it above the React components that render remote widgets.
| Property | Type | Required | Sample | Description |
| --- | --- | --- | --- | --- |
| `config` | `WidgetConfig` | Yes |  | Basic widget configuration. |
| `getToken` | `() => Promise<WidgetToken>` | Yes | `getWidgetToken` | Callback that returns a short-lived widget token. |
| `remotes` | `Array<{ name: string }>` | Yes | `[{ name: "@tiktokshop-widget/product:optimizer" }]` | Widget names enabled for your app. |
| `preloadWidgetNames` | `string[]` | No | `["@tiktokshop-widget/product:optimizer"]` | Widget names to preload. |
# Reference API - RemoteWidget
`RemoteWidget` exists in `@tiktokshop/widget-kit-react`. Use it to render one enabled widget.
| Property | Type | Required | Sample | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | Yes | `"@tiktokshop-widget/product:optimizer"` | Widget name enabled for your app. |
| `className` | `string` | No | `"widget-preview-container"` | CSS class name for the widget container. |
| `style` | `CSSProperties` | No | `{ width: 100 }` | Inline style for the widget container. |
| `options` | `Record<string, any>` | No | `{}` | Props/configuration passed to the remote widget. |
# Reference API - WidgetComponent and WidgetView
These interfaces apply to native JavaScript integration.
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

# Error message list
| Error message | Description | How to fix |
| --- | --- | --- |
| `Please call init first` | `preloadWidget`, `loadWidget`, or `update` was called before SDK initialization. | Call `init` first for native JavaScript, or render widgets inside `WidgetConfigProvider` for React. |
| `Current name configuration not found` | The widget name is not configured in `remotes`, or the name does not match a widget enabled for your app. | Check the widget name provided in your integration documentation, and make sure it is included in `remotes`. |
# FAQ
# FAQ - The widget page fails to load and token requests repeat
Symptom: the browser repeatedly requests a widget token and the widget page never finishes loading.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9150f60428264983bc2309ad7c27af76~tplv-k9wyc2ijk0-image.image)
Most common causes:

* `getToken` does not return `{ token, expire_at }`.
* The backend returned the full OpenAPI response instead of `data.widget_token`.
* The token is expired.
* `shopId`, `oecRegion`, `appKey`, or the seller access token do not match.
* The frontend domain is not allowlisted for the widget.

The frontend `getToken` callback should return only the widget token object:
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

# FAQ - Why do I see `/api/v1/seller/widget/get` in errors?
`/api/v1/seller/widget/get` is an internal widget service request made by the hosted widget page. It is not the public API that developers should call.
Developers should call the public OpenAPI from the backend:
| Purpose | API |
| --- | --- |
| Public API for developers to generate a widget token | `GET /authorization/202401/widget_token` |
| Internal widget page request that may appear in browser errors | `/api/v1/seller/widget/get` |
If the internal request fails, debug your public-token flow first: `getToken` output shape, token expiration, app key, shop ID, region, seller access token, and domain allowlist.
Common internal widget error codes:
| Error code | Error message | Reason |
| --- | --- | --- |
| `36017010` | `Widget domain not match` | The allowlisted domain does not match the actual frontend domain. |
| `36017005` | `Widget Token Is Expired` | The widget token has expired. |
| `36017006` | `Widget token is invalid` | The widget token is missing, malformed, or not accepted by the widget service. |
| `36017008` | `app_key is not match` | The app key does not match the token or widget configuration. |
| `36017009` | `Widget Token Shop Not Match` | The `shopId` in config does not match the shop information in the widget token. |
| `36004003` | `invalid client_key` | The app key allowlist is not configured. Provide the domain and app key to TikTok Shop Open Platform for allowlist configuration. |
| `I01008` | `Traffic is invalid` | The shop region does not match the server room. This is usually caused by mismatched `shopId` and `oecRegion`. |
# FAQ - The widget name is wrong
Symptom: the SDK reports `Current name configuration not found` or the widget page cannot be found.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8a5f75bbb3c3452e9e10b7fe0a8b9a39~tplv-k9wyc2ijk0-image.image)
Check the widget name in the integration documentation shared for your app, then verify:

* The same widget name appears in `remotes`.
* `RemoteWidget.name`, `preloadWidgetNames`, and `loadWidget(name)` use the same exact string.
* The widget scenario is enabled for your app by TikTok Shop Open Platform.

# Related links
| Link | Use it for |
| --- | --- |
| [@tiktokshop/widget-kit on npm](https://www.npmjs.com/package/@tiktokshop/widget-kit) | Native JavaScript package version and package metadata. |
| [@tiktokshop/widget-kit-react on npm](https://www.npmjs.com/package/@tiktokshop/widget-kit-react) | React package version and package metadata. |
| [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) | Public OpenAPI used by your backend to generate a widget token. |
