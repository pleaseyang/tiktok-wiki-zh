# Customer Service API 概述

# 背景
Customer Service 是指卖家和买家的客服用于沟通售前、售中、售后全流程信息的通信渠道。
使用 Customer Service API 完成集成后，来自 TikTok Shop 买家的 message 将被转发到第三方客户支持系统。这消除了登录 Seller Center 管理买家 message 的需要，并允许客服人员直接在其客户支持平台上回复 message。本文适用于接入 TikTok Shop Customer Service 功能的第三方独立服务供应商（以下简称 ISV）或自研商家。
## **Customer Service 在 TTSPC 中作为 custom API 提供。**
Customer Service 是 TTSPC 中的 custom API，对在"Category & Market"中选择 Customer Service 作为业务类别、在"app or service"中选择服务类别的 partner/ISV 可见，但需要根据以下条件获得特别批准：

如果 **partner** 拥有 1000 个或更多授权卖家，或者其有任何 API scope 调用达到 **每天** 100 万次的阈值，则可以获得 CS API scope 的访问权限。例外情况是，如果该卖家拥有"TikTok Shop Seller"APP 类别，这意味着该卖家拥有自有的开发团队，我们可以给予特别批准。

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f68aa5da4afe4a31a4b47789bb5d1fb5~tplv-k9wyc2ijk0-image.image)
[阅读更多](https://partner.tiktokshop.com/docv2/page/64f19916cb677b0286e76d9d#Back%20To%20Top)

卖家可以通过工作台的授权页面，授权第三方软件或系统使用 Customer Service 开放接口，获取 Customer Service 数据和功能。
Customer Service 开放接口将提供以下能力：Customer Service session 列表、session 状态、发送图片等，并支持商家在第三方系统上接收和回复消费者 TTS Customer Service message。


<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSI2MDdweCIgaGVpZ2h0PSI2MThweCIgdmlld0JveD0iLTAuNSAtMC41IDYwNyA2MTgiPjxkZWZzLz48Zz48cmVjdCB4PSIyIiB5PSIyIiB3aWR0aD0iNjAwIiBoZWlnaHQ9IjYxMCIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjMDAwMDAwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PHBhdGggZD0iTSAxNDggNjA3IEwgMTUyIDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2UtZGFzaGFycmF5PSIzIDMiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDI4Mi4yIDYxMy44MyBMIDI4MiAyIiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgc3Ryb2tlLWRhc2hhcnJheT0iMyAzIiBwb2ludGVyLWV2ZW50cz0ic3Ryb2tlIi8+PHBhdGggZD0iTSA0NTIgNjEyIEwgNDUyIDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBzdHJva2UtZGFzaGFycmF5PSIzIDMiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDQ3MiAxMjIgTCAyNjguMzcgMTIyIiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgcG9pbnRlci1ldmVudHM9InN0cm9rZSIvPjxwYXRoIGQ9Ik0gMjYzLjEyIDEyMiBMIDI3MC4xMiAxMTguNSBMIDI2OC4zNyAxMjIgTCAyNzAuMTIgMTI1LjUgWiIgZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48cmVjdCB4PSI0NzIiIHk9IjEwMiIgd2lkdGg9IjEwMCIgaGVpZ2h0PSI0MCIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjMDAwMDAwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuNSAtMC41KSI+PGZvcmVpZ25PYmplY3Qgc3R5bGU9Im92ZXJmbG93OiB2aXNpYmxlOyB0ZXh0LWFsaWduOiBsZWZ0OyIgcG9pbnRlci1ldmVudHM9Im5vbmUiIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiBmbGV4OyBhbGlnbi1pdGVtczogdW5zYWZlIGNlbnRlcjsganVzdGlmeS1jb250ZW50OiB1bnNhZmUgY2VudGVyOyB3aWR0aDogOThweDsgaGVpZ2h0OiAxcHg7IHBhZGRpbmctdG9wOiAxMjJweDsgbWFyZ2luLWxlZnQ6IDQ3M3B4OyI+PGRpdiBzdHlsZT0iYm94LXNpemluZzogYm9yZGVyLWJveDsgZm9udC1zaXplOiAwOyB0ZXh0LWFsaWduOiBjZW50ZXI7ICI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyBmb250LXNpemU6IDEycHg7IGZvbnQtZmFtaWx5OiBIZWx2ZXRpY2E7IGNvbG9yOiAjMDAwMDAwOyBsaW5lLWhlaWdodDogMS4yOyBwb2ludGVyLWV2ZW50czogYWxsOyB3aGl0ZS1zcGFjZTogbm9ybWFsOyB3b3JkLXdyYXA6IG5vcm1hbDsgIj5BdXRob3JpemF0aW9uIFJlcXVlc3Q8L2Rpdj48L2Rpdj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjxwYXRoIGQ9Ik0gMjEyIDE0MiBMIDIxMiAxNjIgTCAyMTIgMTQyIEwgMjEyIDE1NS42MyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDIxMiAxNjAuODggTCAyMDguNSAxNTMuODggTCAyMTIgMTU1LjYzIEwgMjE1LjUgMTUzLjg4IFoiIGZpbGw9IiMwMDAwMDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PHJlY3QgeD0iMTYyIiB5PSIxMDIiIHdpZHRoPSIxMDAiIGhlaWdodD0iNDAiIGZpbGw9IiNmZmZmZmYiIHN0cm9rZT0iIzAwMDAwMCIgcG9pbnRlci1ldmVudHM9ImFsbCIvPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0wLjUgLTAuNSkiPjxmb3JlaWduT2JqZWN0IHN0eWxlPSJvdmVyZmxvdzogdmlzaWJsZTsgdGV4dC1hbGlnbjogbGVmdDsiIHBvaW50ZXItZXZlbnRzPSJub25lIiB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogZmxleDsgYWxpZ24taXRlbXM6IHVuc2FmZSBjZW50ZXI7IGp1c3RpZnktY29udGVudDogdW5zYWZlIGNlbnRlcjsgd2lkdGg6IDk4cHg7IGhlaWdodDogMXB4OyBwYWRkaW5nLXRvcDogMTIycHg7IG1hcmdpbi1sZWZ0OiAxNjNweDsiPjxkaXYgc3R5bGU9ImJveC1zaXppbmc6IGJvcmRlci1ib3g7IGZvbnQtc2l6ZTogMDsgdGV4dC1hbGlnbjogY2VudGVyOyAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgZm9udC1zaXplOiAxMnB4OyBmb250LWZhbWlseTogSGVsdmV0aWNhOyBjb2xvcjogIzAwMDAwMDsgbGluZS1oZWlnaHQ6IDEuMjsgcG9pbnRlci1ldmVudHM6IGFsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgd29yZC13cmFwOiBub3JtYWw7ICI+wqBTZXR1cCBUVCBBY2NvdW50PC9kaXY+PC9kaXY+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48cGF0aCBkPSJNIDI2MiAxODIgTCAyODIgMTgyIEwgMjc4IDE4MiBMIDI5MS42MyAxODIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBwb2ludGVyLWV2ZW50cz0ic3Ryb2tlIi8+PHBhdGggZD0iTSAyOTYuODggMTgyIEwgMjg5Ljg4IDE4NS41IEwgMjkxLjYzIDE4MiBMIDI4OS44OCAxNzguNSBaIiBmaWxsPSIjMDAwMDAwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgcG9pbnRlci1ldmVudHM9ImFsbCIvPjxyZWN0IHg9IjE2MiIgeT0iMTYyIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjQwIiBmaWxsPSIjZmZmZmZmIiBzdHJva2U9IiMwMDAwMDAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC41IC0wLjUpIj48Zm9yZWlnbk9iamVjdCBzdHlsZT0ib3ZlcmZsb3c6IHZpc2libGU7IHRleHQtYWxpZ246IGxlZnQ7IiBwb2ludGVyLWV2ZW50cz0ibm9uZSIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IGZsZXg7IGFsaWduLWl0ZW1zOiB1bnNhZmUgY2VudGVyOyBqdXN0aWZ5LWNvbnRlbnQ6IHVuc2FmZSBjZW50ZXI7IHdpZHRoOiA5OHB4OyBoZWlnaHQ6IDFweDsgcGFkZGluZy10b3A6IDE4MnB4OyBtYXJnaW4tbGVmdDogMTYzcHg7Ij48ZGl2IHN0eWxlPSJib3gtc2l6aW5nOiBib3JkZXItYm94OyBmb250LXNpemU6IDA7IHRleHQtYWxpZ246IGNlbnRlcjsgIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IGZvbnQtc2l6ZTogMTJweDsgZm9udC1mYW1pbHk6IEhlbHZldGljYTsgY29sb3I6ICMwMDAwMDA7IGxpbmUtaGVpZ2h0OiAxLjI7IHBvaW50ZXItZXZlbnRzOiBhbGw7IHdoaXRlLXNwYWNlOiBub3JtYWw7IHdvcmQtd3JhcDogbm9ybWFsOyAiPkF1dGhvcml6ZTwvZGl2PjwvZGl2PjwvZGl2PjwvZm9yZWlnbk9iamVjdD48Lz" />


通过 Customer Service API，您可以构建向买家发送 message、获取 session 列表、session message、新 event hook、获取和设置客服人员状态的应用程序。您可以获取指定订单可用的 message 类型列表，然后调用创建新 conversation 的操作，向该订单的买家发送 message。通过将 Customer Service Open API 与您的第三方系统集成，您将集中客户支持工作，更好地控制通信，并为客户提供一致的体验。

**卖家端概述** 


<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSI5MTFweCIgaGVpZ2h0PSIzNTVweCIgdmlld0JveD0iLTAuNSAtMC41IDkxMSAzNTUiPjxkZWZzLz48Zz48cGF0aCBkPSJNIDMzMiA0MiBMIDM2NS42MyA0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDM3MC44OCA0MiBMIDM2My44OCA0NS41IEwgMzY1LjYzIDQyIEwgMzYzLjg4IDM4LjUgWiIgZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48cmVjdCB4PSIxOTIiIHk9IjIiIHdpZHRoPSIxNDAiIGhlaWdodD0iODAiIHJ4PSIxMiIgcnk9IjEyIiBmaWxsPSIjZmZmZmZmIiBzdHJva2U9IiMwMDAwMDAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC41IC0wLjUpIj48Zm9yZWlnbk9iamVjdCBzdHlsZT0ib3ZlcmZsb3c6IHZpc2libGU7IHRleHQtYWxpZ246IGxlZnQ7IiBwb2ludGVyLWV2ZW50cz0ibm9uZSIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IGZsZXg7IGFsaWduLWl0ZW1zOiB1bnNhZmUgY2VudGVyOyBqdXN0aWZ5LWNvbnRlbnQ6IHVuc2FmZSBjZW50ZXI7IHdpZHRoOiAxMzhweDsgaGVpZ2h0OiAxcHg7IHBhZGRpbmctdG9wOiA0MnB4OyBtYXJnaW4tbGVmdDogMTkzcHg7Ij48ZGl2IHN0eWxlPSJib3gtc2l6aW5nOiBib3JkZXItYm94OyBmb250LXNpemU6IDA7IHRleHQtYWxpZ246IGNlbnRlcjsgIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IGZvbnQtc2l6ZTogMTJweDsgZm9udC1mYW1pbHk6IEhlbHZldGljYTsgY29sb3I6ICMwMDAwMDA7IGxpbmUtaGVpZ2h0OiAxLjI7IHBvaW50ZXItZXZlbnRzOiBhbGw7IHdoaXRlLXNwYWNlOiBub3JtYWw7IHdvcmQtd3JhcDogbm9ybWFsOyAiPlNlbGxlciBsb2dzIGluIHRvIHBhcnRuZXIgYXBwPC9kaXY+PC9kaXY+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48cGF0aCBkPSJNIDQ5MiA0MiBMIDUxMiA0MiBMIDUwNiA0MiBMIDUxOS42MyA0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDUyNC44OCA0MiBMIDUxNy44OCA0NS41IEwgNTE5LjYzIDQyIEwgNTE3Ljg4IDM4LjUgWiIgZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48cmVjdCB4PSIzNzIiIHk9IjIiIHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIHJ4PSIxMiIgcnk9IjEyIiBmaWxsPSIjZmZmZmZmIiBzdHJva2U9IiMwMDAwMDAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC41IC0wLjUpIj48Zm9yZWlnbk9iamVjdCBzdHlsZT0ib3ZlcmZsb3c6IHZpc2libGU7IHRleHQtYWxpZ246IGxlZnQ7IiBwb2ludGVyLWV2ZW50cz0ibm9uZSIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IGZsZXg7IGFsaWduLWl0ZW1zOiB1bnNhZmUgY2VudGVyOyBqdXN0aWZ5LWNvbnRlbnQ6IHVuc2FmZSBjZW50ZXI7IHdpZHRoOiAxMThweDsgaGVpZ2h0OiAxcHg7IHBhZGRpbmctdG9wOiA0MnB4OyBtYXJnaW4tbGVmdDogMzczcHg7Ij48ZGl2IHN0eWxlPSJib3gtc2l6aW5nOiBib3JkZXItYm94OyBmb250LXNpemU6IDA7IHRleHQtYWxpZ246IGNlbnRlcjsgIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IGZvbnQtc2l6ZTogMTJweDsgZm9udC1mYW1pbHk6IEhlbHZldGljYTsgY29sb3I6ICMwMDAwMDA7IGxpbmUtaGVpZ2h0OiAxLjI7IHBvaW50ZXItZXZlbnRzOiBhbGw7IHdoaXRlLXNwYWNlOiBub3JtYWw7IHdvcmQtd3JhcDogbm9ybWFsOyAiPkFkZCB0aGUgVGlrdG9rIFNob3A8L2Rpdj48L2Rpdj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjxwYXRoIGQ9Ik0gNTg2IDgyIEwgNTg2IDEwMiBMIDU4NiA5MiBMIDU4NiAxMDUuNjMiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBwb2ludGVyLWV2ZW50cz0ic3Ryb2tlIi8+PHBhdGggZD0iTSA1ODYgMTEwLjg4IEwgNTgyLjUgMTAzLjg4IEwgNTg2IDEwNS42MyBMIDU4OS41IDEwMy44OCBaIiBmaWxsPSIjMDAwMDAwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgcG9pbnRlci1ldmVudHM9ImFsbCIvPjxyZWN0IHg9IjUyNiIgeT0iMiIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI4MCIgcng9IjEyIiByeT0iMTIiIGZpbGw9IiNmZmZmZmYiIHN0cm9rZT0iIzAwMDAwMCIgcG9pbnRlci1ldmVudHM9ImFsbCIvPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0wLjUgLTAuNSkiPjxmb3JlaWduT2JqZWN0IHN0eWxlPSJvdmVyZmxvdzogdmlzaWJsZTsgdGV4dC1hbGlnbjogbGVmdDsiIHBvaW50ZXItZXZlbnRzPSJub25lIiB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogZmxleDsgYWxpZ24taXRlbXM6IHVuc2FmZSBjZW50ZXI7IGp1c3RpZnktY29udGVudDogdW5zYWZlIGNlbnRlcjsgd2lkdGg6IDExOHB4OyBoZWlnaHQ6IDFweDsgcGFkZGluZy10b3A6IDQycHg7IG1hcmdpbi1sZWZ0OiA1MjrweDsiPjxkaXYgc3R5bGU9ImJveC1zaXppbmc6IGJvcmRlci1ib3g7IGZvbnQtc2l6ZTogMDsgdGV4dC1hbGlnbjogY2VudGVyOyAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgZm9udC1zaXplOiAxMnB4OyBmb250LWZhbWlseTogSGVsdmV0aWNhOyBjb2xvcjogIzAwMDAwMDsgbGluZS1oZWlnaHQ6IDEuMjsgcG9pbnRlci1ldmVudHM6IGFsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgd29yZC13cmFwOiBub3JtYWw7ICI+RW50ZXIgdGhlIGF1dGhvcml6ZWQgbG9naW4gcGFnZTwvZGl2PjwvZGl2PjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PHBhdGggZD0iTSA1ODYgMTcyIEwgNTg2IDE5MiBMIDU4NiAxODIgTCA1ODYgMTk1LjYzIiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgcG9pbnRlci1ldmVudHM9InN0cm9rZSIvPjxwYXRoIGQ9Ik0gNTg2IDIwMC44OCBMIDU4Mi41IDE5My44OCBMIDU4NiAxOTUuNjMgTCA1ODkuNSAxOTMuODggWiIgZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48cmVjdCB4PSI1MjYiIHk9IjExMiIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI2MCIgcng9IjkiIHJ5PSI5IiBmaWxsPSIjZmZmZmZmIiBzdHJva2U9IiMwMDAwMDAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC41IC0wLjUpIj48Zm9yZWlnbk9iamVjdCBzdHlsZT0ib3ZlcmZsb3c6IHZpc2libGU7IHRleHQtYWxpZ246IGxlZnQ7IiBwb2ludGVyLWV2ZW50cz0ibm9uZSIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IGZsZXg7IGFsaWduLWl0ZW1zOiB1bnNhZmUgY2VudGVyOyBqdXN0aWZ5LWNvbnRlbnQ6IHVuc2FmZSBjZW50ZXI7IHdpZHRoOiAxMThweDsgaGVpZ2h0OiAxcHg7IHBhZGRpbmctdG9wOiAxNDJweDsgbWFyZ2luLWxlZnQ6IDUyN3B4OyI+PGRpdiBzdHlsZT0iYm94LXNpemluZzogYm9yZGVyLWJveDsgZm9udC1zaXplOiAwOyB0ZXh0LWFsaWduOiBjZW50ZXI7ICI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyBmb250LXNpemU6IDEycHg7IGZvbnQtZmFtaWx5OiBIZWx2ZXRpY2E7IGNvbG9yOiAjMDAwMDAwOyBsaW5lLWhlaWdodDogMS4yOyBwb2ludGVyLWV2ZW50czogYWxsOyB3aGl0ZS1zcGFjZTogbm9ybWFsOyB3b3JkLXdyYXA6IG5vcm1hbDsgIj5FbnRlciB0aGXCoDxzcGFuIHN0eWxlPSJmb250LXZhcmlhbnQtbGlnYXR1cmVzOm5vcm1hbDt0ZXh0LWFsaWduOnN0YXJ0O2JhY2tncm91bmQtY29sb3I6aW5pdGlhbCI+Y3VzdG9tZXIgc2VydmljZSBhY2NvdW50PC9zcGFuPjwvZGl2PjwvZGl2PjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PHBhdGggZD0iTSA1ODYgMjYyIEwgNTg2IDI4MiBMIDU4NiAyNzIgTCA1ODYgMjg1LjYzIiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgcG9pbnRlci1ldmVudHM9InN0cm9rZSIvPjxwYXRoIGQ9Ik0gNTg2IDI5MC44OCBMIDU4Mi41IDI4My44OCBMIDU4NiAyODUuNjMgTCA1ODkuNSAyODMuODggWiIgZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48cmVjdCB4PSI1MjYiIHk9IjIwMiIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI2MCIgcng9IjkiIHJ5PSI5IiBmaWxsPSIjZmZmZmZmIiBzdHJva2U9IiMwMDAwMDAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC41IC0wLjUpIj48Zm9yZWlnbk9iamVjdCBzdHlsZT0ib3ZlcmZsb3c6IHZpc2libGU7IHRleHQtYWxpZ246IGxlZnQ7IiBwb2ludGVyLWV2ZW50cz0ibm9uZSIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IGZsZXg7IGFsaWduLWl0ZW1zOiB1bnNhZmUgY2VudGVyOyBqdXN0aWZ5LWNvbnRlbnQ6IHVuc2FmZSBjZW50ZXI7IHdpZHRoOiAxMThweDsgaGVpZ2h0OiAxcHg7IHBhZGRpbmctdG9wOiAyMzJweDsgbWFyZ2luLWxlZnQ6IDUyN3B4OyI+PGRpdiBzdHlsZT0iYm94LXNpemluZzogYm9yZGVyLWJveDsgZm9udC1zaXplOiAwOyB0ZXh0LWFsaWduOiBjZW50ZXI7ICI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyBmb250LXNpemU6IDEycHg7IGZvbnQtZmFtaWx5OiBIZWx2ZXRpY2E7IGNvbG9yOiAjMDAwMDAwOyBsaW5lLWhlaWdodDogMS4yOyBwb2ludGVyLWV2ZW50czogYWxsOyB3aGl0ZS1zcGFjZTogbm9ybWFsOyB3b3JkLXdyYXA6IG5vcm1hbDsgIj5TdGFydCBzZXNzaW9uIHN5bmNocm9uaXphdGlvbiAobWF5IGJlIDEwbWluIGZvciB0aGUgZmlyc3QgdGltZSk8L2Rpdj48L2Rpdj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjxwYXRoIGQ9Ik0gNjQ2IDMyMiBMIDY2NiAzMjIgTCA2NjIgMzIyIEwgNjc1LjYzIDMyMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDY4MC44OCAzMjIgTCA2NzMuODggMzI1LjUgTCA2NzUuNjMgMzIyIEwgNjczLjg4IDMxOC41IFoiIGZpbGw9IiMwMDAwMDAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PHJlY3QgeD0iNTI2IiB5PSIyOTIiIHdpZHRoPSIxMjAiIGhlaWdodD0iNjAiIHJ4PSI5IiByeT0iOSIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjMDAwMDAwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuNSAtMC41KSI+PGZvcmVpZ25PYmplY3Qgc3R5bGU9Im92ZXJmbG93OiB2aXNpYmxlOyB0ZXh0LWFsaWduOiBsZWZ0OyIgcG9pbnRlci1ldmVudHM9Im5vbmUiIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiBmbGV4OyBhbGlnbi1pdGVtczogdW5zYWZlIGNlbnRlcjsganVzdGlmeS1jb250ZW50OiB1bnNhZmUgY2VudGVyOyB3aWR0aDogMTE4cHg7IGhlaWdodDogMXB4OyBwYWRkaW5nLXRvcDogMzIycHg7IG1hcmdpbi1sZWZ0OiA1MjdweDsiPjxkaXYgc3R5bGU9ImJveC1zaXppbmc6IGJvcmRlci1ib3g7IGZvbnQtc2l6ZTogMDsgdGV4dC1hbGlnbjogY2VudGVyOyAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgZm9udC1zaXplOiAxMnB4OyBmb250LWZhbWlseTogSGVsdmV0aWNhOyBjb2xvcjogIzAwMDAwMDsgbGluZS1oZWlnaHQ6IDEuMjsgcG9pbnRlci1ldmVudHM6IGFsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgd29yZC13cmFwOiBub3JtYWw7ICI+U3luY2hyb25pemF0aW9uIGNvbXBsZXRlZDwvZGl2PjwvZGl2PjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PHJlY3QgeD0iNjgyIiB5PSIyOTIiIHdpZHRoPSIyMjYiIGhlaWdodD0iNjAiIHJ4PSI5IiByeT0iOSIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjMDAwMDAwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuNSAtMC41KSI+PGZvcmVpZ25PYmplY3Qgc3R5bGU9Im92ZXJmbG93OiB2aXNpYmxlOyB0ZXh0LWFsaWduOiBsZWZ0OyIgcG9pbnRlci1ldmVudHM9Im5vbmUiIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiBmbGV4OyBhbGlnbi1pdGVtczogdW5zYWZlIGNlbnRlcjsganVzdGlmeS1jb250ZW50OiB1bnNhZmUgY2VudGVyOyB3aWR0aDogMjI0cHg7IGhlaWdodDogMXB4OyBwYWRkaW5nLXRvcDogMzIycHg7IG1hcmdpbi1sZWZ0OiA2ODNweDsiPjxkaXYgc3R5bGU9ImJveC1zaXppbmc6IGJvcmRlci1ib3g7IGZvbnQtc2l6ZTogMDsgdGV4dC1hbGlnbjogY2VudGVyOyAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgZm9udC1zaXplOiAxMnB4OyBmb250LWZhbWlseTogSGVsdmV0aWNhOyBjb2xvcjogIzAwMDAwMDsgbGluZS1oZWlnaHQ6IDEuMjsgcG9pbnRlci1ldmVudHM6IGFsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgd29yZC13cmFwOiBub3JtYWw7ICI+UmVjb3JkIG9mIG5ldyBtZXNzYWdlcywgc2Vzc2lvbiBsaXN0cywgaGlzdG9yaWNhbCBtZXNzYWdlcywgZXRjLjwvZGl2PjwvZGl2PjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE0MCIgaGVpZ2h0PSI4MCIgcng9IjEyIiByeT0iMTIiIGZpbGw9IiNmZmZmZmYiIHN0cm9rZT0iIzAwMDAwMCIgcG9pbnRlci1ldmVudHM9ImFsbCIvPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0wLjUgLTAuNSkiPjxmb3JlaWduT2JqZWN0IHN0eWxlPSJvdmVyZmxvdzogdmlzaWJsZTsgdGV4dC1hbGlnbjogbGVmdDsiIHBvaW50ZXItZXZlbnRzPSJub25lIiB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogZmxleDsgYWxpZ24taXRlbXM6IHVuc2FmZSBjZW50ZXI7IGp1c3RpZnktY29udGVudDogdW5zYWZlIGNlbnRlcjsgd2lkdGg6IDEzOHB4OyBoZWlnaHQ6IDFweDsgcGFkZGluZy10b3A6IDQycHg7IG1hcmdpbi1sZWZ0OiAzcHg7Ij48ZGl2IHN0eWxlPSJib3gtc2l6aW5nOiBib3JkZXItYm94OyBmb250LXNpemU6IDA7IHRleHQtYWxpZ246IGNlbnRlcjsgIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IGZvbnQtc2l6ZTogMTJweDsgZm9udC1mYW1pbHk6IEhlbHZldGljYTsgY29sb3I6ICMwMDAwMDA7IGxpbmUtaGVpZ2h0OiAxLjI7IHBvaW50ZXItZXZlbnRzOiBhbGw7IHdoaXRlLXNwYWNlOiBub3JtYWw7IHdvcmQtd3JhcDogbm9ybWFsOyAiPlNlbGxlciBkb3dubG9hZHMgdGhlIHRoaXJkLXBhcnR5IGN1c3RvbWVyIHNlcnZpY2UgcGFydG5lciBhcHAgZnJvbSBUVFMgYXBwIHN0b3JlPC9kaXY+PC9kaXY+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48cGF0aCBkPSJNIDE0MiA0MiBMIDE4NS42MyA0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJzdHJva2UiLz48cGF0aCBkPSJNIDE5MC44OCA0MiBMIDE4My44OCA0NS41IEwgMTg1LjYzIDQyIEwgMTgzLjg4IDM4LjUgWiIgZmlsbD0iIzAwMDAwMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2UtbWl0ZXJsaW1pdD0iMTAiIHBvaW50ZXItZXZlbnRzPSJhbGwiLz48L2c+PC9zdmc+" from="flow-chart" payload="{&quot;data&quot;:{&quot;mxCellList&quot;:[&quot;Xfazc13W&quot;,&quot;Pect1uf9&quot;,&quot;nZ5V68z7&quot;,&quot;TImjBIZR&quot;,&quot;uIwdCUXZ&quot;,&quot;kQrxKnVH&quot;,&quot;xoCGb2BM&quot;,&quot;aObyYjxa&quot;,&quot;s0ubc1DT&quot;,&quot;N4mOBEUc&quot;,&quot;AZsQeaNw&quot;,&quot;btQ6Qbnp&quot;,&quot;kDXtGOE6&quot;,&quot;ecUv55aQ&quot;,&quot;nN7W1HGG&quot;,&quot;UpGHCwA3&quot;,&quot;47gaJq8f&quot;],&quot;mxGraphModel&quot;:{&quot;arrows&quot;:&quot;1&quot;,&quot;connect&quot;:&quot;1&quot;,&quot;dx&quot;:&quot;314&quot;,&quot;dy&quot;:&quot;694&quot;,&quot;fold&quot;:&quot;1&quot;,&quot;grid&quot;:&quot;1&quot;,&quot;gridSize&quot;:&quot;10&quot;,&quot;guides&quot;:&quot;1&quot;,&quot;page&quot;:&quot;1&quot;,&quot;pageHeight&quot;:&quot;1169&quot;,&quot;pageScale&quot;:&quot;1&quot;,&quot;pageWidth&quot;:&quot;827&quot;,&quot;tooltips&quot;:&quot;1&quot;},&quot;mxCellMap&quot;:{&quot;47gaJq8f&quot;:{&quot;-0-mxGeometry&quot;:{&quot;-0-mxPoint&quot;:{&quot;as&quot;:&quot;sourcePoint&quot;,&quot;x&quot;:&quot;170&quot;,&quot;y&quot;:&quot;270&quot;},&quot;-1-mxPoint&quot;:{&quot;as&quot;:&quot;targetPoint&quot;,&quot;x&quot;:&quot;220&quot;,&quot;y&quot;:&quot;220&quot;},&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;50&quot;,&quot;relative&quot;:&quot;1&quot;,&quot;width&quot;:&quot;50&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;DirectionalConnector&quot;,&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;47gaJq8f&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;UpGHCwA3&quot;,&quot;style&quot;:&quot;endArrow=classic;html=1;&quot;,&quot;value&quot;:&quot;&quot;},&quot;AZsQeaNw&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;relative&quot;:&quot;1&quot;},&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;AZsQeaNw&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;btQ6Qbnp&quot;,&quot;style&quot;:&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot;,&quot;target&quot;:&quot;ecUv55aQ&quot;,&quot;value&quot;:&quot;&quot;},&quot;N4mOBEUc&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;60&quot;,&quot;width&quot;:&quot;120&quot;,&quot;x&quot;:&quot;554&quot;,&quot;y&quot;:&quot;290&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;N4mOBEUc&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Enter the <span style=\&quot;font-variant-ligatures: normal; text-align: start; background-color: initial;\&quot;>customer service account</span>&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;Pect1uf9&quot;:{&quot;id&quot;:&quot;Pect1uf9&quot;,&quot;parent&quot;:&quot;Xfazc13W&quot;},&quot;TImjBIZR&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;80&quot;,&quot;width&quot;:&quot;140&quot;,&quot;x&quot;:&quot;220&quot;,&quot;y&quot;:&quot;180&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;TImjBIZR&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Seller logs in to partner app&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;UpGHCwA3&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;80&quot;,&quot;width&quot;:&quot;140&quot;,&quot;x&quot;:&quot;30&quot;,&quot;y&quot;:&quot;180&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;UpGHCwA3&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Seller downloads the third-party customer service partner app from TTS app store&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;Xfazc13W&quot;:{&quot;id&quot;:&quot;Xfazc13W&quot;},&quot;aObyYjxa&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;80&quot;,&quot;width&quot;:&quot;120&quot;,&quot;x&quot;:&quot;554&quot;,&quot;y&quot;:&quot;180&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;aObyYjxa&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Enter the authorized login page&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;btQ6Qbnp&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;60&quot;,&quot;width&quot;:&quot;120&quot;,&quot;x&quot;:&quot;554&quot;,&quot;y&quot;:&quot;380&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;btQ6Qbnp&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Start session synchronization (may be 10min for the first time)&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;ecUv55aQ&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;60&quot;,&quot;width&quot;:&quot;120&quot;,&quot;x&quot;:&quot;554&quot;,&quot;y&quot;:&quot;470&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;ecUv55aQ&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Synchronization completed&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;kDXtGOE6&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;relative&quot;:&quot;1&quot;},&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;kDXtGOE6&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;ecUv55aQ&quot;,&quot;style&quot;:&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot;,&quot;target&quot;:&quot;nN7W1HGG&quot;,&quot;value&quot;:&quot;&quot;},&quot;kQrxKnVH&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;80&quot;,&quot;width&quot;:&quot;120&quot;,&quot;x&quot;:&quot;400&quot;,&quot;y&quot;:&quot;180&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;kQrxKnVH&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Add the Tiktok Shop&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;nN7W1HGG&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;height&quot;:&quot;60&quot;,&quot;width&quot;:&quot;226&quot;,&quot;x&quot;:&quot;710&quot;,&quot;y&quot;:&quot;470&quot;},&quot;diagramCategory&quot;:&quot;general&quot;,&quot;diagramName&quot;:&quot;RoundedRectangle&quot;,&quot;id&quot;:&quot;nN7W1HGG&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;style&quot;:&quot;rounded=1;whiteSpace=wrap;html=1;&quot;,&quot;value&quot;:&quot;Record of new messages, session lists, historical messages, etc.&quot;,&quot;vertex&quot;:&quot;1&quot;},&quot;nZ5V68z7&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;relative&quot;:&quot;1&quot;},&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;nZ5V68z7&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;TImjBIZR&quot;,&quot;style&quot;:&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot;,&quot;target&quot;:&quot;kQrxKnVH&quot;,&quot;value&quot;:&quot;&quot;},&quot;s0ubc1DT&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;relative&quot;:&quot;1&quot;},&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;s0ubc1DT&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;N4mOBEUc&quot;,&quot;style&quot;:&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot;,&quot;target&quot;:&quot;btQ6Qbnp&quot;,&quot;value&quot;:&quot;&quot;},&quot;uIwdCUXZ&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;relative&quot;:&quot;1&quot;},&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;uIwdCUXZ&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;kQrxKnVH&quot;,&quot;style&quot;:&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot;,&quot;target&quot;:&quot;aObyYjxa&quot;,&quot;value&quot;:&quot;&quot;},&quot;xoCGb2BM&quot;:{&quot;-0-mxGeometry&quot;:{&quot;as&quot;:&quot;geometry&quot;,&quot;relative&quot;:&quot;1&quot;},&quot;edge&quot;:&quot;1&quot;,&quot;id&quot;:&quot;xoCGb2BM&quot;,&quot;parent&quot;:&quot;Pect1uf9&quot;,&quot;source&quot;:&quot;aObyYjxa&quot;,&quot;style&quot;:&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot;,&quot;target&quot;:&quot;N4mOBEUc&quot;,&quot;value&quot;:&quot;&quot;}}},&quot;diagramType&quot;:&quot;uml&quot;,&quot;lastEditTime&quot;:0}" />


注意：集成前请参阅[开发者指南](https://partner.tiktokshop.com/doc/page/273731)，了解完整的平台入驻和应用创建，并理解 API 调用和授权须知。

## Customer Service API Operations 和 Webhooks
| Operations |
| --- |
| [Get Conversation Messages](https://partner.tiktokshop.com/docv2/page/650a587edefece02be664cd2?external_id=650a587edefece02be664cd2#Back%20To%20Top) |
| [Get Conversations](https://partner.tiktokshop.com/docv2/page/650a589f0fcef602bf29fecf?external_id=650a589f0fcef602bf29fecf#Back%20To%20Top) |
| [Send Message](https://partner.tiktokshop.com/docv2/page/650a58bbbace3e02b7556286?external_id=650a58bbbace3e02b7556286) |
| [Get Agent Settings](https://partner.tiktokshop.com/docv2/page/650a58d2bace3e02b7556575?external_id=650a58d2bace3e02b7556575) |
| [Update Agent Settings](https://partner.tiktokshop.com/docv2/page/650a59870fcef602bf2a1d79?external_id=650a59870fcef602bf2a1d79) |
| [Upload Buyer Messages Image](https://partner.tiktokshop.com/docv2/page/650a599d0fcef602bf2a1dc8?external_id=650a599d0fcef602bf2a1dc8) |
| [Read Message](https://partner.tiktokshop.com/docv2/page/650a59f7c16ffe02b8e8db3f?external_id=650a59f7c16ffe02b8e8db3f) |
| [Create Conversation](https://partner.tiktokshop.com/docv2/page/650a5a0bf1fd3102b9245b8d?external_id=650a5a0bf1fd3102b9245b8d) |
| **Webhooks** |
| [New Conversation](https://partner.tiktokshop.com/docv2/page/13-new-conversation)  |
| [New Message](https://partner.tiktokshop.com/docv2/page/14-new-message)  |
# 重要概念

**Conversation** - Conversation 是买家和店铺之间的交流。Conversation 可以在需要时实时进行并跨渠道，但可以在不丢失上下文或历史记录的情况下恢复。Conversation 可以通过一条 message 开始，并且可以包含线程化的 message。
**Message** - Message 是买家和卖家之间单次通信的实例。

Conversation 自动关闭的聊天 message 响应窗口。

* 在聊天 conversation 中，如果买家不回复，conversation 将在 6 小时后关闭。
* 卖家客服有 7 天的时间回复聊天 message。如果客服未回复，conversation 将因无响应而自动关闭。


要与买家发起 conversation，必须满足以下三个条件之一：

1. 买家和店铺在过去 30 天内曾有过 conversation。
2. 买家在过去 60 天内在该店铺下过订单。
3. 买家在该店铺有退货或退款记录。


| **"Participant" 中的角色定义** |  |
| --- | --- |
| BUYER | 买家通过在 TikTok message 应用上发送 message 与卖家沟通。 |
| SHOP | 店铺是 TikTok 市场上的卖家企业主。店铺是主账户，同时也具有客服人员角色。在 Customer Service API 中，仅支持主账户与 CS partner 集成。 |
| CUSTOMER_SERVICE | 被分配到 conversation 的卖家客服支持人员。如果卖家有多个客服人员，则他们的 conversation 将通过 Customer Service API 作为主账户传递给买家。 |
示例场景：

1. 当买家发起 conversation 时，该群聊中有 2 个参与者：BUYER 和 SHOP。
2. 如果有客服人员服务该客户，则将有 3 个成员：BUYER、SHOP 和 CUSTOMER SERVICE。
3. conversation 结束后，CUSTOMER_SERVICE 将离开群聊。


| **"Sender" 中的角色定义** |  |
| --- | --- |
| BUYER | 表示 message 由买家发送。 |
| CUSTOMER_SERVICE | 表示 message 由客服人员发送。 |
| SHOP | 自动回复和 FAQ 通过店铺发送。 |
| SYSTEM | 表示此 message 是系统消息。通常这类 message 将通过用户"SHOP"发送，sender 标记为"SYSTEM"，以指示这是一条"系统消息"。 |
| ROBOT | 当卖家在 Seller Center 启用"Chat Bot"时，买家输入某些问题后可能会触发一些自动回复。这类 message 将通过用户"SHOP"或"CUSTOMER_SERVICE"发送，sender 标记为"ROBOT"，以指示此 message 由智能工具触发。 |

| **Customer Service 用户标识符** |  |
| --- | --- |
| **im_user_id** | 这是内部 Customer Service 参与者 ID。<br/>此 ID 不能用于查询订单。查询订单请使用 `buyer_user_id`。 |
| **buyer_user_id** | 这是买家的用户 ID。<br/>Customer Service API 中的 user_id 与 Order API 中的 buyer_user_id 相同。您可以使用"buyer_user_id"获取通过聊天联系您的买家的订单。在任何外部域中查询买家时，请使用 buyer_user_id。 |


# TikTok Shop 市场政策

及时回复买家的 message 非常重要。我们建议卖家在 24 小时内回复买家，因为及时回复 message 可以：

* 帮助卖家解决客户可能存在的任何疑问，提高客户的购买意愿，提升转化率。
* 帮助客户更好地了解产品，降低退货或退款的可能性。
* 提高客户对店铺服务的满意度，减少投诉数量。


**关键绩效指标和目标**
我们鼓励卖家在回复客户时进行直接、专业和高效的沟通。所有通过 TikTok Shop 买家消息发送的 message 都必须遵守本政策规定的响应时间。卖家应注意，TikTok Shop 将根据其客服响应时间进行评估。
由 TikTok Shop 处理的任何客户查询不会影响卖家绩效指标。只有转交给卖家的工单才会用于计算卖家的绩效。
下表概述了卖家回复客户时必须遵守的响应时间。
|  | **指标** | **定义** | **卖家目标** |
| --- | --- | --- | --- |
| 卖家响应效率 | 24 小时响应率 | 24 小时内响应的聊天数/收到的聊天总数（过去 30 个自然日） | ≥80% |
|  | 解决率 | 标记为已解决的聊天数/收到的聊天总数（过去 30 个自然日） | ≥65% |
| 客户满意度 | 客户满意度评分 | 评分为 4 和 5 的聊天数/收到评分的聊天总数（过去 30 个自然日）<br/>  | ≥75%<br/>  |
在 TikTok Academy [此处](https://seller-us.tiktok.com/university/essay?knowledge_id=7454760317110062&role=1&course_type=1&from=search&identity=1)查看 TikTok Shop 客服政策。
# Customer Service API 审批规则
## 谁应该申请
此 API 面向构建自己的客户支持工具并集成 TikTok Shop conversation 的商家或 ISV。
如果您只需要基本的订单同步或目录管理，其他 API 可能更合适。Customer Service API 专门用于**基于聊天的客户支持场景**。
**重要提示：** 本文仅涵盖**入驻和审批规则**。API 参考、endpoint 和技术细节另有文档记录。

## 资格要求
所有申请人在提交 Customer Service API 申请之前，必须满足以下**最低资格标准**。
### 活跃的 app 内聊天窗口
您的产品中必须已经有一个**活跃的 app 内聊天窗口**（商家-买家聊天界面）。
**具体要求**

* 您的产品必须提供一个**用户可见的聊天界面**，其中：
   * 客服或商家可以回复买家 message
   * 买家可以在同一 conversation 中查看回复并进行跟进

例如
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c4245bcdfd26455c860601f216eda960~tplv-k9wyc2ijk0-image.image)
**审核内容**

* **聊天界面**的 UI/UX
* 实时**发送和接收 message** 的能力
* 基本的 **conversation 历史记录**展示（近期 message、时间戳、参与者）

要通过审核，您必须提交现有 app 内聊天窗口的**完整截图**和**屏幕录制**。局部或裁剪的截图通常被认为不够充分。

### 预集成的核心能力（Order / Fulfillment / After-Sales）
在申请 Customer Service API 之前，您的产品应已集成（或明确准备好集成）典型客服流程所依赖的**核心运营能力**：

* **Order** -- 基本订单信息、订单详情和订单状态
* **Fulfillment** -- 发货、配送状态及相关物流信息
* **After-Sales（退货和退款）** -- 退货请求、退款状态及相关工单

**为什么需要这些**客服人员通常需要在聊天窗口的**同一界面**中获取订单、履约和售后信息，以高效解决问题。API 入驻将验证您的产品是否能够：

* 展示与 conversation 关联的订单信息
* 在相关时展示履约/发货状态
* 在支持工作流程中展示售后/退货/退款状态

**审核内容**

* 您的产品是否具有以下**UI 界面**或**工作流程**：
   * 展示与买家或工单关联的订单
   * 显示发货/配送状态
   * 反映相关订单的退货和退款状态
* 您的集成设计是否使客服人员在实时 conversation 中使用这些功能**切实可行**。

### Partner 规模和 API 使用量
如果 partner 满足以下**任一**条件，则可以获得 Customer Service API 的访问权限：

* 拥有 **1,000 个或更多授权卖家**；或
* 达到 **每天 100 万次 API 调用**的阈值。

**例外情况**：如果卖家属于 **"TikTok Shop Seller"** 应用类别（表明其拥有自己的开发团队），则可以获得特别批准。
## 常见拒绝原因及解决方法
本节总结了 Customer Service API 申请被拒绝的最常见原因，以及您在**重新申请之前**应采取的修复措施。
| 拒绝原因 | 解决方法 | 需要重新提交的内容 |
| --- | --- | --- |
| 聊天窗口证据不足 | * 提供 app 内聊天窗口的**未裁剪、全页截图**<br/> * 包含至少一个**真实的 conversation**（测试数据可接受）<br/> * 添加一个**简短的屏幕录制**，展示完整的发送/接收流程 | * 完整的聊天界面截图（conversation 列表和详情）<br/> * 新的屏幕录制（30-90 秒），展示实际 message 的发送和接收 |
| "未展示核心能力集成" | * 确保您的产品在客服流程中**可见地展示** Order / Fulfillment / After-Sales 信息<br/> * 添加或展示显示**订单详情**、**发货状态**和**退货/退款状态**的 UI 面板<br/> * 记录客服人员在聊天时如何使用这些功能 | * 与 conversation 关联的订单详情 UI 截图<br/> * 发货/配送状态界面截图<br/> * 退货/退款视图截图<br/> * 每个功能领域的简短文字说明 |
| 用户基数阈值未达到 | 确保您满足 1,000 用户的要求并提供清晰的量化数据。 | 显示相关用户指标的 Dashboard 截图。 |
# 常见问题
### **被拒绝后何时可以重新申请？**

* 通常，在您完全解决拒绝原因后即可重新申请。

### **如果聊天窗口仍在开发中，可以申请吗？**

* Customer Service API 面向拥有已上线、功能正常的 app 内聊天窗口的产品。
* 如果您的聊天体验仍是模拟或原型，建议先完成开发。

### **如果尚未集成所有核心能力（Order / Fulfillment / After-Sales），可以申请吗？**

* 期望这些能力在审批前已经集成或明确到位。

### 卖家客服何时可以与买家发起新的 conversation？
卖家可以联系曾在其店铺下单的买家。
要与买家发起 conversation，必须满足以下三个条件之一：

* 买家和店铺在过去 30 天内曾有过 conversation。
* 买家在过去 60 天内在该店铺下过订单。
* 买家在该店铺有退货或退款记录。


### TTS Customer Service API 支持哪些 message 类型？
| Message 类型 | Customer Service API 支持 | 描述 |
| --- | --- | --- |
| Text | 是 | 不超过 2000 个字符 |
| Image | 是 | 最大 10 MB |
| emoji（静态） | 是 |  |
| emoji（动画） | 是 |  |
| Video | 是 | 最大 100MB |
| Product card | 是 | Product ID |
| Order card | 是 | Order ID |
| Logistic card | 是 | 运单号和物流服务商名称、预计送达日期、最新物流状态、产品图片和标题、数量和价格信息 |
| Order Reverse card | 是 | 退货/退款请求 |
| Coupon card | 是 |  |
| Return/Refund Status card | 不支持 |  |
| FAQ Card | 不支持 |  |
| Hyperlinks | 不支持 |  |
| Attachments | 不支持 |  |
### 当前支持的 msg type 展示
| msg type | 是否支持 |
| --- | --- |
| text | 是 |
| file_image | 是 |
| allocated_service | 是 |
| notification | 是 |
| user_enter_from_transfer | 是 |
| user_enter_from_goods | 是 |
| user_enter_from_order | 是 |
| goods_card | 是 |
| emoticons | 是 |
| order_card | 是 |
| video | 是 |
| invite_comment_v2 | 否 |
| card | 否 |
| interactive_system_message | 否 |
| card_greeting | 否 |
| message_greeting_question_answer | 否 |
| message_greeting_question | 否 |
| message_greeting_question_answer_image | 否 |
| order_reverse_card | 是 |
| system_button | 否 |
| select_order | 否 |
| coupon_card | 是 |
| order_logistics_card | 是 |
| return_refund_status_card | 否 |
### Customer Service API 与 TTS Seller Center 之间有哪些差异？
 
| 功能 | TTS Shop Chat | Customer Service API <br/>  | Customer Service API 备注 |
| --- | --- | --- | --- |
|  |  |  |  |
| 发送 message | ✅ | ✅ |  |
| 列出 conversation | ✅ | ✅ |  |
| 获取 conversation message | ✅ | ✅ | Customer Service API V3.0 支持通过 messageID 获取 message，通过 ConversationID 获取 conversation 详情 |
| 客户状态 | ✅ | ✅ |  |
| 更新客户状态 | ✅ | ✅ |  |
| 客服工作状态 | ✅ | ✅ |  |
| Customer Service Hook  <br/>  <br/> * 新 Conversation 开始<br/> * 收到新 Message<br/> * sender id/sender role/message | ✅ | ✅ |  |
| 标记已读 | ✅ | ✅ |  |
| 与买家发起新 conversation | ✅ | ✅ |  |
| 智能工具 | ✅ | ❌ |  |
| 聊天详情 | ✅ | ❌ |  |
| 聊天助手 | ✅ | ❌ | CS 平台可能有自己的 Chatbot/FAQ，或更倾向于使用自己的。 |
| 添加备注 | ✅ | ❌ |  |
| 客户满意度评价 | ✅ | ❌ | 买家满意度数据由 TTS 计算，可在 Seller Center 查看。 |
| FAQ 和自动回复 | ✅ | ❌ | 卖家需要先在 TTS 中配置并启用"FAQ 和自动回复"才能在 Chat API 中使用。CS 平台可能有自己的 Chatbot/FAQ。 |
| 订单管理 | ✅ | ❌ <br/>  | 可以通过 Order API 实现，使支持人员能够在 3P CS 平台上查看每个买家的订单列表。 |
| 标签 | ✅ | ❌ | CS 平台可能有自己的标签功能。 |
| 跨境卖家的翻译功能（如英文到中文） | ✅ <br/>  | ❌ |  |
| 按名称/SKU 查看商家产品列表 | ✅ <br/>  | ❌ | 可以通过 Product API 中的 /api/products/search 实现，使支持人员能够在卖家目录中搜索产品以在聊天渠道中引用。 |
| Conversation 监控 | ✅ | ❌ |  |
| 服务数据 | ✅ | ❌ |  |
### 通过 email 接收和回复买家 message。
TikTok Shop 卖家现在可以服务用户，并通过 email 接收和回复买家 message。此外，他们可以通过 Salesforce、Zendesk 或 Gorgias 等第三方客服平台设置 message 集成，这些平台利用 email-to-case 或类似功能。这意味着买家 message 将被汇总并通过 email 发送给卖家，卖家可以直接回复 email，买家将在 TikTok 内收到回复。
[阅读更多](https://seller-us.tiktok.com/university/essay?knowledge_id=5846413191907074&role=1&course_type=1&from=search&identity=1) 

### Customer Service API 是否支持服务数据？
Customer Service API 目前不支持服务数据。
服务数据是指该客服人员个人的数据。

* 24 小时响应率：过去 7 天内客户咨询的聊天中在 24 小时内响应的数量除以客户咨询的聊天总数。
* 满意率：今天客服人员服务的买家满意度，公式 = 客户评价为"满意"和"非常满意"的 session 数除以买家已评价的 session 数。
* 今日 session 数：今天分配给该客服人员发起的消费者 session 数。
