# 第二章 后端开发进阶

## 📖 章节概览

本章将深入学习 FastAPI 框架的高级特性，包括数据库操作、API 设计、认证授权、中间件等核心技能。通过本章学习，您将能够构建功能完整、性能优良的后端服务。

## 🎯 学习目标

- 掌握 FastAPI 的高级特性和最佳实践
- 学会使用 SQLAlchemy 进行数据库操作
- 理解 RESTful API 设计原则
- 实现用户认证和权限控制
- 掌握异步编程和性能优化
- 完成一个完整的后端 API 项目

## 📝 章节内容

### 2.1 FastAPI 进阶
- [依赖注入系统](2.1-fastapi-advanced.md)
- [中间件和异常处理](2.1-fastapi-advanced.md#中间件和异常处理)
- [异步编程基础](2.1-fastapi-advanced.md#异步编程基础)
- [性能优化技巧](2.1-fastapi-advanced.md#性能优化技巧)

### 2.2 数据库操作
- [SQLAlchemy ORM](2.2-database.md)
- [数据库模型设计](2.2-database.md#数据库模型设计)
- [查询和关系操作](2.2-database.md#查询和关系操作)
- [数据库迁移](2.2-database.md#数据库迁移)

### 2.3 API 设计
- [RESTful API 设计原则](2.3-api-design.md)
- [数据验证和序列化](2.3-api-design.md#数据验证和序列化)
- [API 文档和测试](2.3-api-design.md#api-文档和测试)
- [版本控制和兼容性](2.3-api-design.md#版本控制和兼容性)

### 2.4 认证与安全
- [JWT 认证](2.4-authentication.md)
- [OAuth2 集成](2.4-authentication.md#oauth2-集成)
- [权限控制](2.4-authentication.md#权限控制)
- [安全最佳实践](2.4-authentication.md#安全最佳实践)

### 2.5 实践项目
- [项目：用户管理系统](2.5-practice-project.md)
- [系统架构设计](2.5-practice-project.md#系统架构设计)
- [用户认证系统](2.5-practice-project.md#用户认证系统)
- [API 接口开发](2.5-practice-project.md#api-接口开发)
- [测试和部署](2.5-practice-project.md#测试和部署)

## 💻 代码示例

### 数据库模型

```python
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
```

### API 路由

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/users/", response_model=List[UserSchema])
async def get_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users/", response_model=UserSchema)
async def create_user(
    user: UserCreate, 
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
```

## 🎯 实践练习

1. **基础练习**
   - 创建用户注册和登录 API
   - 实现基本的 CRUD 操作
   - 添加数据验证和错误处理

2. **进阶练习**
   - 实现 JWT 认证系统
   - 添加角色权限控制
   - 实现文件上传功能

3. **项目实战**
   - 完成用户管理系统
   - 添加 API 文档和测试
   - 实现性能优化

## 📚 学习资源

### 官方文档
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/)
- [Pydantic 官方文档](https://pydantic-docs.helpmanual.io/)

### 推荐阅读
- [RESTful API 设计指南](https://restfulapi.net/)
- [数据库设计最佳实践](https://www.postgresql.org/docs/)

## 🔍 知识检查

完成本章学习后，请检查是否掌握以下知识点：

- [ ] 能够使用 FastAPI 的高级特性
- [ ] 掌握 SQLAlchemy ORM 的使用
- [ ] 理解 RESTful API 设计原则
- [ ] 能够实现用户认证和权限控制
- [ ] 完成本章的实践项目

## 🚀 下一步

掌握后端开发进阶技能后，您将进入：

**[第三章 前端开发](chapter3/README.md)** - 学习 Vue.js 前端框架，构建现代化的用户界面。

---

**上一章**：[第一章 Web 开发基础](chapter1/README.md) | **下一章**：[第三章 前端开发](chapter3/README.md) 