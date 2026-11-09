# 批量生成发布者分享链接

# 路径：/affiliate_creator/202504/affiliate_sharing_links/publisher/{publisher_id}/generate_batch
# 方法：[POST]
# 功能描述
您可以使用此接口为特定发布者生成素材分享链接。之后，可将该链接分享给该发布者。目前，素材类型必须为 `PRODUCT`。
请使用 [Generate Multi Affiliate Partner Campaign Product Links](generate-multi-affiliate-partner-campaign-product-links) 确保该素材已包含在活动中。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| publisher_id | string | Y | publisher_id_in_your_sys | 合作伙伴系统中的推广者 ID |
# 请求 Query 参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的密钥。请使用分配给您的应用的特定密钥。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以使用此时间戳转换为本地时间。 |
# 请求体参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| material | object | Y |  | 为其生成分享链接的实体。 |
| ^ids | []string | Y | ["7362840009596339971","7362840009596339923"] | 素材 ID 列表。最大长度为 50。当 `type` 为 `PRODUCT` 时，需提供 1 到 50 个商品 ID。 |
| ^type | string | Y | PRODUCT | The material type. 可能的值： |

* `PRODUCT`: 在 `ids` 中提供商品 ID。
* `CAMPAIGN`: Provide `promotion_campaign_schema`. |
   ^promotion_campaign_schema |string |N |https://www.tiktok.com/t/ZSxRC4FEL/ |当 `type` 设为 `CAMPAIGN` 时，此字段为必填。此 schema 与活动页面关联。 |
   campaign_id |string |N |7432840009596339923 |如果达人从活动中添加商品，请包含活动 ID。活动 ID 可在 Affiliate Center 中找到，或使用 Get Affiliate Partner 活动 List API 获取。 |
   link_type |string |N |TOKO |控制当 `material.type` 为 `PRODUCT` 时返回的 `sharing_link`。
* 对于 Tokopedia 商品 URL, 请设置为 `TOKO`. 此选项适用于 Tokopedia 代理机构。
* 对于 TikTok Shop 商品 URL, 请省略此字段。 |

# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202504/affiliate_sharing_links/publisher/publisher_id_in_your_sys/generate_batch?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"material":{"ids":["7362840009596339971","7362840009596339923"],"type":"PRODUCT","promotion_campaign_schema":"https://www.tiktok.com/t/ZSxRC4FEL/"},"campaign_id":"7432840009596339923","link_type":"TOKO "}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sharing_links | []object |  | 为路径中指定的推广者所成功处理的素材生成的联盟分享链接。 |
| ^^material_id | int | 7362840009596339971 | 素材 ID。 |
| ^^sharing_link | string | https://www.tiktok.com/t/AIxvOHlaJoKO | 这是机构可分享给已协作推广者的商品推广链接。推广者可自行发布此链接。 |
| ^^deep_link | string | snssdk1180://ec/pdp?biz_type=0&enter_method=web&gd_label=click_wap_p_product_detail_t_launch_pop_up_s__e__f__fp__fps_affiliate_links_rf_&h5_start_ts=1768977752558&is_commerce=1&jump_time=1768977752558&mall_extra_info=%7B%22mall_out_source%22%3A%22seo.web_product_detail.out_of_app%22%2C%22mall_landing_page%22%3A%22product_detail%22%2C%22mall_homepage_visited_type%22%3A2%7D&media_source=channelshareh5&need_mall=1&needlaunchlog=1&o_app_code=abcsadaadada&page_name=reflow_pdp&page_name=product_detail&params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522merge%2522%252C%2522data%2522%253A%257B%2522channel%2522%253A%255B%2522benefit_hub%2522%255D%257D%252C%2522is_sticky%2522%253A1%257D%26touch_point_product_id%3D1730831248044885504%26trackParams%3D%257B%2522enter_from_info%2522%253A%2522product_share_outside%2522%252C%2522source_page_type%2522%253A%2522product_share%2522%252C%2522enable_shop_tab_popup%2522%253A1%257D%26utm_source%3Dopen_api&previous_page=deeplink_ug_seo_outside_gg_product_detail_link_web&refer=web&requestParams=%7B%22product_id%22%3A%5B%221730831248044885504%22%5D%7D&scene=pdp&trackParams=%7B%22enter_from_info%22%3A%22product_share_outside%22%2C%22source_page_type%22%3A%22product_share%22%2C%22enable_shop_tab_popup%22%3A1%7D&traffic_diversion_info=%7B%22traffic_out_source%22%3A%22affiliate_links%22%2C%22page_name%22%3A%22product_detail%22%7D&ug_media_source=deeplink_ug_seo_outside_gg_product_detail_link_web&ug_medium=fe_component&utm_source=open_api&wid=7506871187759580673 | 打开对应 TikTok Shop 商品详情页的商品推广深度链接。代理机构可将此链接分享给已协作的达人，达人可将其复制/粘贴到网页浏览器中（或分享给用户）。 |
| 如果用户通过此链接下单，生成的电商订单将携带这些参数值用于跟踪。 |  |  |  |
| ^^one_link | string | https://snssdk1180.onelink.me/BAuo?params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522merge%2522%252C%2522data%2522%253A%257B%2522channel%2522%253A%255B%2522benefit_hub%2522%255D%257D%252C%2522is_sticky%2522%253A1%257D%26touch_point_product_id%3D1730831248044885504%26trackParams%3D%257B%2522enter_from_info%2522%253A%2522product_share_outside%2522%252C%2522source_page_type%2522%253A%2522product_share%2522%252C%2522enable_shop_tab_popup%2522%253A1%257D%26utm_source%3Dopen_api |  |
| 打开对应 TikTok Shop 商品详情页的商品推广一键链接。代理机构可将此链接分享给已协作的达人，达人可将其复制/粘贴到网页浏览器中（或分享给用户）。 |  |  |  |
| 如果用户通过此链接下单，生成的电商订单将携带这些参数值用于跟踪。 |  |  |  |
| 如果用户手机上未安装 TikTok, 将被重定向到应用店铺安装 TikTok。 |  |  |  |
| ^failed_materials | []object |  | 生成分享链接失败的素材列表。 |
| ^^material_id | string | 7362840009596339923 | 素材 ID。 |
| ^^fail_reason | string | The product was sold out | 失败原因。 |
# 响应示例
```json
{"code":0,"data":{"sharing_links":[{"material_id":7362840009596339971,"sharing_link":"https://www.tiktok.com/t/AIxvOHlaJoKO","deep_link":"snssdk1180://ec/pdp?biz_type=0\u0026enter_method=web\u0026gd_label=click_wap_p_product_detail_t_launch_pop_up_s__e__f__fp__fps_affiliate_links_rf_\u0026h5_start_ts=1768977752558\u0026is_commerce=1\u0026jump_time=1768977752558\u0026mall_extra_info=%7B%22mall_out_source%22%3A%22seo.web_product_detail.out_of_app%22%2C%22mall_landing_page%22%3A%22product_detail%22%2C%22mall_homepage_visited_type%22%3A2%7D\u0026media_source=channelshareh5\u0026need_mall=1\u0026needlaunchlog=1\u0026o_app_code=abcsadaadada\u0026page_name=reflow_pdp\u0026page_name=product_detail\u0026params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522merge%2522%252C%2522data%2522%253A%257B%2522channel%2522%253A%255B%2522benefit_hub%2522%255D%257D%252C%2522is_sticky%2522%253A1%257D%26touch_point_product_id%3D1730831248044885504%26trackParams%3D%257B%2522enter_from_info%2522%253A%2522product_share_outside%2522%252C%2522source_page_type%2522%253A%2522product_share%2522%252C%2522enable_shop_tab_popup%2522%253A1%257D%26utm_source%3Dopen_api\u0026previous_page=deeplink_ug_seo_outside_gg_product_detail_link_web\u0026refer=web\u0026requestParams=%7B%22product_id%22%3A%5B%221730831248044885504%22%5D%7D\u0026scene=pdp\u0026trackParams=%7B%22enter_from_info%22%3A%22product_share_outside%22%2C%22source_page_type%22%3A%22product_share%22%2C%22enable_shop_tab_popup%22%3A1%7D\u0026traffic_diversion_info=%7B%22traffic_out_source%22%3A%22affiliate_links%22%2C%22page_name%22%3A%22product_detail%22%7D\u0026ug_media_source=deeplink_ug_seo_outside_gg_product_detail_link_web\u0026ug_medium=fe_component\u0026utm_source=open_api\u0026wid=7506871187759580673","one_link":"https://snssdk1180.onelink.me/BAuo?params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522merge%2522%252C%2522data%2522%253A%257B%2522channel%2522%253A%255B%2522benefit_hub%2522%255D%257D%252C%2522is_sticky%2522%253A1%257D%26touch_point_product_id%3D1730831248044885504%26trackParams%3D%257B%2522enter_from_info%2522%253A%2522product_share_outside%2522%252C%2522source_page_type%2522%253A%2522product_share%2522%252C%2522enable_shop_tab_popup%2522%253A1%257D%26utm_source%3Dopen_api\n"}],"failed_materials":[{"material_id":"7362840009596339923","fail_reason":"The product was sold out"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

