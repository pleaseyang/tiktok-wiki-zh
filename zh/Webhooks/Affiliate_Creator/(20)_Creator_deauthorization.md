# (20) 达人取消授权

## 触发场景
当达人完全移除 App 对其数据的访问权限时。
## 数据业务参数
| 参数名称 | 数据类型 | 示例 | 描述 |
| --- | --- | --- | --- |
| type | int | `20` | Webhook 类型，此 webhook 固定为 `20`。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| creator_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 达人的 open_id。获取方式请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的 UNIX 时间戳。 |
| data | object |  |  |
| └ cancel_time | string | `"1644412885"` | 此事件发生时的 UNIX 时间戳。 |
## 事件示例
```JSON
{
  "type": 20,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "cancel_time": 1644412885
  }
}
```


