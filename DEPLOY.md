# 部署到 GitHub Pages

本项目已配置 GitHub Actions 自动部署到 GitHub Pages。

## 步骤

### 1. 在 GitHub 上创建仓库

1. 访问 https://github.com/new
2. 仓库名称建议：`tiktok-docs`
3. 设为 **Public**（GitHub Pages 免费版仅支持公开仓库）
4. **不要** 勾选 "Add a README file"（我们已经有本地文件）
5. 点击 "Create repository"

### 2. 推送本地代码到 GitHub

```bash
cd D:\tiktok\tiktok-docs

# 如果还没有提交
git add .
git commit -m "Initial commit: TikTok Shop 文档"

# 添加远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/tiktok-docs.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 3. 启用 GitHub Pages

1. 访问你的仓库页面：`https://github.com/YOUR_USERNAME/tiktok-docs`
2. 点击 **Settings** → **Pages**
3. 在 **Source** 部分，选择 **GitHub Actions**
4. 保存设置

### 4. 等待部署完成

- GitHub Actions 会自动构建并部署你的网站
- 部署完成后，访问：`https://YOUR_USERNAME.github.io/tiktok-docs/`

## 自定义配置

### 修改仓库名称

如果你使用不同的仓库名称，需要修改 `.vitepress/config.js` 中的 `base` 配置：

```javascript
export default defineConfig({
  base: '/your-repo-name/',  // 修改这里
  // ...
})
```

### 使用自定义域名

如果你有自定义域名，可以：

1. 在仓库根目录创建 `CNAME` 文件，写入你的域名（如 `docs.example.com`）
2. 在你的 DNS 提供商处添加 CNAME 记录指向 `YOUR_USERNAME.github.io`
3. 在 GitHub 仓库 Settings → Pages 中配置自定义域名

## 更新文档

推送新的更改到 `main` 分支后，GitHub Actions 会自动重新部署：

```bash
git add .
git commit -m "Update docs"
git push
```

## 查看部署状态

- 访问仓库的 **Actions** 标签页查看构建和部署状态
- 如果部署失败，可以查看日志排查问题

## 常见问题

### Q: 页面显示 404？

A: 检查 `.vitepress/config.js` 中的 `base` 配置是否与仓库名称一致

### Q: 样式丢失？

A: 确保 `base` 配置正确，路径应该是 `/仓库名称/`

### Q: 部署一直失败？

A: 检查 Actions 日志，常见原因：
- Node.js 版本不兼容
- 依赖安装失败
- 构建错误

## 本地测试

在推送前，可以先本地测试构建：

```bash
npm run build
npm run preview
```

访问 http://localhost:4173 查看构建结果。
