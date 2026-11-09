# (50) SKU状态变更

# SKU状态变更Webhook
## 触发场景
当现有商品的SKU状态发生变更时，将触发此webhook。
典型场景包括：

* 在现有商品下新增SKU
* 从现有商品中删除SKU
* 激活现有SKU
* 停用现有SKU

**前提条件：** 卖家已订阅相应的webhook主题，且相关商品变更事件已被webhook传递管道成功消费。
## 数据业务参数
| 参数名称 | 数据类型 | 示例 | 描述 |
| --- | --- | --- | --- |
| type | int | 50 | 此webhook主题的ID。此值待最终分配。 |
| tts_notification_id | string | "7327112393057371910" | 此webhook通知的ID。 |
| shop_id | string | "7494049642642441621" | 店铺ID。 |
| timestamp | int | 1644412885 | 此webhook触发的时间。Unix时间戳。 |
| data | object |  | 此webhook的业务载荷。 |
| └ product_id | string | "123456789" | SKU状态发生变更的商品ID。 |
| └ skus | object[] | [{"sku_id":"987654321","status":"CREATED"}] | 状态发生变更的SKU列表。 |
| └└ sku_id | string | "987654321" | 状态发生变更的SKU的ID。 |
| └└ status | string | "CREATED" | 新的SKU状态。可能的值：`CREATED`、`DELETED`、`ACTIVATED`、`DEACTIVATED`。 |
| └└ deactivation_source | string | "SELLER" | 停用来源。仅当`status`为`DEACTIVATED`时返回此字段。可能的值：`SELLER`、`PLATFORM`、`COMBO_RELATION`。 |
| └ update_time | int | 1627587600 | 变更发生的时间。Unix时间戳。 |
## 事件示例
```JSON
{
  "type": "TBD",
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "123456789",
    "skus": [
      {
        "sku_id": "987654321",
        "status": "DEACTIVATED",
        "deactivation_source": "SELLER"
      },
      {
        "sku_id": "987654322",
        "status": "CREATED"
      }
    ],
    "update_time": 1627587600
  }
}
```

## 注意事项

* `timestamp`和`update_time`均为秒级Unix时间戳。
* 除非SKU被停用，否则`deactivation_source`将被省略。
* `skus`数组在单个事件中可能包含一条或多条SKU变更记录。
* 最终主题ID应在内部分配确认后更新。
