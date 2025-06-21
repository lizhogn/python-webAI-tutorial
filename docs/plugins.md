# 生产力提升插件

## VS Code 插件推荐

### 语言支持
- **Python**: Microsoft 官方插件，提供语法高亮、调试支持
- **Pylance**: 微软开发的 Python 语言服务器，提供智能补全
- **Vetur/Volar**: Vue.js 开发支持
- **TypeScript**: TypeScript 和 JavaScript 支持

### 代码质量
- **ESLint**: JavaScript/TypeScript 代码检查
- **Prettier**: 代码格式化工具
- **Black Formatter**: Python 代码格式化
- **isort**: Python import 语句排序

### 版本控制
- **GitLens**: Git 增强功能，显示代码行作者信息
- **Git History**: 查看文件历史记录
- **Git Graph**: 可视化 Git 提交历史

### 开发工具
- **REST Client**: API 测试工具
- **Thunder Client**: 轻量级 API 测试
- **Docker**: Docker 容器管理
- **Remote - SSH**: 远程开发支持

### 主题和图标
- **Material Icon Theme**: 文件图标主题
- **One Dark Pro**: 深色主题
- **Dracula Official**: 经典深色主题

## 浏览器插件

### 开发者工具
- **Wappalyzer**: 识别网站使用的技术栈
- **JSON Viewer**: JSON 数据格式化显示
- **Octotree**: GitHub 文件树导航
- **GitHub Dark Theme**: GitHub 深色主题

### 生产力工具
- **uBlock Origin**: 广告拦截器
- **LastPass**: 密码管理器
- **Grammarly**: 英文写作助手
- **Momentum**: 新标签页美化

## 终端增强

### Zsh 插件
```bash
# 自动建议
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 语法高亮
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# 自动补全
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-completions
```

### 常用插件
- **zsh-autosuggestions**: 命令自动建议
- **zsh-syntax-highlighting**: 语法高亮
- **zsh-completions**: 自动补全
- **git**: Git 命令别名
- **docker**: Docker 命令补全

## 系统工具

### macOS
- **Alfred**: 快速启动和搜索
- **Rectangle**: 窗口管理
- **Spectacle**: 窗口布局工具
- **iStat Menus**: 系统监控

### Windows
- **PowerToys**: 微软官方工具集
- **Everything**: 文件搜索工具
- **AutoHotkey**: 自动化脚本

### Linux
- **Albert**: 快速启动器
- **Tilix**: 终端模拟器
- **Synaptic**: 包管理器

## 配置示例

### VS Code 设置
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
```

### Zsh 配置
```bash
# ~/.zshrc
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  docker
  python
)

# 别名
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
```

## 学习资源

- [VS Code 插件市场](https://marketplace.visualstudio.com/)
- [Oh My Zsh 插件](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)
- [Zsh 插件推荐](https://github.com/unixorn/awesome-zsh-plugins) 