# 签名您的 API 请求

## 简介
调用 TikTok Shop API 时，必须包含签名以正确验证您的请求。所有未包含签名或签名无效的请求都将被拒绝访问。
TikTok Shop API 使用 **HMAC-SHA256** 作为生成签名的默认算法。
**HS256（使用 SHA-256 的 HMAC）** 是一种对称算法，意味着双方共享一个私钥。由于使用相同的密钥来生成和验证签名，因此必须注意确保密钥不被泄露。
当 TikTok Shop 收到经过身份验证的请求时，它会使用请求中包含的身份验证信息重新生成签名。如果签名匹配，服务将处理请求。否则，将拒绝请求。
❗ **重要提示**：TikTok Shop API 使用您的 **app secret** 作为身份验证的私钥。您可以从 Partner Center 的应用详情页获取 **app secret**。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/cc8d63acb74b4e7bb18413efa3aaace7~tplv-k9wyc2ijk0-image.image)

对于 API 版本 `202309` 及更高版本，在 `x-tts-access-token` 请求 header 中发送 access token，而不是在查询字符串中。生成签名时不包含 access token。对于仍使用 `access_token` 作为查询参数的旧版 API，在重新排列的查询键中排除 `access_token`。
# 代码示例
您可以在下方找到 GoLang、Java、Node.js 和 Python 的代码示例。借助这些代码示例，您无需深入了解算法细节。如果您需要其他语言的代码示例，请标注相关句子并向我们反馈。
## 签名算法（Go）
```Go
import (  
    "bytes"  
    "crypto/hmac"  
    "crypto/sha256"  
    "encoding/hex"  
    "io"  
    "mime"  
    "net/http"  
    "sort"  
)  
  
// secret: App secret
func CalSign(req *http.Request, secret string) string {  
    queries := req.URL.Query()  
  
    // 提取所有查询参数，排除 sign 和 access_token
    keys := make([]string, len(queries))  
    idx := 0  
    for k := range queries {  
        // 排除 'sign' 和 'access_token' 参数
        if k != "sign" && k != "access_token" {  
            keys[idx] = k  
            idx++  
        }  
    }  
      
    // 按字母顺序重新排列参数键
    sort.Slice(keys, func(i, j int) bool {  
        return keys[i] < keys[j]  
    })  
  
    // 按 {key}{value} 格式拼接所有参数
    input := ""  
    for _, key := range keys {  
        input = input + key + queries.Get(key)  
    }  
  
    // 追加请求路径
    input = req.URL.Path + input  
  
    // 如果请求 header Content-type 不是 multipart/form-data，则在末尾追加 body
    mediaType, _, _ := mime.ParseMediaType(req.Header.Get("Content-type"))  
    if mediaType != "multipart/form-data" {  
        body, _ := io.ReadAll(req.Body)  
        input = input + string(body)  
          
        req.Body.Close()  
        // 从原始 body 读取后重置
        req.Body = io.NopCloser(bytes.NewReader(body))  
    }  
  
    // 用 App secret 包裹第 5 步生成的字符串
    input = secret + input + secret  
  
    return generateSHA256(input, secret)  
}  
  
func generateSHA256(input, secret string) string {  
    // 将摘要字节流编码为十六进制，使用 sha256 以 salt(secret) 生成签名
    h := hmac.New(sha256.New, []byte(secret))  
  
    if _, err := h.Write([]byte(input)); err != nil {  
        // TODO 错误日志
        return ""  
    }  
  
    return hex.EncodeToString(h.Sum(nil))  
}
```

## 签名算法（Java）
```Java
package org.example;

import okhttp3.HttpUrl;
import okhttp3.Request;
import okhttp3.RequestBody;
import okio.Buffer;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public String generateSignature(Request request, String secret) {
    HttpUrl httpUrl = request.url();
    List<String> parameterNameList = new ArrayList<>(httpUrl.queryParameterNames());

    // 提取所有查询参数，排除 sign 和 access_token
    parameterNameList.removeIf(param -> "sign".equals(param) || "access_token".equals(param));

    // 按字母顺序重新排列参数键
    Collections.sort(parameterNameList);

    // 追加请求路径
    StringBuilder parameterStr = new StringBuilder(httpUrl.encodedPath());
    for (String parameterName : parameterNameList) {
        // 按 {key}{value} 格式拼接所有参数
        parameterStr.append(parameterName).append(httpUrl.queryParameter(parameterName));
    }

    // 如果请求 header Content-type 不是 multipart/form-data，则在末尾追加 body
    String contentType = request.header("Content-Type");
    if (!"multipart/form-data".equalsIgnoreCase(contentType)) {
        try {
            RequestBody requestBody = request.body();
            if (requestBody != null) {
                Buffer bodyBuffer = new Buffer();
                requestBody.writeTo(bodyBuffer);
                byte[] bodyBytes = bodyBuffer.readByteArray();
                parameterStr.append(new String(bodyBytes, StandardCharsets.UTF_8));
            }
        } catch (Exception e) {
            throw new RuntimeException("failed to generate signature params", e);
        }
    }

    // 用 App secret 包裹第 5 步生成的字符串
    String signatureParams = secret + parameterStr + secret;

    // 使用 HMAC-SHA256 编码包裹后的字符串
    return generateSHA256(signatureParams, secret);
}

/**
 * 使用 SHA256 生成签名
 * @param signatureParams 签名参数
 * @return 签名
 */
public String generateSHA256(String signatureParams, String secret) {
    try {
        // 获取 HmacSHA256 Mac 实例并使用密钥初始化
        Mac sha256HMAC = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKeySpec = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
        sha256HMAC.init(secretKeySpec);

        // 更新输入数据
        sha256HMAC.update(signatureParams.getBytes(StandardCharsets.UTF_8));

        // 计算 HMAC 并获取结果
        byte[] hashBytes = sha256HMAC.doFinal();

        // 转换为十六进制字符串
        StringBuilder sb = new StringBuilder();
        for (byte hashByte : hashBytes) {
            sb.append(String.format("%02x", hashByte & 0xff));
        }

        return sb.toString();
    } catch (Exception e) {
        throw new RuntimeException("failed to generate signature result", e);
    }
}
}
```

## 签名算法（Node.js）
```TypeScript
import crypto from "crypto";
import localVarRequest from "request";
const excludeKeys = ["access_token", "sign"] as const;
export const generateSign = (
  requestOption: localVarRequest.Options,
  app_secret: string
) => {
  let signString = "";
  // 步骤1：提取所有查询参数，排除 sign 和 access_token。按字母顺序重新排列参数键：
  const params = requestOption.qs || {};
  const sortedParams = Object.keys(params)
    .filter((key) => !excludeKeys.includes(key as any))
    .sort()
    .map((key) => ({ key, value: params[key] }));
  // 步骤2：按 {key}{value} 格式拼接所有参数：
  const paramString = sortedParams
    .map(({ key, value }) => `${key}${value}`)
    .join("");

  signString += paramString;

  // 步骤3：将步骤2的字符串追加到 API 请求路径：
// @ts-ignore
  const pathname = new URL(requestOption!.uri!||'').pathname;

  signString = `${pathname}${paramString}`;

  // 步骤4：如果请求 header content-type 不是 multipart/form-data，则将 API 请求 body 追加到步骤3的字符串：
  if (
    requestOption.headers?.["content-type"] !== "multipart/form-data" &&
    requestOption.body &&
    Object.keys(requestOption.body).length
  ) {
    const body = JSON.stringify(requestOption.body);
    signString += body;
  }

  // 步骤5：用 app_secret 包裹步骤4生成的字符串：
  signString = `${app_secret}${signString}${app_secret}`;

  // 步骤6：使用 HMAC-SHA256 编码包裹后的字符串：
  const hmac = crypto.createHmac("sha256", app_secret);
  hmac.update(signString);
  const sign = hmac.digest("hex");

  return sign;
};
```

## 签名算法（Python）
```Python
import hmac
import hashlib
from urllib.parse import urlparse
import json

def generate_sign(request_option, app_secret):
    """
    生成 HMAC-SHA256 签名
    :param request_option: 请求选项字典，包含 qs（查询参数）、uri（路径）、headers、body 等
    :param app_secret: 签名密钥
    :return: 十六进制签名字符串
    """
    # 步骤1：提取并过滤查询参数，排除 "access_token" 和 "sign"，按字母顺序排序
    params = request_option.get('qs', {})
    exclude_keys = ["access_token", "sign"]
    sorted_params = [
        {"key": key, "value": params[key]}
        for key in sorted(params.keys())
        if key not in exclude_keys
    ]

    # 步骤2：按 {key}{value} 格式拼接参数
    param_string = ''.join([f"{item['key']}{item['value']}" for item in sorted_params])
    sign_string = param_string

    # 步骤3：将 API 请求路径追加到签名字符串
    uri = request_option.get('uri', '')
    pathname = urlparse(uri).path if uri else ''
    sign_string = f"{pathname}{param_string}"

    # 步骤4：如果不是 multipart/form-data 且存在请求 body，则追加要发送的确切 body 字符串
    content_type = request_option.get('headers', {}).get('content-type', '')
    body = request_option.get('body', {})
    if content_type != 'multipart/form-data' and body:
        if isinstance(body, str):
            body_str = body
        else:
            body_str = json.dumps(body, separators=(',', ':'))  # 保持 JSON 序列化紧凑，与请求 body 一致
        sign_string += body_str

    # 步骤5：用 app_secret 包裹签名字符串
    wrapped_string = f"{app_secret}{sign_string}{app_secret}"

    # 步骤6：使用 HMAC-SHA256 编码并生成十六进制签名
    hmac_obj = hmac.new(
        app_secret.encode('utf-8'),
        wrapped_string.encode('utf-8'),
        hashlib.sha256
    )
    sign = hmac_obj.hexdigest()
    return sign
```

# 逐步分解
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9204af7b93b648a4abd51f5969b24bec~tplv-k9wyc2ijk0-image.image)
以下是签名算法工作原理的逐步分解：
📌 **注意**：如果您不需要逐步分解，可以直接跳到**签名算法**部分。我们提供了 Go、Java、Node.js 和 Python 的示例代码。

1. 以调用 Get Authorized Shops endpoint 为例，假设您的 `app_secret` 为 **e59af819cc**：

```HTTP
curl -X GET \
 'https://open-api.tiktokglobalshop.com/authorization/202309/shops?app_key=29a39d&sign=b596b73e0cc6de07ac26f036364178ab16b0a907af13d43f0a0cd2345f582dc8&timestamp=1623812664' \
-H 'x-tts-access-token: TTP_pwSm2AAAAABmmtFz1xlyKMnwg74T2GJ5s0uQbS8jPjb_GkdFVCxPqzQXSyuyfXdQa0AqyDsea2tYFNVf4XeqgZHFfPyv0Vs659QqyLYfsGzanZ5XZAin3_ZkcIxxS0_In6u6XDeU96k' \
-H 'content-type: application/json'
```


2. 提取所有查询参数，排除 `sign` 和 `access_token`。按字母顺序重新排列参数键：

```Go
keys := make([]string, len(queries))    
idx := 0    
for k := range queries {    
    // 排除 'sign' 和 'access_token' 参数
    if k != "sign" && k != "access_token" {    
       keys[idx] = k    
       idx++    
    }    
}    
sort.Slice(keys, func(i, j int) bool {    
    return keys[i] < keys[j]    
})
```

重新排列后的查询键结果为：
```Plain Text
keys = []string{    
    "app_key",       
    "timestamp"    
}
```

📌 **注意**：某些 API endpoint 需要 **shop_cipher** 查询参数，该参数将被包含在重新排列的查询键中。请调用 [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops) 获取店铺对应的 **shop_cipher**。

3. 按 `{key}{value}` 格式拼接所有参数：

```Go
// 按 {key}{value} 格式拼接所有参数
input := ""    
for _, key := range keys {      
   input = input + key + queries.Get(key)      
}
```

拼接后的字符串为：
```Plain Text
app_key29a39dtimestamp1623812664
```


4. 将步骤3的字符串追加到 API 请求路径。Get Authorized Shops 的路径为 `/authorization/202309/shops`：

```Plain Text
input = path + input
```

拼接后的字符串为：
```Plain Text
/authorization/202309/shopsapp_key29a39dtimestamp1623812664
```

📌 **注意**：如果请求 header content-type 不是 multipart/form-data，还需将 API 请求 body 追加到字符串中。使用 HTTP 请求中发送的确切 body 字节。不要解析并重新序列化或重新格式化 body 进行签名，因为字段顺序、空格、转义或字符集的变化可能产生不同的签名。
```Plain Text
input = input + body
```

例如，[Update Shop Webhook](https://partner.tiktokshop.com/docv2/page/update-shop-webhook) endpoint 在 API 请求 body 中包含 address 和 event_type 参数（以及查询参数中的 shop_cipher 参数）。这将产生以下结果：
```Plain Text
/event/202309/webhooksapp_key68xu9ks5p4i8shop_cipherROW_xkMbgAAAeVAQra0eZWebFQq5aIKtimestamp1696909648{"address":"https://partner.tiktokshop.com","event_type":"PACKAGE_UPDATE"}
```


5. 用您的 `app_secret` 包裹步骤4生成的字符串：

```Plain Text
input = app_secret + input + app_secret
```

最终字符串为：
```Plain Text
e59af819cc/authorization/202309/shopsapp_key29a39dtimestamp1623812664e59af819cc
```


6. 使用 **HMAC-SHA256** 编码包裹后的字符串：

```Go
import (      
   "crypto/hmac"      
   "crypto/sha256"      
   "encoding/hex"      
   "sort"      
)      
/**      
** input: 步骤5中创建的字符串
** secret: App secret      
**/      
func generateSHA256(input, secret string) string{      
   // 将摘要字节流编码为十六进制，使用 sha256 以 salt(secret) 生成签名
   h := hmac.New(sha256.New, []byte(secret))      
  
   if _, err := h.Write([]byte(input)); err != nil{      
      // TODO 错误日志
      return ""      
   }      
      
   return hex.EncodeToString(h.Sum(nil))      
}
```

生成的签名结果为：
```Plain Text
b596b73e0cc6de07ac26f036364178ab16b0a907af13d43f0a0cd2345f582dc8
```

# 常见错误
在 API 调用中遇到"签名无效"错误的最常见原因是什么？

* 通常，此错误发生在开发者使用错误的 app key 和 secret 生成签名时。必须验证 app key 和 secret 是否精确匹配。
* 确保 `sign` 和 `access_token` **未**包含在重新排列的查询键中（步骤2）。
* 对于 API 版本 `202309` 及更高版本，在 `x-tts-access-token` header 中发送 access token。不要将此 header 值包含在签名字符串中。
* 始终确保使用 **HMAC-SHA256** 签名方法（不同于普通的 SHA-256）。
* 确保时间戳在平台收到请求时的当前时间 5 分钟以内。时间戳必须表示为 10 位 Unix 时间戳。
* 如果请求不是 `multipart/form-data`，请对您发送的确切 body 字节进行签名。重新序列化 JSON 可能改变空格、字段顺序或转义，导致签名验证失败。
