# Regions and languages

# Introduction
TikTok Shop supports retrieval of text data for different regions in a variety of languages through language tags that follow [IETF BCP 47 language tag syntax (RFC 5646)](https://www.rfc-editor.org/rfc/rfc5646).
> **Important:** Locale support can vary by API. The locale codes specified in the endpoint reference documentation take precedence over this page. If an endpoint lists a smaller set of supported locale codes, use that endpoint-specific set.
> `zh-CN` is available only for retrieving machine-translated Chinese reference text in supported multilingual scenarios for global sellers based in China. `zh-CN` is not a default locale for any supported region and is not supported for writing Chinese text into text fields.
> Region and locale availability may change as TikTok Shop opens or updates markets. Use the latest platform market availability and endpoint reference documentation as the source of truth. Last updated: July 6, 2026.

# Supported languages
You can pass the following locale codes in APIs that support localization to obtain text data in the corresponding language.
| **Language** | **Locale codes** |
| --- | --- |
| English | en-GB, en-IE, en-PH, en-SG, en-US |
| French | fr-FR |
| German | de-DE |
| Indonesian | id-ID |
| Italian | it-IT |
| Japanese | ja-JP |
| Malay | ms-MY |
| Portuguese | pt-BR |
| Spanish | es-ES, es-MX |
| Thai | th-TH |
| Vietnamese | vi-VN |
> **Note:** For global sellers based in China, you can pass `zh-CN` to obtain machine-translated Chinese versions of property text for reference if the property supports multilingual content. However, specifying Chinese text in text fields is not supported.

# Region-to-locale mapping
Use the default locale code for a region unless the endpoint reference explicitly supports another locale code. Optional locale codes are endpoint-specific; do not infer unsupported locale codes from a country code, language name, or browser locale.
| **Country** | **Country code** | **Default locale code** | **Optional locale code rule** |
| --- | --- | --- | --- |
| Brazil | BR | pt-BR | Use only locale codes listed or accepted by the endpoint reference. |
| France | FR | fr-FR | Use only locale codes listed or accepted by the endpoint reference. |
| Germany | DE | de-DE | Use only locale codes listed or accepted by the endpoint reference. |
| Indonesia | ID | id-ID | Use only locale codes listed or accepted by the endpoint reference. |
| Ireland | IE | en-IE | Use only locale codes listed or accepted by the endpoint reference. |
| Italy | IT | it-IT | Use only locale codes listed or accepted by the endpoint reference. |
| Japan | JP | ja-JP | Use only locale codes listed or accepted by the endpoint reference. |
| Malaysia | MY | ms-MY | Use only locale codes listed or accepted by the endpoint reference. |
| Mexico | MX | es-MX | Use only locale codes listed or accepted by the endpoint reference. |
| Philippines | PH | en-PH | Use only locale codes listed or accepted by the endpoint reference. |
| Singapore | SG | en-SG | Use only locale codes listed or accepted by the endpoint reference. |
| Spain | ES | es-ES | Use only locale codes listed or accepted by the endpoint reference. |
| Thailand | TH | th-TH | Use only locale codes listed or accepted by the endpoint reference. |
| United Kingdom | GB | en-GB | Use only locale codes listed or accepted by the endpoint reference. |
| United States | US | en-US | Use only locale codes listed or accepted by the endpoint reference. |
| Vietnam | VN | vi-VN | Use only locale codes listed or accepted by the endpoint reference. |
`zh-CN` is intentionally excluded from the default locale column because it is not a supported default or writable locale for any region.
# Supported regions
| **Country** | **Country code** | **Default locale code** |
| --- | --- | --- |
| Brazil | BR | pt-BR |
| France | FR | fr-FR |
| Germany | DE | de-DE |
| Indonesia | ID | id-ID |
| Ireland | IE | en-IE |
| Italy | IT | it-IT |
| Japan | JP | ja-JP |
| Malaysia | MY | ms-MY |
| Mexico | MX | es-MX |
| Philippines | PH | en-PH |
| Singapore | SG | en-SG |
| Spain | ES | es-ES |
| Thailand | TH | th-TH |
| United Kingdom | GB | en-GB |
| United States | US | en-US |
| Vietnam | VN | vi-VN |
> **Note:** Some locale codes may not be supported in certain APIs. The locale codes specified in the endpoint reference documentation take precedence.
