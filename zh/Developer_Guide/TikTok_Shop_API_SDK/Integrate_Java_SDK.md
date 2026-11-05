# 集成 Java SDK

# 本指南涵盖内容
本指南介绍如何安装 TikTok Shop Java SDK，并以 [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202309) 为例进行首次 API 调用。
开始之前，请创建测试卖家账户并授权您的应用。有关指南，请参阅[创建测试卖家账户](https://partner.tiktokshop.com/docv2/page/create-test-seller-account)和[生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token)。
# SDK 版本和更新说明
TikTok Shop SDK 包是根据您的应用、语言和有效 API 权限范围集生成的。不要假设占位符版本 `1.0.0` 始终是最新版本。
使用 SDK 下载页面或下载的 SDK 包中显示的 SDK 版本，例如生成的 `pom.xml` 中的版本。如果您更新了权限范围、API 版本或 SDK 框架，请重新生成并再次下载 SDK。有关更新流程，请参阅[更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk)。
# SDK 签名和 access token
对于 `ProductV202502Api` 等 SDK API 类，SDK 会在您配置 `ApiClient` 上的 `appKey`、`appSecret` 和 `basePath` 后签署 OpenAPI 请求。
SDK 不能替代 OAuth 授权。您仍然需要：

* 从卖家授权流程获取授权码。
* 将授权码交换为 `access_token` 和 `refresh_token`。
* 在服务器上安全地存储和刷新 token。
* 通过 `x-tts-access-token` 参数将当前卖家的 `access_token` 传递给 SDK API 调用。

如果您不使用 SDK 调用 TikTok Shop OpenAPI，请按照[签名您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)自行生成请求签名。
# 环境
确保您的项目满足以下所有条件：

* Java 1.8+
* Maven 3.8.3+ 或 Gradle 7.2+

# Maven 安装

1. 解压下载的 SDK 包以获取源代码。
2. 在 SDK 源代码目录中运行：

```Bash
mvn clean install
```


1. 将 SDK 依赖项添加到项目的 `pom.xml`。将 `${tts.sdk.version}` 替换为 SDK 包中或 SDK 下载页面上显示的版本。

```XML
<properties>
  <tts.sdk.version>VERSION_FROM_DOWNLOADED_SDK</tts.sdk.version>
</properties>

<dependencies>
  <dependency>
    <groupId>com.tiktokshop</groupId>
    <artifactId>open-sdk-java</artifactId>
    <version>${tts.sdk.version}</version>
    <scope>compile</scope>
  </dependency>
</dependencies>
```


1. 在项目中运行：

```Bash
mvn clean install
```

# Gradle 安装
将 SDK 依赖项添加到 `build.gradle`。将 `VERSION_FROM_DOWNLOADED_SDK` 替换为 SDK 包中或 SDK 下载页面上显示的版本。
```Groovy
repositories {
    mavenCentral()
    mavenLocal()
}

dependencies {
    implementation "com.tiktokshop:open-sdk-java:VERSION_FROM_DOWNLOADED_SDK"
}
```

# 手动 JAR 安装
如果您不使用 Maven 或 Gradle，通过运行以下命令生成 JAR：
```Bash
mvn clean package
```

然后手动安装生成的 SDK JAR 和依赖 JAR：

* `target/open-sdk-java-VERSION_FROM_DOWNLOADED_SDK.jar`
* `target/lib/*.jar`

# Get Authorized Shops 的 API 版本说明
Search Products 等 API 需要 `shop_cipher`。要获取 `shop_cipher`，请调用 [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)。
使用下载的 SDK 中实际生成的最新受支持 Get Authorized Shops API 版本。某些语言 SDK 指南可能显示更新的生成类，例如 Go 的 `AuthorizationV202502API`。本指南使用的 Java SDK 包将 Get Authorized Shops 暴露为 `AuthorizationV202309Api.authorization202309ShopsGet`，因此此 Java 示例使用 `AuthorizationV202309Api`。不要跨语言 SDK 混用类名。
如果下载的更新版 Java SDK 为 Get Authorized Shops 暴露了更新的授权类，请一致地更新 import、类名和方法名。
# 获取 access token
Java SDK 包包含 `AccessTokenAPI`，可以将授权码交换为 access token。授权码是短期且一次性的，因此不要在源代码中硬编码。
```Java
String appKey = System.getenv("TTS_APP_KEY");
String appSecret = System.getenv("TTS_APP_SECRET");
String authCode = System.getenv("TTS_AUTH_CODE");

AccessTokenAPI accessTokenAPI = new AccessTokenAPI(appKey, appSecret);
ResponseInfo tokenResponse = accessTokenAPI.getToken(authCode);

if (tokenResponse == null || tokenResponse.getCode() != 0 || tokenResponse.getData() == null) {
    String message = tokenResponse == null ? "null response" : tokenResponse.getMessage();
    throw new IllegalStateException("Failed to get access token: " + message);
}

String accessToken = tokenResponse.getData().getAccessToken();
String refreshToken = tokenResponse.getData().getRefreshToken();
```

# 获取 shop cipher
获取卖家 `access_token` 后，调用 Get Authorized Shops 并从返回的店铺列表中读取 `cipher`。
```Java
String contentType = "application/json";

AuthorizationV202309Api authApi = new AuthorizationV202309Api(defaultClient);
GetAuthorizedShopsResponse shopsResponse =
        authApi.authorization202309ShopsGet(accessToken, contentType);

if (shopsResponse == null || shopsResponse.getCode() == null || shopsResponse.getCode() != 0) {
    throw new IllegalStateException("Get Authorized Shops failed: " + shopsResponse);
}

if (shopsResponse.getData() == null || shopsResponse.getData().getShops() == null
        || shopsResponse.getData().getShops().isEmpty()) {
    throw new IllegalStateException("No authorized shops returned.");
}

String shopCipher = shopsResponse.getData().getShops().get(0).getCipher();
```

# 搜索商品
获取 `accessToken` 和 `shopCipher` 后，调用 Search Products。
```Java
ProductV202502Api productApi = new ProductV202502Api(defaultClient);
SearchProductsRequestBody requestBody = new SearchProductsRequestBody();
requestBody.setStatus("ALL");

SearchProductsResponse result = productApi.product202502ProductsSearchPost(
        1,
        accessToken,
        "application/json",
        null,
        shopCipher,
        requestBody
);

System.out.println(result);
```

如果 API 请求成功，您将收到类似以下的响应：
```JSON
{
  "code": 0,
  "data": {
    "next_page_token": "b2Zmc2V0PTAK",
    "products": [
      {
        "audit": {
          "status": "AUDITING"
        },
        "create_time": 1234567890,
        "id": "1729592969712207008",
        "integrated_platform_statuses": [
          {
            "platform": "TOKOPEDIA",
            "status": "PLATFORM_DEACTIVATED"
          }
        ]
      }
    ]
  }
}
```

# 代码示例
以下示例使用环境变量而非硬编码的敏感信息。在运行示例之前，请在本地环境或密钥管理器中配置以下值：
| 环境变量 | 描述 |
| --- | --- |
| `TTS_APP_KEY` | 来自 Partner Center 的 App key。 |
| `TTS_APP_SECRET` | 来自 Partner Center 的 App secret。仅限服务器端使用。 |
| `TTS_AUTH_CODE` | 来自授权重定向 URL 的卖家授权码。它是一次性的且短期有效。 |
| `TTS_OPEN_API_BASE_URL` | 可选。默认为 `https://open-api.tiktokglobalshop.com`。 |


```Java
import java.util.List;

import tiktokshop.open.sdk_java.api.AuthorizationV202309Api;
import tiktokshop.open.sdk_java.api.ProductV202502Api;
import tiktokshop.open.sdk_java.invoke.AccessTokenAPI;
import tiktokshop.open.sdk_java.invoke.ApiClient;
import tiktokshop.open.sdk_java.invoke.ApiException;
import tiktokshop.open.sdk_java.invoke.Configuration;
import tiktokshop.open.sdk_java.invoke.ResponseInfo;
import tiktokshop.open.sdk_java.model.Authorization.V202309.GetAuthorizedShopsResponse;
import tiktokshop.open.sdk_java.model.Authorization.V202309.GetAuthorizedShopsResponseDataShops;
import tiktokshop.open.sdk_java.model.Product.V202502.SearchProductsRequestBody;
import tiktokshop.open.sdk_java.model.Product.V202502.SearchProductsResponse;

public class Example {
    private static final String CONTENT_TYPE = "application/json";
    private static final String DEFAULT_BASE_PATH = "https://open-api.tiktokglobalshop.com";

    public static void main(String[] args) throws Exception {
        String appKey = requireEnv("TTS_APP_KEY");
        String appSecret = requireEnv("TTS_APP_SECRET");
        String authCode = requireEnv("TTS_AUTH_CODE");
        String basePath = optionalEnv("TTS_OPEN_API_BASE_URL", DEFAULT_BASE_PATH);

        AccessTokenAPI accessTokenAPI = new AccessTokenAPI(appKey, appSecret);
        ResponseInfo tokenResponse = accessTokenAPI.getToken(authCode);
        if (tokenResponse == null || tokenResponse.getCode() != 0 || tokenResponse.getData() == null
                || tokenResponse.getData().getAccessToken() == null) {
            String message = tokenResponse == null ? "null response" : tokenResponse.getMessage();
            throw new IllegalStateException("Failed to get access token: " + message);
        }

        String accessToken = tokenResponse.getData().getAccessToken();

        ApiClient defaultClient = Configuration.getDefaultApiClient()
                .setAppkey(appKey)
                .setSecret(appSecret)
                .setBasePath(basePath);

        String shopCipher = getFirstShopCipher(defaultClient, accessToken);
        searchProducts(defaultClient, accessToken, shopCipher);
    }

    private static String getFirstShopCipher(ApiClient defaultClient, String accessToken) throws ApiException {
        AuthorizationV202309Api authApi = new AuthorizationV202309Api(defaultClient);
        GetAuthorizedShopsResponse shopsResponse =
                authApi.authorization202309ShopsGet(accessToken, CONTENT_TYPE);

        if (shopsResponse == null || shopsResponse.getCode() == null || shopsResponse.getCode() != 0) {
            throw new IllegalStateException("Get Authorized Shops failed: " + shopsResponse);
        }

        if (shopsResponse.getData() == null || shopsResponse.getData().getShops() == null) {
            throw new IllegalStateException("No authorized shops returned.");
        }

        List<GetAuthorizedShopsResponseDataShops> shops = shopsResponse.getData().getShops();
        for (GetAuthorizedShopsResponseDataShops shop : shops) {
            if (shop.getCipher() != null && !shop.getCipher().isEmpty()) {
                System.out.println("Using authorized shop_id: " + shop.getId());
                return shop.getCipher();
            }
        }

        throw new IllegalStateException("No shop_cipher found in authorized shops.");
    }

    private static void searchProducts(ApiClient defaultClient, String accessToken, String shopCipher)
            throws ApiException {
        ProductV202502Api productApi = new ProductV202502Api(defaultClient);
        SearchProductsRequestBody requestBody = new SearchProductsRequestBody();
        requestBody.setStatus("ALL");

        SearchProductsResponse result = productApi.product202502ProductsSearchPost(
                1,
                accessToken,
                CONTENT_TYPE,
                null,
                shopCipher,
                requestBody
        );

        System.out.println("Search Products response: " + result);
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isEmpty()) {
            throw new IllegalStateException("Missing required environment variable: " + name);
        }
        return value;
    }

    private static String optionalEnv(String name, String defaultValue) {
        String value = System.getenv(name);
        return value == null || value.isEmpty() ? defaultValue : value;
    }
}
```

# 运行示例
在本地设置环境变量，然后编译并运行示例。
```Bash
export TTS_APP_KEY="YOUR_APP_KEY"
export TTS_APP_SECRET="YOUR_APP_SECRET"
export TTS_AUTH_CODE="AUTH_CODE_FROM_AUTHORIZATION_REDIRECT"

mvn clean test
```

不要将真实的 app secret、access token、refresh token 或授权码提交到源代码管理。
# 相关链接
| 链接 | 用途 |
| --- | --- |
| [下载 SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) | 为您的应用下载或重新生成 Java SDK 包。 |
| [更新 SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) | 了解何时更新 SDK 包以及如何迁移。 |
| [生成测试 access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) | 获取用于开发的测试授权码和 token。 |
| [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) | 获取店铺信息和 `shop_cipher`。 |
| [签名您的 API 请求](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | 在不使用 SDK 时手动签署 OpenAPI 请求。 |
