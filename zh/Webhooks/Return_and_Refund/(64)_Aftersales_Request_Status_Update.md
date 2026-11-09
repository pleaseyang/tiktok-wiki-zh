# (64) 售后请求状态更新

# 1. 触发场景
**售后请求状态更新** webhook 在以下两种场景下触发：

1. 买家在其 TikTok 用户应用中提交退货请求。
2. 卖家对请求做出批准或拒绝的决定。


> **注意：** 这被视为退货流程的**初审**阶段。如果售后请求被批准，将进入**复审**阶段，即等待卖家对退回商品做出批准或拒绝的决定。


# 2. 数据业务参数
| **字段** | **类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| shop_id | String | `7494049642642441621` | 与事件关联的 TikTok Shop 标识符。 |
| timestamp | Int | `1732526400` | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| tts_notification_id | String | `7327112393057371910` | 唯一的通知标识符，用于去重和追踪。 |
| type | Int | **`64`** | webhook 事件类型的数字标识。 |
| data | Object |  |  |
| └ aftersales_request_id | String | `576486316948490001` | 售后请求的唯一标识符。 |
| └ return_role | String | `BUYER` | 发起退货流程的角色。可能的枚举值：<br/>  <br/> * `BUYER`<br/> * `SELLER` |
| └ aftersales_request_status | String | `PENDING_REQUEST_REVIEW` | 当前售后请求状态。可能的枚举值：<br/>  <br/> * `PENDING_REQUEST_REVIEW`<br/> * `REQUEST_REVIEW_COMPLETED` |
| └ aftersales_request_create_time | Int | `1627587600` | 售后请求的创建时间，以 Unix 秒表示。 |
| └ aftersales_request_update_time | Int | `1644412885`  | 售后请求的最后更新时间，以 Unix 秒表示。 |


## 事件示例
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


