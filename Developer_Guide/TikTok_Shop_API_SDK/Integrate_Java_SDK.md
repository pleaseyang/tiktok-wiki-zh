# Integrate Java SDK

# What this guide covers
This guide shows how to install the TikTok Shop Java SDK and make a first API call using [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202309) as the example.
Before you start, create a test seller account and authorize your app. For guidance, refer to [Create a test seller account](https://partner.tiktokshop.com/docv2/page/create-test-seller-account) and [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token).
# SDK version and update note
TikTok Shop SDK packages are generated for your app, language, and effective API scope set. Do not assume the placeholder version `1.0.0` is always the latest version.
Use the SDK version shown on the SDK download page or in the downloaded SDK package, such as the version in the generated `pom.xml`. If you update scopes, API versions, or the SDK framework, regenerate and download the SDK again. For the update flow, refer to [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk).
# SDK signing and access tokens
For SDK API classes such as `ProductV202502Api`, the SDK signs OpenAPI requests after you configure `appKey`, `appSecret`, and `basePath` on `ApiClient`.
The SDK does not replace OAuth authorization. You still need to:

* Obtain an authorization code from the seller authorization flow.
* Exchange the authorization code for an `access_token` and `refresh_token`.
* Store and refresh tokens securely on your server.
* Pass the current seller `access_token` to SDK API calls through the `x-tts-access-token` parameter.

If you call TikTok Shop OpenAPI without the SDK, follow [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) to generate the request signature yourself.
# Environment
Ensure your project meets all of the following conditions:

* Java 1.8+
* Maven 3.8.3+ or Gradle 7.2+

# Installation for Maven

1. Unzip the downloaded SDK package to obtain the source code.
2. In the SDK source directory, run:

```Bash
mvn clean install
```


1. Add the SDK dependency to your project's `pom.xml`. Replace `${tts.sdk.version}` with the version shown in the SDK package or on the SDK download page.

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


1. In your project, run:

```Bash
mvn clean install
```

# Installation for Gradle
Add the SDK dependency to `build.gradle`. Replace `VERSION_FROM_DOWNLOADED_SDK` with the version shown in the SDK package or on the SDK download page.
```Groovy
repositories {
    mavenCentral()
    mavenLocal()
}

dependencies {
    implementation "com.tiktokshop:open-sdk-java:VERSION_FROM_DOWNLOADED_SDK"
}
```

# Manual JAR installation
If you do not use Maven or Gradle, generate the JAR by running:
```Bash
mvn clean package
```

Then manually install the generated SDK JAR and dependency JARs:

* `target/open-sdk-java-VERSION_FROM_DOWNLOADED_SDK.jar`
* `target/lib/*.jar`

# API version note for Get Authorized Shops
`shop_cipher` is required by APIs such as Search Products. To get `shop_cipher`, call [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309).
Use the newest supported Get Authorized Shops API version that is actually generated in your downloaded SDK. Some language SDK guides may show a newer generated class, such as Go's `AuthorizationV202502API`. The Java SDK package used by this guide exposes Get Authorized Shops as `AuthorizationV202309Api.authorization202309ShopsGet`, so this Java example uses `AuthorizationV202309Api`. Do not mix class names across language SDKs.
If a newer downloaded Java SDK exposes a newer authorization class for Get Authorized Shops, update the import, class name, and method name consistently.
# Get access token
The Java SDK package includes `AccessTokenAPI`, which can exchange an authorization code for an access token. The authorization code is short-lived and single-use, so do not hardcode it in source code.
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

# Get shop cipher
After you have a seller `access_token`, call Get Authorized Shops and read `cipher` from the returned shop list.
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

# Search products
With `accessToken` and `shopCipher`, call Search Products.
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

If the API request succeeds, you will get a response similar to:
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

# Code demo
The following example uses environment variables instead of hardcoded secrets. Configure these values in your local environment or secret manager before running the demo:
| Environment variable | Description |
| --- | --- |
| `TTS_APP_KEY` | App key from Partner Center. |
| `TTS_APP_SECRET` | App secret from Partner Center. Keep it server-side only. |
| `TTS_AUTH_CODE` | Seller authorization code from the authorization redirect URL. It is single-use and short-lived. |
| `TTS_OPEN_API_BASE_URL` | Optional. Defaults to `https://open-api.tiktokglobalshop.com`. |


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

# Run the demo
Set environment variables locally, then compile and run the demo.
```Bash
export TTS_APP_KEY="YOUR_APP_KEY"
export TTS_APP_SECRET="YOUR_APP_SECRET"
export TTS_AUTH_CODE="AUTH_CODE_FROM_AUTHORIZATION_REDIRECT"

mvn clean test
```

Do not commit real app secrets, access tokens, refresh tokens, or authorization codes to source control.
# Related links
| Link | Use it for |
| --- | --- |
| [Download SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) | Download or regenerate the Java SDK package for your app. |
| [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) | Understand when to update SDK packages and how to migrate. |
| [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) | Obtain a test authorization code and token for development. |
| [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) | Retrieve shop information and `shop_cipher`. |
| [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | Manually sign OpenAPI requests when you are not using the SDK. |
