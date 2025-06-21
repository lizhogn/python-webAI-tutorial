# 第8章：前后端通信

## 📚 学习目标

通过本章学习，你将掌握：
- 前后端分离架构下的通信原理
- HTTP请求与响应流程
- 使用Axios进行API请求
- 跨域（CORS）原理与解决方案
- 前端与后端数据格式约定
- 常见前后端通信错误与调试方法

## 🌐 前后端通信基础

### 8.1 前后端分离通信流程

1. 前端通过HTTP请求（如GET/POST/PUT/DELETE）访问后端API接口
2. 后端处理请求，返回JSON等格式的数据响应
3. 前端解析响应数据，渲染页面或更新状态

### 8.2 常见通信方式

- RESTful API（主流，推荐）
- WebSocket（实时通信）
- GraphQL（灵活查询）

## 🔗 使用Axios进行API请求

### 8.3 安装与配置

```bash
npm install axios
```

```typescript
// src/utils/request.ts
import axios from 'axios'

const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 10000
})

// 请求拦截器
service.interceptors.request.use(config => {
  // 可在此处添加Token等认证信息
  // config.headers['Authorization'] = 'Bearer ...'
  return config
}, error => Promise.reject(error))

// 响应拦截器
service.interceptors.response.use(
  response => response.data,
  error => {
    // 统一错误处理
    return Promise.reject(error)
  }
)

export default service
```

### 8.4 发送请求示例

```typescript
import request from '@/utils/request'

// GET请求
export function fetchUsers(params?: any) {
  return request({
    url: '/api/v1/users',
    method: 'get',
    params
  })
}

// POST请求
export function createUser(data: any) {
  return request({
    url: '/api/v1/users',
    method: 'post',
    data
  })
}
```

## 🛡️ 跨域（CORS）

### 8.5 什么是CORS？

CORS（跨域资源共享）是一种浏览器安全机制，防止前端直接访问不同源的API。

- **同源策略**：协议、域名、端口必须完全一致
- **跨域场景**：前端本地开发，后端部署在远程服务器

### 8.6 FastAPI后端CORS配置

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议指定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📦 数据格式与约定

### 8.7 常用数据格式

- JSON（主流，推荐）
- Form Data（文件上传）
- Multipart（图片/文件上传）

### 8.8 前后端数据约定

- 统一响应结构（如：`{ success, data, message }`）
- 错误码与错误信息
- 分页、排序、过滤参数

## 🛠️ 常见通信错误与调试

### 8.9 常见错误

- 404：接口地址错误
- 401/403：未认证或无权限
- 500：后端服务异常
- CORS错误：跨域未配置

### 8.10 调试技巧

- 使用浏览器开发者工具（Network面板）
- 使用Postman/Insomnia等API测试工具
- 查看后端日志，定位问题

## 💻 实践项目

### 项目：用户管理前后端联调

1. 前端页面通过Axios请求后端API，获取用户列表并渲染
2. 新增、编辑、删除用户均通过API完成
3. 处理接口异常，友好提示用户

## 📝 本章小结

### 重点概念
- ✅ 前后端通信流程与原理
- ✅ Axios请求与拦截器
- ✅ CORS跨域配置
- ✅ 数据格式与接口约定
- ✅ 常见错误与调试方法

### 关键技能
- ✅ 使用Axios与后端API通信
- ✅ 配置后端CORS
- ✅ 处理前后端数据格式
- ✅ 调试和排查通信问题

## 🔗 扩展阅读

- [Axios官方文档](https://axios-http.com/)
- [MDN CORS说明](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS)
- [前后端分离最佳实践](https://juejin.cn/post/6844904106230683655)

## ❓ 常见问题

**Q: 为什么会出现CORS错误？**
A: 因为浏览器的同源策略，需后端正确配置CORS中间件。

**Q: 如何统一前后端接口数据结构？**
A: 约定统一的响应格式和错误码，前后端共同遵守。

**Q: 如何调试前后端通信问题？**
A: 使用浏览器Network面板、API测试工具、后端日志等多种手段定位。 