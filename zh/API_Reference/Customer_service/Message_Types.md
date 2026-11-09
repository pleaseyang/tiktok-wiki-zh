# 消息类型

# 背景
此 API 使您能够获取用于展示对话数据的标准化卡片信息。您可以根据具体需求选择是否使用。
我们的整体数据分为三个部分，这三个部分所包含的内容可能因场景、用户或用途而异。
**Content**
`content` 字段包含消息内容的元数据，仅包含一组有限的关键字段。
**自定义 UI？使用原始数据构建**
`data` 字段封装了与消息相关的业务数据，例如订单、商品或物流信息。
开发者可以使用此字段根据自身需求构建自定义 UI 展示。此字段仅在 `request.query.need_data=true` 时返回。请注意，业务数据可能具有时效性。
**需要速度？使用纯文本。**
`plaintext` 字段是消息的纯文本表示形式，用于 UI 展示。
它已经包含了相关的业务信息，开发者可以直接使用此字段进行 UI 渲染，无需额外处理。此字段仅在 `request.query.need_plaintext=true` 时返回。请注意，业务数据可能具有时效性。

# TEXT
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| content | string | 文本内容 |
#### **示例**
```JSON
{
  "content": "simple text"
}
```

# IMAGE / EMOTICONS
### content
```JSON
{
   "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290",
  "width": 300,
  "height": 300
}
```

#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| url | string | 图片 URL |
| width | int | 图片宽度 |
| height | int | 图片高度 |
###
# VIDEO
### content
```JSON
{
  "url": "https://video-boei18n.byted.org/storage/v1/tos-boei18n-v-c72c01/e8240f35244646428df9c3244d1a7408?x-tos-algorithm=v2&x-tos-authkey=5bf25627da095a5cba28ace592de46cc&x-tos-expires=1681980481&x-tos-signature=r_bRxtrvGhXAuZgMmNhlZ_Upqzg",
  "cover": "https://p-boei18n.byted.org/tos-boei18n-v-c72c01/o8keEOhzTcNCcJyAbkWZwpLIyTfkJxcGbRBvLP~tplv-jvtte31kaf-origin-jpeg.jpeg?",
  "width": 640,
  "height": 360,
  "duration": "20.504",
  "vid": "v0e30cg700f7cgcmu8jc77u9e2bdp95g",
  "expire_time": "1681980481",
  "format": "mp4",
  "size": 400000,
  "bit_rate": 156067,
  "quality": "original",
  "codec_type": "h264"
}
```

#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| url | string | 视频 URL |
| width | int | 视频宽度 |
| height | int | 视频高度 |
| duration | string | 视频时长 |
| vid | string | 视频标识符 |
| expire_time | int | 视频过期时间，Unix 时间戳格式 |
| format | string | 视频文件格式 |
| size | int | 文件大小（字节） |
| bit_rate | int | 视频比特率（kbps） |
| quality | string | 视频质量等级 |
| codec_type | string | 视频编码格式 |
###
# ORDER_CARD
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| order_id | string | 订单标识符 |
#### **示例**
```JSON
{
  "order_id": "123"
}
```

### data
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| order_id | string | 订单标识符 |
| order_status | string | 当前订单状态 |
| product_name | string | 商品名称 |
| product_image | string | 商品图片 URL |
| paid_price | string | 已支付总金额 |
| quantity | int | 订单中的商品数量 |
| order_link | string | 订单详情页 URL |
#### **示例**
```JSON
{
  "order_id": "123",
  "order_status": "Delivered",
  "product_id": "1234",
  "product_name": "abc",
  "product_image": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/1a80a431f63f447dbcb7f19b666757ea~tplv-aphluv4xwc-resize-webp:800:800.webp?dr=15582&t=555f072d&ps=933b5bde&shp=f359665f&shcp=5566cfe3&idc=my2&from=4082722399",
  "paid_price": "Rp16.000",
  "quantity": 3,
  "order_link": "https://seller-us.tiktok.com/order/detail?order_no=123"
}
```

### plaintext
#### **示例**
```YAML
已分享订单卡片：
- 订单 ID：582362672348497014；
- 当前订单状态：已送达；
- 商品数量：3；
- 订单支付金额：Rp16.000。

查看完整详情：https://abc.com/
```


# PRODUCT_CARD
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| product_id | string | 商品标识符 |
#### **示例**
```JSON
{
  "product_id": "1234"
}
```

### data
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| product_id | string | 商品标识符 |
| product_name | string | 商品展示名称 |
| product_image | string | 商品图片 URL |
| product_highest_price | string | 商品价格区间中的最高价 |
| product_lowest_price | string | 商品价格区间中的最低价 |
| sold_quantity | int | 已售出总数量 |
| product_link | string | 商品详情页 URL |
#### **示例**
```JSON
{
  "product_id": "1234",
  "product_name": "abc",
  "product_image": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/1a80a431f63f447dbcb7f19b666757ea~tplv-aphluv4xwc-resize-webp:800:800.webp?dr=15582&t=555f072d&ps=933b5bde&shp=f359665f&shcp=5566cfe3&idc=my2&from=4082722399",
  "product_highest_price": "139.000₫",
  "product_lowest_price": "119.000₫",
  "sold_quantity": 40013,
  "product_link": "https://seller-us.tiktok.com/product/manage?search_content=1234"
}
```

### plaintext
#### **示例**
```YAML
已分享商品卡片：
- 商品 ID：1732529206731441911；
- 商品名称：abc；
- 商品最低价：119.000₫；
- 商品最高价：139.000₫；
- 已售出：40642。

查看完整详情：https://abc.com/
```


# RETURN_REFUND_CARD
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| order_id | string | 关联的订单标识符 |
| sku_id | string | 退货/退款对应的具体商品 SKU 标识符 |
#### **示例**
```JSON
{
  "order_id": "123",
  "sku_id": "1234"
}
```

### data
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| sku_id | string | 具体商品 SKU 标识符 |
| order_id | string | 关联的订单标识符 |
| order_status | string | 订单当前状态 |
| product_name | string | 退货/退款商品名称 |
| product_image | string | 商品图片 URL |
| paid_price | string | 该 SKU 的已支付金额 |
| quantity | int | 该 SKU 的商品数量 |
| order_link | string | 原始订单详情页 URL |
#### **示例**
```JSON
{
  "sku_id": "1",
  "order_id": "123",
  "order_status": "Delivered",
  "product_id": "1234",
  "product_name": "abc",
  "product_image": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/1a80a431f63f447dbcb7f19b666757ea~tplv-aphluv4xwc-resize-webp:800:800.webp?dr=15582&t=555f072d&ps=933b5bde&shp=f359665f&shcp=5566cfe3&idc=my2&from=4082722399",
  "paid_price": "Rp10.667",
  "quantity": 2,
  "order_link": "https://seller-us.tiktok/com/order/detail?order_no=123"
}
```

### plaintext
#### **示例**
```YAML
已分享退货/退款表单：
- SKU ID：1；
- 订单 ID：123；
- 订单状态：已送达；
- 商品 ID：1234；
- 商品名称：abc；
- 商品数量：2；
- 退款金额：Rp10.667。
```


# COUPON_CARD
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| coupon_id | string | 优惠券标识符 |
#### **示例**
```JSON
{
  "coupon_id": "12"
}
```

### data
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| coupon_id | string | 优惠券标识符 |
| coupon_title | string | 优惠券展示标题 |
| coupon_type | string | 优惠券类型（例如 "Regular"） |
| discount | string | 折扣金额或折扣比例 |
| threshold | string | 使用优惠券需满足的条件 |
| scope | string | 优惠券适用的商品范围 |
| start_time | int | 优惠券有效起始时间（Unix 时间戳） |
| end_time | int | 优惠券有效截止时间（Unix 时间戳） |
| coupon_link | string | 优惠券详情页 URL |
#### **示例**
```JSON
{
  "coupon_id": "12",
  "coupon_title": "cheap",
  "coupon_type": "Regular",
  "discount": "₱26.00 off",
  "threshold": "on order over ₱196.00",
  "scope": "Selected products",
  "start_time": 1768634640,
  "end_time": 1773829080,
  "coupon_link": "https://seller-us.toktok.com/promotion/marketing-tools/voucher/view/12"
}
```

### plaintext
#### **示例**
```YAML
已分享优惠券：
- 优惠券 ID：12；
- 优惠券标题：cheap；
- 优惠券折扣：₱26.00 off；
- 优惠券适用范围：Selected products；
- 优惠券使用条件：on order over ₱196.00；
- 优惠券有效期：Jan 17, 2026 3:24 PM 至 Mar 18, 2026 6:18 PM GMT+08:00。

查看完整详情：https://abc.com/
```


# LOGISTICS_CARD
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| order_id | string | 关联的订单标识符 |
| package_id | string | 用于追踪的具体包裹标识符 |
#### **示例**
```JSON
{
  "order_id": "123",
  "package_id": "12345"
}
```

### data
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| packages | list&lt;Package&gt; | 包裹对象数组，每个对象包含物流和商品详情。 |

* **Package**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| package_id | string | 包裹标识符 |
| product_name | string | 商品展示名称 |
| product_image | string | 商品图片 URL |
| paid_price | string | 已支付总金额 |
| quantity | int | 包裹中的商品数量 |
| predict_delivery_time_min | int | 预计最早送达时间 |
| predict_delivery_time_max | int | 预计最晚送达时间 |
| delivery_option | string | 订单选择的配送方式 |
| tracking_number | string | 物流服务商提供的追踪单号 |
| shipping_provider_name | string | 物流服务商或承运商名称 |
| tracking | list&lt;Tracking&gt; | 追踪记录列表，描述物流状态变更历史 |

* **Tracking**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| description | string | 物流状态更新的描述信息 |
| update_time_millis | int | 物流状态更新的时间戳 |
#### **示例**
```JSON
{
  "packages": [
    {
      "package_id": "12345",
      "product_name": "abc",
      "product_image": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/1a80a431f63f447dbcb7f19b666757ea~tplv-aphluv4xwc-resize-webp:800:800.webp?dr=15582&t=555f072d&ps=933b5bde&shp=f359665f&shcp=5566cfe3&idc=my2&from=4082722399",
      "paid_price": "$0.01",
      "quantity": 1,
      "predict_delivery_time_min": 1763198750000,
      "predict_delivery_time_max": 1763457950000,
      "delivery_option": "Standard shipping",
      "tracking_number": "1ZCIETST0422222228",
      "shipping_provider_name": "UPS",
      "tracking": [
        {
          "description": "Package has been delivered!",
          "update_time_millis": 1763954669267
        },
        {
          "description": "Arrived at the carrier's facility.",
          "update_time_millis": 1763954598311
        }
      ]
    }
  ]
}
```

### plaintext
#### **示例**
```YAML
已分享物流卡片：
- 订单 ID：123；
- 包裹 ID：12345；
- 商品数量：1；
- 订单支付金额：Rp63.852；
- 配送方式：Economy shipping
- J&T Express：JX7053814071；
- 预计送达日期：Jan 17, 2026 3:24 PM - Mar 18, 2026 6:18 PM GMT+08:00；
- 物流最新更新：
  Jan 30, 2026 2:35 AM
  您的包裹已离开唐格朗市的分拣中心。
  Jan 30, 2026 1:48 AM
  您的包裹已到达唐格朗市的分拣中心。
  Jan 29, 2026 9:03 PM
  您的包裹已由承运商在唐格朗县揽收。
  Jan 29, 2026 1:34 PM
  卖家正在为您准备包裹，将交付给承运商进行运输。

查看完整详情：https://abc.com/
```


# REVERSE_LOGISTICS_CARD
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| reverse_main_order_id | string | 逆向主订单标识符 |
#### **示例**
```Plain Text
{  "reverse_main_order_id": "70001"}
```

### data
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| reverse_main_order_id | string | 逆向主订单标识符 |
| tracking_no | string | 退货物流追踪单号 |
| provider_name | string | 物流服务商或承运商名称 |
| provider_logo | string | 物流服务商 Logo 的 URL。此字段可能为空。 |
| provider_id | string | 物流服务商标识符 |
| provider_link | string | 物流服务商官网或追踪页面 URL |
| items | list&lt;LogisticsItem&gt; | 追踪记录列表，描述退货物流状态变更历史 |

* **LogisticsItem**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| time | int | 物流更新的时间戳 |
| title | string | 物流追踪事件标题 |
| standard_msg | string | 物流追踪事件的本地化描述 |
#### **示例**
```JSON
{  "reverse_main_order_id": "70001",  "tracking_no": "TRACE-1",  "provider_name": "Fast Carrier",  "provider_logo": "https://example.com/provider-logo.png",  "provider_id": "88",  "provider_link": "https://carrier.example/track/TRACE-1",  "items": [    {      "time": 1769736900000,      "title": "Return package collected",      "standard_msg": "Your return package has been collected by the carrier."    },    {      "time": 1769734080000,      "title": "Return package in transit",      "standard_msg": "Your return package is on its way to the return warehouse."    }  ]}
```

### plaintext
#### **示例**
```YAML
已分享逆向物流卡片：
退货物流
Fast Carrier
追踪单号：TRACE-1

物流进度（GMT+08:00）：
- 退货包裹已揽收
您的退货包裹已由承运商揽收。
Jan 30, 2026 2:35 AM
- 退货包裹运输中
您的退货包裹正在送往退货仓库的途中。
Jan 30, 2026 1:48 AM
后续步骤：
请等待承运商送达退货包裹。
```

# [其他]
OTHER / NOTIFICATION / ALLOCATED_SERVICE / BUYER_ENTER_FROM_TRANSFER
### content
#### **属性**
| 字段 | 类型 | 描述 |
| --- | --- | --- |
| content | string | 文本内容 |
#### **示例**
```JSON
{
  "content": "...."
}
```
