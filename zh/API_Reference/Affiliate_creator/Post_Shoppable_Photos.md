# 发布可购物图片

# 路径：/affiliate_creator/202610/photos
# 方法：[POST]
# 功能描述
使用此接口发布带有 uris 和元数据的可购物照片。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| photos_info | []object | Y |  | 照片信息元数据 |
| ^photo_file_uris | string | Y | tos-useast5-i-photomode-tx/owBwaPnAIiaYg4Ck6aNcAmLkBA14n8QQQGEgi | 照片文件 URI，而非文件上传。使用 [Upload Shoppable Photo File] 上传图片并获取 photo_file_uri，然后在该字段中传入该 URI |
| music_id | string | N | 7577090708998212365 | Music ID |
| title | string | N | Post title | 帖子标题：最大长度为 5000 个 UTF-16 字符。如未指定，该工单帖子将不带任何文案。 - 你可以添加相关话题标签以提高可发现性。格式仅为 # 后跟话题名称。支持多个话题标签，e.g.,#humor#BFCM |
| link_info | object | N |  | 照片锚点及关联元数据 |
| ^post_type | string | Y | 1 | 1-LINK_TO_PRODUCT, 2-LINK_TO_SHOP, 3-LINK_TO_ONE_PIC_ONE_PRODUCT |
| ^shop_info | object | N |  | Shop Info |
| ^^shop_id | string | N | 7494831143334152261 | Shop ID |
| ^^group_type | string | N | 1 | 1 对应 shop_home_page, 2 对应 category, 3 对应 collection |
| ^^group_id | string | N | 6 | 类目 ID/集合 ID. 使用 [Get Shop Category And Collection] 获取有效的 category_id 或 collection_id, 然后在此字段中设置 |
| ^links | []object | N |  | 照片锚点列表 |
| ^^product_id | string | N | 74998589993939330 | Product ID |
| ^^link_title | string | N | product A | 照片锚点标题:商品锚点上展示的标题。锚点标题应少于 30 个字符 |
| is_ai_generated | bool | N | false | 用于指示内容是否为 AI 生成的字段。将此字段标记为 true 将显示一个标签，表明此帖子为 AI 生成帖子。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202610/photos?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"photos_info":[{"photo_file_uris":"tos-useast5-i-photomode-tx/owBwaPnAIiaYg4Ck6aNcAmLkBA14n8QQQGEgi"}],"music_id":"7577090708998212365","title":"Post title","link_info":{"post_type":"1","shop_info":{"shop_id":"7494831143334152261","group_type":"1","group_id":"6"},"links":[{"product_id":"74998589993939330","link_title":"product A"}]},"is_ai_generated":false}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^photo | object |  | 发布可购物照片的响应 |
| ^^photo_post_id | string | 34234234234324342 | 照片帖子 ID |
| ^quota | string | 3/day | 达人的内容发布额度。发布成功时返回；失败时包含在错误消息中；如果没有额度限制则省略。 |
# 响应示例
```json
{"code":0,"data":{"photo":{"photo_post_id":"34234234234324342"},"quota":"3/day"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16011007 | Product link title should be no longer than 30 characters. |
| 16011009 | Product link title contains offensive language. |
| 16011069 | Product link title contains punctuation or emoji. |
| 38007001 | System Error |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 170001002 | Creator TikTok Shop permission check failed. |
| 170001003 | Creator Tiktok Shop permission temporarily banned. |
| 170001004 | Creator TikTok Shop permission is permanently banned. |
| 170001005 | Creator terms of service not signed. Please contact TikTok for more details. |
| 170001006 | GKA terms not signed. Please try again after signing GKA term. |
| 170001007 | Creator did not sign the EU data share agreement. |
| 170001008 | Creator Age verification failed. Please verify age first. |
| 170001009 | 该商品属于不支持的类目。 |
| 170001010 | The commission plan gets failed or rejected. |
| 170001011 | The product doesn't exist. |
| 170001012 | The product is not available. |
| 170001013 | Showcase SPU exceeds limit. |
| 170001014 | Blocked by spam check. |
| 170001015 | Blocked by TikTok Shop risk control. |
| 170001018 | Get creator pay account error. Please verify the pay account first. |
| 170001020 | You have exceeded the frequency to post EC short videos. Please take a rest. |
| 170001030 | Creator account banned. Please contact TikTok agent for your account. |
| 170001031 | Creator forbidden to post content. |
| 170001040 | Please use valid video file id to post TikTok Shop short video. |
| 170001050 | Getting errors during video posting workflow. Please try again or contact TikTok. |
| 170001060 | Posting quota exceeded: the creator is under violation control, resulting in a reduced posting limit. |
| 170001061 | Posting quota exceeded: creator is in the newbie period. |
| 170001062 | Posting quota exceeded: platform-level posting limit reached. |
| 170001063 | The product you added only supports auction sales and cannot be used in shoppable videos or Carousels. |

