# (11) 取消状态变更

# 1. 触发场景
当订单的 `cancel_status` 发生变更时，会触发此**取消状态变更** webhook：

* 发起订单取消：`CANCELLATION_REQUEST_PENDING`
* 订单取消被 `SELLER` 或 `SYSTEM` 接受：`CANCELLATION_REQUEST_SUCCESS`
* 订单取消被 `BUYER` 或 `SYSTEM` 关闭：`CANCELLATION_REQUEST_CANCELLED`
* 订单取消成功并已退款：`CANCELLATION_REQUEST_COMPLETE`

# 2. 数据业务参数
| **参数名称** | **示例** | **描述** |
| --- | --- | --- |
| order_id | 577087614418520388 | TikTok Shop 订单的标识符 |
| cancellations_role | BUYER | 发起取消的用户角色，可能的值：<br/>  <br/> * BUYER<br/> * SELLER<br/> * SYSTEM |
| cancel_status | CANCELLATION_REQUEST_PENDING | 订单取消状态，可能的值：<br/>  <br/> * CANCELLATION_REQUEST_PENDING<br/> * CANCELLATION_REQUEST_SUCCESS<br/> * CANCELLATION_REQUEST_CANCELLED<br/> * CANCELLATION_REQUEST_COMPLETE |
| cancel_id | 4035318504086604100 | 特定订单取消的标识符 |
| create_time | 1627587600 | 买家发起取消请求的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```JSON
{
  "type": 11,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "order_id": "576486316948490001",
    "cancellations_role": "BUYER",
    "cancel_status": "CANCELLATION_REQUEST_PENDING",
    "cancel_id": "4035318504086604100",
    "create_time": 1627587600
  }
}
```


