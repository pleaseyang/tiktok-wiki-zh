# 上传商品文件

# 路径：/product/202309/files/upload
# 方法：[POST]
# 功能描述
将非图片文件（如 PDF 或视频）上传到 TikTok Shop。
当您需要为商品添加视频以改善购物体验，或提交认证或报告以满足 TikTok Shop 上架受限商品的要求时，使用此 API。
**注意**： 保留响应中的文件 ID, 并在创建或编辑商品时传入，以将该文件与商品关联。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | multipart/form-data | 允许类型：multipart/form-data |
# 请求查询参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| data | file | Y |  | 要上传的本地文件。 |
**注意**：

* 支持的格式: PDF, MP4, MOV, MKV, WMV, WEBM, AVI, 3GP, FLV, MPEG
* 零字节文件将被拒绝。
* 最大 PDF 大小: 20 MB
* 最大视频大小: 100 MB
* 视频宽高比：9:16 至 16:9

**商品视频建议**:

* Aspect ratio: 1:1
* 分辨率：HD 720p 或更高
* Duration: 20 - 60 seconds |
   name |string |Y |SNI.pdf |文件名称，包括文件扩展名 (e.g. `certification.pdf`)

**注意**：

* 请勿使用额外的句点，文件扩展名前的句点除外。
* 名称不要以符号开头。
* 不要包含空格。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/files/upload?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^id | string | v09e40f40000cfu0ovhc77ub7fl97k4w | 由 TikTok Shop 生成的文件 ID。 |
| 在创建或编辑商品时传递此值，以将文件与商品关联。 |  |  |  |
| ^url | string | https://p-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |  |
| 访问和查看文件的 URL。 |  |  |  |
|  |  |  |  |
| ^name | string | SNI.PDF | 文件的名称。 |
| ^format | string | PDF | 文件的格式。 |
| 可能的值： PDF, MP4, MOV, MKV, WMV, WEBM, AVI, 3GP, FLV, MPEG |  |  |  |
# 响应示例
```json
{"code":0,"data":{"id":"v09e40f40000cfu0ovhc77ub7fl97k4w","url":"https://p-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe\n","name":"SNI.PDF","format":"PDF"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019103 | Couldn't upload file, the file is empty. |
| 12019104 | The file name is empty. |
| 12019105 | Failed to process the file. The format or content is not supported. |
| 12019122 | The video ratio must be between 9:16 and 16:9. |
| 12038002 | Invalid upload file. Please ensure you are passing the correct file data. |
| 12038004 | Failed to process the image. The format or content is not supported. |
| 12038005 | The file size exceeds the maximum allowed size. |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

