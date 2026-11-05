# (33) 新消息监听

## 触发场景
当达人向卖家发送消息时。
## 数据业务参数
| 参数名称 | 数据类型 | 示例 | 描述 |
| --- | --- | --- | --- |
| type | int64 | `33` | Webhook 类型，此 webhook 固定为 `33`。 |
| shop_id | string | `"7494049642642441621"` | TikTok Shop ID。 |
| tts_notification_id | string | `"7327112393057371910"` | webhook 的 ID。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的 UNIX 时间戳。 |
| data | object |  |  |
| └index | string | `"1735032460678899"` | 消息在会话中的索引。索引值越大，消息越新。 |
| └message_id | string | `"7451907556216407553"` | 消息 ID。 |
| └conversation_id | string | `"7451873679308620048"` | 消息所属会话的 ID。 |
| └msg_type | string | `"TEXT"` | 消息类型，可能的值：<br/>  <br/> * TEXT<br/> * PRODUCT_CARD<br/> * TARGET_COLLABORATION_CARD<br/> * FREE_SAMPLE_CARD |
| └content | string | `"Hello"` | 消息内容，以 JSON 序列化字符串表示。<br/>  <br/> * TEXT：{"content": "simple text"}<br/> * PRODUCT_CARD：{"product_id": "12345"}<br/> * TARGET_INVITATION_CARD：{"invitation_group_id": "1234"}<br/> * FREE_SAMPLE_CARD：{"apply_id": "1234"} |
| └create_time | string | `1691411573` | 消息创建时间，以 Unix 时间戳（秒）表示。 |
| └sender | object |  |  |
| └└sender_im_user_id | string | `"2368694990397660924"` | 发送者在 IM 系统中的 ID。 |
## 事件示例
```JSON
{
  "type": 33,
  "shop_id": "7494049642642441621",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "index": "1735032460678899",
    "message_id": "7451907556216407553",
    "conversation_id": "7451873679308620048",
    "msg_type": "TEXT",
    "content": "Hello",
    "create_time": "1691411573",
    "sender": {
      "sender_im_user_id": "2368694990397660924"
    }
  }
}
```


