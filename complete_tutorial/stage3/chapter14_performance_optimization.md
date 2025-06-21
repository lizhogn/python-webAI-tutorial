# 第14章：性能优化与高可用

## 📚 学习目标

通过本章学习，你将掌握：
- Web应用常见性能瓶颈分析
- FastAPI性能优化技巧
- 前端性能优化方法
- 数据库优化与索引
- 高可用架构设计

## 🚀 性能瓶颈分析

### 14.1 性能瓶颈来源
- 网络延迟与带宽
- 后端接口响应慢
- 前端渲染卡顿
- 数据库慢查询
- 静态资源加载慢

### 14.2 性能分析工具
- 后端：`uvicorn --reload --reload-dir . --log-level debug`、APM（如SkyWalking、Jaeger）
- 前端：Chrome DevTools、Lighthouse
- 数据库：EXPLAIN、慢查询日志

## 🏎️ FastAPI后端优化

### 14.3 并发与异步
- 使用`async def`提升IO密集型接口性能
- 合理设置`uvicorn`/`gunicorn`进程与线程数

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### 14.4 缓存机制
- 内存缓存（如`functools.lru_cache`、`aiocache`）
- 分布式缓存（如Redis）

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_config():
    # 读取配置
    pass
```

### 14.5 静态资源与CDN
- 前端静态资源使用CDN加速
- Nginx配置静态资源缓存

## ⚡ 前端性能优化

### 14.6 代码分割与懒加载
- Vue/React路由懒加载
- Webpack代码分割

### 14.7 图片与资源优化
- 图片压缩、WebP格式
- 懒加载图片
- SVG图标替代

### 14.8 浏览器缓存
- 设置合理的Cache-Control
- Service Worker离线缓存

## 🗄️ 数据库优化

### 14.9 索引与查询优化
- 为高频查询字段添加索引
- 使用EXPLAIN分析SQL
- 避免N+1查询，合理使用JOIN

### 14.10 分页与批量操作
- 使用`limit/offset`分页
- 批量插入/更新减少数据库压力

## 🏢 高可用架构设计

### 14.11 负载均衡
- Nginx/HAProxy反向代理
- 云负载均衡服务

### 14.12 服务健康检查与自动重启
- Docker Compose `restart: always`
- Kubernetes健康检查（liveness/readiness probe）

### 14.13 灾备与数据备份
- 定期自动备份数据库
- 多地多活、主从复制

## 💻 实践项目

### 项目：全栈应用性能优化实战
- 对API接口、前端页面、数据库进行性能分析与优化
- 配置CDN、缓存、索引、负载均衡

## 📝 本章小结

### 重点概念
- ✅ 性能瓶颈分析与工具
- ✅ FastAPI与前端性能优化
- ✅ 数据库优化与索引
- ✅ 高可用架构设计

### 关键技能
- ✅ 使用缓存与CDN
- ✅ 代码分割与懒加载
- ✅ 数据库索引与慢查询分析
- ✅ 负载均衡与健康检查

## 🔗 扩展阅读
- [FastAPI性能优化](https://fastapi.tiangolo.com/zh/advanced/async/)
- [前端性能优化指南](https://web.dev/fast/)
- [PostgreSQL优化](https://www.postgresql.org/docs/current/performance-tips.html)
- [高可用架构设计](https://juejin.cn/post/6844904106230683655)

## ❓ 常见问题

**Q: 如何定位API慢的原因？**
A: 结合日志、APM、数据库慢查询、前端Network面板多方排查。

**Q: 生产环境如何保证高可用？**
A: 多实例部署、负载均衡、自动重启、定期备份。 