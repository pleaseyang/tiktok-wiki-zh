# 上传文件初始化

# 路径: /open/202512/file/init
# 方法: [POST]
# 功能描述
使用此 API 初始化文件上传会话。然后将文件上传到返回的上传 URL。5 MiB（5,242,880 字节）或以下的文件必须以单个非分块请求上传，并将 `total_chunk_count` 设置为 `1`；较大的文件使用分片上传。上传步骤返回 ResourceId 后，将该 ResourceId 传递给目标路径的 API。
更多详情请参阅 https://partner.tiktokshop.com/docv2/page/wfi3nz36。

---


# 公共参数
公共参数请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | 是 | application/json | 允许类型: application/json |
# 请求 Query 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| shop_cipher | string | 否 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| 通过 API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) 获取 |  |  |  |  |
| category_asset_cipher | string | 否 | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。请求 API 时未传递正确值将返回 在 API 请求中使用的合作伙伴标识符。 |
| 使用 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |  |  |  |  |
| app_key | string | 是 | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | 是 | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由签名算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送者。 |
| timestamp | int | 是 | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此值转换为本地时间。 |
# 请求 Body 参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| file_name | string | 是 | video_20251201.mp4 | 此上传会话要上传的文件名称。 |
| file_type | string | 是 | video | 要上传的文件类型。目前仅支持 video。 |
| file_size | int | 是 | 1024 | 文件大小，单位为字节 |
| total_chunk_count | int | 是 | 1 | 上传分片的总数。必须大于 0。对于 5 MiB（5,242,880 字节）或以下的文件，将此值设置为 1。 |
| target_path | string | 是 | [POST]/affiliate_seller/202501/images/upload | 视频上传后，使用此接口将视频资源绑定到特定素材 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/open/202512/file/init?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"file_name":"video_20251201.mp4","file_type":"video","file_size":1024,"total_chunk_count":1,"target_path":"[POST]/affiliate_seller/202501/images/upload"}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^upload_url | string | https://open-api.tiktokglobalshop.com/file/202512/upload | 平台提供的文件上传 URL。 |
| ^upload_token | string | 50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccac74c50b88 | 上传文件到返回的上传 URL 时使用的上传令牌。 |
# 响应示例
```json
{"code":0,"data":{"upload_url":"https://open-api.tiktokglobalshop.com/file/202512/upload","upload_token":"50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccac74c50b88"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码请参阅 [如何调用 TikTok Shop API - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |


