# 获取活动 Product 的达人 Performance

# 路径：/affiliate_partner/202508/campaigns/{campaign_id}/products/{product_id}/performance
# 方法：[GET]
# 功能描述
返回与 affiliate 合作伙伴活动中商品关联的达人分页列表，以及可用的合作和 performance 详情，如佣金、免费样品状态、粉丝数量、视频和直播场次。

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
| page_size | int | N | 10 | 每页返回的结果数量。有效范围：1-50。 |
| page_token | string | N | cGFnZV9udW1iZXI9Mg== | 用于获取分页结果集下一页的不透明 token。从上一次响应的 `next_page_token` 结果中获取此值。第一页不需要此参数。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_partner/202508/campaigns/{campaign_id}/products/{product_id}/performance?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&category_asset_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&page_size=10&page_token=cGFnZV9udW1iZXI9Mg==
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^total_creator_count | int | 1 | 该活动中指定商品跨所有页面关联的达人总数。 |
| ^promotion_creators | []object |  | 表示与商品推广关联的 Affiliate 达人信息的对象列表。 |
| ^^paid_amount | object |  | 表示该商品支付总额的对象。 |
| ^^^currency | string | USD | amount 字段的货币代码。 |
| ^^^amount | string | 3.00 | 该商品的支付总额。 |
| ^^room_count | int | 1 | 与该推广关联的直播间数量。 |
| ^^video_count | int | 1 | 达人发布的与该推广关联的视频总数。 |
| ^^free_sample_status | string | AWAITING_COLLECTION | 达人样品申请的状态。 |

* NOT_REQUESTED
* PENDING
* AWAITING_SHIPMENT
* AWAITING_COLLECTION
* SHIPPED
* CONTENT_PENDING
* REJECT_CANCELLED
* OVERDUE_CANCELLED
* UNFULFIL_CANCELLED
* DEL_PLAN_CANCELLED
* SELLER_NOT_SHIP_CANCELLED
* WITHDRAW_CANCELLED
* UNFULFILLABLE_CANCELLED
* OPERATOR_MANUAL_CANCELLED
* OPERATOR_MANUAL_FAILED
* OPERATOR_MANUAL_COMPLETED
* COMPLETED |
   ^^佣金 |string |100 |佣金率，以百分之一的百分比（0.01%）为单位。例如，值 1000 表示 10.00%。 |
   ^^effective_end_time |string |1731020040687 |合作的有效性结束时间，为 Unix 时间戳格式。 |
   ^^effective_start_time |string |1731019880391 |合作的有效性开始时间，为 Unix 时间戳格式。 |
   ^^达人 |object | |表示与推广关联的达人信息的对象。 |
   ^^^nick_name |string |Test_Creator_E |达人的 TikTok 昵称。 |
   ^^^avatar_url |string |https://p19-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/c614d3b6ba4d93b31fbda5add0802dd7~c5_1080x1080.webp?lk3s=a5d48078&nonce=6796&refresh_token=634d776ec39c2291053675f60c576515&x-expires=1736478000&x-signature=0G6NmM8H8nDRYYVN7e8QazDMRb0%3D&shp=a5d48078&shcp=9f007bb8 |TikTok CDN 中达人头像图片的 URL。 |
   ^^^follower_num |int |19 |达人的 TikTok 粉丝总数。 |
   ^^^user_name |string |us_lxq6213 |达人的 TikTok 用户名。 |
   ^^^creator_open_id |string |uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg |达人 Open ID。更多详情：https://partner.tiktokshop.com/docv2/page/3obfokj6 |
   ^^affiliate_product_id |string |123456789 |affiliate product 标识符。 |
   ^next_page_token |string |cGFnZV9udW1iZXI9Mg== |用于获取下一页的不透明 token。当此值非空时，将其作为下一次请求中的 `page_token` 查询参数传入，并复用相同的 `campaign_id`、`product_id` 和 `page_size`。空 token 表示没有更多结果。 |

# 响应示例
```json
{"code":0,"data":{"total_creator_count":1,"promotion_creators":[{"paid_amount":{"currency":"USD","amount":"3.00"},"room_count":1,"video_count":1,"free_sample_status":"AWAITING_COLLECTION","commission":"100","effective_end_time":"1731020040687","effective_start_time":"1731019880391","creator":{"nick_name":"Test_Creator_E","avatar_url":"https://p19-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/c614d3b6ba4d93b31fbda5add0802dd7~c5_1080x1080.webp?lk3s=a5d48078\u0026nonce=6796\u0026refresh_token=634d776ec39c2291053675f60c576515\u0026x-expires=1736478000\u0026x-signature=0G6NmM8H8nDRYYVN7e8QazDMRb0%3D\u0026shp=a5d48078\u0026shcp=9f007bb8","follower_num":19,"user_name":"us_lxq6213","creator_open_id":"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"},"affiliate_product_id":"123456789"}],"next_page_token":"cGFnZV9udW1iZXI9Mg=="},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [如何调用 TikTok Shop API - 通用 Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |

