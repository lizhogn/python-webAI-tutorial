# 常见问题

## 🚀 环境配置问题

### Q1: Python 版本不兼容怎么办？

**A**: 确保使用 Python 3.8 或更高版本。

```bash
# 检查 Python 版本
python --version

# 如果版本过低，升级 Python
# Ubuntu/Debian
sudo apt update
sudo apt install python3.9 python3.9-venv

# macOS
brew install python@3.9

# Windows
# 从 python.org 下载最新版本
```

### Q2: 依赖包安装失败怎么办？

**A**: 尝试以下解决方案：

```bash
# 升级 pip
pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 或者使用阿里云镜像
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 如果仍有问题，尝试逐个安装
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

### Q3: Node.js 版本过低怎么办？

**A**: 升级到 Node.js 16.0 或更高版本。

```bash
# 检查 Node.js 版本
node --version

# 使用 nvm 管理 Node.js 版本
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 安装最新 LTS 版本
nvm install --lts
nvm use --lts
```

## 🗄️ 数据库问题

### Q4: PostgreSQL 连接失败怎么办？

**A**: 检查数据库配置和服务状态。

```bash
# 检查 PostgreSQL 服务状态
sudo systemctl status postgresql

# 启动 PostgreSQL 服务
sudo systemctl start postgresql

# 检查数据库连接
psql -h localhost -U happy_user -d happy_llm

# 如果连接失败，检查 pg_hba.conf 配置
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

### Q5: 数据库迁移失败怎么办？

**A**: 检查数据库配置和迁移文件。

```bash
# 检查数据库连接
python -c "from database import engine; print('连接成功')"

# 重新生成迁移文件
alembic revision --autogenerate -m "initial"

# 执行迁移
alembic upgrade head

# 如果仍有问题，检查 models.py 文件
```

### Q6: Redis 连接失败怎么办？

**A**: 确保 Redis 服务正在运行。

```bash
# 检查 Redis 服务状态
sudo systemctl status redis

# 启动 Redis 服务
sudo systemctl start redis

# 测试 Redis 连接
redis-cli ping

# 如果返回 PONG，说明连接正常
```

## 🔧 应用启动问题

### Q7: 后端服务启动失败怎么办？

**A**: 检查端口占用和配置问题。

```bash
# 检查端口占用
lsof -i :8000

# 杀死占用进程
kill -9 <PID>

# 检查环境变量
cat .env

# 启动服务
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Q8: 前端服务启动失败怎么办？

**A**: 检查 Node.js 依赖和端口配置。

```bash
# 进入前端目录
cd frontend

# 清理依赖
rm -rf node_modules package-lock.json

# 重新安装依赖
npm install

# 启动开发服务器
npm run dev

# 如果端口被占用，修改 vite.config.js
```

### Q9: API 调用失败怎么办？

**A**: 检查 API 端点和请求格式。

```bash
# 测试健康检查接口
curl http://localhost:8000/health

# 测试聊天接口
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'

# 检查 API 文档
# 访问 http://localhost:8000/docs
```

## 🤖 AI 集成问题

### Q10: OpenAI API 调用失败怎么办？

**A**: 检查 API 密钥和网络连接。

```bash
# 检查环境变量
echo $OPENAI_API_KEY

# 测试 API 连接
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
  https://api.openai.com/v1/models

# 如果网络问题，配置代理
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
```

### Q11: AI 响应速度慢怎么办？

**A**: 优化模型配置和缓存策略。

```python
# 在 .env 中配置模型参数
OPENAI_MODEL=gpt-3.5-turbo  # 使用更快的模型
OPENAI_MAX_TOKENS=1000      # 限制响应长度
OPENAI_TEMPERATURE=0.7      # 调整创造性

# 启用缓存
CACHE_ENABLED=True
REDIS_URL=redis://localhost:6379
```

### Q12: 异步任务处理失败怎么办？

**A**: 检查 Celery 和 Redis 配置。

```bash
# 启动 Celery Worker
celery -A app.celery worker --loglevel=info

# 启动 Celery Beat (如果需要定时任务)
celery -A app.celery beat --loglevel=info

# 检查 Redis 连接
redis-cli ping
```

## 🐳 Docker 部署问题

### Q13: Docker 镜像构建失败怎么办？

**A**: 检查 Dockerfile 和依赖配置。

```bash
# 清理 Docker 缓存
docker system prune -a

# 重新构建镜像
docker build -t happy-llm .

# 检查构建日志
docker build -t happy-llm . --progress=plain

# 如果网络问题，使用国内镜像
# 在 Dockerfile 中添加
# RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
```

### Q14: Docker Compose 启动失败怎么办？

**A**: 检查 docker-compose.yml 配置。

```bash
# 检查服务状态
docker-compose ps

# 查看服务日志
docker-compose logs

# 重新启动服务
docker-compose down
docker-compose up -d

# 检查网络连接
docker network ls
```

### Q15: 容器间通信失败怎么办？

**A**: 检查 Docker 网络配置。

```bash
# 检查网络配置
docker network inspect happy-llm_default

# 进入容器测试连接
docker exec -it happy-llm-backend ping happy-llm-db

# 检查端口映射
docker port happy-llm-backend
```

## 🔒 安全配置问题

### Q16: JWT 认证失败怎么办？

**A**: 检查密钥配置和令牌格式。

```python
# 检查 SECRET_KEY 配置
import os
print(os.getenv('SECRET_KEY'))

# 生成新的密钥
import secrets
print(secrets.token_urlsafe(32))

# 检查令牌格式
# 确保令牌包含三部分：header.payload.signature
```

### Q17: CORS 跨域问题怎么办？

**A**: 配置正确的 CORS 设置。

```python
# 在 FastAPI 应用中配置 CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Q18: 数据库密码泄露怎么办？

**A**: 立即更改密码并检查安全配置。

```bash
# 更改数据库密码
sudo -u postgres psql
ALTER USER happy_user WITH PASSWORD 'new_secure_password';
\q

# 更新环境变量
nano .env
# 修改 DATABASE_URL

# 重启应用
docker-compose restart
```

## 📊 性能优化问题

### Q19: 应用响应速度慢怎么办？

**A**: 进行性能分析和优化。

```bash
# 使用 cProfile 分析性能
python -m cProfile -o profile.stats main.py

# 使用 memory_profiler 分析内存
pip install memory_profiler
python -m memory_profiler main.py

# 检查数据库查询性能
# 在 SQLAlchemy 中启用日志
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

### Q20: 内存使用过高怎么办？

**A**: 优化内存使用和垃圾回收。

```python
# 在 .env 中配置内存限制
MAX_WORKERS=4
WORKER_MEMORY_LIMIT=512MB

# 使用连接池
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20

# 定期清理缓存
import gc
gc.collect()
```

## 🔍 调试技巧

### Q21: 如何调试 FastAPI 应用？

**A**: 使用调试工具和日志。

```python
# 启用调试模式
DEBUG=True

# 添加详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

# 使用 pdb 调试
import pdb; pdb.set_trace()

# 使用 FastAPI 调试器
uvicorn main:app --reload --log-level debug
```

### Q22: 如何调试 Vue.js 应用？

**A**: 使用浏览器开发工具。

```javascript
// 在代码中添加调试信息
console.log('调试信息:', data)

// 使用 Vue DevTools 浏览器插件
// 安装 Vue DevTools 扩展

// 在组件中添加调试
export default {
  mounted() {
    console.log('组件已挂载')
  }
}
```

### Q23: 如何查看应用日志？

**A**: 配置日志系统和监控。

```bash
# 查看 Docker 容器日志
docker-compose logs -f

# 查看特定服务日志
docker-compose logs -f backend

# 查看系统日志
journalctl -u docker.service -f

# 配置日志文件
# 在 docker-compose.yml 中添加
volumes:
  - ./logs:/app/logs
```

## 📞 获取帮助

### Q24: 在哪里可以获得帮助？

**A**: 多种渠道获取技术支持。

- **GitHub Issues**: 在项目仓库提交问题
- **Stack Overflow**: 搜索或提问技术问题
- **技术社区**: 掘金、思否、V2EX 等
- **官方文档**: 各技术的官方文档
- **Discord/Slack**: 加入技术交流群

### Q25: 如何提交 Bug 报告？

**A**: 提供详细的问题描述。

```markdown
## Bug 描述
详细描述遇到的问题

## 复现步骤
1. 第一步
2. 第二步
3. 第三步

## 期望行为
描述期望的正确行为

## 实际行为
描述实际发生的错误

## 环境信息
- 操作系统: Ubuntu 20.04
- Python 版本: 3.9.7
- Node.js 版本: 16.13.0
- Docker 版本: 20.10.12

## 错误日志
粘贴相关的错误日志
```

### Q26: 如何贡献代码？

**A**: 遵循项目的贡献指南。

1. Fork 项目仓库
2. 创建功能分支
3. 编写代码和测试
4. 提交 Pull Request
5. 等待代码审查

**记住：遇到问题时，先查看文档和搜索现有解决方案！** 🔍 