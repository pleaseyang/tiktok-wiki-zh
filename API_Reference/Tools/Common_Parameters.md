# Common Parameters

When calling TikTok Shop APIs, include the following common parameters unless the endpoint documentation states otherwise.
# Query parameters
| **Parameter** | **Location** | **Type** | **Description** | **Sample** |
| --- | --- | --- | --- | --- |
| `app_key` | Query | string | The unique key assigned to your app. Refer to Create your app to find out where to get your **`app_key`**. | 29a39d |
| `sign` | Query | string | A HMAC-SHA256 hash based on the request parameter values, used by the service to verify the sender of the request in addition to the access token. <br/> Refer to Sign your API request to learn how to generate this signature. | bc721f0e0182914e3487b81df204de37a352fc3aa96947efda6dc1e5dd0d5290 |
| `timestamp` | Query | Unix timestamp | A 10-digit Unix timestamp in seconds, used to ensure timeliness of the request and prevent replay attacks. Do not send a millisecond-level timestamp. This value is also used to generate the digital signature for the **`sign`** parameter. <br/> Valid range: [current time - 5 mins, current time + 30 secs]. Sending an invalid timestamp may cause error `36009004 Invalid timestamp`. | 1623812664 |
# Header parameters
| **Parameter** | **Type** | **Description** | **Sample** |
| --- | --- | --- | --- |
| `x-tts-access-token` | string | The access token used to authenticate the shop or seller authorization for the request. For API version `202309` and later, the access token must be sent in this header instead of the query string. | act.example_access_token |
| `content-type` | string | The request content type. Use `application/json` when sending a JSON request body. | application/json |

> **Version note:** For legacy APIs before version `202309`, some older documents may show `access_token` as a query parameter. For API version `202309` and later, use the `x-tts-access-token` header.

# Endpoint-specific common identifiers
Some endpoints require common business identifiers in addition to the parameters above. Whether these fields are required depends on the specific endpoint. Always follow the endpoint documentation for the exact location, requirement, and allowed value.
| **Parameter** | **Location** | **Type** | **Description** | **Sample** |
| --- | --- | --- | --- | --- |
| `shop_cipher` | Depends on endpoint | string | The encrypted shop identifier. Include this field when the endpoint requires a shop-level identifier. If the field is part of the signed request parameters for the endpoint, include it when generating `sign`. | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMtA |
| `category_asset_cipher` | Depends on endpoint | string | The encrypted category asset identifier. Include this field when the endpoint requires a category asset identifier. If the field is part of the signed request parameters for the endpoint, include it when generating `sign`. | CAT_ASSET_XF90igAAAABh00qsWgtvOiGFNqyubMtA |
