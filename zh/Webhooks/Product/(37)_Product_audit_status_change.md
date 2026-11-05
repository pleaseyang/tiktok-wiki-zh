# (37) 商品审核状态变更

## 触发场景
当商品审核状态发生变更时，您会收到此 webhook。
通过此 webhook，您可以轻松获取商品的审核状态信息，而无需调用 [Get Product](get-product) API。
要接收此 webhook，您必须确保在合作伙伴中心已启用 `Product Basic` API 权限范围。
## 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `37` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| shop_id | string | `"7494049642642441621"` | 店铺的 ID。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| data | object |  |  |
| └ product_id | int | `789078671231` | 商品的 ID。 |
| └ audit | object |  | 商品审核信息。 |
| └└ status | string | `PRE_APPROVED` | 商品审核状态。<br/>可能的值：<br/>  <br/> * NONE：商品不适用审核，因为尚未提交在此平台上架，或处于草稿、冻结或停用状态。<br/> * AUDITING：商品正在审核中。<br/> * FAILED：商品审核未通过，或审核已被取消。<br/> * PRE_APPROVED：商品已通过审核但尚未上架，因为存在待满足的前提条件。请参考 `pre_approved_reasons` 了解前提条件。<br/> * APPROVED：商品已通过审核并已上架。 |
| └└ pre_approved_reasons | []string | ["KYC_PENDING"] | 商品审核状态为 `PRE_APPROVED` 的原因。<br/>可能的值：<br/>  <br/> * KYC_PENDING：卖家的入驻（KYC - 了解您的客户信息）不完整或正在等待处理。<br/> * RESTRICTED_CATEGORY_PENDING：仅适用于美国市场。商品属于受限类目，类目审批仍在进行中。如需申请访问权限，请通过 TikTok Shop 卖家中心的资质中心提交申请。 |
| └ integrated_platform_statuses | object |  | 商品在与 TikTok Shop 原生集成的平台（如 TOKOPEDIA）上的当前审核状态。 |
| └└ platform | string | `TOKOPEDIA` | 集成平台名称。<br/>可能的值：<br/>  <br/> * TOKOPEDIA。 |
| └└ status | string | `AUDITING` | 商品审核状态。<br/>可能的值：<br/>  <br/> * NONE：商品不适用审核，因为尚未提交在此平台上架，或处于草稿、冻结或停用状态。<br/> * AUDITING：商品正在审核中。<br/> * FAILED：商品审核未通过，或审核已被取消。<br/> * APPROVED：商品已通过审核并已上架。 |
| └ update_time | int | `1644412885` | 状态变更的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```JSON
{
  "type": 37,
  "shop_id": "7494049642642441621",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "product_id": 789078671231,
    "audit": {
        "status": "PRE_APPROVED",
        "pre_approved_reason": "KYC_PENDING"
    },
    "integrated_platform_statuses": {
        "platform": "TOKOPEDIA",
        "status": "AUDITING"
    },
    "update_time": 1644412885
  }
}
```


