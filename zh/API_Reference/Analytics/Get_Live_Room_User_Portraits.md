# 获取直播间用户画像

# Path: /analytics/202502/live_rooms/{live_room_id}/user_portraits
# Method: [GET]
# 功能描述
返回指定直播间的用户画像指标，包括年龄、性别、粉丝、广告和地区分布。

---


# 公共参数
有关公共参数，请参阅 [如何调用 TikTok Shop API - 公共参数](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | 是否必填 <!-- width:60px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| content-type | header | string | Y | application/json | 允许类型：application/json |
# 请求 Path 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| live_room_id | string | Y | 7274599999999999999 | 请求用户画像指标的直播间 ID。 |
# 请求 Query 参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 是否必填 <!-- width:90px --> | 示例 <!-- width:254px --> | 属性描述 <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| app_key | string | Y | 38abcd | 每个应用都有一个唯一的 key。请使用分配给您应用的特定 key。 |
| sign | string | Y | 5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c | 由 gen 算法生成的签名。当您向 TTS 发送 API 请求时，必须对其进行签名，以便 TTS 能够识别发送方。 |
| timestamp | int | Y | 1623812664 | Unix 时间戳 GMT（UTC+00:00）。此时间戳用于所有 API 请求。开发者可以将其转换为本地时间。 |
# 请求示例
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202502/live_rooms/7274599999999999999/user_portraits?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```

# 响应参数
| Properties <!-- width:110px --> | Type <!-- width:90px --> | 示例 <!-- width:289px --> | 属性描述 <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | API 响应中返回的成功或失败状态码。 |
| message | string | Success | API 响应中返回的成功或失败消息。失败原因将在消息中说明。 |
| request_id | string | 202203070749000101890810281E8C70B7 | 请求日志 |
| data | object |  | 具体返回信息 |
| ^all_ads_gender_indicators | []object |  | 广告的性别指标 |
| ^^type | string | USER_PORTRAIT_GENDER_UNKNOWN | 此指标代表的性别类别。 |
| 可选值： |  |  |  |

* USER_PORTRAIT_GENDER_UNKNOWN：未知性别。
* USER_PORTRAIT_GENDER_M：男性。
* USER_PORTRAIT_GENDER_F：女性。 |
   ^^value |string |123 |对应性别指标的数量。 |
   ^all_fan_indicators |[]object | |粉丝指标 |
   ^^type |string |USER_PORTRAIT_FOLLOWER |stats_type 描述以下值的类型。

USER_PORTRAIT_FOLLOWER：粉丝的用户画像
USER_PORTRAIT_NON_FOLLOWER：非粉丝的用户画像 |
^^value |string |123 |对应粉丝状态指标的数量。 |
^all_ads_age_indicators |[]object | |广告的年龄指标 |
^^type |string |USER_PORTRAIT_AGE_LESS_THAN_15 |年龄指标的类型。
USER_PORTRAIT_AGE_LESS_THAN_15：年龄小于 15 岁的用户。
USER_PORTRAIT_AGE_MORE_THAN_34：年龄大于 34 岁的用户。
USER_PORTRAIT_AGE_MORE_THAN_55：年龄大于 55 岁的用户。
USER_PORTRAIT_AGE_13_TO_17：年龄在 13 至 17 岁之间的用户。
USER_PORTRAIT_AGE_15_TO_17：年龄在 15 至 17 岁之间的用户。
USER_PORTRAIT_AGE_18_TO_24：年龄在 18 至 24 岁之间的用户。
USER_PORTRAIT_AGE_25_TO_34：年龄在 25 至 34 岁之间的用户。
USER_PORTRAIT_AGE_35_TO_44：年龄在 35 至 44 岁之间的用户。
USER_PORTRAIT_AGE_45_TO_54：年龄在 45 至 54 岁之间的用户。 |
^^value |string |123 |对应年龄指标的数量。 |
^region_indicators |[]object | |直播间的国家级用户画像指标。 |
^^value |string |123 |对应指标的份额，按 10,000 缩放。除以 10,000 即可得到实际比例。 |
^^type |string |ID |指标的国家/地区
|
^paid_ads_age_indicators |[]object | |付费广告的年龄指标 |
^^type |string |USER_PORTRAIT_AGE_LESS_THAN_15 |付费广告年龄指标的类型。
USER_PORTRAIT_AGE_LESS_THAN_15：年龄小于 15 岁的用户。
USER_PORTRAIT_AGE_MORE_THAN_34：年龄大于 34 岁的用户。
USER_PORTRAIT_AGE_MORE_THAN_55：年龄大于 55 岁的用户。
USER_PORTRAIT_AGE_13_TO_17：年龄在 13 至 17 岁之间的用户。
USER_PORTRAIT_AGE_15_TO_17：年龄在 15 至 17 岁之间的用户。
USER_PORTRAIT_AGE_18_TO_24：年龄在 18 至 24 岁之间的用户。
USER_PORTRAIT_AGE_25_TO_34：年龄在 25 至 34 岁之间的用户。
USER_PORTRAIT_AGE_35_TO_44：年龄在 35 至 44 岁之间的用户。
USER_PORTRAIT_AGE_45_TO_54：年龄在 45 至 54 岁之间的用户。 |
^^value |string |123 |对应付费广告年龄指标的数量。 |
^paid_ads_gender_indicators |[]object | |付费广告的性别指标 |
^^type |string |USER_PORTRAIT_GENDER_UNKNOWN |此指标代表的性别类别。
可选值：

* USER_PORTRAIT_GENDER_UNKNOWN：未知性别。
* USER_PORTRAIT_GENDER_M：男性。
* USER_PORTRAIT_GENDER_F：女性。 |
   ^^value |string |123 |对应付费广告性别指标的数量。 |
   ^paid_fan_indicators |[]object | |付费粉丝指标 |
   ^^type |string |USER_PORTRAIT_FOLLOWER |stats_type 描述以下值的类型。

USER_PORTRAIT_FOLLOWER：粉丝的用户画像
USER_PORTRAIT_NON_FOLLOWER：非粉丝的用户画像 |
^^value |string |123 |对应付费粉丝状态指标的数量。 |
# 响应示例
```json
{"code":0,"data":{"all_ads_gender_indicators":[{"type":"USER_PORTRAIT_GENDER_UNKNOWN","value":"123"}],"all_fan_indicators":[{"type":"USER_PORTRAIT_FOLLOWER","value":"123"}],"all_ads_age_indicators":[{"type":"USER_PORTRAIT_AGE_LESS_THAN_15","value":"123"}],"region_indicators":[{"value":"123","type":"ID"}],"paid_ads_age_indicators":[{"type":"USER_PORTRAIT_AGE_LESS_THAN_15","value":"123"}],"paid_ads_gender_indicators":[{"type":"USER_PORTRAIT_GENDER_UNKNOWN","value":"123"}],"paid_fan_indicators":[{"type":"USER_PORTRAIT_FOLLOWER","value":"123"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# 错误码
有关常见错误码，请参阅 [如何调用 TikTok Shop API - 常见错误码](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 66009302 | 参数无效。请检查直播间 ID。 |
| 66009315 | 无操作权限。 |
