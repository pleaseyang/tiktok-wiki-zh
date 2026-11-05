# (23) 商品匹配

## 触发场景
当卖家将 TikTok Shop 商品与 FBT 商品进行匹配/取消匹配时，会触发此 webhook。
> 前提条件：在合作伙伴中心已启用 **Fulfilled by TikTok(FBT) Info** API 权限范围。更多信息请参见[访问权限范围](access-scope)。

## 数据业务参数
| **参数名称** <!-- width:240px --> | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | `23` | 此 webhook 主题的 ID，固定为 23。 |
| tts_notification_id | string | `"7327112393057371910"` | 此 webhook 通知的 ID。 |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | 卖家的 open_id。更多信息请参见[授权概述](authorization-overview-202407)。 |
| timestamp | int | `1644412885` | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ match_type | string | `"MATCH"` | 表示卖家是在匹配还是取消匹配商品。可能的枚举值为：`MATCH` 和 `UNMATCH`。 |
| └ product_type | string | `"LOCAL"` | 可能的枚举值为：`LOCAL` 和 `GLOBAL`。 |
| └ goods_id | string | `"732357708734418520388"` | FBT 商品 ID。 |
| └ product_id | string | `"123513234"` | TikTok Shop 商品 ID。 |
| └ sku_id | string | `"123563781"` | TikTok Shop SKU ID。 |
| └ update_time | int | `1644412845` | 操作发生的时间。Unix 时间戳。 |
## 事件示例
```JSON
{
  "type": 23,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "match_type": "MATCH",
    "product_type": "LOCAL",
    "goods_id": "732357708734418520388",
    "product_id": "123513234",
    "sku_id": "123563781",
    "update_time": 1644412845
  }
}
```


