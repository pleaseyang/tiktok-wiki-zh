# TikTok Shop 合作伙伴中心文档

本项目是 TikTok Shop 合作伙伴中心文档的本地镜像，使用 VitePress 构建，支持中英文双语切换。

## 项目结构

```
tiktok-docs/
├── .vitepress/          # VitePress 配置目录
│   └── config.js        # 主配置文件（包含中英文侧边栏）
├── API_Reference/       # API 参考文档（英文）
├── Developer_Guide/     # 开发者指南（英文）
├── Partner_Guide/       # 合作伙伴指南（英文）
├── Webhooks/            # Webhooks 文档（英文）
├── zh/                  # 中文版本文档
│   ├── API_Reference/
│   ├── Developer_Guide/
│   ├── Partner_Guide/
│   └── Webhooks/
├── index.md             # 英文首页
└── zh/index.md          # 中文首页
```

## 安装依赖

```bash
npm install
```

## 开发模式

启动本地开发服务器：

```bash
npm run dev
```

默认访问地址：http://localhost:5173

指定端口：

```bash
npm run dev -- --port 3000
```

## 构建生产版本

```bash
npm run build
```

构建产物将输出到 `.vitepress/dist` 目录。

## 预览生产版本

```bash
npm run preview
```

## 功能特性

- ✅ 完整的中英文双语支持
- ✅ 可展开的侧边栏导航
- ✅ 353 篇 API Reference 文档
- ✅ 开发者指南、合作伙伴指南、Webhooks 文档
- ✅ 响应式设计，支持移动端访问

## 语言切换

- 点击右上角语言按钮切换中英文
- 英文版本路径：`/API_Reference/...`
- 中文版本路径：`/zh/API_Reference/...`

## 技术栈

- **VitePress**: 静态站点生成器
- **Vue 3**: 前端框架
- **Markdown**: 文档格式

## 注意事项

- 项目使用 ESM 模块系统（`"type": "module"`）
- 配置文件已设置 `ignoreDeadLinks: true` 以忽略文档内部的死链
- 部分 API 端点名称保留英文专有名词（如 "Products API"、"Fulfillment API"）

## 更新文档

如需重新下载或更新文档，请参考项目根目录下的下载脚本：

```bash
node download-docs-v2.js
```

## License

本文档仅供学习参考使用，版权归 TikTok Shop 所有。
