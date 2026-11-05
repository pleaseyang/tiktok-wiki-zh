# Test your App

Before you launch your app, test it in Partner Center using Development Shop (Sandbox) and API Testing Tool. These Partner Center tools help you simulate seller workflows, authorize a test seller account to an unpublished app, and verify API requests and responses before you publish.
Some test flows open Seller Center for the test seller account. Use Seller Center only as part of the Development Shop (Sandbox) testing flow; manage app creation, test accounts, API scopes, authorization, and API testing from Partner Center.
Use the following tools for app testing:

* Development Shop (Sandbox)
* API Testing Tool
* Postman or cURL for local and scripted API testing

# Development Shop
Development Shop is the sandbox testing environment in Partner Center. Related guides may also refer to this tool as Sandbox or Development Shop (Sandbox). In this guide, use Development Shop (Sandbox) to refer to the same Partner Center testing tool.
Development Shop allows you to build and test your app by simulating seller and buyer workflows without affecting production shop data. Full Function test accounts can support production-like seller workflows, including product management, orders, returns, refunds, promotions, and customer support functionality.
For unpublished apps, you can only test with test seller accounts created through Development Shop (Sandbox). Create the test seller account, authorize your app from that test seller account, then use the generated authorization data to call APIs and validate your integration.
**Learn more:** [Development Shop](https://partner.tiktokshop.com/docv2/page/seller-center-development-shops)
# Development Shop limitations
Before creating test accounts, review these limitations:

* Do not use production TikTok accounts as official test accounts or buyer test accounts.
* Once a TikTok account is linked in Development Shop (Sandbox), it is converted to a test account. This action is permanent and cannot be reversed.
* The TikTok account must be in the same region as the test shop. If you are not physically in the same region, use the required regional setup, such as removing the SIM card and using a VPN/IP location that matches the test shop region, before creating and linking the test account.
* Development Shop (Sandbox) data is isolated from production. Test operations do not affect real orders, real users, or production shop data.
* API Testing Tool keeps app and store authorization restrictions consistent with online stores, while sandbox stores may skip regional restriction verification for testing.

# How to test APIs
Testing your app's integration with TikTok Shop involves configuring API scopes, completing authorization, and calling the APIs required by your app's use cases.
Choose the guide based on what you need to test:

* [API Testing Tool](https://partner.tiktokshop.com/docv2/page/api-testing-tool) - Use this when you want to test directly in Partner Center and inspect exact request parameters, response parameters, sample code, and API documentation guidance.
* [Call Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/call-get-authorized-shops) - Use this as the first API call guide after you have an access token and signature. It explains the Open API domain, required headers, required query parameters, and the Get Authorized Shops request.
* [How to call APIs using Postman](https://partner.tiktokshop.com/docv2/page/call-tts-apis-with-postman) - Use this when you want local, repeatable, or scripted API testing with Postman environments, variables, pre-request scripts, and saved requests.

Use API Testing Tool for quick Partner Center testing and request/response inspection. Use Postman, cURL, or your own backend code when you need to test the same API flow repeatedly, automate signing, or debug your local integration.
# Minimum testing checklist
Use this checklist before submitting a public app for review or publishing a custom app:

1. Create or confirm your app in Partner Center.
2. Configure the required API scopes and webhook settings for the use cases you support.
3. Create a Development Shop (Sandbox) test seller account and a buyer test account.
4. Authorize the app with the Development Shop (Sandbox) test seller account.
5. Generate and store test access tokens securely.
6. Call core APIs for your app, such as authorization, products, orders, fulfillment, logistics, returns, refunds, or customer service APIs, depending on your scope.
7. Confirm that your app handles `shop_cipher`, seller/shop region, token expiration, token refresh, error codes, and API signatures correctly.
8. Trigger and verify required webhooks, including delivery, retry handling, de-duplication, and idempotent processing.
9. Run seller and buyer workflows end to end in Development Shop (Sandbox), including product setup, order placement, order status changes, cancellation, return, or refund flows as applicable.
10. Record test evidence, key request IDs, webhook event IDs, and unresolved issues before moving to app review or launch.

# How to get help with testing your app
If you have questions about testing your app, you can connect with the Partner Center Support team in the following ways:

* [Contact us through email](https://partner.tiktokshop.com/docv2/page/how-to-contact-support#Option%201:%20Contact%20us%20through%20email)
* [Submit a ticket](https://partner.tiktokshop.com/docv2/page/how-to-contact-support#Option%202:%20Submit%20a%20ticket%20through%20the%20Partner%20Console) through Partner Center (login required)

# Next Steps
Continue to the [App Launch Overview](https://partner.tiktokshop.com/docv2/page/app-launch-overview) to learn how to publish and list your app on the TTS App & Service Store.
