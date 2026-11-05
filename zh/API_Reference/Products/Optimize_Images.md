# 优化图片

# Path: /product/202404/images/optimize
# Method: [POST]
# 功能描述
Optimize images used in your TikTok Shop by changing the background to white.
This is especially useful for images displayed in the product image gallery as it enhances product visibility.
**Note**:

* The images to be optimized must first be uploaded to TikTok Shop through the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). You will not be able to optimize any images that are not hosted by TikTok Shop.
* Images that were previously optimized will not be processed again.
* The optimization is processed asynchronously and typically completes within a few seconds. If no stored optimization result exists, `optimize_status` is `PROCESSING`, indicating that optimization is underway. If a stored final result already exists, the API may return it immediately. When `optimize_status` is `PROCESSING`, call the API again after a few seconds to get the final optimization status.


---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 属性 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求查询参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性 description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| images | []object | N |  | The list of images to be optimized. |
| Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload the images first and obtain the corresponding image URIs. |  |  |  |  |
| Max count: 200 |  |  |  |  |
| ^uri | string | N | tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d | 图片的 URI。 |
| Retrieve the URI from the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). |  |  |  |  |
| ^optimization_mode | []string | N | ["WHITE_BACKGROUND"] | The optimization type. |
| Possible values: |  |  |  |  |

* WHITE_BACKGROUND: Change the background to white. |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202404/images/optimize?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"images":[{"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","optimization_mode":["WHITE_BACKGROUND"]}]}
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^images | []object |  | The list of images to be optimized. |
| ^^height | int | 600 | The height of the original image, in pixels. |
| ^^width | int | 600 | The width of the original image, in pixels. |
| ^^original_uri | string | tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d | The original URI of the image to be optimized. |
| ^^original_url | string | https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp | The original URL of the image to be optimized. |
| ^^optimized_uri | string | tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6 | 优化后图片的 URI。 |
| 在创建或编辑产品时传递此值，以将图片与产品关联。 |  |  |  |
Applicable only if `optimize_status`is `SUCCESS`. |
^^optimized_url |string |https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp |优化后图片的 URL。
Use this URL in product descriptions by embedding it within an HTML `<img>` tag.
Applicable only if `optimize_status`is `SUCCESS`. |
^^optimize_status |string |SUCCESS |The optimization status.
Possible values:

* SUCCESS: The image has been successfully optimized.
* IGNORE: The image already has a white background, so no optimization was applied.
* PROCESSING: The optimization is in progress, and typically completes within a few seconds. Call this API again to obtain the final optimization status. |

# 响应示例
```json
{"code":0,"data":{"images":[{"height":600,"width":600,"original_uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","original_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/53b55d6e8cdf1f315affa7e70b45707d~tplv-1por3rr4fy-image.webp","optimized_uri":"tos-maliva-i-o3syd03w52-us/0266127022264e54ad2f639f5e0fb5e6","optimized_url":"https://p16-graph-va.ibyteimg.com/tos-maliva-i-1por3rr4fy-us/v2/0266127022264e54ad2f639f5e0fb5e6~tplv-1por3rr4fy-image.webp","optimize_status":"SUCCESS"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 12019065 | The image URI is invalid. Please use the URI generated by the Upload Product Image API. |
| 12019070 | The optimization mode is invalid. |
| 12038007 | The number of image URIs exceeded the limit of 200. |
| 12052722 | The image URI does not exist in TikTok Shop. |

