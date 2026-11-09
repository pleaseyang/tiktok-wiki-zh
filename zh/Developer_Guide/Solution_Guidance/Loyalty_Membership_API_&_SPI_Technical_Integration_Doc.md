# 忠诚会员 API 与 SPI 技术集成文档

# 背景与目标
本文档面向卖家和 ISV（独立软件供应商）集成开发团队。描述了将 TTS 与卖家忠诚会员系统集成所需的外部 Open API 和 SPI 接口。重点介绍接口方向、通用规则、请求/响应参数、错误码、幂等性要求、重试建议和时序图。本文档的目标是帮助开发者：

* 查询 TTS 端的会员数据进行对账和故障排查。
* 接收 TTS 通过卖家提供的 SPI 发起的会员绑定检查、绑定/注册和解绑通知。
* 一致使用 `buyer_id`、`merchant_member_id`、`idempotency_key` 和 `request_id` 等关键参数，使请求可追踪、可重试且幂等。

# 术语表
| **术语** | **描述** |
| --- | --- |
| TTS | TikTok Shop 平台。 |
| 卖家 / ISV | 卖家系统，或经授权的外部独立服务提供商。 |
| Buyer ID / `buyer_id` | TTS 端的全局唯一买家标识符，会员 API 中的主要用户标识符。 |
| 卖家会员 ID / `merchant_member_id` | 卖家会员系统中的唯一会员标识符。 |
| Open API | 卖家/ISV 调用 TTS 的 API。 |
| Open SPI | TTS 调用卖家端的 API。 |
# 端到端集成流程
此图展示了 Loyalty Membership MVP 计划上线后卖家/ISV 的端到端集成流程。
此图仅用于与现有 API/SPI 集成。如果第三方希望创建新的 API/SPI，则需要经过标准需求流程，包括字节跳动研发与第三方共同开发和测试。


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b0f336e14038440ba8a6787cdc24877b~tplv-k9wyc2ijk0-image.image)
# 时序图
以下时序图仅展示外部集成视图。参与者合并为三方：TT App、TTS 后端和卖家。我们不拆分卖家内部系统，也不暴露任何 TTS 内部域名、内部服务名称或实现细节。
## 会员绑定 / 注册
**注意**：在 TT App 和 TTS 后端之间，我们仅表示用户操作和页面结果，不包含具体请求参数。在 TTS 后端和卖家之间，我们保留 SPI 语义和关键字段，以便卖家理解需要实现的 `MembershipBindCheck` 和 `MembershipBind` 逻辑。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/11cf7b181fb8451f92d578c5d5f9b9c9~tplv-k9wyc2ijk0-image.image)
## 会员解绑

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a24423b6fb3544e3a6690a432c9be397~tplv-k9wyc2ijk0-image.image)
## 对账查询
**注意**：对账分为两个独立场景：第一，当卖家在订单事件中看到脱敏邮箱时，调用 `MemberInfoQuery` 查询 TTS 端会员信息；第二，卖家通过 `MemberProfileBatchUpdate` 将会员资料、等级或绑定状态批量同步到 TTS。
### MemberInfoQuery API：卖家查询 TTS 会员信息

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/78b94a872bc04acb855ce57a90eb7623~tplv-k9wyc2ijk0-image.image)
### MemberProfileBatchUpdate API：卖家批量更新 TTS 会员资料

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/785dcb88fba34792beb7c43a1471f3ab~tplv-k9wyc2ijk0-image.image)
# 集成范围
| 方向 | 接口 | 用途 |
| --- | --- | --- |
| 卖家 / ISV → TTS | **`MemberProfileBatchUpdate` API** | 批量更新多个会员的资料、等级或绑定状态。 |
| 卖家 / ISV → TTS <br/>  | **`MemberInfoQuery` API** <br/>  | 查询 TTS 端会员数据。当在订单事件中看到脱敏邮箱时，可用于查询会员信息。 |
| 卖家 / ISV → TTS | **`CreateCoupon`** **API** |  |
| 卖家 / ISV → TTS | **`DeactivateCoupon`** **API** |  |
| 卖家 / ISV → TTS | **`LoyaltyProgramInfoUpdate`** **API** |  |
| TTS → 卖家 / ISV | **`MembershipBindCheck` SPI** | 在绑定或注册之前，检查买家是否已是卖家会员。 |
| TTS → 卖家 / ISV | **`MembershipBind` SPI** <br/>  | 绑定现有会员，或注册并绑定新会员。 |
| TTS → 卖家 / ISV | **`MembershipUnbind` SPI** | 通知卖家会员关系已解绑。 |
| TTS → 卖家 / ISV | **`MemberPointsQuery` SPI** | 当用户查看会员页面时，实时查询当前总积分。 |
| TTS → 卖家 / ISV | **`MemberPointsTransactionQuery` SPI** <br/>  | 当用户查看积分明细页面时，分页查询积分交易记录。 |
| TTS → 卖家 / ISV | **`MembershipRedeem`** **SPI** |  |
| TTS → 卖家 / ISV | **`MembershipRedeemReverse`** **SPI** |  |
# 通用规则
## 标识符规则

* `buyer_id` 是 TTS 端的全局唯一买家标识符，应作为 TTS 会员 API 的主要用户标识符。
* `merchant_member_id` 是卖家会员系统中的会员标识符，应在卖家的会员计划中保持稳定。在同一卖家会员计划下的不同店铺之间应保持全局唯一。如果卖家使用集团级标识符或 `merchant_member_id` 在同一卖家会员计划下不全局唯一，卖家必须在集成设计阶段提出，以便在上线前对齐标识符粒度。

## `request_id` 和 `idempotency_key`

* `request_id` 在 API 响应中返回，作为日志查询、故障排查和重试处理的唯一追踪 ID；调用方不应在请求体中传递此参数。
* 写操作还应携带 `idempotency_key` 用于业务级幂等控制。
* 重试同一业务操作时，调用方必须复用相同的 `idempotency_key` 并保持请求体不变。
* 如果相同的 `idempotency_key` 使用了不同的请求体，接收方应返回幂等冲突错误。
* 只读 API 不使用 `idempotency_key`，但仍应返回 `request_id` 以便追踪。

## 通用 Open API 查询参数
| 参数 | 位置 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| `app_key` | Query | string | 是 | 应用创建后分配的 App Key。 |
| `timestamp` | Query | int64 | 是 | 用于签名生成和请求过期验证的 Unix 时间戳。 |
| `sign` | Query | string | 是 | 按开放平台签名算法生成的请求签名。 |
| `shop_cipher` | Query | string | 是 | 已授权店铺上下文标识符。 |
## 通用 Open API Headers
| Header | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `content-type` | string | 是 | 固定为 `application/json`。 |
| `x-tts-access-token` | string | 是 | 卖家授权 access token。 |
## 通用 Open API 响应信封
除非另有说明，API 返回以下顶层结构：
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `code` | int | `0` 表示成功；非 `0` 表示失败。 |
| `message` | string | 结果描述或错误信息。 |
| `request_id` | string | 唯一请求标识符，用于追踪和重试处理。 |
| `data` | object | 按 API 场景返回的业务响应数据。 |
# Open API 定义
## MemberProfileBatchUpdate API
**描述**：一次请求最多更新五个买家的会员数据。此操作支持批量订单处理、历史迁移和会员信息修正。每个条目携带独立的 `idempotency_key`；使用相同 key 和相同条目数据的重试应返回稳定结果，而使用相同 key 但不同条目数据应返回幂等冲突错误。
| 类型 | 值 |
| --- | --- |
| API 名称 | `member_profile_batch_update` |
| API 版本 | `202607` |
| Host / Scheme | `open-api.tiktokglobalshop.com` / HTTPS |
| API 路径 | `/customer_engagement/:version/member_profiles/partial_edit` |
| 方法 | `POST` |
### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `member_profiles` | array[object] | 是 | 会员资料更新。最多五个条目。每个条目独立处理，响应保留请求条目标识。 |
### member_profiles 条目
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TTS 端的唯一买家标识符。 |
| `idempotency_key` <br/>  | string | 是 | 此会员资料更新条目的唯一重试 key。使用相同 key 但不同条目数据返回 `IDEMPOTENCY_CONFLICT`。 |
| `bind_status` | string | 否 | 会员绑定状态。可能的值包括 `UNKNOWN`、`BOUND`、`UNBOUND` 和 `PENDING`。允许的状态转换包括 `UNKNOWN -> BOUND` 和 `BOUND <-> UNBOUND`。 |
| `merchant_member_id` | string | 否 | 卖家分配的会员标识符。 |
| `program_level_name` | string | 否 | 要设置的卖家忠诚计划等级名称，例如 `GOLD` 或 `SILVER`。 |
| `program_level_expire_time_ms` | int64 | 否 | 忠诚计划等级过期的 Unix 时间戳（毫秒）。 |
| `update_time_ms` | int64 | 否 | 卖家生成此资料更新的 Unix 时间戳（毫秒）。 |
**请求体示例：**
```JSON
{
  "member_profiles": [
    {
      "bind_status": "BOUND",
      "buyer_id": "7451234567890123456",
      "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
      "merchant_member_id": "MEMBER_10001",
      "program_level_expire_time_ms": 1798761600000,
      "program_level_name": "GOLD",
      "update_time_ms": 1785168000000
    }
  ]
}
```

### 响应参数（顶层）
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `code` | int32 | API 响应中返回的成功或失败状态码。 |
| `message` | string | 成功或失败消息。失败原因在消息中描述。 |
| `request_id` | string | 响应中返回的请求日志 ID，用于追踪和故障排查。 |
| `data` | object | 具体返回信息。 |
### data 对象
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `total_count` | int32 | 提交的会员资料更新总数。 |
| `success_count` | int32 | 成功的会员资料更新数量。 |
| `fail_count` | int32 | 失败的会员资料更新数量。 |
| `successes` | array[object] | 成功的会员资料更新结果。空结果返回空数组。 |
| `errors` | array[object] | 失败的会员资料更新结果。空结果返回空数组。 |
### successes 条目
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `buyer_id` | string | 对应请求条目中的唯一买家标识符。 |
| `idempotency_key` | string | 对应请求条目中的幂等 key。 |
| `merchant_member_id` | string | 对应请求条目中的卖家会员标识符。 |
### errors 条目
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `code` | string | 稳定的条目结果码。 |
| `message` | string | 更新失败时的人类可读条目结果及修正操作。 |
| `detail` | object | 失败请求条目的标识符，包括 `buyer_id`、`idempotency_key` 和 `merchant_member_id`。 |
**响应体示例：**
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "fail_count": 1,
    "errors": [
      {
        "code": "INTERNAL_ERROR",
        "detail": {
          "buyer_id": "7451234567890123456",
          "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
          "merchant_member_id": "MEMBER_10001"
        },
        "message": "INVALID_BUYER_ID"
      }
    ],
    "success_count": 1,
    "successes": [
      {
        "buyer_id": "7451234567890123456",
        "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
        "merchant_member_id": "MEMBER_10001"
      }
    ],
    "total_count": 2
  }
}
```

## MemberInfoQuery API
**描述**：一次请求最多查询 20 个 buyer ID 的会员资料数据。卖家和授权服务提供商可使用响应来核对会员身份、忠诚等级、积分和绑定状态。这是只读操作，不需要 `idempotency_key`。返回的邮箱受用户授权和平台数据保护策略约束。
| 类型 | 值 |
| --- | --- |
| API 名称 | `Query Member Information` |
| API 版本 | `202607` |
| Host / Scheme | `open-api.tiktokglobalshop.com` / HTTPS |
| API 路径 | `/customer_engagement/:version/member_profiles/search` |
| 方法 | `POST` |
### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_ids` | array[string] | 是 | 要查询会员信息的 Buyer ID。最多 20 个。 |
**请求体示例：**
```JSON
{
  "buyer_ids": [
    "7451234567890123456"
  ]
}
```

### 响应参数（顶层）
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `code` | int32 | API 响应中返回的成功或失败状态码。 |
| `message` | string | 成功或失败消息。失败原因在消息中描述。 |
| `request_id` | string | 响应中返回的请求日志 ID，用于追踪和故障排查。 |
| `data` | object | 具体返回信息。 |
### data 对象
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `member_profiles` | array[object] | 与提交的 buyer ID 匹配的会员资料。空结果返回空数组。 |
### member_profiles 条目
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `bind_status` | string | 会员绑定状态。可能的值包括 `UNKNOWN`、`BOUND`、`UNBOUND` 和 `PENDING`。 |
| `buyer_id` | string | 唯一买家标识符。 |
| `email` <br/>  | string | 仅在用户授权时返回的买家邮箱。邮箱可能根据平台数据保护策略进行脱敏处理。 |
| `merchant_member_id` | string | 卖家分配的会员标识符。 |
| `points` | int64 | 当前会员积分余额。 |
| `expiring_points` | int64 | 计划在 `points_expire_time_ms` 过期的会员积分。 |
| `points_expire_time_ms` | int64 | 即将过期的积分的过期 Unix 时间戳（毫秒）。 |
| `program_level_name` | string | 卖家忠诚计划等级名称。 |
| `update_time_ms` | int64 | 会员资料最后更新的 Unix 时间戳（毫秒）。 |
**响应体示例：**
```JSON
{
  "code": 0,
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7",
  "data": {
    "member_profiles": [
      {
        "bind_status": "BOUND",
        "buyer_id": "7451234567890123456",
        "email": "m***@example.com",
        "merchant_member_id": "MEMBER_10001",
        "points": 1250,
        "expiring_points": 200,
        "points_expire_time_ms": 1798761600000,
        "program_level_name": "GOLD",
        "update_time_ms": 1785168000000
      }
    ]
  }
}
```

## 创建会员优惠券 API
为已授权店铺创建全店会员优惠券，并配置领取所需积分。
### 基本信息
| 项目 | 值 |
| --- | --- |
| 路径 | `/customer_engagement/202609/membership/coupons` |
| 方法 | `POST` |
| 版本 | `202609` |
| 幂等性 | 必填查询参数 `idempotency_key`，UUID 格式。重试必须复用相同 key 和请求体。 |
此 API 使用**通用规则**中定义的通用查询参数和 headers。查询 `timestamp` 为 Unix 时间（秒）。`app_key`、`sign`、`timestamp` 和 `shop_cipher` 为必填项；`x-tts-access-token` 和 `Content-Type: application/json` 为必填 headers。
### 请求体参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | string | 是 | 卖家定义的优惠券标题。 |
| `claim_duration` | object | 是 | 买家可领取优惠券的时间段。 |
| `redemption_duration` | object | 是 | 已领取优惠券可兑换的时间段。 |
| `usage_limits` | object | 是 | 单买家和总领取数量限制。 |
| `discount` | object | 是 | 满减或折扣配置。 |
| `threshold` | object | 是 | 无门槛或最低消费要求。 |
| `points_required` | integer (int64) | 是 | 领取优惠券所需积分，非负整数。0 表示不扣积分。 |
#### claim_duration 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `start_time` | string (date-time) | 是 | 领取开始的 RFC 3339 时间。 <br/>  |
| `end_time` | string (date-time) | 是 | 领取结束的 RFC 3339 时间；必须晚于 start_time。 |
#### redemption_duration 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type` | string enum | 是 | `ABSOLUTE` 或 `RELATIVE`。 |
| `start_time` | string (date-time) | 条件必填 | `ABSOLUTE` 时必填；`RELATIVE` 时禁止。 |
| `end_time` | string (date-time) | 条件必填 | `ABSOLUTE` 时必填；`RELATIVE` 时禁止。 |
| `relative_duration_days` | integer (int32) | 条件必填 | `RELATIVE` 时必填；最小 1。`ABSOLUTE` 时禁止。 |
#### usage_limits 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `single_buyer_claim_limit` | integer (int32) | 是 | 每个买家的最大领取次数；最小 1。 |
| `total_claim_limit` | integer (int64) | 是 | 总最大领取次数；最小 1。 |
#### discount 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type` | string enum | 是 | `AMOUNT_OFF` 或 `PERCENT_OFF`。 |
| `reduction_amount` | string | 条件必填 | `AMOUNT_OFF` 时必填；店铺币种金额，如 5.00。 |
| `percentage` | string | 条件必填 | `PERCENT_OFF` 时必填；0 到 100 的十进制百分比。 |
| `max_discount` | string | 否 | `PERCENT_OFF` 的可选最大店铺币种折扣。 |
#### threshold 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type` | string enum | 是 | `NONE` 或 `MIN_SPEND`。 |
| `min_spend` | string | 条件必填 | `MIN_SPEND` 时必填；店铺币种金额。`NONE` 时省略。 |
### 请求示例
```JSON
{
  "title": "Gold Member Welcome Coupon",
  "claim_duration": {
    "start_time": "2026-10-01T00:00:00Z",
    "end_time": "2026-10-31T23:59:59Z"
  },
  "redemption_duration": {
    "type": "RELATIVE",
    "relative_duration_days": 30
  },
  "usage_limits": {
    "single_buyer_claim_limit": 1,
    "total_claim_limit": 10000
  },
  "discount": {
    "type": "AMOUNT_OFF",
    "reduction_amount": "5.00"
  },
  "threshold": {
    "type": "MIN_SPEND",
    "min_spend": "30.00"
  },
  "points_required": 500
}
```

### 响应 data 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `coupon_id` | string | 是 | 新创建的会员优惠券标识符。 |
| `status` | string enum | 是 | `NOT_START` 或 `ONGOING`。 |
### 业务规则

* 相对兑换期限以整天为单位计算。
* 金额字段为店铺币种的十进制字符串；不要发送二进制浮点值。
* 重试时复用相同的幂等 key 和相同请求体。

## 停用会员优惠券 API
停用已授权店铺拥有的会员优惠券。停用后的优惠券不能再被领取或兑换。
### 基本信息
| 项目 | 值 |
| --- | --- |
| 路径 | `/customer_engagement/202609/membership/coupons/{coupon_id}/deactivate` |
| 方法 | `POST` |
| 版本 | `202609` |
| 请求体 | 无 |
此 API 使用**通用规则**中定义的通用查询参数和 headers。查询 `timestamp` 为 Unix 时间（秒）。`app_key`、`sign`、`timestamp` 和 `shop_cipher` 为必填项；`x-tts-access-token` 和 `Content-Type: application/json` 为必填 headers。
### 路径参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `coupon_id` | string | 是 | 要停用的会员优惠券唯一标识符。 |
### 响应 data 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `coupon_id` | string | 是 | 已停用的优惠券标识符。 |
| `title` | string | 否 | 卖家定义的优惠券标题。 |
| `status` | string enum | 是 | 成功后始终为 `DEACTIVATED`。 |
### 业务规则

* 只能停用尚未开始或当前可领取的优惠券。
* 停用后将阻止后续的领取和兑换操作。

## 更新忠诚计划信息 API
更新已授权店铺的忠诚计划隐私政策链接、积分规则和展示权益。
### 基本信息
| 项目 | 值 |
| --- | --- |
| 路径 | `/customer_engagement/202609/loyalty_program/info/partial_edit` |
| 方法 | `POST` |
| 版本 | `202609` |
| 幂等性 | 必填查询参数 `idempotency_key`，UUID 格式。重试必须复用相同 key 和请求体。 |
此 API 使用**通用规则**中定义的通用查询参数和 headers。查询 `timestamp` 为 Unix 时间（秒）。`app_key`、`sign`、`timestamp` 和 `shop_cipher` 为必填项；`x-tts-access-token` 和 `Content-Type: application/json` 为必填 headers。
### 请求体参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `privacy_policy_links` | array&lt;object&gt; | 是 | 完整的有序隐私政策链接列表；1-3 个条目。 |
| `points_rules` | string | 是 | 完整的纯文本积分规则，最多 20,000 字符。不支持 HTML。 |
| `sign_up_bonus` | object | 否 | 仅展示的注册奖励；TikTok Shop 不发放积分。省略则保持当前设置。 |
| `earning_rule` | object | 否 | 仅展示的赚取规则；TikTok Shop 不计算或发放积分。省略则保持当前设置。 |
#### privacy_policy_links 条目
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | string | 是 | 展示标题，最多 100 字符。 |
| `url` | string (URI) | 是 | HTTPS URL，最多 2,048 字符。不得使用凭证、片段、localhost 或私有网络地址。 |
#### sign_up_bonus 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `is_enabled` | boolean | 是 | 是否展示注册奖励；`false` 隐藏。 |
| `points` | integer (int64) | 条件必填 | 加入时获得的整数积分；最小 1。`is_enabled` 为 `true` 时必填。 |
#### earning_rule 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `is_enabled` | boolean | 是 | 是否展示赚取权益；`false` 隐藏。 |
| `method` | string enum | 条件必填 | `PER_SPEND`：每 `spend_amount` 消费金额的积分。`PER_ORDER`：每笔订单的固定积分。`is_enabled` 为 `true` 时必填。 |
| `points` | integer (int64) | 条件必填 <br/>  | 每 `spend_amount` 或每笔订单的整数积分；最小 1。`is_enabled` 为 `true` 时必填。 |
| `spend_amount` | object | 条件必填 | `PER_SPEND` 时必填；`PER_ORDER` 时省略。 |
#### spend_amount 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `amount` | string | 是 | 十进制金额，例如 `"1.00"`。必须大于 0。 |
| `currency` | string | 是 | 三字母大写 ISO 4217 货币代码，例如 `USD`。必须与店铺币种匹配。 |
### 请求示例
```JSON
{
  "privacy_policy_links": [
    {
      "title": "Membership Privacy Policy",
      "url": "https://www.example.com/membership/privacy"
    }
  ],
  "points_rules": "Members earn one point for every eligible dollar spent.",
  "sign_up_bonus": {
    "is_enabled": true,
    "points": 100
  },
  "earning_rule": {
    "is_enabled": true,
    "method": "PER_SPEND",
    "points": 1,
    "spend_amount": {
      "amount": "1.00",
      "currency": "USD"
    }
  }
}
```

### 响应 data 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | string enum | 是 | `ACTIVE` 或 `PENDING_VALIDATION`。 |
### 业务规则

* 请求将替换完整的隐私政策链接列表和完整的积分规则文本。
* 隐私政策链接按请求数组顺序展示。
* 重试时复用相同的幂等 key 和相同请求体。
* `sign_up_bonus` 和 `earning_rule` 仅用于展示。TikTok Shop 不会据此发放或计算积分。
* 省略 `sign_up_bonus` 或 `earning_rule` 以保持当前设置。将 `is_enabled` 设为 `false` 以隐藏对应权益。
* 如果两项权益均被禁用或从未设置，则权益部分将被隐藏。


# Open SPI 定义
## MembershipBindCheck SPI
**SPI 码**：`MEMBERSHIP_BIND_CHECK` · **版本**：`202608`
**描述**：检查买家是否已有卖家会员。卖家通过隐私保护的邮箱 token 进行匹配，并返回脱敏的潜在匹配项供买家确认。
### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TikTok Shop 买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 编码后的 TikTok Shop 店铺标识符，1-128 字符。 |
| `tts_shop_id` | string <br/>  | 否 | 与请求关联的 TikTok Shop ID，1-64 字符。这不是 Shop OpenID。如果省略，卖家必须使用现有字段继续处理。 |
| `email_match_token` | string | 是 | 买家授权的脱敏邮箱，用于隐私保护匹配，3-320 字符。按可见字符匹配；这不是 HMAC 或认证 token，不得暴露完整邮箱地址。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `has_potential_matches` | boolean | 是 | 是否找到一个或多个潜在会员。`true` 需要 `potential_matches` 中至少一个条目；`false` 需要空数组。 |
| `potential_matches` | array&lt;object&gt; | 是 | 供买家确认的潜在会员。未找到匹配时返回空数组，而非 null。 |
### `potential_matches` 条目
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `masked_email` | string | 是 | 卖家端部分脱敏的邮箱，供买家识别，3-320 字符。不得包含完整邮箱地址。 |
| `merchant_member_id` | string | 是 | 稳定的卖家会员标识符，1-128 字符。 |
## MembershipBind SPI
**SPI 码**：`MEMBERSHIP_BIND` · **版本**：`202608`
**描述**：在买家授权后，关联现有卖家会员或注册并关联新会员。TikTok Shop 仅在收到 `BOUND` 结果后才记录关系。
如果会员已绑定，重复调用此 SPI 不应返回错误结果，而应返回最新的会员信息。

### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TikTok Shop 买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 编码后的 TikTok Shop 店铺标识符，1-128 字符。 |
| `tts_shop_id` | string | 否 | 与请求关联的 TikTok Shop ID，1-64 字符。这不是 Shop OpenID。如果省略，卖家必须使用现有字段继续处理。 |
| `bind_type` | string enum | 是 | `EXISTING_MEMBER` 或 `NEW_MEMBER`。 |
| `merchant_member_id` | string | 条件必填 | `EXISTING_MEMBER` 时必填，`NEW_MEMBER` 时禁止；1-128 字符。 |
| `user_profile` | object | 条件必填 | `NEW_MEMBER` 时可选，`EXISTING_MEMBER` 时禁止。该对象及每个属性均为可选，因为可用性取决于买家同意程度和资料完整性。视为个人数据，不得记录日志。 |
| `idempotency_key` | string (UUID) | 是 | 稳定操作 key。重试使用相同 key 和相同请求体并接收原始结果；使用相同 key 但不同业务输入必须作为调用方错误拒绝。 |
### `user_profile` 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `email` | string (email) | 否 | 买家授权的联系邮箱，最多 320 字符。 |
| `first_name` | string | 否 | 买家授权的名，1-128 字符。 |
| `last_name` | string | 否 | 买家授权的姓，1-128 字符。 |
| `phone_number` | string | 否 | 买家授权的联系电话号码，1-64 字符。 |
| `birth_date` | string (date) | 否 | 买家授权的出生日期，YYYY-MM-DD 格式。 |
| `full_name` | string | 否 | 买家授权的全名，1-256 字符。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `bind_status` | string enum | 是 | `BOUND` 或 `REJECTED`。 |
| `merchant_member_id` | string | 条件必填 | `BOUND` 时必填；`REJECTED` 时禁止；1-128 字符。 |
| `program_level` | object | 否 | `BOUND` 结果的卖家定义等级；`REJECTED` 时必须省略。如果存在，name 必填，expire_time 可选。 |
| `points` | integer (int64) | 否 | 绑定后的非负可用余额，包括欢迎积分；仅限 `BOUND`，`REJECTED` 时省略。 |
| `expiring_points` | integer (int64) | 否 | 计划过期的非负积分；仅限 `BOUND`，`REJECTED` 时省略。必须与 `points_expire_time` 同时出现。 |
| `points_expire_time` | integer (int64) | 否 | `expiring_points` 过期的 Unix 时间戳（毫秒）；仅限 `BOUND`，`REJECTED` 时省略。必须与 `expiring_points` 同时出现。 |
| `welcome_points` | integer (int64) | 否 | 新会员获得的非负欢迎积分；仅限 `BOUND`，`REJECTED` 时省略。 |
| `bind_time` | integer (int64) | 否 | 绑定完成的 Unix 时间戳（毫秒）；仅限 `BOUND`，`REJECTED` 时省略。 |
| `reason_code` | string enum | 条件必填 | `REJECTED` 时必填，`BOUND` 时禁止。可选值：`MEMBER_NOT_FOUND`、`REGISTRATION_REJECTED`、`MEMBER_CONFLICT`。 |
| `reason_message` | string | 否 | 人类可读的拒绝说明，最多 500 字符；仅限 `REJECTED`，`BOUND` 时省略。 |
### `program_level` 对象
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | string | 是 | 卖家定义的会员等级名称，最多 128 字符。 |
| `expire_time` | integer (int64) | 否 | 会员等级过期的 Unix 时间戳（毫秒）。 |
## MembershipUnbind SPI
**SPI 码**：`MEMBERSHIP_UNBIND` · **版本**：`202608`
**描述**：移除 TikTok Shop 到卖家会员的关联。不得终止底层的卖家会员关系。
### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TikTok Shop 买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 编码后的 TikTok Shop 店铺标识符，1-128 字符。 |
| `tts_shop_id` | string | 否 | 与请求关联的 TikTok Shop ID，1-64 字符。这不是 Shop OpenID。如果省略，卖家必须使用现有字段继续处理。 |
| `merchant_member_id` | string | 是 | 与买家关联的稳定卖家会员标识符，1-128 字符。 |
| `unbind_reason` | string enum | 是 | `USER_REQUEST` 或 `PLATFORM_REVOKE`。 |
| `idempotency_key` | string (UUID) | 是 | 稳定操作 key。重试使用相同 key 和相同请求体并重放原始结果；使用相同 key 但不同输入必须作为调用方错误拒绝。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `unbind_status` | string enum | 是 | 如果此操作移除了关联则为 `UNBOUND`；如果新操作未发现活跃关联则为 `ALREADY_UNBOUND`。重放现有 key 返回其原始结果。 |
| `unbind_time` | integer (int64) | 条件必填 | `UNBOUND` 时必填，`ALREADY_UNBOUND` 时省略；卖家移除关联的 Unix 时间戳（毫秒）。 |
## MemberPointsQuery SPI
**SPI 码**：`MEMBER_POINTS_QUERY` · **版本**：`202608`
**描述**：当前卖家会员积分余额的只读查询。卖家为数据权威来源；此 SPI 不使用 `idempotency_key`。
* 我们的系统会缓存会员积分，因此某些更新可能略有延迟。
* 此 SPI 应具有高可用性，因为它直接影响买家体验。

### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TikTok Shop 买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 编码后的 TikTok Shop 店铺标识符，1-128 字符。 |
| `tts_shop_id` | string | 否 | 与请求关联的 TikTok Shop ID，1-64 字符。这不是 Shop OpenID。如果省略，卖家必须使用现有字段继续处理。 |
| `merchant_member_id` | string | 是 | 要查询积分的稳定卖家会员标识符，1-128 字符。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `membership_status` | string enum | 是 | `BOUND` 或 `NOT_BOUND`。`NOT_BOUND` 时必须省略以下所有会员和积分字段。 |
| `merchant_member_id` | string | 条件必填 | `BOUND` 时必填；`NOT_BOUND` 时省略；1-128 字符。 |
| `points` | integer (int64) | 条件必填 | `BOUND` 时必填，非负当前可用余额；`NOT_BOUND` 时省略。 |
| `expiring_points` <br/>  | integer (int64) | 否 | 计划过期的非负积分；仅限 `BOUND`，`NOT_BOUND` 时省略。必须与 `points_expire_time` 同时出现。 |
| `points_expire_time` | integer (int64) | 否 | `expiring_points` 过期的 Unix 时间戳（毫秒）；仅限 `BOUND`，`NOT_BOUND` 时省略。必须与 `expiring_points` 同时出现。 |
| `update_time` | integer (int64) | 否 | 卖家最后更新余额的 Unix 时间戳（毫秒）；仅限 `BOUND`，`NOT_BOUND` 时省略。 |
## MemberPointsTransactionQuery SPI
**SPI 码**：`MEMBER_POINTS_TRANSACTION_QUERY` · **版本**：`202608`
**描述**：积分交易的只读游标分页查询。按 `occur_time` 降序返回交易。此 SPI 不使用 `idempotency_key`。
* 此 SPI 应具有高可用性，因为它直接影响买家体验。

### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TikTok Shop 买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 编码后的 TikTok Shop 店铺标识符，1-128 字符。 |
| `tts_shop_id` | string | 否 | 与请求关联的 TikTok Shop ID，1-64 字符。这不是 Shop OpenID。如果省略，卖家必须使用现有字段继续处理。 |
| `merchant_member_id` | string | 是 | 要查询 `transactions` 的稳定卖家会员标识符，1-128 字符。 |
| `page_size` | integer (int32) | 否 | 最大返回 `transactions` 数量，1-50；默认 20。 |
| `page_token` | string | 否 | 上一次响应中的不透明 `next_page_token`，最多 1024 字符。首页时省略。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `membership_status` | string enum | 是 | `BOUND` 或 `NOT_BOUND`。`NOT_BOUND` 需要空的 `transactions` 数组和空的 `next_page_token`。 |
| `transactions` | array&lt;object&gt; | 是 | 按 `occur_time` 降序排列的最多 50 条 `transactions`。返回空数组，而非 null。 |
| `next_page_token` | string | 是 | URL 安全的不透明下一页 token，最多 1024 字符，仅包含 A-Z、a-z、0-9、下划线或连字符。最后一页返回空字符串；无填充或百分号编码字符。 |
### `transactions` 条目
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `transaction_id` | string | 是 | 全局唯一的卖家积分交易标识符，1-128 字符。 |
| `points_change_type` | string enum | 是 | `EARN`、`DEDUCT`、`REFUND_REVERSE`、`ADJUST` 或 `EXPIRE`。 |
| `points_delta` | integer (int64) | 是 | 带符号积分变动：正数增加积分，负数减少积分。 |
| `points` | integer (int64) | 是 | 交易后立即生效的非负可用余额。 |
| `description` | string | 是 | 卖家提供的买家可读说明，1-500 字符。 |
| `related_event_id` | string | 否 | 关联的卖家业务事件标识符，1-128 字符。 |
| `occur_time` | integer (int64) | 是 | 积分交易发生的 Unix 时间戳（毫秒）。 |
## MembershipRedeem SPI
**SPI Code**: `MEMBERSHIP_REDEEM` · **Version**: `202609` · **Direction**: TikTok Shop → 卖家 / ISV
原子扣除所选奖励的全部积分费用。TikTok Shop 在扣除成功后单独发放优惠券。
### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | TikTok Shop 买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 编码后的 TikTok Shop 店铺标识符，1-128 字符。 |
| `tts_shop_id` | string | 否 | TikTok Shop ID，1-64 字符。如果省略，使用现有标识符继续处理。 |
| `merchant_member_id` | string | 是 | 稳定的卖家会员标识符，1-128 字符。 |
| `reward_type` | string enum | 是 | 此版本为 `COUPON`。 |
| `reward_id` | string | 是 | 所选奖励标识符，1-64 字符。 |
| `points_to_deduct` | integer (int64) | 是 | 精确的正整数积分费用；最小 1。不支持部分扣除。 |
| `idempotency_key` | string (UUID) | 是 | 稳定业务 key。重试必须使用相同 key 和相同请求体。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `redeem_status` | string enum | 是 | `SUCCEEDED` 或 `REJECTED`。 |
| `redemption_id` | string | 条件必填 | `SUCCEEDED` 时必填；1-128 字符。`REJECTED` 时禁止。 |
| `deducted_points` | integer (int64) | 条件必填 | `SUCCEEDED` 时必填；最小 1 且必须等于 points_to_deduct。`REJECTED` 时禁止。 |
| `points` | integer (int64) | 条件必填 | `SUCCEEDED` 时必填；扣除后的非负余额。`REJECTED` 时禁止。 |
| `reason_code` | string enum | 条件必填 | `REJECTED` 时必填；`SUCCEEDED` 时禁止。 |
| `reason_message` | string | 否 | `REJECTED` 时可选，最多 500 字符；`SUCCEEDED` 时禁止。 |
### 响应示例
**成功**
```JSON
{
  "redeem_status": "SUCCEEDED",
  "redemption_id": "REDEMPTION_10001",
  "deducted_points": 100,
  "points": 1150
}
```

**拒绝**
```JSON
{
  "redeem_status": "REJECTED",
  "reason_code": "INSUFFICIENT_POINTS",
  "reason_message": "The member does not have sufficient available points."
}
```

### 业务规则

* 使用相同幂等 key 的重复请求返回原始结果，不得重复扣除积分。
* SUCCEEDED 表示全额请求金额恰好被扣除一次；REJECTED 表示未扣除任何积分。
* 仅在优惠券发放确定失败后才使用 MembershipRedeemReverse。

### 拒绝原因码
| 原因码 | 含义 |
| --- | --- |
| `INSUFFICIENT_POINTS` | 可用余额低于请求的费用。 |
| `MEMBER_NOT_FOUND` | 没有与买家和店铺匹配的活跃会员关系。 |
| `REWARD_NOT_AVAILABLE` | 所选奖励或兑换规则不可用。 |
## MembershipRedeemReverse SPI
**SPI Code**: `MEMBERSHIP_REDEEM_REVERSE` · **Version**: `202609` · **Direction**: TikTok Shop → 卖家 / ISV
当优惠券发放确定失败时，从成功兑换中恢复全部积分金额。
### 请求参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `buyer_id` | string | 是 | 原始兑换中的买家标识符，1-64 字符。 |
| `shop_open_id` | string | 是 | 原始兑换中编码后的店铺标识符，1-128 字符。 |
| `tts_shop_id` | string | 否 | TikTok Shop ID，1-64 字符。 |
| `merchant_member_id` | string | 是 | 原始兑换中的卖家会员标识符，1-128 字符。 |
| `reward_type` | string enum | 是 | 此版本为 `COUPON`；必须与原始兑换匹配。 |
| `reward_id` | string | 是 | 原始兑换中的奖励标识符，1-64 字符。 |
| `redemption_id` | string | 是 | 成功的 MembershipRedeem 调用返回的标识符，1-128 字符。 |
| `points_to_reverse` | integer (int64) | 是 | 要恢复的精确正整数积分；最小 1 且必须等于原始全额扣除。 |
| `reverse_reason` | string enum | 是 | 此版本为 `COUPON_ISSUE_FAILED`。 |
| `idempotency_key` | string (UUID) | 是 | 稳定冲正 key。重试必须使用相同 key 和相同请求体。 |
### 响应参数
| 字段 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `reverse_status` | string enum | 是 | `SUCCEEDED` 或 `REJECTED`。 |
| `reversed_points` | integer (int64) | 条件必填 | `SUCCEEDED` 时必填；最小 1。`REJECTED` 时禁止。 |
| `points` | integer (int64) | 条件必填 | `SUCCEEDED` 时必填；冲正后的非负余额。`REJECTED` 时禁止。 |
| `reason_code` | string enum | 条件必填 | `REJECTED` 时必填；`SUCCEEDED` 时禁止。 |
| `reason_message` | string | 否 | `REJECTED` 时可选，最多 500 字符；`SUCCEEDED` 时禁止。 |
### 响应示例
**成功**
```JSON
{
  "reverse_status": "SUCCEEDED",
  "reversed_points": 100,
  "points": 1250
}
```

**拒绝**
```JSON
{
  "reverse_status": "REJECTED",
  "reason_code": "REDEMPTION_NOT_FOUND",
  "reason_message": "No successful original redemption was found."
}
```

### 业务规则

* 将积分记入被原始兑换扣减的同一会员账户。
* 不支持部分冲正；points_to_reverse 必须等于原始全额扣除。
* 使用相同幂等 key 的重复请求返回原始结果，不得重复记入积分。
* 如果买家、会员、奖励、兑换 ID 或积分金额与原始兑换不匹配，则拒绝请求。

### 拒绝原因码
| 原因码 | 含义 |
| --- | --- |
| `REDEMPTION_NOT_FOUND` | 未找到匹配的原始兑换。 |
| `REDEMPTION_NOT_SUCCEEDED` | 原始兑换未成功，因此无需冲正。 |
| `REDEMPTION_MISMATCH` | 买家、会员、奖励、兑换或积分详情与原始记录不匹配。 |
# Webhooks

* 订单 webhook：https://partner.tiktokshop.com/docv2/page/1-order-status-change#Back%20To%20Top
* 退款 webhook：https://partner.tiktokshop.com/docv2/page/8y10pibm

# 安全与合规说明

* API 仅传输会员集成所需的最少必要字段。
* 本文档定义的标准接口参数中不应出现电话号码、邮箱、姓名或地址等明文敏感信息。如果匹配需要此类数据，请使用双方商定的合规处理方式，如哈希或加密标识符。
* 调用方应在请求日志中保留 `request_id`，用于重试、故障排查和对账。
* 卖家应忽略未知的扩展字段，以确保向后兼容。

## 脱敏方案：邮箱
**我们不对域名进行脱敏，仅对本地部分进行脱敏。**
**邮箱是我们传输的唯一用户信息。**

* 对于本地部分，我们根据本地部分长度 n 采用以下规则：
   * n = 1：例如 a@gmail.com -> *@gmail.com
   * n = 2：例如 ab@gmail.com -> a*@gmail.com
   * n = 3：例如 abc@gmail.com -> a*c@gmail.com
   * n = 4：例如 abcd@gmail.com -> a**d@gmail.com
   * n = 5：例如 abcde@gmail.com -> a***e@gmail.com
   * n = 6：例如 abcdef@gmail.com -> a****f@gmail.com
   * n > 6：例如 abcdefg@gmail.com -> a****fg@gmail.com（最多脱敏 4 个字符）
* 此脱敏方案用于以下 API/SPI 中的邮箱字段：
   * **MembershipBindCheck** SPI：
      * 我们始终对会员邮箱进行脱敏
      * 对于返回结果，匹配的邮箱必须按输入脱敏的相反方式返回：

```JSON
Original email: abcdefg@gmail.com
Input email: a****fg@gmail.com
Output email: *bcde**@gmail.com 
Result: Match!
```


   * **MembershipBind** SPI：
      *  我们仅对在过去 90 天内在指定店铺没有订单的新会员进行脱敏
   * **MemberInfoQuery** API：
      * 我们仅对在过去 90 天内在指定店铺没有订单的会员进行脱敏

## 认证方案

* TTS API、SPI 和 webhooks 的认证方式是什么？
   1. API（ISV -> TTS）：
      1. TTS API 通过两个字段验证：**x-tts-access-token (请求头)**，从 **GetAccessToken** API 获取的 token 值；**shop-cipher (query)**，用于传输店铺信息，此值可从 [GetAuthorizedShops API](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309#Back%20To%20Top) 获取（通过链接查看请求请求头、query、body 的配置示例）
      2. 认证概述：https://partner.tiktokshop.com/docv2/page/authorization-overview-202407
   1. SPI（TTS -> ISV）：
      * 取决于第三方，我们目前使用 **IP 白名单。**
      * 我们还携带一个字段，其值为 ISV 在我们的 TTSPC 平台上创建的 app secret，ISV 可使用此 app secret 进行认证。
      3. TTS SPI 应通过 **x-tt-signature (请求头)** 验证。
      4. 签名生成算法如下，请参考此算法验证签名。更多信息请查看 [[External] SPI Integration Guide](https://bytedance.my.larkoffice.com/docx/HUa8diEO6oXem2xrZ3um8bbnyhc)

```JSON
canonical_query = Canonicalize(raw_query)

plaintext =
    app_secret
    + canonical_path
    + canonical_query
    + request_body
    + unix_timestamp
    + app_secret

signature = lowercase_hex(
    HMAC-SHA256(
        key  = app_secret,
        data = plaintext
    )
)
```


3. Webhook（TTS -> ISV）：
   1. TTS webhooks 列在官方 webhook 文档中：https://partner.tiktokshop.com/docv2/page/1-order-status-change#Back%20To%20Top
   2. webhook 配置指南包含如何认证 TTS webhooks 的信息 [https://partner.tiktokshop.com/docv2/page/configuration-guide#Back%20To%20Top](https://partner.tiktokshop.com/docv2/page/configuration-guide#Back%20To%20Top)

```JSON
signature_base_string = app_key + raw_request_body  
signature = HMAC-SHA256(signature_base_string, app_secret)
```

# 建议测试

* 请在上线前对应用进行端到端测试。以下是一些您可以测试的用例，但请创建自己的测试用例以确保行为符合预期后再发布。
* 用户旅程：[Loyalty Program User Experience and Incentive Policy](https://bytedance.larkoffice.com/wiki/TUkEwcpvviIVeKkPM4tc8VQunJQ)
* 请参阅 TTS 开发者指南获取官方端到端测试材料：https://partner.tiktokshop.com/docv2/page/tts-developer-guide
1. **前提条件**
   1. **环境和店铺**
      1. 在 [TTS Partner Center](https://partner.tiktokshop.com/) 中，创建一个 **Full Function Development Shop**（在 Development Kits -> Development Shops 下）用于测试。
         1. 至少发布一个测试商品并发布 Shop Home 设计。
         2. 在同一用于测试的 Development Shop 上安装并授权 ISV 应用。
      2. 在与 Development Shop 相同区域创建一个专用的 Buyer Test TikTok 账户，并将其关联到 Development Kits -> Development Shops 下的测试店铺。

      **步骤**

         1. 在 TikTok 应用中创建第二个新 TikTok 账户，最好使用测试邮箱地址。
         2. 使用要作为买家测试账户的账户登录 TikTok 应用。
         3. 在 Partner Center 中，进入 **Development Kits > Sandbox > Buyer test accounts**。
         4. 点击 **Link account**。
         5. 使用 TikTok 应用扫描 **Link TikTok account as buyer account** 页面上的二维码。
         6. 在 TikTok 应用中按照 **Authorize TikTok Partner Center** 流程操作。
         7. 在买家账户关联页面上点击 **Link the account**。

      **重要注意事项**

         * **不要**使用生产或个人 TikTok 账户。一旦关联为测试账户，将永久转换且无法撤销。
         * 买家 TikTok 账户必须与开发店铺在**相同区域/市场**。
         * 对于 Full Function 测试，您至少需要两个 TikTok 账户：一个 **Official Test TikTok Account** 和一个 **Buyer Test TikTok Account**。
         * 您不能将同一 TikTok 账户同时用作官方账户和买家测试账户。
         * 一个 Partner Center 账户最多可关联 **10 个 Buyer Test TikTok Account**。
      3. 请求 TikTok Shop 团队为测试店铺启用 Loyalty/Membership API/SPI 白名单和所需的前端配置。
2. **测试用例示例**

### 未绑定买家预检查
**前提条件：** 买家没有活跃的会员关联；测试 endpoint 已发布并上线。

1. 使用买家测试账户在 Shop 首页打开会员入口。
2. 触发 MembershipBindCheck/Precheck。
3. 记录平台请求 ID 和 ISV 请求 ID。

**预期结果：** SPI 到达集成测试 URL，响应通过 OAS 验证，平台选择有效的注册或匹配路径
### 注册并绑定
**前提条件：** 买家资料为 UNBOUND，手机可接收 OTP

1. 在 TikTok 应用中选择 Join。
2. 完成 OTP 步骤。
3. 确认 MembershipBind/Register SPI 到达 ISV。
4. 返回成功的 OAS 验证响应。
5. 查询最终会员资料或再次运行 BindCheck。

**预期结果：** 买家资料为 BOUND，ISV 恰好有一条会员/关联记录，重新打开会员页面不会创建重复会员。
### 幂等绑定重试

1. 发送有效的 Bind 请求并记录幂等 key。
2. 使用相同 key 和相同请求体重复同一请求。
3. 使用相同 key 但不同请求体重复。

**预期结果：** 相同 key 和请求体返回现有结果，不会重复创建会员或重复发放欢迎奖励；相同 key 但不同请求体产生确定性冲突。
### 积分余额和交易

1. 查询余额为零的新绑定会员。
2. 查询余额为正的会员。
3. 查询空交易列表和分页的非空列表。
4. 将 UI/平台值与 ISV 账本进行比对。

**预期结果：** 余额和交易历史与 ISV 账本匹配；分页、顺序、类型和时间字段符合 OAS；响应在平台超时之前以明确的延迟余量完成。
### 解绑并重新绑定

1. 使用会员页面菜单取消关联会员。
2. 确认 MembershipUnbind 到达 ISV。
3. 再次查询资料。
4. 重新绑定同一买家并验证现有会员被识别。

**预期结果：** 取消关联后资料变为 UNBOUND，重新绑定后恢复为 BOUND，不会丢失正确的会员身份或账本。
### 如何创建测试订单？
在关联买家测试账户并至少有一个上架测试商品后，从 Development Shop (Sandbox) Buyer View 创建测试订单。
**前提条件**

* 进入 Partner Center Console > Development Kits > Development Shops。
* 创建或使用 Development Shop 测试账户。
* 从 Development Kits > Development Shops > Manage accounts > Settings 关联一个客户/买家测试 TikTok 账户。
* 使用与开发店铺相同市场/区域的买家账户。
* 不要使用生产 TikTok 账户作为测试买家；一旦在 Development Shop 中关联，该账户将永久变为测试账户。
* 确保开发店铺有上架的测试商品。对于 TikTok 应用中的买家端购买，使用 Full Function development shop；Core Function 账户不支持真实买家购买。

**Partner Center 测试订单流程**
Partner Center
 -> Development Kits
 -> Development Shops
 -> Manage accounts
 -> Buyer View
 -> 创建测试订单
 -> Select products
 -> 选择配送方式
 -> 订单创建时状态为挂起
# 附录
## 会员信息查询

* 路径：POST `/customer_engagement/202607/member_profiles/search`
* 请求示例：

```Plain Text
curl -X POST \\ 
 'https://open-api.tiktokglobalshop.com/customer_engagement/:version/member_profiles/search?sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1623812664&app_key=38abcd&shop_cipher=GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3' \\ 
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \\ 
-H 'content-type: application/json' \\ 
-d '{
  "buyer_ids": [
    "7451234567890123456"
  ]
}'
```


* 响应示例：

```JSON
{
  "code": 0,
  "data": {
    "member_profiles": [
      {
        "bind_status": "BOUND",
        "buyer_id": "7451234567890123456",
        "email": "m***@example.com",
        "merchant_member_id": "MEMBER_10001",
        "points": 1250,
        "expiring_points": 200,
        "points_expire_time_ms": 1798761600000,
        "program_level_name": "GOLD",
        "update_time_ms": 1785168000000
      }
    ]
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/03808268ed9d47b69786c45829bdc467~tplv-k9wyc2ijk0-image.image" width="1860px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fddc26a7056f49f58c5ef6296d97b970~tplv-k9wyc2ijk0-image.image" width="1812px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f44e0e9967274e8fba6feb9736c586ba~tplv-k9wyc2ijk0-image.image" width="1816px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/3c4d946a71514ad593767cc483ffe6ba~tplv-k9wyc2ijk0-image.image" width="1812px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f4fd74c558024b08af9cc702bc8a36d1~tplv-k9wyc2ijk0-image.image" width="1782px" /></div>

## 会员资料批量更新

* 路径：`/customer_engagement/202607/member_profiles/partial_edit`
* 请求示例：

```JSON
curl -X POST \\ 
 'https://open-api.tiktokglobalshop.com/customer_engagement/:version/member_profiles/partial_edit?app_key=38abcd&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1623812664&shop_cipher=GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3' \\ 
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \\ 
-H 'content-type: application/json' \\ 
-d '{
  "member_profiles": [
    {
      "bind_status": "BOUND",
      "buyer_id": "7451234567890123456",
      "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
      "merchant_member_id": "MEMBER_10001",
      "program_level_expire_time_ms": 1798761600000,
      "program_level_name": "GOLD",
      "update_time_ms": 1785168000000
    }
  ]
}'
```


* 响应示例：

```JSON
{
  "code": 0,
  "data": {
    "fail_count": 1,
    "errors": [
      {
        "code": "INTERNAL_ERROR",
        "detail": {
          "buyer_id": "7451234567890123456",
          "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
          "merchant_member_id": "MEMBER_10001"
        },
        "message": ""
      }
    ],
    "success_count": 1,
    "successes": [
      {
        "buyer_id": "7451234567890123456",
        "idempotency_key": "7802d8ce-f651-4d7c-9431-0ad7c957921f",
        "merchant_member_id": "MEMBER_10001"
      }
    ],
    "total_count": 2
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/31d8741b717747248d62731623cec2c5~tplv-k9wyc2ijk0-image.image" width="2048px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/dc651f316585479c8f10b8c093ddc268~tplv-k9wyc2ijk0-image.image" width="1864px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b5b77fb679c74c94b28b93b32a6ba71f~tplv-k9wyc2ijk0-image.image" width="1840px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/33311fa3ee2e4b878463262ebb78fdf9~tplv-k9wyc2ijk0-image.image" width="1800px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/d215c25dc0b347f2abb1531e5a0efb54~tplv-k9wyc2ijk0-image.image" width="1832px" /></div>


