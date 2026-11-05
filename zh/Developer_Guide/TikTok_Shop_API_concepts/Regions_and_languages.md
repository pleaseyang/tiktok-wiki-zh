# 区域和语言

# 简介
TikTok Shop 支持通过遵循 [IETF BCP 47 语言标签语法 (RFC 5646)](https://www.rfc-editor.org/rfc/rfc5646) 的语言标签，以多种语言检索不同区域的文本数据。
> **重要提示：** Locale 支持因 API 而异。endpoint 参考文档中指定的 locale 代码优先于本页面。如果某个 endpoint 列出了较小的受支持 locale 代码集，请使用该 endpoint 特定的集合。
> `zh-CN` 仅可用于在中国注册的全球卖家的受支持多语言场景中获取机器翻译的中文参考文本。`zh-CN` 不是任何受支持区域的默认 locale，也不支持将中文文本写入文本字段。
> 随着 TikTok Shop 开设或更新市场，区域和 locale 的可用性可能会发生变化。以最新的平台市场可用性和 endpoint 参考文档为准。最后更新日期：2026 年 7 月 6 日。

# 支持的语言
您可以在支持本地化的 API 中传递以下 locale 代码，以获取相应语言的文本数据。
| **语言** | **Locale 代码** |
| --- | --- |
| 英语 | en-GB, en-IE, en-PH, en-SG, en-US |
| 法语 | fr-FR |
| 德语 | de-DE |
| 印度尼西亚语 | id-ID |
| 意大利语 | it-IT |
| 日语 | ja-JP |
| 马来语 | ms-MY |
| 葡萄牙语 | pt-BR |
| 西班牙语 | es-ES, es-MX |
| 泰语 | th-TH |
| 越南语 | vi-VN |
> **注意：** 对于在中国注册的全球卖家，如果属性支持多语言内容，您可以传递 `zh-CN` 获取机器翻译的中文版属性文本以供参考。但是，不支持在文本字段中指定中文文本。

# 区域到 locale 的映射
除非 endpoint 参考明确支持其他 locale 代码，否则请使用区域的默认 locale 代码。可选的 locale 代码是 endpoint 特定的；不要从国家代码、语言名称或浏览器 locale 推断不受支持的 locale 代码。
| **国家** | **国家代码** | **默认 Locale 代码** | **可选 Locale 代码规则** |
| --- | --- | --- | --- |
| 巴西 | BR | pt-BR | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 法国 | FR | fr-FR | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 德国 | DE | de-DE | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 印度尼西亚 | ID | id-ID | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 爱尔兰 | IE | en-IE | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 意大利 | IT | it-IT | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 日本 | JP | ja-JP | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 马来西亚 | MY | ms-MY | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 墨西哥 | MX | es-MX | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 菲律宾 | PH | en-PH | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 新加坡 | SG | en-SG | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 西班牙 | ES | es-ES | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 泰国 | TH | th-TH | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 英国 | GB | en-GB | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 美国 | US | en-US | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
| 越南 | VN | vi-VN | 仅使用 endpoint 参考中列出或接受的 locale 代码。 |
`zh-CN` 被有意从默认 locale 列中排除，因为它不是任何区域的受支持默认或可写入 locale。
# 受支持的区域
| **国家** | **国家代码** | **默认 Locale 代码** |
| --- | --- | --- |
| 巴西 | BR | pt-BR |
| 法国 | FR | fr-FR |
| 德国 | DE | de-DE |
| 印度尼西亚 | ID | id-ID |
| 爱尔兰 | IE | en-IE |
| 意大利 | IT | it-IT |
| 日本 | JP | ja-JP |
| 马来西亚 | MY | ms-MY |
| 墨西哥 | MX | es-MX |
| 菲律宾 | PH | en-PH |
| 新加坡 | SG | en-SG |
| 西班牙 | ES | es-ES |
| 泰国 | TH | th-TH |
| 英国 | GB | en-GB |
| 美国 | US | en-US |
| 越南 | VN | vi-VN |
> **注意：** 某些 locale 代码可能在特定 API 中不受支持。以 endpoint 参考文档中指定的 locale 代码为准。
