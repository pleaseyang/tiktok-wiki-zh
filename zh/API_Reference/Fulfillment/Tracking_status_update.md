# 物流状态更新

# 路径：/fulfillment/202609/order/sof/track/update
# 方法：[POST]
# 功能描述
**此接口目前仅适用于以下市场: US, BR.**
此接口适用于卖家自行配送和承运订单，不通过第三方服务商发货，即不通过 3PL 寄送包裹，而是卖家自行发货的订单。卖家可使用此接口回传此类订单并更新订单轨迹。入参中的 Action Code 和 Failed Reason 为枚举值，详见文档: https://partner.tiktokshop.com/docv2/page/1cjht3qx

---


# 通用参数
通用参数请参考 [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 字段 <!-- width:110px --> | 位置 <!-- width:75px --> | 类型 <!-- width:75px --> | 必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | 使用此属性在请求 API 时传递店铺信息。在请求跨境店铺的 API 时，如果未传递正确的值，将返回错误的响应。 |
| 通过 API 获取 [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
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
| country | string | Y | BR | Order Country. |
| order_id | string | Y | 577071607420326620 | TikTok Shop 订单 ID。 |
| external_tracking_url | string | N | https://www.correios.com.br/rastreamento/BR3PL202609090001 | 服务商的追踪 URL / 官网链接。 |
| tracks | []object | Y |  | 轨迹节点数组；单次请求最多 [50] 条，处理结果在数组内逐条返回。也就是说，在接口中一次最多可为每个订单回传 50 条轨迹。 |
| ^action_code | int | Y | 20201 | 标准轨迹节点代码必须属于允许名单。参见下方 action code。action code 有限，可用枚举列表请参阅文档: https://partner.tiktokshop.com/docv2/page/1cjht3qx |
| ^occur_time | int | Y | 1788920100000 | 实际轨迹发生时间。Unix 时间戳 GMT (UTC+00:00)。单位为毫秒。 |
| ^description | string | Y | 包裹已由 3PL 承运商揽收 | 调用方的原始轨迹描述。 |
| ^failed_reason | string | N | R110 | 异常原因，详情如下。参见下方 reason code。reason code 有限，可用枚举列表请参阅文档: https://partner.tiktokshop.com/docv2/page/1cjht3qx |
| ^proof_url | string | N | https://carrier-proof.example.com/proof/BR3PL202609090001 | 第三方追踪凭证链接或凭据。 |
| ^location | object | N |  | 城市、州、省、国家、纬度和经度等位置字段； |
| ^^country | string | N | BR | country. |
| ^^state | string | N | SP | state. |
| ^^city | string | N | Campinas | city. |
| ^^zip_code | string | N | 13010-000 | 邮政编码/邮编。 |
| ^tracking_no | string | Y | BR443310090002 | 下单时使用的运单号。如无追踪码，请填写 invoice id 代替。在拆单发货场景下，该值可能变化，也可能因不同物流轨迹而变化。 |
| provider_id | string | Y | 7189579428429563650 | 物流服务商 ID，即下单或上传运单号时填写的 ID，必须与其一致。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/fulfillment/202609/order/sof/track/update?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY
```

**Body**
```json
{"country":"BR","order_id":"577071607420326620","external_tracking_url":"https://www.correios.com.br/rastreamento/BR3PL202609090001","tracks":[{"action_code":20201,"occur_time":1788920100000,"description":"Package picked up by 3PL carrier","failed_reason":"R110","proof_url":"https://carrier-proof.example.com/proof/BR3PL202609090001","location":{"country":"BR","state":"SP","city":"Campinas","zip_code":"13010-000"},"tracking_no":"BR443310090002"}],"provider_id":"7189579428429563650"}
```

# 响应参数
| 字段 <!-- width:110px --> | 类型 <!-- width:90px --> | 示例 <!-- width:289px --> | 描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中描述。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^track_results | []object |  | 轨迹节点数组，数组中每个元素的字段表示它是哪条轨迹。`code` 和 `message` 字段描述该轨迹是否已接收；若未接收，则表示相应的错误码和错误描述。 |
| ^^action_code | int | 32401 | 标准轨迹节点码必须属于白名单。参见下方动作码。 |
| ^^occur_time | int | 1788920100012 | 实际轨迹发生时间。Unix 时间戳 GMT (UTC+00:00)。单位为毫秒。 |
| ^^description | string | 干线运输已发车 | 调用方的原始轨迹描述。 |
| ^^code | int | 0 | 此 action code 对应轨迹的成功或失败状态，参见下方错误码 |
| ^^message | string | Success | 该动作码对应轨迹中返回的成功或失败消息。失败原因将在消息中说明。 |
| ^^tracking_no | string | BR123456789 | 下单时使用的运单号。如无追踪码，请填写 invoice id 代替。在拆单发货场景下，该值可能变化，也可能因不同物流轨迹而变化。 |
# 响应示例
```json
{"code":0,"data":{"track_results":[{"action_code":32401,"occur_time":1788920100012,"description":"Line-haul transport departed","code":0,"message":"Success","tracking_no":"BR123456789"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
通用错误码请参考 [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| 错误码 <!-- width:250px --> | 消息 <!-- width:553px --> |
| --- | --- |
| 36009003 | 内部错误。请重试。如果多次尝试后问题仍然存在，请联系平台支持。 |
| 11007010 | System is busy, please try again later. |
| 11007016 | The merchant is not in the merchant allowlist. |
| 11007017 | The action_code is not in the allowlist table. |
| 11007018 | The order cannot be located using the provided TrackingNO and OrderId. |
| 11007019 | The merchant in the request does not match the actual merchant of the order. |
| 11007020 | Invalid trajectory. Please check the parameters in tracks. |
| 11007021 | Invalid provider id. Please check whether the postback provider id you submitted is a provider id allowed under the merchant self-shipping and self-delivery method. |

