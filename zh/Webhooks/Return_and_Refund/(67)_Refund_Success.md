# (67) 退款成功

使用此 webhook 识别退款完成状态以及精确的退款行项目引用。
# 1. 触发场景
当 RMA 的退款成功完成时。

# 2. 数据业务参数
| **字段** | **类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| shop_id | String | `7494049642642441621` | 与事件关联的 TikTok Shop 标识符。 |
| timestamp | Int | `1732526400` | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| tts_notification_id | String | `7327112393057371910` | 唯一的通知标识符，用于去重和追踪。 |
| type | Int | **`67`** | webhook 事件类型的数字标识。 |
| data | Object |  |  |
| └ aftersales_request_id | String | `576486316948490001` | 父级售后请求标识符。 |
| └ line_items | []object |  | 成功退款中包含的行项目级标识符。 |
| └└ main_order_id | String | `576486316948490003` | 正向主订单标识符。 |
| └└ return_line_item_id | String | `4035312491762651201` | 退货行项目标识符。 |
| └└ sku_id | String | `1732309230575784932` | SKU 标识符。 |
| └└ sku_return_request_id | String | `4035312491762585666` | SKU 级退货请求标识符。 |
| └└ sub_return_line_item_id | String | `4035312491762651202` | 可选的子行项目标识符，仅适用于虚拟捆绑商品退货。 |
| └ refund_currency | String | `USD` | 退款金额的币种。 |
| └ refund_status | String | `REFUND_SUCCESS` | 退款结果。当前示例显示 `REFUND_SUCCESS`。 |
| └ refund_timestamp | Int | `1776102211` | 退款完成时间，以 Unix 秒表示。 |
| └ refund_total | String | `1.25` | 退款总金额。 |
| └ rma_id | String | `576486316948490002` | 关联的 RMA 标识符。 |


## 事件示例
```JSON
{
  "type": 67,
  "tts_notification_id": "7628321701399676688",
  "shop_id": "123456",
  "timestamp": 1776107052,
  "data": {
    "aftersales_request_id": "111111111",
    "line_items": [
      {
        "main_order_id": "789456123",
        "return_line_item_id": "999999",
        "sku_id": "147852",
        "sku_return_request_id": "321654987",
        "sub_return_line_item_id": "888888"
      },
      {
        "main_order_id": "789456123",
        "return_line_item_id": "999999",
        "sku_id": "147853",
        "sku_return_request_id": "321654987",
        "sub_return_line_item_id": "777777"
      },
      {
        "main_order_id": "789456123",
        "return_line_item_id": "666666",
        "sku_id": "147853",
        "sku_return_request_id": "321654987"
      }
    ],
    "refund_currency": "USD",
    "refund_status": "REFUND_SUCCESS",
    "refund_timestamp": 1776102211,
    "refund_total": "1.25",
    "rma_id": "222222222"
  }
}
```


