# GitHub Pages 部署配置指南

## 🚀 自动部署已配置完成

我已经为你配置了 GitHub Actions 自动部署工作流，现在需要你在 GitHub 仓库设置中启用 GitHub Pages。

## 📋 配置步骤

### 1. 访问仓库设置
1. 打开你的 GitHub 仓库：https://github.com/lizhogn/python-webAI-tutorial
2. 点击仓库页面顶部的 **Settings** 标签
3. 在左侧菜单中找到 **Pages** 选项

### 2. 配置 GitHub Pages
1. 在 **Source** 部分，选择 **GitHub Actions**
2. 系统会自动检测到我们配置的部署工作流
3. 点击 **Configure** 按钮

### 3. 等待部署完成
1. 部署过程大约需要 2-3 分钟
2. 你可以在 **Actions** 标签页查看部署进度
3. 部署成功后，页面会显示你的文档 URL

## 🌐 访问你的文档

部署完成后，你的文档将在以下地址可用：
- **主域名**: https://lizhogn.github.io/python-webAI-tutorial/
- **自定义域名** (可选): 你可以在 Pages 设置中配置自定义域名

## 📁 部署内容

GitHub Actions 会自动部署 `docs/` 目录下的所有文件：
- `index.html` - 文档首页
- `_coverpage.md` - 封面页
- `_sidebar.md` - 侧边栏导航
- 所有章节内容 (chapter1-6)
- 工具资源页面
- 其他文档文件

## 🔧 自动更新

每次你推送代码到 `main` 分支时，GitHub Actions 会自动：
1. 检测到代码变更
2. 运行部署工作流
3. 更新 GitHub Pages 内容

## 📊 部署状态检查

### 检查 Actions 状态
1. 访问 https://github.com/lizhogn/python-webAI-tutorial/actions
2. 查看最新的部署工作流状态
3. 绿色勾表示部署成功，红色叉表示失败

### 检查 Pages 状态
1. 在仓库 Settings > Pages 页面
2. 查看 "Your site is live at" 部分
3. 确认 URL 是否可访问

## 🐛 常见问题

### 部署失败
如果部署失败，检查：
1. 仓库是否公开 (GitHub Pages 需要公开仓库)
2. Actions 权限是否正确设置
3. 工作流文件语法是否正确

### 页面无法访问
如果页面无法访问，检查：
1. 部署是否成功完成
2. URL 是否正确
3. 是否有 DNS 缓存问题

### 内容不更新
如果内容不更新，检查：
1. 代码是否成功推送到 main 分支
2. Actions 是否正常运行
3. 是否有缓存问题 (可以强制刷新浏览器)

## 🎯 下一步

配置完成后，你可以：
1. 访问你的文档网站
2. 分享链接给其他人
3. 继续更新文档内容
4. 配置自定义域名 (可选)

## 📞 获取帮助

如果遇到问题：
1. 检查 GitHub Actions 日志
2. 查看 GitHub Pages 文档
3. 在仓库 Issues 中提问

---

**配置完成后，你的文档就可以通过 https://lizhogn.github.io/python-webAI-tutorial/ 访问了！** 🎉 