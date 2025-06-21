# Python Web AI 开发教程

> 📚 从零开始的 Python Web AI 开发完整教程

[![GitHub stars](https://img.shields.io/github/stars/lizhogn/python-webAI-tutorial.svg?style=social&label=Star)](https://github.com/lizhogn/python-webAI-tutorial)
[![GitHub forks](https://img.shields.io/github/forks/lizhogn/python-webAI-tutorial.svg?style=social&label=Fork)](https://github.com/lizhogn/python-webAI-tutorial)
[![GitHub issues](https://img.shields.io/github/issues/lizhogn/python-webAI-tutorial.svg)](https://github.com/lizhogn/python-webAI-tutorial/issues)
[![GitHub license](https://img.shields.io/github/license/lizhogn/python-webAI-tutorial.svg)](https://github.com/lizhogn/python-webAI-tutorial/blob/main/LICENSE)

## 🎯 项目简介

本项目是一个完整的 Python Web AI 开发教程，从基础概念到实战应用，帮助学习者掌握现代 Web 开发与 AI 集成的全栈技能。

### ✨ 特色亮点

* 🚀 **循序渐进** 从 Web 基础到 AI 集成的完整学习路径
* 💻 **实战导向** 每个阶段都有完整的项目实践
* 🔧 **技术栈全面** 涵盖 Flask、FastAPI、Vue.js、Docker 等主流技术
* 🤖 **AI 集成** 从模型训练到 Web 部署的全流程
* 📚 **开源免费** 完全开源，持续更新维护

## 📖 文档结构

```
docs/
├── README.md              # 文档首页
├── preface.md             # 前言
├── _sidebar.md            # 侧边栏导航
├── _coverpage.md          # 封面页面
├── index.html             # Docsify 配置
├── chapter1/              # 第一章：Web 开发基础
│   ├── README.md
│   ├── 1.1-http-basics.md
│   ├── 1.2-web-frameworks.md
│   ├── 1.3-frontend-backend.md
│   └── 1.4-practice-project.md
├── chapter2/              # 第二章：后端开发进阶
│   ├── README.md
│   ├── 2.1-fastapi-advanced.md
│   ├── 2.2-database.md
│   ├── 2.3-api-design.md
│   ├── 2.4-authentication.md
│   └── 2.5-practice-project.md
├── chapter3/              # 第三章：前端开发
├── chapter4/              # 第四章：AI 模型集成
├── chapter5/              # 第五章：部署与运维
└── chapter6/              # 第六章：实战项目
```

## 🚀 快速开始

### 环境要求

- Node.js 16+
- npm 或 yarn

### 启动文档

1. **克隆项目**
   ```bash
   git clone https://github.com/lizhogn/python-webAI-tutorial.git
   cd python-webAI-tutorial
   ```

2. **启动文档服务器**
   ```bash
   # 使用启动脚本（推荐）
   ./start_docsify.sh
   
   # 或手动启动
   npm install -g docsify-cli
   cd docs
   docsify serve . --port 3000 --open
   ```

3. **访问文档**
   打开浏览器访问 http://localhost:3000

## 📚 学习路径

### 第一阶段：Web 开发基础 (2-3周)
- HTTP 协议基础
- Web 框架入门
- 前后端交互
- 实践项目：待办事项应用

### 第二阶段：后端开发进阶 (3-4周)
- FastAPI 高级特性
- 数据库操作
- API 设计
- 认证与安全
- 实践项目：用户管理系统

### 第三阶段：前端开发 (3-4周)
- Vue.js 基础
- 组件化开发
- 状态管理
- 路由和导航
- 实践项目：管理后台

### 第四阶段：AI 模型集成 (3-4周)
- 模型服务化
- 异步处理
- 性能优化
- 模型管理
- 实践项目：AI 预测服务

### 第五阶段：部署与运维 (2-3周)
- Docker 容器化
- 反向代理
- 监控与日志
- 安全加固
- 实践项目：生产环境部署

### 第六阶段：实战项目 (2-3周)
- 项目架构设计
- 开发流程
- 测试策略
- 部署上线
- 项目总结

## 💻 项目示例

### 快速开始项目

```bash
cd quick_start_project
pip install -r requirements.txt
python main.py
```

访问 http://localhost:8000 体验第一个 AI Web 应用！

### 完整教程项目

```bash
cd complete_tutorial
pip install -r requirements.txt
# 按照各阶段说明运行项目
```

## 🛠️ 技术栈

### 后端技术
- **Python 3.8+** - 主要开发语言
- **FastAPI** - 现代 Web 框架
- **SQLAlchemy** - ORM 数据库操作
- **Pydantic** - 数据验证
- **Celery** - 异步任务队列

### 前端技术
- **Vue.js 3.0+** - 前端框架
- **Bootstrap 5.0+** - UI 组件库
- **Axios** - HTTP 客户端
- **Vue Router** - 路由管理
- **Vuex** - 状态管理

### 部署运维
- **Docker** - 容器化部署
- **Nginx** - 反向代理
- **Redis** - 缓存和消息队列
- **PostgreSQL** - 主数据库

### AI 相关
- **scikit-learn** - 机器学习库
- **TensorFlow** - 深度学习框架
- **Hugging Face** - 预训练模型
- **ONNX** - 模型格式转换

## 📖 学习资源

### 官方文档
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Vue.js 官方文档](https://vuejs.org/)
- [Docker 官方文档](https://docs.docker.com/)

### 推荐阅读
- [Python Web 开发最佳实践](https://realpython.com/)
- [AI 模型部署指南](https://huggingface.co/docs)

## 🤝 如何贡献

我们欢迎任何形式的贡献！

* 🐛 **报告 Bug** - 发现问题请提交 Issue
* 💡 **功能建议** - 有好想法就告诉我们
* 📝 **内容完善** - 帮助改进教程内容
* 🔧 **代码优化** - 提交 Pull Request

### 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 开源协议

本作品采用 [MIT License](LICENSE) 进行许可。

## 🙏 致谢

感谢所有为本项目做出贡献的开发者们 ❤️

## 📞 联系我们

- 📧 Email: your-email@example.com
- 💬 微信群: 扫描二维码加入
- 🐛 Issues: [GitHub Issues](https://github.com/lizhogn/python-webAI-tutorial/issues)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=lizhogn/python-webAI-tutorial&type=Date)](https://star-history.com/#lizhogn/python-webAI-tutorial&Date)

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！ 