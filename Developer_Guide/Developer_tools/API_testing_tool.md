# API testing tool

The API Testing Tool helps developers test TikTok Shop Open APIs from Partner Center. It lets you select an API, fill request parameters, send a test request, inspect the response, and copy generated sample code when you test with your own app key.
# Feature updates
Feature update notes are maintained in the [changelog](https://partner.tiktokshop.com/docv2/changelog). Avoid treating dated examples on this page as the latest tool status. Use the changelog and the live API Testing Tool UI as the source of truth for newly released testing capabilities, supported API versions, and tool behavior changes.
# Before you call any API
> **Important:** Most API Testing Tool failures are caused by missing API scopes or missing seller/shop authorization. Before you test with your own app key, make sure the app has the required API scope and the seller or test shop has authorized that scope.

Pre-call checklist:

1. Open the endpoint reference page and identify the required API scope.
2. In Partner Center Console, go to **App & Service > Manage > Manage API** for your app.
3. Confirm that the required scope is enabled or approved for the app.
4. Complete seller/test-shop authorization for the app.
5. If you obtain an access token manually, confirm that the token response `granted_scopes` includes the required scope.
6. In the API Testing Tool, use the correct app key and fill the access token in the request token field, usually the `x-tts-access-token` header field for `202309` and later APIs.

Common authorization and scope errors:
| Symptom or code | Likely cause | What to check |
| --- | --- | --- |
| `105005 Access denied` | The app or access token does not contain the required API scope. | Check **App & Service > Manage > Manage API**, then compare the token's `granted_scopes` with the endpoint's required scope. |
| `105002 Expired credentials` | The access token has expired. | Refresh the token or authorize again. |
| `36009004 Invalid credentials` with `access_token` or `x-tts-access-token` message | The token is invalid, copied incorrectly, or belongs to the wrong authorization principal. | Generate a new token and paste it into the correct token/header field. |
| Empty or missing shops when testing shop APIs | The app has not been authorized by the target seller or test shop. | Use the tool's authorization function or follow the authorization guide to authorize the app. |
For broader troubleshooting, refer to Common errors and Access scope.
# What is the API Testing Tool?
The API Testing Tool enables developers to test TikTok Shop Open APIs directly in Partner Center.
You can use it to:

* select APIs and versions supported by the tool;
* fill query, header, path, and body parameters;
* send requests and inspect responses;
* validate whether your app key, scopes, authorization, token, and request parameters are correct;
* copy generated sample code, such as a `curl` request, when using your own app key.

The API Testing Tool is useful for manual validation and debugging. For production integrations, continue to implement signing, token refresh, retry, logging, and error handling in your own backend.
# Entry points
Use one consistent naming convention:
**Partner Center Console > Development Kits > API Testing Tool**
You can also open the direct entry:
[API Testing Tool](https://partner.tiktokshop.com/dev/api-testing-tool)
Do not confuse the tool entry with app configuration:
| Task | Partner Center path |
| --- | --- |
| Open the API Testing Tool | **Development Kits > API Testing Tool** |
| Find your app key | **App & Service > Manage > App details** |
| Configure API scopes | **App & Service > Manage > Manage API** |
| Authorize a test shop or seller | Use the API Testing Tool authorization flow, or follow Authorization Guide. |
If older screenshots use **Partner Console**, **Partner Center**, **Development**, or **Development Kits** inconsistently, treat **Partner Center Console** as the product area name and **Development Kits > API Testing Tool** as the tool entry.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/43e04e10d604411197ee5440c10497b3~tplv-k9wyc2ijk0-image.image)
# Choose an app key mode
| Mode | Best for | Supports | Limitations |
| --- | --- | --- | --- |
| Platform app key | Quick exploration before creating or selecting your own app. | Basic read-only `GET` API testing supported by the platform key. | Does not represent your app's scopes, authorizations, or market access. The tool may not provide generated request demo/sample code for this mode. |
| Your own app key | Realistic app debugging and integration validation. | App-specific API scopes, seller/test-shop authorization, access token, and generated sample code. | Requires app setup, scope configuration, and authorization before the call can succeed. |
# Using the platform app key
The platform app key is a built-in option in the API Testing Tool for basic API exploration. It lets developers try supported read-only APIs without first selecting their own app key.
Use it only for quick checks. It does not prove that your own app has access to the same endpoint. For app-specific testing, use your own app key.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2eb30f87ee764689a1d6f4dddabe875f~tplv-k9wyc2ijk0-image.image)
# Using your own app key
Use your own app key when you need to validate your actual app configuration, seller/test-shop authorization, request parameters, and generated sample code.
## Setup steps

1. Log in to [TikTok Shop Partner Center Console](https://partner-sso.tiktok.com/account/login).
2. Go to **App & Service > Manage > App details** and copy your **App Key**.
3. Go to **App & Service > Manage > Manage API** and enable or apply for the required API scope.
4. Authorize the seller or test shop for the app.
5. Open **Development Kits > API Testing Tool**.
6. Select **Use your own app key** and choose or paste your app key.
7. Select the API and API version you want to test.
8. Fill required query, path, header, and body parameters.
9. Fill the access token in the token/header field shown by the tool. For `202309` and later APIs, this is usually the `x-tts-access-token` header.
10. Send the request and inspect the response.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/124df2df16f1473ebacf959a88505e8d~tplv-k9wyc2ijk0-image.image)
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/99352b7e4739481e8f0d955583f64bf4~tplv-k9wyc2ijk0-image.image)
## Authorization and access token options
Your own app key must be authorized before you can test APIs that require seller, shop, creator, or partner data.
You have two options:
| Option | How it works | When to use |
| --- | --- | --- |
| Tool authorization flow | Use the authorization function provided in the API Testing Tool to authorize the test shop or seller, then continue testing in the tool. | Fastest path for tool-based manual testing. |
| Manual authorization flow | Follow Authorization Guide, obtain an `access_token`, and paste it into the API Testing Tool token/header field. | Use when you need to reproduce your real OAuth flow or debug token exchange. |
When manually backfilling a token, paste the `access_token` into the request token field shown by the API Testing Tool. For `202309` and later APIs, this maps to the `x-tts-access-token` header. Do not paste the refresh token into the request token field.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5fc05b9d5fbb4fe09944fbb4980e8be9~tplv-k9wyc2ijk0-image.image)
# Tips for using the API Testing Tool
| Tip | How to use it | Demo |
| --- | --- | --- |
| Documentation guide | When selecting an API, use the documentation guide to jump from the testing tool to the endpoint reference. When an API error occurs, use the error documentation guide to identify the likely issue and next step. | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/427ca078185944a6ae2cbed42e7af561~tplv-k9wyc2ijk0-image.image) <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3bf3df94b13e449a9a164015cb817b63~tplv-k9wyc2ijk0-image.image) |
| Sample code | When using your own app key, copy the generated request demo, such as `curl`, and run it in a terminal to reproduce the same request outside Partner Center. This is useful for comparing tool behavior with your backend implementation. | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b9883c37938b4d119ffd120c85d9352b~tplv-k9wyc2ijk0-image.image) <br/>  <br/> ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5ac394c4c7544b30bed4d4bfedea3d09~tplv-k9wyc2ijk0-image.image) |
# Quick troubleshooting flow

1. Confirm you are using the correct app key.
2. Confirm the endpoint's required API scope.
3. Confirm that the scope is enabled or approved in **App & Service > Manage > Manage API**.
4. Confirm that the seller or test shop has authorized the app after the scope was enabled.
5. Confirm that the access token is pasted into the correct request token/header field.
6. Confirm that the request method, path, API version, query parameters, body, and required identifiers such as `shop_cipher` match the endpoint reference.
7. If the same request works in the API Testing Tool but fails in your backend, compare the generated sample code with your backend signing, headers, token, and body serialization.
