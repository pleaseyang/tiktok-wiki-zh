# (27) 库存状态变更

# 1. 触发场景
以下任一情况都会触发此 webhook：

* `current_inventory_status` 已降至 LOW_STOCK / OUT_OF_STOCK。
* TikTok Shop 预测 `available_quantity` 将在 X 天内降至 `0`。

> 注意：X 的值可以由系统配置或由卖家手动设置。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 27 | 此 webhook 主题的 ID，固定为 27。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ product_id | string | "732357708734418520388" | 商品 ID。 |
| └ sku_id | string | "73235770873441823254" | SKU ID。 |
| └ trigger_reason | object |  |  |
| └└ alert_type | string | "PREDICTION" | PREDICTION：TikTok Shop 预测库存将在 X 天内售罄<br/> REALTIME：库存已达到 LOW_STOCK 或 OUT_OF_STOCK |
| └└ lead_days | int | 21 | 当 `alert_type == PREDICTION` 时，该值为 `update_time` 与预测售罄日期之间的时间间隔。<br/>当 `alert_type == REALTIME` 时，不返回此参数。 |
| └└ low_stock_threshold | int | 0 | 当 `alert_type == REALTIME` 时，该值为达到的低库存阈值。<br/>当 `alert_type == PREDICTION` 时，不返回此参数。 |
| └ current_inventory_status | string | "LOW_STOCK" | SUFFICIENT_STOCK：定义为库存充足。<br/> LOW_STOCK：定义为可用库存 ≤ 库存预警值<br/> OUT_OF_STOCK：定义为可用库存为 0。 |
| └ inventory_distribution | object |  |  |
| └└ total_quantity | int | 100 | 仓库中实际持有的库存总量。`total_quantity`=`available_quantity` + `creator_reserved_quantity` + `campaign_reserved_quantity` + `committed_quantity`。 |
| └└ available_quantity | int | 50 | 仓库中可用于下单的 SKU 总数。 |
| └└ creator_reserved_quantity | int | 20 | 仓库中为达人预留的 SKU 总数。 |
| └└ campaign_reserved_quantity | int | 20 | 仓库中为营销活动预留的 SKU 总数。 |
| └└ committed_quantity | int | 10 | 仓库中现有客户订单已占用的 SKU 总数。 |
| └ update_time | int | 1627587600 | 状态变更的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```JSON
{
  "type": 27,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "732357708734418520388"
    "sku_id": "73235770873441823254"
    "trigger_reason": {
        "alert_type": "PREDICTION",
        "lead_days": 21
    },
    "current_inventory_status": "LOW_STOCK",
    "inventory_distribution": {
        "total_quantity": 100,
        "available_quantity": 50,
        "creator_reserved_quantity": 20,
        "campaign_reserved_quantity": 20,
        "committed_quantity": 10
    },
    "update_time": 1627587600
  }
}
```


