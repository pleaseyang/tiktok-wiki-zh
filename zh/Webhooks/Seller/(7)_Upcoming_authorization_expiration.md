# (7) 授权即将过期

# 1. 触发场景
在授权自动过期前 30 天，会触发此**授权即将过期** webhook。此 webhook 将持续每天 0:00 通知卖家，直到重新授权完成。
# 2. 数据业务参数
| **参数名称** | **示例** | **描述** |
| --- | --- | --- |
| type | 7 | 每种通知类型的标识符 |
| shop_id | 123455 | 店铺的标识符 |
| timestamp | 1627587506 | 通知推送的时间，以 Unix 时间戳（秒）表示。 |
| data | "data": {"message": "Authorization of shop_id {xxx} is expiring in {} days. Please direct the merchant to re-authorize.", "expiration_time": "1627587506"} | 包含与特定通知类型相关的业务参数的对象。 |
## 事件示例
```JSON
{
  "type": 7,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "message": "Authorization of shop_id {xxx} is expiring in {x} days. Please direct the merchant to re-authorize.",
    "expiration_time": "1627587506"
  }
}
```


