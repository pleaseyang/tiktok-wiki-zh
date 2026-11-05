# TikTok Shop 合作伙伴中心文档

本项目是 TikTok Shop 合作伙伴中心文档的本地镜像，使用 VitePress 构建，支持中英文双语切换。

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 启动开发服务器

```bash
npm run dev
```

浏览器访问：http://localhost:5173

### 3. 构建生产版本

```bash
npm run build
```

### 4. 预览生产版本

```bash
npm run preview
```

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
│   ├── API_Reference/   # API 参考文档（中文）
│   ├── Developer_Guide/ # 开发者指南（中文）
│   ├── Partner_Guide/   # 合作伙伴指南（中文）
│   └── Webhooks/        # Webhooks 文档（中文）
├── index.md             # 英文首页
├── zh/index.md          # 中文首页
└── package.json         # 项目配置
```

## 文档内容

- **API Reference**: 353 篇 API 接口文档，涵盖商品、订单、履约、物流、财务等模块
- **Developer Guide**: 开发者指南，包含快速开始、API 概念、SDK 下载等
- **Partner Guide**: 合作伙伴指南，包含注册流程、控制台使用等
- **Webhooks**: Webhooks 事件订阅文档

## 语言切换

- 点击右上角语言按钮切换中英文
- 英文版本路径：`/API_Reference/...`
- 中文版本路径：`/zh/API_Reference/...`

## 常用命令

| 命令 | 说明 |
|------|------|
| `npm run dev` | 启动开发服务器 |
| `npm run build` | 构建生产版本 |
| `npm run preview` | 预览生产版本 |
| `npm run dev -- --port 3000` | 指定端口启动 |

## 技术栈

- **VitePress** 1.5.0 - 静态站点生成器
- **Vue** 3.5.0 - 前端框架
- **Node.js** - 运行环境

## 注意事项

1. 项目使用 ESM 模块系统，需要 Node.js 14+ 版本
2. 配置文件已设置 `ignoreDeadLinks: true` 以忽略文档内部的死链
3. 部分 API 端点名称保留英文专有名词（如 "Products API"、"Fulfillment API"）
4. 首次启动可能需要等待 VitePress 预热

## 常见问题

### Q: 端口被占用怎么办？

A: 使用 `npm run dev -- --port 3000` 指定其他端口

### Q: 构建失败怎么办？

A: 删除 `node_modules` 和 `.vitepress/.cache` 目录，重新运行 `npm install`

### Q: 如何添加新文档？

A: 在对应目录下创建 `.md` 文件，然后在 `.vitepress/config.js` 中添加侧边栏配置

## License

本文档仅供学习参考使用，版权归 TikTok Shop 所有。
