# 概述

Webhook 为 TikTok Shop 事件提供实时 HTTPS 通知。店铺订阅 webhook 主题后，当订阅的事件发生时，TikTok Shop 会向应用注册的回调 URL 发送 HTTP `POST` 请求。
不要将 webhook 作为唯一的数据来源。网络故障、端点停机、重试或延迟送达都可能发生，因此您的系统还应通过定时 API 轮询来核对关键业务状态。
# Webhook 投递机制
下图展示了订单状态 webhook 流程。其他 webhook 主题适用相同的投递模式。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/33f8046e84ec4c6f9946d446020184da~tplv-k9wyc2ijk0-image.image)

1. 应用为店铺订阅 webhook 主题，例如 `ORDER_STATUS_CHANGE`。
2. 应用注册一个由应用服务器托管的 HTTPS 端点。
3. 店铺中发生匹配的业务事件，例如新订单或订单状态更新。
4. TikTok Shop 将事件发布到订阅的 webhook 主题。
5. TikTok Shop 向注册的端点发送包含特定主题 payload 的 webhook 请求。

# Webhook 主题快速参考
在使用 webhook API 或 Partner Center 配置店铺 webhook 时使用 `event_type` 值。投递的 payload 还包含一个数字 `type` 字段。共享的 Event API 模式发布了完整的 `event_type` 枚举，但不为每个主题发布完整的数字 `type` 映射。不要仅根据数字 `type` 进行分支处理；请使用订阅的 `event_type` 上下文和特定主题的 payload 模式。
| Webhook 主题 | `event_type` 值 | Payload `type` 值 | 触发场景 |
| --- | --- | --- | --- |
| 订单状态变更 | `ORDER_STATUS_CHANGE` | 示例 payload 中为 `1`；请以主题页面的生产逻辑为准 | 订单创建或订单状态变更时。 |
| 收件地址更新 | `RECIPIENT_ADDRESS_UPDATE` | 参见特定主题的 payload 参考 | 订单的收件地址被更新时。 |
| 包裹更新 | `PACKAGE_UPDATE` | 参见特定主题的 payload 参考 | 包裹被更新时，例如合并、拆分或因地址更新而变更。 |
| 商品状态变更 | `PRODUCT_STATUS_CHANGE` | 参见特定主题的 payload 参考 | 商品审核结果更新时。 |
| 卖家取消授权 | `SELLER_DEAUTHORIZATION` | 参见特定主题的 payload 参考 | 撤销或失去对应用的授权。使用此事件停止对该店铺的 API 调用并清理本地连接状态。 |
| 即将到期的授权 | `UPCOMING_AUTHORIZATION_EXPIRATION` | 参见特定主题的 payload 参考 | 卖家授权即将到期。TikTok Shop 在到期前 30 天发送此事件，然后每天 00:00 发送直到重新授权完成。 |
| 取消状态变更 | `CANCELLATION_STATUS_CHANGE` | 参见特定主题的 payload 参考 | 订单取消状态变更时。 |
| 退货状态变更 | `RETURN_STATUS_CHANGE` | 参见特定主题的 payload 参考 | 订单退货状态变更时。 |
| 新会话 | `NEW_CONVERSATION` | 参见特定主题的 payload 参考 | 客服代理加入或离开会话时。 |
| 新消息 | `NEW_MESSAGE` | 参见特定主题的 payload 参考 | 客服会话中发送新消息时。 |
| 商品信息变更 | `PRODUCT_INFORMATION_CHANGE` | 参见特定主题的 payload 参考 | 商品标题、描述、主图或属性的变更生效时。 |
| 商品创建 | `PRODUCT_CREATION` | 参见特定主题的 payload 参考 | 新商品被创建时。 |
| 商品类目变更 | `PRODUCT_CATEGORY_CHANGE` | 参见特定主题的 payload 参考 | 商品类目被变更时。 |
| 新消息监听器 | `NEW_MESSAGE_LISTENER` | 参见特定主题的 payload 参考 | 达人向卖家发送消息时。 |
| 发票状态变更 | `INVOICE_STATUS_CHANGE` | 参见特定主题的 payload 参考 | 使用上传发票端点后，发票上传状态变更时。 |
| 商品审核状态变更 | `PRODUCT_AUDIT_STATUS_CHANGE` | 参见特定主题的 payload 参考 | 商品审核状态变更时。 |
| 逆向状态更新 | `REVERSE_STATUS_UPDATE` | 参见特定主题的 payload 参考 | 买家发起需要卖家操作的取消、仅退款或退货退款请求时。 |
对于店铺连接生命周期处理，当您的应用需要维护长期店铺访问时，请同时订阅 `UPCOMING_AUTHORIZATION_EXPIRATION` 和 `SELLER_DEAUTHORIZATION`。
# 配置 Webhook
您可以在 Partner Center 中或通过 Event API 配置店铺 webhook。
在 Partner Center 中，打开应用或服务，进入 webhook 或事件订阅设置：
```Plain Text
Partner Center
  -> App & Service
  -> 选择应用或服务
  -> Webhooks / Event subscriptions
  -> 添加或更新主题和回调 URL
```

控制台标签可能因 Partner Center 版本而异。所需配置是 webhook 主题（由 `event_type` 表示）和由您的应用控制的 HTTPS 回调 URL。
要通过 API 配置 webhook，请调用 **Update Shop Webhook**：
```HTTP
PUT https://open-api.tiktokglobalshop.com/event/202309/webhooks?app_key={app_key}&timestamp={timestamp}&sign={sign}&shop_cipher={shop_cipher}
Content-Type: application/json
x-tts-access-token: {access_token}

{
  "address": "https://example.com/tiktok-shop/webhooks",
  "event_type": "ORDER_STATUS_CHANGE"
}
```

使用 **Get Shop Webhooks** 查看店铺当前配置的 webhook 主题和回调 URL。仅在您有意要移除主题订阅时使用 **Delete Shop Webhook**。
# 请求头与签名验证
TikTok Shop 在 HTTP `Authorization` 头中发送 webhook 签名。值为小写的十六进制 HMAC-SHA256 摘要。它不是 bearer token，不应包含 `Bearer` 前缀。
签名计算方式如下：
```Plain Text
signature_base_string = app_key + raw_request_body
signature = HMAC-SHA256(signature_base_string, app_secret)
```

重要验证规则：
| 规则 | 重要性 |
| --- | --- |
| 使用接收到的原始请求体。 | 重新序列化 JSON、排序键、更改空格或更改编码都会产生不同的签名。 |
| 在解析或修改请求体之前计算签名。 | 某些 Web 框架在 JSON 解析过程中会消费或规范化请求体。请保存原始请求体用于验证。 |
| 使用恒定时间比较来对比签名。 | 这可以避免基于时间的比较泄漏。 |
| 拒绝缺失或不匹配的签名。 | 当 `Authorization` 头缺失或无效时，不应处理该请求。 |

可重现的示例：

1. App key：

```Plain Text
abcdef
```


2. 原始请求体：

```JSON
{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}
```


3. 签名字符串：

```Plain Text
abcdef{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}
```


4. App secret：

```Plain Text
123
```


5. HMAC-SHA256 结果：

```Plain Text
5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05
```

伪代码：
```JavaScript
const crypto = require("crypto");

function verifyWebhookSignature({ appKey, appSecret, rawBody, authorization }) {
  const base = appKey + rawBody;
  // 使用 app_secret 计算 HMAC-SHA256 签名
  const expected = crypto
    .createHmac("sha256", appSecret)
    .update(base, "utf8")
    .digest("hex");

  const expectedBuffer = Buffer.from(expected, "utf8");
  const receivedBuffer = Buffer.from(authorization || "", "utf8");

  // 使用恒定时间比较防止时序攻击
  return (
    expectedBuffer.length === receivedBuffer.length &&
    crypto.timingSafeEqual(expectedBuffer, receivedBuffer)
  );
}
```

# Body 参数
所有 webhook 通知包含通用元数据和特定主题的 `data` 对象。
| 参数名 | 示例 | 描述 |
| --- | --- | --- |
| `type` | `1` | 投递 payload 中的数字通知类型。不要将其与配置 webhook 订阅时使用的 `event_type` 字符串混淆。 |
| `tts_notification_id` | `7380066284010030890` | 唯一的 TikTok Shop 通知 ID。存在时存储此值用于幂等性和重复事件处理。 |
| `shop_id` | `7495540735365777507` | 与事件关联的 TikTok Shop ID。使用它将 webhook 映射到本地店铺连接。 |
| `timestamp` | `1718305585` | Unix 时间戳（秒），表示通知推送的时间。 |
| `data` | `{"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}` | 特定主题的业务 payload。字段取决于 webhook 主题。 |
# 请求示例
以下示例请求使用可重现示例中展示的相同原始请求体和签名。
```Bash
curl --location --request POST 'https://example.com/tiktok-shop/webhooks' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: 5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05' \
  --data-raw '{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}'
```

# 建议的监听器行为
| 场景 | 建议行为 |
| --- | --- |
| 签名有效且 `shop_id` 已知 | 处理事件，更新本地状态，并快速响应成功状态。 |
| 重复的 `tts_notification_id` | 将事件视为幂等，避免创建重复的业务记录。 |
| 未知的 `shop_id` | 记录事件并调查本地店铺映射是否缺失或过期。 |
| 收到 `SELLER_DEAUTHORIZATION` | 将店铺连接标记为非活跃，停止对该店铺的卖家范围 API 调用，并在仍需访问时要求卖家重新授权。 |
| 收到 `UPCOMING_AUTHORIZATION_EXPIRATION` | 通知卖家并在访问到期前引导其完成重新授权。 |
| Webhook 投递失败或延迟 | 通过定时 API 轮询核对关键资源，如订单、包裹、商品、退货和取消。 |
# 相关参考

* [Get Shop Webhooks](https://partner.tiktokshop.com/docv2/page/get-shop-webhooks)
* [Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook)
* [Delete Shop Webhook](https://partner.tiktokshop.com/docv2/page/delete-shop-webhook)
* [Order Status Change webhook](https://partner.tiktokshop.com/docv2/page/order-status-change)
* [Seller deauthorization webhook](https://partner.tiktokshop.com/docv2/page/65095746defece02be4d749d)
* [Upcoming authorization expiration webhook](https://partner.tiktokshop.com/docv2/page/6509579c0fcef602bf11312c)
* [Reauthorize shops](https://partner.tiktokshop.com/docv2/page/reauthorize-shops)
* [Disconnecting shops](https://partner.tiktokshop.com/docv2/page/disconnecting-shops)
