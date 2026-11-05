# (64) Aftersales Request Status Update

# 1. Trigger scenario
The **Aftersales Request Status Update** webhook is triggered in two scenarios:

1. Buyer submits a return request in their TikTok user app.
2. A seller makes a decision on whether to approve or reject the request.


> **Note:** This is considered the **first-review** stage of the return journey. If the Afterales request is approved, it will enter the **second-review** stage, which is waiting for the seller to make a decision to approve or reject the returned items.


# 2. Data business parameters
| **Properties** | **Type** | **Example** | **Description** |
| --- | --- | --- | --- |
| shop_id | String | `7494049642642441621` | TikTok Shop identifier associated with the event. |
| timestamp | Int | `1732526400` | The time when this webhook was triggered, represented by Unix timestamp. |
| tts_notification_id | String | `7327112393057371910` | Unique notification identifier for deduplication and tracing. |
| type | Int | **`64`** | Numeric webhook event type. |
| data | Object |  |  |
| └ aftersales_request_id | String | `576486316948490001` | Unique identifier of the aftersales request. |
| └ return_role | String | `BUYER` | Role that initiated the return flow. Possible enumerations: <br/>  <br/> * `BUYER` <br/> * `SELLER` |
| └ aftersales_request_status | String | `PENDING_REQUEST_REVIEW` | Current aftersales request status. Possible enumerations: <br/>  <br/> * `PENDING_REQUEST_REVIEW` <br/> * `REQUEST_REVIEW_COMPLETED` |
| └ aftersales_request_create_time | Int | `1627587600` | Creation time of the aftersales request in Unix seconds. |
| └ aftersales_request_update_time | Int | `1644412885`  | Last update time of the aftersales request in Unix seconds. |


## Event example
```JSON
{
  "type": 64,
  "tts_notification_id": "1111111111",
  "shop_id": "1234567890",
  "timestamp": 1644412885,
  "data": {
    "aftersales_request_id": "576486316948490001",
    "return_role": "BUYER",
    "aftersales_request_status": "PENDING_REQUEST_REVIEW",
    "aftersales_request_create_time": 1627587600,
    "aftersales_request_update_time": 1644412885
  }
}
```


