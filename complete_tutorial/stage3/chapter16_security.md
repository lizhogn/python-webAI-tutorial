# 第16章：安全加固与最佳实践

## 📚 学习目标

通过本章学习，你将掌握：
- Web应用常见安全风险
- FastAPI安全配置与防护
- 前端安全防护措施
- 数据库与云安全
- 安全开发与合规最佳实践

## 🛡️ Web安全基础

### 16.1 常见安全风险
- XSS（跨站脚本攻击）
- CSRF（跨站请求伪造）
- SQL注入
- 认证与会话劫持
- 敏感信息泄露

### 16.2 OWASP Top 10
- 了解Web安全十大风险
- 参考：https://owasp.org/www-project-top-ten/

## 🔒 FastAPI安全加固

### 16.3 HTTPS与证书
- 强制HTTPS，使用Let's Encrypt免费证书
- 配置HSTS响应头

### 16.4 输入校验与防注入
- 使用Pydantic严格校验输入
- ORM参数化查询，禁止字符串拼接SQL

### 16.5 CSRF防护
- API采用Token认证天然防CSRF
- 重要操作可加二次确认

### 16.6 安全响应头
- 配置CORS、Content-Security-Policy、X-Frame-Options等

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 16.7 日志与异常处理
- 统一异常处理，避免敏感信息泄露
- 记录安全相关日志

## 🛡️ 前端安全防护

### 16.8 XSS防护
- 前端输出内容时使用`v-html`需谨慎，优先纯文本渲染
- 使用前端库自动转义

### 16.9 CSRF与Token存储
- Token只存储在`httpOnly` Cookie或内存中，避免localStorage泄露
- 重要操作二次确认

### 16.10 依赖与第三方包安全
- 定期升级依赖，使用`npm audit`、`pip-audit`检查漏洞
- 锁定依赖版本，避免供应链攻击

## 🗄️ 数据库与云安全

### 16.11 数据库安全
- 只开放必要端口，强密码
- 定期备份，敏感数据加密
- 最小权限原则

### 16.12 云安全
- 安全组限制端口访问
- 关闭不必要的服务
- 使用云厂商安全工具（如云防火墙、DDoS防护）

## 📝 安全开发与合规

### 16.13 安全开发流程
- 代码评审关注安全
- 自动化安全测试
- 安全培训与意识提升

### 16.14 合规与隐私保护
- 遵守GDPR、网络安全法等法规
- 明确用户数据收集与用途
- 用户数据可导出、可删除

## 💻 实践项目

### 项目：全栈应用安全加固实战
- 配置HTTPS与安全响应头
- 输入校验与异常处理
- 前端XSS/CSRF防护
- 依赖安全扫描与升级

## 📝 本章小结

### 重点概念
- ✅ Web安全风险与防护
- ✅ FastAPI与前端安全加固
- ✅ 数据库与云安全
- ✅ 安全开发与合规

### 关键技能
- ✅ 配置HTTPS与安全头
- ✅ 输入校验与异常处理
- ✅ 前端XSS/CSRF防护
- ✅ 依赖与云安全管理

## 🔗 扩展阅读
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [FastAPI安全文档](https://fastapi.tiangolo.com/zh/tutorial/security/)
- [前端安全最佳实践](https://developer.mozilla.org/zh-CN/docs/Web/Security)
- [GDPR合规](https://gdpr-info.eu/)

## ❓ 常见问题

**Q: Token存储在哪里最安全？**
A: 推荐httpOnly Cookie，避免XSS窃取。

**Q: 如何防止SQL注入？**
A: ORM参数化查询，绝不拼接SQL字符串。 