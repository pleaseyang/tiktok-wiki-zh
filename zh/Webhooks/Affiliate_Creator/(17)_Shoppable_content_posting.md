# (17) 可购物内容发布

## 触发场景
当达人在视频或直播中添加、更新或移除商品链接时，会触发此 webhook。
> 此 webhook 仅在达人已授权 `Read Creator Affiliate Collaborations` 权限范围后才会触发。

## 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `17` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| creator_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 达人的 open_id。获取方式请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的 UNIX 时间戳。 |
| data | object |  |  |
| └product_id | string | `"789078671231"` | 达人视频中推广的商品 ID。 |
| └event | object |  |  |
| └└type | string | `"ADD"` | 达人对视频或直播中推广商品执行的操作。可能的枚举值如下：<br/>  <br/> * `ADD`：添加商品。<br/> * `UPDATE`：更新商品。<br/> * `REMOVE`：移除商品。 |
| └└scene | string | `"VIDEO"` | 达人推广商品的场景。可能的枚举值如下：<br/>  <br/> * `VIDEO`：短视频。 |
| └└content_id | string | `"789078671231"` | 短视频的 ID。 |
## 事件示例
```JSON
{
  "type": 17,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "product_id": "789078671231",
    "event": {
      "type": "ADD",
      "scene": "VIDEO",
      "content_id": "789078671231"
    }
  }
}
```


