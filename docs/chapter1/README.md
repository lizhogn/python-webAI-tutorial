# 第一章 Web 开发基础

## 📖 章节概览

本章将介绍 Web 开发的基础概念，包括 HTTP 协议、Web 框架、前后端交互等核心知识。通过本章学习，您将掌握现代 Web 开发的基本原理和工具。

## 🎯 学习目标

- 理解 HTTP 协议的工作原理
- 掌握 Web 框架的基本概念
- 学会使用 Flask 和 FastAPI 构建 Web 应用
- 了解前后端分离架构
- 完成第一个 Web 应用项目

## 📝 章节内容

### 1.1 HTTP 协议基础
- [HTTP 协议概述](1.1-http-basics.md)
- [请求和响应](1.1-http-basics.md#请求和响应)
- [状态码和头部](1.1-http-basics.md#状态码和头部)
- [RESTful API 设计](1.1-http-basics.md#restful-api-设计)

### 1.2 Web 框架入门
- [Web 框架简介](1.2-web-frameworks.md)
- [Flask 基础](1.2-web-frameworks.md#flask-基础)
- [FastAPI 入门](1.2-web-frameworks.md#fastapi-入门)
- [框架对比与选择](1.2-web-frameworks.md#框架对比与选择)

### 1.3 前后端交互
- [前后端分离架构](1.3-frontend-backend.md)
- [JSON 数据交换](1.3-frontend-backend.md#json-数据交换)
- [AJAX 和 Fetch API](1.3-frontend-backend.md#ajax-和-fetch-api)
- [CORS 跨域处理](1.3-frontend-backend.md#cors-跨域处理)

### 1.4 实践项目
- [项目：简单的待办事项应用](1.4-practice-project.md)
- [项目需求分析](1.4-practice-project.md#项目需求分析)
- [后端 API 开发](1.4-practice-project.md#后端-api-开发)
- [前端界面实现](1.4-practice-project.md#前端界面实现)
- [项目部署和测试](1.4-practice-project.md#项目部署和测试)

## 💻 代码示例

### 快速开始

```python
# 使用 FastAPI 创建简单的 Web 应用
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

### 运行应用

```bash
# 安装依赖
pip install fastapi uvicorn

# 启动服务器
uvicorn main:app --reload
```

## 🎯 实践练习

1. **基础练习**
   - 创建一个简单的 Hello World 应用
   - 实现基本的 GET 和 POST 接口
   - 添加参数验证和错误处理

2. **进阶练习**
   - 构建一个简单的博客系统
   - 实现用户注册和登录功能
   - 添加文件上传功能

3. **项目实战**
   - 完成待办事项应用
   - 添加数据持久化
   - 实现用户界面优化

## 📚 学习资源

### 官方文档
- [HTTP 协议规范](https://tools.ietf.org/html/rfc7231)
- [Flask 官方文档](https://flask.palletsprojects.com/)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)

### 推荐阅读
- [Web 开发最佳实践](https://developer.mozilla.org/en-US/docs/Learn)
- [RESTful API 设计指南](https://restfulapi.net/)

## 🔍 知识检查

完成本章学习后，请检查是否掌握以下知识点：

- [ ] 能够解释 HTTP 协议的基本工作原理
- [ ] 理解 Web 框架的作用和优势
- [ ] 能够使用 Flask 或 FastAPI 创建简单的 Web 应用
- [ ] 了解前后端分离架构的概念
- [ ] 完成本章的实践项目

## 🚀 下一步

掌握 Web 开发基础后，您将进入：

**[第二章 后端开发进阶](chapter2/README.md)** - 深入学习 FastAPI、数据库操作、API 设计等进阶技能。

---

**上一章**：[前言](preface.md) | **下一章**：[第二章 后端开发进阶](chapter2/README.md) 