# (4) 包裹更新

# 1. 触发场景
当发生包裹合并、拆分、取消合并包裹等操作时，会触发此**包裹更新** webhook。
# 2. 数据业务参数
| **参数名称** | **示例** | **描述** |
| --- | --- | --- |
| sc_type | COMBINE | 事件触发的类型，可能的值：<br/>  <br/> * COMBINE<br/> * CANCEL_COMBINE<br/> * SPLIT<br/> * CANCEL_SPLIT<br/> * ADDRESS_UPDATE_SPLIT<br/> * CANCEL_FULFILL_SPLIT<br/> * FULFILL_UNCOMBINE<br/> * PARTLY_CANCEL_SPLIT<br/> * SPLIT_BY_SKU_CANCEL |
| role_type | ROLE_USER | 事件触发的操作角色，可能的值：<br/>  <br/> * ROLE_USER<br/> * ROLE_SELLER<br/> * ROLE_OPERATOR<br/> * ROLE_SYSTEM |
| package_list | []object | 事件触发更新的包裹列表 |
| └ package_id | "123456" | 包裹的标识符 |
| └ order_id_list | ["152523", "532123"] | 指定包裹中的订单 ID 列表 |
| update_time | 1627587600 | 包裹更新的时间，以 Unix 时间戳（秒）表示。 |
## 事件示例
```JSON
{
  "type": 4,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "sc_type": "COMBINE",
    "role_type": "ROLE_USER",
    "package_list": [
      {
        "package_id": "123456",
        "order_id_list": [
          "152523",
          "532123"
        ]
      }
    ],
    "update_time": 1644412885
  }
}
```


