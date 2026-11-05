# Integrate GoLang SDK

# Overview
Follow this guide to install the TikTok Shop Go SDK, exchange a seller authorization code for an access token, get the authorized shop's `shop_cipher`, and make your first product API call with [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502).
The SDK signs TikTok Shop API requests for you. Use [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) only when you call OpenAPI endpoints with your own HTTP client instead of the SDK.
This guide uses:
| Task | SDK API or helper | OpenAPI endpoint |
| --- | --- | --- |
| Exchange an authorization code for an access token | `apis.NewAccessToken(appKey, appSecret).GetToken(authCode)` | Authorization token exchange helper in the SDK |
| Get authorized shops and `shop_cipher` | `AuthorizationV202309API.Authorization202309ShopsGet(ctx)` | [GET /authorization/202309/shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) |
| Search products | `ProductV202502API.Product202502ProductsSearchPost(ctx)` | [POST /product/202502/products/search](https://partner.tiktokshop.com/docv2/page/search-products-202502) |

Version note: API groups do not always share the same version. For example, this guide uses `AuthorizationV202309API` for Get Authorized Shops because the current endpoint is `/authorization/202309/shops`, while the Search Products example uses `ProductV202502API`.
# Prerequisites
Before integrating the SDK, you need:

1. A TikTok Shop app and a test seller account. See [Create a test seller account](https://partner.tiktokshop.com/docv2/page/create-test-seller-account).
2. A seller authorization code from the redirect URL configured for your test app. See [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token).
3. The latest Go SDK package downloaded from Partner Center. SDK packages are generated for your app's enabled scopes and API versions. See [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk).

Do not commit `app_key`, `app_secret`, `access_token`, `refresh_token`, authorization codes, or seller data to source control. Load secrets from environment variables or your secret manager.
# Environment
Use Go 1.18 or later. The examples use the standard library `context` package. Do not add `golang.org/x/net/context`; it is obsolete for modern Go projects.
Runtime dependencies should come from the SDK package and your application code. Do not add `github.com/stretchr/testify/assert` as a runtime dependency; `testify` is a test helper and belongs in test-only files if your project uses it.
# Project Layout
After downloading and unzipping the SDK, place the SDK folder in your project and use one consistent folder name in `go.mod`.
Example layout:
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

Example `go.mod`:
```Go
module example.com/my-project

go 1.22

require tiktokshop/open/sdk_golang v1.0.0

replace tiktokshop/open/sdk_golang => ./sdk_golang
```

If your SDK folder has a different name, use the same placeholder in both lines:
```Go
require tiktokshop/open/<sdk-folder> v1.0.0
replace tiktokshop/open/<sdk-folder> => ./<sdk-folder>
```

After updating `go.mod`, run:
```Shell
go mod tidy
go build ./...
```

# Configure the SDK Client
Create the API client after loading `app_key` and `app_secret`. Do not build a Search Products request here, because `accessToken` and `shopCipher` are runtime values obtained in later steps.
```Go
configuration := apis.NewConfiguration()
configuration.AddAppInfo(appKey, appSecret)

apiClient := apis.NewAPIClient(configuration)
```

# Get Access Token
Use the SDK helper to exchange the one-time seller authorization code for an access token.
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

In production, store the access token, refresh token, and their expiration timestamps in a secure server-side data store. Do not print tokens in logs or store them in frontend code.
# Get Shop Cipher
`shop_cipher` identifies the authorized shop for shop-level APIs such as Search Products. Call [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) with the seller `accessToken` and use `data.shops[].cipher` from the response.
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

Do not hard-code `shop_cipher`. Always assign it from the shop you want to access. The assignment must happen inside the loop or immediately after selecting a shop from `shopsResponse.Data.Shops`; the loop variable is not available after the loop ends.
# Search Products
Call [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) after you have both `accessToken` and `shopCipher`.
OpenAPI endpoint:
| Item | Value |
| --- | --- |
| Method and path | `POST /product/202502/products/search` |
| Required query parameter | `page_size`, valid range: 1 to 100 |
| Optional query parameters | `page_token`, `shop_cipher` |
| Required headers | `x-tts-access-token`, `Content-Type: application/json` |
| Optional request body filters | `audit_status`, `category_version`, `create_time_ge`, `create_time_le`, `listing_platforms`, `listing_quality_tiers`, `return_draft_version`, `seller_skus`, `sku_ids`, `sns_filter`, `status`, `update_time_ge`, `update_time_le` |

Go SDK request builder used in this guide:
| Method | Meaning |
| --- | --- |
| `ContentType("application/json")` | Sets the `Content-Type` header. |
| `XTtsAccessToken(accessToken)` | Sends the seller token as `x-tts-access-token`. |
| `ShopCipher(shopCipher)` | Maps to query parameter `shop_cipher`. |
| `PageSize(1)` | Maps to required query parameter `page_size`. |
| `Product202502SearchProductsRequestBody(reqBody)` | Sets the JSON request body filters. |

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

# Complete Demo
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

Run the demo with environment variables:
```Shell
TTS_APP_KEY="your_app_key" \
TTS_APP_SECRET="your_app_secret" \
TTS_AUTH_CODE="your_auth_code" \
go run .
```

# SDK Updates
SDK packages are app-specific and generated from the scopes and API versions available to your app. Record the SDK download date or package version in your project so you can reproduce generated method names such as `AuthorizationV202309API` and `ProductV202502API`.
Update the SDK when:
| Trigger | Action |
| --- | --- |
| You enable new API scopes for the app | Download the latest SDK from the [SDK download page](https://partner.tiktokshop.com/docv2/page/download-sdk). |
| An API adds a new version or sunsets an old version | Regenerate the SDK and check generated API names and model package paths. |
| The SDK module path changes | Update both `require` and `replace` in `go.mod` so they refer to the same SDK folder. |
| Method names differ from this guide | Use the method names generated in your downloaded Go SDK and keep the endpoint versions aligned with the OpenAPI reference. |

For SDK update behavior, see [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk).
