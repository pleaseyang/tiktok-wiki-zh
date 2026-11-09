# 获取 Conversation Messages

# 路径：/customer_service/202309/conversations/{conversation_id}/messages
# 方法：[GET]
# 功能描述
使用此 API 获取买家与店铺之间 conversation 中的一页消息。
调用此 API 不会将消息标记为已读。请调用 [Read Message](650a59f7c16ffe02b8e8db3f) 将其标记为已读。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确的值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| conversation_id | string | Y | 7494560109732334261 | Conversation ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| page_token | string | N | 7494560109732337542 | 分页游标，表示此次查询应从何处开始。 |
| 获取下一页时，使用响应中的 "next_page_token"。 |  |  |  |  |
| page_size | int | Y | 10 | 每页返回的消息数量。值必须在 1 到 10 之间（含）。 |
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
   sort_order |string |N |DESC |排序方式。
   可能的枚举值：
* DESC（默认）
* ASC |
   sort_field |string |N |create_time |按以下属性之一对消息进行排序：
* `create_time`（默认）
* `index` |
   need_data |bool |N |false |当结构化数据可用时，是否请求可见消息的 `data` 字段。默认值：`false`。 |
   need_plaintext |bool |N |false |当人类可读表示可用时，是否请求可见消息的 `plaintext` 字段。默认值：`false`。 |
   time_zone |string |N |Asia/Shanghai |用于格式化受支持消息内容中日期和时间值的时区，包括生成的纯文本。此参数不会更改 `create_time`，它仍然是以秒为单位的 Unix 时间戳。使用 IANA 时区名称，例如 `Asia/Shanghai` 或 `America/Los_Angeles`。默认值：`UTC`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/customer_service/202309/conversations/7494560109732334261/messages?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_token=7494560109732337542&page_size=10&locale=en&sort_order=DESC&sort_field=create_time&need_data=false&need_plaintext=false&time_zone=Asia/Shanghai
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | 162312320 | 该索引表示下一页应从何处开始。 |
| 如果没有更多记录，此字段将为 ""（空字符串）。 |  |  |  |
| 将此值放入请求参数 "page_token" 以查询下一页。 |  |  |  |
| ^unsupported_msg_tips | string | 请在 Seller Center 查看此消息。 |  |
| 如果您的应用遇到不支持的消息类型，可以显示此文本引导用户前往 TikTok Shop 查看该消息。消息内容取决于具体的 `locale`。 |  |  |  |
| ^messages | []object |  | Conversation 中的消息。 |
| ^^id | string | 7494560109732334263 | 消息 ID。 |
| ^^type | string | TEXT | 消息类型。 |
| 可能的枚举值： |  |  |  |

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
* LOGISTICS_CARD
* OTHER：此 API 不支持的消息类型。 |
   ^^content |string |{"content": "simple text message"} |消息内容，JSON 序列化字符串格式。
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


* LOGISTICS_CARD：

```Plain Text
{
    "order_id": "12345",
    "package_id": "321"
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
^^create_time |int |1691411573 |消息创建的 Unix 时间戳，单位为秒。 |
^^is_visible |bool |true |此消息是否应展示给客服人员。
例如，买家在 conversation 结束时将收到来自系统的评价请求消息。您不应将此类消息展示给卖家或客服支持人员。 |
^^sender |object | |消息发送者。对于系统和机器人角色，店铺为发送者。 |
^^^im_user_id |string |7494560109732334261 |发送者的 ID。
这些是 IM ID，不能用于查询订单。 |
^^^role |string |BUYER |发送者的角色。可能的枚举值：

* `BUYER`
* `SHOP`
* `CUSTOMER_SERVICE`
* `SYSTEM`
* `ROBOT`
   对于 `SYSTEM` 和 `ROBOT` 角色，`im_user_id`、`nickname` 和 `avatar` 的值与 `SHOP` 角色相同。 |
   ^^^nickname |string |Albert |发送者的昵称。
* 对于店铺，昵称为店铺名称。
* 对于客服人员，昵称为客服人员的名称。
* 对于买家，昵称为买家在 TikTok 上的昵称。
   您可以在 Seller Center 设置店铺和客服人员的昵称。 |
   ^^^avatar |string |https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image? |发送者的头像 URL。
   |
   ^^index |string |7494560109732334274 |消息索引。此字段可用于消息排序。
   "index" 表示消息在 conversation 中的顺序。此值在 conversation 中每条消息都是唯一的。此值与时间相关，意味着较新的消息会获得更大的 "index"。但它并非严格递增。 |
   ^^data |string |{} |以 JSON 字符串编码的结构化消息数据。使用 `need_data=true` 请求此字段。该字段仅对可见消息以及可生成结构化数据的消息类型可用。

对于 `LOGISTICS_CARD` 消息，`predict_delivery_time_min`、`predict_delivery_time_max` 和 `tracking[].update_time_millis` 是以毫秒为单位的 Unix 时间戳，在 `data` 中保持原始数值。`time_zone` 请求参数影响生成的本地化 `plaintext`；它不会转换这些结构化数据的时间戳值。
`LOGISTICS_CARD` 消息示例：
```json
{
  "packages": [
    {
      "package_id": "456",
      "product_name": "Nutrition",
      "product_image": "https://cdn-us.com/us/123jpeg:1000:1000.jpeg?dr=123&t=555",
      "paid_price": "$0.01",
      "quantity": 1,
      "predict_delivery_time_min": 1763198750000,
      "predict_delivery_time_max": 1763457950000,
      "delivery_option": "Standard shipping",
      "tracking_number": "1Z789",
      "shipping_provider_name": "UPS",
      "tracking": [
        {
          "description": "Package has been delivered!",
          "update_time_millis": 1763954669267
        },
        {
          "description": "Arrived at the carrier's facility.",
          "update_time_millis": 1763954598311
        },
        {
          "description": "Package picked up.",
          "update_time_millis": 1763954598024
        },
        {
          "description": "Order packed and ready for dropoff at carrier's facility.",
          "update_time_millis": 1763451813897
        },
        {
          "description": "Order placed.",
          "update_time_millis": 1763112346906
        }
      ]
    }
  ]
}
``` |
^^plaintext |string |已分享商品卡片：
- 商品 ID：1732529206731441911；
- 商品名称：Áo Khoác Cardigan Logo Thêu Phong Cách Hàn Quốc By Zonef, Áo Khoác Thu Đông Chất Vải Cotton Tổ Ong Nam Nữ Unisex；
- 商品价格：；
- 划线价格：
- 已售出：40013。

查看完整详情：https://seller-vn.tiktok.com/product/manage?search_content=1732529206731441911 |人类可读的消息内容。使用 `need_plaintext=true` 请求此字段。该字段仅对可见消息以及可生成纯文本的消息类型可用。

`PRODUCT_CARD` 消息示例：
已分享商品卡片：
- 商品 ID：1732529206731441911；
- 商品名称：Áo Khoác Cardigan Logo Thêu Phong Cách Hàn Quốc By Zonef, Áo Khoác Thu Đông Chất Vải Cotton Tổ Ong Nam Nữ Unisex；
- 商品价格：；
- 划线价格：
- 已售出：40013。

查看完整详情：https://seller-vn.tiktok.com/product/manage?search_content=1732529206731441911 |


# 响应示例
```json
{"code":0,"data":{"next_page_token":"162312320","unsupported_msg_tips":"Please check this message in Seller Center.\n","messages":[{"id":"7494560109732334263","type":"TEXT","content":"{\"content\": \"simple text message\"}","create_time":1691411573,"is_visible":true,"sender":{"im_user_id":"7494560109732334261","role":"BUYER","nickname":"Albert","avatar":"https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/566c497faaaf4491a84d3ce55d9cb095~tplv-omjb5zjo8w-origin-image.image?"},"index":"7494560109732334274","data":"{}","plaintext":"Product card shared:\n- Product ID: 1732529206731441911; \n- Product name: Áo Khoác Cardigan Logo Thêu Phong Cách Hàn Quốc By Zonef, Áo Khoác Thu Đông Chất Vải Cotton Tổ Ong Nam Nữ Unisex; \n- Product price: ; \n- Strike-through price: \n- Sold: 40013. \n\nView full details at: https://seller-vn.tiktok.com/product/manage?search_content=1732529206731441911"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参考 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 45101001 | 内部错误。请稍后重试或联系技术支持团队寻求帮助。 |
| 45101003 | 未找到记录。请检查参数。 |
| 45101004 | 已达到查询配额（每天 10000 次请求）。请明天再试。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
