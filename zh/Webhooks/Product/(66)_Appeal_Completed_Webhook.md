# (66) 申诉完成 Webhook


### **Webhook 名称：** 申诉完成 Webhook
**触发场景：** 当尺码表验证申诉被批准或拒绝时，会触发此 webhook。
**场景：** SHOP
**分类：** 商品
## 参数
| 属性 |  |  |  | 类型 | 必返回 |
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
