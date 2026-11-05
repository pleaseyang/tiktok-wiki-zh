# (56) 样品申请状态变更

## 触发场景
当达人的样品申请状态发生变更时，会触发此 webhook。
## 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `56` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| shop_id | string | `"7494049642642441621"` | TikTok Shop ID |
| timestamp | int | `1644412885` | 此 webhook 触发时的 UNIX 时间戳。 |
| data | object |  |  |
| └application_id | string | `"123456"` | 样品申请的 ID |
| └new_status | string | `"PENDING"` | 样品申请的状态。<br/>可能的枚举值如下：<br/>  <br/> * `PENDING`：样品申请正在等待卖家审核。<br/> * `AWAITING_SHIPMENT`：申请已批准，卖家需要寄送样品。<br/> * `SHIPPED`：样品已由卖家发出，等待达人收货。<br/> * `CONTENT_PENDING`：达人已收到样品包裹，预计需要创作内容。<br/> * `REJECT_CANCELLED`：样品申请已被卖家拒绝。<br/> * `OVERDUE_CANCELLED`：样品申请因逾期已过期。<br/> * `UNFULFILL_CANCELLED`：达人未在约定时间内履行创作内容的承诺。<br/> * `DEL_OPEN_COLLAB`：公开合作已被删除。<br/> * `SELLER_NOT_SHIP_CANCELLED`：卖家未在规定时间内寄送样品。<br/> * `WITHDRAW_CANCELLED`：达人在卖家批准前撤回了样品申请。<br/> * `UNFULFILLABLE_CANCELLED`：由于达人无法控制的原因，申请被取消，无法创作内容。<br/> * `OPS_CANCELLED`：运营人员手动取消了申请。<br/> * `OPS_FAILED`：运营人员将申请标记为失败。<br/> * `OPS_COMPLETED`：运营人员手动将申请标记为已完成。<br/> * `COMPLETED`：申请已完成，达人已发布内容。<br/>  <br/> 此字段允许跟踪样品申请在整个生命周期中的状态，为卖家和达人提供每个阶段的可见性。 |
| └creator | []object |  | 达人详细信息。包括达人的 TikTok 用户名和 TikTok 用户 ID 等详细信息。 |
| └└creator_open_id | string | `"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"` | 达人 Open ID。[更多详情](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
| └product | []object |  | 商品信息。 |
| └└id | string | `"1729859829942358814"` | 商品标识符。 |
| └└sku_id | string | `"1729859567502267166"` | 达人申请样品的商品 SKU 唯一 ID。 |
## 事件示例
```JSON
{
  "type": 56,
  "shop_id": "7494049642642441621",
  "tts_notification_id": "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "application_id": "123456",
    "new_status": "PENDING",
    "creator": {
      "creator_open_id": "uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"
    },
    "product": {
      "id": "1729859829942358814",
      "sku_id": "1729859567502267166"
    }
  }
}
```


