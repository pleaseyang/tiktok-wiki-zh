# FBT Inbound API 概述指南

**综合参考** — FBT Inbound 和商品创建 API 的入门指南、关键概念、工作流程图和商家集成指南。 

## 1. 概述
**FBT Inbound API** 套件使卖家和物流合作伙伴能够通过编程方式创建、管理和跟踪发送至 TikTok **Fulfillment by TikTok (FBT)** warehouse 的 inbound 货件。
### 新 API 能力
FBT 正在推出 **2 个新 API 组**，与现有 API（已支持 inventory 搜索、inbound 搜索和 inventory 记录）并行。
**① 创建 Inbound**
将 inventory 运送到 FBT warehouse 的端到端工作流程：

* 创建 inbound plan 并选择入库方案
* 确认运输方式并审核要求
* 打包并发货 — 提交箱或单位清单
* 获取运输标签并更新承运商追踪信息
* 根据需要管理和取消 inbound 订单

→ 涵盖于 **箱拆分** & **单位拆分**
**② 创建与匹配商品**
管理 FBT 商品目录并绑定 TikTok Shop SKU：

* 检查每个 SKU 的危险品和保质期要求
* 创建 FBT 商品记录并绑定到 Shop SKU
* 更新商品信息（尺寸、条形码、危险品信息）
* 管理 SKU 与商品的绑定关系（绑定 / 解绑）

→ 涵盖于 **商品管理**

### 支持的两种 Inbound 工作流程
**箱拆分**

* Inventory 在创建 inbound 和发货前已预装入箱中
* 每个箱包含一个或多个 SKU
* TikTok 按箱分配 warehouse

**单位拆分**

* 创建 inbound 时 inventory 尚未打包，打包信息在发货步骤中后续提供
* 基于流程的打包具有更高的灵活性


**所需权限范围**：`seller.fbt.inbound` — 两种工作流程中的所有 endpoint 都需要 seller access token 上的此权限。


## 2. 关键概念
FBT API 集成的核心术语。
### Merchant
**Merchant** 代表在 TikTok Shop 中使用 FBT 履约提供产品或服务销售的实体。每个商家都有一个唯一的 **FBT Merchant ID**，在任何 API 调用之前都需要。
> **获取 Merchant ID**：Merchant ID 在 FBT 入驻期间分配。在调用任何 inbound API 之前，使用 **Get FBT Merchant Onboarded Regions** 验证卖家是否已注册并获取其活跃区域。

### 商品
**FBT 商品**是 FBT 分配的唯一记录，用于在 Fulfilled by TikTok 系统中跟踪和管理单个卖家的 inventory。
商品必须**与 TikTok 产品 ID 匹配**，然后商家才能创建 inbound 货件、管理 inventory 或履约订单。如果商品与 SKU 取消匹配，相应的 inventory 将不再在 TikTok Shop 上可供销售。
**关键术语**
| Full Name | Who Assigns It | Used In |
| --- | --- | --- |
| TikTok Shop Product /SKU ID | TikTok Shop（来自您的产品目录） | CreateGoods, GetHazmatInfo, UpdateSkuRelation |
| FBT Goods ID | FBT 系统 — 在 CreateGoods 成功时返回 | UpdateGoods, UpdateSkuRelation, Inbound APIs |
**商品生命周期**

1. **检查要求** — 调用 *Get Hazmat & Expiration Info* 确定特殊处理需求
2. **创建并绑定** — 使用 `CREATE_AND_BIND` 调用 *Create Goods* 创建 FBT 商品记录并将其链接到 TikTok Shop SKU
3. **创建 inbound** — 匹配后，使用 Inbound API 发货 inventory
4. **管理绑定** — 使用 *Update Goods SKU Relation* 随时添加或删除 SKU 关联

**提示**：当商家启用渠道 inventory 时，单个 FBT 商品记录可以绑定到**多个 TikTok Shop SKU（1:N）** — 适用于在多个店铺或区域销售同一实物产品。

### FBT Warehouse
FBT warehouse 在**入驻后自动订阅**。有两种 warehouse 类型，各有不同的作用：
| Warehouse Type | Accepts Inbound | Fulfills Orders | Notes |
| --- | --- | --- | --- |
| **HUB** | ✅ 是 | ❌ 否 | 仅进行 inbound 处理和分拣 — inventory 在转为可售之前会转移到 FC。<br/> 收取 hub 入库费用，详见 FBT [商家学院](https://scm-us.tiktok.com/merchant-university/home)  |
| **FC**（Fulfillment Center） | ✅ 是 | ✅ 是 | 接收 inventory；用于订单履约。<br/> 商家无法手动选择，FBT placement 决定 FC。 |
使用 **Get FBT Warehouse List** 检索所有 warehouse ID、名称、地址和类型。创建 inbound plan 时需要返回的 `warehouse_id`。

## 3. 认证
每个 API 请求必须包含以下 header：
| Header | Value | Notes |
| --- | --- | --- |
| `content-type` | `application/json` | 所有请求必需 |
| `x-tts-access-token` | 您的 seller access token | 通过 TikTok Shop OAuth 获取（`user_type = 0`）。**Token 会过期** — 请在流程中加入刷新逻辑 |
**Example**
```HTTP
POST /fbt/202602/create_update_inbound_plan?shop_id=123456 HTTP/1.1
content-type: application/json
x-tts-access-token: eyJhbGciOiJSUzI1NiIsInR5cCI6...
```

**Token 过期**：Access token 会过期。在自动化流程中发起 API 调用前，请务必检查过期时间并使用 refresh token 刷新。


## 4. 开始之前 — 检查清单
在发起第一次 API 调用之前，请确认以下所有事项：

- [ ] 您拥有有效的 **FBT Merchant ID**（在 FBT 入驻期间分配）。使用 *Get FBT Merchant Onboarded Regions* 验证
- [ ] 您的 TikTok Shop 商品已通过商品管理 API 或 FBT 卖家门户**创建并匹配**到 FBT
- [ ] 您拥有具有 `seller.fbt.inbound` OAuth 权限的 **seller access token**
- [ ] 您已决定使用**箱拆分**（预装箱）还是**单位拆分**（散装单位）
- [ ] 您已决定使用 **Single_Hub（单次货件）** 还是 **D2FC（多次货件）** 发送至 FBT


## 5. 创建与匹配商品 — API 概述
在将 inventory 发送至 FBT 之前，卖家必须**创建 FBT 商品记录并将其与** TikTok Shop SKU 匹配。这些 API 通常应在创建 inbound plan **之前**调用。
### 推荐的商品设置顺序
| # | API | Method | Purpose | Key Output |
| --- | --- | --- | --- | --- |
| 1 | **Get Hazmat & Expiration Info** | POST | 在创建商品之前检查 SKU 是否有危险品分类或保质期规则。每次调用最多 50 个 SKU。 | 危险品标志、保质期规则 |
| 2 | **Create Goods** | POST | 创建 FBT 商品记录并绑定到 TikTok Shop SKU（`CREATE_AND_BIND`）。如果在步骤 1 中标记了危险品/保质期字段，请一并包含。 | `tts_goods_id` |
| 3 | **Update Goods** | POST | 编辑现有商品记录 — 名称、尺寸、条形码、退货处理、危险品/保质期信息。 | 更新确认 |
| 4 | **Update Goods SKU Relation** | POST | 管理 FBT 商品与 Shop SKU 之间的绑定关系。使用 `BIND` 添加或使用 `UN_BIND` 移除。 | 操作确认 |
### 关键商品参数
| Parameter | Where Used | Description |
| --- | --- | --- |
| `tt_sku_id` | GetHazmat, CreateGoods | TikTok Shop SKU ID — 来自卖家产品目录的主要标识符 |
| `tts_goods_id` | UpdateGoods, UpdateSkuRelation | FBT Goods ID — 在 CreateGoods 成功时分配。**请保存此值** |
| `create_goods_type` | CreateGoods | `CREATE_AND_BIND` — 创建 FBT 商品记录并在一次调用中绑定到 SKU |
| `operation_type` | UpdateSkuRelation | `BIND` 关联 SKU，`UN_BIND` 移除关联 |
### 特殊处理标志
某些产品在创建商品时需要额外的数据字段：

* **危险品**（`is_hazmat = true`）：必须提供包含 `hazmat_type`（`BATTERY`、`MAGNETIZED`、`FLAMMABLE_LIQUID`、`AEROSOLS`）及特定类型详情的 `hazmat_info`
* **电池产品**：需要电池类型（`LITHIUM_ION`、`LITHIUM_METAL`、`OTHER`）、容量、包装类型（`STANDALONE` / `IN_EQUIPMENT` / `WITH_EQUIPMENT`）和 UN 代码。请注意 SDS 适用于 

请参考下表了解危险品信息映射规则
| **Hazmat type** | **Class** | **How batteries are packed** | **Battery type** | **Flammable liquid type** | **Un code** |
| --- | --- | --- | --- | --- | --- |
| Battery | 9 | Standalone | Lithion Ion |  | UN 3480 |
| Battery | 9 | Standalone | Lithion metal |  | UN3090 |
| Battery | 9 | Standalone | Other |  | Other |
| Battery | 9 | In equipment | Lithion Ion |  | UN 3481 |
| Battery | 9 | In equipment | Lithion metal |  | UN3091 |
| Battery | 9 | In equipment | Other |  | Other |
| Battery | 9 | With equipment | Lithion Ion |  | UN 3481 |
| Battery | 9 | With equipment | Lithion metal |  | UN3091 |
| Battery | 9 | With equipment | Other |  | Other |
| Magnetized material | 9 |  |  |  | UN2807 |
| Flammable liquids | 3 |  |  | Paints | UN1263 |
| Flammable liquids | 3 |  |  | Perfumery products | UN1266 |
| Flammable liquids | 3 |  |  | Alcohols | UN3065 |
| Flammable liquids | 3 |  |  | Other | Other |
| Aerosols | 2 |  |  |  | UN1950 |
| Aerosols | 2 |  |  |  | Other |

* **保质期**（`is_expiration_management = true`）：必须提供 `shelf_life_attribute_info`，包括 inbound 截止天数、过期预警天数、销售截止天数和过期单位处理方式


## 6. 选择您的 Inbound 工作流程
| Criteria | Carton Splitting | Unit Splitting |
| --- | --- | --- |
| **使用时机** | 您在发货前已知箱尺寸和内容 | 您在创建 inbound 订单时尚未装箱，或者箱由您的 warehouse 动态装箱 |
| **inbound_type 值** | `CARTON_SPLITTING` | `UNIT_SPLITTING` |
| **payload 中的箱数据** | 必需 — 在创建 plan 时； | 非必需，需在 Ship IBR 步骤中后续提供 <br/>  |

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/9589c9d242b34d60847afa481ab4a129~tplv-k9wyc2ijk0-image.image)

## 7. 创建 Inbound — API 调用顺序
按顺序执行以下 **9 个步骤**。每个步骤可能会生成下一步所需的 ID。两种工作流程（箱拆分 / 单位拆分）共享相同的顺序 — 区别仅在于请求/响应字段。
| # | API | Method | Purpose | Key Output | Comments |
| --- | --- | --- | --- | --- | --- |
| 1 | **Create / Update Inbound Plan** | POST | 创建新的 inbound plan 或更新现有草稿。指定 SKU、数量和目的地 warehouse。 | `inbound_plan_id` |  |
| 2 | **List Available Inbound Methods** | GET | 检索 plan 可用的 inbound 方式及预期时间范围（Single Hub, D2FC）。<br/> 对于 hub 还包括入库费用估算。<br/>  | inbound 方式可用的 ETA | 此步骤告知您 inbound 方式的可用性。<br/> FBT inbound 方式  |
| 3 | **Get Inbound Method Detail** | POST | 获取每个 inbound 方式和 ETA 的详情，包括 placement option ID 和 warehouse ID。<br/> 对于 hub 还包括入库费用估算。 | `placement_option_id` <br/> 如果要发往特定 hub，请使用对应 hub 的正确 placement option ID。 | **异步轮询操作**：此 endpoint 可能需要最多 **3-5 秒**才能返回成功。<br/> 建议每 3-5 秒轮询一次，直到 placement 任务成功 <br/>  |
| 4 | **Confirm Inbound Method** | POST | 选择并确认首选的 inbound 方式和 placement option。包含步骤 3 返回的 `placement_option_id`。 | 已确认的 `inbound_order_ids` <br/> 对于单个 hub，您将获得 1 个订单 ID <br/> 对于 D2FC，您将获得订单 ID 列表 <br/>  |  |
| 5 | **Ship Inbound Order** | POST | 提交最终发货详情：箱/单位清单，如果是单位拆分则提供箱内容 <br/>  | `inbound_order_id` 状态变为"已发货" | 这是接收 inventory 所必需的。未发货的 inbound 订单将导致 NCI |
| 6 | **Print Label** | POST | 生成可打印的运输标签（每箱 / 每货件）。 | 标签 PDF / URL | **异步轮询操作**：此 endpoint 可能需要最多 **30 秒**才能返回成功。<br/> 建议每 3-5 秒轮询一次，直到 task_status 成功并返回 URL |
| 7 | **Update Tracking** | POST | 在每个箱的小包裹标签可用后推送承运商追踪号。 |  |  |
| 8 | **Get Inbound Order** | GET | 检索订单详情 | 订单状态和详情 |  |
| 9 | **Cancel Inbound Order** | POST | 取消订单（仅在 warehouse 收货之前）。 <br/> 请注意，如果 D2FC IBR 的部分 plan 已收货而剩余部分未收货，取消可能会产生费用。 | 取消确认 |  |
关键字段参考
### `plan_id` — 创建与更新
| Scenario | `plan_id` in request body |
| --- | --- |
| 创建新的 inbound plan | **省略** — 系统生成并返回新的 `inbound_plan_id` |
| 更新现有草稿 plan | **必需** — 包含原始 create 调用返回的 `inbound_plan_id` |
### 时间戳格式
请求参数中的所有 `timestamp` 字段必须为 **Unix 时间戳（秒，UTC）**：
```JSON
{
  "cartons": [
    {
      "items": [
        {
          "tts_goods_id": "9988776655",
          "quantity": 10,
          "expiration_timestamp": "1780000000"
        }
      ]
    }
  ]
}
```

> 使用秒（UTC），**而非毫秒**。



## 8. 错误处理
### HTTP 错误码

* **400 Bad Request** — 在提交前验证所有必填字段和数据类型
* **401 Unauthorized** — Token 过期或缺失。刷新后重试
* **409 Conflict** — 重复的 plan/订单。检查 `idempotency_key` 或现有记录
* **429 Rate Limited** — 实施带抖动的指数退避。默认限制：**每店铺 10 次请求/秒**
* **5xx Server Error** — 使用退避重试（最多 3 次）。记录响应头中的 `request_id` 以便上报

### 常见问题与修复
**ETA 时段不可用。** ETA 帮助 FBT 规划 warehouse inbound 容量。**** 在高峰期，部分 inbound 方式或站点可能不可用，请选择其他 ETA 

* 从 *Get Inbound Method Detail*（步骤 3）检索可用 ETA 并从列表中选择

**Create Inbound Plan 出现通用"Internal Error"：** 请尝试以下步骤

* 验证您的商品已与 TikTok Shop SKU 匹配（未匹配的商品无法进行 inbound）
* 如果问题持续，请提供完整的请求 payload 和响应头中的 `request_id` 进行上报

**Print Label API 延迟** 标签打印在调用 print label API 后**异步**运行。

## 9. 其他 FBT API 和 Webhook
| # | Type | API / Webhook | Description |
| --- | --- | --- | --- |
| 1 | API | Get FBT Warehouse List | 检索所有 FBT warehouse 信息，包括名称和地址 |
| 2 | API | Search Goods Info | 检索商品信息，包括 warehouse 验证的尺寸和重量 |
| 3 | API | Search FBT Inventory | 检索 inventory 详情 — warehouse 级别的可售、预留、不可售和在途 inventory |
| 4 | API | Search FBT Inventory Record | 检索 inventory 变更记录，可按 warehouse 和时间范围筛选 |
| 5 | API | Get Inbound Orders | 检索 inbound 订单详情，包括计划/实际的 inbound 详情和状态 |
| 6 | Webhook | Merchant Onboard | 当卖家入驻 FBT 时触发 |
| 7 | Webhook | Goods Match | 当 TikTok Shop SKU 与 FBT 商品匹配或取消匹配时触发 |
| 8 | Webhook | FBT Inventory Update | 当 FBT inventory 更新时触发 |
| 9 | Webhook | FBT Inbound Status Change | 当 FBT inbound 订单状态更新时触发 |

## 10. 测试与上线检查清单
### 上线

- [ ] 已实现 Token 刷新逻辑
- [ ] ETA 选择：通过调用 List Inbound method 检索可用 ETA 
- [ ] 标签生成：在调用 print label 后短暂异步延迟后调用 Print Label
- [ ] 错误处理：记录所有 5xx 错误的响应中的 `request_id`
- [ ] 已确认 inbound plan 中所有 SKU 的商品匹配
- [ ] 已确认 warehouse 对您的商家处于活跃状态
- [ ] **仅在 sandbox 签核后**使用真实 `shop_id` 和凭据转入生产环境


## 11. 常见问题
### Inbound 方式值
**问：ListAvailableInboundMethod 响应中的 D2FC 和 ONE_HUB 是什么意思？**

* **D2FC**：*Direct to Fulfillment Center* — 您的货件直接发送到履约客户订单的最终 FC
* **ONE_HUB**：您的货件首先发送到 hub/合并点进行分拣，然后转发到 FC。这是两个标准值；根据 warehouse 位置，可能有额外的区域特定值可用。

**Q: Can I update the tracking number after submission?​**Yes — use the *Update Tracking* API to push a new or corrected carrier tracking number at any time after handing off to the carrier.

