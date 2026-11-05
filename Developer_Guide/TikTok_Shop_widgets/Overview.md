# Overview

# Widget overview
TikTok Shop widgets are frontend components provided through the Widget SDK. A widget combines TikTok Shop-hosted user interface and platform capabilities for a specific seller workflow, such as warehouse settings, shipping template setup, product optimization, or order fulfillment.
Widgets do not replace TikTok Shop Open APIs. They are useful when you want to embed a TikTok Shop-managed UI into your app, while still keeping authorization, token exchange, and integration control in your own backend.
# API vs widget
| Area | TikTok Shop Open API | TikTok Shop Widget |
| --- | --- | --- |
| Integration model | Backend-to-backend REST API integration. | Frontend SDK integration with TikTok Shop-hosted UI. |
| UI ownership | You design and maintain the seller-facing UI in your app. | TikTok Shop provides the widget UI for the supported workflow. |
| Backend work | Required for API signing, access token storage, retries, data mapping, and error handling. | Still required for authorization, access token storage, widget token generation, and backend security. |
| Frontend work | Optional, depending on your own product UI. | Required. Your frontend initializes the SDK, loads the widget, and passes a `getToken` callback. |
| Flexibility | Highest flexibility because you own the full user experience. | Faster to integrate for supported scenarios, but the widget UI itself is not customizable. |
| Best for | Full custom workflows, backend automation, and data sync. | Embedding supported TikTok Shop workflows with lower UI build effort. |

Visual reference from the source guide:
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e843fec729141ff9c2bcd062983cd38~tplv-k9wyc2ijk0-image.image)
# Benefits
Widgets can help developers:

* reduce frontend build effort for supported seller workflows;
* provide a TikTok Shop-consistent workflow inside a third-party app;
* reduce errors caused by missing seller-side setup, such as warehouse or shipping template configuration;
* let sellers complete selected operational steps without switching back to Seller Center.

# Integration flow
Use this flow when integrating a widget:
| Step | What to do | Main entry or owner |
| --- | --- | --- |
| 1. Browse widgets | Review available widget options and read the detail page for each widget. | **Partner Center Console > Development Kits > Widget** |
| 2. Confirm availability | Confirm that the widget supports your app type, seller market, seller type, and use case. | Widget detail page and Partner Center UI |
| 3. Configure widget | Select the app and configure widget settings. | **Development Kits > Widget > Configure**, or the app detail page |
| 4. Allowlist domains | Add the root frontend domains where the widget will be embedded. | Widget configuration page |
| 5. Build token flow | Use a seller `access_token` on your backend to call Get Widget Token, then return the short-lived widget token to the frontend. | Your backend and [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) |
| 6. Initialize SDK | Pass the widget config and `getToken` callback to the Widget SDK. | [Widget SDK user guide](https://partner.tiktokshop.com/docv2/page/widget-sdk-user-guide) |
| 7. Test and launch | Test the widget with the correct app key, shop, market, domain, and widget name before release. | Partner Center, your staging environment, and support if needed |

Visual reference from the source guide:
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a1a917b63a1c400da3def8a0cd80f376~tplv-k9wyc2ijk0-image.image)
# Token flow
The frontend must not call TikTok Shop Open APIs directly. Use this token chain:
| Step | Token or call | Description |
| --- | --- | --- |
| 1 | Seller authorization | The seller authorizes your app and your backend obtains a seller `access_token`. |
| 2 | `GET /authorization/202401/widget_token` | Your backend calls Get Widget Token with the seller `access_token` in the `x-tts-access-token` header. |
| 3 | `widget_token` | TikTok Shop returns a short-lived widget token, usually valid for about 5 minutes. |
| 4 | SDK `getToken` callback | Your frontend calls your backend token endpoint and returns `{ token, expire_at }` to the Widget SDK. |

Keep the App Secret, signing logic, and seller `access_token` on your backend. Only the short-lived widget token should be handed to the frontend SDK.
# Before you begin
Before integrating a widget, confirm:

* the app has been created in Partner Center;
* the seller has authorized the app and the app has the required scopes;
* the widget is enabled or available for your app and use case;
* your frontend domain is ready for widget allowlisting;
* your backend can generate signed TikTok Shop Open API requests;
* your frontend can install and initialize the Widget SDK package.

# Step 1: Browse widget options
Use **Partner Center Console > Development Kits > Widget** to browse available widgets. If an older screenshot uses **Development kits > Widget**, treat it as the same Widget entry under **Development Kits**.
For each widget, click **Learn more** or open the widget detail page to check the latest description, prerequisites, market availability, and integration guide.
| Screenshot | What it shows | How to use it |
| --- | --- | --- |
| Widget tab entry | The **Development Kits > Widget** tab where available widgets are listed. | Open this page to browse widget options and compare scenarios. |
| Widget detail entry | The widget card or detail entry with a learn-more action. | Click the detail entry to review widget prerequisites and integration instructions. |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2d7fb32d36704133bc10cf9a9946f613~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/765bcb50a6754ec4909bf353232d21ab~tplv-k9wyc2ijk0-image.image)
# Step 2: Configure widget settings
In **Development Kits > Widget**, check the app list and whether widget settings are enabled for each app. Click **Configure** for the target app to open the app details or widget configuration page.
You can also start widget pre-configuration from the app detail page when creating or editing an app.
| Screenshot | What it shows | How to use it |
| --- | --- | --- |
| App list and widget status | A list of apps and whether each app has enabled widgets. | Select the target app and click **Configure**. |
| Configure action | The configure button or entry point for widget settings. | Use this button to jump to the app detail or widget configuration page. |
| App detail widget setting | Widget pre-setting configuration on the app detail page. | Use this when you are creating or editing the app and need to configure widget options. |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8943ab9293824232bf4252c8c5f1fc61~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/e0becb76e1e54345b42494d3a75ff8af~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/913e5f9d2e924d76b6838867538342f1~tplv-k9wyc2ijk0-image.image)
# Step 3: Configure domain allowlist
Add the frontend root domain where your app will embed the widget.
Rules:

* Use your own production or staging frontend domain. Do not use placeholder domains from examples.
* Include the scheme and host, for example `https://app.example.com`.
* Do not include paths such as `/settings/widgets`.
* Configure every frontend root domain that will load the widget.
* The source guide states that up to 10 URLs can be added. If Partner Center shows a different limit, follow the live UI.

| Screenshot | What it shows | How to use it |
| --- | --- | --- |
| Domain allowlist page | Widget domain URL configuration. | Add the root frontend domains that will host the widget and save the configuration. |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/0304ca539d2248868f29b3ba558f4899~tplv-k9wyc2ijk0-image.image)
# Step 4: Integrate and test
After widget configuration is complete:

1. Follow the widget-specific integration guide.
2. Install the Widget SDK package.
3. Implement a backend token endpoint that calls [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token).
4. Initialize the SDK with app key, shop ID, seller region, widget name, and `getToken`.
5. Test in a staging environment whose domain is already allowlisted.
6. Verify that browser errors are not caused by domain mismatch, expired widget token, app key mismatch, shop mismatch, or region mismatch.

# Widget scenarios
Widget availability can change by market, app type, seller type, and TikTok Shop enablement status. Do not rely on a copied market list such as "US" or "US and UK" as the source of truth. Confirm the current market availability in **Development Kits > Widget**, the widget detail page, or the integration material provided for your app.
| Widget | Use case | Market availability | Integration guide |
| --- | --- | --- | --- |
| Warehouse widget | Lets sellers enter or update delivery warehouse and return warehouse information, including contact, address, and sales range. This can reduce product listing failures caused by missing warehouse setup. | Confirm in Partner Center. | [Warehouse widget guide](https://partner.tiktokshop.com/docv2/page/66599ca675ead002e4e0c3fb) |
| Shipping template widget | Lets sellers set shipping templates required for seller-fulfilled listings, especially for 3PL workflows. | Confirm in Partner Center. | [Shipping template widget guide](https://partner.tiktokshop.com/docv2/page/66599c6d36f34802de23344e) |
| Product optimizer widget | Provides recommendations to improve product information quality and product performance after product sync. | Confirm in Partner Center. | [Product optimizer widget guide](https://partner.tiktokshop.com/docv2/page/66599c4236f34802de23338d) |
| Orders by TikTok Shipping widget | Helps sellers using TikTok Shipping process orders, create labels, print labels, and process shipments from the third-party app. | Confirm in Partner Center. | [Orders by TikTok Shipping widget guide](https://partner.tiktokshop.com/docv2/page/665999a9e5764002e59be4e2) |
# Widget demo screenshots
The screenshots below are retained from the source guide as visual examples. Use the live widget detail page to confirm current UI and supported markets.
| Widget | Screenshot |
| --- | --- |
| Warehouse widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/7407a25b6dec45318669705c9fe1e659~tplv-k9wyc2ijk0-image.image) |
| Shipping template widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/280f49b7ef964c38b41f83fe8e45aa0e~tplv-k9wyc2ijk0-image.image) |
| Product optimizer widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8fded8be498840c39c90597662675a41~tplv-k9wyc2ijk0-image.image) <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fd90ebe76bc04eda9b7695eb71e3e431~tplv-k9wyc2ijk0-image.image) |
| Orders by TikTok Shipping widget | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/331c80590868472d9ebf9ef49eff392c~tplv-k9wyc2ijk0-image.image) |
# Related pages
| Page | Use it for |
| --- | --- |
| [Get Widget Token](https://partner.tiktokshop.com/docv2/page/get-widget-token) | Backend token exchange from seller `access_token` to short-lived `widget_token`. |
| [Widget SDK user guide](https://partner.tiktokshop.com/docv2/page/widget-sdk-user-guide) | Frontend SDK installation, initialization, `getToken`, and widget troubleshooting. |
| [Authorization guide](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) | Seller authorization and access token flow. |
