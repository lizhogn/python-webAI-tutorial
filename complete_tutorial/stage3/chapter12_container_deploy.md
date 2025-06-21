# 第12章：容器化与部署

## 📚 学习目标

通过本章学习，你将掌握：
- 容器化基础与Docker原理
- 编写Dockerfile与多阶段构建
- Docker Compose编排多服务
- FastAPI+前端+数据库一体化部署
- 云服务器部署与常见运维

## 🐳 容器化基础

### 12.1 什么是容器？
- 轻量级、可移植、隔离的运行环境
- 解决"在我电脑上能跑"的问题

### 12.2 Docker核心概念
- 镜像（Image）：应用及其依赖的只读模板
- 容器（Container）：镜像运行时的实例
- 仓库（Registry）：存储和分发镜像的平台

## 🛠️ 编写Dockerfile

### 12.3 FastAPI后端Dockerfile

```dockerfile
# backend/Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 12.4 前端Dockerfile（Vue）

```dockerfile
# frontend/Dockerfile
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 🔗 Docker Compose多服务编排

### 12.5 docker-compose.yml示例

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/appdb
    depends_on:
      - db
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: appdb
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:
```

## ☁️ 云服务器部署

### 12.6 云服务器部署流程
1. 购买云服务器（如阿里云、腾讯云、AWS）
2. 安装Docker和Docker Compose
3. 上传项目代码
4. 配置环境变量和端口安全组
5. 一键启动：`docker-compose up -d`
6. 访问公网IP测试服务

### 12.7 常见运维操作
- 查看日志：`docker-compose logs -f backend`
- 重启服务：`docker-compose restart backend`
- 数据备份：挂载卷定期备份
- 镜像更新：`docker-compose pull && up -d`

## 💻 实践项目

### 项目：全栈AI应用一键部署
- 编写后端、前端、数据库Dockerfile
- 用docker-compose一键启动所有服务
- 云服务器上线并测试

## 📝 本章小结

### 重点概念
- ✅ 容器化与Docker原理
- ✅ Dockerfile与Compose编排
- ✅ 一体化部署全栈应用
- ✅ 云服务器部署与运维

### 关键技能
- ✅ 编写Dockerfile
- ✅ 使用Compose编排多服务
- ✅ 云服务器部署上线

## 🔗 扩展阅读
- [Docker官方文档](https://docs.docker.com/)
- [Compose文档](https://docs.docker.com/compose/)
- [云服务器部署教程](https://cloud.tencent.com/developer/article/1630052)

## ❓ 常见问题

**Q: Docker和虚拟机有何区别？**
A: Docker更轻量，资源占用低，启动快，适合微服务和持续集成。

**Q: 如何安全管理数据库数据？**
A: 使用数据卷，定期备份，生产环境建议分离数据库和应用。 