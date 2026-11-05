# (24) FBT 库存更新

## 触发场景
当 FBT 库存更新时，会触发此 webhook。
> 前提条件：在合作伙伴中心已启用 **Fulfilled by TikTok(FBT) Info** API 权限范围。更多信息请参见[访问权限范围](access-scope)。

## 数据业务参数
| 参数名称 <!-- width:240px --> | 数据类型 | 示例 | 描述 |
| --- | --- | --- | --- |
| type | int | `24` | 此 webhook 主题的 ID，固定为 24。 |
| tts_notification_id | string | `"7327112393057371910"` | 此 webhook 通知的 ID。 |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 卖家的 open_id。更多信息请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ goods_id | string | `"732357708734418520388"` | FBT 商品 ID。 |
| └ sku_id | string | `"123513234"` | TikTok Shop SKU ID。 |
| └ fbt_warehouse_inventory | []object |  | 不同 FBT 仓库中的库存。 |
| └└ fbt_warehouse_id | string | `"73823232239293999999"` | FBT 仓库的 ID。 |
| └└ on_hand_detail | object |  | 仓库中实际持有的商品数量，不包括在途或损坏的商品。 |
| └└└ total_quantity | int | `7` | 商品总数量。 |
| └└└ reserved_quantity | int | `5` | 已确认订单预留且尚未出库的商品数量。 |
| └└└ available_quantity | int | `2` | 可用于销售的商品数量。不包括已预留的商品。 |
| └ update_time | int | `1644412845` | 操作发生的时间。Unix 时间戳。 |
## 事件示例
```JSON
{
  "type": 24,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "goods_id": "732357708734418520388",
    "sku_id": "123513234",
    "fbt_warehouse_inventory": [
        {
            "fbt_warehouse_id": "73823232239293999999",
            "on_hand_detail": {
                "total_quantity": 7,
                "reserved_quantity": 5,
                "available_quantity": 2
            }
        }
    ],
    "update_time": 1644412845
  }
}
```


