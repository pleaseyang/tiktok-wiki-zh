# 搜索商品信息

# Path: /fbt/202607/goods/search
# Method: [POST]
# 功能描述
检索属于商家且匹配指定筛选条件的商品，并返回其 ID、名称、商品-SKU 关系、商家申报的尺寸、warehouse 确认的尺寸和其他属性。当提供 `goods_ids`、`product_ids`、`reference_codes` 和 `sku_ids` 中的多个时，API 仅返回匹配所有提供的筛选字段的商品。如果所有四个筛选条件都为空或省略，API 按创建时间降序返回商家的商品，受 `page_size` 限制。

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
| page_size | int | Y | 50 | 每页返回的结果数量。 |
| 有效范围：[1-100]。 |  |  |  |  |
| page_token | string | N | cGFnZV9udW1iZXI9Mg== | 用于检索分页结果集下一页的不透明 token。从上一个响应的 `next_page_token` 结果中获取此值。第一页不需要此值。 |
| app_key | string | Y | 38abcd | 每个 app 都有一个唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | string | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求 Body 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| goods_ids | []string | N | ["256080616234"] | 用于筛选结果的 Fulfilled by TikTok 商品 ID。每个 ID 必须为正十进制字符串。每次请求最多 100 个 ID。 |
| product_ids | []string | N | ["256990616123"] | 用于筛选结果的 TikTok Shop 产品 ID。每个 ID 必须为正十进制字符串。每次请求最多 100 个 ID。 |
| reference_codes | []string | N | ["SELLERSKU 123456"] | 用于筛选结果的商家定义商品参考代码。每次请求最多 100 个代码。 |
| sku_ids | []string | N | ["256086568895"] | 用于筛选结果的 TikTok Shop SKU ID。每个 ID 必须为正十进制字符串。每次请求最多 100 个 ID。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fbt/202607/goods/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=50&page_token=cGFnZV9udW1iZXI9Mg==
```

**Body**
```json
{"goods_ids":["256080616234"],"product_ids":["256990616123"],"reference_codes":["SELLERSKU 123456"],"sku_ids":["256086568895"]}
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^next_page_token | string | cGFnZV9udW1iZXI9Mg== | 用于检索下一页的不透明 token。当此值非空时，在下一个请求的 `page_token` 中原样传递。空字符串表示没有更多页面。 |
| ^total_count | int | 123 | 满足查询条件的商品总数。 |
| ^goods | []object |  | Fulfilled by TikTok 商品的详细信息列表。 |
| ^^id | string | 86533997569 | Fulfilled by TikTok 系统生成的商品标识符。 |
| ^^name | string | water1.0 | 商品名称。 |
| ^^barcodes | []object |  | 商品条形码的详细信息列表。 |
| ^^^code | string | 014673829105 | 商品的可打印条形码。 |
| ^^^type | string | UPC | 条形码类型。 |
| Possible values: |  |  |  |

* UPC
* EAN
* GTIN
* ASIN_OR_FNSKU
* MERCHANT_SKU_ID
* FBT_SPECIFIC_BARCODE |
   ^^reference_code |string |abc32323 |商家定义的商品标识符。 |
   ^^image_url |string |https://example.com/fbt/goods-image.jpg |商品图片 URL。 |
   ^^merchant_declaration_info |object | |商家输入的尺寸和重量信息。 |
   ^^^weight |object | |商品重量。 |
   ^^^^value |string |1.122 |重量值，最多三位小数。 |
   ^^^^unit |string |GRAM |重量单位。
   Possible values:
* MILLIGRAM
* GRAM
* KILOGRAM
* POUND
* OUNCE |
   ^^^dimension |object | |商品尺寸。 |
   ^^^^width |string |1.122 |宽度值，最多三位小数。 |
   ^^^^length |string |2.122 |长度值，最多三位小数。 |
   ^^^^height |string |3.122 |高度值，最多三位小数。 |
   ^^^^unit |string |CENTIMETER |尺寸单位。
   Possible values:
* MILLIMETER
* CENTIMETER
* METER
* FOOT
* INCH
* MICROMETER |
   ^^warehouse_confirmation_info |object | |warehouse 在商品首次 inbound 时验证的尺寸和重量信息。仅当至少有一个 warehouse 确认的重量、长度、宽度或高度值可用时返回。如果省略此对象，则此响应中没有 warehouse 确认的测量值。 |
   ^^^weight |object | |商品重量。 |
   ^^^^value |string |1 |warehouse 验证的重量值，最多三位小数。 |
   ^^^^unit |string |GRAM |重量单位。
   Possible values:
* MILLIGRAM
* GRAM
* KILOGRAM
* POUND
* OUNCE |
   ^^^dimension |object | |商品尺寸。 |
   ^^^^width |string |1 |warehouse 验证的宽度值，最多三位小数。 |
   ^^^^length |string |2.5 |warehouse 验证的长度值，最多三位小数。 |
   ^^^^height |string |3 |warehouse 验证的高度值，最多三位小数。 |
   ^^^^unit |string |CENTIMETER |尺寸单位。
   Possible values:
* MILLIMETER
* CENTIMETER
* METER
* FOOT
* INCH
* MICRO |
   ^^skus |[]object | |与当前 FBT 商品匹配的 Stock Keeping Units（SKU）信息列表。 |
   ^^^id |string |1729439634328225260 |TikTok Shop 系统生成的 SKU 标识符。 |
   ^^^name |string |Testcase SKU |SKU 名称。 |
   ^^^image_url |string |https://example.com/fbt/sku-image.jpg |TikTok Shop SKU 图片 URL。 |
   ^^^product |object | |与当前 Fulfilled by TikTok 商品匹配的 TikTok Shop 产品。 |
   ^^^^id |string |1729439631253210604 |TikTok Shop 系统生成的产品标识符。 |
   ^^^^name |string |Testcase_xd2.0_test_goods |TikTok Shop 产品名称。 |
   ^^^^image_url |string |https://example.com/fbt/product-image.jpg |TikTok Shop 产品图片 URL。 |
   ^^^regions |[]string |["US"] |SKU 正在销售的区域，以两位字符的 ISO 3166-1 alpha-2 格式的区域代码表示。 |
   ^^^matched |bool |true |表示 SKU 已与当前 Fulfilled by TikTok 商品匹配。`skus` 中的条目为已匹配关系，因此此值始终为 `true`。 |
   ^^lot_expiration_info |object | |商品的批次控制和保质期管理信息。 |
   ^^^is_lot_control |bool |true |表示商品是否受批次控制的标志。
   True: 受批次控制。
   False: 不受批次控制。
   注意：根据 Fulfilled by TikTok 指南，批次码和保质期管理信息对这些[产品类别](https://bytedance.us.larkoffice.com/sheets/OoT2sKH7jhykXCtHEseuzkGYsod)是强制性的。 |
   ^^^is_expiration_management |bool |true |表示商品是否受保质期管理的标志。
   True: 受保质期管理。
   False: 不受保质期管理。 |
   ^^^shelf_life_days |int |12 |商家输入的商品保质期天数，表示产品从制造到过期之间可使用的总天数。 |
   ^^^inbound_cutoff_days |int |90 |商品过期前的 inbound 截止天数，表示在产品过期前 warehouse 不再接受 inbound 货件的时间段。 |
   ^^^expiration_alert_days |int |60 |商品过期前的预警天数，表示平台向商家发送过期提醒警报的时间段。 |
   ^^^sales_cutoff_days |int |20 |商品过期前的销售截止天数，表示在过期前商品不再可供销售的时间段。 |
   ^^^handling_method |string |DISPOSE |过期 inventory 的处理方式。
   Possible values:
* `STORE_UNITS`：将单位移至缺陷 inventory。
* `RETURN_TO_SELLER`：将单位退回给卖家。
* `DISPOSE`：处置单位。 |
   ^^is_hazmat |bool |false |是否为危险品商品 |
   ^^hazmat_info |object | |危险品详情。仅在 `is_hazmat` 为 `true` 时返回。子类型对象取决于 `hazmat_type`：`BATTERY` 对应 `battery_extra_info`，`FLAMMABLE_LIQUID` 对应 `flammable_liquids_extra_info`，`AEROSOLS` 对应 `aerosol_extra_info`。`MAGNETIZED` 不包含子类型对象。 |
   ^^^hazmat_type |string |MAGNETIZED |危险品类型
   Possible values:
   -MAGNETIZED
   -BATTERY
   -FLAMMABLE_LIQUID
   -AEROSOLS |
   ^^^battery_extra_info |object | |危险品的附加电池信息。 |
   ^^^^battery_type |string |LITHIUM_ION |电池类型
   Possible values:
   LITHIUM_ION
   LITHIUM_METAL
   OTHER |
   ^^^^battery_packaging_type |string |STANDALONE |电池包装类型。
   Possible values:
* STANDALONE
* IN_EQUIPMENT
* WITH_EQUIPMENT
* OTHER |
   ^^^^total_battery_weight |string |1 |以 total_battery_weight_unit 指定单位表示的总电池重量。 |
   ^^^^total_battery_weight_unit |string |GRAM |total_battery_weight 的单位。可能的值：GRAM。 |
   ^^^^total_battery_capacity |string |1 |Total battery capacity in the unit specified by total_battery_capacity_unit. |
   ^^^^battery_count_per_package |string |2 |每个包装的电池数量 |
   ^^^^is_need_un_38_3_test |bool |false |UN38.3 测试确保电池符合特定的安全标准。如果报告中未包含在 MSDS 中，请在此字段中发送报告。 |
   ^^^^un_38_3_test_file_url |string |https://example.com/fbt/msds-report.pdf |UN38.3 测试文件 URL |
   ^^^^total_battery_capacity_unit |string |WATT_HOURS |`total_battery_capacity` 的单位，如 `WATT_HOURS`。 |
   ^^^flammable_liquids_extra_info |object | |易燃液体信息 |
   ^^^^flammable_liquids_type |string |PAINT |易燃液体类型，可能的值
   -PAINT
   -PERFUMERY
   -ALCOHOLIC
   -OTHER |
   ^^^^flammable_liquids_volume |string |1 |以 volume_unit 指定单位表示的易燃液体体积。 |
   ^^^^volume_unit |string |MILLILITER |`flammable_liquids_volume` 的单位，如 `MILLILITER`。 |
   ^^^aerosol_extra_info |object | |aerosol info |
   ^^^^volume |string |1 |气雾剂体积 |
   ^^^^volume_unit |string |MILLILITER |气雾剂体积 unit |
   ^^^dg_class |string |CLASS_2
   |危险品等级
   Possible values:
   -CLASS_2
   -CLASS_3
   -CLASS_9 |
   ^^^dg_uncode |string |UN1266 |危险物质的 UN 标识符。标准 UN 值使用 `UN` 前缀加四位数字；也支持 `OTHER`。
   Possible values:
* UN2807
* UN3480
* UN3090
* UN3481
* UN3091
* UN1263
* UN1266
* UN3065
* OTHER |
   ^^^msds_file_url |string |https://example.com/fbt/msds-report.pdf |危险品的材料安全数据表，用于支持在 FBT 中审核商品的安全合规性 |
   ^^sioc_approval_status |string |SIOC_APPROVAL_STATUS_APPROVE |SIOC 特定的审批状态。当 `is_sioc` 为 `true` 且 SIOC 审批状态可用时返回此字段。
   Possible values:
* SIOC_APPROVAL_STATUS_INVALID
* SIOC_APPROVAL_STATUS_INIT
* SIOC_APPROVAL_STATUS_UNDER_REVIEW
* SIOC_APPROVAL_STATUS_APPROVE
* SIOC_APPROVAL_STATUS_REJECT |
   ^^hazmat_approval_status |string |APPROVAL_STATUS_UNDER_REVIEW |FBT 履约审批状态。此字段针对危险品或作为 Ships in Own Container（SIOC）管理的商品返回。
   Possible values:
* APPROVAL_STATUS_INVALID
* APPROVAL_STATUS_INIT
* APPROVAL_STATUS_UNDER_REVIEW
* APPROVAL_STATUS_FULFILLABLE
* APPROVAL_STATUS_UNFULFILLABLE |
   ^^bulky_item_attribute |object | |大件商品信息 |
   ^^^is_bulky_item |bool |false |商品是否为大件商品 |
   ^^^is_bulky_item_accessories |bool |false |商品是否为大件配件 |
   ^^goods_safety_attributes |object | |安全属性信息 |
   ^^^is_fragile |bool |false |是否易碎 |
   ^^^is_liquid |bool |false |是否液体 |
   ^^^is_sharp |bool |false |是否尖锐 |
   ^^is_sioc |bool |false |是否 SIOC |
   ^^sioc_attribute |object | |SIOC 信息 |
   ^^^sioc_files |[]object | |SIOC 文件 |
   ^^^^sioc_certification_url |string |https://example.com/fbt/sioc-certification.jpg |SIOC 附件 URL |
   ^^^^sioc_file_type |string |PHOTO |SIOC 附件类型：
* PHOTO
* DOCUMENT
* DROP_TEST_VIDEO |

# 响应示例
```json
{"code":0,"data":{"next_page_token":"cGFnZV9udW1iZXI9Mg==","total_count":123,"goods":[{"id":"86533997569","name":"water1.0","barcodes":[{"code":"014673829105","type":"UPC"}],"reference_code":"abc32323","image_url":"https://example.com/fbt/goods-image.jpg","merchant_declaration_info":{"weight":{"value":"1.122","unit":"GRAM"},"dimension":{"width":"1.122","length":"2.122","height":"3.122","unit":"CENTIMETER"}},"warehouse_confirmation_info":{"weight":{"value":"1","unit":"GRAM"},"dimension":{"width":"1","length":"2.5","height":"3","unit":"CENTIMETER"}},"skus":[{"id":"1729439634328225260","name":"Testcase SKU","image_url":"https://example.com/fbt/sku-image.jpg","product":{"id":"1729439631253210604","name":"Testcase_xd2.0_test_goods","image_url":"https://example.com/fbt/product-image.jpg"},"regions":["US"],"matched":true}],"lot_expiration_info":{"is_lot_control":true,"is_expiration_management":true,"shelf_life_days":12,"inbound_cutoff_days":90,"expiration_alert_days":60,"sales_cutoff_days":20,"handling_method":"DISPOSE"},"is_hazmat":false,"hazmat_info":{"hazmat_type":"MAGNETIZED","battery_extra_info":{"battery_type":"LITHIUM_ION","battery_packaging_type":"STANDALONE","total_battery_weight":"1","total_battery_weight_unit":"GRAM","total_battery_capacity":"1","battery_count_per_package":"2","is_need_un_38_3_test":false,"un_38_3_test_file_url":"https://example.com/fbt/msds-report.pdf","total_battery_capacity_unit":"WATT_HOURS"},"flammable_liquids_extra_info":{"flammable_liquids_type":"PAINT","flammable_liquids_volume":"1","volume_unit":"MILLILITER"},"aerosol_extra_info":{"volume":"1","volume_unit":"MILLILITER"},"dg_class":"CLASS_2\n","dg_uncode":"UN1266","msds_file_url":"https://example.com/fbt/msds-report.pdf"},"sioc_approval_status":"SIOC_APPROVAL_STATUS_APPROVE","hazmat_approval_status":"APPROVAL_STATUS_UNDER_REVIEW","bulky_item_attribute":{"is_bulky_item":false,"is_bulky_item_accessories":false},"goods_safety_attributes":{"is_fragile":false,"is_liquid":false,"is_sharp":false},"is_sioc":false,"sioc_attribute":{"sioc_files":[{"sioc_certification_url":"https://example.com/fbt/sioc-certification.jpg","sioc_file_type":"PHOTO"}]}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

