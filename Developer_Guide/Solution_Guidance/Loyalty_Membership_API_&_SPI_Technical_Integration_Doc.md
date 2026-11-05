# Loyalty Membership API & SPI Technical Integration Doc

# Background and Objectives
This document is intended for merchants and ISV (Independent Service Vendor) integration development teams. It describes the external Open API and SPI interfaces required to integrate TTS with merchant's loyalty membership system. It focuses on the interface directions, common rules, request/response parameters, error codes, idempotency requirements, retry recommendations, and sequence diagrams. The goal of this document is to help developers:

* Query membership data on the TTS side for reconciliation and troubleshooting.
* Receive membership bind-check, bind/registration, and unbind notifications initiated by TTS via the merchant-provided SPI.
* Use key parameters such as `buyer_id`, `merchant_member_id`, `idempotency_key`, and `request_id` consistently to make requests traceable, retryable, and idempotent.

# Glossary
| **Term** | **Description** |
| --- | --- |
| TTS | TikTok Shop platform. |
| Merchant / ISV | Merchant system, or an authorized external independent service provider. |
| Buyer ID / `buyer_id` | A globally unique buyer identifier on the TTS side and the primary user identifier in membership APIs. |
| Merchant Member ID / `merchant_member_id` | The unique member identifier in the merchant membership system. |
| Open API | APIs that merchants / ISVs call to TTS. |
| Open SPI | APIs that TTS calls on the merchant side. |
# E2E Integration Process
This diagram demonstrates the E2E integration process for merchants/ISV after the launch of the Loyalty Membership MVP program. 
This diagram is only for integrating with existing API/SPIs. If the 3rd party wishes to create new API/SPIs, we will need to go through the standard requirement process, which involves the Bytedance RD developing and testing alongside the 3rd party. 


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b0f336e14038440ba8a6787cdc24877b~tplv-k9wyc2ijk0-image.image)
# Sequence Diagrams
The following sequence diagrams show only the external integration view. Participants are consolidated into three parties: TT App, TTS backend, and the merchant. We do not break down the merchant’s internal systems, and we do not expose any internal TTS domains, internal service names, or implementation details.
## Membership Binding / Enrollment
**Note**: Between TT App and the TTS backend, we only represent user actions and page outcomes, without specific request parameters. Between the TTS backend and the merchant, we keep the SPI semantics and key fields so that the merchant can understand the `MembershipBindCheck` and `MembershipBind` logic to implement.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/11cf7b181fb8451f92d578c5d5f9b9c9~tplv-k9wyc2ijk0-image.image)
## Membership Unbinding

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a24423b6fb3544e3a6690a432c9be397~tplv-k9wyc2ijk0-image.image)
## Reconciliation Queries
**Note**: Reconciliation is split into two independent scenarios: first, when the merchant sees a masked email in order events, it calls `MemberInfoQuery` to query TTS-side membership information; second, the merchant batch-syncs member profile, tier, or bind status to TTS via `MemberProfileBatchUpdate`.
### MemberInfoQuery API: Merchant queries TTS member information

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/78b94a872bc04acb855ce57a90eb7623~tplv-k9wyc2ijk0-image.image)
### MemberProfileBatchUpdate API: Merchant batch-updates TTS member profiles

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/785dcb88fba34792beb7c43a1471f3ab~tplv-k9wyc2ijk0-image.image)
# Integration Scope
| Direction | Interface | Purpose |
| --- | --- | --- |
| Merchant / ISV → TTS | **`MemberProfileBatchUpdate` API** | Batch update member profiles, tiers, or binding status for multiple members. |
| Merchant / ISV → TTS <br/>  | **`MemberInfoQuery` API** <br/>  | Query TTS-side membership data. When a masked email is seen in order events, it can be used to look up member information. |
| Merchant / ISV → TTS | **`CreateCoupon`** **API** |  |
| Merchant / ISV → TTS | **`DeactivateCoupon`** **API** |  |
| Merchant / ISV → TTS | **`LoyaltyProgramInfoUpdate`** **API** |  |
| TTS → Merchant / ISV | **`MembershipBindCheck` SPI** | Before binding or registration, check whether the buyer is already a merchant member. |
| TTS → Merchant / ISV | **`MembershipBind` SPI** <br/>  | Bind an existing member, or register and bind a new member. |
| TTS → Merchant / ISV | **`MembershipUnbind` SPI** | Notify merchants that the membership relationship has been unbound. |
| TTS → Merchant / ISV | **`MemberPointsQuery` SPI** | When the user views the membership page, query the current total points in real time. |
| TTS → Merchant / ISV | **`MemberPointsTransactionQuery` SPI** <br/>  | When the user views the points details page, query paginated points transactions. |
| TTS → Merchant / ISV | **`MembershipRedeem`** **SPI** |  |
| TTS → Merchant / ISV | **`MembershipRedeemReverse`** **SPI** |  |
# Common Rules
## Identifier Rules

* `buyer_id` is the globally unique buyer identifier on the TTS side and should be used as the primary user identifier for TTS membership APIs.
* `merchant_member_id` is the member identifier in the merchant membership system and should remain stable within the merchant’s membership program. It should be globally unique across shops under the same merchant membership program. If the merchant uses a group-level identifier or `merchant_member_id` is not globally unique across shops, the merchant must call this out during integration design so that the identifier granularity can be aligned before launch.

## `request_id` and `idempotency_key`

* `request_id` is returned in the API response as a unique trace ID for log lookup, troubleshooting, and retry handling; callers should not pass it in the request payload.
* Write operations should additionally carry an `idempotency_key` for business-level idempotency control.
* When retrying the same business operation, the caller must reuse the same `idempotency_key` and keep the payload unchanged.
* If the same `idempotency_key` is used with different payloads, the receiver should return an idempotency conflict error.
* Read-only APIs do not use `idempotency_key`, but should still return `request_id` for traceability.

## Common Open API Query Parameters
| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `app_key` | Query | string | Yes | App Key assigned after the application is created. |
| `timestamp` | Query | int64 | Yes | Unix timestamp for signature generation and request expiry validation. |
| `sign` | Query | string | Yes | Request signature generated per the Open Platform signing algorithm. |
| `shop_cipher` | Query | string | Yes | Authorized shop context identifier. |
## Common Open API Headers
| Header | Type | Required | Description |
| --- | --- | --- | --- |
| `content-type` | string | Yes | Fixed to `application/json`. |
| `x-tts-access-token` | string | Yes | Seller authorization access token. |
## Common Open API Response Envelope
Unless otherwise specified, the API returns the following top-level structure:
| Field | Type | Description |
| --- | --- | --- |
| `code` | int | `0` means success; a non-`0` value means failure. |
| `message` | string | Result description or error message. |
| `request_id` | string | Unique request identifier used for tracing and retry handling. |
| `data` | object | Business response payload returned per API scenario. |
# Open API Definitions
## MemberProfileBatchUpdate API
**Description**: Updates membership data for up to five buyers in one request. This operation supports bulk order processing, historical migration, and membership corrections. Each item carries its own `idempotency_key`; retries with the same key and identical item payload should return a stable result, while reusing the key with different item data should fail with an idempotency conflict.
| Type | Value |
| --- | --- |
| API Name | `member_profile_batch_update` |
| API Version | `202607` |
| Host / Scheme | `open-api.tiktokglobalshop.com` / HTTPS |
| API Path | `/customer_engagement/:version/member_profiles/partial_edit` |
| Method | `POST` |
### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `member_profiles` | array[object] | Y | Member profile updates. Maximum count is five. Each item is processed independently and the response preserves request item identity. |
### member_profiles Item
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | Unique buyer identifier on the TTS side. |
| `idempotency_key` <br/>  | string | Y | Unique key for retrying this member profile update item. Reusing the key with different item data returns `IDEMPOTENCY_CONFLICT`. |
| `bind_status` | string | N | Member binding status. Possible values include `UNKNOWN`, `BOUND`, `UNBOUND`, and `PENDING`. Allowed transitions include `UNKNOWN -> BOUND` and `BOUND <-> UNBOUND`. |
| `merchant_member_id` | string | N | Member identifier assigned by the merchant. |
| `program_level_name` | string | N | Merchant loyalty-program level name to set, for example `GOLD` or `SILVER`. |
| `program_level_expire_time_ms` | int64 | N | Unix timestamp in milliseconds when the loyalty-program level expires. |
| `update_time_ms` | int64 | N | Unix timestamp in milliseconds when the merchant generated this profile update. |
**Request body example:**
```JSON
{
  "member_profiles": [
    {
      "bind_status": "BOUND",
      "buyer_id": "7451234567890123456",
      "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
      "merchant_member_id": "MEMBER_10001",
      "program_level_expire_time_ms": 1798761600000,
      "program_level_name": "GOLD",
      "update_time_ms": 1785168000000
    }
  ]
}
```

### Response Parameters（Top-Level）
| Field | Type | Description |
| --- | --- | --- |
| `code` | int32 | The success or failure status code returned in the API response. |
| `message` | string | Success or failure message. Failure reasons are described in the message. |
| `request_id` | string | Request log ID returned in response to tracing and troubleshooting. |
| `data` | object | Specific return information. |
### data Object
| Field | Type | Description |
| --- | --- | --- |
| `total_count` | int32 | Total number of submitted member profile updates. |
| `success_count` | int32 | Number of member profile updates that succeeded. |
| `fail_count` | int32 | Number of member profile updates that failed. |
| `successes` | array[object] | Successful member profile update results. Empty result is returned as an empty array. |
| `errors` | array[object] | Failed member profile update results. Empty result is returned as an empty array. |
### successes Item
| Field | Type | Description |
| --- | --- | --- |
| `buyer_id` | string | Unique buyer identifier from the corresponding request item. |
| `idempotency_key` | string | Idempotency key from the corresponding request item. |
| `merchant_member_id` | string | Merchant member identifier from the corresponding request item. |
### errors Item
| Field | Type | Description |
| --- | --- | --- |
| `code` | string | Stable item result code. |
| `message` | string | Human-readable item result with corrective action when the update fails. |
| `detail` | object | Identifiers for the failed request item, including `buyer_id`, `idempotency_key`, and `merchant_member_id`. |
**Response body example:**
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "fail_count": 1,
    "errors": [
      {
        "code": "INTERNAL_ERROR",
        "detail": {
          "buyer_id": "7451234567890123456",
          "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
          "merchant_member_id": "MEMBER_10001"
        },
        "message": "INVALID_BUYER_ID"
      }
    ],
    "success_count": 1,
    "successes": [
      {
        "buyer_id": "7451234567890123456",
        "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
        "merchant_member_id": "MEMBER_10001"
      }
    ],
    "total_count": 2
  }
}
```

## MemberInfoQuery API
**Description**: Queries member profile data for up to 20 buyer IDs in one request. Merchants and authorized service providers can use the response to reconcile member identity, loyalty level, points, and binding status. This is a read-only operation and does not require `idempotency_key`. The returned email is subject to user authorization and platform data-protection policy.
| Type | Value |
| --- | --- |
| API Name | `Query Member Information` |
| API Version | `202607` |
| Host / Scheme | `open-api.tiktokglobalshop.com` / HTTPS |
| API Path | `/customer_engagement/:version/member_profiles/search` |
| Method | `POST` |
### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_ids` | array[string] | Y | Buyer IDs whose member information is queried. Maximum count is 20. |
**Request body example:**
```JSON
{
  "buyer_ids": [
    "7451234567890123456"
  ]
}
```

### Response Parameters（Top-Level）
| Field | Type | Description |
| --- | --- | --- |
| `code` | int32 | The success or failure status code returned in the API response. |
| `message` | string | Success or failure message. Failure reasons are described in the message. |
| `request_id` | string | Request log ID returned in the response for tracing and troubleshooting. |
| `data` | object | Specific return information. |
### data Object
| Field | Type | Description |
| --- | --- | --- |
| `member_profiles` | array[object] | Member profiles matching the submitted buyer IDs. Empty result is returned as an empty array. |
### member_profiles Item
| Field | Type | Description |
| --- | --- | --- |
| `bind_status` | string | Member binding status. Possible values include `UNKNOWN`, `BOUND`, `UNBOUND`, and `PENDING`. |
| `buyer_id` | string | Unique buyer identifier. |
| `email` <br/>  | string | Buyer email returned only with user authorization. The email may be masked according to platform data-protection policy. |
| `merchant_member_id` | string | Member identifier assigned by the merchant. |
| `points` | int64 | Current member points balance. |
| `expiring_points` | int64 | Member points scheduled to expire at `points_expire_time_ms`. |
| `points_expire_time_ms` | int64 | Unix timestamp in milliseconds when expiring points expire. |
| `program_level_name` | string | Merchant loyalty-program level name. |
| `update_time_ms` | int64 | Unix timestamp in milliseconds when the member profile was last updated. |
**Response body example:**
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "member_profiles": [
      {
        "bind_status": "BOUND",
        "buyer_id": "7451234567890123456",
        "email": "m***@example.com",
        "merchant_member_id": "MEMBER_10001",
        "points": 1250,
        "expiring_points": 200,
        "points_expire_time_ms": 1798761600000,
        "program_level_name": "GOLD",
        "update_time_ms": 1785168000000
      }
    ]
  }
}
```

## Create Membership Coupon API
Creates a full-shop membership coupon for the authorized shop and configures the points required to claim it.
### Basic Information
| Item | Value |
| --- | --- |
| Path | `/customer_engagement/202609/membership/coupons` |
| Method | `POST` |
| Version | `202609` |
| Idempotency | Required query parameter `idempotency_key` in UUID format. Retries must reuse the same key and payload. |
This API uses the common query parameters and headers defined in **Common Rules**. The query `timestamp` is Unix time in seconds. `app_key`, `sign`, `timestamp`, and `shop_cipher` are required; `x-tts-access-token` and `Content-Type: application/json` are required headers.
### Request Body Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `title` | string | Y | Merchant-defined coupon title. |
| `claim_duration` | object | Y | Period during which buyers may claim the coupon. |
| `redemption_duration` | object | Y | Period during which a claimed coupon may be redeemed. |
| `usage_limits` | object | Y | Per-buyer and total claim limits. |
| `discount` | object | Y | Amount-off or percentage-off discount configuration. |
| `threshold` | object | Y | No-threshold or minimum-spend requirement. |
| `points_required` | integer (int64) | Y | Non-negative points required to claim the coupon. 0 means no points are deducted. |
#### claim_duration Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `start_time` | string (date-time) | Y | RFC 3339 time when claiming starts. <br/>  |
| `end_time` | string (date-time) | Y | RFC 3339 time when claiming ends; must be later than start_time. |
#### redemption_duration Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string enum | Y | `ABSOLUTE` or `RELATIVE`. |
| `start_time` | string (date-time) | Conditional | Required for `ABSOLUTE`; prohibited for `RELATIVE`. |
| `end_time` | string (date-time) | Conditional | Required for `ABSOLUTE`; prohibited for `RELATIVE`. |
| `relative_duration_days` | integer (int32) | Conditional | Required for `RELATIVE`; minimum 1. Prohibited for `ABSOLUTE`. |
#### usage_limits Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `single_buyer_claim_limit` | integer (int32) | Y | Maximum claims per buyer; minimum 1. |
| `total_claim_limit` | integer (int64) | Y | Maximum total claims; minimum 1. |
#### discount Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string enum | Y | `AMOUNT_OFF` or `PERCENT_OFF`. |
| `reduction_amount` | string | Conditional | Required for `AMOUNT_OFF`; shop-currency amount such as 5.00. |
| `percentage` | string | Conditional | Required for `PERCENT_OFF`; decimal percentage from 0 through 100. |
| `max_discount` | string | N | Optional maximum shop-currency discount for `PERCENT_OFF`. |
#### threshold Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string enum | Y | `NONE` or `MIN_SPEND`. |
| `min_spend` | string | Conditional | Required for `MIN_SPEND`; shop-currency amount. Omit for `NONE`. |
### Request Example
```JSON
{
  "title": "Gold Member Welcome Coupon",
  "claim_duration": {
    "start_time": "2026-10-01T00:00:00Z",
    "end_time": "2026-10-31T23:59:59Z"
  },
  "redemption_duration": {
    "type": "RELATIVE",
    "relative_duration_days": 30
  },
  "usage_limits": {
    "single_buyer_claim_limit": 1,
    "total_claim_limit": 10000
  },
  "discount": {
    "type": "AMOUNT_OFF",
    "reduction_amount": "5.00"
  },
  "threshold": {
    "type": "MIN_SPEND",
    "min_spend": "30.00"
  },
  "points_required": 500
}
```

### Response data Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `coupon_id` | string | Y | Newly created membership coupon identifier. |
| `status` | string enum | Y | `NOT_START` or `ONGOING`. |
### Business Rules

* For relative redemption periods, duration is measured in whole days.
* Money fields are decimal strings in the shop currency; do not send binary floating-point values.
* Reuse the same idempotency key and identical payload for retries.

## Deactivate Membership Coupon API
Deactivates a membership coupon owned by the authorized shop. A deactivated coupon can no longer be claimed or redeemed.
### Basic Information
| Item | Value |
| --- | --- |
| Path | `/customer_engagement/202609/membership/coupons/{coupon_id}/deactivate` |
| Method | `POST` |
| Version | `202609` |
| Request Body | None |
This API uses the common query parameters and headers defined in **Common Rules**. The query `timestamp` is Unix time in seconds. `app_key`, `sign`, `timestamp`, and `shop_cipher` are required; `x-tts-access-token` and `Content-Type: application/json` are required headers.
### Path Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `coupon_id` | string | Y | Unique identifier of the membership coupon to deactivate. |
### Response data Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `coupon_id` | string | Y | Identifier of the deactivated coupon. |
| `title` | string | N | Merchant-defined coupon title. |
| `status` | string enum | Y | Always `DEACTIVATED` after success. |
### Business Rules

* Only coupons that have not started or are currently claimable can be deactivated.
* Deactivation prevents subsequent claim and redemption attempts.

## Update Loyalty Program Information API
Updates the authorized shop's loyalty program privacy policy links, points rules, and displayed benefits.
### Basic Information
| Item | Value |
| --- | --- |
| Path | `/customer_engagement/202609/loyalty_program/info/partial_edit` |
| Method | `POST` |
| Version | `202609` |
| Idempotency | Required query parameter `idempotency_key` in UUID format. Retries must reuse the same key and payload. |
This API uses the common query parameters and headers defined in **Common Rules**. The query `timestamp` is Unix time in seconds. `app_key`, `sign`, `timestamp`, and `shop_cipher` are required; `x-tts-access-token` and `Content-Type: application/json` are required headers.
### Request Body Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `privacy_policy_links` | array&lt;object&gt; | Y | Complete ordered list of privacy-policy links; 1–3 items. |
| `points_rules` | string | Y | Complete plain-text points rules, maximum 20,000 characters. HTML is not supported. |
| `sign_up_bonus` | object | N | Display-only sign-up bonus; TikTok Shop does not award points. Omit to keep the current setting. |
| `earning_rule` | object | N | Display-only earning rule; TikTok Shop does not calculate or award points. Omit to keep the current setting. |
#### privacy_policy_links Item
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `title` | string | Y | Display title, maximum 100 characters. |
| `url` | string (URI) | Y | HTTPS URL, maximum 2,048 characters. Do not use credentials, fragments, localhost, or private-network addresses. |
#### sign_up_bonus Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `is_enabled` | boolean | Y | Whether to display the sign-up bonus; `false` hides it. |
| `points` | integer (int64) | Conditional | Whole points for joining; minimum 1. Required when `is_enabled` is `true`. |
#### earning_rule Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `is_enabled` | boolean | Y | Whether to display the earning benefit; `false` hides it. |
| `method` | string enum | Conditional | `PER_SPEND`: points per `spend_amount` paid. `PER_ORDER`: fixed points per order. Required when `is_enabled` is `true`. |
| `points` | integer (int64) | Conditional <br/>  | Whole points per `spend_amount` or order; minimum 1. Required when `is_enabled` is `true`. |
| `spend_amount` | object | Conditional | Required for `PER_SPEND`; omit for `PER_ORDER`. |
#### spend_amount Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `amount` | string | Y | Decimal amount, for example `"1.00"`. Must be greater than 0. |
| `currency` | string | Y | Three-letter uppercase ISO 4217 currency code, for example `USD`. Must match the shop's currency. |
### Request Example
```JSON
{
  "privacy_policy_links": [
    {
      "title": "Membership Privacy Policy",
      "url": "https://www.example.com/membership/privacy"
    }
  ],
  "points_rules": "Members earn one point for every eligible dollar spent.",
  "sign_up_bonus": {
    "is_enabled": true,
    "points": 100
  },
  "earning_rule": {
    "is_enabled": true,
    "method": "PER_SPEND",
    "points": 1,
    "spend_amount": {
      "amount": "1.00",
      "currency": "USD"
    }
  }
}
```

### Response data Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string enum | Y | `ACTIVE` or `PENDING_VALIDATION`. |
### Business Rules

* The request replaces the complete privacy-policy link list and complete points-rules text.
* Privacy-policy links are displayed in request-array order.
* Reuse the same idempotency key and identical payload for retries.
* `sign_up_bonus` and `earning_rule` are display-only. TikTok Shop does not award or calculate points from them.
* Omit `sign_up_bonus` or `earning_rule` to keep that setting. Set `is_enabled` to `false` to hide the matching benefit.
* If both benefits are disabled or have never been set, the Benefits section is hidden.


# Open SPI Definitions
## MembershipBindCheck SPI
**SPI Code**: `MEMBERSHIP_BIND_CHECK` · **Version**: `202608`
**Description**: Checks whether a buyer may already have a merchant membership. The merchant matches a privacy-preserving email token and returns masked potential matches for buyer confirmation.
### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | TikTok Shop buyer identifier, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded TikTok Shop shop identifier, 1–128 characters. |
| `tts_shop_id` | string <br/>  | N | TikTok Shop ID associated with the request, 1–64 characters. This is not the Shop OpenID. If omitted, the merchant must continue processing with existing fields. |
| `email_match_token` | string | Y | Buyer-authorized masked email used for privacy-preserving matching, 3–320 characters. Match on visible characters; this is not an HMAC or authentication token and must not reveal the full email address. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `has_potential_matches` | boolean | Y | Whether one or more potential memberships were found. `true` requires at least one item in `potential_matches`; `false` requires an empty array. |
| `potential_matches` | array&lt;object&gt; | Y | Potential memberships for buyer confirmation. Return an empty array, never null, when no match is found. |
### `potential_matches` Item
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `masked_email` | string | Y | Partially concealed merchant-side email for buyer recognition, 3–320 characters. It must never contain the full email address. |
| `merchant_member_id` | string | Y | Stable merchant membership identifier, 1–128 characters. |
## MembershipBind SPI
**SPI Code**: `MEMBERSHIP_BIND` · **Version**: `202608`
**Description**: Links an existing merchant membership or registers and links a new membership after buyer authorization. TikTok Shop records the relationship only after a `BOUND` result. 
If the member is already bound, repeatedly calling this SPI should not return an error result. Instead, should return the latest member info. 

### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | TikTok Shop buyer identifier, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded TikTok Shop shop identifier, 1–128 characters. |
| `tts_shop_id` | string | N | TikTok Shop ID associated with the request, 1–64 characters. This is not the Shop OpenID. If omitted, the merchant must continue processing with existing fields. |
| `bind_type` | string enum | Y | `EXISTING_MEMBER` or `NEW_MEMBER`. |
| `merchant_member_id` | string | Conditional | Required for `EXISTING_MEMBER` and must be omitted for `NEW_MEMBER`; 1–128 characters. |
| `user_profile` | object | Conditional | Optional for `NEW_MEMBER` and must be omitted for `EXISTING_MEMBER`. The object and every attribute are optional because availability depends on buyer consent and profile completeness. Treat as personal data and do not log it. |
| `idempotency_key` | string (UUID) | Y | Stable operation key. Retries use the same key and identical payload and receive the original result; reusing the key with different business input must be rejected as a caller error. |
### `user_profile` Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | string (email) | N | Buyer-authorized contact email, maximum 320 characters. |
| `first_name` | string | N | Buyer-authorized given name, 1–128 characters. |
| `last_name` | string | N | Buyer-authorized family name, 1–128 characters. |
| `phone_number` | string | N | Buyer-authorized contact telephone number, 1–64 characters. |
| `birth_date` | string (date) | N | Buyer-authorized date of birth in YYYY-MM-DD format. |
| `full_name` | string | N | Buyer-authorized full name, 1–256 characters. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `bind_status` | string enum | Y | `BOUND` or `REJECTED`. |
| `merchant_member_id` | string | Conditional | Required for `BOUND`; must be omitted for `REJECTED`; 1–128 characters. |
| `program_level` | object | N | Merchant-defined level for a `BOUND` result; must be omitted for `REJECTED`. If present, name is required and expire_time is optional. |
| `points` | integer (int64) | N | Non-negative available balance after binding, including welcome points; `BOUND` only and omitted for `REJECTED`. |
| `expiring_points` | integer (int64) | N | Non-negative points scheduled to expire; `BOUND` only and omitted for `REJECTED`. Must appear together with `points_expire_time`. |
| `points_expire_time` | integer (int64) | N | Unix time in milliseconds when `expiring_points` expire; `BOUND` only and omitted for `REJECTED`. Must appear together with `expiring_points`. |
| `welcome_points` | integer (int64) | N | Non-negative points granted for the new membership; `BOUND` only and omitted for `REJECTED`. |
| `bind_time` | integer (int64) | N | Unix time in milliseconds when binding completed; `BOUND` only and omitted for `REJECTED`. |
| `reason_code` | string enum | Conditional | Required for `REJECTED` and must be omitted for `BOUND`. Values: `MEMBER_NOT_FOUND`, `REGISTRATION_REJECTED`, `MEMBER_CONFLICT`. |
| `reason_message` | string | N | Human-readable refusal explanation, maximum 500 characters; `REJECTED` only and omitted for `BOUND`. |
### `program_level` Object
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Y | Merchant-defined membership level name, maximum 128 characters. |
| `expire_time` | integer (int64) | N | Unix time in milliseconds when the membership level expires. |
## MembershipUnbind SPI
**SPI Code**: `MEMBERSHIP_UNBIND` · **Version**: `202608`
**Description**: Removes the TikTok Shop-to-merchant membership link. It must not terminate the underlying merchant membership.
### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | TikTok Shop buyer identifier, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded TikTok Shop shop identifier, 1–128 characters. |
| `tts_shop_id` | string | N | TikTok Shop ID associated with the request, 1–64 characters. This is not the Shop OpenID. If omitted, the merchant must continue processing with existing fields. |
| `merchant_member_id` | string | Y | Stable merchant membership identifier linked to the buyer, 1–128 characters. |
| `unbind_reason` | string enum | Y | `USER_REQUEST` or `PLATFORM_REVOKE`. |
| `idempotency_key` | string (UUID) | Y | Stable operation key. Retries use the same key and identical payload and replay the original result; reusing the key with different input must be rejected as a caller error. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `unbind_status` | string enum | Y | `UNBOUND` if this operation removed the link; `ALREADY_UNBOUND` if a new operation found no active link. Replaying an existing key returns its original result. |
| `unbind_time` | integer (int64) | Conditional | Required for `UNBOUND` and omitted for `ALREADY_UNBOUND`; Unix time in milliseconds when the merchant removed the link. |
## MemberPointsQuery SPI
**SPI Code**: `MEMBER_POINTS_QUERY` · **Version**: `202608`
**Description**: Read-only query for the current merchant membership points balance. The merchant remains the source of truth; this SPI does not use `idempotency_key`.
* Our system caches member points, so some updates may be slightly delayed.
* This SPI should be highly available because it directly affects the buyer experience.

### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | TikTok Shop buyer identifier, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded TikTok Shop shop identifier, 1–128 characters. |
| `tts_shop_id` | string | N | TikTok Shop ID associated with the request, 1–64 characters. This is not the Shop OpenID. If omitted, the merchant must continue processing with existing fields. |
| `merchant_member_id` | string | Y | Stable merchant membership identifier whose points are queried, 1–128 characters. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `membership_status` | string enum | Y | `BOUND` or `NOT_BOUND`. `NOT_BOUND` must omit all membership and points fields below. |
| `merchant_member_id` | string | Conditional | Required for `BOUND`; omitted for `NOT_BOUND`; 1–128 characters. |
| `points` | integer (int64) | Conditional | Required, non-negative current available balance for `BOUND`; omitted for `NOT_BOUND`. |
| `expiring_points` <br/>  | integer (int64) | N | Non-negative points scheduled to expire; `BOUND` only and omitted for `NOT_BOUND`. Must appear together with `points_expire_time`. |
| `points_expire_time` | integer (int64) | N | Unix time in milliseconds when `expiring_points` expire; `BOUND` only and omitted for `NOT_BOUND`. Must appear together with `expiring_points`. |
| `update_time` | integer (int64) | N | Unix time in milliseconds when the merchant last updated the balance; `BOUND` only and omitted for `NOT_BOUND`. |
## MemberPointsTransactionQuery SPI
**SPI Code**: `MEMBER_POINTS_TRANSACTION_QUERY` · **Version**: `202608`
**Description**: Read-only, cursor-paginated query for points transactions. Return transactions in descending `occur_time` order. This SPI does not use `idempotency_key`.
* This SPI should be highly available because it directly affects the buyer experience.

### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | TikTok Shop buyer identifier, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded TikTok Shop shop identifier, 1–128 characters. |
| `tts_shop_id` | string | N | TikTok Shop ID associated with the request, 1–64 characters. This is not the Shop OpenID. If omitted, the merchant must continue processing with existing fields. |
| `merchant_member_id` | string | Y | Stable merchant membership identifier whose `transactions` are queried, 1–128 characters. |
| `page_size` | integer (int32) | N | Maximum `transactions` to return, 1–50; default 20. |
| `page_token` | string | N | Opaque `next_page_token` from the previous response, maximum 1024 characters. Omit for the first page. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `membership_status` | string enum | Y | `BOUND` or `NOT_BOUND`. `NOT_BOUND` requires an empty `transactions` array and empty `next_page_token`. |
| `transactions` | array&lt;object&gt; | Y | Up to 50 `transactions` in descending `occur_time` order. Return an empty array, never null. |
| `next_page_token` | string | Y | URL-safe opaque next-page token, maximum 1024 characters and characters A–Z, a–z, 0–9, underscore, or hyphen only. Return an empty string on the last page; no padding or percent-encoded characters. |
### `transactions` Item
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `transaction_id` | string | Y | Globally unique merchant points transaction identifier, 1–128 characters. |
| `points_change_type` | string enum | Y | `EARN`, `DEDUCT`, `REFUND_REVERSE`, `ADJUST`, or `EXPIRE`. |
| `points_delta` | integer (int64) | Y | Signed points change: positive adds points and negative removes points. |
| `points` | integer (int64) | Y | Non-negative available balance immediately after the transaction. |
| `description` | string | Y | Merchant-provided, buyer-readable explanation, 1–500 characters. |
| `related_event_id` | string | N | Related merchant business event identifier, 1–128 characters. |
| `occur_time` | integer (int64) | Y | Unix time in milliseconds when the points transaction occurred. |
## MembershipRedeem SPI
**SPI Code**: `MEMBERSHIP_REDEEM` · **Version**: `202609` · **Direction**: TikTok Shop → Merchant / ISV
Atomically deducts the full points cost for a selected reward. TikTok Shop issues the coupon separately after a successful deduction.
### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | TikTok Shop buyer identifier, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded TikTok Shop shop identifier, 1–128 characters. |
| `tts_shop_id` | string | N | TikTok Shop ID, 1–64 characters. If omitted, continue processing with existing identifiers. |
| `merchant_member_id` | string | Y | Stable merchant membership identifier, 1–128 characters. |
| `reward_type` | string enum | Y | `COUPON` in this version. |
| `reward_id` | string | Y | Selected reward identifier, 1–64 characters. |
| `points_to_deduct` | integer (int64) | Y | Exact positive whole-number points cost; minimum 1. Partial deduction is unsupported. |
| `idempotency_key` | string (UUID) | Y | Stable business key. Retries must use the same key and identical payload. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `redeem_status` | string enum | Y | `SUCCEEDED` or `REJECTED`. |
| `redemption_id` | string | Conditional | Required for `SUCCEEDED`; 1–128 characters. Prohibited for `REJECTED`. |
| `deducted_points` | integer (int64) | Conditional | Required for `SUCCEEDED`; minimum 1 and must equal points_to_deduct. Prohibited for `REJECTED`. |
| `points` | integer (int64) | Conditional | Required for `SUCCEEDED`; non-negative balance after deduction. Prohibited for `REJECTED`. |
| `reason_code` | string enum | Conditional | Required for `REJECTED`; prohibited for `SUCCEEDED`. |
| `reason_message` | string | N | Optional for `REJECTED`, maximum 500 characters; prohibited for `SUCCEEDED`. |
### Response Examples
**Success**
```JSON
{
  "redeem_status": "SUCCEEDED",
  "redemption_id": "REDEMPTION_10001",
  "deducted_points": 100,
  "points": 1150
}
```

**Rejected**
```JSON
{
  "redeem_status": "REJECTED",
  "reason_code": "INSUFFICIENT_POINTS",
  "reason_message": "The member does not have sufficient available points."
}
```

### Business Rules

* A duplicate request with the same idempotency key returns the original result and must not deduct points again.
* SUCCEEDED means the full requested amount was deducted exactly once; REJECTED means no points were deducted.
* Use MembershipRedeemReverse only after coupon issuance definitively fails.

### Rejection Reason Codes
| Reason Code | Meaning |
| --- | --- |
| `INSUFFICIENT_POINTS` | Available balance is below the requested cost. |
| `MEMBER_NOT_FOUND` | No active membership relationship matches the buyer and shop. |
| `REWARD_NOT_AVAILABLE` | The selected reward or exchange rule is unavailable. |
## MembershipRedeemReverse SPI
**SPI Code**: `MEMBERSHIP_REDEEM_REVERSE` · **Version**: `202609` · **Direction**: TikTok Shop → Merchant / ISV
Restores the full points amount from a successful redemption when coupon issuance definitively fails.
### Request Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buyer_id` | string | Y | Buyer identifier from the original redemption, 1–64 characters. |
| `shop_open_id` | string | Y | Encoded shop identifier from the original redemption, 1–128 characters. |
| `tts_shop_id` | string | N | TikTok Shop ID, 1–64 characters. |
| `merchant_member_id` | string | Y | Merchant membership identifier from the original redemption, 1–128 characters. |
| `reward_type` | string enum | Y | `COUPON` in this version; must match the original redemption. |
| `reward_id` | string | Y | Reward identifier from the original redemption, 1–64 characters. |
| `redemption_id` | string | Y | Identifier returned by the successful MembershipRedeem call, 1–128 characters. |
| `points_to_reverse` | integer (int64) | Y | Exact positive whole-number points to restore; minimum 1 and must equal the full original deduction. |
| `reverse_reason` | string enum | Y | `COUPON_ISSUE_FAILED` in this version. |
| `idempotency_key` | string (UUID) | Y | Stable reversal key. Retries must use the same key and identical payload. |
### Response Parameters
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `reverse_status` | string enum | Y | `SUCCEEDED` or `REJECTED`. |
| `reversed_points` | integer (int64) | Conditional | Required for `SUCCEEDED`; minimum 1. Prohibited for `REJECTED`. |
| `points` | integer (int64) | Conditional | Required for `SUCCEEDED`; non-negative balance after reversal. Prohibited for `REJECTED`. |
| `reason_code` | string enum | Conditional | Required for `REJECTED`; prohibited for `SUCCEEDED`. |
| `reason_message` | string | N | Optional for `REJECTED`, maximum 500 characters; prohibited for `SUCCEEDED`. |
### Response Examples
**Success**
```JSON
{
  "reverse_status": "SUCCEEDED",
  "reversed_points": 100,
  "points": 1250
}
```

**Rejected**
```JSON
{
  "reverse_status": "REJECTED",
  "reason_code": "REDEMPTION_NOT_FOUND",
  "reason_message": "No successful original redemption was found."
}
```

### Business Rules

* Credit the same membership account that was debited by the original redemption.
* Partial reversal is unsupported; points_to_reverse must equal the full original deduction.
* A duplicate request with the same idempotency key returns the original result and must not credit points again.
* Reject the request if the buyer, member, reward, redemption ID, or points amount does not match the original redemption.

### Rejection Reason Codes
| Reason Code | Meaning |
| --- | --- |
| `REDEMPTION_NOT_FOUND` | No matching original redemption was found. |
| `REDEMPTION_NOT_SUCCEEDED` | The original redemption did not succeed, so there is nothing to reverse. |
| `REDEMPTION_MISMATCH` | Buyer, membership, reward, redemption, or points details do not match the original record. |
# Webhooks

* Order webhook: https://partner.tiktokshop.com/docv2/page/1-order-status-change#Back%20To%20Top
* Refund webhook: https://partner.tiktokshop.com/docv2/page/8y10pibm

# Security and Compliance Notes

* APIs only transmit the minimum necessary fields required for membership integration.
* Plaintext sensitive information such as phone number, email, name, or address should not appear in the standard interface parameters defined in this document. If matching requires such data, use compliant handling approaches agreed by both parties, such as hashed or encrypted identifiers.
* Callers should retain the `request_id` in request logs for retries, troubleshooting, and reconciliation.
* Merchants should ignore unknown extended fields to ensure backward compatibility.

## Masking Approach: Email 
**We do not mask the domain, only the local part.**
**Email is the only user information we transmit.** 

* For the local part, we have the following rules depending on the length of the local part n:
   * n = 1: eg. a@gmail.com -> *@gmail.com
   * n = 2: eg. ab@gmail.com -> a*@gmail.com
   * n = 3: eg. abc@gmail.com -> a*c@gmail.com
   * n = 4: eg. abcd@gmail.com -> a**d@gmail.com
   * n = 5: eg. abcde@gmail.com -> a***e@gmail.com 
   * n = 6: eg. abcdef@gmail.com -> a****f@gmail.com
   * n > 6: eg. abcdefg@gmail.com -> a****fg@gmail.com (mask at most 4 characters)
* This masking approach is used in the following API/SPI in the email field:
   * **MembershipBindCheck** SPI:
      * We mask members' email regardlessly 
      * For the return result, the matched emails must be returned as the mask-opposite of the input:

```JSON
Original email: abcdefg@gmail.com
Input email: a****fg@gmail.com
Output email: *bcde**@gmail.com 
Result: Match!
```


   * **MembershipBind** SPI: 
      *  We only mask new members who have not had an order in the past 90 days at the given shop
   * **MemberInfoQuery** API:
      * We only mask members who have not had an order in the past 90 days at the given shop

## Authentication Approach

* What are the authentication methods for TTS API, SPI, and webhooks? 
   1. API (ISV -> TTS):
      1. TTS APIs are verified with two fields: **x-tts-access-token (header)**, which is token value retrieved from **GetAccessToken** API; **shop-cipher (query)**, which is used to transmit the shop information, this value can be retrieved from [GetAuthorizedShops API](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309#Back%20To%20Top) **** (examples on how the request header, query, body should be configured via link)
      2. Authentication overview: https://partner.tiktokshop.com/docv2/page/authorization-overview-202407
   1. SPI (TTS -> ISV): 
      * Depends on the 3rd party, we currently use **IP Whitelist.** 
      * We also carry a field that has the value of the app secret created by ISV on our TTSPC platform, ISV could use this app secret to authenticate. 
      3. The TTS SPI should be verified with **x-tt-signature (header).** 
      4. The algorithm of the signature generation is below, please refer to this algorithm to verify the signature. For more information, please check [[External] SPI Integration Guide](https://bytedance.my.larkoffice.com/docx/HUa8diEO6oXem2xrZ3um8bbnyhc)

```JSON
canonical_query = Canonicalize(raw_query)

plaintext =
    app_secret
    + canonical_path
    + canonical_query
    + request_body
    + unix_timestamp
    + app_secret

signature = lowercase_hex(
    HMAC-SHA256(
        key  = app_secret,
        data = plaintext
    )
)
```


3. Webhook (TTS -> ISV):
   1. TTS webhooks are listed here in the official webhook documentation: https://partner.tiktokshop.com/docv2/page/1-order-status-change#Back%20To%20Top
   2. The webhook configuration guide includes information on how to authenticate TTS webhooks [https://partner.tiktokshop.com/docv2/page/configuration-guide#Back%20To%20Top](https://partner.tiktokshop.com/docv2/page/configuration-guide#Back%20To%20Top)

```JSON
signature_base_string = app_key + raw_request_body  
signature = HMAC-SHA256(signature_base_string, app_secret)
```

# Suggested Testing

* Please test your app end-to-end before launching. Below are some of the test cases you can test out, but please create your own test cases to ensure the behavior meets expectation before publishing.
* User Journey: [Loyalty Program User Experience and Incentive Policy](https://bytedance.larkoffice.com/wiki/TUkEwcpvviIVeKkPM4tc8VQunJQ)
* Please refer to the TTS developer guide for official E2E testing material: https://partner.tiktokshop.com/docv2/page/tts-developer-guide
1. **Prerequisites**
   1. **Environment and shop**
      1. In [TTS Partner Center](https://partner.tiktokshop.com/), Create a **Full Function Development Shop** (under Development Kits -> Development Shops) for testing.
         1. Publish at least one test product and publish the Shop Home design.
         2. Install and authorize the ISV app on the same Development Shop used for testing.
      2. Create a dedicated Buyer Test TikTok Account in the same region as the Development Shop and link it to your test shop under Development Kits -> Development Shops.

      **Steps**

         1. Create a second new TikTok account in the TikTok app, preferably with a testing email address.
         2. Log in to the TikTok app with the account you want to use as the buyer test account.
         3. In Partner Center, go to **Development Kits > Sandbox > Buyer test accounts**.
         4. Click **Link account**.
         5. Use the TikTok app to scan the QR code on the **Link TikTok account as buyer account** page.
         6. Follow the **Authorize TikTok Partner Center** flow in the TikTok app.
         7. Click **Link the account** on the buyer-account linking page.

      **Important notes**

         * Do **not** use a production or personal TikTok account. Once linked as a test account, it is permanently converted and cannot be reversed.
         * The buyer TikTok account must be in the **same region/market** as the development shop.
         * For Full Function testing, you need at least two TikTok accounts: one **Official Test TikTok Account** and one **Buyer Test TikTok Account**.
         * You cannot use the same TikTok account as both the official account and the buyer test account.
         * You can link up to **10 Buyer Test TikTok Accounts** to one Partner Center account.
      3. Ask the TikTok Shop team to enable Loyalty/Membership API/SPIs for whitelisting and the required frontend configuration for the test shop.
2. **Sample Test Cases**

### Unbound buyer precheck
**Preconditions:** the buyer has no active membership link; the test endpoint is published and online.

1. Open the member entry on Shop home page with the Buyer Test Account.
2. Trigger MembershipBindCheck/Precheck.
3. Capture the platform request ID and the ISV request ID.

**Expected result:** the SPI reaches the Integration Test URL, the response passes OAS validation, and the platform selects a valid registration or match path
### Register and bind
**Preconditions:** the buyer profile is UNBOUND, mobile phone can receive OTP

1. Select Join in the TikTok App.
2. Complete the OTP step.
3. Confirm the MembershipBind/Register SPI reaches the ISV.
4. Return a successful OAS-valid response.
5. Query the final membership profile or run BindCheck again.

**Expected result:** the buyer profile is BOUND, the ISV has exactly one member/link record, and reopening the member page does not create a duplicate membership.
### Idempotent bind retry

1. Send a valid Bind request and record the idempotency key.
2. Repeat the same request with the same key and payload.
3. Repeat the key with a different payload.

**Expected result:** the same key and payload returns the existing result without duplicate member creation or duplicate welcome reward; the same key with a different payload produces a deterministic conflict.
### Points balance and transactions

1. Query a newly bound member with zero balance.
2. Query a member with a positive balance.
3. Query an empty transaction list and a paginated non-empty list.
4. Compare UI/platform values with the ISV ledger.

**Expected result:** balances and transaction history match the ISV ledger; pagination, order, type, and time fields conform to OAS; the response completes with clear latency margin below the platform timeout.
### Unbind and rebind

1. Use the member-page menu to unlink the membership.
2. Confirm MembershipUnbind reaches the ISV.
3. Query the profile again.
4. Rebind the same buyer and verify the existing member is recognized.

**Expected result:** the profile becomes UNBOUND after unlink and returns to BOUND after rebind without losing the correct member identity or ledger.
### How to create a test order?
Create the test order from Development Shop (Sandbox) Buyer View after you have a linked buyer test account and at least one live test product.
**Prerequisites**

* Go to Partner Center Console > Development Kits > Development Shops.
* Create or use a Development Shop test account.
* Link a customer/buyer test TikTok account from Development Kits > Development Shops > Manage accounts > Settings.
* Use a buyer account in the same market/region as the development shop.
* Do not use a production TikTok account as the test buyer; once linked in Development Shop, the account becomes a test account permanently.
* Make sure the development shop has a live test product. For buyer-side purchases in the TikTok app, use a Full Function development shop; Core Function accounts do not support real buyer purchases.

**Partner Center Test Order flow**
Partner Center
 -> Development Kits
 -> Development Shops
 -> Manage accounts
 -> Buyer View
 -> Create test order
 -> Select products
 -> Select shipping option
 -> Order created with On Hold status
# Appendix
## Member Info Query

* Path: POST `/customer_engagement/202607/member_profiles/search`
* Example Request:

```Plain Text
curl -X POST \\ 
 'https://open-api.tiktokglobalshop.com/customer_engagement/:version/member_profiles/search?sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1623812664&app_key=38abcd&shop_cipher=GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3' \\ 
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \\ 
-H 'content-type: application/json' \\ 
-d '{
  "buyer_ids": [
    "7451234567890123456"
  ]
}'
```


* Example Response:

```JSON
{
  "code": 0,
  "data": {
    "member_profiles": [
      {
        "bind_status": "BOUND",
        "buyer_id": "7451234567890123456",
        "email": "m***@example.com",
        "merchant_member_id": "MEMBER_10001",
        "points": 1250,
        "expiring_points": 200,
        "points_expire_time_ms": 1798761600000,
        "program_level_name": "GOLD",
        "update_time_ms": 1785168000000
      }
    ]
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/03808268ed9d47b69786c45829bdc467~tplv-k9wyc2ijk0-image.image" width="1860px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fddc26a7056f49f58c5ef6296d97b970~tplv-k9wyc2ijk0-image.image" width="1812px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f44e0e9967274e8fba6feb9736c586ba~tplv-k9wyc2ijk0-image.image" width="1816px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3c4d946a71514ad593767cc483ffe6ba~tplv-k9wyc2ijk0-image.image" width="1812px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f4fd74c558024b08af9cc702bc8a36d1~tplv-k9wyc2ijk0-image.image" width="1782px" /></div>

## Member Profiles Batch Update

* Path: `/customer_engagement/202607/member_profiles/partial_edit`
* Example Request:

```JSON
curl -X POST \\ 
 'https://open-api.tiktokglobalshop.com/customer_engagement/:version/member_profiles/partial_edit?app_key=38abcd&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1623812664&shop_cipher=GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3' \\ 
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \\ 
-H 'content-type: application/json' \\ 
-d '{
  "member_profiles": [
    {
      "bind_status": "BOUND",
      "buyer_id": "7451234567890123456",
      "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
      "merchant_member_id": "MEMBER_10001",
      "program_level_expire_time_ms": 1798761600000,
      "program_level_name": "GOLD",
      "update_time_ms": 1785168000000
    }
  ]
}'
```


* Example Response:

```JSON
{
  "code": 0,
  "data": {
    "fail_count": 1,
    "errors": [
      {
        "code": "INTERNAL_ERROR",
        "detail": {
          "buyer_id": "7451234567890123456",
          "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
          "merchant_member_id": "MEMBER_10001"
        },
        "message": ""
      }
    ],
    "success_count": 1,
    "successes": [
      {
        "buyer_id": "7451234567890123456",
        "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
        "merchant_member_id": "MEMBER_10001"
      }
    ],
    "total_count": 2
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/31d8741b717747248d62731623cec2c5~tplv-k9wyc2ijk0-image.image" width="2048px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/dc651f316585479c8f10b8c093ddc268~tplv-k9wyc2ijk0-image.image" width="1864px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b5b77fb679c74c94b28b93b32a6ba71f~tplv-k9wyc2ijk0-image.image" width="1840px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/33311fa3ee2e4b878463262ebb78fdf9~tplv-k9wyc2ijk0-image.image" width="1800px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/d215c25dc0b347f2abb1531e5a0efb54~tplv-k9wyc2ijk0-image.image" width="1832px" /></div>


