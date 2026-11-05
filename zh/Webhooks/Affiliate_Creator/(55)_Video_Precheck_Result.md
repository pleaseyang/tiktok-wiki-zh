# (55) 视频预审结果

## 触发场景
当调用视频内容预审 API 后，会触发此 webhook，返回视频是否存在违规或通过审核的结果。
## 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `55` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| creator_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 达人的 open_id。获取方式请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的 UNIX 时间戳。 |
| data | object |  |  |
| └precheck_task_id | string | `"7493990579714164574"` | TikTok Shop 生成的预审任务 ID。 |
| └result | string | `"FAIL"` | 可能的枚举值：<br/> `PASS`<br/> `FAIL` |
| └issues | []object |  | 仅当 `result` 为 `FAIL` 时返回 |
| └└risk | string | `"Pirated Content"` | 风险类型。 |
| └└suggestion | string | `"Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."` | 修复风险的建议。 |
## 事件示例
```JSON
{
  "type": 55,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id": "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "precheck_task_id": "7493990579714164574",
    "result": "FAIL",
    "issues": [
      {
        "risk": "Pirated Content",
        "suggestion": "Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."
      }
    ]
  }
}
```


