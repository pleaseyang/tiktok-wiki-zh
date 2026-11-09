# 获取仓库列表

# 路径：/logistics/202309/warehouses
# 方法：[GET]
# 功能描述
获取与卖家关联的仓库信息，包括名称、生效状态、类型、默认标识以及可用的地址信息。

---


# 公共参数
公共参数详情请参考 [如何调用 TikTok Shop APIs - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 参数 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 用于在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求 Query 参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 参数描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以使用此转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/logistics/202309/warehouses?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

# 响应参数
| 参数 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 参数描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^warehouses | []object |  | 为卖家返回的仓库列表。当结果中没有仓库时，此字段将被省略。 |
| ^^id | string | 7000714532876273410 | 仓库 ID，唯一且不可变的主键，用于所有仓库 logistics。 |
| ^^entity_id | string | 7395366865142499073 | 仓库实体 ID，用于关联仓库的物理信息，不同仓库可能关联到同一实体。 |
| ^^name | string | Guangzhou | 仓库名称。此名称在 TikTok Shop 系统中不唯一。 |
| ^^effect_status | string | ENABLED | 表示仓库中的库存是否可供销售。 |
| 可能的值： |  |  |  |

* `ENABLED`：所有库存商品均可销售。
* `DISABLED`：所有库存商品均不可销售。
* `RESTRICTED`：仓库处于假期模式或订单限制模式，因此所有库存商品均不可销售。

卖家可以在 Seller Center 中启用假期模式，当卖家无法从该仓库履行订单时。当 TikTok Shop 因政策违规而限制仓库可履行的订单量时，将应用订单限制模式。 |
^^type |string |SALES_WAREHOUSE |可能的值：

* SALES_WAREHOUSE：用于发货的仓库。
* RETURN_WAREHOUSE：用于接收退货的仓库。
   您可以将同一仓库同时用于发货和接收退货，但它们将具有不同的仓库 ID 和相同的地址。 |
   ^^sub_type |string |DOMESTIC_WAREHOUSE |可能的值：
* DOMESTIC_WAREHOUSE：仓库与目标市场和卖家在同一国家。
* CB_OVERSEA_WAREHOUSE：对于跨境卖家，位于目标市场的本地仓库。
* CB_DIRECT_SHIPPING_WAREHOUSE：对于跨境卖家，位于卖家所在国的仓库，例如中国大陆或香港。 |
   ^^is_default |bool |true |默认仓库。如果商品上架时未指定仓库，将使用默认仓库。 |
   ^^address |object | |仓库地址。 |
   ^^^region |string |China |仓库地址的国家或地区。 |
   ^^^state |string |GuangDong |仓库所在的州或省。 |
   ^^^city |string |GuanZhou |仓库所在城市。 |
   ^^^distict |string |HuaDu |仓库所在区。 |
   ^^^town |string |town |仓库所在镇。 |
   ^^^contact_person |string |Lee |仓库联系人姓名。 |
   ^^^first_name |string |新一 |汉字名（姓）
   仅适用于 JP 市场。 |
   ^^^last_name |string |工藤 |汉字姓（名）
   仅适用于 JP 市场。 |
   ^^^first_name_local_script |string |しんいち |平假名或片假名名
   仅适用于 JP 市场。 |
   ^^^last_name_local_script |string |くどう |平假名或片假名姓
   仅适用于 JP 市场。 |
   ^^^postal_code |string |510000 |仓库地址邮政编码（也称为 zip code） |
   ^^^full_address |string |South Sea 11 floor |组合仓库地址，包括街道地址和其他地址信息，如公寓号、楼栋、楼层等（可选） |
   ^^^region_code |string |CN |仓库地址的国家或地区代码。 |
   ^^^phone_number |string |188****2234 |仓库电话号码。 |
   ^^^address_line1 |string |Bairro/Distrito |仓库地址的第一行，如街道名称和门牌号。
   注意：
* 对于巴西市场，这代表社区或区。
* 对于 JP 市场，这代表区（Chome）、番地（Banchi）、楼栋号（Go）。 |
   ^^^address_line2 |string |Caminho Trinta e Três |仓库地址的第二行，如单元号、公寓号或套房号。
   注意：对于巴西市场，这代表街道名称。 |
   ^^^address_line3 |string |3 |门牌号。字面值 `s/n` 表示没有门牌号。仅适用于巴西市场。 |
   ^^^address_line4 |string |11 floor |补充信息，如单元号、公寓号或套房号（可选）。
   注意：仅适用于巴西市场。 |
   ^^^geolocation |object | |地址的地理位置。 |
   ^^^^latitude |string |45.41634 |地址的纬度。 |
   ^^^^longitude |string |-75.6868 |地址的经度。 |

# 响应示例
```json
{"code":0,"data":{"warehouses":[{"id":"7000714532876273410","entity_id":"7395366865142499073","name":"Guangzhou","effect_status":"ENABLED","type":"SALES_WAREHOUSE","sub_type":"DOMESTIC_WAREHOUSE","is_default":true,"address":{"region":"China","state":"GuangDong","city":"GuanZhou","distict":"HuaDu","town":"town","contact_person":"Lee","first_name":"新一","last_name":"工藤","first_name_local_script":"しんいち","last_name_local_script":"くどう","postal_code":"510000","full_address":"South Sea 11 floor","region_code":"CN","phone_number":"188****2234","address_line1":"Bairro/Distrito","address_line2":"Caminho Trinta e Três","address_line3":"3","address_line4":"11 floor","geolocation":{"latitude":"45.41634","longitude":"-75.6868"}}}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
公共错误码详情请参考 [如何调用 TikTok Shop APIs - 公共错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 错误信息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
