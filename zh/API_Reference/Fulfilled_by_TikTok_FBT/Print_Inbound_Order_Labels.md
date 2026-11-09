# 打印 Inbound 订单标签

# 路径：/fbt/202602/inbound_orders/label_print
# 方法：[POST]
# 功能描述
此 API 使用**异步长时间运行操作（LRO）**为 inbound 订单生成标签文件。inbound 订单必须已发货或处于之后的合格状态，且不得已取消。
**格式适用性**

* 仅当 `print_items` 包含 `CARTON_PALLET_LABEL` 时，`carton_label_format` 才控制箱或托盘标签布局。
* 仅当 `print_items` 包含 `FBT_BARCODE` 时，`barcode_format` 才控制商品条形码标签布局。

所选的 `print_items` 和两个已解析的格式值是打印任务标识符的一部分，因此在每次轮询请求中请保持相同的选择。
**工作流程**

1. **发起。** 发送带有子 inbound `order_id` 和所需 `print_items` 的请求。API 在生成标签文件期间返回 `PROCESSING`；相同请求值的已完成任务可能立即返回 `SUCCESS`。
2. **轮询。** 如果 `task_status` 为 `PROCESSING`，请使用相同的 `order_id`、`print_items`、`carton_label_format` 和 `barcode_format` 值重复请求。每 3-5 秒轮询一次。
3. **完成。** 当 `task_status` 为 `SUCCESS` 时，`download_url` 包含生成的 ZIP 文件。


---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| order_id | string | Y | 5766071177167344427 | 要打印标签的子 inbound 订单的数字标识符。 |
**说明：** 仅提供数字序列；不要包含 `IBR` 前缀（例如，使用 `123456` 而不是 `IBR123456`）。不要使用入库计划 ID。 |
print_items |[]string |N |[
"CARTON_PALLET_LABEL",
"FBT_BARCODE",
"PACKING_PICKING_LIST"
] |指定要生成的文档类型。可以在一个组合输出中包含多个值。
**允许值：**

* `CARTON_PALLET_LABEL`：箱或托盘的识别标签。将箱标签贴在每个箱的至少两个相邻面上。
* `PACKING_PICKING_LIST`：用于识别和打包物品的仓库文档。
* `FBT_BARCODE`：Fulfilled by TikTok 条形码标签。

**注意：** 如果此列表为空或省略，则默认生成 `CARTON_PALLET_LABEL`。 |
carton_label_format |string |N |DEFAULT_1UP |指定箱标签的布局和尺寸。如果省略此参数或提供无效值，系统将使用默认单标签格式。
**允许值：**

* `DEFAULT_1UP`：标准格式（每页 1 个标签）。
* `A4_4UP`：A4 纸格式（每页 4 个标签）。

**注意：** 如果未提供值，则默认使用 `DEFAULT_1UP` 格式。 |
barcode_format |string |N |DEFAULT_40MM_60MM |指定生成的标签 PDF 的布局和尺寸。如果省略此参数或提供无效值，系统将使用默认热敏标签格式。
**允许值：**
**标准 / 默认**

* `DEFAULT_40MM_60MM`：标准 40mm x 60mm 热敏标签格式

**A4 纸布局**

* `A4_21UP_60_0MM_40_0MM`：A4 纸上的 21 排标签（60.0mm x 40.0mm）
* `A4_21UP_63_5MM_38_1MM`：A4 纸上的 21 排标签（63.5mm x 38.1mm）
* `A4_24UP_63_5MM_33_9MM`：A4 纸上的 24 排标签（63.5mm x 33.9mm）
* `A4_24UP_64_6MM_33_8MM`：A4 纸上的 24 排标签（64.6mm x 33.8mm）
* `A4_24UP_66_0MM_33_9MM`：A4 纸上的 24 排标签（66.0mm x 33.9mm）
* `A4_24UP_66_0MM_35_0MM`：A4 纸上的 24 排标签（66.0mm x 35.0mm）
* `A4_24UP_70_0MM_36_0MM`：A4 纸上的 24 排标签（70.0mm x 36.0mm）
* `A4_24UP_70_0MM_37_0MM`：A4 纸上的 24 排标签（70.0mm x 37.0mm）
* `A4_27UP_63_5MM_29_6MM`：A4 纸上的 27 排标签（63.5mm x 29.6mm）
* `A4_40UP_52_5MM_29_7MM`：A4 纸上的 40 排标签（52.5mm x 29.7mm）
* `A4_44UP_48_5MM_25_4MM`：A4 纸上的 44 排标签（48.5mm x 25.4mm）

**US Letter 布局**

* `US_LETTER_30UP_1IN_2_625IN`：US Letter 纸上的 30 排标签（1" x 2-5/8"）

**注意：** 如果未提供值，则默认使用 `DEFAULT_40MM_60MM` 格式。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202602/inbound_orders/label_print?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"order_id":"5766071177167344427","print_items":["CARTON_PALLET_LABEL","FBT_BARCODE","PACKING_PICKING_LIST"],"carton_label_format":"DEFAULT_1UP","barcode_format":"DEFAULT_40MM_60MM"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^download_url | string | https://example.com/fbt/inbound_files.zip?download_token=sample_token | 包含 inbound 订单标签的 URL。 |
**请注意：URL 将进行 unicode 转义。如果尝试将 URL 手动粘贴到浏览器中，需要先对 URL 反转义（例如 '\u0026'->'&'）** |
^task_status |string |PROCESSING |* `PROCESSING`：任务正在处理中。继续定期轮询。

* `SUCCESS`：任务已完成。`download_url` 应包含在响应中 |

# 响应示例
```json
{"code":0,"data":{"download_url":"https://example.com/fbt/inbound_files.zip?download_token=sample_token","task_status":"PROCESSING"},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 39001002 | 请求或请求参数为空。请重新检查输入参数。 |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 39015007 | 访问被拒绝。此 API 要求卖家绑定到恰好一个 merchant。 |
| 39015009 | SellerId 输入无效 |
| 39015010 | 未找到该 merchant 的 inbound 订单。 |

