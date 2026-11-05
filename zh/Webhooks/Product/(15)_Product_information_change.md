# (15) 商品信息变更

# 1. 触发场景
当**已上架**商品的属性变更并在线上生效时，会触发此 webhook。
**前提条件**：商品处于 **已上架** 状态，且在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 15 | 此 webhook 主题的 ID，固定为 15。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ product_id | string | "123456789" | 发生变更的商品 ID。 |
| └ change_source | string | "SELLER_CENTER" | 变更的来源。 <br/>可能的值：<br/> - `SELLER_CENTER`<br/> - `OPEN_API` |
| └ changed_fields | []string | [ <br/> "title", <br/> "description", <br/> "main_images", <br/> "product_attributes", <br/> "size_chart_image", <br/> "size_chart_template", <br/> "others" <br/> ] | 发生变更的商品属性。<br/>可能的值：<br/> - `title`：商品名称已变更。<br/> - `description`：商品描述已变更。<br/> - `main_images`：商品图片（在图片库中显示）已添加、删除或更改。<br/> - `product_attributes`：商品属性已添加、删除或编辑。<br/> - `size_chart_image`：尺码表图片已添加、删除或更改。<br/> - `size_chart_template`：关联的尺码表模板已删除或其详情已编辑，或关联了新的尺码表模板。<br/> - `others`：上述未列出的其他商品属性已变更。 |
| └ update_time | int | 1627587600 | 变更发生的时间。Unix 时间戳。 |
## 事件示例
```JSON
{
  "type": 15,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "123456789",
    "change_source": "SELLER_CENTER",
    "changed_fields": [
      "title",
      "description",
      "main_images",
      "product_attributes",
      "size_chart_image",
      "size_chart_template",
      "others"
    ],
    "update_time": 1627587600
  }
}
```


