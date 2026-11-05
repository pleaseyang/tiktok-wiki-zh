# 大文件上传解决方案指南

# 现状与背景
大文件上传功能旨在支持超出现有直接上传限制的文件大小。之前的直接上传方案会将整个文件加载到内存中，这可能给网关服务带来内存溢出（OOM）风险，并限制新的业务场景。
分块上传方案支持大视频、高清图片、PDF 文件及其他支持的媒体类型的稳定上传。单个文件最大支持 1 GB，具体取决于业务场景的限制。

* 客服场景支持最大 **100 MB** 的文件。
* 可购物视频场景支持最大 **500 MB** 的文件。
* 小于 **10 MB** 的文件，请继续使用对应业务场景的现有直接上传 API。
* 大于 **10 MB** 的文件，请使用本指南中描述的分块上传流程。

# 技术方案概述
大文件上传使用业务文件网关和分块上传模型：

1. 客户端通过 OpenAPI 初始化上传会话。
2. 客户端将本地文件分割为多个分块，并上传到返回的 `upload_url`。
3. 文件网关在最后一个分块上传成功后自动合并分块。
4. 客户端将返回的 `resource_id` 绑定到目标业务资源。

核心能力：

* **上传令牌**：`upload_token` 由上传初始化 API 返回，是分块上传会话的凭证。请将其视为短期有效且特定于上传会话的令牌。
* **安全与认证**：上传初始化使用标准 OpenAPI 认证。分块上传使用返回的 `upload_url`、`upload_token`、`x-tts-access-token` 以及 `shop_cipher` 等必需标识符。
* **合规性**：文件网关和 OpenAPI 网关使用相同的 open-api 域名和流量调度策略，确保文件流量保持在对应的合规单元中。

# 版本与 endpoint 约定
本指南中的上传初始化使用以下 endpoint：
```Plain Text
[POST] /open/202512/file/init
```

请勿使用从早期草稿中复制的旧版上传初始化路径。上传初始化 API 参考文档为 [Upload File Init](https://partner.tiktokshop.com/docv2/page/upload-file-init-202512)。
`target_path` 是后续业务绑定 API 的路径。它可能使用不同的 API 版本，因为它属于目标业务 API，而非 Upload File Init。例如，客服绑定 API 为 [Send Message](https://partner.tiktokshop.com/docv2/page/send-message-202309)。
# 大文件上传流程
大文件上传分为三个步骤：
| ID | 步骤 | 流程 | API 路径 | 描述 |
| --- | --- | --- | --- | --- |
| 1 | 初始化上传 | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4d9955462e5c4f09a2de65d8c340179b~tplv-k9wyc2ijk0-image.image) | `[POST] /open/202512/file/init` | 在上传文件分块之前调用初始化 API。响应返回 `data.upload_url` 和 `data.upload_token`。 |
| 2 | 分块上传与完成 | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2a8f3fbedfb64b5a9415b4c4a47f565a~tplv-k9wyc2ijk0-image.image) | Upload File Init 返回的 `[PUT] {upload_url}` | 将文件分割为多个分块，逐个上传到 `data.upload_url`。`chunk_num` 从 1 开始。最后一个分块上传成功后，网关自动合并分块并返回 `data.resource_id`。无需额外的合并 API。 |
| 3 | 绑定资源 | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/0a2c6728c85b432caa4be5ef00232d2f~tplv-k9wyc2ijk0-image.image) | 因业务而异。示例：`[POST] /customer_service/202309/conversations/{conversation_id}/messages` | 调用特定业务的资源绑定 API，传入 `resource_id`。在客服场景中，将 `resource_id` 作为 [Send Message](https://partner.tiktokshop.com/docv2/page/send-message-202309) 的 `vid` 参数传入。 |
# API 详情
# 1. 初始化上传
使用 [Upload File Init](https://partner.tiktokshop.com/docv2/page/upload-file-init-202512) 获取目标上传 URL 和上传令牌。
**Endpoint**
```Plain Text
[POST] /open/202512/file/init
```

**公共查询参数**
| 参数 | 类型 | 描述 |
| --- | --- | --- |
| `app_key` | String | 您的 app key。 |
| `timestamp` | Integer | 当前 Unix 时间戳（秒）。 |
| `sign` | String | 请求签名。签名规则请参考 [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request)。 |

**Headers**
| Header | 类型 | 描述 |
| --- | --- | --- |
| `Content-Type` | String | `application/json`。 |
| `x-tts-access-token` | String | 已授权用户的 access token。 |

**请求体**
| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `file_size` | Integer | 是 | 文件总大小（字节）。 |
| `file_name` | String | 是 | 文件名，包含扩展名，如 `my_video.mp4`。 |
| `total_chunk_count` | Integer | 是 | 将要上传的分块总数。 |
| `file_type` | String | 是 | 文件类型。支持的值：`video`、`image`、`pdf`。 |
| `target_path` | String | 是 | 目标资源绑定 endpoint 的 API 路径，用于权限检查和路由。示例：`[POST]/customer_service/202309/conversations/{conversation_id}/messages`。 |

**成功响应**
```JSON
{
  "code": 0,
  "data": {
    "upload_url": "https://open-api.tiktokglobalshop.com/file/v1/upload",
    "upload_token": "RETURNED_UPLOAD_TOKEN"
  },
  "message": "Success",
  "request_id": "20251201000000000000000000000000"
}
```

请严格按照返回的 `data.upload_url` 使用。不要从示例中重建 URL，因为返回的 URL 可能包含路由信息。
# 2. 上传文件分块
将每个分块上传到 Upload File Init 返回的 `data.upload_url`。
**Endpoint**
```Plain Text
[PUT] {upload_url}
```

**查询参数**
| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `upload_token` | String | 是 | Upload File Init 返回的上传令牌。 |
| `chunk_num` | Integer | 是 | 当前分块的序号，从 1 开始。 |
| `app_key` | String | 是 | 您的 app key。 |
| `shop_cipher` | String | 条件必填 | 当 token 关联到 TikTok Shop 卖家时（如 `user_type=0`（`TTS`）），店铺范围上传必需。从 [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) 获取。请勿使用旧标签 `user_type=3 (Partner)`：token `user_type` 值为 `0=TTS`、`1=TTC`、`2=PARTNER`、`3=PARTNERV2`、`4=GS` 和 `5=GSV2`。对于 partner token 上传，请遵循目标业务 API 的标识符要求。 |

**Headers**
| Header | 类型 | 描述 |
| --- | --- | --- |
| `Content-Type` | String | 分块的 MIME 类型。必须与初始化时声明的 `file_type` 兼容。 |
| `x-tts-access-token` | String | 已授权用户的 access token。 |

**请求体**
请求体为当前分块的二进制数据。
**分块大小**
默认分块大小设置为 **20 MB**。每个分块应在 **5 MB** 到 **30 MB** 之间。如果最后一个分块小于 5 MB，请将其合并到前一个分块中。
**响应示例**
当非最后一个分块上传成功时：
```JSON
{
  "code": 0,
  "data": {
    "part_id": "PART_ID_FOR_THIS_CHUNK"
  },
  "message": "Success",
  "request_id": "20251201000000000000000000000001"
}
```

当最后一个分块上传成功且合并完成时：
```JSON
{
  "code": 0,
  "data": {
    "resource_id": "FINAL_RESOURCE_ID"
  },
  "message": "Success",
  "request_id": "20251201000000000000000000000002"
}
```

# 支持的内容类型
| 文件类别 | `file_type` | 支持的 `Content-Type` 值 |
| --- | --- | --- |
| 视频 | `video` | `video/mp4`、`video/quicktime`、`video/webm` |
| 图片 | `image` | `image/png`、`image/jpeg` |
| PDF | `pdf` | `application/pdf` |
# 3. 绑定资源
在从最后一个分块响应中收到 `data.resource_id` 后，调用目标业务 API 将上传的资源与您的业务对象关联。
例如，在客服业务中，调用 [Send Message](https://partner.tiktokshop.com/docv2/page/send-message-202309) 并将 `resource_id` 作为 `vid` 参数传入。
# 验证流程
在分块上传过程中，网关会验证：

1. **大小累计**：网关累计已上传分块的大小，并与初始化时声明的 `file_size` 进行校验。
2. **内容类型**：每个分块的 `Content-Type` 必须与初始化时声明的 `file_type` 匹配。
3. **分块计数**：网关在 `total_chunk_count` 中的所有分块上传成功后合并文件。
4. **标识符**：对于店铺范围的上传，请求必须包含对应 access token 和目标店铺的正确 `shop_cipher`。

# cURL 示例
# 初始化上传
```Bash
curl -X POST 'https://open-api.tiktokglobalshop.com/open/202512/file/init?app_key=YOUR_APP_KEY&timestamp=1710000000&sign=YOUR_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -H 'x-tts-access-token: USER_ACCESS_TOKEN' \
  -d '{
    "file_size": 20971520,
    "file_name": "test_video.mp4",
    "total_chunk_count": 1,
    "file_type": "video",
    "target_path": "[POST]/customer_service/202309/conversations/{conversation_id}/messages"
  }'
```

预期响应：
```JSON
{
  "code": 0,
  "data": {
    "upload_url": "https://open-api.tiktokglobalshop.com/file/v1/upload",
    "upload_token": "RETURNED_UPLOAD_TOKEN"
  },
  "message": "Success",
  "request_id": "20251201000000000000000000000000"
}
```

# 上传分块
使用 Upload File Init 返回的 `data.upload_url` 和 `data.upload_token`。
```Bash
curl -X PUT 'https://open-api.tiktokglobalshop.com/file/v1/upload?upload_token=RETURNED_UPLOAD_TOKEN&chunk_num=1&app_key=YOUR_APP_KEY&shop_cipher=YOUR_SHOP_CIPHER' \
  -H 'Content-Type: video/mp4' \
  -H 'Content-Length: 20971520' \
  -H 'x-tts-access-token: USER_ACCESS_TOKEN' \
  --data-binary '@/path/to/your/local/file_chunk_1.dat'
```

如果您的 token 类型和目标 API 不需要 `shop_cipher`，请在分块上传查询中省略它。
# Go 示例
以下示例初始化一个上传会话，将本地文件分割为 20 MB 的分块，将小于 5 MB 的最后一个分块合并到前一个分块中，按顺序上传分块，并返回最后一个分块的响应。
```Go
package main

import (
        "bytes"
        "context"
        "crypto/hmac"
        "crypto/sha256"
        "encoding/hex"
        "encoding/json"
        "errors"
        "fmt"
        "io"
        "log"
        "mime"
        "net/http"
        "net/url"
        "os"
        "path/filepath"
        "sort"
        "strconv"
        "strings"
        "time"
)

const apiVersion = "202512"
const defaultChunkSize = 20 * 1024 * 1024
const minChunkSize = 5 * 1024 * 1024

type OpenAPIClient struct {
        BaseURL     string
        AccessToken string
        AppKey      string
        AppSecret   string
        HTTP        *http.Client
}

func New(baseURL, accessToken, appKey, appSecret string) *OpenAPIClient {
        return &OpenAPIClient{
                BaseURL:     strings.TrimRight(baseURL, "/"),
                AccessToken: accessToken,
                AppKey:      appKey,
                AppSecret:   appSecret,
                HTTP:        &http.Client{Timeout: 60 * time.Second},
        }
}

type UploadInitRequest struct {
        FileSize        int64  `json:"file_size"`
        TotalChunkCount int    `json:"total_chunk_count"`
        FileType        string `json:"file_type"`
        TargetPath      string `json:"target_path"`
        FileName        string `json:"file_name"`
}

type UploadInitResponse struct {
        Code int `json:"code"`
        Data struct {
                UploadURL   string `json:"upload_url"`
                UploadToken string `json:"upload_token"`
        } `json:"data"`
        Message   string `json:"message"`
        RequestID string `json:"request_id"`
}

// 初始化上传会话，获取上传 URL 和 token
func (c *OpenAPIClient) UploadInit(ctx context.Context, body UploadInitRequest) (*UploadInitResponse, error) {
        apiPath := "/open/" + apiVersion + "/file/init"
        bodyBytes, err := json.Marshal(body)
        if err != nil {
                return nil, err
        }

        timestamp := strconv.FormatInt(time.Now().Unix(), 10)
        signParams := map[string]string{
                "app_key":   c.AppKey,
                "timestamp": timestamp,
        }

        query := url.Values{}
        query.Set("app_key", c.AppKey)
        query.Set("timestamp", timestamp)
        query.Set("sign", c.computeSign(apiPath, signParams, "application/json", bodyBytes))

        req, err := http.NewRequestWithContext(ctx, http.MethodPost, c.BaseURL+apiPath+"?"+query.Encode(), bytes.NewReader(bodyBytes))
        if err != nil {
                return nil, err
        }
        req.Header.Set("Content-Type", "application/json")
        req.Header.Set("x-tts-access-token", c.AccessToken)

        resp, err := c.HTTP.Do(req)
        if err != nil {
                return nil, err
        }
        defer resp.Body.Close()

        respBody, err := io.ReadAll(resp.Body)
        if err != nil {
                return nil, err
        }
        log.Printf("UploadInit status=%d logid=%s", resp.StatusCode, resp.Header.Get("X-Tt-Logid"))

        var parsed UploadInitResponse
        if err := json.Unmarshal(respBody, &parsed); err != nil {
                return nil, err
        }
        if parsed.Code != 0 {
                return nil, fmt.Errorf("upload init failed: %s", parsed.Message)
        }
        if parsed.Data.UploadURL == "" || parsed.Data.UploadToken == "" {
                return nil, errors.New("upload init response missing upload_url or upload_token")
        }
        return &parsed, nil
}

type chunkRange struct {
        start int64
        end   int64
}

// 构建分块范围，如果最后一个分块小于最小分块大小则合并到前一个分块
func buildChunkRanges(size int64) []chunkRange {
        if size <= 0 {
                return []chunkRange{{start: 0, end: 0}}
        }

        chunks := make([]chunkRange, 0, int(size/defaultChunkSize)+1)
        for start := int64(0); start < size; start += defaultChunkSize {
                end := start + defaultChunkSize
                if end > size {
                        end = size
                }
                chunks = append(chunks, chunkRange{start: start, end: end})
        }

        // 如果最后一个分块小于最小分块大小，将其合并到前一个分块
        if len(chunks) >= 2 {
                last := chunks[len(chunks)-1]
                if last.end-last.start < minChunkSize {
                        chunks[len(chunks)-2].end = last.end
                        chunks = chunks[:len(chunks)-1]
                }
        }
        return chunks
}

// 按顺序上传所有分块到上传 URL
func (c *OpenAPIClient) ChunkUpload(ctx context.Context, uploadURL, uploadToken, filePath, contentType, shopCipher string) (*http.Response, []byte, error) {
        file, err := os.Open(filePath)
        if err != nil {
                return nil, nil, err
        }
        defer file.Close()

        info, err := file.Stat()
        if err != nil {
                return nil, nil, err
        }

        chunks := buildChunkRanges(info.Size())
        var lastResp *http.Response
        var lastBody []byte

        for i, rg := range chunks {
                chunkNum := i + 1
                reader := io.NewSectionReader(file, rg.start, rg.end-rg.start)

                parsedURL, err := url.Parse(uploadURL)
                if err != nil {
                        return nil, nil, err
                }
                query := parsedURL.Query()
                query.Set("upload_token", uploadToken)
                query.Set("chunk_num", strconv.Itoa(chunkNum))
                query.Set("app_key", c.AppKey)
                if shopCipher != "" {
                        query.Set("shop_cipher", shopCipher)
                }
                parsedURL.RawQuery = query.Encode()

                req, err := http.NewRequestWithContext(ctx, http.MethodPut, parsedURL.String(), reader)
                if err != nil {
                        return nil, nil, err
                }
                req.Header.Set("Content-Type", contentType)
                req.Header.Set("x-tts-access-token", c.AccessToken)
                req.ContentLength = rg.end - rg.start

                resp, err := c.HTTP.Do(req)
                if err != nil {
                        return resp, nil, err
                }
                body, readErr := io.ReadAll(resp.Body)
                resp.Body.Close()
                if readErr != nil {
                        return resp, body, readErr
                }

                log.Printf("Chunk %d/%d status=%d logid=%s", chunkNum, len(chunks), resp.StatusCode, resp.Header.Get("X-Tt-Logid"))
                lastResp, lastBody = resp, body
        }

        return lastResp, lastBody, nil
}

// 完整的上传流程：初始化、分块、上传
func (c *OpenAPIClient) UploadFile(ctx context.Context, filePath, fileType, targetPath, shopCipher string) (*http.Response, []byte, error) {
        info, err := os.Stat(filePath)
        if err != nil {
                return nil, nil, err
        }

        ranges := buildChunkRanges(info.Size())
        initResp, err := c.UploadInit(ctx, UploadInitRequest{
                FileSize:        info.Size(),
                TotalChunkCount: len(ranges),
                FileName:        filepath.Base(filePath),
                FileType:        fileType,
                TargetPath:      targetPath,
        })
        if err != nil {
                return nil, nil, err
        }

        contentType := contentTypeForFile(filePath, fileType)
        return c.ChunkUpload(ctx, initResp.Data.UploadURL, initResp.Data.UploadToken, filePath, contentType, shopCipher)
}

// 根据文件扩展名和文件类型确定 Content-Type
func contentTypeForFile(filePath, fileType string) string {
        ext := strings.ToLower(filepath.Ext(filePath))
        switch {
        case fileType == "pdf" || ext == ".pdf":
                return "application/pdf"
        case ext == ".jpg" || ext == ".jpeg":
                return "image/jpeg"
        case ext == ".png":
                return "image/png"
        case ext == ".mov":
                return "video/quicktime"
        case ext == ".webm":
                return "video/webm"
        default:
                return "video/mp4"
        }
}

// 计算 API 请求签名
func (c *OpenAPIClient) computeSign(path string, params map[string]string, contentType string, body []byte) string {
        cleaned := make(map[string]string, len(params))
        for k, v := range params {
                if k != "sign" && k != "access_token" {
                        cleaned[k] = v
                }
        }

        keys := make([]string, 0, len(cleaned))
        for k := range cleaned {
                keys = append(keys, k)
        }
        sort.Strings(keys)

        input := path
        for _, k := range keys {
                input += k + cleaned[k]
        }

        if mediaType, _, err := mime.ParseMediaType(contentType); err != nil || mediaType != "multipart/form-data" {
                input += string(body)
        }

        input = c.AppSecret + input + c.AppSecret
        mac := hmac.New(sha256.New, []byte(c.AppSecret))
        _, _ = mac.Write([]byte(input))
        return hex.EncodeToString(mac.Sum(nil))
}

func main() {
        client := New(
                "https://open-api.tiktokglobalshop.com",
                os.Getenv("TTS_ACCESS_TOKEN"),
                os.Getenv("TTS_APP_KEY"),
                os.Getenv("TTS_APP_SECRET"),
        )

        _, body, err := client.UploadFile(
                context.Background(),
                "/path/to/test_video.mp4",
                "video",
                "[POST]/customer_service/202309/conversations/{conversation_id}/messages",
                os.Getenv("TTS_SHOP_CIPHER"),
        )
        if err != nil {
                log.Fatal(err)
        }
        log.Printf("Final upload response: %s", string(body))
}
```

# 常见问题
# Q1：如何设置分块大小？
默认分块大小设置为 **20 MB**。有效分块大小范围为 **5-30 MB**。如果最后一个分块小于 **5 MB**，请将其合并到前一个分块中。这使实现与 Go 示例保持一致，并避免小尾部分块上传失败。
# Q2：为什么我 68 MB 的本地文件上传到视频云后只显示 65 MB？
这是正常现象。视频在上传后可能会经过处理，如封装或压缩，因此可能存在轻微的文件大小差异。这不会影响视频发布或后续发布流程。
# Q3：沙箱环境有什么限制？
有。**沙箱应用的 QPH（每小时查询数）限制为 10**。这仅用于功能验证，不适合高频测试。
# Q4：下载 SDK 之前应该做什么？
在下载 SDK 之前：

1. 点击 **Check for updates**。
2. 将开发工具更新到最新版本。
3. 重新下载 SDK。

未更新工具可能导致 SDK 下载失败或版本不匹配问题。
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/72215ea66ff94d00b3435dff4776facd~tplv-k9wyc2ijk0-image.image)
