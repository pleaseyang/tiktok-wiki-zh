# 获取可购物视频预审结果

# 路径：/affiliate_creator/202601/videos/precheck_tasks/{task_id}
# 方法：[GET]
# 功能描述
获取视频预检任务的违规检查结果，以及启用时的优质检查结果。如果返回的检查状态为 `PROCESSING`，请稍后再次调用此 API。如果检查状态为 `FAIL`，请查看其 `issues` 字段了解检测到的问题和建议的改进。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| task_id | string | Y | 7493990579714164574 | 来自 [Precheck Video Content](https://partner.tiktokshop.com/docv2/page/precheck-video-content-202511) 的任务 ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202601/videos/precheck_tasks/7493990579714164574?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^precheck_task | object |  | 视频预检任务 |
| ^^id | string | 7493990579714164574 | 视频预检任务的 ID。 |
| ^^violation_check_result | object |  | 违规检查详情 |
| ^^^status | string | FAIL | SUCCESS: 预检任务通过了违规检查 |
| FAIL: 预检任务因违规而失败。详情请查看 'issues' 字段。 |  |  |  |
| PROCESSING: 预检违规任务仍在进行中 |  |  |  |
| ^^^issues | []object |  | 违规检查失败时返回的政策违规详情列表 |
| ^^^^risk | string | Pirated Content | Policy violation |
| ^^^^suggestions | string | 您的视频可能包含非原创内容。创作原创内容是脱颖而出的关键。 | 针对所检测到的违规的详细解决指引。 |
| ^^good_quality_check_result | object |  | 优质检查详情。禁用优质检查时，此字段将省略。 |
| ^^^status | string | FAIL | SUCCESS: 预检任务通过了所有优质检查 |
| FAIL: 预检任务未通过优质检查。详情请查看 'issues' 字段。 |  |  |  |
| PROCESSING: 优质检查仍在进行中 |  |  |  |
| ^^^issues | []object |  | 优质检查失败时的质量问题与改进建议列表。 |
| ^^^^code | string | LOW_CONTENT_PROMOTIO | Quality finding |
| ^^^^suggestions | string | 你可以尝试从多个角度展示商品。 | 根据质量检查结果提供的改进建议。 |
# 响应示例
```json
{"code":0,"data":{"precheck_task":{"id":"7493990579714164574","violation_check_result":{"status":"FAIL","issues":[{"risk":"Pirated Content","suggestions":"Your video may include unoriginal content. Creating original content is essential for standing out from the crowd."}]},"good_quality_check_result":{"status":"FAIL","issues":[{"code":"LOW_CONTENT_PROMOTIO","suggestions":"You can try to showcase the product from multiple perspectives."}]}}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

