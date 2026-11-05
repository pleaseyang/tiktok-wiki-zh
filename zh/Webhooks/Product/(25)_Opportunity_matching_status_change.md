# (25) 商机匹配状态变更

# 1. 触发场景
当候选商品的商机匹配状态发生变更时，会触发此 webhook。
**前提条件**：在合作伙伴中心已启用 "Product Opportunities" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
<span style="background-color: rgb(255, 245, 235)">📌 此 webhook 目前仅对部分开发者开放。</span>
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 25 | 此 webhook 主题的 ID，固定为 25。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1730458800 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ external_product_id | string | "576486316948490000" | 外部电商平台使用的商品标识符。 |
| └ opportunity_matching_status | string | "PENDING" | 商机匹配的状态。<br/>可能的值：<br/> - `PENDING`：等待商机匹配。<br/> - `MATCHED`：有一个或多个匹配成功的商机。<br/> - `NOT_MATCHED`：没有匹配到商机。 |
| └ opportunity_ids | []string | ["213231", "213233"] | 匹配成功的商机 ID 列表。 |
| └ opportunity_matching_end_time | int | 1735603200 | 系统停止为此候选商品匹配商机的截止时间。Unix 时间戳。<br/> - 默认值：上传时间后 60 天。<br/> - 最晚允许时间：上传时间后 60 天。 |
| └ update_time | int | 1730458800 | 商机匹配状态最后更新的时间。Unix 时间戳。 |
## 事件示例
```JSON
{  
  "type": 25,  
  "tts_notification_id": "7327112393057371910", 
  "shop_id": "7494049642642441621",  
  "timestamp": 1730458800,  
  "data": {  
    "external_product_id": "576486316948490000",  
    "opportunity_matching_status": "PENDING",
    "opportunity_ids": ["213231", "213233"],
    "opportunity_matching_end_time": 1735603200,
    "update_time": 1730458800
  }  
}
```


