# 获取 Affiliate Partner 活动列表

# 路径：/affiliate_partner/202405/campaigns
# 方法：[GET]
# 功能描述
列出 affiliate 合作伙伴的活动列表，可按活动类别、参与状态和活动状态进行筛选。

---


# 通用参数
通用参数请参考 [如何调用 TikTok Shop API - 通用参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型: application/json |
| category_asset_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个 app 都有唯一的 key。请使用分配给您的 app 的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT (UTC+00:00)。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
| category_asset_cipher | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | API 请求中使用的合作伙伴标识符。通过 [Get Authorized Category Assets API](https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995) 获取此值。 |
| page_size | int | Y | 10 | 每页返回的活动数量。有效范围：1-100。 |
| page_token | string | N | b2Zmc2V0PTAK | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此参数。最大页面大小为 `100` 项。 |
| status | string | N | READY | 此参数为必填项。 |
| 活动状态。此状态为枚举类型，取值如下： |  |  |  | |

* `READY`
* `UPCOMING`
* `ONGOING`
* `CLOSED`
* `UNSPECIFIED` |
   type |string |N |MY_CAMPAIGNS |活动类型。此类型为枚举类型，取值如下：
* MY_CAMPAIGNS
* GS_SELLING_CAMPAIGNS
* SELLER_CAMPAIGNS
* EXCLUSIVE_TIKTOK_SHOP
   默认值为 MY_CAMPAIGNS。 |
   query_type_filter |string |N |DEFAULT |附加筛选条件，其有效值取决于 `type`：
* `SELLER_CAMPAIGNS`：`query_type_filter` 为必填项。设置为 `MARKETPLACE` 以包含合作伙伴尚未加入的活动，或设置为 `JOINED` 以仅包含合作伙伴已加入的活动。使用 `MARKETPLACE` 时，将 `status` 设置为 `UNSPECIFIED`。
* `EXCLUSIVE_TIKTOK_SHOP`：`query_type_filter` 为必填项。设置为 `AVAILABLE` 以包含合作伙伴有权加入的活动，或设置为 `JOINED` 以仅包含合作伙伴已加入的活动。对于任一值，将 `status` 设置为 `UNSPECIFIED`。
* `MY_CAMPAIGNS` 或 `GS_SELLING_CAMPAIGNS`：省略 `query_type_filter` 或将其设置为 `DEFAULT`。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202405/campaigns?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=10&page_token=b2Zmc2V0PTAK&status=READY&type=MY_CAMPAIGNS&query_type_filter=DEFAULT
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^campaigns | []object |  | 活动列表。 |
|  |  |  |  |
| ^^id | string | 7360590375814268715 | 活动标识符。 |
| ^^name | string | test | 活动名称。 |
| ^^status | string | READY | 活动状态。此状态为枚举类型，取值如下： |

* READY
* UPCOMING
* ONGOING
* CLOSED |
   ^^registration_start_time |int |1712941200 |计划的卖家商品注册开始时间，为 Unix 时间戳格式。请注意，此字段仅在活动状态设置为 `READY` 或 `UPCOMING` 时可以更新。 |
   ^^registration_end_time |int |1713891599 |计划的卖家商品注册结束时间，为 Unix 时间戳格式。当活动状态设置为 `CLOSED` 时，此字段不再可编辑。 |
   ^^campaign_start_time |int |1712941200 |计划的活动开始时间，为 Unix 时间戳格式。请注意，此字段仅在活动状态设置为 `READY` 或 `UPCOMING` 时可以更新。 |
   ^^campaign_end_time |int |1715878799 |计划的活动结束时间，为 Unix 时间戳格式。请注意，结束时间必须距开始日期少于 360 天。当活动状态设置为 `CLOSED` 时，此字段不再可编辑。 |
   ^next_page_token |string |cGFnZV9udW1iZXI9Mg== |用于获取分页结果集下一页的不透明 token。对于第一次请求，省略 `page_token` 或传入空值。对于后续每次请求，传入上一次响应中非空的 `next_page_token` 作为 `page_token`，并保持相同的 `category_asset_cipher`、`page_size`、`status`、`type` 和 `query_type_filter` 值，包括每个Optional参数是否被省略或提供。如果 `next_page_token` 为空，则表示没有更多页面可用。 |
   ^total_count |int |1570 |列表中的活动总数。 |

# 响应示例
```json
{"code":0,"data":{"campaigns":[{"id":"7360590375814268715","name":"test","status":"READY","registration_start_time":1712941200,"registration_end_time":1713891599,"campaign_start_time":1712941200,"campaign_end_time":1715878799}],"next_page_token":"cGFnZV9udW1iZXI9Mg==","total_count":1570},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 16032001 | nvalid parameter Creator and Seller, please ensure Region mismatch. |
| 16032007 | Permission denied |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

