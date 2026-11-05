# (52) 全球上架方式变更

# 1. 触发场景
当店铺的全球上架方式发生变更时，会触发此 webhook。
**仅适用于全球卖家。**
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 52 | 此 webhook 主题的 ID，固定为 52。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| seller_open_id | string | "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw" | 卖家的 open_id。更多信息请参见[授权概述](https://partner.tiktokshop.com/docv2/page/authorization-overview-202407)。 |
| data | object |  |  |
| └ global_product_id | string | "1729715829872102020" | 与本地商品关联的全球商品 ID。 |
| └ local_product_id | []string | ["1731711955927208538"] | 本地商品 ID。 |
| └ listing_method | string | "GLOBAL_PUBLISHING" | 适用于本地商品的上架方式。<br/>可能的值：<br/>  <br/> * GLOBAL_PUBLISHING：创建全球商品，然后将其发布到目标本地市场。<br/> * LOCAL_REPLICATION：创建本地商品，然后将其复制到其他目标本地市场。 |

---


## 事件示例
```JSON
{
    "type": 52,
    "tts_notification_id": "7327112393057371910",
    "timestamp": 1644412885,
    "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"
    "data": {
        "global_product_id": "1729715829872102020",
        "local_product_id": ["1731711955927208538"],
        "listing_method": "GLOBAL_PUBLISHING"
            }
        }
    }
}
```

