# 获取图片翻译任务

# Path: /product/202506/images/translation_tasks
# Method: [GET]
# 功能描述
Retrieves the image translation task status and translated images for one or more previously submitted images.
**Note**: Please wait 5 minutes after [task creation](684f8b2d6e0b37048b2448b4) before calling this API, and retry at intervals over 10 seconds to avoid rate limiting.
Applicable only for sellers that sell across EU.

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
| translation_task_ids | []string | N | 764c6e87eedcea90399a0dafcd572b71,fadsf7eedcea90399a0dafcd572b71df | The image translation task IDs for retrieving translation results. |
| Max count: 20 |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/product/202506/images/translation_tasks?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&translation_task_ids=764c6e87eedcea90399a0dafcd572b71,fadsf7eedcea90399a0dafcd572b71df
```

# 响应参数
| 属性 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 属性 description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^translation_tasks | []object |  | The requested translation tasks and the corresponding results. Each task corresponds to the translation of 1 image into 1 target language. |
| ^^original_image | object |  | The original image to be translated. |
| ^^^uri | string | tos-useast2a-i-tulkllf4y5-euttp/748e39ecff38453ab8396a36a53dbb92 | The URI of the original image. |
| ^^^url | string | https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg | The URL of the original image. |
| ^^id | string | 764c6e87eedcea90399a0dafcd572b71 | The ID to identify the image translation task. |
| ^^target_language | string | it-IT | The target language to translate the image into. |
| Possible values: |  |  |  |

* de-DE
* en-IE
* es-ES
* fr-FR
* it-IT |
   ^^status |string |COMPLETED |The translation result.
   Possible values:
* PROCESSING: Translation is underway and has not yet completed.
* COMPLETED: Translation has completed and results are ready.
* FAILED: Translation did not complete due to an error. |
   ^^fail_reason |string |This image can't be translated. Try a different image. |The reason why the translation task failed.
   Possible values:
* Invalid image URI.
* Internal processing error, please try calling this endpoint again.
* This image can't be translated. Try a different image. |
   ^^translated_image |object | |The translated image. |
   ^^^uri |string |tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d |The URI of the translated image. |
   ^^^url |string |https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg |The URL of the translated image. |

# 响应示例
```json
{"code":0,"data":{"translation_tasks":[{"original_image":{"uri":"tos-useast2a-i-tulkllf4y5-euttp/748e39ecff38453ab8396a36a53dbb92","url":"https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg"},"id":"764c6e87eedcea90399a0dafcd572b71","target_language":"it-IT","status":"COMPLETED","fail_reason":"This image can't be translated. Try a different image.","translated_image":{"uri":"tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d","url":"https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg"}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 代码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | Internal error. Please try again. If the issue persists after multiple attempts, please contact platform support. |
| 12038010 | The number of translation task IDs exceeded the limit of 20. |
| 12038011 | The translation task ID is invalid. |
| 12038013 | This operation is not available for this shop. |

