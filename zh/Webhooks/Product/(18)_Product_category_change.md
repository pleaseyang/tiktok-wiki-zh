# (18) 商品类目变更

# 1. 触发场景
当商品的类目发生变更时，所有被店铺（使用 `shop_id`）授权的应用都会收到此 webhook。收到 webhook 后，您可以使用 [Get Product](get-product) API 获取更详细的商品信息。
无论商品类目以何种方式变更，都会触发此 webhook。类目可以由卖家、开发者或 TikTok Shop 进行变更。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `18` | webhook 类型的 ID。 |
| tts_notification_id | string | `"7327112393057371910"` | 通知的 ID。 |
| shop_id | string | `"7494049642642441621"` | 店铺的 ID。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| data | object |  |  |
| └product_id | string | `"789078671231"` | 达人视频中推广的商品 ID。 |
| └previous_category_id | string | `"600001"` | 类目更新前商品的类目 ID。 |
| └current_category_id | string | `"600002"` | 类目更新后商品的类目 ID。 |
| └update_time | int | `1644412845` | 此次类目更新发生的时间，以 Unix 时间戳表示。 |
## 事件示例
```JSON
{
  "type": 18,
  "shop_id": "7494049642642441621",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "product_id": "789078671231",
    "previous_category_id": "600001",
    "current_category_id": "600002",
    "update_time": 1644412845
  }
}
```


