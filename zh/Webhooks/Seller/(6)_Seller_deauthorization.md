# (6) 卖家取消授权

# 1. 触发场景
当卖家被取消授权后，会触发此**卖家取消授权** webhook。这很重要，可以防止开发者误以为是平台授权功能出了问题。
# 2. 数据业务参数
| **参数名称** | **示例** | **描述** |
| --- | --- | --- |
| type | 6 | 每种通知类型的标识符 |
| shop_id | 123455 | 店铺的标识符 |
| timestamp | 1627587506 | 通知推送的时间，以 Unix 时间戳（秒）表示。 |
| data | "data": {"message": "Shop_id {xxx} is deauthorized from your APP by merchant."} | 包含与特定通知类型相关的业务参数的对象 |
## 事件示例
```JSON
{
  "type": 6,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "message": "Shop_id {xxx} is deauthorized from your APP by merchant."
  }
}
```


