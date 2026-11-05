# (46) 图片翻译完成

# 1. 触发场景
当图片翻译完成或失败时，会触发此 webhook。


仅适用于在欧盟地区跨境销售的卖家。
**前提条件**：在合作伙伴中心已启用 "Product Basic" API 权限范围。更多信息请参见[访问权限范围](access-scope)。
# 2. 数据业务参数
| **参数名称** | **数据类型** | **示例** | **描述** |
| --- | --- | --- | --- |
| type | int | 46 | 此 webhook 主题的 ID，固定为 46。 |
| tts_notification_id | string | "7327112393057371910" | 此 webhook 通知的 ID。 |
| shop_id | string | "7494049642642441621" | 店铺 ID。 |
| timestamp | int | 1644412885 | 此 webhook 触发时的时间。Unix 时间戳。 |
| data | object |  |  |
| └ translation_task | object |  | 图片翻译任务及对应结果。每个任务对应将 1 张图片翻译为 1 种目标语言。 |
| └ └ id | string | 764c6e87eedcea90399a0dafcd572b71 | 标识图片翻译任务的 ID。 |
| └ └ status | string | COMPLETED | 翻译状态。<br/>可能的值：<br/> - PROCESSING：翻译进行中，尚未完成。<br/> - COMPLETED：翻译已完成，结果可用。<br/> - FAILED：由于错误，翻译未完成。 |
| └ └ fail_reason | string |  | 翻译任务失败的原因。 |
| └ └ target_language | string | it-IT | 图片翻译的目标语言。<br/>可能的值：<br/> - de-DE<br/> - en-IE<br/> - es-ES<br/> - fr-FR<br/> - it-IT |
| └ └ original_image | string |  | 待翻译的原始图片。 |
| └ └ └ uri | string | tos-useast2a-i-tulkllf4y5-euttp/748e39ecff38453ab8396a36a53dbb92 | 原始图片的 URI。 |
| └ └ └ url | string | https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xyz-sg/sample.jpeg | 原始图片的 URL。 |
| └ └ translated_image | object |  | 翻译后的图片。 |
| └ └ └ uri | string | tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d | 翻译后图片的 URI。 |
| └ └ └ url | string | https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg | 翻译后图片的 URL。 |

---


## 事件示例
```JSON
{
    "type": 46,
    "shop_id": "7494049642642441621",
    "tts_notification_id": "7327112393057371910",
    "timestamp": 1644412885,
    "data": {
        "translation_task": {
            "id": "764c6e87eedcea90399a0dafcd572b71",
            "status": "COMPLETED",
            "fail_reason": "",            
            "target_lang": "it-IT",
            "original_image": {
                "uri": "tos-useast2a-i-tulkllf4y5-euttp/748e39ecff38453ab8396a36a53dbb92",
                "url": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xyz-sg/sample.jpeg"
            },
            "translated_image": {
                "uri": "tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d",
                "url": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg"
            }
        }
    }
}
```


