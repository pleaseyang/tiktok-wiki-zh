# 集成 GoLang SDK

# 概述
按照本指南安装 TikTok Shop Go SDK，将卖家授权码交换为 access token，获取授权店铺的 `shop_cipher`，并使用[搜索商品](https://partner.tiktokshop.com/docv2/page/search-products-202502)发起您的第一次商品 API 调用。
SDK 为您签署 TikTok Shop API 请求。仅当您使用自己的 HTTP 客户端而非 SDK 调用 OpenAPI 端点时，才需要使用[签署您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。
本指南使用：
| 任务 | SDK API 或辅助工具 | OpenAPI 端点 |
| --- | --- | --- |
| 将授权码交换为 access token | `apis.NewAccessToken(appKey, appSecret).GetToken(authCode)` | SDK 中的授权 token 交换辅助工具 |
| 获取授权店铺和 `shop_cipher` | `AuthorizationV202309API.Authorization202309ShopsGet(ctx)` | [GET /authorization/202309/shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| 搜索商品 | `ProductV202502API.Product202502ProductsSearchPost(ctx)` | [POST /product/202502/products/search](https://partner.tiktokshop.com/docv2/page/search-products-202502) |

版本说明：API 组不一定共享相同版本。例如，本指南对获取授权店铺使用 `AuthorizationV202309API`，因为当前端点为 `/authorization/202309/shops`，而搜索商品示例使用 `ProductV202502API`。
# 前提条件
集成 SDK 之前，您需要：

1. 一个 TikTok Shop 应用和测试卖家账号。请参阅[创建测试商家账号](https://partner.tiktokshop.com/docv2/page/create-test-seller-account)。
2. 从为测试应用配置的重定向 URL 获取的卖家授权码。请参阅[生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token)。
3. 从合作伙伴中心下载的最新 Go SDK 包。SDK 包根据您应用已启用的范围和 API 版本生成。请参阅[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。

不要将 `app_key`、`app_secret`、`access_token`、`refresh_token`、授权码或卖家数据提交到源代码管理。请从环境变量或密钥管理器加载密钥。
# 环境要求
使用 Go 1.18 或更高版本。示例使用标准库 `context` 包。不要添加 `golang.org/x/net/context`；对于现代 Go 项目它已过时。
运行时依赖应来自 SDK 包和您的应用代码。不要将 `github.com/stretchr/testify/assert` 添加为运行时依赖；`testify` 是测试辅助工具，如果项目使用它应仅放在测试文件中。
# 项目结构
下载并解压 SDK 后，将 SDK 文件夹放在项目中，并在 `go.mod` 中使用一个一致的文件夹名称。
示例结构：
```Plain Text
my-project/
  go.mod
  main.go
  sdk_golang/
    apis/
    models/
    utils/
    ...
```

示例 `go.mod`：
```Go
module example.com/my-project

go 1.22

require tiktokshop/open/sdk_golang v1.0.0

replace tiktokshop/open/sdk_golang => ./sdk_golang
```

如果您的 SDK 文件夹名称不同，请在两行中使用相同的占位符：
```Go
require tiktokshop/open/<sdk-folder> v1.0.0
replace tiktokshop/open/<sdk-folder> => ./<sdk-folder>
```

更新 `go.mod` 后，运行：
```Shell
go mod tidy
go build ./...
```

# 配置 SDK 客户端
在加载 `app_key` 和 `app_secret` 后创建 API 客户端。不要在此处构建搜索商品请求，因为 `accessToken` 和 `shopCipher` 是在后续步骤中获取的运行时值。
```Go
configuration := apis.NewConfiguration()
configuration.AddAppInfo(appKey, appSecret)

apiClient := apis.NewAPIClient(configuration)
```

# 获取 Access Token
使用 SDK 辅助工具将一次性卖家授权码交换为 access token。
```Go
at := apis.NewAccessToken(appKey, appSecret)

resp, err := at.GetToken(authCode)
if err != nil {
    return fmt.Errorf("GetToken failed: %w", err)
}
if resp.Code != 0 {
    return fmt.Errorf("GetToken business error: code=%d", resp.Code)
}

accessToken := resp.Data.AccessToken
if accessToken == "" {
    return fmt.Errorf("GetToken response has empty access_token")
}
```

在生产环境中，将 access token、refresh token 及其过期时间戳存储在安全的服务端数据存储中。不要在日志中打印 token 或将其存储在前端代码中。
# 获取 Shop Cipher
`shop_cipher` 标识用于搜索商品等店铺级 API 的授权店铺。使用卖家 `accessToken` 调用[获取授权店铺](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)，并使用响应中的 `data.shops[].cipher`。
```Go
shopsRequest := apiClient.AuthorizationV202309API.Authorization202309ShopsGet(ctx)
shopsRequest = shopsRequest.ContentType("application/json")
shopsRequest = shopsRequest.XTtsAccessToken(accessToken)

shopsResponse, httpRes, err := shopsRequest.Execute()
if err != nil {
    return fmt.Errorf("Authorization202309ShopsGet failed: %w", err)
}
if httpRes != nil && httpRes.StatusCode != http.StatusOK {
    return fmt.Errorf("Authorization202309ShopsGet HTTP status: %d", httpRes.StatusCode)
}
if shopsResponse == nil {
    return fmt.Errorf("Authorization202309ShopsGet response is nil")
}
if shopsResponse.GetCode() != 0 {
    return fmt.Errorf(
        "Authorization202309ShopsGet business error: code=%d message=%s",
        shopsResponse.GetCode(),
        shopsResponse.GetMessage(),
    )
}
if len(shopsResponse.Data.Shops) == 0 {
    return fmt.Errorf("no authorized shops found")
}

var shopCipher string
for _, shop := range shopsResponse.Data.Shops {
    var shopID string
    var cipher string
    if shop.Id != nil {
        shopID = *shop.Id
    }
    if shop.Cipher != nil {
        cipher = *shop.Cipher
    }

    fmt.Printf("Authorized shop: shop_id=%s, shop_cipher=%s\n", shopID, cipher)

    if shopCipher == "" && cipher != "" {
        shopCipher = cipher
    }
}

if shopCipher == "" {
    return fmt.Errorf("no shop_cipher found in authorized shops")
}
```

不要硬编码 `shop_cipher`。始终从您要访问的店铺分配它。赋值必须在循环内或从 `shopsResponse.Data.Shops` 选择店铺后立即进行；循环变量在循环结束后不可用。
# 搜索商品
在获得 `accessToken` 和 `shopCipher` 后，调用[搜索商品](https://partner.tiktokshop.com/docv2/page/search-products-202502)。
OpenAPI 端点：
| 项目 | 值 |
| --- | --- |
| 方法和路径 | `POST /product/202502/products/search` |
| 必填 query 参数 | `page_size`，有效范围：1 至 100 |
| 可选 query 参数 | `page_token`、`shop_cipher` |
| 必填 headers | `x-tts-access-token`、`Content-Type: application/json` |
| 可选请求体过滤器 | `audit_status`、`category_version`、`create_time_ge`、`create_time_le`、`listing_platforms`、`listing_quality_tiers`、`return_draft_version`、`seller_skus`、`sku_ids`、`sns_filter`、`status`、`update_time_ge`、`update_time_le` |

本指南使用的 Go SDK 请求构建器：
| 方法 | 含义 |
| --- | --- |
| `ContentType("application/json")` | 设置 `Content-Type` 请求头。 |
| `XTtsAccessToken(accessToken)` | 将卖家 token 作为 `x-tts-access-token` 发送。 |
| `ShopCipher(shopCipher)` | 映射到 query 参数 `shop_cipher`。 |
| `PageSize(1)` | 映射到必填 query 参数 `page_size`。 |
| `Product202502SearchProductsRequestBody(reqBody)` | 设置 JSON 请求体过滤器。 |

```Go
productsRequest := apiClient.ProductV202502API.Product202502ProductsSearchPost(ctx)
productsRequest = productsRequest.ContentType("application/json")
productsRequest = productsRequest.XTtsAccessToken(accessToken)
productsRequest = productsRequest.ShopCipher(shopCipher)
productsRequest = productsRequest.PageSize(1)

reqBody := productV202502.Product202502SearchProductsRequestBody{
    Status: utils.PtrString("ALL"),
}
productsRequest = productsRequest.Product202502SearchProductsRequestBody(reqBody)

searchProductsResponse, httpRes, err := productsRequest.Execute()
if err != nil {
    return fmt.Errorf("Product202502ProductsSearchPost failed: %w", err)
}
if httpRes != nil && httpRes.StatusCode != http.StatusOK {
    return fmt.Errorf("Product202502ProductsSearchPost HTTP status: %d", httpRes.StatusCode)
}
if searchProductsResponse == nil {
    return fmt.Errorf("Product202502ProductsSearchPost response is nil")
}
if searchProductsResponse.GetCode() != 0 {
    return fmt.Errorf(
        "Product202502ProductsSearchPost business error: code=%d message=%s",
        searchProductsResponse.GetCode(),
        searchProductsResponse.GetMessage(),
    )
}

fmt.Printf("Search Products data: %+v\n", searchProductsResponse.GetData())
```

# 完整演示
```Go
package main

import (
    "context"
    "fmt"
    "log"
    "net/http"
    "os"

    "tiktokshop/open/sdk_golang/apis"
    productV202502 "tiktokshop/open/sdk_golang/models/product/v202502"
    "tiktokshop/open/sdk_golang/utils"
)

func requiredEnv(name string) string {
    value := os.Getenv(name)
    if value == "" {
        log.Fatalf("missing required environment variable: %s", name)
    }
    return value
}

func getAccessToken(appKey string, appSecret string, authCode string) (string, error) {
    at := apis.NewAccessToken(appKey, appSecret)

    resp, err := at.GetToken(authCode)
    if err != nil {
        return "", fmt.Errorf("GetToken failed: %w", err)
    }
    if resp.Code != 0 {
        return "", fmt.Errorf("GetToken business error: code=%d", resp.Code)
    }

    accessToken := resp.Data.AccessToken
    if accessToken == "" {
        return "", fmt.Errorf("GetToken response has empty access_token")
    }

    return accessToken, nil
}

func getFirstShopCipher(ctx context.Context, apiClient *apis.APIClient, accessToken string) (string, error) {
    shopsRequest := apiClient.AuthorizationV202309API.Authorization202309ShopsGet(ctx)
    shopsRequest = shopsRequest.ContentType("application/json")
    shopsRequest = shopsRequest.XTtsAccessToken(accessToken)

    shopsResponse, httpRes, err := shopsRequest.Execute()
    if err != nil {
        return "", fmt.Errorf("Authorization202309ShopsGet failed: %w", err)
    }
    if httpRes != nil && httpRes.StatusCode != http.StatusOK {
        return "", fmt.Errorf("Authorization202309ShopsGet HTTP status: %d", httpRes.StatusCode)
    }
    if shopsResponse == nil {
        return "", fmt.Errorf("Authorization202309ShopsGet response is nil")
    }
    if shopsResponse.GetCode() != 0 {
        return "", fmt.Errorf(
            "Authorization202309ShopsGet business error: code=%d message=%s",
            shopsResponse.GetCode(),
            shopsResponse.GetMessage(),
        )
    }
    if len(shopsResponse.Data.Shops) == 0 {
        return "", fmt.Errorf("no authorized shops found")
    }

    var shopCipher string
    for _, shop := range shopsResponse.Data.Shops {
        var shopID string
        var cipher string
        if shop.Id != nil {
            shopID = *shop.Id
        }
        if shop.Cipher != nil {
            cipher = *shop.Cipher
        }

        fmt.Printf("Authorized shop: shop_id=%s, shop_cipher=%s\n", shopID, cipher)

        if shopCipher == "" && cipher != "" {
            shopCipher = cipher
        }
    }

    if shopCipher == "" {
        return "", fmt.Errorf("no shop_cipher found in authorized shops")
    }

    return shopCipher, nil
}

func searchProducts(ctx context.Context, apiClient *apis.APIClient, accessToken string, shopCipher string) error {
    productsRequest := apiClient.ProductV202502API.Product202502ProductsSearchPost(ctx)
    productsRequest = productsRequest.ContentType("application/json")
    productsRequest = productsRequest.XTtsAccessToken(accessToken)
    productsRequest = productsRequest.ShopCipher(shopCipher)
    productsRequest = productsRequest.PageSize(1)

    reqBody := productV202502.Product202502SearchProductsRequestBody{
        Status: utils.PtrString("ALL"),
    }
    productsRequest = productsRequest.Product202502SearchProductsRequestBody(reqBody)

    searchProductsResponse, httpRes, err := productsRequest.Execute()
    if err != nil {
        return fmt.Errorf("Product202502ProductsSearchPost failed: %w", err)
    }
    if httpRes != nil && httpRes.StatusCode != http.StatusOK {
        return fmt.Errorf("Product202502ProductsSearchPost HTTP status: %d", httpRes.StatusCode)
    }
    if searchProductsResponse == nil {
        return fmt.Errorf("Product202502ProductsSearchPost response is nil")
    }
    if searchProductsResponse.GetCode() != 0 {
        return fmt.Errorf(
            "Product202502ProductsSearchPost business error: code=%d message=%s",
            searchProductsResponse.GetCode(),
            searchProductsResponse.GetMessage(),
        )
    }

    fmt.Printf("Search Products data: %+v\n", searchProductsResponse.GetData())
    return nil
}

func main() {
    ctx := context.Background()

    appKey := requiredEnv("TTS_APP_KEY")
    appSecret := requiredEnv("TTS_APP_SECRET")
    authCode := requiredEnv("TTS_AUTH_CODE")

    configuration := apis.NewConfiguration()
    configuration.AddAppInfo(appKey, appSecret)
    apiClient := apis.NewAPIClient(configuration)

    accessToken, err := getAccessToken(appKey, appSecret, authCode)
    if err != nil {
        log.Fatal(err)
    }

    shopCipher, err := getFirstShopCipher(ctx, apiClient, accessToken)
    if err != nil {
        log.Fatal(err)
    }

    if err := searchProducts(ctx, apiClient, accessToken, shopCipher); err != nil {
        log.Fatal(err)
    }
}
```

使用环境变量运行演示：
```Shell
TTS_APP_KEY="your_app_key" \
TTS_APP_SECRET="your_app_secret" \
TTS_AUTH_CODE="your_auth_code" \
go run .
```

# SDK 更新
SDK 包是应用特定的，根据您应用可用的范围和 API 版本生成。在项目中记录 SDK 下载日期或包版本，以便您可以复现生成的方法名称，如 `AuthorizationV202309API` 和 `ProductV202502API`。
在以下情况更新 SDK：
| 触发条件 | 操作 |
| --- | --- |
| 您为应用启用了新的 API 范围 | 从 [SDK 下载页面](https://partner.tiktokshop.com/docv2/page/download-sdk) 下载最新 SDK。 |
| API 添加了新版本或淘汰了旧版本 | 重新生成 SDK 并检查生成的 API 名称和模型包路径。 |
| SDK 模块路径变更 | 更新 `go.mod` 中的 `require` 和 `replace`，使它们指向同一个 SDK 文件夹。 |
| 方法名称与本指南不同 | 使用下载的 Go SDK 中生成的方法名称，并保持端点版本与 OpenAPI 参考一致。 |

有关 SDK 更新行为，请参阅[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。
