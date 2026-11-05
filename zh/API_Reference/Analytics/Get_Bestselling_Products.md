# 获取畅销商品

# Path: /analytics/202511/products/bestselling
# Method: [GET]
# 功能描述
返回目标日期范围内按 GMV 排名的最多 100 个商品。

---


# 公共参数
公共参数请参考 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此参数在请求 API 时传递店铺信息。跨境店铺请求 API 时未传递正确值将返回错误的响应。 |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | 允许类型: application/json |
# 请求查询参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有唯一的 key。请使用分配给您的应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_id | string | N | 12334 | 按一级类目 ID 筛选商品。 |
| date | string | Y | 2025-11-13 | 查询期的截止日期（含），格式为 ISO 8601 YYYY-MM-DD，使用店铺注册的时区。该周期跨越所选 time_slot 并以此日期结束（例如 7D 查询以此日期结束的七天数据）。该日期必须不晚于最新可用日期。如果请求使用更晚的日期，错误响应将标识最新可用日期；请使用该日期或更早的日期重试。 |
| time_slot | string | Y | 7D | 以 date 结尾的查询周期长度。支持的值有： |

* 1D — 1 天
* 7D — 7 天
* 30D — 30 天 |
   currency |string |N |USD |货币单位。使用 USD 表示美元，使用 LOCAL 表示店铺注册地的当地货币。默认值：LOCAL。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202511/products/bestselling?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&category_id=12334&date=2025-11-13&time_slot=7D&currency=USD
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^products | []object |  | 目标日期范围内按 GMV 排名的畅销商品记录列表。 |
| ^^rank | int | 1 | 商品的 GMV 排名。 |
| ^^gmv_range | string | $97000.00~$191000.00 | 商品的 GMV 范围，使用 currency 指定的货币单位。 |
| ^^id | string | 123456 | 商品 ID |
| ^^name | string | Labubu | 商品名称 |
| ^^rating | string | 4.5 | 商品历史评分 |
| ^^product_image | object |  | 商品图片信息，包括 URI、URL、缩略图 URL、高度和宽度。 |
| ^^^height | int | 2000 | 图片高度。 |
| 单位：px |  |  |  |
| ^^^width | int | 2000 | 图片宽度。 |
| 单位：px |  |  |  |
| ^^^thumb_urls | []string | ["tos-useast5-i-omjb5zjo8w-tx/cad4b7c7409f459a87c54baf31ff8a20"] | 查看图片缩略图的 URL。 |
| ^^^uri | string | tos-useast5-i-omjb5zjo8w-tx/cad4b7c7409f459a87c54baf31ff8a20 | 图片的 URI。 |
| ^^^urls | []string | ["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/157d5bf9ac5a4af5855a2284626605c8~tplv-o3syd03w52-origin-jpeg.jpeg"] | 查看图片的 URL。 |
| ^^shop_name | string | Nia Batik | TikTok Shop 名称。 |
| ^^shop_id | string | 7028916274713380866 | 与商品关联的 TikTok Shop 的 ID。 |
# 响应示例
```json
{"code":0,"data":{"products":[{"rank":1,"gmv_range":"$97000.00~$191000.00","id":"123456","name":"Labubu","rating":"4.5","product_image":{"height":2000,"width":2000,"thumb_urls":["tos-useast5-i-omjb5zjo8w-tx/cad4b7c7409f459a87c54baf31ff8a20"],"uri":"tos-useast5-i-omjb5zjo8w-tx/cad4b7c7409f459a87c54baf31ff8a20","urls":["https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/157d5bf9ac5a4af5855a2284626605c8~tplv-o3syd03w52-origin-jpeg.jpeg"]},"shop_name":"Nia Batik","shop_id":"7028916274713380866"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
常见错误码请参考 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

