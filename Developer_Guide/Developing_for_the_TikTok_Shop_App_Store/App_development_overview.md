# App development overview


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a7ac69987a034bda96296e0b6be8a4b5~tplv-k9wyc2ijk0-image.image)
This page provides an overview of the typical development process for a TikTok Shop application.
If you have questions about any step, contact your partner manager or open a Partner Center support ticket. For support entry points and ticket guidance, see [How to contact support](https://partner.tiktokshop.com/docv2/page/how-to-contact-support).
**Developer type matters:** Public apps, custom apps, seller developer apps, and system integrator solutions can follow different review paths. Before you start, complete or review [Developer onboarding](https://partner.tiktokshop.com/docv2/page/developer-onboarding) so you know which app and developer type applies to your use case.
**Terminology:** This guide uses **Development Shop (sandbox)** as the standard name for the TikTok Shop testing environment. If another page or Partner Center menu uses **Sandbox**, it refers to the same Development Shop testing capability.
# Step 1: Design your app
Plan and design your solution using your preferred methodology. As you design your solution, we recommend that you:

* Review TikTok Shop APIs and use cases to determine which features to integrate into your app.
* Explore the [TikTok Shop Seller Academy](https://seller-us.tiktok.com/university/home?identity=1&role=seller) for marketplace policy guidance. Understanding seller workflows and platform policies helps you design an app that fits seller needs.
* Create seller and buyer test accounts in the [Development Shop (sandbox)](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops) environment so you can test both seller and buyer experiences before launch.

**Note:** TikTok Shop offers design review support for developers or system integrators creating public apps. Contact your partner manager for details.
# Step 2: Create your app in Partner Center
Creating an app in Partner Center establishes the workspace and credentials you need to integrate with TikTok Shop services. This step includes:

1. Determining the type of app you are building, such as public app or custom app.
2. Specifying basic app information, such as category, target market, app name, and logo.
3. Obtaining the app key and app secret required for TikTok Shop Open API calls.
4. Selecting API scopes and configuring webhooks for your app.

**Learn more:** See [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app). We also recommend reviewing:

* [Overview on TikTok Shop APIs](https://partner.tiktokshop.com/docv2/page/tts-api-concepts-overview)
* [Authentication Guide](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309)
* [Webhooks](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview)
* [Development Shop (sandbox)](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops)

# Step 3: Test your app
After you create your app in Partner Center and build your integration, test it with TikTok Shop services before launch.
If you have not already done so, create seller and buyer test accounts in the [Development Shop (sandbox)](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops). Development Shop (sandbox) lets you simulate seller workflows without affecting real shop data.
**Notes:**

* Public apps must complete testing before launch.
* Seller developers and system integrators building a custom solution for a single seller are not required to complete the public app testing phase, but testing in Development Shop (sandbox) is still recommended.
* You can only use test seller accounts created in Development Shop (sandbox) to test an unpublished app.

**Learn more:** See [Test your app](https://partner.tiktokshop.com/docv2/page/test-your-app) and [Development Shop (sandbox)](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops).
# Step 4: Initiate reviews and launch your app
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Develop_and_launch_a_TikTok_Shop_App/App_development_overview/Step4.jpeg)
Launching an app means publishing it for use and, for public apps, listing it on the TikTok Shop App and Service Store so sellers can discover it.
Review requirements vary by app type, app category, target market, and seller authorization scale. Public apps generally require the full launch review path. Custom apps can often launch privately through an authorization link, but some custom apps still require review, such as Connector apps or custom apps with 25 or more seller authorizations.
An **App Requirement Document (ARD)** is a review worksheet used to confirm app scope, required APIs, data handling, testing evidence, and launch readiness. If an ARD is required for your category or market, request the latest ARD template and submission path from your partner manager or through [Partner Center support](https://partner.tiktokshop.com/docv2/page/how-to-contact-support).
## Launch requirements quick reference
| Launch item | Public app | Custom app | Notes |
| --- | --- | --- | --- |
| Developer onboarding | Required | Required | Use [Developer onboarding](https://partner.tiktokshop.com/docv2/page/developer-onboarding) to confirm developer and app type. |
| Design review | Recommended or required when requested | Usually not required for single-seller custom solutions | Contact your partner manager if your public app needs design review support. |
| Testing in Development Shop (sandbox) | Required | Recommended | Custom apps for a single seller are not required to complete the public app testing phase, but should still test before production use. |
| Registration review | Required | Usually not required | Public app launch flow should start with registration review. |
| Language listing review | Required for each listing language or market | Not required | Prepare app listing content for each target market. |
| App review | Required | Required only for applicable custom apps | Custom apps may need review if they are Connector apps or reach 25 or more seller authorizations. |
| Compliance and legal review | Required when applicable | Required when applicable | Data security, privacy, and legal checks depend on app scope and data access. |
| Go-to-market plan | Usually required for public apps when requested | Usually not required for single-seller custom solutions | Coordinate with your partner manager for the required template and timeline. |
| Beta testing | Usually required for public apps when requested | Usually not required for single-seller custom solutions | Beta testing may be part of public app launch readiness. |
| Launch method | List on the TikTok Shop App and Service Store | Publish privately and share the authorization link | Public apps are discoverable by sellers; custom apps are distributed privately. |
## Typical launch for public apps
Follow the public app launch checklist in this order:

1. Initiate and pass registration review.
2. Initiate and pass language listing review for each market or language where you intend to list the app.
3. Initiate and pass app review.
4. Pass compliance and legal review when required by your app scope, data access, market, or category.
5. List your app on the TikTok Shop App and Service Store.

## Typical launch for custom apps
For a single-seller custom solution:

1. Publish your app.
2. Share the private authorization link with the seller.
3. Have the seller authorize the app.

If your custom app is a Connector app, reaches 25 or more seller authorizations, or falls under a category or market that requires review, follow the review instructions in Partner Center or from your partner manager before broader use.
**Learn more:** See [App Launch Overview](https://partner.tiktokshop.com/docv2/page/app-launch-overview), [Publish and list a public app](https://partner.tiktokshop.com/docv2/page/publish-and-list-public-app), [App review process](https://partner.tiktokshop.com/docv2/page/app-review-process), and [Compliance and legal review process](https://partner.tiktokshop.com/docv2/page/data-security-and-privacy-review).
# Next steps
Continue to [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) to create your app in Partner Center.
