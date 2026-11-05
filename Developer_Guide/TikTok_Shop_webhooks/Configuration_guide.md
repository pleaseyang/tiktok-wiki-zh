# Configuration guide

Webhooks notify your HTTPS endpoint when subscribed TikTok Shop events occur. You can configure webhook subscriptions in Partner Center Console or with the Events API.
# Webhook configuration overview
There are two supported configuration methods:
| Method | Best for | Where to manage it |
| --- | --- | --- |
| Partner Center Console | Manual setup, first-time setup, and visual confirmation of webhook URL and selected topics. | **Partner Center Console > App & Service > Select your app or service > Basic Information > Developing** |
| Events API | Programmatic shop-level webhook configuration, automation, or configuration sync across shops. | `PUT /event/202309/webhooks`, `GET /event/202309/webhooks`, and `DELETE /event/202309/webhooks` |

Use one operational source of truth for each app or shop. Partner Center and the Events API manage the same webhook configuration surface; changes made in one place can affect what you see in the other.
# Requirements
Before you configure webhooks, make sure that:

* You understand the webhook event model and payload format. See [Webhooks overview](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview).
* Your app has the API scopes and topic permissions required by the events you want to subscribe to.
* Your receiving service exposes a reachable HTTPS endpoint that meets the webhook URL requirements below.
* If you use the Events API, you can send signed TikTok Shop API requests and provide a valid `x-tts-access-token` when the endpoint requires it. See [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request).

# Webhook URL requirements
| Requirement | Details |
| --- | --- |
| Scheme | Use `https://`. |
| TLS | Support TLS v1.2 or later. |
| Host | Use a domain name. Do not use an IP address. |
| Port | Do not include a custom port in the webhook URL. |
| Success acknowledgement | Return HTTP `200` within 3 seconds when the notification is accepted. |
| Authentication failure | Return HTTP `401` only when your service rejects the webhook signature or authentication. `401` is not a successful delivery acknowledgement. |
# Method 1: Configure webhooks in Partner Center Console
Use this path for webhook URL and topic configuration:
```Plain Text
Partner Center Console
  -> App & Service
  -> Select your app or service
  -> Basic Information
  -> Developing
  -> Webhook URL / Event subscriptions
```

Use **Development Kits > Webhook Log** only when you want to inspect delivery history. It is a monitoring entry, not the webhook configuration entry.
# Step 1: Configure the webhook URL
Add your HTTPS webhook receiver URL in the **Developing** section under **Basic Information**.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/84d2e7f5f4a94851b923a1308308aabc~tplv-k9wyc2ijk0-image.image)
creenshot reference: the webhook URL field is in the app or service configuration area, not in **Development Kits**.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5ab7fe180c1041f3ac0726950f072196~tplv-k9wyc2ijk0-image.image)

# Step 2: Choose webhook topics
Partner Center may preselect default webhook notifications for your app. The exact default set can vary by app type, market, seller type, and approved scopes, so confirm the selected default topics in the Partner Center subscription UI before launch.
For optional topics, select only the events your integration actually handles. Common webhook categories include:
| Topic category | Example use case | Subscribe when |
| --- | --- | --- |
| Order status updates | Receive a notification when an order is created or the order status changes. | Your app syncs orders, fulfillment state, or order lifecycle changes. |
| Order recipient address updates | Receive a notification when order recipient address information changes. | Your app needs to update shipping, warehouse, or fulfillment data after address changes. |
| Return, refund, or replacement updates | Receive a notification when a return, refund, or replacement status changes. | Your app manages post-sales workflows. |
| Product status updates | Receive a notification when product status changes. | Your app syncs product listing status or listing health. |
| Package or fulfillment updates | Receive package-related status changes when supported for your app and market. | Your app manages fulfillment, shipment, or delivery workflows. |
| Authorization lifecycle events | Receive `UPCOMING_AUTHORIZATION_EXPIRATION` or `SELLER_DEAUTHORIZATION` when supported. | Your app stores seller authorization tokens and needs to maintain or stop shop access. |

For the full and current event list, use the event list in [Webhooks overview](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview) and the event-specific reference pages linked from that overview.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/796b668db0b44dc196622dab013fc56d~tplv-k9wyc2ijk0-image.image)
creenshot reference: use this area to confirm which topics are selected by default and which optional topics you have enabled.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/7e97002885864b27921395d63794ea6e~tplv-k9wyc2ijk0-image.image)

# Step 3: Receive and verify webhook notifications
TikTok Shop sends an HTTP `POST` request to your configured URL when a subscribed event occurs. The request body contains JSON data for the event.
TikTok Shop verifies SSL certificates when delivering payloads to HTTPS webhook addresses. Make sure your server certificate is valid and trusted.
TikTok Shop places the webhook signature in the `Authorization` request header. This webhook signature is different from the signature you generate when your app calls TikTok Shop APIs. For webhook verification:

1. Read the raw request body exactly as received.
2. Concatenate `{app_key}{raw_webhook_payload}` with no added whitespace or reformatting.
3. Use your app secret as the HMAC-SHA256 key.
4. Compare the generated lowercase hexadecimal value with the `Authorization` header value.

Do not parse and re-serialize the JSON body before verification. Reformatting the body can change whitespace or field order and cause signature verification to fail. For the webhook signing example, see the **Webhooks Header and Body** section in [Webhooks overview](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview).
# Step 4: Respond to webhook notifications
Return a response within 3 seconds for each notification.
| Situation | HTTP status | Body | Meaning | Retry behavior |
| --- | --- | --- | --- | --- |
| Notification accepted and queued or processed | `200` | Empty body | Successful delivery acknowledgement. | TikTok Shop treats the notification as delivered. |
| Signature or authentication failed | `401` | Empty body | Your service rejected the notification. This is a valid semantic response for authentication failure, but not a success acknowledgement. | Treat as failed delivery. TikTok Shop may retry according to the retry schedule. |
| Timeout, network failure, or other non-200 response | Non-`200` or no response | Any | Delivery failed or was not acknowledged in time. | TikTok Shop retries according to the retry schedule. |

TikTok Shop stops retrying after the 4th retry failure.
| Retry | Trigger |
| --- | --- |
| 1st retry | 2 minutes after the initial push failure |
| 2nd retry | 30 minutes after the 1st retry failure |
| 3rd retry | 3 hours after the 2nd retry failure |
| 4th retry | 12 hours after the 3rd retry failure |

Webhook delivery is at-least-once. Your listener must be idempotent because the same event can be delivered more than once during retries. Store and deduplicate by `tts_notification_id` when it is present in the payload. If an event-specific payload does not include `tts_notification_id`, use the most stable available combination, such as event type, `shop_id`, timestamp, and the business object ID.
# Method 2: Configure webhooks with the Events API
Use the Events API when you need to create, inspect, or delete webhook subscriptions programmatically.
Before calling these APIs:
| Prerequisite | What to check |
| --- | --- |
| API access | Your app must have access to the Events API and the event topic you are configuring. Check the endpoint reference and **App & Service > Manage API** for the required scope or permission. |
| Seller/shop authorization | Use a valid `x-tts-access-token` when the endpoint requires seller-scoped authorization. |
| Request signing | Include the required OpenAPI query parameters such as `app_key`, `timestamp`, and `sign`. Generate `sign` with the TikTok Shop API request signing rules. |
| Shop context | Include `shop_cipher` when the endpoint or shop type requires a shop-level context. |
| Topic value | Use the exact `event_type` value from the event-specific reference page. |

Events API configuration and Partner Center configuration are not mutually exclusive. They update the same underlying subscription configuration. If you call **Update Shop Webhook** for a shop and event that was configured manually, the API can update or replace that shop-event configuration. After any API change, call **Get Shop Webhooks** or check Partner Center to confirm the final state.
Available Events API operations:
| API | Use it for |
| --- | --- |
| [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) | Create or update a shop webhook subscription for a specific event. This corresponds to setting the callback URL and selected topic in Partner Center. |
| [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) | Retrieve existing shop webhook configurations and verify the current callback URL and event subscriptions. |
| [Delete Shop Webhook](https://partner.tiktokshop.com/docv2/page/delete-shop-webhook) | Cancel a shop webhook subscription for a specific event. Use this only when you intentionally want to stop receiving that event. |
# Check webhook event history
Use this path to inspect webhook delivery logs:
```Plain Text
Partner Center Console
  -> Development Kits
  -> Webhook Log
  -> Select the app or service
```

The webhook log is for monitoring and debugging delivery history. Use it to confirm whether TikTok Shop sent a notification, which callback URL was used, and what response your server returned.
Screenshot reference: this screenshot shows the log and debugging entry under **Development Kits**, separate from the app configuration entry under **App & Service > Developing**.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5a30e72db1614b4ea89547aac013dc70~tplv-k9wyc2ijk0-image.image)

# Related pages
| Page | Use it for |
| --- | --- |
| [Webhooks overview](https://partner.tiktokshop.com/docv2/page/tts-webhooks-overview) | Webhook concepts, event list, payload format, and webhook signature verification example. |
| [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request) | Signing TikTok Shop API requests made by your app, including Events API requests. Do not use this algorithm as the webhook receiver verification algorithm. |
| [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) | Create or update a shop webhook subscription by API. |
| [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks) | Verify current shop webhook configuration by API. |
| [Delete Shop Webhook](https://partner.tiktokshop.com/docv2/page/delete-shop-webhook) | Delete a shop webhook subscription by API. |
