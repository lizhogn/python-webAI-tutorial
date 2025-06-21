# 第3章：FastAPI进阶

## 📚 学习目标

通过本章学习，你将掌握：
- FastAPI框架的核心概念和优势
- 异步编程基础
- Pydantic数据验证
- RESTful API设计
- 自动API文档生成
- 中间件和依赖注入

## ⚡ FastAPI简介

### 3.1 什么是FastAPI？

FastAPI是一个现代、快速、基于Python 3.7+的Web框架，用于构建API，具有以下特点：
- **高性能**：与NodeJS和Go相当的性能
- **快速开发**：自动生成API文档
- **类型提示**：基于Python类型提示
- **自动验证**：自动数据验证和序列化
- **现代Python**：支持异步编程

### 3.2 FastAPI vs 其他框架

| 特性 | FastAPI | Flask | Django | Express.js |
|------|---------|-------|--------|------------|
| 性能 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 学习曲线 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| 自动文档 | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐ |
| 类型安全 | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐ |
| 异步支持 | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## 🚀 第一个FastAPI应用

### 3.3 环境准备

```bash
# 创建虚拟环境
python -m venv fastapi_env
source fastapi_env/bin/activate  # Linux/Mac
# 或
fastapi_env\Scripts\activate     # Windows

# 安装FastAPI和服务器
pip install fastapi uvicorn[standard]
```

### 3.4 Hello World应用

创建 `main.py` 文件：

```python
from fastapi import FastAPI
from typing import Optional

# 创建FastAPI应用实例
app = FastAPI(
    title="我的FastAPI应用",
    description="这是一个学习FastAPI的示例应用",
    version="1.0.0"
)

# 根路径
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 带参数的路径
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# 启动应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

运行应用：
```bash
uvicorn main:app --reload
```

访问：
- 应用：http://localhost:8000
- 文档：http://localhost:8000/docs
- 另一种文档：http://localhost:8000/redoc

## 📝 Pydantic数据验证

### 3.5 基本数据模型

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    is_offer: bool = False
    tags: List[str] = []

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    full_name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

# 使用数据模型
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

@app.post("/users/", response_model=User)
async def create_user(user: User):
    return user
```

## 🛣️ 路由和HTTP方法

### 3.6 基本路由

```python
from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional

app = FastAPI()

# GET请求
@app.get("/items/")
async def read_items(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    return {"skip": skip, "limit": limit}

# GET请求 - 单个项目
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., gt=0)):
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

# POST请求
@app.post("/items/")
async def create_item(item: Item):
    return item

# PUT请求
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# DELETE请求
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

## 🔄 异步编程基础

### 3.7 异步函数

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

# 异步函数示例
@app.get("/async-example")
async def async_example():
    # 模拟异步操作
    await asyncio.sleep(1)
    return {"message": "异步操作完成"}

# 并发异步操作
@app.get("/concurrent-fetch")
async def concurrent_fetch():
    # 并发执行多个任务
    tasks = [
        asyncio.sleep(1),
        asyncio.sleep(2),
        asyncio.sleep(3)
    ]
    results = await asyncio.gather(*tasks)
    return {"results": results}
```

## 🔧 依赖注入

### 3.8 基本依赖注入

```python
from fastapi import FastAPI, Depends, HTTPException
from typing import Optional

app = FastAPI()

# 模拟数据库
fake_items_db = {"1": {"name": "Item 1"}, "2": {"name": "Item 2"}}

# 依赖函数
def get_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

# 使用依赖
@app.get("/items/{item_id}")
async def read_item(item: dict = Depends(get_item)):
    return item
```

## 🛡️ 错误处理

### 3.9 异常处理

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

# 自定义异常
class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message

# 异常处理器
@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": exc.message}
    )

# 使用自定义异常
@app.get("/custom-error")
async def custom_error():
    raise CustomException("这是一个自定义错误")

# 使用HTTPException
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > 100:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return {"item_id": item_id}
```

## 💻 实践项目

### 项目：图书管理API

创建一个完整的图书管理API系统。

#### 步骤1：数据模型

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class BookStatus(str, Enum):
    available = "available"
    borrowed = "borrowed"
    reserved = "reserved"

class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., regex=r"^[0-9-]{10,17}$")
    publication_year: int = Field(..., ge=1900, le=2024)
    status: BookStatus = BookStatus.available
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Python编程从入门到实践",
                "author": "张三",
                "isbn": "978-7-111-12345-6",
                "publication_year": 2023,
                "status": "available"
            }
        }

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    publication_year: Optional[int] = None
    status: Optional[BookStatus] = None
```

#### 步骤2：API实现

```python
from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional

app = FastAPI(title="图书管理系统", version="1.0.0")

# 模拟数据库
books_db = {}

# 依赖函数
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="图书不存在")
    return books_db[book_id]

# API端点
@app.post("/books/", response_model=Book, status_code=201)
async def create_book(book: Book):
    book_id = len(books_db) + 1
    book.id = book_id
    books_db[book_id] = book.dict()
    return book

@app.get("/books/", response_model=List[Book])
async def list_books(skip: int = 0, limit: int = 10):
    books = list(books_db.values())
    return books[skip : skip + limit]

@app.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book: Book = Depends(get_book)):
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="图书不存在")
    
    stored_book = books_db[book_id]
    update_data = book_update.dict(exclude_unset=True)
    updated_book = Book(**{**stored_book, **update_data})
    books_db[book_id] = updated_book.dict()
    return updated_book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="图书不存在")
    
    del books_db[book_id]
    return {"message": "图书删除成功"}
```

## 📝 本章小结

### 重点概念
- ✅ FastAPI框架的核心概念和优势
- ✅ 异步编程基础
- ✅ Pydantic数据验证
- ✅ RESTful API设计
- ✅ 自动API文档生成
- ✅ 中间件和依赖注入

### 关键技能
- ✅ 创建和运行FastAPI应用
- ✅ 使用Pydantic进行数据验证
- ✅ 设计RESTful API接口
- ✅ 实现异步操作
- ✅ 使用依赖注入
- ✅ 处理错误和异常
- ✅ 生成API文档

## 🔗 扩展阅读

- [FastAPI官方文档](https://fastapi.tiangolo.com/)
- [Pydantic文档](https://pydantic-docs.helpmanual.io/)
- [异步编程指南](https://docs.python.org/3/library/asyncio.html)
- [RESTful API设计](https://restfulapi.net/)

## ❓ 常见问题

**Q: FastAPI和Flask有什么区别？**
A: FastAPI性能更好，支持异步编程，自动生成API文档，类型安全；Flask更简单，学习曲线平缓。

**Q: 什么时候使用FastAPI？**
A: 适合构建高性能API，需要自动文档，重视类型安全的项目。

**Q: 如何调试FastAPI应用？**
A: 使用 `--reload` 参数，查看自动生成的文档，使用日志记录。

**Q: 如何处理数据库连接？**
A: 使用依赖注入管理数据库连接，结合SQLAlchemy等ORM。

---

**下一章：数据库集成** → [第4章：数据库集成](./chapter4_database.md) 