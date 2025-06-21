# 快速开始

## 🚀 环境准备

### 系统要求
- **操作系统**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8 或更高版本
- **Node.js**: 16.0 或更高版本
- **Git**: 最新版本
- **Docker**: 20.10 或更高版本 (可选)

### 开发工具
- **代码编辑器**: VS Code (推荐)
- **终端**: 系统默认终端或 iTerm2 (macOS)
- **浏览器**: Chrome, Firefox, Safari 或 Edge

## 📦 安装步骤

### 1. 克隆项目

```bash
# 克隆项目到本地
git clone https://github.com/lizhogn/python-webAI-tutorial.git

# 进入项目目录
cd python-webAI-tutorial
```

### 2. 后端环境配置

```bash
# 创建 Python 虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖包
pip install -r requirements.txt
```

### 3. 前端环境配置

```bash
# 进入前端目录
cd frontend

# 安装 Node.js 依赖
npm install

# 或者使用 yarn
yarn install
```

### 4. 数据库配置

```bash
# 安装 PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# 安装 PostgreSQL (macOS)
brew install postgresql

# 启动 PostgreSQL 服务
# Ubuntu/Debian
sudo systemctl start postgresql
# macOS
brew services start postgresql

# 创建数据库和用户
sudo -u postgres psql
CREATE DATABASE happy_llm;
CREATE USER happy_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE happy_llm TO happy_user;
\q
```

### 5. 环境变量配置

创建 `.env` 文件：

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑环境变量
nano .env
```

配置内容：

```env
# 数据库配置
DATABASE_URL=postgresql://happy_user:your_password@localhost/happy_llm

# OpenAI API 配置
OPENAI_API_KEY=your_openai_api_key

# 应用配置
SECRET_KEY=your_secret_key
DEBUG=True
```

## 🏃‍♂️ 启动应用

### 1. 启动后端服务

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行数据库迁移
alembic upgrade head

# 启动后端服务
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. 启动前端服务

```bash
# 新开一个终端窗口
cd frontend

# 启动开发服务器
npm run dev

# 或者使用 yarn
yarn dev
```

### 3. 访问应用

- **后端 API**: http://localhost:8000
- **API 文档**: http://localhost:8000/docs
- **前端应用**: http://localhost:3000

## 🧪 测试验证

### 1. 后端 API 测试

```bash
# 测试健康检查接口
curl http://localhost:8000/health

# 测试聊天接口
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, AI!"}'
```

### 2. 前端功能测试

1. 打开浏览器访问 http://localhost:3000
2. 在聊天界面输入消息
3. 检查 AI 回复是否正常
4. 测试用户注册和登录功能

### 3. 数据库连接测试

```bash
# 进入 Python 交互环境
python

# 测试数据库连接
from database import engine
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("数据库连接成功!")
```

## 🔧 常见问题

### 1. Python 环境问题

```bash
# 检查 Python 版本
python --version

# 如果版本过低，升级 Python
# Ubuntu/Debian
sudo apt install python3.9

# macOS
brew install python@3.9
```

### 2. 依赖安装失败

```bash
# 升级 pip
pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 3. 数据库连接失败

```bash
# 检查 PostgreSQL 服务状态
sudo systemctl status postgresql

# 重启 PostgreSQL 服务
sudo systemctl restart postgresql

# 检查数据库连接
psql -h localhost -U happy_user -d happy_llm
```

### 4. 端口被占用

```bash
# 查看端口占用情况
lsof -i :8000
lsof -i :3000

# 杀死占用进程
kill -9 <PID>
```

## 📚 学习路径

### 第一天：环境搭建
- [x] 完成环境配置
- [x] 启动应用并测试
- [x] 阅读项目结构

### 第二天：基础功能
- [ ] 学习 FastAPI 基础
- [ ] 理解 API 设计
- [ ] 测试聊天功能

### 第三天：前端开发
- [ ] 学习 Vue.js 基础
- [ ] 理解组件化开发
- [ ] 修改界面样式

### 第四天：功能扩展
- [ ] 添加用户认证
- [ ] 实现数据持久化
- [ ] 优化用户体验

### 第五天：部署上线
- [ ] 学习 Docker 容器化
- [ ] 配置生产环境
- [ ] 部署到服务器

## 🎯 下一步

完成快速开始后，建议按以下顺序学习：

1. **阅读文档**: 从 [前言](preface.md) 开始，了解项目背景
2. **跟随教程**: 按章节顺序学习 [教程内容](../#-教程内容)
3. **动手实践**: 每章都有实践项目，务必完成
4. **扩展学习**: 参考 [工具与资源](../#️-工具与资源) 深入学习

## 💡 学习建议

1. **循序渐进**: 不要急于求成，打好基础很重要
2. **动手实践**: 理论结合实践，多写代码
3. **记录笔记**: 记录学习过程中的问题和解决方案
4. **参与讨论**: 遇到问题及时在社区寻求帮助

## 🔗 相关链接

- [项目 GitHub 仓库](https://github.com/lizhogn/python-webAI-tutorial)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Vue.js 官方文档](https://vuejs.org/)
- [Docker 官方文档](https://docs.docker.com/)

**开始你的学习之旅吧！** 🚀 