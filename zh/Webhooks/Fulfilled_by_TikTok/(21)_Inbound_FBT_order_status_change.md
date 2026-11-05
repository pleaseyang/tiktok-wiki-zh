# (21) 入库 FBT 订单状态变更

## 触发场景
当 FBT 入库订单状态发生变更时，会触发此 webhook。
> 前提条件：在合作伙伴中心已启用 **Fulfilled by TikTok(FBT) Info** API 权限范围。更多信息请参见[访问权限范围](access-scope)。

## 数据业务参数
| **参数名称** <!-- width:240px --> | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `21` | 此 webhook 主题的 ID，固定为 21。 |
| tts_notification_id | string | `"7327112393057371910"` | 此 webhook 通知的 ID。 |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 卖家的 open_id。更多信息请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ inbound_order_id | string | `"IBR577087614418520388"` | FBT 入库订单 ID。 |
| └ order_status | string | `"CANCELLED"` | 入库订单状态。可能的枚举值：<br/>- TO_BE_RECEIVED<br/>- ARRIVE_HUB<br/>- RECEIVING<br/>- PARTIALLY_RECEIVED<br/>- RECEIVED<br/>- CANCELLED |
| └ update_time | int | `1644412845` | 变更发生的时间。Unix 时间戳。 |
## 事件示例
```JSON
{
  "type": 21,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "inbound_order_id": "IBR577087614418520388",
    "order_status": "CANCELLED",
    "update_time": 1644412845
  }
}
```


