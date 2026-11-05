# 上传产品图片

# Path: /product/202309/images/upload
# Method: [POST]
# 功能描述
将本地图片上传到 TikTok Shop，用作产品图片、变体图片、尺码表、认证图片或支持的其他图片用例。
**Note**:

* All images used in TikTok Shop products must be uploaded through this API. You cannot use image URLs that are not hosted by TikTok Shop.
* Store `data.uri` to associate the uploaded image with a product when creating or editing it. Store `data.url` when you need to display the image in a product description by using an HTML `<img>` tag.


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | multipart/form-data | 允许类型：multipart/form-data |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| data | file | Y |  | 要上传的本地图片文件。 |
**Note**:

* Supported formats: JPG, JPEG, PNG, WEBP, HEIC, BMP
* Zero-byte files are rejected.
* Max size: 10MB
* Dimensions: [100x100 px, 20000x20000 px]
* For `use_case=MAIN_IMAGE`, the dimensions must be between 300x300 px and 4000x4000 px.
* For `use_case=SIZE_CHART_IMAGE`, the dimension must be at least 1024 px on the shorter side. |
   use_case |string |N |MAIN_IMAGE |图片的使用场景。
   Possible values:
* MAIN_IMAGE: An image displayed in the product image gallery.
* ATTRIBUTE_IMAGE: An image that represents a product variant (e.g. color).
* DESCRIPTION_IMAGE: An image used within the product description.
* CERTIFICATION_IMAGE: An image to provide supporting information to meet TikTok Shop requirements for listing restricted products (e.g., images of certifications, product packaging, labeling).
* SIZE_CHART_IMAGE: An image that displays the product's measurement details.
* CUSTOMIZATION_IMAGE: Images used for POD product customization, such as background images, mask images, or default images configured for customizable areas. These images are used to render or preview consumer-customizable product content.

**Note**: Images for use cases `MAIN_IMAGE` and `ATTRIBUTE_IMAGE` that do not fit within the 3:4 to 4:3 aspect ratio range will be automatically converted to 1:1. |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202309/images/upload?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^uri | string | tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe | The URI to identify the image in API requests and responses. |
| 在创建或编辑产品时传递此值，以将图片与产品关联。 |  |  |  |
| ^url | string | https://p-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/c668cdf70b7f483c94dbe |  |
| 访问和查看图片的 URL。 |  |  |  |
| Use this URL in product descriptions by embedding it within an HTML `<img>` tag. |  |  |  |
| ^height | int | 720 | 调整宽高比后的图片高度。 |
|  |  |  |  |
| ^width | int | 720 | 调整宽高比后的图片宽度。 |
|  |  |  |  |
| ^use_case | string | MAIN_IMAGE | 上传时指定的使用场景。 |
| Possible values: |  |  |  |

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
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12038002 | Invalid upload file. Please ensure you are passing the correct file data. |
| 12038004 | Failed to process the image. The format or content is not supported. |
| 12038005 | The file size exceeds the maximum allowed size. |
| 12038014 | The image dimensions exceed the allowed limits. Allowed dimensions (width x height in pixels): &lbrace;&lbrace;min_width&rbrace;&rbrace; x &lbrace;&lbrace;min_height&rbrace;&rbrace; to &lbrace;&lbrace;max_width&rbrace;&rbrace; x &lbrace;&lbrace;max_height&rbrace;&rbrace; |
| 12038015 | Failed to process the image. The format or content is not supported. Supported formats: &lbrace;&lbrace;formats&rbrace;&rbrace; |

