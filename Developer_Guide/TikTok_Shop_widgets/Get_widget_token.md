# Get widget token

# Overview
Use **Get Widget Token** to generate a short-lived `widget_token` for TikTok Shop Widget SDK integration.
The token flow is:
| Step | Actor | Token or interface | Purpose |
| --- | --- | --- | --- |
| 1 | Seller and developer backend | `access_token` | The seller authorizes the app, and the developer backend obtains an access token through the TikTok Shop authorization flow. |
| 2 | Developer backend | `GET /authorization/202401/widget_token` | The backend calls this Open API with the signed query parameters and `x-tts-access-token` header. |
| 3 | TikTok Shop Open API | `widget_token` | The API returns a short-lived widget token. It usually expires in about 5 minutes. |
| 4 | Developer backend and frontend | Developer-owned token endpoint, for example `/api/widget-token` | The backend returns the widget token to the frontend. Do not expose the seller `access_token` or App Secret to frontend code. |
| 5 | Frontend Widget SDK | `getToken` callback | The frontend SDK uses the widget token to load and call widget services. |

`access_token` and `widget_token` are different credentials. The `access_token` is used by the developer backend to call TikTok Shop Open APIs. The `widget_token` is a short-lived token passed to the Widget SDK.
# API endpoint
| Item | Value |
| --- | --- |
| API name | Get Widget Token |
| API version | `202401` |
| Host | `https://open-api.tiktokglobalshop.com` |
| Method | `GET` |
| Path | `/authorization/202401/widget_token` |
| Request body | None |
| Authentication | Signed common query parameters plus `x-tts-access-token` header |
# Domain and interface scope
Use the correct domain or interface for each part of the integration.
| Domain or interface | Use for | Called by |
| --- | --- | --- |
| `https://open-api.tiktokglobalshop.com` | TikTok Shop Open API resource server. Use this host to call `GET /authorization/202401/widget_token`. | Developer backend |
| `https://partner.tiktokshop.com` and `https://partner.us.tiktokshop.com` | Partner Center, documentation, app configuration, seller authorization entry, API Testing Tool, and support tickets. | Developers in browser / authorization flows |
| `/api/v1/seller/widget/get` | Widget SDK-side interface mentioned in the Widget SDK guide and SDK troubleshooting. Do not use it as the Open API endpoint for generating a widget token. | Widget runtime / SDK-side service |
# Request headers
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-tts-access-token` | string | Yes | The seller access token obtained through the TikTok Shop authorization flow. This token must belong to the seller/shop that will use the widget. |
| `Content-Type` | string | Yes | Use `application/json`. |
# Query parameters
This API has no required business request parameters. Use only the common signed query parameters for normal calls.
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `app_key` | string | Yes | The unique key assigned to your app in Partner Center. |
| `timestamp` | int64 | Yes | Unix timestamp in seconds. The same timestamp value must be used when generating `sign`. |
| `sign` | string | Yes | Signature generated from the request path, query parameters, request body if any, and App Secret. See [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request). |
| `shop_id` | int64 | No | Optional in the API schema, but not needed for normal calls. The seller/shop context is resolved from `x-tts-access-token`. Do not pass it unless TikTok Shop support or the API Testing Tool explicitly instructs you to do so. |
# Sample request
```Bash
curl --location --request GET 'https://open-api.tiktokglobalshop.com/authorization/202401/widget_token?app_key=<your_app_key>&timestamp=<unix_timestamp>&sign=<signature>' \
  --header 'Content-Type: application/json' \
  --header 'x-tts-access-token: <seller_access_token>'
```

# Response parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | int32 | Yes | The success or failure status code returned in the API response. |
| `message` | string | Yes | Success message or failure reason. |
| `request_id` | string | Yes | Request log ID. Include this value when contacting support. |
| `data` | object | No | Response data. |
| `data.widget_token` | object | No | Widget token information. |
| `data.widget_token.token` | string | No | The short-lived token passed to the Widget SDK. |
| `data.widget_token.expire_at` | int64 | No | Expiration timestamp of the widget token. The widget token usually expires in about 5 minutes. |
# Response sample
```JSON
{
  "code": 0,
  "data": {
    "widget_token": {
      "token": "<widget_token>",
      "expire_at": 1703100448
    }
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

# Frontend SDK handoff
Your frontend should call your own backend endpoint to get the widget token. The backend should call TikTok Shop Open API and return only the short-lived widget token information.
```TypeScript
async function getWidgetToken() {
  const response = await fetch('/api/widget-token', {
    method: 'GET',
    credentials: 'include'
  });
  const result = await response.json();

  if (result.code !== 0) {
    throw new Error(result.message || 'Failed to get widget token');
  }

  return result.data.widget_token;
}
```

When configuring `@tiktokshop/widget-kit` or `@tiktokshop/widget-kit-react`, pass this function to the SDK `getToken` field. The frontend SDK should receive a value with `token` and `expire_at`.
# Error codes
| Error code | Error message | Meaning | Recommended action |
| --- | --- | --- | --- |
| `98001001` | `internal error` | The service failed to retrieve the authorization or shop context. | Retry with exponential backoff. If the error persists, contact TikTok Shop support with `request_id`, app key, market, timestamp, and the full response. |
| `98001004` | `Invalid param` | A required query parameter or header is missing, invalid, or inconsistent with the generated signature. | Check `app_key`, `timestamp`, `sign`, `x-tts-access-token`, `Content-Type`, endpoint path, and API version. Regenerate the signature after confirming the exact request URL. |
| `13002013` | `Seller does not exist` | The access token does not map to a valid authorized seller/shop for this API call. | Confirm that the seller has authorized the app, use the correct seller `access_token`, refresh or re-authorize if needed, and verify the authorized shop mapping with Get Authorized Shops. |

Widget SDK errors are handled separately from this Open API response. For example, `/api/v1/seller/widget/get` errors such as domain whitelist mismatch, expired widget token, invalid widget token, app key mismatch, or shop/region mismatch should be debugged in the Widget SDK integration layer.
# Testing
You can test this API in the [API Testing Tool](https://partner.tiktokshop.com/docv2/page/api-testing-tool) or with a command-line client such as cURL.
Before testing:

1. Confirm that the app is created and the App Key is correct.
2. Complete seller authorization and obtain a valid seller `access_token`.
3. Generate the `sign` value using the exact request path and query parameters.
4. Pass `x-tts-access-token` in the request header.
5. After receiving `widget_token`, verify that your frontend SDK `getToken` callback returns the object containing `token` and `expire_at`.

# Related pages
| Page | Use it for |
| --- | --- |
| [Authorization guide](https://partner.tiktokshop.com/docv2/page/authorization-guide-202309) | Seller authorization and access token flow. |
| [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | Signature generation rules. |
| [API Testing Tool](https://partner.tiktokshop.com/docv2/page/api-testing-tool) | Testing Open API requests in Partner Center. |
| [Widget SDK user guide](https://partner.tiktokshop.com/docv2/page/widget-sdk-user-guide) | Frontend SDK integration and `getToken` callback usage. |
