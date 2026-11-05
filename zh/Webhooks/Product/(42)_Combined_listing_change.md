# (42) 组合商品变更

# 1. 触发场景
当组合商品被创建、更新（组合商品中的商品列表发生变化）或删除时，会触发此 webhook。
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 42 | 此 webhook 主题的 ID，固定为 42。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ combined_listing_id | string | "123456789" | 组合商品 ID。 |
| └ products | []object |  | 变更后此组合商品中当前的商品列表。 |
| └└ id | string | "987654321" | 商品 ID。 |
| └ status | string | "LIVE" | 组合商品的状态。<br/>可能的值：<br/>  <br/> * LIVE<br/> * SYSTEM_DEACTIVATED<br/> * SELLER_DEACTIVATED<br/> * DELETED<br/>  <br/>注意：只有处于 LIVE 状态的组合商品才会出现在商品展示页面上。 |
| └ change_type | string | "UPDATE" | 对此组合商品进行的变更类型。<br/>可能的值：<br/>  <br/> * CREATE：组合商品已创建。<br/> * UPDATE：组合商品已更新，添加或移除了商品。<br/> * DELETE：组合商品已删除。 |
| └ added_product_ids | []string | ["987654321"] | 新添加到组合商品中的商品 ID 列表。 |
| └ removed_product_ids | []string | ["987654322"] | 从组合商品中移除的商品 ID 列表。 |
## 事件示例
```JSON
{
  "type": 42,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "combined_listing_id": "123456789",
    "products": [
      {
        "id": "987654321"
      },
      {
        "id": "987654322"
      }
    ],
    "status": "LIVE",
    "change_type": "UPDATE",
    "added_product_ids": ["987654321"],
    "removed_product_ids": ["987654333"]    
  }
}
```


