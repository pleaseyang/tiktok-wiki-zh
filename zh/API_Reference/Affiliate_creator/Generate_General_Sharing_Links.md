# 生成通用分享链接

# 路径：/affiliate_creator/202505/affiliate_sharing_links/general_publishers/generate_batch
# 方法：[POST]
# 功能描述
您可以使用此接口为您的发布者生成素材分享链接。之后，可将分享链接与发布者 ID 等附加信息一起封装。目前，素材类型必须为 `PRODUCT`。
请确保已使用 [Generate Multi Affiliate Partner 活动 Product Links] 将该素材加入活动。

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
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
| ^ids | []string | Y | ["7362840009596339971","7362840009596339923"] | 材质 ID 列表. 对于 `PRODUCT` 请求，请提供 1 到 50 个商品 ID。 |
| ^type | string | Y | PRODUCT | 目前，唯一可能的取值为 `PRODUCT`。 |
| 当 `type` 为 `PRODUCT` 时，将商品 ID 用于 `ids`。 |  |  |  |  |
| ^promotion_campaign_schema | string | N | https://www.tiktok.com/t/ZSxRC4FEL/ | 当 type 设置为 CAMPAIGN 时，该字段为必填项。此 schema 与活动页面关联。 |
| campaign_id | string | N | 7332840009596339923 | 如果达人从活动中添加商品，请附上活动 ID。活动 ID 可在 Affiliate Center 中找到，或使用 Get Affiliate Partner 活动 List API 获取。 |
| link_type | string | N | TOKO | 可选。对于 Tokopedia 代理机构，请将此字段设为 `TOKO`。响应会在 `sharing_link` 中返回 Tokopedia 商品 URL，并省略 `deep_link` 和 `one_link`。 |
| 如果省略此字段或将其设为其他值，响应将在 `sharing_link` 中返回 TikTok Shop 商品 URL。对于 `PRODUCT` 请求，还会返回 `deep_link` 和 `one_link`。 |  |  |  |  |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/affiliate_creator/202505/affiliate_sharing_links/general_publishers/generate_batch?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

**Body**
```json
{"material":{"ids":["7362840009596339971","7362840009596339923"],"type":"PRODUCT","promotion_campaign_schema":"https://www.tiktok.com/t/ZSxRC4FEL/"},"campaign_id":"7332840009596339923","link_type":"TOKO"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^sharing_links | []object |  | 成功生成的分享链接。 |
| ^^material_id | string | 7362840009596339971 | 素材 ID。 |
| ^^sharing_link | string | https://www.tiktok.com/view/product/1730958349688804006?chain_key=%7B%22t%22%3A1%2C%22k%22%3A%22000000000000000007518161308526446350%22%2C%22sc%22%3A%22OPEN_API%22%7D&scene=pdp&utm_source=open_api&trackParams=%7B%22enter_from_info%22%3A%22product_share_outside%22%2C%22source_page_type%22%3A%22product_share%22%2C%22enable_shop_tab_popup%22%3A1%7D&share_app_id=1233 | 这是机构可分享给已协作达人的商品推广链接。达人可以将此链接复制/粘贴到网页浏览器中。 |
| 获得链接后，将以下请求参数及其对应值添加到链接 URL 的末尾。当用户使用此链接下单时，生成的电商订单将在其信息中携带这些参数： |  |  |  |

* event_id: 每次点击的唯一事件 id
* publisher_id: CJ 分配的唯一 publish_id
   最好具备
* publisher_name: 来自 CJ 发布商资料。
* device_type: 1-移动端，2-桌面端。
* device_id: 来自同一设备 ID 的点击可聚合为 UV。
* referrer_src: 用户进入当前分享链接之前所访问网页的 URL。 |
   ^^deep_link |string |snssdk1180://ec/pdp?biz_type=0&enter_method=web&gd_label=click_wap_p_product_detail_t_launch_pop_up_s__e__f__fp__fps_affiliate_links_rf_&h5_start_ts=1768977752558&is_commerce=1&jump_time=1768977752558&need_mall=1&needlaunchlog=1&o_app_code=abcsadaadada&page_name=reflow_pdp&page_name=product_detail&params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522
   |A product promotion app deep link that opens the corresponding TikTok Shop product detail page. It is returned for `PRODUCT` requests that use the TikTok Shop link type and is omitted when `link_type` is `TOKO`. Agencies can share this link with collaborated creators, and creators can share it with users. Use `one_link` for the HTTPS link that can be opened in a web browser.

要启用归因，请将返回的 `deep_link` URL 中的 `o_event_id` 占位符替换为开发者为每次点击生成的唯一 ID。请勿对返回的链接进行 URL 编码或 URL 解码。如果用户通过此链接下单，生成的电商订单将携带该事件 ID 用于跟踪。 |
^^one_link |string |https://snssdk1180.onelink.me/BAuo?params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522merge%2522%252C%2522data%2522%253A%257B%2522channel%2522%253A%255B%2522benefit_hub%2522%255D%257D%252C%2522is_sticky%2522%253A1%257D%26touch_point_product_id%3D1730831248044885504%26trackParams%3D%257B%2522enter_from_info%2522%253A%2522product_share_outside%2522%252C%2522source_page_type%2522%253A%2522product_share%2522%252C%2522enable_shop_tab_popup%2522%253A1%257D%26utm_source%3Dopen_api
|A product promotion one-link that opens the corresponding TikTok Shop product detail page. It is returned for `PRODUCT` requests that use the TikTok Shop link type and is omitted when `link_type` is `TOKO`. Agencies can share this link with collaborated creators, and creators can copy and paste it into a web browser or share it with users.
要启用归因，请将返回的 `one_link` URL 中的 `o_event_id` 占位符替换为开发者为每次点击生成的唯一 ID。请勿对返回的链接进行 URL 编码或 URL 解码。如果用户通过此链接下单，生成的电商订单将携带该事件 ID 用于跟踪。如果用户未安装 TikTok，该链接会将用户重定向到应用店铺以安装 TikTok。 |
^failed_materials |[]object | |生成分享链接失败的素材列表。 |
^^material_id |string |7362840009596339972 |素材 ID。 |
^^fail_reason |string |Product was sold out |Fail reason. |
# 响应示例
```json
{"code":0,"data":{"sharing_links":[{"material_id":"7362840009596339971","sharing_link":"https://www.tiktok.com/view/product/1730958349688804006?chain_key=%7B%22t%22%3A1%2C%22k%22%3A%22000000000000000007518161308526446350%22%2C%22sc%22%3A%22OPEN_API%22%7D\u0026scene=pdp\u0026utm_source=open_api\u0026trackParams=%7B%22enter_from_info%22%3A%22product_share_outside%22%2C%22source_page_type%22%3A%22product_share%22%2C%22enable_shop_tab_popup%22%3A1%7D\u0026share_app_id=1233","deep_link":"snssdk1180://ec/pdp?biz_type=0\u0026enter_method=web\u0026gd_label=click_wap_p_product_detail_t_launch_pop_up_s__e__f__fp__fps_affiliate_links_rf_\u0026h5_start_ts=1768977752558\u0026is_commerce=1\u0026jump_time=1768977752558\u0026need_mall=1\u0026needlaunchlog=1\u0026o_app_code=abcsadaadada\u0026page_name=reflow_pdp\u0026page_name=product_detail\u0026params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522\n","one_link":"https://snssdk1180.onelink.me/BAuo?params_url=https%3A%2F%2Fshop-id.tokopedia.com%2Fview%2Fproduct%2F1730831248044885504%3Fchain_key%3D%257B%2522event_id%2522%253A%2522o_event_id%2522%252C%2522k%2522%253A%2522000000000000000007596668298679682828%2522%252C%2522sc%2522%253A%2522OPEN_API%2522%252C%2522t%2522%253A1%257D%26div_media_source%3Daffiliate%26event_id%3Do_event_id%26landing_page_name%3Dproduct_detail%26landpage_form%3Dhalf%26page_name%3Dproduct_detail%26scene%3Dpdp%26share_app_id%3D1180%26sticky_diversion_config%3D%257B%2522merge_action%2522%253A%2522merge%2522%252C%2522data%2522%253A%257B%2522channel%2522%253A%255B%2522benefit_hub%2522%255D%257D%252C%2522is_sticky%2522%253A1%257D%26touch_point_product_id%3D1730831248044885504%26trackParams%3D%257B%2522enter_from_info%2522%253A%2522product_share_outside%2522%252C%2522source_page_type%2522%253A%2522product_share%2522%252C%2522enable_shop_tab_popup%2522%253A1%257D%26utm_source%3Dopen_api\n"}],"failed_materials":[{"material_id":"7362840009596339972","fail_reason":"Product was sold out"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |

