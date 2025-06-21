# 第11章：异步处理与任务队列

## 📚 学习目标

通过本章学习，你将掌握：
- Python异步编程基础（async/await）
- FastAPI中的异步视图与性能提升
- 后台任务（BackgroundTask）用法
- Celery任务队列与分布式任务调度
- 实践：异步AI推理、邮件发送等场景

## ⚡ Python异步编程基础

### 11.1 async/await语法

```python
import asyncio

async def main():
    print('开始')
    await asyncio.sleep(1)
    print('结束')

asyncio.run(main())
```

### 11.2 FastAPI异步视图

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get('/async-demo')
async def async_demo():
    await asyncio.sleep(2)
    return {'msg': '异步响应'}
```

## 🔄 后台任务与定时任务

### 11.3 FastAPI后台任务

```python
from fastapi import BackgroundTasks

@app.post('/send-email')
async def send_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_func, email)
    return {'msg': '邮件发送中'}

def send_email_func(email):
    # 实际发送邮件逻辑
    pass
```

### 11.4 定时任务（APScheduler）

```python
from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler()

def job():
    print('定时任务执行')

scheduler.add_job(job, 'interval', seconds=10)
scheduler.start()

# FastAPI启动时集成
@app.on_event('startup')
def start_scheduler():
    scheduler.start()
```

## 🛠️ Celery任务队列

### 11.5 Celery基本用法

```python
# tasks.py
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def add(x, y):
    return x + y
```

```python
# 调用任务
from tasks import add
add.delay(2, 3)  # 异步执行
```

### 11.6 FastAPI集成Celery

```python
from fastapi import FastAPI
from tasks import add

app = FastAPI()

@app.post('/add')
async def add_task(x: int, y: int):
    task = add.delay(x, y)
    return {'task_id': task.id}
```

### 11.7 任务状态查询

```python
from celery.result import AsyncResult

@app.get('/task-status/{task_id}')
async def get_status(task_id: str):
    result = AsyncResult(task_id)
    return {'status': result.status, 'result': result.result}
```

## 💻 实践项目

### 项目：异步AI推理与邮件通知
- 用户上传数据，后台异步调用AI模型推理
- 推理完成后通过邮件通知用户
- 使用Celery+Redis实现任务队列

## 📝 本章小结

### 重点概念
- ✅ Python异步编程与async/await
- ✅ FastAPI异步视图与后台任务
- ✅ Celery任务队列与分布式任务
- ✅ 实践异步AI推理与通知

### 关键技能
- ✅ 编写异步API接口
- ✅ 使用Celery实现任务分发
- ✅ 查询任务状态与结果

## 🔗 扩展阅读
- [FastAPI异步文档](https://fastapi.tiangolo.com/zh/async/)
- [Celery官方文档](https://docs.celeryq.dev/)
- [APScheduler文档](https://apscheduler.readthedocs.io/zh/latest/)

## ❓ 常见问题

**Q: FastAPI异步接口和同步接口能混用吗？**
A: 可以，推荐IO密集型用异步，CPU密集型用同步或任务队列。

**Q: Celery和FastAPI如何通信？**
A: 通过消息中间件（如Redis、RabbitMQ）异步分发任务，API查询任务状态。 