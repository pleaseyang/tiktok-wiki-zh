# Large File Uploads Solution Guide

# Status quo and background
Large file upload is designed to support file sizes that exceed the existing direct-upload limit. The previous direct-upload solution loaded the whole file into memory, which could create Out of Memory (OOM) risk for gateway services and limit new business scenarios.
The chunked upload solution supports stable uploads for large videos, high-definition images, PDF files, and other supported media types. A single file can support up to 1 GB, subject to the limit of the specific business scenario.

* Customer Service supports files up to **100 MB**.
* Shoppable Video supports files up to **500 MB**.
* For files smaller than **10 MB**, continue to use the existing direct-upload API for the corresponding business scenario.
* For files larger than **10 MB**, use the chunked upload flow described in this guide.

# Technical solution overview
Large file upload uses a business file gateway and chunked upload model:

1. The client initializes an upload session through OpenAPI.
2. The client splits the local file into chunks and uploads them to the returned `upload_url`.
3. The file gateway merges the chunks automatically after the final chunk succeeds.
4. The client binds the returned `resource_id` to the target business resource.

Key capabilities:

* **Upload token**: `upload_token` is returned by the upload initialization API and is the credential for the chunk upload session. Treat it as short-lived and upload-session specific.
* **Security and authentication**: Upload initialization uses standard OpenAPI authentication. Chunk upload uses the returned `upload_url`, `upload_token`, `x-tts-access-token`, and required identifiers such as `shop_cipher`.
* **Compliance**: The file gateway and OpenAPI gateway use the same open-api domain and traffic scheduling policies so that file traffic stays in the corresponding compliance unit.

# Version and endpoint conventions
Use the following endpoint for upload initialization in this guide:
```Plain Text
[POST] /open/202512/file/init
```

Do not use legacy upload-init paths copied from earlier drafts. The upload init API reference is [Upload File Init](https://partner.tiktokshop.com/docv2/page/upload-file-init-202512).
`target_path` is the path of the later business binding API. It may use a different API version because it belongs to the target business API, not to Upload File Init. For example, the Customer Service binding API is [Send Message](https://partner.tiktokshop.com/docv2/page/send-message-202309).
# Large file upload process
Large file uploads are divided into three steps:
| ID | Step | Flow | API path | Description |
| --- | --- | --- | --- | --- |
| 1 | Initialize Upload | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4d9955462e5c4f09a2de65d8c340179b~tplv-k9wyc2ijk0-image.image) | `[POST] /open/202512/file/init` | Call the initialization API before uploading file chunks. The response returns `data.upload_url` and `data.upload_token`. |
| 2 | Chunk Upload and Completion | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/2a8f3fbedfb64b5a9415b4c4a47f565a~tplv-k9wyc2ijk0-image.image) | `[PUT] {upload_url}` returned by Upload File Init | Split the file into chunks and upload each chunk to `data.upload_url`. Set `chunk_num` starting from 1. After the last chunk succeeds, the gateway merges the chunks and returns `data.resource_id`. No extra merge API is required. |
| 3 | Bind Resource | ![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/0a2c6728c85b432caa4be5ef00232d2f~tplv-k9wyc2ijk0-image.image) | Varies by business. Example: `[POST] /customer_service/202309/conversations/{conversation_id}/messages` | Call the business-specific resource binding API and pass the `resource_id`. In Customer Service, pass `resource_id` as the `vid` parameter of [Send Message](https://partner.tiktokshop.com/docv2/page/send-message-202309). |
# API details
# 1. Initialize upload
Use [Upload File Init](https://partner.tiktokshop.com/docv2/page/upload-file-init-202512) to obtain the target upload URL and upload token.
**Endpoint**
```Plain Text
[POST] /open/202512/file/init
```

**Common query parameters**
| Parameter | Type | Description |
| --- | --- | --- |
| `app_key` | String | Your app key. |
| `timestamp` | Integer | Current Unix timestamp in seconds. |
| `sign` | String | Request signature. For signing rules, refer to [Sign your API request](https://partner.tiktokshop.com/docv2/page/sign-your-api-request). |

**Headers**
| Header | Type | Description |
| --- | --- | --- |
| `Content-Type` | String | `application/json`. |
| `x-tts-access-token` | String | The access token of the authorized user. |

**Request body**
| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `file_size` | Integer | Yes | Total file size in bytes. |
| `file_name` | String | Yes | File name, including the extension, such as `my_video.mp4`. |
| `total_chunk_count` | Integer | Yes | Total number of chunks that will be uploaded. |
| `file_type` | String | Yes | File type. Supported values: `video`, `image`, `pdf`. |
| `target_path` | String | Yes | The API path of the target resource binding endpoint, used for permission checks and routing. Example: `[POST]/customer_service/202309/conversations/{conversation_id}/messages`. |

**Success response**
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

Use `data.upload_url` exactly as returned. Do not reconstruct it from the examples, because the returned URL may include routing information.
# 2. Upload file chunk
Upload each chunk to `data.upload_url` from Upload File Init.
**Endpoint**
```Plain Text
[PUT] {upload_url}
```

**Query parameters**
| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `upload_token` | String | Yes | Upload token returned by Upload File Init. |
| `chunk_num` | Integer | Yes | Sequence number of the current chunk, starting from 1. |
| `app_key` | String | Yes | Your app key. |
| `shop_cipher` | String | Conditional | Required for shop-scoped uploads when the token is associated with a TikTok Shop seller, such as `user_type=0` (`TTS`). Obtain it from [Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309). Do not use the legacy label `user_type=3 (Partner)`: token `user_type` values are `0=TTS`, `1=TTC`, `2=PARTNER`, `3=PARTNERV2`, `4=GS`, and `5=GSV2`. For partner token uploads, follow the target business API's identifier requirement. |

**Headers**
| Header | Type | Description |
| --- | --- | --- |
| `Content-Type` | String | MIME type of the chunk. It must be compatible with the `file_type` declared during initialization. |
| `x-tts-access-token` | String | The authorized user's access token. |

**Request body**
The request body is the binary data of the current chunk.
**Chunk size**
Set the default chunk size to **20 MB**. Each chunk should be between **5 MB** and **30 MB**. If the final chunk would be smaller than 5 MB, merge it into the previous chunk.
**Response examples**
When a non-final chunk succeeds:
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

When the final chunk succeeds and the merge is complete:
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

# Supported content types
| File category | `file_type` | Supported `Content-Type` values |
| --- | --- | --- |
| Video | `video` | `video/mp4`, `video/quicktime`, `video/webm` |
| Image | `image` | `image/png`, `image/jpeg` |
| PDF | `pdf` | `application/pdf` |
# 3. Bind resource
After you receive `data.resource_id` from the final chunk response, call the target business API to associate the uploaded resource with your business object.
For example, in the Customer Service business, call [Send Message](https://partner.tiktokshop.com/docv2/page/send-message-202309) and pass `resource_id` as the `vid` parameter.
# Validation process
During chunk upload, the gateway validates:

1. **Size accumulation**: The gateway accumulates uploaded chunk sizes and checks them against the `file_size` declared during initialization.
2. **Content type**: The `Content-Type` of each chunk must match the `file_type` declared during initialization.
3. **Chunk count**: The gateway merges the file after all chunks in `total_chunk_count` have been uploaded successfully.
4. **Identifiers**: For shop-scoped uploads, the request must include the correct `shop_cipher` for the access token and target shop.

# cURL example
# Initialize upload
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

Expected response:
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

# Upload chunk
Use the `data.upload_url` and `data.upload_token` returned by Upload File Init.
```Bash
curl -X PUT 'https://open-api.tiktokglobalshop.com/file/v1/upload?upload_token=RETURNED_UPLOAD_TOKEN&chunk_num=1&app_key=YOUR_APP_KEY&shop_cipher=YOUR_SHOP_CIPHER' \
  -H 'Content-Type: video/mp4' \
  -H 'Content-Length: 20971520' \
  -H 'x-tts-access-token: USER_ACCESS_TOKEN' \
  --data-binary '@/path/to/your/local/file_chunk_1.dat'
```

If `shop_cipher` is not required for your token type and target API, omit it from the chunk upload query.
# Go example
The following example initializes an upload session, splits a local file into 20 MB chunks, merges a final chunk smaller than 5 MB into the previous chunk, uploads chunks sequentially, and returns the final chunk response.
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

        if len(chunks) >= 2 {
                last := chunks[len(chunks)-1]
                if last.end-last.start < minChunkSize {
                        chunks[len(chunks)-2].end = last.end
                        chunks = chunks[:len(chunks)-1]
                }
        }
        return chunks
}

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

# FAQ
# Q1: How should I set the chunk size?
Set the default chunk size to **20 MB**. The valid chunk size range is **5-30 MB**. If the final chunk is smaller than **5 MB**, merge it into the previous chunk. This keeps the implementation consistent with the Go example and avoids small-tail upload failures.
# Q2: Why does my 68 MB local file show as only 65 MB after being uploaded to the video cloud?
This is normal. Videos may be processed after upload, such as encapsulation or compression, so there may be a slight file size discrepancy. This does not affect video publishing or subsequent posting processes.
# Q3: Are there any limitations in the sandbox environment?
Yes. The **QPH (Queries Per Hour) limit for sandbox apps is 10**. This is intended for functional verification only and is not suitable for high-frequency testing.
# Q4: What should I do before downloading the SDK?
Before downloading the SDK:

1. Click **Check for updates**.
2. Update your development tools to the latest version.
3. Download the SDK again.

Failure to update your tools may lead to SDK download failures or version mismatch issues.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/72215ea66ff94d00b3435dff4776facd~tplv-k9wyc2ijk0-image.image)
