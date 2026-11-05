# (58) 获取 FBT MCF 订单状态

## 触发场景
当 FBT 多渠道履约（MCF）订单状态发生变更/更新时，会触发此 webhook。
> 前提条件：在合作伙伴中心已启用 **Fulfilled by TikTok(FBT) Info** API 权限范围。更多信息请参见[访问权限范围](access-scope)。

## 数据业务参数
| 属性 |  |  |  |  | 类型 | 示例 | 属性描述 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| type |  |  |  |  | int | 58 | webhook 类型的 ID。 |
| tts_notification_id |  |  |  |  | string | 7327112393057371910 | 通知的 ID。 |
| seller_open_id <br/>  |  |  |  |  | string | VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw | 卖家的 open_id。更多信息请参见[授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)。 |
| timestamp |  |  |  |  | int | 1644412885 | 此 webhook 触发时的 UNIX 时间戳。 |
| data |  |  |  |  |  |  |  |
|  | mcf_order |  |  |  | object |  | MCF 订单信息 |
| > |  | external_order_id <br/>  |  |  | string | shopify202208291503530001100220033 | 您 OMS 系统中对应的订单 ID。 |
| > |  | mcf_order_id |  |  | string | 7136104329798256386 | 标识不同 MCF 订单的唯一 ID |
| > |  | consign_orders |  |  | []object |  | 订单发货后，`consign_orders` 字段将显示订单的托运详情。 |
| > |  | > | id |  | string | OBF12345678 | `托运订单`唯一 ID |
| > |  | > | tracking_number |  | string | TN87654321 | 此托运订单的物流追踪号。如果订单尚未交给物流承运商，此字段可能为空值。 |
| > |  | > | status |  | string | processing | 此托运订单的状态<br/>  <br/> 可能的状态枚举值<br/> 1. **SHIPPED** - 订单已从仓库发出<br/> 2. **HANDOVER** - 订单已由物流承运商接收并处于运输中<br/> 3. **CLOSED** - 订单已关闭<br/> 4. **LOST** - 订单丢失<br/> 5. **DAMAGE** - 订单损坏<br/> 6. **COMPLETED** - 订单已完成<br/> 7. **ABNORMAL** - 此订单存在问题，无法履约。 |
| > |  | > | goods |  | []object |  | 此托运订单中的商品 ID 和数量。 |
| > |  | > | > | id | string | 1231231 | Fulfilled by TikTok 系统生成的商品标识符 |
| > |  | > | > | quantity | int16 | 1 | 此托运订单中的商品数量 |
|  |  | > <br/>  | is_platform_closed <br/>  |  | string  | true <br/>  | 此字段表示托运订单是否已被 FBT 平台取消。如果值为 true，表示订单已被平台取消；如果为 false，表示订单已被您的 OMS 取消。 |
|  |  | > | issue |  | string | 库存不足 | 此字段显示订单停滞的原因。当 `托运订单` 处于异常状态（如 ABNORMAL、LOST 等）时，此处会显示具体的问题原因。 |
|  |  | > | shipping_provider |  | object |  | 此托运订单的物流承运商详细信息。如果订单尚未交给物流承运商，此字段可能为空值。 |
|  |  | > | > | id | string | 7345645330412603141 | 物流承运商唯一 ID。 |
|  |  | > | > | name | string | UPS | 物流承运商名称。 |
| > |  | create_time |  |  | int64 | 1661756811 | MCF 订单创建的时间 |

## 事件示例
```JSON
{
  "type": 58,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id": "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "mcf_order": {
      "external_order_id": "shopify202208291503530001100220033",
      "mcf_order_id": "7136104329798256386",
      "consign_orders": {
        "id": "OBF12345678",
        "tracking_number": "TN87654321",
        "carrier": "USPS",
        "status": "processing",
        "goods": {
          "id": "1231231",
          "quantity": 1
        }
      },
      "create_time": 1661756811
    }
  }
}
```


