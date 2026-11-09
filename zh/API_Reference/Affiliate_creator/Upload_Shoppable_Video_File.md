# 上传可购物视频文件

# 路径：/affiliate_creator/202505/videos/video_files
# 方法：[POST]
# 功能描述
在向 TikTok 发布可购物视频之前，先上传视频文件。上传成功后，调用 `POST /affiliate_creator/202505/videos`，并将返回的 `video_file.id` 作为 `video_info.file_id` 传入。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | multipart/form-data | 允许类型：multipart/form-data |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| data | file | Y |  | 要上传的本地文件。 |
| Note： |  |  |  |  |

* 对于大于 10 MB 的文件，请使用 [Large File Uploads](https://partner.tiktokshop.com/docv2/page/wfi3nz36)。
* 支持的格式: MP4, MOV, MKV, WMV, WEBM, AVI, 3GP, FLV, MPEG
* 最大视频大小: 10 MB
* 视频宽高比：9:16 至 16:9
   商品视频建议:
* 分辨率: 720p 或更高
* Duration: > 30 seconds |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202505/videos/video_files?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^video_file | object |  | 视频文件信息。 |
| ^^id | string | 123123123123 | 已上传视频文件的 id。 |
| ^^md5 | string | D41D8CD98F00B204E9800998ECF8427E | 上传文件 md5 校验和 |
# 响应示例
```json
{"code":0,"data":{"video_file":{"id":"123123123123","md5":"D41D8CD98F00B204E9800998ECF8427E"}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

