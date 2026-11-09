# (63) 活动变更

## 触发场景
活动变更 webhook 用于通知合作伙伴与活动及其关联商品的修改。此通知使应用程序能够与活动详情或商品纳入/排除列表的变更保持同步。
## 数据业务参数
| 字段 | 类型 | 示例 | 描述 |
| --- | --- | --- | --- |
| shop_id | String | "7494049642642441621" | 店铺的 ID。 |
| timestamp | Int64 | 1732526400 | 此 webhook 触发时的时间，以 Unix 时间戳表示。 |
| tts_notification_id | String | "7327112393057371910" | 通知的 ID。 |
| type | Int64 | 63 | webhook 类型的 ID。 |
| data | Object |  |  |
| └ activity_id | String | "7136104329798256386" | 促销活动的 ID。 |
| └ update_time | Int64 | 1732526465 | 状态变更的时间，以 Unix 时间戳（秒）表示。 |
| └ change_type | String | CREATE | 活动变更的类型。<br/>  <br/> * CREATE<br/> * UPDATE<br/> * DEACTIVATE |
| └ product_update_list | Object |  | 纳入更新范围的商品。 |
| └└ product_ids | []String | ["123456","789012"] | 纳入的商品 ID。 |
| └└ exclude_product_ids | []String | ["345678"] | 要移除的 BXGY 排除商品 ID。<br/>最大数量：100。 |
| └└ benefit_product_ids | []String | ["456789"] | TikTokShop 商品 ID 列表。 |
| └ product_remove_list | Object |  | 从活动中移除的商品。 |
| └└ product_ids | []String | ["111222","333444"] | 被移除的商品 ID。 |
| └└ sku_ids | []String | ["111","222"] | 被移除的 SKU ID。 |
| └└ benefit_product_ids | []String | ["555666"] | TikTokShop 商品 ID 列表。 |
| └└ exclude_product_ids | []String | ["345678"] | 要移除的 BXGY 排除商品 ID。<br/>最大数量：100。 |

## 事件示例
```JSON
{
  "type": 63,
  "timestamp": 1678886400,
  "shop_id": "789123456789123456",
  "tts_notification_id": "000000000000000001",
  "data": {
    "activity_id": "act_123456789012345678",
    "update_time": 1678886400,
    "change_type": "product_update",
    "product_update_list": {
      "product_ids": [
        "11111111",
        "22222222"
      ],
      "exclude_product_ids": [
        "33333333"
      ],
      "benefit_product_ids": [
        "44444444"
      ]
    },
    "product_remove_list": {
      "product_ids": [
        "55555555"
      ],
      "sku_ids": [
        "66666666"
      ],
      "benefit_product_ids": [],
      "exclude_product_ids": []
    }
  }
}
```


