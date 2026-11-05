# (62) 商品包裹推荐

# 1. 触发场景
当生成商品包裹推荐时，会触发此 webhook。
**注意：** 仅适用于巴西（**BR**）和墨西哥（**MX**）市场。
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](https://partner.tiktokshop.com/docv2/page/access-scope)。
# 2. 数据业务参数
| 属性 |  |  |  | 类型 | 示例 | 属性描述 |
| --- | --- | --- | --- | --- | --- | --- |
| type |  |  |  | int | 62 | webhook 类型的 ID。 |
| tts_notification_id |  |  |  | string | 7327112393057371910 | 通知的 ID。 |
| shop_id <br/>  |  |  |  | string | 2123123 | 卖家的 shop_id。获取方式请参见[授权概述](https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75)。<br/>  |
| timestamp |  |  |  | int | 1644412885 | 此 webhook 触发时的 UNIX 时间戳。 |
| data |  |  |  | object |  |  |
| > | product_id |  |  | string <br/>  | 7493990579714164574 <br/>  | TikTok Shop 生成的商品 ID。<br/>  |
| > | > <br/>  | abnormality_types <br/>  |  | []string <br/>  | ["Weight","Dimension"] | 当前异常类型列表。<br/>如果状态为 NORMAL，返回 ["None"]。<br/>  |
| > | > | weight_recommendation <br/>  |  | object <br/>  |  | 重量修正建议。 |
| > | > | > | unit | string | GRAM | 建议值单位 |
| > | > | > | weight | object |  | 重量的建议值。 |
| > | > | > | >min_value | string | 450 | 建议范围最小值；单位：g |
| > | > | > | >max_value | string | 550 | 建议范围最大值；单位：g |
| > | > | dimension_recommendation |  | object |  | 尺寸修正建议。 |
| > | > | > | unit | string <br/>  | CENTIMETER | 建议值单位 |
| > | > | > | length | object <br/>  | <br/>  | 长度的建议值。 |
| > | > | > | > min_value | string | 19 | 建议范围最小值；单位：cm |
| > | > | > | > max_value | string | 22 | 建议范围最大值。单位：cm |
| > | > | > | width | object |  | 宽度的建议值。 |
| > | > | > | > min_value | string | 19 | 建议范围最小值；单位：cm |
| > | > | > | > max_value | string | 22 | 建议范围最大值。单位：cm |
| > <br/>  | > | > | height | object |  | 高度的建议值。 |
| > | > | > | > min_value | string | 19 | 建议范围最小值；单位：cm |
| > | > | > | > max_value | string | 22 | 建议范围最大值；单位：cm |



---



## 事件示例
```JSON
{
    "type": 62,
    "tts_notification_id": "7611238471432161025",
    "shop_id": "1111111",
    "timestamp": 1772129552,
    "data": {
        "abnormality_types": [
            "Weight",
            "Dimension"
        ],
        "dimension_recommendation": {
            "height": {
                "max_value": "3",
                "min_value": "3"
            },
            "length": {
                "max_value": "1234",
                "min_value": "123"
            },
            "unit": "CENTIMETER",
            "width": {
                "max_value": "666",
                "min_value": "555"
            }
        },
        "product_id": "1733529220361062152",
        "weight_recommendation": {
            "unit": "GRAM",
            "weight": {
                "max_value": "12000",
                "min_value": "12000"
            }
        }
    }
}
```

