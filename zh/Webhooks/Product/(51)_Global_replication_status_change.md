# (51) 全球复制状态变更

# 1. 触发场景
当商品在另一个市场的复制操作完成时（无论成功或失败），会触发此 webhook。如果复制失败，失败原因将包含在响应中。
**仅适用于全球卖家。**
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 51 | 此 webhook 主题的 ID，固定为 51。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ source_product_id | string | "764c6e87eedcea90399a0dafcd572b71" | 被复制到其他市场的商品 ID。 |
| └ replicated_product | object |  | 从源商品复制而来的商品。 |
| └ └ product_id | string | "576486316948490000" | 通过复制创建的商品 ID。<br/>将此 ID 传递给 [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) endpoint 以获取更多商品详情。 |
| └ └ region | string | "GB" | 商品被复制到的市场。 |
| └ └ result | string | "SUCCESS" | 商品复制的结果。<br/>可能的值：<br/>  <br/> * SUCCESS：商品已成功复制到本地店铺，已提交上架并正在审核中。<br/> * DRAFT：商品已成功复制到本地店铺，但由于验证错误被保存为本地草稿商品。您需要调用 [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) 获取原始提交数据，将该数据传递给 [POST Check Product Listing](https://partner.tiktokshop.com/docv2/page/check-product-listing-202309) 以识别错误，然后调用 [PUT Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309) 更正错误并提交审核。<br/> * FAILED：商品复制到本地店铺失败。 |
| └ └ fail_reasons | []object |  | 复制失败的原因列表。 |
| └ └ └ message | string |  | 复制失败的原因。 |

---


## 事件示例
```JSON
{
    "type": 51,
    "shop_id": "7494049642642441621",
    "tts_notification_id": "7327112393057371910",
    "timestamp": 1644412885,
    "data": {
        "source_product_id": "764c6e87eedcea90399a0dafcd572b71",
        "replicated_product": {
            "product_id": "576486316948490000",
            "region": "GB",
            "result": "SUCCESS",            
            "fail_reasons": {
                "message": ""
                }
            }
        }
    }
}
```

