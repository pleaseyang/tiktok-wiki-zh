# (65) RMA Status Update

Use this webhook to track the package-level lifecycle for the RMA object generated from approved items in the Aftersales Request.
# 1. Trigger scenario
The **RMA Status Update** webhook is triggered in the following scenarios:

1. RMA is created
2. The RMA package is delivered and is pending the seller to review items to make a refund **decision.**
3. The RMA items review and refund decision is completed.


> **Note:** The RMA is automatically created once the Aftersales Request has been approved. The RMA decision is considered the second-review stage of the Aftersales journey. 


# 2. Data business parameters
| **Properties** | **Type** | **Example** | **Description** |
| --- | --- | --- | --- |
| shop_id | String | `7494049642642441621` | TikTok Shop identifier associated with the event. |
| timestamp | Int | `1732526400` | The time when this webhook was triggered, represented by Unix timestamp. |
| tts_notification_id | String | `7327112393057371910` | Unique notification identifier for deduplication and tracing. |
| type | Int | **`65`** | Numeric webhook event type. |
| data | Object |  |  |
| └ rma_id | String | `576486316948490002` | Unique identifier of the RMA. |
| └ aftersales_request_id | String | `576486316948490001` | Parent aftersales request identifier. |
| └ return_role | String | `BUYER` | Role that initiated the return flow. Possible enumerations: <br/>  <br/> * `BUYER` <br/> * `SELLER` |
| └ rma_status | String |  | Current RMA status. Possible enumerations: <br/>  <br/> * `INIT` = The RMA has been created <br/> * `AWAITING_BUYER_SHIPPED` = Awaiting buyer's action to ship the return package with carrier <br/> * `RETURN_IN_TRANSIT` = Buyer has shipped the return and is in transit to the sellers destination warehouse <br/> * `PENDING_PACKAGE_REVIEW` = The return package has been delivered and is pending seller package review. The seller has **2-4 business days** **SLA** to respond with a refund review/decision. Please refer to the latest seller academy document. <br/> * `PACKAGE_REVIEW_COMPLETED` = The package review lifecycle is complete, and the RMA refund has either been approved or rejected. |
| └ rma_request_create_time | Int | `1627587600` | Creation time of the RMA in Unix seconds. |
| └ rma_request_update_time | Int | `1644412885`  | Last update time of the RMA in Unix seconds. |


## Event example
```JSON
{
  "type": 65,
  "tts_notification_id": "1111111113",
  "shop_id": "1234567890",
  "timestamp": 1644412889,
  "data": {
    "rma_id": "576486316948490002",
    "aftersales_request_id": "576486316948490001",
    "return_role": "BUYER",
    "rma_status": "INIT",
    "rma_create_time": 1627587601,
    "rma_update_time": 1644412889
  }
}
```


