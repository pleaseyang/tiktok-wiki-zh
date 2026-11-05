# (38) 划线价过期

# 1. 触发场景
当划线价验证信息过期时（提交后 90 天），会触发此 webhook。
前提条件：在合作伙伴中心已启用 "Strikethrough Price" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 38 | 此 webhook 主题的 ID，固定为 38。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ product_id | string | "732357708734418520388" | TikTok Shop 商品 ID。 |
| └ sku_id | string | "73235770873441823254" | TikTok Shop SKU ID。 |
## 事件示例
```JSON
{
  "type": 38,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "732357708734418520388",
    "sku_id": "73235770873441823254"
  }
}
```


