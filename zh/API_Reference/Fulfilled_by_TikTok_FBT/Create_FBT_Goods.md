# 创建 FBT 商品

# Path: /fbt/202607/goods/create_goods
# Method: [POST]
# 功能描述
创建 FBT 商品记录并将每条记录链接到 TikTok Shop SKU。请求级别的错误可能在每条商品结果生成之前返回。当 `create_result_info.create_result_list` 包含条目时，请通过 `tts_sku_id` 进行关联，检查每个返回条目的 `is_success`，读取失败条目的 `fail_reason`，并使用成功条目的 `tts_goods_id`。
该请求支持尺寸和重量、退货处理、危险品、保质期、SIOC、大件商品和安全属性。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时未传递正确的值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| create_goods_dto_list | []object | Y |  | 要创建的商品记录列表。 |
| ^tts_sku_id | string | Y | 723456789012345678 | TikTok Shop 系统生成的 Stock Keeping Unit（SKU）标识符 |
| ^create_goods_type | string | Y | CREATE_AND_BIND | 创建商品操作的类型。当前支持的值：CREATE_AND_BIND。 |
| ^goods_name | string | Y | Wireless Charging Cable | 商品名称。最大长度：255 个字符。 |
| ^goods_image_url | string | Y | https://example.com/fbt/goods-image.jpg | 商品图片 URL。 |
| ^reference_code | string | N | ABDK999d | 商品参考代码。最大长度：50 个字符。 |
| ^barcode_infos | []object | N |  | 商品条形码。每条商品记录最多提供一个 UPC、EAN 或 GTIN，最多提供五个 ASIN_OR_FNSKU 值，以及最多五个 MERCHANT_SKU_ID 值。 |
| ^^barcode_type | string | N | UPC | 商品提供的条形码类型，如 UPC。 |
| ^^barcode_value | string | N | 12345678905 | 条形码值。UPC 必须包含 8 位或 12 位数字；EAN 必须包含 8 位或 13 位数字；GTIN 必须包含 8 位、12 位、13 位或 14 位数字。UPC、EAN 和 GTIN 值必须具有有效的校验和。ASIN_OR_FNSKU 必须包含 10 个大写字母或数字，并以 B 或 X 开头。MERCHANT_SKU_ID 必须包含 1 到 32 个可打印的 ASCII 字符，不含空格。 |
| ^return_handling_method | string | Y | RESTOCK_SELLABLE_DISPOSE_UNSELLABLE | FBT 客户退货服务的退货处理方式。默认值为 Restock sellable, Dispose unsellable。 |
| 可能的值： |  |  |  |  |

* COLLECT_RETURN_UNITS
* RESTOCK_SELLABLE_COLLECT_UNSELLABLE
* RESTOCK_SELLABLE_DISPOSE_UNSELLABLE
* DISPOSAL_WITHOUT_INSPECTION
* RETURN_WITHOUT_INSPECTION
* RESTOCK_SELLABLE_RETURN_UNSELLABLE |
   ^dimension_and_weight_base_info |object |Y | |商品的尺寸和重量。weight_value、length_value、width_value 和 height_value 必须各自为大于 0 的数字字符串。 |
   ^^weight_value |string |Y |500 |以指定 weight_unit 为单位的商品重量。 |
   ^^length_value |string |Y |2 |以指定 dimension_unit 为单位的商品长度。 |
   ^^width_value |string |Y |2 |以指定 dimension_unit 为单位的商品宽度。 |
   ^^height_value |string |Y |3 |以指定 dimension_unit 为单位的商品高度。 |
   ^^weight_unit |string |Y |GRAM |重量单位。可能的值：MILLIGRAM (mg)、GRAM (g)、KILOGRAM (kg)、POUND (lb)、OUNCE (oz)。 |
   ^^dimension_unit |string |Y |CENTIMETER |尺寸单位。可能的值：MILLIMETER (mm)、CENTIMETER (cm)、METER (m)、FOOT (ft)、INCH (in)。 |
   ^is_hazmat |bool |Y |false |是否为危险品商品 |
   ^hazmat_info |object |N | |危险品详情。当 is_hazmat 为 true 时必填。对于 hazmat_type 为 BATTERY、FLAMMABLE_LIQUID 或 AEROSOLS 的情况，分别需提供 battery_extra_info、flammable_liquids_extra_info 或 aerosol_extra_info。 |
   ^^hazmat_type |string |Y |BATTERY |危险品类型
   可能的值：
   -MAGNETIZED
   -BATTERY
   -FLAMMABLE_LIQUID
   -AEROSOLS |
   ^^battery_extra_info |object |N | |当 hazmat_type 设置为 BATTERY 时的电池详情。total_battery_weight 必须大于 0。当 battery_packaging_type 为 STANDALONE 时，battery_count_per_package 必须大于 0。当 is_need_un_38_3_test 为 true 时，需提供 un_38_3_test_file_url。 |
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
   ^^^total_battery_weight |string |Y |10 |以 total_battery_weight_unit 指定单位表示的总电池重量。 |
   ^^^total_battery_weight_unit |string |Y |GRAM |total_battery_weight 的单位。可能的值：GRAM。 |
   ^^^total_battery_capacity |string |Y |2 |以 total_battery_capacity_unit 指定单位表示的总电池容量。 |
   ^^^total_battery_capacity_unit |string |Y |WATTHOUR |total_battery_capacity 的单位，如 WATTHOUR。 |
   ^^^is_need_un_38_3_test |bool |Y |false |UN38.3 测试确保电池符合特定的安全标准。如果报告中未包含在 MSDS 中，请在此字段中发送报告。 |
   ^^^un_38_3_test_file_url |string |N |https://example.com/fbt/un38-3-test-report.pdf |UN38.3 测试文件 URL |
   ^^^battery_count_per_package |string |N |3 |每个包装的电池数量 |
   ^^flammable_liquids_extra_info |object |N | |当 hazmat_type 设置为 FLAMMABLE_LIQUID 时的易燃液体详情。flammable_liquids_volume 必须为大于 0 的数字字符串。 |
   ^^^flammable_liquids_type |string |Y |PAINT |易燃液体类型。
   可能的值：
* PAINT
* PERFUMERY
* ALCOHOLIC
* OTHER |
   ^^^flammable_liquids_volume |string |Y |1 |以 volume_unit 指定单位表示的易燃液体体积。 |
   ^^^volume_unit |string |N |MILLILITERS |flammable_liquids_volume 的单位，如 MILLILITERS。 |
   ^^dg_class |string |Y |CLASS_2 |危险品等级
   可能的值：
   -CLASS_2
   -CLASS_3
   -CLASS_9 |
   ^^dg_uncode |string |Y |UN3480 |危险物质的 UN 标识符。标准 UN 值使用 `UN` 前缀加四位数字；也支持 `OTHER`。
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
   ^^aerosol_extra_info |object |N | |气雾剂信息 |
   ^^^volume |string |N |1 |气雾剂体积。当 `hazmat_type` 为 `AEROSOLS` 时必填。值必须为大于 0 的数字字符串。 |
   ^^^volume_unit |string |N |MILLILITERS |气雾剂体积单位 |
   ^is_lot_code |bool |Y |false |商品是否启用批次码管理。 |
   ^is_expiration_management |bool |Y |false |商品是否启用保质期管理。当为 true 时，需要提供 shelf_life_attribute_info。 |
   ^shelf_life_attribute_info |object |N | |商品的保质期属性。截止值必须为非负数，且满足 sales_cutoff_days < expiration_alert_days < inbound_cutoff_days。如果提供，shelf_life 必须小于 3650 天。 |
   ^^shelf_life |int |N |90 |商品保质期（天） |
   ^^inbound_cutoff_days |int |Y |100 |商品过期前的 inbound 截止天数，表示在产品过期前 warehouse 不再接受 inbound 货件的时间段。 |
   ^^expiration_alert_days |int |Y |90 |商品过期前的预警天数，表示平台向商家发送过期提醒警报的时间段。 |
   ^^sales_cutoff_days |int |Y |80 |商品过期前的销售截止天数，表示在过期前商品不再可供销售的时间段。 |
   ^^handling_method_expired_goods |string |N |DISPOSE |过期 inventory 的处理方式。
   可能的值：
* `STORE_UNITS`：将单位移至缺陷 inventory。
* `RETURN_TO_SELLER`：将单位退回给卖家。
* `DISPOSE`：处置单位。 |
   ^is_sioc |bool |N |false |商品是否在 SIOC 管理下的标志 |
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
   ^^is_liquid |bool |N |false |商品是否为液体 |
   ^^is_sharp |bool |N |false |是否尖锐 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202607/goods/create_goods?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"create_goods_dto_list":[{"tts_sku_id":"723456789012345678","create_goods_type":"CREATE_AND_BIND","goods_name":"Wireless Charging Cable","goods_image_url":"https://example.com/fbt/goods-image.jpg","reference_code":"ABDK999d","barcode_infos":[{"barcode_type":"UPC","barcode_value":"12345678905"}],"return_handling_method":"RESTOCK_SELLABLE_DISPOSE_UNSELLABLE","dimension_and_weight_base_info":{"weight_value":"500","length_value":"2","width_value":"2","height_value":"3","weight_unit":"GRAM","dimension_unit":"CENTIMETER"},"is_hazmat":false,"hazmat_info":{"hazmat_type":"BATTERY","battery_extra_info":{"battery_type":"LITHIUM_ION","battery_packaging_type":"STANDALONE","total_battery_weight":"10","total_battery_weight_unit":"GRAM","total_battery_capacity":"2","total_battery_capacity_unit":"WATTHOUR","is_need_un_38_3_test":false,"un_38_3_test_file_url":"https://example.com/fbt/un38-3-test-report.pdf","battery_count_per_package":"3"},"flammable_liquids_extra_info":{"flammable_liquids_type":"PAINT","flammable_liquids_volume":"1","volume_unit":"MILLILITERS"},"dg_class":"CLASS_2","dg_uncode":"UN3480","msds_file_url":"https://example.com/fbt/msds-report.pdf","aerosol_extra_info":{"volume":"1","volume_unit":"MILLILITERS"}},"is_lot_code":false,"is_expiration_management":false,"shelf_life_attribute_info":{"shelf_life":90,"inbound_cutoff_days":100,"expiration_alert_days":90,"sales_cutoff_days":80,"handling_method_expired_goods":"DISPOSE"},"is_sioc":false,"sioc_attribute":{"sioc_files":[{"sioc_certification_url":"https://example.com/fbt/sioc-certification.jpg","sioc_file_type":"PHOTO"}]},"bulky_item_attribute":{"is_bulky_item_accessories":false},"goods_safety_attributes":{"is_fragile":false,"is_liquid":false,"is_sharp":false}}]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^create_result_info | object |  | 商品创建结果信息。 |
| ^^create_result_list | []object |  | 商品创建结果列表。 |
| ^^^tts_sku_id | string | 723456789012345678 | TikTok Shop 系统生成的 SKU 标识符。 |
| ^^^is_success | bool | false | 商品创建是否成功。 |
| ^^^tts_goods_id | string | 9988776655 | FBT 商品记录的标识符。当 is_success 为 true 时返回。 |
| ^^^fail_reason | string | Goods creation failed. | 商品记录未被创建的原因。当 is_success 为 false 时返回。 |
# 响应示例
```json
{"code":0,"data":{"create_result_info":{"create_result_list":[{"tts_sku_id":"723456789012345678","is_success":false,"tts_goods_id":"9988776655","fail_reason":"Goods creation failed."}]}},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
