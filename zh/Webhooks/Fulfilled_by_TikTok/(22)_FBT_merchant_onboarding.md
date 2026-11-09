# (22) FBT 卖家入驻

## 触发场景
当 TikTok Shop 卖家入驻 FBT 平台并启用 FBT 服务时，会触发此 webhook。
> 前提条件：在合作伙伴中心已启用 **Fulfilled by TikTok(FBT) Info** API 权限范围。更多信息请参见[访问权限范围](access-scope)。

## 数据业务参数
| **参数名称** <!-- width:240px --> | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `22` | 此 webhook 主题的 ID，固定为 22。 |
| tts_notification_id | string | `"7327112393057371910"` | 此 webhook 通知的 ID。 |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 卖家的 open_id。更多信息请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | FBT 入驻状态更新时的 UNIX 时间戳。 |
| data | object |  |  |
| └ onboarded_regions | []object |  | 所有已入驻的 FBT 区域。 |
| └└ region_code | string | `"GB"` | 已入驻的 FBT 区域代码。 |
| └ update_time | int | `1644412845` | 最新更新时间。Unix 时间戳。 |
## 事件示例
```JSON
{
  "type": 22,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "onboarded_regions": [
      {
        "region_code": "GB"
      }
    ],
    "update_time": 1644412845
  }
}
```


