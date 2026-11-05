# Action Code 名称对照表

| **Action Code** | **Action Code 名称** | **说明** |
| --- | --- | --- |
| 30901 | pickup_success | 包裹已被承运商揽收，或承运商首次持有该包裹 |
| 31001 | trans_inbound | 本地转运入库 |
| 31101 | trans_outbound | 本地转运出库 |
| 31201 | sc_sign | 承运商网点已签收包裹。首次到达分拨中心。包裹不在运输中 |
| 31301 | sc_inbound | 承运商网点已收到包裹，但非首次到达分拨中心。包裹不在运输  |
| 31401 | sc_outbound | 从任一承运商网点出发，前往目的地承运商网点/邮局 |
| 32001 | trans_operate | 转运中心操作（如合并、重新贴标） |
| 32201 | trans_sign | 包裹已到达物流合作伙伴网点或其他承运商的枢纽 |
| 32301 | trans_handover | 已交接给配送合作伙伴 |
| 32401 | transport_departed | 包裹 outbound 航班/卡车已出发 |
| 32501 | transport_intransit | 包裹在两个承运商网点之间 — 包裹准时到达或在途中 |
| 32601 | transport_arrived | 包裹已到达机场/海港 |
| 32701 | sc_operate | 包裹正在分拨中心或枢纽进行处理 |
| 32801 | transport_assigned | 干线已签收并接收 |
| 36201 | drop_off_success | 卖家将包裹送至门店 |
| 39901 | pickup_station_in | 揽收网点已接收并入库，已发往下一个站点 |
| 40101 | station_inbound | 到达最终承运商网点/目的地网点或邮局 |
| 40201 | station_out | 包裹已离开最终承运商网点/目的地网点，准备开始配送 |
| 40301 | station_operate | 在目的地/最终网点处理中 |
| 41301 | delivery_transfer | 配送已转交至不同承运商/地址 |
| 43101 | platform_wh_received | 无法投递的包裹已退回仓库 |
| 43201 | pkg_wh_received | 无法投递的包裹已退回仓库 |
| 3010001 | pickup_station_out | 从揽收网点出库，转发至下一站 |
| 3013901 | sc_handover | 本地分拨中心交接 |
| 40501 | delivery_start | 包裹已装上配送车辆/正在派送/今日到达 |
| 40601 | 1st_attempt_failed | 首次尝试配送失败，原因：地址封锁、地址未找到/地址搬迁/无安全存放点、缺少签名 |
| 40801 | 2nd_attempt_failed | 第二次尝试配送失败，原因：地址封锁、无安全存放点、缺少签名 |
| 41001 | delivery_twice | 已安排重新配送，首次配送失败 — 通知/异常 |
| 41101 | delivery_thrice | 第三次配送中，第二次配送失败 — 通知/异常 |
| 41201 | delivery_multiple | 多次重复尝试配送 |
| 41401 | delivery_exception | 包裹正在派送中，因天气或运营原因导致配送延迟，且至少还有一次配送机会 |
| 41501 | pop_arrived | 包裹可在自提点/邮局领取，或包裹已被扣留待取 |
| 41801 | 3rd_attempt_failed | 第三次尝试配送失败，原因：地址封锁、地址未找到/地址搬迁/无安全存放点、缺少签名 |
| 41901 | multiple_attempt_failed | 第七次或以上尝试配送失败，原因：地址封锁、地址未找到/地址搬迁/无安全存放点、缺少签名 |
| 42001 | delivery_schedule | 承运商已安排配送或配送日期已更新 |
| 60101 | sign_failure | 配送失败，原因：无收件人/地址错误/配送指令不完整，或承运商不再重新尝试 |
| 50101 | signed_personally | 配送成功 |
| 59801 | pkg_received | 仓库已签收接收，英国平台专属逆向退货仓库 |
| 110101 | pkg_cancelled | 包裹已被承运商或发件人取消 |
| 120101 | lo_cancelled | 运单已被平台取消 |
| 140101 | operate_delay | 逾期未到包裹 |
| 90101 | pkg_damaged | 包裹在运输或派送过程中损坏 |
| 100101 | pkg_lost | 包裹在运输或派送过程中丢失 |
| 160101 | pkg_scrap | 包裹在运输或派送过程中被承运商销毁 |
| 70201 | unreachable_returning | 配送失败后，包裹正在退回原发件人 |
| 70301 | unreachable_return_failure | 包裹无法退回原发件人 |
| 70401 | unreachable_return_exception | 退货异常 |
| 70501 | unreachable_return_start | 配送失败的包裹从配送站点开始退回卖家 |
| 60201 | unreachable_returned_wh | 配送失败的包裹已送达退货仓库 |
| 80101 | unreachable_returned | 包裹无法投递给收件人，已成功退回原发件人 |
| 10101 | pkg_created | 包裹已创建 |
| 20101 | pkg_shipped | 包裹已准备好由卖家发货 |
| 20201 | pickup_start | 服务商已安排揽收资源；快递员正在前往揽收途中 |
| 20301 | pickup_failure | 承运商在运输前揽收包裹失败 |
| 20801 | drop_off_intransit | 正在将包裹送至承运商网点的途中 |
| 20901 | ready_for_pickup | 包裹已准备好由承运商揽收 |
| 21001 | data_send_carrier | 首次向承运商发送电子信号，生成运单号。通常在生成运输面单时 |
| 21101 | 2nd_pickup_failure | 第二次揽收尝试失败 |
| 21201 | 3rd_pickup_failure | 第三次揽收尝试失败 |
| 21301 | 4th_pickup_failure | 第四次揽收尝试失败 |
| 21401 | pickup_schedule | 承运商从发件人网点计划揽收 |
| 21901 | manifest_scaned | 承运商已接收货物 |
| 21402 | pickup_check_in | 司机已到达揽收地点 |
| 301002 | pickup_station_handover | 揽收地点交接 |
