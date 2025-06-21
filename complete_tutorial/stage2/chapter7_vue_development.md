# 第7章：Vue.js前端开发

## 📚 学习目标

通过本章学习，你将掌握：
- Vue.js 3的核心概念和Composition API
- 组件化开发思想
- 状态管理和数据流
- 路由配置和导航
- 与后端API的通信
- 前端工程化和构建工具

## ⚡ Vue.js 3基础

### 7.1 什么是Vue.js？

Vue.js是一个渐进式JavaScript框架，用于构建用户界面。Vue 3带来了以下改进：

- **Composition API**：更好的逻辑复用和类型推导
- **性能提升**：更小的包体积和更快的渲染速度
- **TypeScript支持**：原生TypeScript支持
- **更好的Tree-shaking**：按需导入，减少包体积

### 7.2 Vue.js vs 其他框架

| 特性 | Vue.js | React | Angular |
|------|--------|-------|---------|
| 学习曲线 | 简单 | 中等 | 复杂 |
| 性能 | 高 | 高 | 中等 |
| 生态系统 | 丰富 | 非常丰富 | 丰富 |
| 类型支持 | 优秀 | 良好 | 优秀 |
| 社区活跃度 | 高 | 很高 | 高 |

## 🚀 第一个Vue应用

### 7.3 环境准备

```bash
# 安装Node.js和npm
# 下载并安装：https://nodejs.org/

# 创建Vue项目
npm create vue@latest my-vue-app

# 选择配置
# ✓ Add TypeScript? Yes
# ✓ Add JSX Support? No
# ✓ Add Vue Router? Yes
# ✓ Add Pinia? Yes
# ✓ Add Vitest? No
# ✓ Add End-to-End Testing? No
# ✓ Add ESLint? Yes
# ✓ Add Prettier? Yes

# 进入项目目录
cd my-vue-app

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 7.4 Hello World应用

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <header>
      <h1>{{ title }}</h1>
    </header>
    
    <main>
      <p>{{ message }}</p>
      <button @click="incrementCount">点击次数: {{ count }}</button>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'

// 响应式数据
const title = ref('Vue.js 3 应用')
const message = ref('欢迎学习Vue.js!')
const count = ref(0)

// 响应式对象
const user = reactive({
  name: '张三',
  age: 25,
  email: 'zhangsan@example.com'
})

// 方法
const incrementCount = () => {
  count.value++
}

// 生命周期钩子
onMounted(() => {
  console.log('组件已挂载')
})
</script>

<style scoped>
#app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

h1 {
  color: #42b883;
  font-size: 2.5em;
}

main {
  text-align: center;
}

button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
}

button:hover {
  background-color: #369870;
}
</style>
```

## 🧩 组件化开发

### 7.5 基本组件

```vue
<!-- components/UserCard.vue -->
<template>
  <div class="user-card">
    <div class="avatar">
      <img :src="user.avatar" :alt="user.name">
    </div>
    <div class="info">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <p>{{ user.bio }}</p>
    </div>
    <div class="actions">
      <button @click="editUser">编辑</button>
      <button @click="deleteUser" class="delete">删除</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

// 定义Props
interface User {
  id: number
  name: string
  email: string
  bio: string
  avatar: string
}

const props = defineProps<{
  user: User
}>()

// 定义事件
const emit = defineEmits<{
  edit: [user: User]
  delete: [userId: number]
}>()

// 方法
const editUser = () => {
  emit('edit', props.user)
}

const deleteUser = () => {
  emit('delete', props.user.id)
}
</script>

<style scoped>
.user-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 20px;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.avatar img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
}

.info {
  flex: 1;
}

.info h3 {
  margin: 0 0 5px 0;
  color: #333;
}

.info p {
  margin: 5px 0;
  color: #666;
}

.actions {
  display: flex;
  gap: 10px;
}

.actions button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.actions button:first-child {
  background-color: #42b883;
  color: white;
}

.actions button.delete {
  background-color: #ff4757;
  color: white;
}

.actions button:hover {
  opacity: 0.8;
}
</style>
```

### 7.6 使用组件

```vue
<!-- views/UserList.vue -->
<template>
  <div class="user-list">
    <h2>用户列表</h2>
    
    <div class="search-bar">
      <input 
        v-model="searchQuery" 
        @input="filterUsers"
        placeholder="搜索用户..."
        type="text"
      >
    </div>
    
    <div class="users">
      <UserCard
        v-for="user in filteredUsers"
        :key="user.id"
        :user="user"
        @edit="handleEdit"
        @delete="handleDelete"
      />
    </div>
    
    <div v-if="filteredUsers.length === 0" class="no-results">
      没有找到匹配的用户
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import UserCard from '@/components/UserCard.vue'

// 响应式数据
const users = ref<User[]>([])
const searchQuery = ref('')
const loading = ref(false)

// 计算属性
const filteredUsers = computed(() => {
  if (!searchQuery.value) {
    return users.value
  }
  
  return users.value.filter(user => 
    user.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    user.email.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

// 方法
const fetchUsers = async () => {
  loading.value = true
  try {
    const response = await fetch('/api/users')
    const data = await response.json()
    users.value = data
  } catch (error) {
    console.error('获取用户列表失败:', error)
  } finally {
    loading.value = false
  }
}

const filterUsers = () => {
  // 搜索逻辑已在computed中处理
}

const handleEdit = (user: User) => {
  console.log('编辑用户:', user)
  // 跳转到编辑页面或打开编辑模态框
}

const handleDelete = async (userId: number) => {
  if (confirm('确定要删除这个用户吗？')) {
    try {
      await fetch(`/api/users/${userId}`, {
        method: 'DELETE'
      })
      // 从列表中移除用户
      users.value = users.value.filter(user => user.id !== userId)
    } catch (error) {
      console.error('删除用户失败:', error)
    }
  }
}

// 生命周期
onMounted(() => {
  fetchUsers()
})
</script>

<style scoped>
.user-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.search-bar {
  margin-bottom: 20px;
}

.search-bar input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
}

.search-bar input:focus {
  outline: none;
  border-color: #42b883;
}

.no-results {
  text-align: center;
  color: #666;
  padding: 40px;
  font-size: 18px;
}
</style>
```

## 🔄 状态管理

### 7.7 Pinia状态管理

```typescript
// stores/user.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export interface User {
  id: number
  name: string
  email: string
  bio: string
  avatar: string
}

export const useUserStore = defineStore('user', () => {
  // 状态
  const users = ref<User[]>([])
  const currentUser = ref<User | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  // 计算属性
  const userCount = computed(() => users.value.length)
  const activeUsers = computed(() => users.value.filter(user => user.isActive))

  // 方法
  const fetchUsers = async () => {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch('/api/users')
      if (!response.ok) {
        throw new Error('获取用户列表失败')
      }
      const data = await response.json()
      users.value = data
    } catch (err) {
      error.value = err instanceof Error ? err.message : '未知错误'
    } finally {
      loading.value = false
    }
  }

  const addUser = async (userData: Omit<User, 'id'>) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      })
      
      if (!response.ok) {
        throw new Error('创建用户失败')
      }
      
      const newUser = await response.json()
      users.value.push(newUser)
      return newUser
    } catch (err) {
      error.value = err instanceof Error ? err.message : '未知错误'
      throw err
    } finally {
      loading.value = false
    }
  }

  const updateUser = async (userId: number, userData: Partial<User>) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch(`/api/users/${userId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      })
      
      if (!response.ok) {
        throw new Error('更新用户失败')
      }
      
      const updatedUser = await response.json()
      const index = users.value.findIndex(user => user.id === userId)
      if (index !== -1) {
        users.value[index] = updatedUser
      }
      return updatedUser
    } catch (err) {
      error.value = err instanceof Error ? err.message : '未知错误'
      throw err
    } finally {
      loading.value = false
    }
  }

  const deleteUser = async (userId: number) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch(`/api/users/${userId}`, {
        method: 'DELETE'
      })
      
      if (!response.ok) {
        throw new Error('删除用户失败')
      }
      
      users.value = users.value.filter(user => user.id !== userId)
    } catch (err) {
      error.value = err instanceof Error ? err.message : '未知错误'
      throw err
    } finally {
      loading.value = false
    }
  }

  const setCurrentUser = (user: User | null) => {
    currentUser.value = user
  }

  return {
    // 状态
    users,
    currentUser,
    loading,
    error,
    
    // 计算属性
    userCount,
    activeUsers,
    
    // 方法
    fetchUsers,
    addUser,
    updateUser,
    deleteUser,
    setCurrentUser
  }
})
```

### 7.8 在组件中使用Store

```vue
<!-- views/UserManagement.vue -->
<template>
  <div class="user-management">
    <div class="header">
      <h2>用户管理</h2>
      <button @click="showAddModal = true" class="add-btn">
        添加用户
      </button>
    </div>

    <!-- 加载状态 -->
    <div v-if="userStore.loading" class="loading">
      加载中...
    </div>

    <!-- 错误信息 -->
    <div v-if="userStore.error" class="error">
      {{ userStore.error }}
    </div>

    <!-- 用户列表 -->
    <div v-else class="user-grid">
      <UserCard
        v-for="user in userStore.users"
        :key="user.id"
        :user="user"
        @edit="handleEdit"
        @delete="handleDelete"
      />
    </div>

    <!-- 统计信息 -->
    <div class="stats">
      <p>总用户数: {{ userStore.userCount }}</p>
      <p>活跃用户: {{ userStore.activeUsers.length }}</p>
    </div>

    <!-- 添加用户模态框 -->
    <UserModal
      v-if="showAddModal"
      :user="editingUser"
      @close="closeModal"
      @save="handleSave"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import UserCard from '@/components/UserCard.vue'
import UserModal from '@/components/UserModal.vue'
import type { User } from '@/stores/user'

const userStore = useUserStore()
const showAddModal = ref(false)
const editingUser = ref<User | null>(null)

// 方法
const handleEdit = (user: User) => {
  editingUser.value = user
  showAddModal.value = true
}

const handleDelete = async (userId: number) => {
  if (confirm('确定要删除这个用户吗？')) {
    try {
      await userStore.deleteUser(userId)
    } catch (error) {
      console.error('删除用户失败:', error)
    }
  }
}

const closeModal = () => {
  showAddModal.value = false
  editingUser.value = null
}

const handleSave = async (userData: Partial<User>) => {
  try {
    if (editingUser.value) {
      await userStore.updateUser(editingUser.value.id, userData)
    } else {
      await userStore.addUser(userData as Omit<User, 'id'>)
    }
    closeModal()
  } catch (error) {
    console.error('保存用户失败:', error)
  }
}

// 生命周期
onMounted(() => {
  userStore.fetchUsers()
})
</script>

<style scoped>
.user-management {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.add-btn {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
}

.add-btn:hover {
  background-color: #369870;
}

.loading {
  text-align: center;
  padding: 40px;
  font-size: 18px;
  color: #666;
}

.error {
  background-color: #ff4757;
  color: white;
  padding: 15px;
  border-radius: 6px;
  margin-bottom: 20px;
}

.user-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stats {
  display: flex;
  gap: 20px;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 6px;
}

.stats p {
  margin: 0;
  font-weight: bold;
  color: #333;
}
</style>
```

## 🛣️ 路由配置

### 7.9 Vue Router配置

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    meta: { title: '首页' }
  },
  {
    path: '/users',
    name: 'UserList',
    component: () => import('@/views/UserList.vue'),
    meta: { title: '用户列表', requiresAuth: true }
  },
  {
    path: '/users/:id',
    name: 'UserDetail',
    component: () => import('@/views/UserDetail.vue'),
    meta: { title: '用户详情', requiresAuth: true },
    props: true
  },
  {
    path: '/users/new',
    name: 'UserCreate',
    component: () => import('@/views/UserCreate.vue'),
    meta: { title: '创建用户', requiresAuth: true }
  },
  {
    path: '/users/:id/edit',
    name: 'UserEdit',
    component: () => import('@/views/UserEdit.vue'),
    meta: { title: '编辑用户', requiresAuth: true },
    props: true
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { title: '登录' }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/Register.vue'),
    meta: { title: '注册' }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/views/Profile.vue'),
    meta: { title: '个人资料', requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue'),
    meta: { title: '页面未找到' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 设置页面标题
  document.title = to.meta.title ? `${to.meta.title} - 我的应用` : '我的应用'
  
  // 检查是否需要认证
  if (to.meta.requiresAuth) {
    const userStore = useUserStore()
    if (!userStore.currentUser) {
      next({ name: 'Login', query: { redirect: to.fullPath } })
      return
    }
  }
  
  next()
})

export default router
```

### 7.10 导航组件

```vue
<!-- components/Navigation.vue -->
<template>
  <nav class="navigation">
    <div class="nav-container">
      <router-link to="/" class="logo">
        <h1>我的应用</h1>
      </router-link>
      
      <div class="nav-links">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/users" class="nav-link">用户管理</router-link>
        <router-link to="/posts" class="nav-link">文章管理</router-link>
      </div>
      
      <div class="nav-user">
        <template v-if="userStore.currentUser">
          <div class="user-info">
            <img :src="userStore.currentUser.avatar" :alt="userStore.currentUser.name" class="avatar">
            <span class="username">{{ userStore.currentUser.name }}</span>
          </div>
          <div class="user-menu">
            <router-link to="/profile" class="menu-item">个人资料</router-link>
            <button @click="logout" class="menu-item logout">退出登录</button>
          </div>
        </template>
        <template v-else>
          <router-link to="/login" class="nav-link">登录</router-link>
          <router-link to="/register" class="nav-link">注册</router-link>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const logout = () => {
  userStore.setCurrentUser(null)
  router.push('/login')
}
</script>

<style scoped>
.navigation {
  background-color: #fff;
  border-bottom: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
}

.logo {
  text-decoration: none;
  color: #333;
}

.logo h1 {
  margin: 0;
  font-size: 24px;
  color: #42b883;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-link {
  text-decoration: none;
  color: #333;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover,
.nav-link.router-link-active {
  background-color: #f0f0f0;
  color: #42b883;
}

.nav-user {
  display: flex;
  align-items: center;
  gap: 15px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.username {
  font-weight: 500;
  color: #333;
}

.user-menu {
  position: relative;
  display: inline-block;
}

.menu-item {
  display: block;
  padding: 8px 16px;
  text-decoration: none;
  color: #333;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 14px;
  text-align: left;
  width: 100%;
}

.menu-item:hover {
  background-color: #f0f0f0;
}

.menu-item.logout {
  color: #ff4757;
}

.menu-item.logout:hover {
  background-color: #ffe6e6;
}
</style>
```

## 🌐 API通信

### 7.11 API服务层

```typescript
// services/api.ts
import { useUserStore } from '@/stores/user'

// API基础配置
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

// 请求拦截器
const createRequest = async (url: string, options: RequestInit = {}) => {
  const userStore = useUserStore()
  
  const config: RequestInit = {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers
    },
    ...options
  }
  
  // 添加认证Token
  if (userStore.currentUser?.token) {
    config.headers = {
      ...config.headers,
      'Authorization': `Bearer ${userStore.currentUser.token}`
    }
  }
  
  const response = await fetch(`${API_BASE_URL}${url}`, config)
  
  if (!response.ok) {
    if (response.status === 401) {
      // Token过期，清除用户信息
      userStore.setCurrentUser(null)
      window.location.href = '/login'
    }
    throw new Error(`HTTP error! status: ${response.status}`)
  }
  
  return response
}

// API服务类
export class ApiService {
  // 用户相关API
  static async getUsers(params?: { page?: number; limit?: number; search?: string }) {
    const queryParams = new URLSearchParams()
    if (params?.page) queryParams.append('page', params.page.toString())
    if (params?.limit) queryParams.append('limit', params.limit.toString())
    if (params?.search) queryParams.append('search', params.search)
    
    const response = await createRequest(`/api/v1/users?${queryParams}`)
    return response.json()
  }
  
  static async getUser(id: number) {
    const response = await createRequest(`/api/v1/users/${id}`)
    return response.json()
  }
  
  static async createUser(userData: any) {
    const response = await createRequest('/api/v1/users', {
      method: 'POST',
      body: JSON.stringify(userData)
    })
    return response.json()
  }
  
  static async updateUser(id: number, userData: any) {
    const response = await createRequest(`/api/v1/users/${id}`, {
      method: 'PUT',
      body: JSON.stringify(userData)
    })
    return response.json()
  }
  
  static async deleteUser(id: number) {
    await createRequest(`/api/v1/users/${id}`, {
      method: 'DELETE'
    })
  }
  
  // 认证相关API
  static async login(credentials: { username: string; password: string }) {
    const response = await createRequest('/api/v1/login', {
      method: 'POST',
      body: JSON.stringify(credentials)
    })
    return response.json()
  }
  
  static async register(userData: any) {
    const response = await createRequest('/api/v1/register', {
      method: 'POST',
      body: JSON.stringify(userData)
    })
    return response.json()
  }
  
  static async getProfile() {
    const response = await createRequest('/api/v1/users/me')
    return response.json()
  }
  
  // 文章相关API
  static async getPosts(params?: { page?: number; limit?: number; category?: string }) {
    const queryParams = new URLSearchParams()
    if (params?.page) queryParams.append('page', params.page.toString())
    if (params?.limit) queryParams.append('limit', params.limit.toString())
    if (params?.category) queryParams.append('category', params.category)
    
    const response = await createRequest(`/api/v1/posts?${queryParams}`)
    return response.json()
  }
  
  static async getPost(id: number) {
    const response = await createRequest(`/api/v1/posts/${id}`)
    return response.json()
  }
  
  static async createPost(postData: any) {
    const response = await createRequest('/api/v1/posts', {
      method: 'POST',
      body: JSON.stringify(postData)
    })
    return response.json()
  }
  
  static async updatePost(id: number, postData: any) {
    const response = await createRequest(`/api/v1/posts/${id}`, {
      method: 'PUT',
      body: JSON.stringify(postData)
    })
    return response.json()
  }
  
  static async deletePost(id: number) {
    await createRequest(`/api/v1/posts/${id}`, {
      method: 'DELETE'
    })
  }
}
```

### 7.12 在组件中使用API

```vue
<!-- views/UserDetail.vue -->
<template>
  <div class="user-detail">
    <div v-if="loading" class="loading">
      加载中...
    </div>
    
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    
    <div v-else-if="user" class="user-content">
      <div class="user-header">
        <img :src="user.avatar" :alt="user.name" class="user-avatar">
        <div class="user-info">
          <h1>{{ user.name }}</h1>
          <p class="email">{{ user.email }}</p>
          <p class="bio">{{ user.bio }}</p>
        </div>
        <div class="user-actions">
          <router-link :to="`/users/${user.id}/edit`" class="edit-btn">
            编辑
          </router-link>
          <button @click="handleDelete" class="delete-btn">
            删除
          </button>
        </div>
      </div>
      
      <div class="user-stats">
        <div class="stat">
          <h3>文章数量</h3>
          <p>{{ user.posts?.length || 0 }}</p>
        </div>
        <div class="stat">
          <h3>注册时间</h3>
          <p>{{ formatDate(user.created_at) }}</p>
        </div>
      </div>
      
      <div v-if="user.posts?.length" class="user-posts">
        <h2>用户文章</h2>
        <div class="posts-grid">
          <div v-for="post in user.posts" :key="post.id" class="post-card">
            <h3>{{ post.title }}</h3>
            <p>{{ post.excerpt }}</p>
            <span class="post-date">{{ formatDate(post.created_at) }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ApiService } from '@/services/api'

const route = useRoute()
const router = useRouter()

const user = ref(null)
const loading = ref(true)
const error = ref('')

// 方法
const fetchUser = async () => {
  try {
    loading.value = true
    error.value = ''
    const userId = parseInt(route.params.id as string)
    const userData = await ApiService.getUser(userId)
    user.value = userData
  } catch (err) {
    error.value = '获取用户信息失败'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const handleDelete = async () => {
  if (confirm('确定要删除这个用户吗？')) {
    try {
      const userId = parseInt(route.params.id as string)
      await ApiService.deleteUser(userId)
      router.push('/users')
    } catch (err) {
      error.value = '删除用户失败'
      console.error(err)
    }
  }
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('zh-CN')
}

// 生命周期
onMounted(() => {
  fetchUser()
})
</script>

<style scoped>
.user-detail {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.loading, .error {
  text-align: center;
  padding: 40px;
  font-size: 18px;
}

.error {
  color: #ff4757;
}

.user-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.user-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.user-info {
  flex: 1;
}

.user-info h1 {
  margin: 0 0 10px 0;
  color: #333;
}

.email {
  color: #666;
  margin: 5px 0;
}

.bio {
  color: #888;
  margin: 10px 0 0 0;
}

.user-actions {
  display: flex;
  gap: 10px;
}

.edit-btn, .delete-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
  font-size: 14px;
}

.edit-btn {
  background-color: #42b883;
  color: white;
}

.delete-btn {
  background-color: #ff4757;
  color: white;
}

.user-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stat h3 {
  margin: 0 0 10px 0;
  color: #666;
  font-size: 14px;
}

.stat p {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  color: #42b883;
}

.user-posts {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.user-posts h2 {
  margin: 0 0 20px 0;
  color: #333;
}

.posts-grid {
  display: grid;
  gap: 15px;
}

.post-card {
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 6px;
}

.post-card h3 {
  margin: 0 0 10px 0;
  color: #333;
}

.post-card p {
  margin: 0 0 10px 0;
  color: #666;
}

.post-date {
  font-size: 12px;
  color: #999;
}
</style>
```

## 📝 本章小结

### 重点概念
- ✅ Vue.js 3的核心概念和Composition API
- ✅ 组件化开发思想
- ✅ 状态管理和数据流
- ✅ 路由配置和导航
- ✅ 与后端API的通信
- ✅ 前端工程化和构建工具

### 关键技能
- ✅ 创建Vue.js 3应用
- ✅ 使用Composition API
- ✅ 组件化开发
- ✅ 状态管理(Pinia)
- ✅ 路由配置(Vue Router)
- ✅ API通信和错误处理

## 🔗 扩展阅读

- [Vue.js官方文档](https://vuejs.org/)
- [Vue Router文档](https://router.vuejs.org/)
- [Pinia状态管理](https://pinia.vuejs.org/)
- [Vue.js最佳实践](https://vuejs.org/guide/best-practices/)

## ❓ 常见问题

**Q: Vue 2和Vue 3有什么区别？**
A: Vue 3引入了Composition API、更好的TypeScript支持、更小的包体积和更好的性能。

**Q: 什么时候使用Vuex，什么时候使用Pinia？**
A: Pinia是Vue 3的官方推荐状态管理库，比Vuex更简单、类型安全更好。

**Q: 如何优化Vue应用性能？**
A: 使用v-memo、shallowRef、组件懒加载、虚拟滚动等技术。

**Q: 如何处理Vue应用中的错误？**
A: 使用错误边界、全局错误处理器、API错误处理等方式。

---

**下一章：前后端通信** → [第8章：前后端通信](./chapter8_frontend_backend_communication.md) 