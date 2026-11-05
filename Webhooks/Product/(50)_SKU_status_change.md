# (50) SKU status change

# SKU Status Change Webhook
## Trigger scenario
This webhook is triggered when the SKU status of an existing product changes.
Typical scenarios include:

* A new SKU is added under an existing product.
* An existing SKU is deleted from an existing product.
* An existing SKU is activated.
* An existing SKU is deactivated.

**Prerequisite:** The merchant has subscribed to the corresponding webhook topic and the related product change event is successfully consumed by the webhook delivery pipeline.
## Data business parameters
| Parameter name | Data type | Sample | Description |
| --- | --- | --- | --- |
| type | int | 50 | The ID of this webhook topic. This value is pending final assignment. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| shop_id | string | "7494049642642441621" | The shop ID. |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  | The business payload of this webhook. |
| └ product_id | string | "123456789" | The ID of the product whose SKU status changed. |
| └ skus | object[] | [{"sku_id":"987654321","status":"CREATED"}] | The list of SKUs whose status changed. |
| └└ sku_id | string | "987654321" | The ID of the SKU whose status changed. |
| └└ status | string | "CREATED" | The new SKU status. Possible values: `CREATED`, `DELETED`, `ACTIVATED`, `DEACTIVATED`. |
| └└ deactivation_source | string | "SELLER" | The source of deactivation. This field is returned only when `status` is `DEACTIVATED`. Possible values: `SELLER`, `PLATFORM`, `COMBO_RELATION`. |
| └ update_time | int | 1627587600 | The time when the change occurred. Unix timestamp. |
## Event example
```JSON
{
  "type": "TBD",
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "123456789",
    "skus": [
      {
        "sku_id": "987654321",
        "status": "DEACTIVATED",
        "deactivation_source": "SELLER"
      },
      {
        "sku_id": "987654322",
        "status": "CREATED"
      }
    ],
    "update_time": 1627587600
  }
}
```

## Notes

* `timestamp` and `update_time` are both Unix timestamps in seconds.
* `deactivation_source` is omitted unless the SKU is deactivated.
* The `skus` array may contain one or multiple SKU change records in a single event.
* The final topic ID should be updated after internal assignment is confirmed.
