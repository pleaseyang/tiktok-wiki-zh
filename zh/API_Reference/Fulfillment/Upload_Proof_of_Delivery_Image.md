# 上传交付证明图片

# 路径：/fulfillment/202309/images/upload
# 方法：[POST]
# 功能描述
此 API 用于卖家上传 package 的交付证明图片，并生成对应文件的 URL。生成的 URL 用于 [Update Package Delivery Status API](https://partner.tiktokshop.com/docv2/page/650aa332c16ffe02b8f0ba82?external_id=650aa332c16ffe02b8f0ba82) 以指示包裹已送达。
使用要求：

* 图片格式必须为 `JPEG`、`PNG` 或 `JPG`。
* 图片大小不得超过 5MB。


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺 API 时未传递正确值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | multipart/form-data | 允许类型: multipart/form-data |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 可以识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| data | file | Y | BWWCusFdYKa4W1wlphrbBWWCusFdYKaxtOawMj5ftPCQAAAABJRU5ErkJggg== | 在此 multipart/form-data 字段中以二进制数据上传的图片文件。 |
要求：

* 格式：`JPG`、`JPEG` 或 `PNG`。
* 分辨率：100 x 100 到 20,000 x 20,000 像素之间。
* 文件大小：不超过 5 MB。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202309/images/upload?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^url | string | https://p-pbe38.byted.org/tos-ppdi18n-i-0euhj0x6u9/0a119a90d90b41e3838608bc384 | 上传图片后返回的 URL，可以直接在浏览器中打开。 |
| ^height | int | 256 | 上传图片后返回的图片高度。此高度指处理后的图片高度，而非原始图片高度。 |
| 单位：像素。 |  |  |  |
| ^width | int | 256 | 上传图片后返回的图片宽度。此宽度指处理后的图片宽度，而非原始图片宽度。 |
| 单位：像素。 |  |  |  |
# 响应示例
```json
{"code":0,"data":{"url":"https://p-pbe38.byted.org/tos-ppdi18n-i-0euhj0x6u9/0a119a90d90b41e3838608bc384","height":256,"width":256},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019116 | 图片分辨率无效。请确保您的图片在 100 x 100 像素到 20000 x 20000 像素之间。 |
| 12038002 | 上传文件无效。请确保您传递了正确的文件数据。 |
| 12038004 | 图片文件类型无效。请确保您的图片为 JPG、JPEG 或 PNG 格式。 |
| 12038005 | 图片文件大小无效。请确保您的图片文件大小不超过 5MB。 |

