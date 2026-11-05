# (66) Appeal Completed Webhook


### **Webhook Name:** Appeal Completed Webhook
**Trigger Scenario:** This webhook is triggered when a size chart verification appeal is approved or rejected.
**Scenario:** SHOP
**Category:** Products
## Params
| Properties |  |  |  | Type | Must Return |
| --- | --- | --- | --- | --- | --- |
| shop_id |  |  |  | string | true |
| type |  |  |  | int64 | true |
| tts_notification_id |  |  |  | string | true |
| timestamp |  |  |  | int64 | true |
| data |  |  |  | object | true |
| └ | appeal_task |  |  | object | true |
| └ | └ | size_chart_id |  | int64 | false |
| └ | └ | size_chart_image_uri |  | string | false |
| └ | └ | appeal_audit_result |  | []object | true |
| └ | └ | └ | indicator_type | string | true |
| └ | └ | └ | status | string | true |
| └ | └ | └ | reject_reason | string | false |
| └ | product_id |  |  | int64 | true |
