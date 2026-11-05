# (12) 退货状态变更

# 1. 触发场景
当订单的 `return_status` 发生变更时，会触发此**退货状态变更** webhook：

* `BUYER` 发起退货或退款请求，等待 `SELLER` 审核：`RETURN_OR_REFUND_REQUEST_PENDING`
* `SELLER` 拒绝 `BUYER` 的退货或退款请求：`REFUND_OR_RETURN_REQUEST_REJECT`
* 退货请求已批准，`SELLER` 等待 `BUYER` 退回已批准的商品：`AWAITING_BUYER_SHIP`。如果 `BUYER` 未在截止日期前将商品寄回给 `SELLER`，请求将自动关闭。
* `BUYER` 成功投递退货包裹或 `BUYER` 寄出包裹并上传物流追踪号：`BUYER_SHIPPED_ITEM`
* `SELLER` 拒绝退货的退款请求：`REJECT_RECEIVE_PACKAGE`
* `SELLER` 接受退款请求或为退货发起退款：`RETURN_OR_REFUND_REQUEST_SUCCESS`
* `BUYER` 或 `SYSTEM` 关闭退货或退款请求：`RETURN_OR_REFUND__REQUEST_CANCELLED`
* 退货或退款成功：`RETURN_OR_REFUND_REQUEST_COMPLETE`

此外，`BUYER` 可以申请换货（相同的替换商品）而非退款：

* `BUYER` 发起换货请求，等待 `SELLER` 审核：`REPLACEMENT_REQUEST_PENDING`
* `SELLER` 拒绝 `BUYER` 的换货请求：`REPLACEMENT_REQUEST_REJECT`
* `SELLER` 决定直接退款而不换货：`REPLACEMENT_REQUEST_REFUND_SUCCESS`
* `BUYER` 取消换货请求：`REPLACEMENT_REQUEST_CANCEL`
* `SELLER` 批准换货请求：`REPLACEMENT_REQUEST_COMPLETE`

# 2. 数据业务参数
| **参数** | **描述** | **示例** |
| --- | --- | --- |
| order_id | TikTok Shop 订单的标识符 | 577087614418520388 |
| return_role | 退货或退款请求的用户角色，可能的值：<br/>  <br/> * BUYER<br/> * SELLER<br/> * SYSTEM | BUYER |
| return_type | 退货或退款请求类型，可能的值：<br/>  <br/> * REFUND<br/> * REPLACEMENT<br/> * RETURN_AND_REFUND | REFUND |
| return_status | 请求的退货状态，可能的值：<br/>  <br/> * AWAITING_BUYER_SHIP<br/> * BUYER_SHIPPED_ITEM<br/> * REFUND_OR_RETURN_REQUEST_REJECT<br/> * REJECT_RECEIVE_PACKAGE<br/> * REPLACEMENT_REQUEST_CANCEL<br/> * REPLACEMENT_REQUEST_COMPLETE<br/> * REPLACEMENT_REQUEST_PENDING<br/> * REPLACEMENT_REQUEST_REFUND_SUCCESS<br/> * REPLACEMENT_REQUEST_REJECT<br/> * RETURN_OR_REFUND_REQUEST_CANCEL<br/> * RETURN_OR_REFUND_REQUEST_COMPLETE<br/> * RETURN_OR_REFUND_REQUEST_PENDING<br/> * RETURN_OR_REFUND_REQUEST_SUCCESS | RETURN_OR_REFUND_REQUEST_PENDING |
| return_id | 特定退货的标识符 | 4035318504086604100 |
| create_time | 请求创建的时间。 | 1627587600 |
| update_time | 退货订单状态更新的时间，以 Unix 时间戳（秒）表示。 | 1627587600 |
## 事件示例
```JSON
{
  "type": 12,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "order_id": "576486316948490001",
    "return_role": "BUYER",
    "return_type": "REFUND",
    "return_status": "RETURN_OR_REFUND_REQUEST_PENDING",
    "return_id": "576486316948490001",
    "create_time": 1627587600
    "update_time": 1644412885
  }
}
```


