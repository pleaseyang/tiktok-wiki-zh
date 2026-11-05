# (19) 尺码表变更

# 1. 触发场景
当商品尺码表被创建、编辑或删除时，会触发此 webhook。
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
# 2. 数据业务参数
| **参数名称** <!-- width:240px --> | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `19` | 此 webhook 主题的 ID，固定为 19。 |
| tts_notification_id | string | `"7327112393057371910"` | 此 webhook 通知的 ID。 |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 卖家的 open_id。更多信息请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ size_chart_template_id | string | `"789078671231"` | 发生变更的尺码表模板 ID。 |
| └ size_chart_template_name | string | `"600001"` | 发生变更的尺码表模板名称。 |
| └ event_type | string | `"EDIT"` | 尺码表发生的变更类型。可能的值：<br/> - `CREATE`：创建了新的尺码表<br/> - `EDIT`：编辑了尺码表<br/> - `DELETE`：删除了尺码表 |
| └ update_time | int | `1644412845` | 变更发生的时间。Unix 时间戳。 |
## 事件示例
```JSON
{
  "type": 19,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "size_chart_template_id": "789078671231",
    "size_chart_template_name": "600001",
    "event_type": "EDIT",
    "update_time": 1644412845
  }
}
```


