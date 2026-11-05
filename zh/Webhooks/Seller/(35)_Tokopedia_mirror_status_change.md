# (35) Tokopedia 镜像状态变更

# 1. 触发场景
当 TikTok Shop 到 Tokopedia 的镜像流程完成或回滚时，会触发此 webhook。仅适用于**印度尼西亚**市场。

**前提条件**：店铺处于[活跃](get-active-shops)状态，且在合作伙伴中心已启用 "**Shop Authorized Information**" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 35 | 此 webhook 主题的 ID，固定为 35。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| seller_open_id | string | "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw" | 卖家的 open_id。更多信息请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ tts_shop_id | string | "7494049642642441621" | TikTok Shop 中的店铺 ID。 |
| └ update_time | int | 1627587600 | 变更发生的时间。Unix 时间戳。 |
| └ mirror_status | string | "MIRRORED" | 店铺镜像状态：<br/> - MIRRORED<br/> - ROLLED_BACK<br/> - CANCELED |
## 事件示例
```JSON
{
  "type": 35,
  "tts_notification_id" : "7327112393057371910",
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "timestamp": 1644412885,
  "data": {
    "tts_shop_id": "7494049642642441621",
    "mirror_status" : "MIRRORED",
    "update_time": 1627587600
  }
}
```


