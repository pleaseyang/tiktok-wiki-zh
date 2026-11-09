# 更新 FBT 商品信息

# 路径：/fbt/202607/goods/update_goods_info
# 方法：[POST]
# 功能描述
更新 FBT 商品信息，包括商品名称、图片 URL、尺寸、危险品详情、保质期属性和退货地址信息。

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
| update_goods_dto | object | N |  | 要更新的商品信息。 |
更新行为是字段特定的；此对象既不是统一的部分补丁也不是完全替换。
共享字段：

* `tts_goods_id`：标识要更新的商品记录；不可修改。
* `goods_name`、`goods_image_url`、`return_handling_method` 和 `dimension_and_weight_base_info`：替换其存储值。
* `reference_code`：如果省略或为空，则重置为系统生成的备用值。
* `barcode_infos`：替换现有条形码集合。FBT 系统条形码被保留或添加，请求中省略的现有非系统条形码被删除。带有 inbound 记录的条形码的删除将被拒绝。
* `is_hazmat`：`false` 清除现有危险品信息。`true` 需要有效的 `hazmat_info`。

可选扩展字段：

* `is_sioc` 和 `sioc_attribute`：`is_sioc` 控制 Ships in Own Container（SIOC）管理。如果省略 `is_sioc`，则不请求 SIOC 状态或属性更新，且单独提供 `sioc_attribute` 将被忽略。
* `goods_safety_attributes`：省略的易碎、液体或尖锐子字段保留其存储值。更改锁定子字段的值会导致请求失败；重新提交相同的锁定值为空操作。提供的可编辑值将被更新。

请勿发送显式 `null`；这些字段的公共 schema 不可为空。 |
^tts_goods_id |string |Y |8839232030 |Fulfilled by TikTok 系统生成的商品标识符。 |
^goods_name |string |Y |Wireless Charging Cable |商品名称。 |
^goods_image_url |string |Y |https://example.com/fbt/goods-image.jpg |商品图片 URL。 |
^reference_code |string |N |ABDK999d |商品参考代码。 |
^barcode_infos |[]object |N | |条形码信息列表 |
^^barcode_type |string |N |UPC |商品提供的条形码类型。 |
^^barcode_value |string |N |223333 |商品的条形码值。 |
^return_handling_method |string |Y |RESTOCK_SELLABLE_DISPOSE_UNSELLABLE |FBT 客户退货服务存储的退货处理方式。此字段在每次更新请求中必填。
可能的值：

* RESTOCK_SELLABLE_DISPOSE_UNSELLABLE
* DISPOSAL_WITHOUT_INSPECTION
* RETURN_WITHOUT_INSPECTION
* RESTOCK_SELLABLE_RETURN_UNSELLABLE |
   ^dimension_and_weight_base_info |object |Y | |尺寸和重量信息 |
   ^^weight_value |string |Y |500 |以指定 weight_unit 为单位的商品重量。 |
   ^^length_value |string |Y |40 |以指定 dimension_unit 为单位的商品长度。 |
   ^^width_value |string |Y |20 |以指定 dimension_unit 为单位的商品宽度。 |
   ^^height_value |string |Y |30 |以指定 dimension_unit 为单位的商品高度。 |
   ^^weight_unit |string |Y |GRAM |重量单位。
   可能的值：
* MILLIGRAM
* GRAM
* KILOGRAM
* POUND
* OUNCE |
   ^^dimension_unit |string |Y |CENTIMETER |尺寸单位。
   可能的值：
* MILLIMETER
* CENTIMETER
* METER
* FOOT
* INCH |
   ^is_hazmat |bool |Y |false |是否为危险品商品 |
   ^hazmat_info |object |N | |当 `is_hazmat` 为 `true` 时使用的危险品信息。 |
   ^^hazmat_type |string |Y |BATTERY |危险品类型
   可能的值：
   -MAGNETIZED
   -BATTERY
   -FLAMMABLE_LIQUID
   -AEROSOLS |
   ^^battery_extra_info |object |N | |电池详情。当 `is_hazmat` 为 `true`、`dg_class` 为 `CLASS_9` 且 `hazmat_type` 为 `BATTERY` 时必填。提供此对象中标记为必填的每个字段。`total_battery_weight` 必须为大于 `0` 的数字字符串。当 `battery_packaging_type` 为 `STANDALONE` 时，`battery_count_per_package` 必填且必须为大于 `0` 的数字字符串。 |
   ^^^battery_type |string |Y |LITHIUM_ION |电池类型
   可能的值：
   LITHIUM_ION
   LITHIUM_METAL
   OTHER |
   ^^^battery_packaging_type |string |Y |STANDALONE |电池包装类型。
   可能的值：
* STANDALONE
* IN_EQUIPMENT
* WITH_EQUIPMENT
* OTHER |
   ^^^total_battery_weight |string |Y |10 |总电池重量 |
   ^^^total_battery_weight_unit |string |Y |GRAM |总电池重量单位，可能的值：GRAM |
   ^^^total_battery_capacity |string |Y |2 |总电池容量（瓦时）。 |
   ^^^total_battery_capacity_unit |string |Y |WATTHOUR |总电池容量单位，可能的值：WATTHOUR |
   ^^^is_need_un_38_3_test |bool |Y |false |UN38.3 测试确保电池符合特定的安全标准。如果报告中未包含在 MSDS 中，请在此字段中发送报告。 |
   ^^^un_38_3_test_file_url |string |N |https://example.com/fbt/un38-3-test-report.pdf |UN38.3 测试文件 URL |
   ^^^battery_count_per_package |string |N |3 |每个包装的电池数量 |
   ^^flammable_liquids_extra_info |object |N | |易燃液体详情。当 `is_hazmat` 为 `true`、`dg_class` 为 `CLASS_3` 且 `hazmat_type` 为 `FLAMMABLE_LIQUID` 时必填。`flammable_liquids_type` 必须有效，`flammable_liquids_volume` 必须为大于 `0` 的数字字符串。 |
   ^^^flammable_liquids_type |string |Y |PAINT |易燃液体类型。
   可能的值：
* PAINT
* PERFUMERY
* ALCOHOLIC
* OTHER |
   ^^^flammable_liquids_volume |string |Y |1 |易燃液体体积， |
   ^^^volume_unit |string |N |MILLILITERS |体积单位 |
   ^^dg_class |string |Y |CLASS_3 |危险品等级
   可能的值：
   -CLASS_2
   -CLASS_3
   -CLASS_9 |
   ^^dg_uncode |string |Y |UN2807 |危险物质的 UN 标识符。标准 UN 值使用 `UN` 前缀加四位数字；也支持 `OTHER`。
   可能的值：
* UN2807
* UN3480
* UN3090
* UN3481
* UN3091
* UN1263
* UN1266
* UN3065
* OTHER |
   ^^msds_file_url |string |Y |https://example.com/fbt/msds-report.pdf |危险品的材料安全数据表，用于支持在 FBT 中审核商品的安全合规性 |
   ^^aerosol_extra_info |object |N | |气雾剂详情。当 `is_hazmat` 为 `true`、`dg_class` 为 `CLASS_2` 且 `hazmat_type` 为 `AEROSOLS` 时必填。`volume` 必填且必须为大于 `0` 的数字字符串。 |
   ^^^volume |string |N |1 |气雾剂体积 |
   ^^^volume_unit |string |N |MILLILITERS |气雾剂体积单位 |
   ^is_lot_code |bool |Y |false |根据 FBT 类别规则，商品是否需要批次管理
   TRUE：此商品需要批次控制
   FALSE：此商品不需要批次控制
   |
   ^is_expiration_management |bool |Y |false |商品是否需要保质期管理。 |
   ^shelf_life_attribute_info |object |N | |商品的保质期属性。 |
   ^^shelf_life |int |N |10 |商品保质期（天） |
   ^^inbound_cutoff_days |int |Y |90 |商品过期前的 inbound 截止天数，表示在商品过期前仓库不再接受 inbound 货件的时间段。 |
   ^^expiration_alert_days |int |Y |80 |商品过期前的预警天数，表示平台向卖家发送过期提醒警报的时间段。 |
   ^^sales_cutoff_days |int |Y |70 |商品过期前的销售截止天数，表示在过期前商品不再可供销售的时间段。 |
   ^^handling_method_expired_goods |string |N |DISPOSE |过期 inventory 的处理方式。
   可能的值：
* `STORE_UNITS`：将单位移至缺陷 inventory。
* `RETURN_TO_SELLER`：将单位退回给卖家。
* `DISPOSE`：处置单位。 |
   ^is_sioc |bool |N |false |是否 SIOC |
   ^sioc_attribute |object |N | |SIOC 信息 |
   ^^sioc_files |[]object |N | |SIOC 文件 |
   ^^^sioc_certification_url |string |N |https://example.com/fbt/sioc-certification.jpg |SIOC 附件 URL |
   ^^^sioc_file_type |string |N |PHOTO |SIOC 附件类型：
* PHOTO
* DOCUMENT
* DROP_TEST_VIDEO |
   ^bulky_item_attribute |object |N | |大件商品信息 |
   ^^is_bulky_item_accessories |bool |N |false |商品是否为大件配件 |
   ^goods_safety_attributes |object |N | |安全属性信息 |
   ^^is_fragile |bool |N |false |是否易碎 |
   ^^is_liquid |bool |N |false |是否液体 |
   ^^is_sharp |bool |N |false |是否尖锐 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202607/goods/update_goods_info?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"update_goods_dto":{"tts_goods_id":"8839232030","goods_name":"Wireless Charging Cable","goods_image_url":"https://example.com/fbt/goods-image.jpg","reference_code":"ABDK999d","barcode_infos":[{"barcode_type":"UPC","barcode_value":"223333"}],"return_handling_method":"RESTOCK_SELLABLE_DISPOSE_UNSELLABLE","dimension_and_weight_base_info":{"weight_value":"500","length_value":"40","width_value":"20","height_value":"30","weight_unit":"GRAM","dimension_unit":"CENTIMETER"},"is_hazmat":false,"hazmat_info":{"hazmat_type":"BATTERY","battery_extra_info":{"battery_type":"LITHIUM_ION","battery_packaging_type":"STANDALONE","total_battery_weight":"10","total_battery_weight_unit":"GRAM","total_battery_capacity":"2","total_battery_capacity_unit":"WATTHOUR","is_need_un_38_3_test":false,"un_38_3_test_file_url":"https://example.com/fbt/un38-3-test-report.pdf","battery_count_per_package":"3"},"flammable_liquids_extra_info":{"flammable_liquids_type":"PAINT","flammable_liquids_volume":"1","volume_unit":"MILLILITERS"},"dg_class":"CLASS_3","dg_uncode":"UN2807","msds_file_url":"https://example.com/fbt/msds-report.pdf","aerosol_extra_info":{"volume":"1","volume_unit":"MILLILITERS"}},"is_lot_code":false,"is_expiration_management":false,"shelf_life_attribute_info":{"shelf_life":10,"inbound_cutoff_days":90,"expiration_alert_days":80,"sales_cutoff_days":70,"handling_method_expired_goods":"DISPOSE"},"is_sioc":false,"sioc_attribute":{"sioc_files":[{"sioc_certification_url":"https://example.com/fbt/sioc-certification.jpg","sioc_file_type":"PHOTO"}]},"bulky_item_attribute":{"is_bulky_item_accessories":false},"goods_safety_attributes":{"is_fragile":false,"is_liquid":false,"is_sharp":false}}}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^update_result_info | object |  | 商品更新结果信息。 |
| ^^tts_goods_id | string | 1233444 | Fulfilled by TikTok 系统生成的商品标识符 |
| ^^is_success | bool | true | 商品更新是否成功。 |
| ^^fail_reason | string | Goods update failed. | 商品更新失败的原因。 |
# 响应示例
```json
{"code":0,"data":{"update_result_info":{"tts_goods_id":"1233444","is_success":true,"fail_reason":"Goods update failed."}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

