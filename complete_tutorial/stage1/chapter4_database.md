# 第4章：数据库集成

## 📚 学习目标

通过本章学习，你将掌握：
- SQLAlchemy ORM的基本概念
- 数据库模型设计和关系
- 数据库迁移和版本控制
- CRUD操作实现
- 数据库查询优化
- 连接池和事务管理

## 🗄️ 数据库基础

### 4.1 为什么需要数据库？

在Web应用中，数据库用于：
- **持久化存储**：数据不会因为应用重启而丢失
- **数据管理**：提供结构化的数据存储和查询
- **并发控制**：多个用户同时访问数据
- **数据完整性**：确保数据的准确性和一致性

### 4.2 数据库类型选择

| 数据库类型 | 特点 | 适用场景 |
|------------|------|----------|
| SQLite | 轻量级，文件型 | 开发测试，小型应用 |
| PostgreSQL | 功能强大，开源 | 生产环境，复杂查询 |
| MySQL | 流行，易用 | 中小型应用 |
| MongoDB | 文档型，灵活 | 非结构化数据 |

## 🔧 SQLAlchemy ORM

### 4.3 什么是ORM？

ORM (Object-Relational Mapping) 将数据库表映射为Python对象，让我们可以用面向对象的方式操作数据库。

### 4.4 安装和配置

```bash
# 安装SQLAlchemy
pip install sqlalchemy psycopg2-binary alembic

# 对于开发环境，也可以使用SQLite
pip install sqlalchemy
```

### 4.5 基本配置

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 创建数据库引擎
# PostgreSQL
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# SQLite (开发环境)
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()

# 依赖函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## 📊 数据模型设计

### 4.6 基本模型

```python
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float
from sqlalchemy.sql import func
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    author_id = Column(Integer, nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
```

### 4.7 模型关系

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    
    # 一对多关系：一个用户可以有多个文章
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    # 多对一关系：每篇文章属于一个作者
    author = relationship("User", back_populates="posts")
    
    # 多对多关系：文章可以有多个标签
    tags = relationship("Tag", secondary="post_tags", back_populates="posts")

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    
    # 多对多关系：标签可以属于多篇文章
    posts = relationship("Post", secondary="post_tags", back_populates="tags")

# 中间表
class PostTag(Base):
    __tablename__ = "post_tags"
    
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
```

## 🚀 数据库迁移

### 4.8 Alembic配置

```bash
# 初始化Alembic
alembic init alembic
```

配置 `alembic.ini`：
```ini
[alembic]
script_location = alembic
sqlalchemy.url = postgresql://username:password@localhost/dbname
```

配置 `alembic/env.py`：
```python
from models import Base
target_metadata = Base.metadata
```

### 4.9 创建迁移

```bash
# 创建初始迁移
alembic revision --autogenerate -m "Initial migration"

# 应用迁移
alembic upgrade head

# 查看迁移历史
alembic history

# 回滚迁移
alembic downgrade -1
```

## 🔄 CRUD操作

### 4.10 创建操作 (Create)

```python
from sqlalchemy.orm import Session
from models import User, Post

def create_user(db: Session, username: str, email: str, hashed_password: str):
    db_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_post(db: Session, title: str, content: str, author_id: int):
    db_post = Post(
        title=title,
        content=content,
        author_id=author_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
```

### 4.11 读取操作 (Read)

```python
from sqlalchemy.orm import Session
from models import User, Post

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()

def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.author_id == user_id).all()
```

### 4.12 更新操作 (Update)

```python
from sqlalchemy.orm import Session
from models import User, Post

def update_user(db: Session, user_id: int, **kwargs):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in kwargs.items():
            if hasattr(db_user, key):
                setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def update_post(db: Session, post_id: int, **kwargs):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        for key, value in kwargs.items():
            if hasattr(db_post, key):
                setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post
```

### 4.13 删除操作 (Delete)

```python
from sqlalchemy.orm import Session
from models import User, Post

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False
```

## 🔍 查询优化

### 4.14 基本查询

```python
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, not_

# 条件查询
def get_active_users(db: Session):
    return db.query(User).filter(User.is_active == True).all()

# 复合条件查询
def search_posts(db: Session, keyword: str, author_id: int = None):
    query = db.query(Post).filter(
        or_(
            Post.title.contains(keyword),
            Post.content.contains(keyword)
        )
    )
    if author_id:
        query = query.filter(Post.author_id == author_id)
    return query.all()

# 排序查询
def get_latest_posts(db: Session, limit: int = 10):
    return db.query(Post).order_by(Post.created_at.desc()).limit(limit).all()

# 分组查询
from sqlalchemy import func
def get_post_count_by_author(db: Session):
    return db.query(
        Post.author_id,
        func.count(Post.id).label('post_count')
    ).group_by(Post.author_id).all()
```

### 4.15 关联查询

```python
from sqlalchemy.orm import Session, joinedload

# 预加载关联数据
def get_posts_with_author(db: Session):
    return db.query(Post).options(joinedload(Post.author)).all()

# 子查询
def get_users_with_post_count(db: Session):
    from sqlalchemy import func
    return db.query(
        User,
        func.count(Post.id).label('post_count')
    ).outerjoin(Post).group_by(User.id).all()
```

## 🔒 事务管理

### 4.16 基本事务

```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def create_user_with_posts(db: Session, user_data: dict, posts_data: list):
    try:
        # 创建用户
        db_user = User(**user_data)
        db.add(db_user)
        db.flush()  # 获取用户ID
        
        # 创建文章
        for post_data in posts_data:
            post_data['author_id'] = db_user.id
            db_post = Post(**post_data)
            db.add(db_post)
        
        db.commit()
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e
```

### 4.17 上下文管理器

```python
from contextlib import contextmanager
from sqlalchemy.orm import Session

@contextmanager
def get_db_transaction():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

# 使用示例
def create_user_safe(user_data: dict):
    with get_db_transaction() as db:
        db_user = User(**user_data)
        db.add(db_user)
        return db_user
```

## 💻 实践项目

### 项目：博客系统数据库

创建一个完整的博客系统数据库。

#### 步骤1：数据模型

```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from datetime import datetime

DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    bio = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=func.now())
    
    posts = relationship("Post", back_populates="category")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    excerpt = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    is_published = Column(Boolean, default=False)
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    author = relationship("User", back_populates="posts")
    category = relationship("Category", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    tags = relationship("Tag", secondary="post_tags", back_populates="posts")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey("comments.id"))
    is_approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    
    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    posts = relationship("Post", secondary="post_tags", back_populates="tags")

class PostTag(Base):
    __tablename__ = "post_tags"
    
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
```

#### 步骤2：CRUD操作

```python
# crud.py
from sqlalchemy.orm import Session
from models import User, Post, Category, Comment, Tag
from typing import List, Optional

class UserCRUD:
    @staticmethod
    def create_user(db: Session, username: str, email: str, hashed_password: str, full_name: str = None):
        db_user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            full_name=full_name
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

class PostCRUD:
    @staticmethod
    def create_post(db: Session, title: str, content: str, author_id: int, category_id: int = None):
        db_post = Post(
            title=title,
            content=content,
            author_id=author_id,
            category_id=category_id
        )
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post
    
    @staticmethod
    def get_post(db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()
    
    @staticmethod
    def get_published_posts(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Post).filter(Post.is_published == True).order_by(Post.created_at.desc()).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_posts_by_author(db: Session, author_id: int):
        return db.query(Post).filter(Post.author_id == author_id).all()
    
    @staticmethod
    def update_post(db: Session, post_id: int, **kwargs):
        db_post = db.query(Post).filter(Post.id == post_id).first()
        if db_post:
            for key, value in kwargs.items():
                if hasattr(db_post, key):
                    setattr(db_post, key, value)
            db.commit()
            db.refresh(db_post)
        return db_post
    
    @staticmethod
    def delete_post(db: Session, post_id: int):
        db_post = db.query(Post).filter(Post.id == post_id).first()
        if db_post:
            db.delete(db_post)
            db.commit()
            return True
        return False
```

#### 步骤3：数据库初始化

```python
# init_db.py
from sqlalchemy.orm import Session
from models import Base, engine, User, Category, Tag
from crud import UserCRUD, PostCRUD

def init_db():
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    # 创建会话
    db = Session(engine)
    
    try:
        # 创建示例数据
        # 创建用户
        user1 = UserCRUD.create_user(
            db=db,
            username="admin",
            email="admin@example.com",
            hashed_password="hashed_password_here",
            full_name="管理员"
        )
        
        # 创建分类
        categories = [
            Category(name="技术", description="技术相关文章"),
            Category(name="生活", description="生活感悟"),
            Category(name="教程", description="学习教程")
        ]
        
        for category in categories:
            db.add(category)
        
        # 创建标签
        tags = [
            Tag(name="Python"),
            Tag(name="Web开发"),
            Tag(name="数据库"),
            Tag(name="FastAPI")
        ]
        
        for tag in tags:
            db.add(tag)
        
        db.commit()
        print("数据库初始化完成！")
        
    except Exception as e:
        db.rollback()
        print(f"数据库初始化失败: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
```

## 📝 本章小结

### 重点概念
- ✅ SQLAlchemy ORM的基本概念
- ✅ 数据库模型设计和关系
- ✅ 数据库迁移和版本控制
- ✅ CRUD操作实现
- ✅ 数据库查询优化
- ✅ 连接池和事务管理

### 关键技能
- ✅ 配置SQLAlchemy数据库连接
- ✅ 设计数据库模型和关系
- ✅ 使用Alembic进行数据库迁移
- ✅ 实现完整的CRUD操作
- ✅ 优化数据库查询性能
- ✅ 管理数据库事务

## 🔗 扩展阅读

- [SQLAlchemy官方文档](https://docs.sqlalchemy.org/)
- [Alembic迁移指南](https://alembic.sqlalchemy.org/)
- [PostgreSQL文档](https://www.postgresql.org/docs/)
- [数据库设计最佳实践](https://www.postgresql.org/docs/current/ddl.html)

## ❓ 常见问题

**Q: 什么时候使用SQLite，什么时候使用PostgreSQL？**
A: SQLite适合开发测试和小型应用，PostgreSQL适合生产环境和复杂查询。

**Q: 如何优化数据库查询性能？**
A: 使用索引、避免N+1查询、合理使用JOIN、分页查询等。

**Q: 如何处理数据库连接池？**
A: 配置合适的连接池大小，及时释放连接，使用连接池管理器。

**Q: 如何备份和恢复数据库？**
A: 使用数据库自带的备份工具，定期备份，测试恢复流程。

---

**下一章：前端基础** → [第5章：前端基础](./chapter5_frontend_basics.md) 