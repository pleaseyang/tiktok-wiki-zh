# (5) 商品状态变更

# 1. 触发场景
当商品审核状态发生变更或完成时，会触发此**商品状态变更** webhook：

* 商品通过初审：`PRODUCT_FIRST_PASS_REVIEW`
* 商品状态由平台变更：`PRODUCT_STATUS_CHANGED`
* 商品审核未通过：`PRODUCT_AUDIT_FAILURE`

# 2. 数据业务参数
| **参数名称** | **示例** | **描述** |
| --- | --- | --- |
| product_id | 1X2X3X4X5 | TikTok Shop 商品的标识符 |
| status | 直播销售 | 商品审核状态，可能的值：<br/>  <br/> * PRODUCT_FIRST_PASS_REVIEW<br/> * PRODUCT_STATUS_CHANGED<br/> * PRODUCT_AUDIT_FAILURE |
| suspended_reason | 1X2X3X4X5 | 商品审核被拒绝或冻结的原因 |
| update_time | 1627587600 | 状态变更的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```JSON
{
  "type": 5,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": 576486316948490000,
    "status": "PRODUCT_FIRST_PASS_REVIEW",
    "suspended_reason": "",
    "update_time": 1644412885
  }
}
```


