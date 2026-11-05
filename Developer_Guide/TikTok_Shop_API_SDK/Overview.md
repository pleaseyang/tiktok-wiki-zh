# Overview

TikTok Shop API SDKs help the backend of your TikTok Shop app call TikTok Shop APIs with less integration work. They generate request clients and handle common request authentication steps, so you do not need to implement the signing flow for every supported API call yourself.
# Availability
The API SDK download page is available from Partner Center for developers who have an effective TikTok Shop app. To download a useful SDK package, sign in with the developer account that owns or manages the app, then confirm the effective apps and API access scopes shown on the SDK page.
Use the SDK download page as the source of truth for account-specific access. If the API SDK entry is not visible for your account, first confirm that you have created a TikTok Shop app and enabled the API scopes required by your integration. If the entry is still unavailable, contact Partner Center support or your TikTok Shop partner manager.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/81b2df68-85e8-4ded-8225-59e4f9a3063b.png)
# Supported Languages and Versions
The SDKs currently support Java, Go, and Node.js. SDK packages are generated based on your effective apps, approved API scopes, selected language, and available API versions, so there may not be a single global "latest SDK version" that applies to every developer.
Before integrating or updating an SDK, confirm the language, SDK version, generation time, included apps, and included API scopes on the [API SDK download page](https://partner.tiktokshop.com/openlearn/api-sdk). If you need newly approved scopes, newly released APIs, or SDK framework updates, see [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk).
| Language | Latest SDK version to use | Supported API versions |
| --- | --- | --- |
| Java | Use the version shown on the SDK download page or in the downloaded package files such as `pom.xml` or `build.gradle`. Replace placeholder values such as `1.0.0` in examples with that downloaded version. | The API versions included in your downloaded package. The Java guide examples include versioned clients such as `AuthorizationV202309Api` and `ProductV202502Api`. |
| Go | Use the module version generated in the downloaded SDK package. Replace placeholder values such as `v1.0.0` with the version from your package. | The API versions included in your downloaded package. The Go guide examples include versioned clients such as `AuthorizationV202502API` and `ProductV202502API`. |
| Node.js | Use the generated Node.js SDK package or folder from the SDK download page. Do not assume example dependency versions are the latest SDK package version. | The API versions included in your downloaded package. The Node.js guide examples include versioned clients such as `AuthorizationV202309Api` and `ProductV202502Api`. |
# Choose SDK or Manual Signing
Use the SDK when you are integrating in Java, Go, or Node.js and the API you need is included in the generated SDK package. The SDK is the preferred path for routine API calls because it reduces repetitive request construction and signing work.
Use manual signing when you call TikTok Shop APIs from another language, use a custom HTTP client that does not use the SDK, debug raw HTTP requests, or call an API that is not included in your generated SDK package. For the signing algorithm and language samples, see [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request).
# Webhook Configuration
The API SDK is for making TikTok Shop API requests. It does not replace your webhook configuration or webhook listener implementation. Configure webhook callback URLs and event subscriptions in Partner Center or through the Events API, then implement your own HTTPS endpoint to receive and process webhook events.
For webhook setup, see the [configuration guide](https://partner.tiktokshop.com/docv2/page/configuration-guide). For Events API references, see [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) and [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook).
# Integration Guides
Use the language-specific guide that matches the SDK package you downloaded:
| Language | Integration guide | Minimum environment from the guide |
| --- | --- | --- |
| Java | [Integrate Java SDK](https://partner.tiktokshop.com/docv2/page/integrate-java-sdk) | Java 1.8+; Maven 3.8.3+ or Gradle 7.2+ |
| Go | [Integrate GoLang SDK](https://partner.tiktokshop.com/docv2/page/integrate-golang-sdk) | Go 1.18+ |
| Node.js | [Integrate Node.js SDK](https://partner.tiktokshop.com/docv2/page/integrate-nodejs-sdk) | Node.js 16+ |
# Download and Update Flow

1. Create a TikTok Shop app and configure the API scopes required by your integration.
2. Open [API SDK](https://partner.tiktokshop.com/openlearn/api-sdk) in Partner Center.
3. Review the effective apps and combined API access scopes included in the generated SDK.
4. Select Java, Go, or Node.js and confirm the SDK version and generation time shown on the page.
5. Download the SDK package and integrate it by following the matching language guide.
6. When scopes, API versions, or SDK framework support change, follow [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) and download the regenerated package.

# Related Pages
| Page | Use it for |
| --- | --- |
| [Download SDK](https://partner.tiktokshop.com/docv2/page/download-sdk) | Find the SDK download entry and confirm effective apps, scopes, language, version, and generation time. |
| [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) | Understand SDK regeneration triggers, daily generation, and manual update checks. |
| [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) | Create an app and configure app type, scopes, redirect URL, webhook URL, app key, and app secret. |
| [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) | Generate an access token before making SDK calls against seller or shop data. |
| [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | Implement request signing manually when the SDK is not the right fit. |
| [Configuration guide](https://partner.tiktokshop.com/docv2/page/configuration-guide) | Configure webhook callback URLs and event subscriptions. |

