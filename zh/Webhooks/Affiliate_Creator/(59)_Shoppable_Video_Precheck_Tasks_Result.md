# (59) 可购物视频预审任务结果

## 触发场景
当调用视频内容预审 API 后，会触发此 webhook，提供视频质量评估和违规检查的结果。
## 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `59` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057389710"` | 通知的 ID。 |
| creator_open_id | string | `"VIyStQAAAADCBQ40s4TzODDSEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 达人的 open_id。获取方式请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的 UNIX 时间戳。 |
| data | object |  |  |
| └task_id | string | `"7493990579714178574"` | TikTok Shop 生成的预审任务 ID。 |
| └violation_check_result | object |  |  |
| └└status | string | `SUCCESS` | 可能的枚举值：<br/> `SUCCESS`<br/> `FAIL`<br/> `PROCESSING` |
| └└issues | []object |  |  |
| └└└risk | string | `"HIGH"` | 风险类型。 |
| └└└suggestions | string | `"Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."` | 修复风险的建议。 |
| └good_quality_check_result | object |  |  |
| └└status | string | `FAIL` | 可能的枚举值：<br/> `SUCCESS`<br/> `FAIL`<br/> `PROCESSING` |
| └└issues | []object |  |  |
| └└└code | string | `"LOW RESOLUTION"` | 质量检查代码。 |
| └└└suggestions | string | `"Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."` | 提升视频质量的建议。 |
## 事件示例
```JSON
{
  "type": 59,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id": "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "task_id": "task_202402011200001234",
    "violation_check_result": {
      "status": "FAIL",
      "issues": [
        {
          "risk": "HIGH",
          "suggestions": "Remove prohibited visual elements and resubmit the video."
        }
      ]
    },
    "good_quality_check_result": {
      "status": "SUCCESS",
      "issues": [
        {
          "code": "LOW_RESOLUTION",
          "suggestions": "Consider uploading a higher-resolution video for better viewing experience."
        }
      ]
    }
  }
}
```


