# Rate limits

# Overview
The TTS Open Platform uses a dynamic QPS allocation mechanism. Your effective request capacity is calculated from multiple factors, including authorized shop scale, API resource characteristics, endpoint load, and platform-level protection rules.
Key principles:

* The platform does not expose a single fixed QPS query API for all endpoints.
* Endpoint reference documentation, if it publishes a specific limit or counting rule, takes precedence over this page.
* Build a self-adaptive client that reacts to throttling signals, smooths request bursts, uses batch APIs, caches hot data, and retries with exponential backoff plus jitter.
* A throttling response does not always mean your app alone exceeded its app-shop quota. It can also be caused by endpoint-level or platform-level protective throttling.

# 1. Why API Rate Limiting Exists
API rate limiting is a foundational mechanism that keeps the platform stable and fair. It serves two goals:

* **Platform stability**: prevents traffic spikes from overloading the service and degrading access quality for everyone.
* **Fair resource allocation**: distributes platform capacity equitably among developers, so a few apps cannot monopolize resources at the expense of others.

We strongly recommend every developer adopt industry-standard throttling, caching, batching, and retry patterns to build resilient applications.
# 2. Dynamic QPS Allocation
## 2.1 How Quota Is Calculated
Instead of a one-size-fits-all fixed quota, the platform computes effective request capacity dynamically.
| **Dimension** | **How It Affects Capacity** |
| --- | --- |
| **App authorization scale** (number of authorized shops) | Authorized shop count is a major input to your aggregate capacity. In general, more authorized shops means more total capacity, but the relationship is not guaranteed to be strictly linear. It may be stepwise, endpoint-weighted, and adjusted by platform conditions. Authorization changes may also take time to take effect across all rate-limit systems. |
| **API resource characteristics** (per-endpoint tiering) | Lightweight read APIs usually have higher tolerance than heavy read, write, or complex analytics APIs. Endpoint reference documentation takes precedence if it specifies a different limit, counting rule, or retry behavior. |
| **Real-time platform load** | The ceiling for an endpoint can be adjusted dynamically based on service health, traffic spikes, or protective controls. |
## 2.2 Capacity Planning Baseline
Because the platform quota is dynamic and endpoint-specific, the following values are **not guaranteed platform limits**. Use them only as conservative starting points for client-side throttling, capacity estimates, and load-test baselines when endpoint reference documentation does not publish an explicit value.
| **API type** | **Suggested initial dispatch target per App ID x Authorized Shop** | **How to use it** |
| --- | --- | --- |
| Heavy write APIs or complex analytics | 0.2-1 request/second | Start low, queue requests, and ramp only after sustained success without throttling. |
| Standard write APIs | 1-3 requests/second | Use idempotency keys or equivalent safeguards before enabling retries. |
| Standard read or sync APIs | 3-10 requests/second | Prefer incremental sync and avoid full pulls. |
| Lightweight read or batch APIs | 5-20 requests/second | Batch where possible and monitor 429 / `36009002` rates during ramp-up. |
Recommended ramp-up pattern:

1. Start from the low end of the relevant range.
2. Increase traffic gradually, for example by 20-30% every 10-15 minutes.
3. Stop ramping immediately when throttling, latency spikes, or error rates increase.
4. Treat the observed stable rate as an operational baseline, not as a guaranteed quota.

## 2.3 How Shop Scale Affects Capacity
Expanding shop authorization scale is the most direct way to increase aggregate capacity, but do not assume exact linear scaling.

* The total capacity generally increases as more shops authorize the same app.
* Capacity is still affected by endpoint tiering, platform load, and protective controls.
* Newly authorized shops may not raise effective capacity immediately in every internal rate-limit layer.
* For large promotions, migration bursts, or traffic peaks, validate capacity with gradual ramp tests.

# 3. Rate Limit Isolation and Trigger Dimensions
The minimum shop-scoped isolation unit is the **App ID x Authorized Shop** combination.
| **Dimension** | **When It Applies** | **What It Means** | **Developer Action** |
| --- | --- | --- | --- |
| App ID x Authorized Shop | Shop-scoped endpoints called with a valid shop authorization | The same shop authorized to different apps has independent app-shop capacity. The same app authorized to multiple shops has separate shop-level isolation units. | Throttle separately per app-shop pair. Do not let one shop's traffic consume another shop's queue. |
| App ID x endpoint or resource | App-level endpoints, or endpoints where no shop-level authorization applies | Some endpoints may be governed at the app/resource level rather than by shop. | Maintain endpoint-level limiters in addition to shop-level limiters. |
| Endpoint platform protection | Any endpoint during platform-wide traffic spikes or service pressure | The platform may temporarily lower available capacity for all callers, independent of your app's normal request rate. | Back off and retry. Do not assume adding shops immediately resolves this condition. |
| Abuse, security, or network protection | Abnormal bursts, high concurrency, suspicious patterns, or infrastructure-level controls | Additional controls may apply outside the normal app-shop quota model, including IP or traffic-pattern protection. | Smooth traffic, reduce concurrency, and contact support if throttling persists at very low request volume. |
| Unauthorized or unbound shop | Requests for shops that have not authorized the app, or invalid shop identifiers | This is usually an authorization or request validation problem, not a usable shop-level quota. | Fix authorization or shop identity first. Do not treat it as capacity. |
Implementation tip: Do not hard-code one global QPS threshold. Use separate limiters by app, shop, endpoint, and operation type, then adapt dynamically to throttling responses.
# 4. Throttling Signals and Response Handling
## 4.1 HTTP Status and Business Code Relationship
Rate limiting may be surfaced through both the HTTP layer and the response body:
| **Signal** | **Meaning** | **How to Handle** |
| --- | --- | --- |
| HTTP `429 Too Many Requests` | Transport-level throttling signal. | Treat as rate limited. Stop new requests for the affected limiter and retry with backoff. |
| Business code `36009002` | OpenAPI business error code for rate limiting or request frequency control. | Treat as rate limited even if your HTTP client or SDK surfaces the HTTP status separately. |
| HTTP `429` with body code `36009002` | The clearest rate-limit response: both transport and business layers agree. | Treat as rate limited. Log both fields for diagnosis. |
If either HTTP status `429` or business code `36009002` appears, handle the response as a throttling event. For monitoring, record both HTTP status and business code because SDKs, gateways, and logs may expose them differently.
## 4.2 429 vs. 503
Distinguishing `429` from `503` is the prerequisite for a robust client.
| **HTTP Status** | **Root Cause** | **Action** |
| --- | --- | --- |
| `429 Too Many Requests` | Your app exceeded the dynamically allocated capacity within the current isolation unit, or the endpoint hit platform-level protective throttling. | Stop sending new requests for the affected limiter. Retry using `Retry-After` if present, otherwise exponential backoff plus random jitter. Never retry immediately at high frequency. |
| `503 Service Unavailable` | Not a rate limit. The underlying service may be overloaded, temporarily unavailable, or under maintenance. | Retry after a short wait. If it persists, check developer announcements or contact technical support to verify whether a known incident is in progress. |
# 5. Best Practices
## 5.1 Use Batch APIs
The platform offers batch endpoints for many scenarios. Wherever a batch endpoint exists, do not loop the single-item endpoint. Collapsing N calls into one request is the most effective way to stay below the rate limit.
Batch endpoints are typically counted as one call per HTTP request, not per item in the batch, unless the endpoint documentation states otherwise.
## 5.2 Use Request Queues and Throttling
Maintain an internal request queue and dispatch at a smooth, controlled rate. Avoid bursts where many requests fire within a single second. Apply throttling separately by App ID, shop, endpoint, and operation type.
## 5.3 Fetch Only What You Need
Trim API requests to the minimum fields and volume your business actually requires. Avoid full-table pulls when incremental sync, cursor-based pagination, or changed-since filters are available.
## 5.4 Cache Hot Data
Cache low-churn, high-read data such as product master data, shop configuration, category mappings, and reference dictionaries on your side. This drastically reduces unnecessary API traffic.
## 5.5 Build Idempotent Writes and Tiered Error Handling

* Make write operations idempotent so retries cannot produce duplicates or dirty data.
* Distinguish `429`, business code `36009002`, `503`, other business errors, and network errors.
* Apply the right response to each class instead of using one retry policy for everything.

## 5.6 Use Exponential Backoff, Jitter, and Retry-After
When you receive HTTP `429` or business code `36009002`, retry with exponential backoff plus jitter. If the response includes a `Retry-After` header, honor it as the minimum wait time.
```Plain Text
wait = max(retry_after_seconds, min(base_delay * (2 ** retry_count) + random_jitter, cap))
```

Key parameters:

* `Retry-After`: if present, may be seconds or an HTTP date. Use it to avoid retrying earlier than the platform requested.
* `base_delay`: start at 1 second when no `Retry-After` header is present.
* Exponential growth: double the wait time on each failure, for example 1s -> 2s -> 4s -> 8s.
* `cap`: cap locally generated backoff, for example at 60 seconds. If `Retry-After` is longer, honor it or surface an alert instead of retrying early.
* `random_jitter`: add a small random offset, for example 0-500ms, to prevent multiple instances from synchronizing retries and creating a new spike.
* `max_retry_count`: set a maximum retry count, for example 5. Beyond that, alert or fall back to a degraded path.

Python reference implementation:
```Python
import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Optional

def parse_retry_after(value: Optional[str]) -> Optional[float]:
    if not value:
        return None

    try:
        return max(0.0, float(value))
    except ValueError:
        pass

    try:
        retry_at = parsedate_to_datetime(value)
        if retry_at.tzinfo is None:
            retry_at = retry_at.replace(tzinfo=timezone.utc)
        return max(0.0, (retry_at - datetime.now(timezone.utc)).total_seconds())
    except Exception:
        return None

def backoff_sleep(
    retry: int,
    retry_after: Optional[str] = None,
    base: float = 1.0,
    cap: float = 60.0,
) -> None:
    generated_wait = min(base * (2 ** retry) + random.uniform(0, 0.5), cap)
    header_wait = parse_retry_after(retry_after)
    wait = max(generated_wait, header_wait) if header_wait is not None else generated_wait
    time.sleep(wait)
```

# 6. FAQ
## Q1: How do I know exactly how much QPS quota my app gets?
Quotas are computed dynamically. The platform does not expose a fixed quota query API for all endpoints. Use endpoint reference documentation first if it publishes an explicit limit. Otherwise, use the capacity planning baseline in section 2.2 as a conservative starting point, then measure your stable rate through gradual ramp-up and throttling metrics.
## Q2: My business is growing fast. How do I increase my QPS quota?
The core idea of the dynamic allocation mechanism is that aggregate capacity generally grows with authorized shop scale. The most direct and recommended path is to expand your shop authorization scale.
However, do not assume every added shop increases every endpoint's QPS by the same fixed amount. The relationship may be non-linear, endpoint-weighted, stepwise, and affected by platform load. Authorization changes may also have propagation delays. For peak events, ramp gradually.
## Q3: I rarely send requests. Why do I still see 429 or 36009002 occasionally?
Common causes include:

1. **Sub-second bursts**: even when average QPS is low, several requests in the same second can trigger throttling. Use a request queue to smooth dispatch.
2. **Platform-level protective throttling**: when an endpoint's platform-wide load reaches a protective threshold, the platform may temporarily lower capacity for all callers. This is independent of your normal app request rate.
3. **Concurrency contention within the same isolation unit**: multiple app instances can stack requests within millisecond windows even if each instance appears safe alone.
4. **Endpoint-level constraints**: some endpoints may have stricter resource-level limits than your overall app-shop capacity.

The handling is the same: reduce concurrency, back off, honor `Retry-After` if present, and retry with jitter.
## Q4: How is QPS counted for batch endpoints vs. single-item endpoints?
Batch endpoints are typically counted as one call per HTTP request, not per item in the batch. Whenever a batch endpoint is available, prefer it. Refer to each endpoint's documentation for its exact counting rule.
## Q5: Should I retry every 429 or 36009002 response?
Retry only after backoff. Immediate high-frequency retries can worsen throttling and extend the restriction. For write APIs, retry only when the operation is idempotent or protected by an idempotency mechanism.
