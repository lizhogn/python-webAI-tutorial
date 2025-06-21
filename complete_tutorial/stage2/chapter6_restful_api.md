# 第6章：RESTful API设计

## 📚 学习目标

通过本章学习，你将掌握：
- REST架构风格的核心原则
- HTTP方法和状态码的正确使用
- API设计的最佳实践
- 版本控制和文档规范
- 错误处理和响应格式
- API安全和认证机制

## 🌐 REST架构基础

### 6.1 什么是REST？

REST (Representational State Transfer) 是一种软件架构风格，用于设计网络应用程序的API。它基于HTTP协议，具有以下特点：

- **无状态**：每个请求包含所有必要信息
- **统一接口**：使用标准HTTP方法
- **资源导向**：以资源为中心设计API
- **可缓存**：支持缓存机制
- **分层系统**：支持代理、网关等中间层

### 6.2 REST vs 其他API风格

| 特性 | REST | GraphQL | gRPC | SOAP |
|------|------|---------|------|------|
| 协议 | HTTP | HTTP | HTTP/2 | HTTP/SMTP |
| 数据格式 | JSON/XML | JSON | Protocol Buffers | XML |
| 查询灵活性 | 固定 | 高度灵活 | 中等 | 固定 |
| 性能 | 中等 | 高 | 很高 | 低 |
| 学习曲线 | 简单 | 中等 | 中等 | 复杂 |

## 🔧 HTTP方法和状态码

### 6.3 HTTP方法详解

```python
from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

app = FastAPI()

# GET - 获取资源
@app.get("/users/", response_model=List[User])
async def get_users(skip: int = 0, limit: int = 10):
    """获取用户列表"""
    return get_users_from_db(skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """获取单个用户"""
    user = get_user_from_db(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

# POST - 创建资源
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """创建新用户"""
    return create_user_in_db(user)

# PUT - 完整更新资源
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    """完整更新用户信息"""
    updated_user = update_user_in_db(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return updated_user

# PATCH - 部分更新资源
@app.patch("/users/{user_id}", response_model=User)
async def patch_user(user_id: int, user: UserPatch):
    """部分更新用户信息"""
    patched_user = patch_user_in_db(user_id, user)
    if not patched_user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return patched_user

# DELETE - 删除资源
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """删除用户"""
    success = delete_user_from_db(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="用户不存在")
```

### 6.4 HTTP状态码使用

```python
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse

app = FastAPI()

# 成功响应
@app.get("/success")
async def success_example():
    return {"message": "操作成功"}

@app.post("/created", status_code=status.HTTP_201_CREATED)
async def created_example():
    return {"message": "资源创建成功"}

@app.put("/updated", status_code=status.HTTP_200_OK)
async def updated_example():
    return {"message": "资源更新成功"}

@app.delete("/deleted", status_code=status.HTTP_204_NO_CONTENT)
async def deleted_example():
    return None

# 客户端错误
@app.get("/bad-request")
async def bad_request_example():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="请求参数错误"
    )

@app.get("/unauthorized")
async def unauthorized_example():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="需要身份验证"
    )

@app.get("/forbidden")
async def forbidden_example():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="没有权限访问"
    )

@app.get("/not-found")
async def not_found_example():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="资源不存在"
    )

@app.get("/conflict")
async def conflict_example():
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="资源冲突"
    )

# 服务器错误
@app.get("/internal-error")
async def internal_error_example():
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="服务器内部错误"
    )

# 自定义响应
@app.get("/custom-response")
async def custom_response():
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"message": "请求已接受，正在处理"}
    )
```

## 📋 API设计最佳实践

### 6.5 URL设计规范

```python
# 好的URL设计
@app.get("/api/v1/users")                    # 获取用户列表
@app.get("/api/v1/users/{user_id}")          # 获取特定用户
@app.post("/api/v1/users")                   # 创建用户
@app.put("/api/v1/users/{user_id}")          # 更新用户
@app.delete("/api/v1/users/{user_id}")       # 删除用户

@app.get("/api/v1/users/{user_id}/posts")    # 获取用户的文章
@app.get("/api/v1/users/{user_id}/posts/{post_id}")  # 获取特定文章

# 查询参数
@app.get("/api/v1/posts")
async def get_posts(
    page: int = Query(1, ge=1, description="页码"),
    size: int = Query(10, ge=1, le=100, description="每页数量"),
    category: Optional[str] = Query(None, description="分类"),
    author: Optional[str] = Query(None, description="作者"),
    sort: str = Query("created_at", description="排序字段"),
    order: str = Query("desc", regex="^(asc|desc)$", description="排序方向")
):
    """获取文章列表，支持分页、过滤和排序"""
    pass
```

### 6.6 响应格式标准化

```python
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List
from datetime import datetime

# 标准响应模型
class StandardResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)

# 分页响应模型
T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int
    has_next: bool
    has_prev: bool

# 错误响应模型
class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    message: str
    details: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)

# 使用示例
@app.get("/api/v1/users", response_model=PaginatedResponse[User])
async def get_users_paginated(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    users, total = get_users_with_pagination(page, size)
    pages = (total + size - 1) // size
    
    return PaginatedResponse(
        items=users,
        total=total,
        page=page,
        size=size,
        pages=pages,
        has_next=page < pages,
        has_prev=page > 1
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.detail,
            message="请求处理失败",
            details={"status_code": exc.status_code}
        ).dict()
    )
```

### 6.7 数据验证和序列化

```python
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional
from datetime import datetime

# 输入模型
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., min_length=6, description="密码")
    full_name: Optional[str] = Field(None, max_length=100, description="全名")
    
    @validator('username')
    def username_must_be_valid(cls, v):
        if not v.isalnum():
            raise ValueError('用户名只能包含字母和数字')
        return v
    
    @validator('password')
    def password_must_be_strong(cls, v):
        if len(v) < 6:
            raise ValueError('密码长度至少6位')
        if not any(c.isupper() for c in v):
            raise ValueError('密码必须包含大写字母')
        if not any(c.isdigit() for c in v):
            raise ValueError('密码必须包含数字')
        return v

# 更新模型
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = None

# 响应模型
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

# 使用模型
@app.post("/api/v1/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    """创建用户，自动验证输入数据"""
    return create_user_in_db(user)

@app.put("/api/v1/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate):
    """更新用户，支持部分更新"""
    return update_user_in_db(user_id, user)
```

## 🔐 API安全和认证

### 6.8 基本认证

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import secrets

app = FastAPI()
security = HTTPBasic()
bearer = HTTPBearer()

# 基本认证
def get_current_user_basic(credentials: HTTPBasicCredentials = Depends(security)):
    """基本认证验证"""
    is_correct_username = secrets.compare_digest(credentials.username, "admin")
    is_correct_password = secrets.compare_digest(credentials.password, "password")
    
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Bearer Token认证
def get_current_user_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    """Token认证验证"""
    token = credentials.credentials
    user = verify_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# 使用认证
@app.get("/api/v1/protected-basic")
async def protected_basic(current_user: str = Depends(get_current_user_basic)):
    return {"message": f"Hello {current_user}", "method": "basic"}

@app.get("/api/v1/protected-token")
async def protected_token(current_user: dict = Depends(get_current_user_token)):
    return {"message": f"Hello {current_user['username']}", "method": "token"}
```

### 6.9 JWT认证

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# JWT配置
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

# 创建Token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 验证Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return {"username": username}
    except JWTError:
        return None

# 获取当前用户
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = verify_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# 登录接口
@app.post("/api/v1/login")
async def login(username: str, password: str):
    # 验证用户名密码
    if not authenticate_user(username, password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    
    # 创建访问Token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }

# 受保护的接口
@app.get("/api/v1/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"]}
```

## 📚 API版本控制

### 6.10 URL版本控制

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()

# v1版本
v1_router = APIRouter(prefix="/api/v1", tags=["v1"])

@v1_router.get("/users")
async def get_users_v1():
    return {"version": "v1", "users": []}

@v1_router.post("/users")
async def create_user_v1():
    return {"version": "v1", "message": "用户创建成功"}

# v2版本
v2_router = APIRouter(prefix="/api/v2", tags=["v2"])

@v2_router.get("/users")
async def get_users_v2():
    return {"version": "v2", "users": [], "metadata": {"total": 0}}

@v2_router.post("/users")
async def create_user_v2():
    return {"version": "v2", "message": "用户创建成功", "id": 123}

# 注册路由
app.include_router(v1_router)
app.include_router(v2_router)
```

### 6.11 Header版本控制

```python
from fastapi import FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI()

def get_api_version(accept_version: Optional[str] = Header(None)):
    """从Header获取API版本"""
    if not accept_version:
        return "v1"  # 默认版本
    return accept_version

@app.get("/api/users")
async def get_users(version: str = Depends(get_api_version)):
    if version == "v1":
        return {"version": "v1", "users": []}
    elif version == "v2":
        return {"version": "v2", "users": [], "metadata": {"total": 0}}
    else:
        raise HTTPException(status_code=400, detail="不支持的API版本")
```

## 📖 API文档规范

### 6.12 OpenAPI文档配置

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="我的API",
    description="这是一个示例API，展示了RESTful API设计的最佳实践",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 自定义OpenAPI模式
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="我的API",
        version="1.0.0",
        description="这是一个示例API",
        routes=app.routes,
    )
    
    # 添加安全定义
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    
    # 添加全局安全要求
    openapi_schema["security"] = [{"BearerAuth": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# API端点示例
@app.get(
    "/api/v1/users",
    response_model=List[UserResponse],
    summary="获取用户列表",
    description="获取系统中的所有用户，支持分页和过滤",
    response_description="用户列表",
    tags=["用户管理"]
)
async def get_users(
    skip: int = Query(0, ge=0, description="跳过的记录数"),
    limit: int = Query(10, ge=1, le=100, description="返回的记录数")
):
    """
    获取用户列表
    
    - **skip**: 跳过的记录数，用于分页
    - **limit**: 返回的记录数，最大100
    """
    return get_users_from_db(skip=skip, limit=limit)
```

## 💻 实践项目

### 项目：博客API系统

创建一个完整的博客API系统。

#### 步骤1：数据模型

```python
# models.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class PostStatus(str, Enum):
    draft = "draft"
    published = "published"
    archived = "archived"

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    full_name: Optional[str] = Field(None, max_length=100)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    excerpt: Optional[str] = Field(None, max_length=500)
    status: PostStatus = PostStatus.draft
    category_id: Optional[int] = None
    tags: List[str] = []

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    excerpt: Optional[str] = Field(None, max_length=500)
    status: Optional[PostStatus] = None
    category_id: Optional[int] = None
    tags: Optional[List[str]] = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    excerpt: Optional[str]
    status: PostStatus
    author_id: int
    category_id: Optional[int]
    tags: List[str]
    view_count: int
    created_at: datetime
    updated_at: datetime
    author: UserResponse
    
    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)
    parent_id: Optional[int] = None

class CommentResponse(BaseModel):
    id: int
    content: str
    author_id: int
    post_id: int
    parent_id: Optional[int]
    is_approved: bool
    created_at: datetime
    author: UserResponse
    
    class Config:
        orm_mode = True
```

#### 步骤2：API实现

```python
# api.py
from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer
from typing import List, Optional
from models import *

app = FastAPI(
    title="博客API",
    description="一个完整的博客系统API",
    version="1.0.0"
)

security = HTTPBearer()

# 依赖函数
def get_current_user(credentials = Depends(security)):
    # 验证Token并返回用户信息
    pass

# 用户相关API
@app.post("/api/v1/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """创建新用户"""
    pass

@app.get("/api/v1/users", response_model=List[UserResponse])
async def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """获取用户列表"""
    pass

@app.get("/api/v1/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """获取特定用户"""
    pass

@app.put("/api/v1/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, current_user = Depends(get_current_user)):
    """更新用户信息"""
    pass

@app.delete("/api/v1/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, current_user = Depends(get_current_user)):
    """删除用户"""
    pass

# 文章相关API
@app.post("/api/v1/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, current_user = Depends(get_current_user)):
    """创建新文章"""
    pass

@app.get("/api/v1/posts", response_model=List[PostResponse])
async def get_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[PostStatus] = Query(None),
    category_id: Optional[int] = Query(None),
    author_id: Optional[int] = Query(None),
    search: Optional[str] = Query(None)
):
    """获取文章列表"""
    pass

@app.get("/api/v1/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    """获取特定文章"""
    pass

@app.put("/api/v1/posts/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, post: PostUpdate, current_user = Depends(get_current_user)):
    """更新文章"""
    pass

@app.delete("/api/v1/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, current_user = Depends(get_current_user)):
    """删除文章"""
    pass

# 评论相关API
@app.post("/api/v1/posts/{post_id}/comments", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(post_id: int, comment: CommentCreate, current_user = Depends(get_current_user)):
    """创建评论"""
    pass

@app.get("/api/v1/posts/{post_id}/comments", response_model=List[CommentResponse])
async def get_comments(post_id: int, skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    """获取文章评论"""
    pass

@app.delete("/api/v1/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(comment_id: int, current_user = Depends(get_current_user)):
    """删除评论"""
    pass
```

## 📝 本章小结

### 重点概念
- ✅ REST架构风格的核心原则
- ✅ HTTP方法和状态码的正确使用
- ✅ API设计的最佳实践
- ✅ 版本控制和文档规范
- ✅ 错误处理和响应格式
- ✅ API安全和认证机制

### 关键技能
- ✅ 设计符合REST规范的API
- ✅ 正确使用HTTP方法和状态码
- ✅ 实现API版本控制
- ✅ 编写API文档
- ✅ 处理API错误和异常
- ✅ 实现API安全认证

## 🔗 扩展阅读

- [RESTful API设计指南](https://restfulapi.net/)
- [HTTP状态码详解](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)
- [OpenAPI规范](https://swagger.io/specification/)
- [JWT认证最佳实践](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/)

## ❓ 常见问题

**Q: 什么时候使用POST，什么时候使用PUT？**
A: POST用于创建新资源，PUT用于完整更新资源，PATCH用于部分更新资源。

**Q: 如何设计API版本控制策略？**
A: 可以使用URL路径、Header参数或内容协商等方式，建议使用URL路径方式。

**Q: 如何处理API的向后兼容性？**
A: 保持旧版本API可用，在新版本中添加新功能，逐步废弃旧功能。

**Q: 如何优化API性能？**
A: 使用缓存、分页、压缩、CDN等技术，合理设计数据库查询。

---

**下一章：Vue.js前端开发** → [第7章：Vue.js前端开发](./chapter7_vue_development.md) 