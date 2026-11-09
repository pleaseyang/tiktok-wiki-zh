# 上传商品图片

# 路径：/product/202309/images/upload
# 方法：[POST]
# 功能描述
将本地图片上传到 TikTok Shop，用作商品图片、变体图片、尺码表、认证图片或支持的其他图片用例。
**注意**：

* TikTok Shop 商品中使用的所有图片都必须通过此 API 上传. 不能使用非 TikTok Shop 托管的图片 URL。
* 保存 `data.uri`，以便在创建或编辑商品时将上传的图片与商品关联。保存 `data.url`，用于需要使用 HTML `<img>` 标签在商品描述中展示图片的情形。


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
| data | file | Y |  | 要上传的本地图片文件。 |
**注意**：

* 支持的格式：JPG, JPEG, PNG, WEBP, HEIC, BMP
* 零字节文件将被拒绝。
* 最大大小: 10MB
* 尺寸: [100x100 px, 20000x20000 px]
* 对于 `use_case=MAIN_IMAGE`，尺寸必须介于 300x300 px 和 4000x4000 px 之间。
* 对于 `use_case=SIZE_CHART_IMAGE`，短边尺寸必须至少为 1024 px。 |
   use_case |string |N |MAIN_IMAGE |图片的使用场景。
   可能的值：
* MAIN_IMAGE: 在商品图片库中展示的图片。
* ATTRIBUTE_IMAGE: 表示商品变体的图片 (e.g. color)。
* DESCRIPTION_IMAGE: 商品描述中使用的图片。
* CERTIFICATION_IMAGE：用于提供佐证信息以满足 TikTok Shop 对上架受限商品要求的图片（例如认证图片、商品包装、标签）。
* SIZE_CHART_IMAGE: 展示商品尺寸详情的图片。
* CUSTOMIZATION_IMAGE: 用于 POD 商品定制的图片，例如背景图片、蒙版图片或为可定制区域配置的默认图片。这些图片用于渲染或预览消费者可定制的商品内容。

**说明**：对于 `MAIN_IMAGE` 和 `ATTRIBUTE_IMAGE` 用例，不符合 3:4 至 4:3 宽高比范围的图片将自动转换为 1:1。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/images/upload?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | 用于在接口请求和响应中标识图片的 URI。 |
| 在创建或编辑商品时传递此值，以将图片与商品关联。 |  |  |  |
| ^url | string | https://p-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |  |
| 访问和查看图片的 URL。 |  |  |  |
| 在商品描述中使用此 URL, 将其嵌入 HTML `<img>` 标签中。 |  |  |  |
| ^height | int | 720 | 调整宽高比后的图片高度。 |
|  |  |  |  |
| ^width | int | 720 | 调整宽高比后的图片宽度。 |
|  |  |  |  |
| ^use_case | string | MAIN_IMAGE | 上传时指定的使用场景。 |
| 可能的值： |  |  |  |

* MAIN_IMAGE
* ATTRIBUTE_IMAGE
* DESCRIPTION_IMAGE
* CERTIFICATION_IMAGE
* SIZE_CHART_IMAGE
* CUSTOMIZATION_IMAGE |

# 响应示例
```json
{"code":0,"data":{"uri":"tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe","url":"https://p-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe\n","height":720,"width":720,"use_case":"MAIN_IMAGE"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 11050001 | invalid param |
| 12019116 | The image dimensions exceed the allowed limits. |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 12038002 | Invalid upload file. Please ensure you are passing the correct file data. |
| 12038004 | Failed to process the image. The format or content is not supported. |
| 12038005 | The file size exceeds the maximum allowed size. |
| 12038014 | 图片尺寸超出允许的限制。允许的尺寸（宽 x 高，单位像素）：&lbrace;&lbrace;min_width&rbrace;&rbrace; x &lbrace;&lbrace;min_height&rbrace;&rbrace; 至 &lbrace;&lbrace;max_width&rbrace;&rbrace; x &lbrace;&lbrace;max_height&rbrace;&rbrace; |
| 12038015 | 处理图片失败。不支持该格式或内容。支持的格式：&lbrace;&lbrace;formats&rbrace;&rbrace; |

