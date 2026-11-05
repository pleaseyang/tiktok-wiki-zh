# (71) Inventory Changed By Shop

## 1. Trigger scenario
This webhook is triggered when a SKU's inventory quantity changes in a shop. Each notification identifies the affected shop, product, and SKU, and includes an inventory snapshot after the change together with the individual change details.
**Prerequisite**: The "Product Basic" API scope is enabled in Partner Center. For more information, refer to [Access Scope](https://partner.tiktokshop.com/docv2/page/access-scope).
The following events trigger this webhook when they cause an inventory quantity change:
| Trigger source | Description |
| --- | --- |
| `order_created` | An order is successfully placed, and inventory is committed to the order. |
| `order_canceled` | A buyer or seller cancels an order, and the committed inventory is released back to available stock. |
| `order_shipped` | An order is shipped, and the committed inventory is deducted. |
| `manual_adjustment` | A seller manually adjusts inventory in Seller Center. |
| `api_sync` | A developer updates inventory through an inventory-related OpenAPI. |
| `campaign_lock` | A seller joins a platform marketing campaign, and inventory is locked for the campaign. |
| `campaign_unlock` | A marketing campaign ends or a seller withdraws, and the locked inventory is released. |
| `creator_lock` | A seller allocates exclusive inventory to a creator collaboration. |
| `creator_unlock` | A creator collaboration ends, and the locked inventory is released. |
| `system_auto_replenish` | The system automatically replenishes inventory, such as after an order fails due to an exception. |
## 2. Data business parameters
All fields listed below are required in the notification payload. Sample IDs and quantities are illustrative.
| Parameter name | Data type | Sample | Description |
| --- | --- | --- | --- |
| `type` | int64 | `71` | The webhook topic ID. |
| `tts_notification_id` | string | `"7327112393057371910"` | The notification ID. |
| `shop_id` | string | `"7494049642642441621"` | The shop ID. |
| `timestamp` | int64 | `1775122114` | The time when the webhook is triggered, expressed as a Unix timestamp. |
| `data` | object | — | The inventory change event data. |
| └ `event_id` | string | `"inventory_event_001"` | An identifier for the inventory event; use it to deduplicate events. |
| └ `occurred_at` | string | `"2026-04-02T09:28:34Z"` | The event time in UTC, formatted as ISO 8601. |
| └ `shop_id` | int64 | `7494049642642441621` | The ID of the shop whose inventory changed. |
| └ `product_id` | int64 | `1891234567890123456` | The ID of the affected product. |
| └ `sku_id` | int64 | `1729507467923261408` | The ID of the affected SKU. |
| └ `quantity_snapshot_after_change` | object | — | The SKU inventory quantities after the change. |
| └ └ `total_quantity` | int64 | `100` | Total inventory: `total_available_quantity + total_committed_quantity`. |
| └ └ `total_available_quantity` | int64 | `80` | Available inventory, including quantities reserved for campaigns and creator collaborations. |
| └ └ `total_committed_quantity` | int64 | `20` | Inventory committed to orders that have not yet shipped. |
| └ └ `in_shop_quantity` | int64 | `65` | Available shop inventory: `total_available_quantity - campaign_locked_quantity - creator_locked_quantity`. |
| └ └ `campaign_locked_quantity` | int64 | `10` | Inventory reserved for marketing campaigns. |
| └ └ `creator_locked_quantity` | int64 | `5` | Inventory reserved for creator collaborations. |
| └ `change_detail` | []object | — | The individual inventory changes associated with the event. |
| └ └ `idempotency_key` | string | `"inventory_change_001"` | An identifier for an individual change; use it to deduplicate change details. |
| └ └ `trigger_source` | string | `"manual_adjustment"` | The cause of the change. See the trigger sources in Section 1. |
| └ └ `occurred_at` | string | `"2026-04-02T09:28:34Z"` | The UTC time of the individual change. |
| └ └ `total_quantity_delta` | int64 | `4` | The change in `total_quantity`. |
| └ └ `available_quantity_delta` | int64 | `4` | The change in `total_available_quantity`. |
| └ └ `committed_quantity_delta` | int64 | `0` | The change in `total_committed_quantity`. |
| └ └ `in_shop_quantity_delta` | int64 | `4` | The change in `in_shop_quantity`. |
| └ └ `campaign_locked_quantity_delta` | int64 | `0` | The change in `campaign_locked_quantity`. |
| └ └ `creator_locked_quantity_delta` | int64 | `0` | The change in `creator_locked_quantity`. |

For delta fields, a positive value indicates an increase, a negative value indicates a decrease, and zero indicates no change.
### Event example
The following example illustrates a seller adding four units to a SKU through Seller Center. Total inventory increases from 96 to 100, total available inventory from 76 to 80, and in-shop inventory from 61 to 65. Committed inventory and inventory reserved for campaigns or creators remain unchanged.
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

