# Overview

Webhooks enable real-time HTTPS notifications for TikTok Shop events. After a shop subscribes to a webhook topic, TikTok Shop sends an HTTP `POST` request to the callback URL registered by the app when the subscribed event occurs.
Do not rely on webhooks as the only source of truth. Network failures, endpoint downtime, retries, or delayed delivery can happen, so your system should also reconcile critical business state through scheduled API polling.
# How webhook delivery works
The diagram below shows the order-status webhook flow. The same delivery pattern applies to other webhook topics.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/33f8046e84ec4c6f9946d446020184da~tplv-k9wyc2ijk0-image.image)

1. The app subscribes to a webhook topic, such as `ORDER_STATUS_CHANGE`, for a shop.
2. The app registers an HTTPS endpoint hosted by the app server.
3. A matching business event happens in the shop, such as a new order or an order-status update.
4. TikTok Shop publishes the event to the subscribed webhook topic.
5. TikTok Shop sends a webhook request with the topic-specific payload to the registered endpoint.

# Webhook topic quick reference
Use the `event_type` value when configuring a shop webhook with the webhook API or in Partner Center. The delivered payload also contains a numeric `type` field. The shared Event API schema publishes the full `event_type` enum, but it does not publish a complete numeric `type` mapping for every topic. Do not branch only on the numeric `type`; use the subscribed `event_type` context and the topic-specific payload schema.
| Webhook topic | `event_type` value | Payload `type` value | Trigger scenario |
| --- | --- | --- | --- |
| Order status change | `ORDER_STATUS_CHANGE` | `1` in the sample payload; confirm against the topic page for production logic | An order is created or the order status changes. |
| Recipient address update | `RECIPIENT_ADDRESS_UPDATE` | See topic-specific payload reference | The recipient address of an order is updated. |
| Package update | `PACKAGE_UPDATE` | See topic-specific payload reference | A package is updated, such as being combined, split, or changed because of address updates. |
| Product status change | `PRODUCT_STATUS_CHANGE` | See topic-specific payload reference | Product audit results are updated. |
| Seller deauthorization | `SELLER_DEAUTHORIZATION` | See topic-specific payload reference | A seller revokes or loses authorization for the app. Use this event to stop API calls for the shop and clean up local connection state. |
| Upcoming authorization expiration | `UPCOMING_AUTHORIZATION_EXPIRATION` | See topic-specific payload reference | The seller authorization will expire soon. TikTok Shop sends this event 30 days before expiration and then daily at 00:00 until reauthorization is completed. |
| Cancellation status change | `CANCELLATION_STATUS_CHANGE` | See topic-specific payload reference | An order cancellation status changes. |
| Return status change | `RETURN_STATUS_CHANGE` | See topic-specific payload reference | An order return status changes. |
| New conversation | `NEW_CONVERSATION` | See topic-specific payload reference | A customer-service agent joins or leaves a conversation. |
| New message | `NEW_MESSAGE` | See topic-specific payload reference | A new message is sent in a customer-service conversation. |
| Product information change | `PRODUCT_INFORMATION_CHANGE` | See topic-specific payload reference | Changes to a product title, description, main images, or attributes go live. |
| Product creation | `PRODUCT_CREATION` | See topic-specific payload reference | A new product is created. |
| Product category change | `PRODUCT_CATEGORY_CHANGE` | See topic-specific payload reference | A product category is changed. |
| New message listener | `NEW_MESSAGE_LISTENER` | See topic-specific payload reference | A creator sends a message to the seller. |
| Invoice status change | `INVOICE_STATUS_CHANGE` | See topic-specific payload reference | The status of an invoice upload changes after using the Upload Invoice endpoint. |
| Product audit status change | `PRODUCT_AUDIT_STATUS_CHANGE` | See topic-specific payload reference | The product audit status changes. |
| Reverse status update | `REVERSE_STATUS_UPDATE` | See topic-specific payload reference | A buyer raises a cancellation, refund-only, or return-and-refund request that requires seller action. |
For shop connection lifecycle handling, subscribe to both `UPCOMING_AUTHORIZATION_EXPIRATION` and `SELLER_DEAUTHORIZATION` when your app needs to maintain long-lived shop access.
# Configure webhooks
You can configure a shop webhook in Partner Center or through the Event API.
In Partner Center, open the app or service and go to the webhook or event-subscription settings:
```Plain Text
Partner Center
  -> App & Service
  -> Select the app or service
  -> Webhooks / Event subscriptions
  -> Add or update the topic and callback URL
```

Console labels may vary by Partner Center version. The required configuration is the webhook topic, represented by `event_type`, and an HTTPS callback URL controlled by your app.
To configure a webhook by API, call **Update Shop Webhook**:
```HTTP
PUT https://open-api.tiktokglobalshop.com/event/202309/webhooks?app_key={app_key}&timestamp={timestamp}&sign={sign}&shop_cipher={shop_cipher}
Content-Type: application/json
x-tts-access-token: {access_token}

{
  "address": "https://example.com/tiktok-shop/webhooks",
  "event_type": "ORDER_STATUS_CHANGE"
}
```

Use **Get Shop Webhooks** to inspect the currently configured webhook topics and callback URLs for a shop. Use **Delete Shop Webhook** only when you intentionally want to remove a topic subscription.
# Header and signature verification
TikTok Shop sends the webhook signature in the HTTP `Authorization` header. The value is the lowercase hexadecimal HMAC-SHA256 digest. It is not a bearer token and should not include a `Bearer` prefix.
The signature is calculated as follows:
```Plain Text
signature_base_string = app_key + raw_request_body
signature = HMAC-SHA256(signature_base_string, app_secret)
```

Important validation rules:
| Rule | Why it matters |
| --- | --- |
| Use the raw request body exactly as received. | Re-serializing JSON, sorting keys, changing whitespace, or changing encoding will produce a different signature. |
| Calculate the signature before parsing or modifying the body. | Some web frameworks consume or normalize the body during JSON parsing. Store the raw body for verification. |
| Compare signatures using a constant-time comparison. | This avoids timing-based comparison leaks. |
| Reject missing or mismatched signatures. | The request should not be processed when the `Authorization` header is absent or invalid. |

Reproducible example:

1. App key:

```Plain Text
abcdef
```


2. Raw request body:

```JSON
{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}
```


3. Signature base string:

```Plain Text
abcdef{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}
```


4. App secret:

```Plain Text
123
```


5. HMAC-SHA256 result:

```Plain Text
5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05
```

Pseudocode:
```JavaScript
const crypto = require("crypto");

function verifyWebhookSignature({ appKey, appSecret, rawBody, authorization }) {
  const base = appKey + rawBody;
  const expected = crypto
    .createHmac("sha256", appSecret)
    .update(base, "utf8")
    .digest("hex");

  const expectedBuffer = Buffer.from(expected, "utf8");
  const receivedBuffer = Buffer.from(authorization || "", "utf8");

  return (
    expectedBuffer.length === receivedBuffer.length &&
    crypto.timingSafeEqual(expectedBuffer, receivedBuffer)
  );
}
```

# Body parameters
All webhook notifications include common metadata and a topic-specific `data` object.
| Param name | Sample | Description |
| --- | --- | --- |
| `type` | `1` | Numeric notification type in the delivered payload. Do not confuse this with the `event_type` string used when configuring webhook subscriptions. |
| `tts_notification_id` | `7380066284010030890` | Unique TikTok Shop notification ID. Store this value for idempotency and duplicate-event handling when present. |
| `shop_id` | `7495540735365777507` | TikTok Shop ID associated with the event. Use this to map the webhook to the local shop connection. |
| `timestamp` | `1718305585` | Unix timestamp, in seconds, when the notification was pushed. |
| `data` | `{"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}` | Topic-specific business payload. The fields depend on the webhook topic. |
# Sample request
The sample request below uses the same raw body and signature shown in the reproducible example.
```Bash
curl --location --request POST 'https://example.com/tiktok-shop/webhooks' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: 5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05' \
  --data-raw '{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}'
```

# Recommended listener behavior
| Situation | Recommended behavior |
| --- | --- |
| Valid signature and known `shop_id` | Process the event, update local state, and respond with a success status quickly. |
| Duplicate `tts_notification_id` | Treat the event as idempotent and avoid creating duplicate business records. |
| Unknown `shop_id` | Log the event and investigate whether the local shop mapping is missing or stale. |
| `SELLER_DEAUTHORIZATION` received | Mark the shop connection inactive, stop seller-scoped API calls for the shop, and ask the seller to authorize again if access is still required. |
| `UPCOMING_AUTHORIZATION_EXPIRATION` received | Notify the seller and route them through reauthorization before access expires. |
| Webhook delivery fails or is delayed | Reconcile through scheduled API polling for critical resources such as orders, packages, products, returns, and cancellations. |
# Related references

* [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks)
* [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook)
* [Delete Shop Webhook](https://partner.tiktokshop.com/docv2/page/delete-shop-webhook)
* [Order Status Change webhook](https://partner.tiktokshop.com/docv2/page/order-status-change)
* [Seller deauthorization webhook](https://partner.tiktokshop.com/docv2/page/65095746defece02be4d749d)
* [Upcoming authorization expiration webhook](https://partner.tiktokshop.com/docv2/page/6509579c0fcef602bf11312c)
* [Reauthorize shops](https://partner.tiktokshop.com/docv2/page/reauthorize-shops)
* [Disconnecting shops](https://partner.tiktokshop.com/docv2/page/disconnecting-shops)
