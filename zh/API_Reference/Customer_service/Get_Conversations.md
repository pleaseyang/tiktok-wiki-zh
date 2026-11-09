# 获取 Conversations

# 路径：/customer_service/202309/conversations
# 方法：[GET]
# 功能描述
使用此 API 获取店铺与买家的 conversations。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_token | string | N | 1612356123 | 分页游标，表示此次查询应从何处开始。 |
| 获取下一页时，使用响应中的 "next_page_token"。 |  |  |  |  |
| page_size | int | Y | 10 | 每页返回的 conversation 数量。必须在 1 到 20 之间。 |
| locale | string | N | en | 系统消息的显示语言。系统发送的消息将按设定语言返回；买家、店铺、客服人员发送的消息不受影响。默认值为 en（英语）。 |
可能的枚举值：

* de-DE（德语，德国）
* en（英语）
* en-GB（英语，英国）
* es-ES（西班牙语，西班牙）
* es-MX（西班牙语，拉丁美洲）
* fr-FR（法语，法国）
* id-ID（印尼语，印度尼西亚）
* it-IT（意大利语，意大利）
* ja-JP（日语）
* ms-MY（马来语，马来西亚）
* th-TH（泰语，泰国）
* vi-VN（越南语，越南）
* pt-BR（葡萄牙语，巴西）
* zh-CN（简体中文，中国） |
   need_session_id |bool |N |false |设置为 `true` 以请求 `cur_session_id`。该字段仅在 conversation 存在当前开放 session 且其公开阶段为 `AUTO_REPLY`、`QUEUED` 或 `ASSIGNED` 时返回。将 `need_session_info` 设置为 `true` 也会请求此字段。 |
   need_session_info |bool |N |false |设置为 `true` 以请求 `cur_session` 和 `cur_session_id`。这些字段仅在 conversation 存在当前开放 session 且其公开阶段为 `AUTO_REPLY`、`QUEUED` 或 `ASSIGNED` 时返回。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202309/conversations?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=1612356123&page_size=10&locale=en&need_session_id=false&need_session_info=false
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 1612353423 | 该索引表示下一页应从何处开始。 |
| 如果没有更多记录，此字段将为 ""（空字符串）。 |  |  |  |
| 将此值放入请求参数 "page_token" 以查询下一页。 |  |  |  |
| ^conversations | []object |  | Conversation 信息。 |
|  |  |  |  |
| ^^id | string | 7494560109732334261 | Conversation ID |
| ^^participant_count | int | 3 | Conversation 中的参与者数量。 |

* 如果 conversation 中没有客服人员参与，则值为 `2`：店铺和买家；
* 否则，值为 `3`：店铺、买家和客服人员。 |
   ^^can_send_message |bool |true |客服人员是否可以在此 conversation 中发送消息。在以下任一情况下，客服人员可以发送消息：
1. 买家与店铺在过去 30 天内存在历史 conversation。
2. 买家在过去 60 天内在该店铺下过订单。
3. 买家在该店铺有退货或退款记录。 |
   ^^unread_count |int |0 |客服人员未读消息数量。 |
   ^^create_time |int |1691411573 |Conversation 创建时的 Unix 时间戳。单位为秒。 |
   ^^participants |[]object | |Conversation 参与者。 |
   ^^^im_user_id |string |7494560109732334261 |参与者在 IM 系统中的 ID。此 ID 用于 IM 系统，不能用于查询订单。要查询订单，请使用 `user_id`。 |
   ^^^avatar |string |https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image? |参与者的头像 URL。
   |
   ^^^user_id |string |7494560109732334262 |参与者的 ID。 |
   ^^^role |string |BUYER |参与者的角色。
   可能的枚举值：
* `BUYER`
* `SHOP`
* `CUSTOMER_SERVICE` |
   ^^^nickname |string |Albert |参与者的昵称。 |
   ^^^buyer_platform |string |TIKTOK_SHOP |买家来自哪个平台。
   此字段仅在参与者的 `role` 为 `BUYER` 且店铺所在地区为印度尼西亚时返回。可能的枚举值：
* TIKTOK_SHOP
* TOKOPEDIA
   您不能向来自不同平台的买家发送特定平台的内容。例如，当您向 Tokopedia 买家发送商品卡片时，必须确保该商品已在 Tokopedia 上架。 |
   ^^latest_message |object | |Conversation 中的最新消息。 |
   ^^^id |string |7494560109732334263 |消息 ID。 |
   ^^^type |string |TEXT |消息类型。
   可能的枚举值：
* TEXT
* IMAGE
* ALLOCATED_SERVICE - 客服人员加入 conversation。
* NOTIFICATION - 来自系统的通知。
* BUYER_ENTER_FROM_TRANSFER：conversation 已转接给另一位客服人员。
* BUYER_ENTER_FROM_PRODUCT：买家在发送此消息前正在浏览商品。
* BUYER_ENTER_FROM_ORDER：买家在发送此消息前正在查看订单。
* PRODUCT_CARD
* EMOTICONS
* ORDER_CARD
* VIDEO
* RETURN_REFUND_CARD：退货/退款卡片。
* COUPON_CARD
* OTHER：此 API 不支持的消息类型。 |
   ^^^content |string |{"content": "simple text message"} |消息内容，JSON 序列化字符串格式。
   各类型消息的 content 示例如下：
* TEXT：

```Plain Text
{
    "content": "simple text"
}
```


* IMAGE：

```Plain Text
{
    "height": "290",
    "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290",
    "width": "304"
}
```


* PRODUCT_CARD、BUYER_ENTER_FROM_PRODUCT：

```Plain Text
{
    "product_id": "12345"
}
```


* ORDER_CARD、BUYER_ENTER_FROM_ORDER：

```Plain Text
{
    "order_id": "12345"
}
```


* RETURN_REFUND_CARD：

```Plain Text
{
    "order_id": "12345",
    "sku_id": "45678"
}
```


* VIDEO：

```Plain Text
{
    "url": "https://video-boei18n.byted.org/storage/v1/tos-boei18n-v-c72c01/e8240f35244646428df9c3244d1a7408?x-tos-algorithm=v2&x-tos-authkey=5bf25627da095a5cba28ace592de46cc&x-tos-expires=1681980481&x-tos-signature=r_bRxtrvGhXAuZgMmNhlZ_Upqzg",
    "cover": "https://p-boei18n.byted.org/tos-boei18n-v-c72c01/o8keEOhzTcNCcJyAbkWZwpLIyTfkJxcGbRBvLP~tplv-jvtte31kaf-origin-jpeg.jpeg?",
    "width": 640,
    "height": 360,
    "duration": "20.504",
    "vid": "v0e30cg700f7cgcmu8jc77u9e2bdp95g",
    "expire_time": "1681980481",
    "format": "mp4",
    "size": 400000,
    "bit_rate": 156067,
    "quality": "original",
    "codec_type": "h264"
}
```


* ALLOCATED_SERVICE、NOTIFICATION、BUYER_ENTER_FROM_TRANSFER、OTHER：

```Plain Text
{
    "content": "simple text"
}
```


* COUPON_CARD：

```Plain Text
{
    "coupon_id": "7262992004278206762"
}
```

注意：使用 [Get Coupon](6699dce0de15e502ed219e37) 获取优惠券详情。 |
^^^create_time |int |1691411573 |消息创建的 Unix 时间戳，单位为秒。 |
^^^is_visible |bool |true |此消息是否应展示给客服人员。
例如，买家在 conversation 结束时将收到来自系统的评价请求消息。您不应将此类消息展示给卖家或客服支持人员。 |
^^^sender |object | |消息发送者。 |
^^^^im_user_id |string |7494560109732334261 |发送者的 IM ID。发送者在 TikTok Shop IM 系统中的唯一标识符。 |
^^^^avatar |string |https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image? |发送者的头像 URL。
|
^^^^role |string |BUYER |发送者的角色。可能的枚举值：

* `BUYER`
* `SHOP`
* `CUSTOMER_SERVICE`
* `SYSTEM`
* `ROBOT`
   对于 `SYSTEM` 和 `ROBOT` 角色，`im_user_id`、`nickname` 和 `avatar` 的值与 `SHOP` 角色相同。 |
   ^^^^nickname |string |Albert |发送者的昵称。
* 对于店铺，昵称为店铺名称。
* 对于客服人员，昵称为客服人员的名称。
* 对于买家，昵称为买家在 TikTok 上的昵称。
   您可以在 Seller Center 设置店铺和客服人员的昵称。 |
   ^^^index |string |7494560109732334274 |消息索引。此字段可用于消息排序。
   "index" 表示消息在 conversation 中的顺序。此值在 conversation 中每条消息都是唯一的。此值与时间相关，意味着较新的消息会获得更大的 "index"。但它并非严格递增。 |
   ^^cur_session_id |string |7494472109882334261 |当前 session ID。 |
   ^^cur_session |object | |当前 session。 |
   ^^^id |string |7494472109882334261 |当前 session ID。 |
   ^^^phase |string |ASSIGNED |session 的当前阶段。
   可能的枚举值：
* `AUTO_REPLY` — session 正在由自动回复或聊天机器人处理。
* `QUEUED` — session 正在等待分配给客服人员。
* `ASSIGNED` — session 已分配给客服人员。 |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"1612353423","conversations":[{"id":"7494560109732334261","participant_count":3,"can_send_message":true,"unread_count":0,"create_time":1691411573,"participants":[{"im_user_id":"7494560109732334261","avatar":"https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image?","user_id":"7494560109732334262","role":"BUYER","nickname":"Albert","buyer_platform":"TIKTOK_SHOP"}],"latest_message":{"id":"7494560109732334263","type":"TEXT","content":"{\"content\": \"simple text message\"}","create_time":1691411573,"is_visible":true,"sender":{"im_user_id":"7494560109732334261","avatar":"https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image?","role":"BUYER","nickname":"Albert"},"index":"7494560109732334274"},"cur_session_id":"7494472109882334261","cur_session":{"id":"7494472109882334261","phase":"ASSIGNED"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 45101003 | 未找到记录。请检查参数。 |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
