# (1) 订单状态变更

# 1. 触发场景
当订单的 `order_status` 发生变更时，会触发此**订单状态变更** webhook。
# 2. 数据业务参数
| **参数名称** | **示例** | **描述** |
| --- | --- | --- |
| order_id | 576462377512830168 | TikTok Shop 订单的标识符 |
| order_status | CANCEL | 最新的订单状态，可能的值：<br/>  <br/> * `UNPAID`<br/> * `ON_HOLD`<br/> * `AWAITING_SHIPMENT`<br/> * `AWAITING_COLLECTION`<br/> * `CANCEL`<br/> * `IN_TRANSIT`<br/> * `DELIVERED`<br/> * `COMPLETED` |
| is_on_hold_order | false | 表示订单是否经历或将会经历 `ON_HOLD` 状态 |
| update_time | 1627587505 | 订单状态更新的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```json
{
    "type":1,
    "tts_notification_id": "7327112393057371910",
    "shop_id":"7494049642642441621",
    "timestamp":1644412885,
    "data":{
        "order_id":"576486316948490001",
        "order_status":"UNPAID",
        "is_on_hold_order": false,
        "update_time":1644412885
    }
}
```


