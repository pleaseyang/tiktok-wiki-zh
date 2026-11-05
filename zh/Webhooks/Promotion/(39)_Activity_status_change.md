# (39) 活动状态变更

## 触发场景
当指定类型的促销活动开始、过期或被停用时，您会收到此 webhook。
仅当满足以下所有条件时，才会触发此 webhook：

* 您的 App 已被授予 `Promotion Information` 权限范围。
* 活动类型为以下类型之一：
   * `FIXED_PRICE`
   * `DIRECT_DISCOUNT`
   * `SHIPPING_DISCOUNT`
   * `BUY_MORE_SAVE_MORE`
   * `FLASHSALE`（仅适用于东南亚市场：SG、TH、ID、MY、PH、VN）
* 发生以下状态变更之一：
   * 活动开始：状态从 `NOT_START` 变为 `ONGOING`。
   * 活动过期：状态从 `ONGOING` 变为 `EXPIRED`。
   * 活动被停用：状态变为 `DEACTIVATED`。

## 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `39` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| shop_id | string | `"7494049642642441621"` | 店铺的 ID。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| data | object |  |  |
| └ activity_id | string | `"7136104329798256386"` | 促销活动的 ID。 |
| └ update_time | int | `1644412885` | 状态变更的时间，以 Unix 时间戳（秒）表示。 |
| └ activity_type | string | `"FIXED_PRICE"` | 促销活动的类型。可能的值为：<br/>  <br/> * `FIXED_PRICE`<br/> * `DIRECT_DISCOUNT`<br/> * `SHIPPING_DISCOUNT`<br/> * `BUY_MORE_SAVE_MORE`<br/> * `FLASHSALE`（仅适用于东南亚市场：SG、TH、ID、MY、PH、VN） |
| └ product_level | string | `"PRODUCT"` | 活动商品维度，值为：<br/>  <br/> * `PRODUCT`<br/> * `VARIATION`<br/> * `SHOP` |
| └ status | string | `ONGOING` | 促销活动的当前状态。可能的值为：<br/>  <br/> * `ONGOING`<br/> * `EXPIRED`<br/> * `DEACTIVATED` |
## 事件示例
```JSON
{
  "type": 39,
  "shop_id": "7494049642642441621",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "activity_id": "7136104329798256386",
    "update_time": 1644412885,
    "activity_type": "FIXED_PRICE",
    "product_level": "PRODUCT",
    "status": "ONGOING"
  }
}
```


