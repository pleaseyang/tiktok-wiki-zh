# (14) 新消息

# 1. 触发场景
当客服会话中发送新消息时，会触发此**新消息** webhook。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| message_id | string | 7494560109732334263 | 消息的标识符 |
| index | string | 7494560109732334274 | 消息索引，可用于消息排序。<br/>较新的消息具有更大的索引值。 |
| conversation_id | string | 576486316948490001 | 会话的标识符 |
| type | string(enum) | TEXT | 消息类型，可能的值：<br/> * TEXT<br/> * IMAGE<br/> * ALLOCATED_SERVICE<br/> * NOTIFICATION<br/> * BUYER_ENTER_FROM_TRANSFER<br/> * BUYER_ENTER_FROM_PRODUCT<br/> * BUYER_ENTER_FROM_ORDER<br/> * PRODUCT_CARD<br/> * ORDER_CARD<br/> * EMOTICONS<br/> * VIDEO<br/> * COUPON_CARD<br/> *LOGISTICS_CARD<br/> * OTHER |
| content | string | {"content": "simple text message"} | 消息内容，以 JSON 序列化字符串表示。<br/>示例：<br/>  <br/> * TEXT：<br/> {"content": "simple text"}<br/>  <br/> * IMAGE：<br/> {  <br/>      "height": "290",  <br/>      "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290",  <br/>      "width": "304"  <br/>  }  <br/>  <br/> * PRODUCT_CARD, BUYER_ENTER_FROM_PRODUCT：<br/>  {"product_id": "12345"}  <br/>  <br/> * ORDER_CARD, BUYER_ENTER_FROM_ORDER：<br/>  {"order_id": "12345"}  <br/>  <br/> * VIDEO：<br/>  {  <br/>      "url": "https://video-boei18n.byted.org/storage/v1/tos-boei18n-v-c72c01/e8240f35244646428df9c3244d1a7408?x-tos-algorithm=v2&x-tos-authkey=5bf25627da095a5cba28ace592de46cc&x-tos-expires=1681980481&x-tos-signature=r_bRxtrvGhXAuZgMmNhlZ_Upqzg",  <br/>      "cover": "https://p-boei18n.byted.org/tos-boei18n-v-c72c01/o8keEOhzTcNCcJyAbkWZwpLIyTfkJxcGbRBvLP~tplv-jvtte31kaf-origin-jpeg.jpeg?",  <br/>      "width": 640,  <br/>      "height": 360,  <br/>      "duration": "20.504",  <br/>      "vid": "v0e30cg700f7cgcmu8jc77u9e2bdp95g",  <br/>      "expire_time": "1681980481",  <br/>      "format": "mp4",  <br/>      "size": 400000,  <br/>      "bit_rate": 156067,  <br/>      "quality": "original",  <br/>      "codec_type": "h264"  <br/>  }  <br/>  <br/> * LOGISTICS_CARD：<br/> { <br/>     "order_id": "580874485811283206", <br/>     "package_id": "123456"  // 可选（建议一个订单多个包裹时使用；一个订单一个包裹时不需要） <br/> } <br/>  <br/> * COUPON_CARD：<br/>  {"coupon_id": "7262992004278206762"} <br/>  <br/>  <br/> 注意：使用 Get Coupon 接口获取优惠券详情。<br/>  <br/> * ALLOCATED_SERVICE, NOTIFICATION, BUYER_ENTER_FROM_TRANSFER, OTHER：<br/> {"content": "simple text"} |
| create_time | int | 1691411573 | 消息创建时间，以 Unix 时间戳（秒）表示。 |
| is_visible | bool | true | 此消息是否应展示给客服人员。 |
| sender | Object |  | 消息发送者。<br/>对于系统和机器人角色，店铺为发送者。 |
| ^im_user_id | string | 7494560109732334261 | 发送者 ID<br/>这些是 IM ID，不能用于查询订单。 |
| ^role | string(enum) | BUYER | 发送者角色，可能的值：<br/> * BUYER<br/> * SHOP<br/> * CUSTOMER_SERVICE<br/> * SYSTEM<br/> * ROBOT |
## 事件示例
```JSON
{
  "type": 14,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "content": "{\"content\":\"444\"}",
    "conversation_id": "710688832392260838",
    "create_time": 1681790246,
    "is_visible": true,
    "message_id": "722323407926368819",
    "index": "7494560109732334274",
    "type": "TEXT",
    "sender": {
      "im_user_id": "707885565181165594",
      "role": "BUYER"
    }
  }
}
```


