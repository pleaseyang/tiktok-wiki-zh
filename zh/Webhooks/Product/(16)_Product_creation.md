# (16) 商品创建

# 1. 触发场景
当商品被创建时触发 webhook 消息。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| product_id | int | 1X2X3X4X5 | TikTok Shop 商品的标识符 |
| product_types | []string | ["GPR_PRODUCT"] | 商品类型，包括：<br/>  <br/> * COMBINED_PRODUCT：虚拟捆绑商品。<br/> * GPR_PRODUCT：使用 GPR 工具创建的目标商品 |
| update_time | int | 1627587600 | 商品创建的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```JSON
{
  "type": 16,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": 576486316948490000,
    "product_types": ["GPR_PRODUCT"],
    "update_time": 1644412885
  }
}
```


