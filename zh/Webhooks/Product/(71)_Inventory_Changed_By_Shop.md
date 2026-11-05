# (71) 店铺库存变更

## 1. 触发场景
当店铺中 SKU 的库存数量发生变更时，会触发此 webhook。每条通知标识受影响的店铺、商品和 SKU，并包含变更后的库存快照以及各项变更明细。
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)。
以下事件在导致库存数量变更时会触发此 webhook：
| 触发来源 | 描述 |
| --- | --- |
| `order_created` | 订单成功创建，库存被占用。 |
| `order_canceled` | 买家或卖家取消订单，已占用的库存释放回可用库存。 |
| `order_shipped` | 订单已发货，已占用的库存被扣减。 |
| `manual_adjustment` | 卖家在卖家中心手动调整库存。 |
| `api_sync` | 开发者通过库存相关的 OpenAPI 更新库存。 |
| `campaign_lock` | 卖家参加平台营销活动，库存被锁定。 |
| `campaign_unlock` | 营销活动结束或卖家退出，锁定的库存被释放。 |
| `creator_lock` | 卖家为达人合作分配专属库存。 |
| `creator_unlock` | 达人合作结束，锁定的库存被释放。 |
| `system_auto_replenish` | 系统自动补充库存，例如订单因异常失败后。 |
## 2. 数据业务参数
以下列出的所有字段在通知 payload 中均为必填。示例 ID 和数量仅供参考。
| 参数名称 | 数据类型 | 示例 | 描述 |
| --- | --- | --- | --- |
| `type` | int64 | `71` | webhook 主题 ID。 |
| `tts_notification_id` | string | `"7327112393057371910"` | 通知 ID。 |
| `shop_id` | string | `"7494049642642441621"` | 店铺 ID。 |
| `timestamp` | int64 | `1775122114` | webhook 触发时的时间，以 Unix 时间戳表示。 |
| `data` | object | — | 库存变更事件数据。 |
| └ `event_id` | string | `"inventory_event_001"` | 库存事件的标识符；可用于事件去重。 |
| └ `occurred_at` | string | `"2026-04-02T09:28:34Z"` | 事件时间（UTC），格式为 ISO 8601。 |
| └ `shop_id` | int64 | `7494049642642441621` | 库存发生变更的店铺 ID。 |
| └ `product_id` | int64 | `1891234567890123456` | 受影响的商品 ID。 |
| └ `sku_id` | int64 | `1729507467923261408` | 受影响的 SKU ID。 |
| └ `quantity_snapshot_after_change` | object | — | 变更后的 SKU 库存数量。 |
| └ └ `total_quantity` | int64 | `100` | 总库存：`total_available_quantity + total_committed_quantity`。 |
| └ └ `total_available_quantity` | int64 | `80` | 可用库存，包括为营销活动和达人合作预留的库存数量。 |
| └ └ `total_committed_quantity` | int64 | `20` | 已占用但未发货的订单库存。 |
| └ └ `in_shop_quantity` | int64 | `65` | 店铺可用库存：`total_available_quantity - campaign_locked_quantity - creator_locked_quantity`。 |
| └ └ `campaign_locked_quantity` | int64 | `10` | 为营销活动预留的库存。 |
| └ └ `creator_locked_quantity` | int64 | `5` | 为达人合作预留的库存。 |
| └ `change_detail` | []object | — | 与该事件关联的各项库存变更明细。 |
| └ └ `idempotency_key` | string | `"inventory_change_001"` | 单项变更的标识符；可用于变更明细去重。 |
| └ └ `trigger_source` | string | `"manual_adjustment"` | 变更的原因。参见第 1 节中的触发来源。 |
| └ └ `occurred_at` | string | `"2026-04-02T09:28:34Z"` | 单项变更的 UTC 时间。 |
| └ └ `total_quantity_delta` | int64 | `4` | `total_quantity` 的变更量。 |
| └ └ `available_quantity_delta` | int64 | `4` | `total_available_quantity` 的变更量。 |
| └ └ `committed_quantity_delta` | int64 | `0` | `total_committed_quantity` 的变更量。 |
| └ └ `in_shop_quantity_delta` | int64 | `4` | `in_shop_quantity` 的变更量。 |
| └ └ `campaign_locked_quantity_delta` | int64 | `0` | `campaign_locked_quantity` 的变更量。 |
| └ └ `creator_locked_quantity_delta` | int64 | `0` | `creator_locked_quantity` 的变更量。 |

对于 delta 字段，正值表示增加，负值表示减少，零表示无变化。
### 事件示例
以下示例展示了卖家通过卖家中心为一个 SKU 增加了 4 件库存。总库存从 96 增加到 100，总可用库存从 76 增加到 80，店铺库存从 61 增加到 65。已占用库存以及营销活动和达人预留库存保持不变。
```JSON
{
  "type": 71,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1775122114,
  "data": {
    "event_id": "inventory_event_001",
    "occurred_at": "2026-04-02T09:28:34Z",
    "shop_id": 7494049642642441621,
    "product_id": 1891234567890123456,
    "sku_id": 1729507467923261408,
    "quantity_snapshot_after_change": {
      "total_quantity": 100,
      "total_available_quantity": 80,
      "total_committed_quantity": 20,
      "in_shop_quantity": 65,
      "campaign_locked_quantity": 10,
      "creator_locked_quantity": 5
    },
    "change_detail": [
      {
        "idempotency_key": "inventory_change_001",
        "trigger_source": "manual_adjustment",
        "occurred_at": "2026-04-02T09:28:34Z",
        "total_quantity_delta": 4,
        "available_quantity_delta": 4,
        "committed_quantity_delta": 0,
        "in_shop_quantity_delta": 4,
        "campaign_locked_quantity_delta": 0,
        "creator_locked_quantity_delta": 0
      }
    ]
  }
}
```

