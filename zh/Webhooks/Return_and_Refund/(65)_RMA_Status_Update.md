# (65) RMA 状态更新

使用此 webhook 追踪售后请求中已批准商品生成的 RMA 对象的包裹级生命周期。
# 1. 触发场景
**RMA 状态更新** webhook 在以下场景触发：

1. RMA 已创建
2. RMA 包裹已送达，等待卖家审核商品以做出退款**决定。**
3. RMA 商品审核和退款决定已完成。


> **注意：** 一旦售后请求被批准，RMA 将自动创建。RMA 决定被视为售后流程的复审阶段。


# 2. 数据业务参数
| **字段** | **类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| shop_id | String | `7494049642642441621` | 与事件关联的 TikTok Shop 标识符。 |
| timestamp | Int | `1732526400` | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| tts_notification_id | String | `7327112393057371910` | 唯一的通知标识符，用于去重和追踪。 |
| type | Int | **`65`** | webhook 事件类型的数字标识。 |
| data | Object |  |  |
| └ rma_id | String | `576486316948490002` | RMA 的唯一标识符。 |
| └ aftersales_request_id | String | `576486316948490001` | 父级售后请求标识符。 |
| └ return_role | String | `BUYER` | 发起退货流程的角色。可能的枚举值：<br/>  <br/> * `BUYER`<br/> * `SELLER` |
| └ rma_status | String |  | 当前 RMA 状态。可能的枚举值：<br/>  <br/> * `INIT` = RMA 已创建<br/> * `AWAITING_BUYER_SHIPPED` = 等待买家通过物流承运商寄出退货包裹<br/> * `RETURN_IN_TRANSIT` = 买家已寄出退货，包裹正在运输至卖家目的地仓库途中<br/> * `PENDING_PACKAGE_REVIEW` = 退货包裹已送达，等待卖家进行包裹审核。卖家有 **2-4 个工作日**的 **SLA** 来响应退款审核/决定。请参阅最新的卖家学院文档。<br/> * `PACKAGE_REVIEW_COMPLETED` = 包裹审核生命周期已完成，RMA 退款已被批准或拒绝。 |
| └ rma_request_create_time | Int | `1627587600` | RMA 的创建时间，以 Unix 秒表示。 |
| └ rma_request_update_time | Int | `1644412885`  | RMA 的最后更新时间，以 Unix 秒表示。 |


## 事件示例
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


