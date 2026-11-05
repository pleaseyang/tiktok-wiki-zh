# (36) 发票状态变更

# 1. 触发场景
使用 [POST Upload Invoice](upload-invoice) endpoint 后，当发票上传状态发生变更时，会触发此 webhook。
**注意**：[POST Upload Invoice](upload-invoice) API 目前仅适用于巴西市场。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| shop_id | string | "7494049642642441621" | TikTok Shop ID。 |
| type | int64 | 36 | 此 webhook 主题的 ID，固定为 36。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| timestamp | int64 | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ package_id | string | "123456" | 包裹的 ID。 |
| └ order_ids | []string | ["152523", "532123"] | 对应 `package_id` 中的订单 ID 列表。 |
| └ invoice_status | string | "SUCCESS" | 发票上传的状态。可能的值：<br/>  <br/> * `SUCCESS`<br/> * `PROCESSING`<br/> * `FAILED`<br/> * `INVALID` |
| └ invalid_reason | string | "NOT_FOUND" | `invoice_status = INVALID` 的原因。可能的值：<br/>  <br/> * `UNKNOWN`：内部系统错误。请稍后重试。<br/> * `FAILED`：NFe 文件或访问密钥无效。请检查 XML 文件的正确性。<br/> * `NOT_FOUND`：未找到 NFe。这可能是由于数据延迟。请稍后重试。<br/> * `NOT_AUTHORIZED`：NFe 未获得合法授权。可能尚未开具或已被取消。<br/> * `ACCESS_KEY_DUPLICATE`：访问密钥已存在。您不能上传具有重复访问密钥的发票。<br/> * `CNPJ_NOT_MATCH`：请确保 NF-e 的 CNPJ 前 8 位与您入驻时提供的 CNPJ 一致。<br/> * `UF_Inconsistent_Required`：NF-e 验证失败：用于开具 NF-e 的 CNPJ 注册的州与您的仓库所在州不同。<br/> * `UF_Inconsistent_Dismisse_Retirada_missing`：NF-e 验证失败：用于开具 NF-e 的 CNPJ 注册的州与您的仓库所在州不同。要使用此 CNPJ 开具有效的 NF-e，请在 NF-e 中包含仓库信息（取货地点标识）。<br/> * `UF_Inconsistent_Dismissed_Retirada_Inconsistent`：用于开具 NF-e 的 CNPJ 注册的州与您的仓库所在州不同。要使用此 CNPJ 开具有效的 NF-e，请在 NF-e 中包含仓库信息（取货地点标识）。 |
## 事件示例
```json
{
    "type":36,
    "tts_notification_id": "7327112393057371910",
    "shop_id": "7494049642642441621",
    "timestamp": 1644412885,
    "data":{
        "package_id": "123456",
        "order_ids": ["152523", "532123"],
        "invoice_status": "INVALID",
        "invalid_reason": "NOT_FOUND"
    }
}
```


