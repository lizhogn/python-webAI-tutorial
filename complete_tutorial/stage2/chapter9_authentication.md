# 第9章：用户认证与权限管理

## 📚 学习目标

通过本章学习，你将掌握：
- 用户注册、登录、登出流程
- Token（JWT）认证机制
- 前端登录态管理
- 权限控制与接口保护
- 常见安全风险与防护

## 👤 用户认证基础

### 9.1 认证与授权区别
- **认证（Authentication）**：确认用户身份（如登录）
- **授权（Authorization）**：判断用户是否有权限访问资源

### 9.2 常见认证方式
- Session/Cookie（传统Web）
- Token（JWT，主流推荐）
- OAuth2（第三方登录）

## 🔑 JWT认证机制

### 9.3 JWT原理
- 用户登录成功后，后端生成JWT Token返回给前端
- 前端存储Token（如localStorage）
- 后续请求在Header中携带Token，后端校验

### 9.4 FastAPI实现JWT认证

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

# 生成Token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 校验Token
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
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="无效的Token")
    return user

# 登录接口
@app.post("/api/v1/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 验证用户名密码
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
```

## 🛡️ 前端登录态管理

### 9.5 登录流程
1. 用户输入用户名密码，前端调用`/api/v1/login`接口
2. 后端返回JWT Token，前端保存到localStorage/sessionStorage
3. 后续API请求在Header中携带`Authorization: Bearer <token>`
4. 退出登录时清除Token

### 9.6 前端实现

```typescript
// 登录
import axios from 'axios'

export async function login(username: string, password: string) {
  const res = await axios.post('/api/v1/login', {
    username,
    password
  })
  localStorage.setItem('token', res.data.access_token)
}

// 请求拦截器自动带Token
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

// 退出登录
export function logout() {
  localStorage.removeItem('token')
}
```

## 🛡️ 权限控制

### 9.7 FastAPI接口保护

```python
from fastapi import Depends

@app.get("/api/v1/users/me")
async def get_me(current_user=Depends(get_current_user)):
    return current_user

@app.get("/api/v1/admin")
async def admin_only(current_user=Depends(get_current_user)):
    if not current_user.get('is_admin'):
        raise HTTPException(status_code=403, detail="无权限")
    return {"msg": "管理员接口"}
```

### 9.8 前端路由守卫

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [/* ... */]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next({ name: 'Login', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})
```

## 🛡️ 常见安全风险与防护

### 9.9 风险与防护措施
- XSS：前端输出内容时注意转义，后端过滤
- CSRF：Token认证天然防CSRF，重要操作可加二次确认
- 信息泄露：错误信息不暴露敏感数据
- Token泄露：Token只存储在安全位置，及时失效

## 💻 实践项目

### 项目：实现注册、登录、登出、权限接口保护
- 前端实现登录表单，调用后端API获取Token
- 登录后访问受保护页面，未登录自动跳转登录页
- 后端接口根据Token校验用户身份和权限

## 📝 本章小结

### 重点概念
- ✅ 用户认证与授权流程
- ✅ JWT认证机制
- ✅ 前端登录态管理
- ✅ 权限控制与接口保护
- ✅ 常见安全风险与防护

### 关键技能
- ✅ 实现注册、登录、登出
- ✅ 使用JWT保护API
- ✅ 前端路由守卫
- ✅ 防范常见Web安全风险

## 🔗 扩展阅读
- [JWT官方文档](https://jwt.io/)
- [FastAPI安全文档](https://fastapi.tiangolo.com/zh/tutorial/security/)
- [Web安全最佳实践](https://developer.mozilla.org/zh-CN/docs/Web/Security)

## ❓ 常见问题

**Q: JWT如何失效？**
A: 设置过期时间，或后端维护黑名单。

**Q: 如何防止Token泄露？**
A: 只在HTTPS下传输，前端不暴露Token，及时清除。 