# Download SDK

# Overview
Use this page when you need to download a TikTok Shop Open API SDK for the first time.
TikTok Shop SDK packages are generated from the effective apps and API access scopes available to your Partner Center account. The SDK package can differ by app, language, API version, and scope set. Always confirm the app list, scope list, language, SDK version, and generation time on the SDK download page before adding the SDK to your project.
# Before you download
Follow this sequence for a first-time integration:
| Step | Required before download? | Required before making SDK API calls? | What to do |
| --- | --- | --- | --- |
| Create a TikTok Shop app | Yes | Yes | Create the app and configure basic app information. See [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) or [Create a TikTok Shop app OAuth client](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client). |
| Configure API scopes | Yes, if the SDK should include those API domains | Yes | In **App & Service > Manage > Manage API**, enable or apply for the API scopes required by your integration. |
| Download SDK | Yes | Yes | Download the generated SDK package for your selected language from the SDK download page. |
| Create a test seller account or use an authorized seller | No | Yes | For test calls, create a test seller account or use an eligible seller account. See [Create a test seller account](https://partner.tiktokshop.com/docv2/page/create-test-seller-account). |
| Obtain an access token | No | Yes | Complete seller authorization and exchange the authorization code for an `access_token`. See [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token). |

The difference is intentional: app creation and scope configuration are required to generate a useful SDK package; a test seller account and access token are required when you actually run SDK calls that access seller or shop data.
# SDK download entry
Open the SDK download page from Partner Center:
| Entry type | Path or URL |
| --- | --- |
| Partner Center path | **Partner Center Console > Development Kits > API SDK** or the equivalent SDK download entry shown in your Partner Center navigation. |
| Direct URL | [https://partner.tiktokshop.com/openlearn/api-sdk](https://partner.tiktokshop.com/openlearn/api-sdk) |

If your Partner Center UI uses a slightly different label, search for **API SDK** or **SDK** under **Development Kits**. Avoid mixing this entry with **App & Service > Manage API**, which is used to configure API scopes rather than download SDK packages.
# Download steps

1. Sign in to Partner Center with the developer account that owns or manages the app.
2. Open **Development Kits > API SDK**.
3. Review the effective apps shown on the page.
4. Review the combined API access scopes included in the generated SDK.
5. Select the SDK language you plan to integrate, such as Java, Go, or Node.js if those options are available on the page.
6. Check the SDK version and generation time shown for that language.
7. Download the SDK package.
8. Store the downloaded package version, generation time, app key, language, and scope set in your project release notes so future SDK updates are traceable.

# Screenshot reference
The screenshot below is retained from the source guide. Use it together with the text steps above.
| Screenshot | What to look for | Action |
| --- | --- | --- |
| SDK download page | Effective apps, combined API access scopes, language selector or language tabs, SDK version/generation time, and download button. | Confirm the SDK includes the APIs and scopes you need, then download the package for your project language. |

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/download_sdk.PNG)
# Language and version selection
The SDK download page is the source of truth for the currently available SDK languages and package versions.
The language-specific integration guides currently cover:
| Language | Minimum environment from the integration guide | Version guidance |
| --- | --- | --- |
| Java | Java 1.8+; Maven 3.8.3+ or Gradle 7.2+ | Replace placeholder versions such as `1.0.0` with the SDK version shown on the download page. |
| Go | Go 1.18+ | Use the module path and version generated in the downloaded SDK package. |
| Node.js | Use a supported Node.js LTS release for new integrations. | Use the generated package or folder from the download page. Do not assume examples with placeholder versions are the latest package. |

There may not be a single global "latest SDK version" for all developers. SDK packages are generated based on your effective app, language, API scopes, and API versions. If the SDK page shows a version number or generation timestamp, use that value for your project records.
# Scope coverage
The SDK includes APIs from the combined API access scopes of your effective apps. Before downloading, confirm that the scopes shown on the page match the APIs your integration needs.
| Scope type | Meaning | What to check |
| --- | --- | --- |
| Public API scope | A standard API scope available to eligible developers after app setup and seller authorization. | Enable or apply for it in **App & Service > Manage > Manage API**, then confirm it appears in the SDK scope list. |
| Private API scope | A restricted scope granted only after TikTok Shop approval, invitation, market/category enablement, or partner-specific access. It may not be visible to all developers. | If your integration requires a private scope, follow the application path shown in Partner Center or contact your Partner Center support/partner manager. After approval, confirm the private scope appears in the effective scope list before downloading the SDK. |

Adding a new scope after the SDK is downloaded does not update your existing local SDK automatically. Confirm the new scope is approved, ask sellers to reauthorize if the new permission requires seller consent, then download the regenerated SDK.
# Download vs update
This page covers first-time SDK download. Use [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) when you already have an SDK integrated and need to refresh it.
| Page | Use it for |
| --- | --- |
| Download SDK | Find the SDK page, confirm effective apps and scopes, select a language, and download the SDK package for the first integration. |
| Update SDK | Understand when SDKs are regenerated, when to click **check for updates**, how daily generation works, and how to migrate an existing project. |
# Troubleshooting
| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Expected API is missing from the SDK | The required API scope is not enabled or approved for the effective app. | Check **App & Service > Manage > Manage API** and compare it with the SDK scope list. |
| Newly approved scope is not in the downloaded SDK | The SDK package has not been regenerated yet. | Wait for daily generation or use **check for updates** on the SDK page if available. |
| Seller API call fails even though the SDK contains the method | The seller has not authorized the required scope, or the token does not include it. | Complete seller authorization or reauthorization and check `granted_scopes` in the token response. |
| Language version in the example does not match your package | The example uses a placeholder or older version. | Use the SDK version and package structure shown in the downloaded package. |
# Related pages
| Page | Use it for |
| --- | --- |
| [Update SDK](https://partner.tiktokshop.com/docv2/page/update-sdk) | Regeneration triggers, manual update checks, and migration steps. |
| [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) | App creation, app type selection, scopes, redirect URL, and app credentials. |
| [Create a TikTok Shop app OAuth client](https://partner.tiktokshop.com/docv2/page/create-tts-app-oauth-client) | OAuth client setup for authorization code and token exchange. |
| [Create a test seller account](https://partner.tiktokshop.com/docv2/page/create-test-seller-account) | Test seller account setup before making SDK API calls. |
| [Generate a test access token](https://partner.tiktokshop.com/docv2/page/generate-test-access-token) | Access token generation for testing SDK calls. |
| [Access scope](https://partner.tiktokshop.com/docv2/page/access-scope) | Scope concepts and access management. |






## Prerequisites
If you are a developer who has developed Apps for TikTok Shop, you can download TikTok Shop API SDK on the [TikTok Shop Partner Center console](https://partner.tiktokshop.com/openlearn/api-sdk).
If you are a developer new to TikTok Shop, you must [create a TikTok Shop App](create-tts-app-oauth-client) before downloading the SDK on the [console](https://partner.tiktokshop.com/openlearn/api-sdk).
## Download SDK
The SDK includes APIs of the combined collection of access scopes corresponding to your effective apps. The effective apps and combined access scopes, private API scopes included, are listed on the page. Confirm the API access scopes included in the SDK before downloading the SDK.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/TTSPC_API_SDK/download_sdk.PNG)

