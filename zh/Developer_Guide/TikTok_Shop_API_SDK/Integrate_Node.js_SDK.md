# 集成 Node.js SDK

# 概述
按照本指南安装 TikTok Shop Node.js SDK，获取卖家 access token，获取授权店铺的 `shop_cipher`，并使用[搜索商品](https://partner.tiktokshop.com/docv2/page/search-products-202502)发起您的第一次商品 API 调用。
SDK 为您签署 TikTok Shop API 请求。仅当您使用自己的 HTTP 客户端而非 SDK 调用 OpenAPI 端点时，才需要使用[签署您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。
本指南使用：
| 任务 | SDK API 或辅助工具 | OpenAPI 端点 |
| --- | --- | --- |
| 将授权码交换为 access token | `AccessTokenTool.getAccessToken(authCode)` | SDK 中的授权 token 交换辅助工具 |
| 获取授权店铺和 `shop_cipher` | `AuthorizationV202309Api.ShopsGet` | [GET /authorization/202309/shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| 搜索商品 | `ProductV202502Api.ProductsSearchPost` | [POST /product/202502/products/search](https://partner.tiktokshop.com/docv2/page/search-products-202502) |
版本说明：API 组不一定共享相同版本。例如，本指南对获取授权店铺使用 `AuthorizationV202309Api`，因为当前端点为 `/authorization/202309/shops`，而搜索商品示例使用 `ProductV202502Api`。
# 前提条件
集成 SDK 之前，您需要：

1. 一个 TikTok Shop 应用和测试卖家账号。请参阅[创建测试商家账号](https://partner.tiktokshop.com/docv2/page/create-test-seller-account)。
2. 从为测试应用配置的重定向 URL 获取的卖家授权码。请参阅[生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token)。
3. 从合作伙伴中心下载的最新 Node.js SDK 包。SDK 包根据您应用已启用的范围和 API 版本生成。请参阅[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。

不要将 `app_key`、`app_secret`、`access_token`、`refresh_token`、授权码或卖家数据提交到源代码管理。请从环境变量或密钥管理器加载密钥。
# 环境要求
使用受支持的 Node.js LTS 版本。截至 2026 年 7 月，Node.js 22.x 和 24.x 是受支持的 LTS 系列；Node.js 16.x 已停止维护。在发布本指南的新版本之前，请查看 [Node.js 发布计划](https://github.com/nodejs/release#release-schedule)。
建议基线：
| 组件 | 建议 |
| --- | --- |
| Node.js | 22.x LTS 或 24.x LTS |
| TypeScript | 项目使用的当前受支持的 TypeScript 主要版本 |
| HTTP 客户端 | 使用 SDK 生成的客户端。对于自定义 HTTP 调用，使用 Node 内置的 `fetch` 或其他维护中的客户端。不要在新项目中添加 `request`。 |
# 项目结构
下载并解压 SDK 后，将其放在项目中，并从代码文件到 SDK 入口点的相对路径导入。
示例结构：
```Plain Text
my-project/
  package.json
  tsconfig.json
  src/
    index.ts
  tiktok-shop-node-sdk/
    index.ts
    api/
    model/
    ...
```

如果您的演示文件是 `src/index.ts`，使用以下方式从 SDK 文件夹导入：
```TypeScript
import {
  AccessTokenTool,
  ClientConfiguration,
  TikTokShopNodeApiClient,
} from "../tiktok-shop-node-sdk";
```

如果将演示文件直接放在 SDK 根目录内，`from "."` 可以工作，因为它指向该文件夹的 `index.ts`。在应用项目中，建议从显式的 SDK 文件夹路径导入。
# 安装
安装下载的 SDK 包中列出的依赖。如果生成的 SDK 包含自己的 `package.json`，以该文件为准。
对于围绕 SDK 的新 TypeScript 项目，从类似以下的维护基线开始：
```JSON
{
  "type": "module",
  "scripts": {
    "start": "tsx src/index.ts"
  },
  "dependencies": {
    "tslib": "^2.8.1"
  },
  "devDependencies": {
    "@types/node": "^24",
    "tsx": "^4",
    "typescript": "^6"
  }
}
```

不要在新集成中添加 `request` 或 `@types/request`。[request](https://www.npmjs.com/package/request) 包已弃用，不应用于新的自定义 HTTP 代码。如果您下载的 SDK 仍依赖 `request`，请从合作伙伴中心下载最新 SDK 并检查生成的客户端是否已更新；否则仅将该依赖保留为该特定 SDK 包的兼容性要求。
在 `tsconfig.json` 中添加以下内容：
```JSON
{
  "compilerOptions": {
    "esModuleInterop": true,
    "moduleResolution": "node",
    "target": "ES2022",
    "module": "ESNext",
    "strict": true
  }
}
```

安装依赖：
```Shell
npm install
```

如果您的项目标准化使用 Yarn 或 pnpm，也可以使用 `yarn install` 或 `pnpm install`。
# 配置
从环境变量配置 SDK：
```TypeScript
const requiredEnv = (name: string): string => {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
};

ClientConfiguration.globalConfig.app_key = requiredEnv("TTS_APP_KEY");
ClientConfiguration.globalConfig.app_secret = requiredEnv("TTS_APP_SECRET");

const client = new TikTokShopNodeApiClient({
  config: {
    sandbox: process.env.TTS_SANDBOX === "true",
  },
});
```

`sandbox: false` 将请求发送到生产环境。仅在测试 SDK 包支持的沙箱或开发店铺环境时使用 `sandbox: true`。
# 获取 Access Token
使用 SDK 辅助工具将一次性卖家授权码交换为 access token。
```TypeScript
const authCode = requiredEnv("TTS_AUTH_CODE");

const { body: tokenBody } = await AccessTokenTool.getAccessToken(authCode);
console.log("getAccessToken response:", JSON.stringify(tokenBody, null, 2));

const accessToken = tokenBody.data?.access_token;
if (!accessToken) {
  throw new Error("Failed to get access token");
}
```

在生产环境中，将 access token、refresh token 及其过期时间戳存储在安全的服务端数据存储中。不要将 token 存储在前端代码中。
# 获取 Shop Cipher
`shop_cipher` 标识用于搜索商品等店铺级 API 的授权店铺。使用卖家 `accessToken` 调用[获取授权店铺](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)，并使用响应中的 `data.shops[].cipher`。
```TypeScript
const contentType = "application/json";

const { body: shopsGetBody } =
  await client.api.AuthorizationV202309Api.ShopsGet(accessToken, contentType);

console.log("ShopsGet response:", JSON.stringify(shopsGetBody, null, 2));

const shopList = shopsGetBody.data?.shops ?? [];
if (shopList.length === 0) {
  throw new Error("No authorized shops found.");
}

const selectedShop = shopList[0];
const shopId = selectedShop.id;
const shopCipher = selectedShop.cipher;

if (!shopCipher) {
  throw new Error(`No shop_cipher found for shop_id: ${shopId}`);
}

console.log(`Using shop_id: ${shopId}, shop_cipher: ${shopCipher}`);
```

不要硬编码 `shop_cipher`。始终使用您要访问其商品的店铺的 cipher。
# 搜索商品
在获得 `accessToken` 和 `shopCipher` 后，调用[搜索商品](https://partner.tiktokshop.com/docv2/page/search-products-202502)。
OpenAPI 端点：
| 项目 | 值 |
| --- | --- |
| 方法和路径 | `POST /product/202502/products/search` |
| 必填 query 参数 | `page_size`，有效范围：1 至 100 |
| 可选 query 参数 | `page_token`、`shop_cipher` |
| 必填 headers | `x-tts-access-token`、`Content-Type: application/json` |
| 可选请求体过滤器 | `status`、`seller_skus`、`sku_ids`、`category_version`、`create_time_ge`、`create_time_le`、`update_time_ge`、`update_time_le` 以及端点参考中显示的其他字段 |

本指南使用的 Node.js SDK 方法调用：
| 位置 | 参数 | 含义 |
| --- | --- | --- |
| 1 | `pageSize` | 映射到 query 参数 `page_size`。 |
| 2 | `accessToken` | 作为 `x-tts-access-token` 发送。 |
| 3 | `contentType` | 通常为 `application/json`。 |
| 4 | `pageToken` | 可选分页 token。第一页使用 `undefined`。 |
| 5 | `searchProductsRequestBody` | 可选的 JSON 请求体过滤器。不需要过滤器时使用 `{}` 或 `undefined`。 |
| 6 | `shopCipher` | 映射到 query 参数 `shop_cipher`。 |

不同 SDK 语言可能生成不同的位置参数顺序。不要将 Java 或 Go 的方法参数顺序复制到 Node.js 代码中。更新 SDK 时，请检查下载的 SDK 中生成的 Node.js 方法签名。
```TypeScript
const pageSize = 10;
const pageToken = undefined;
const searchProductsRequestBody = {};

const result = await client.api.ProductV202502Api.ProductsSearchPost(
  pageSize,
  accessToken,
  contentType,
  pageToken,
  searchProductsRequestBody,
  shopCipher
);

console.log("Search Products response:", JSON.stringify(result.body, null, 2));
```

# 完整演示
```TypeScript
import {
  AccessTokenTool,
  ClientConfiguration,
  TikTokShopNodeApiClient,
} from "../tiktok-shop-node-sdk";

const requiredEnv = (name: string): string => {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
};

ClientConfiguration.globalConfig.app_key = requiredEnv("TTS_APP_KEY");
ClientConfiguration.globalConfig.app_secret = requiredEnv("TTS_APP_SECRET");

const client = new TikTokShopNodeApiClient({
  config: {
    sandbox: process.env.TTS_SANDBOX === "true",
  },
});

const main = async () => {
  const contentType = "application/json";

  const authCode = requiredEnv("TTS_AUTH_CODE");
  const { body: tokenBody } = await AccessTokenTool.getAccessToken(authCode);
  console.log("getAccessToken response:", JSON.stringify(tokenBody, null, 2));

  const accessToken = tokenBody.data?.access_token;
  if (!accessToken) {
    throw new Error("Failed to get access token");
  }

  const { body: shopsGetBody } =
    await client.api.AuthorizationV202309Api.ShopsGet(accessToken, contentType);
  console.log("ShopsGet response:", JSON.stringify(shopsGetBody, null, 2));

  const shopList = shopsGetBody.data?.shops ?? [];
  if (shopList.length === 0) {
    throw new Error("No authorized shops found.");
  }

  const selectedShop = shopList[0];
  const shopId = selectedShop.id;
  const shopCipher = selectedShop.cipher;
  if (!shopCipher) {
    throw new Error(`No shop_cipher found for shop_id: ${shopId}`);
  }

  console.log(`Using shop_id: ${shopId}, shop_cipher: ${shopCipher}`);

  const pageSize = 10;
  const pageToken = undefined;
  const searchProductsRequestBody = {};

  const result = await client.api.ProductV202502Api.ProductsSearchPost(
    pageSize,
    accessToken,
    contentType,
    pageToken,
    searchProductsRequestBody,
    shopCipher
  );

  console.log("Search Products response:", JSON.stringify(result.body, null, 2));
};

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

使用环境变量运行演示：
```Shell
TTS_APP_KEY="your_app_key" \
TTS_APP_SECRET="your_app_secret" \
TTS_AUTH_CODE="your_auth_code" \
TTS_SANDBOX="true" \
npm run start
```

生产环境请使用 `TTS_SANDBOX="false"` 或省略 `TTS_SANDBOX`。
# SDK 更新
SDK 包是应用特定的，根据您应用可用的范围和 API 版本生成。在项目中记录 SDK 下载日期或包版本，以便您可以复现生成的方法签名。
在以下情况更新 SDK：
| 触发条件 | 操作 |
| --- | --- |
| 您为应用启用了新的 API 范围 | 从 [SDK 下载页面](https://partner.tiktokshop.com/docv2/page/download-sdk) 下载最新 SDK。 |
| API 添加了新版本或淘汰了旧版本 | 重新生成 SDK 并检查生成的 API 类名，如 `ProductV202502Api`。 |
| SDK 框架变更 | 从 SDK 包重新安装依赖并重新运行构建。 |
| 重新生成后方法参数顺序变更 | 根据生成的 Node.js 方法签名更新代码，而不是从 Java 或 Go 复制示例。 |

有关 SDK 更新行为，请参阅[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。
