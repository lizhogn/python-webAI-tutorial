# 第13章：生产环境与持续集成

## 📚 学习目标

通过本章学习，你将掌握：
- 生产环境部署注意事项
- Nginx反向代理与HTTPS配置
- 日志与监控方案
- 持续集成/持续部署（CI/CD）流程
- 自动化测试与质量保障

## 🚀 生产环境部署

### 13.1 生产环境与开发环境区别
- 配置分离（环境变量）
- 日志与监控
- 安全加固
- 自动化运维

### 13.2 Nginx反向代理

```nginx
server {
    listen 80;
    server_name example.com;

    location /api/ {
        proxy_pass http://127.0.0.1:8000/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location / {
        proxy_pass http://127.0.0.1:80/;
    }
}
```

### 13.3 HTTPS配置（Let's Encrypt）

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com
```

## 📊 日志与监控

### 13.4 日志收集
- 后端：uvicorn/gunicorn日志、应用日志
- 前端：Nginx访问日志、前端异常上报
- 日志集中：ELK/EFK、云日志服务

### 13.5 监控方案
- 进程监控：supervisor、systemd
- 性能监控：Prometheus + Grafana
- 报警通知：邮件、钉钉、企业微信

## 🔄 持续集成/持续部署（CI/CD）

### 13.6 CI/CD流程
1. 代码提交到Git仓库（GitHub/GitLab）
2. 自动化测试（pytest、jest等）
3. 构建镜像并推送到仓库
4. 自动部署到服务器

### 13.7 GitHub Actions示例

```yaml
# .github/workflows/deploy.yml
name: CI/CD
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r backend/requirements.txt
      - name: Run backend tests
        run: |
          cd backend && pytest
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install frontend dependencies
        run: |
          cd frontend && npm install
      - name: Run frontend tests
        run: |
          cd frontend && npm run test
      - name: Build Docker images
        run: |
          docker-compose build
      - name: Deploy to server
        env:
          SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
        run: |
          # 通过SSH部署到服务器
          echo "$SSH_PRIVATE_KEY" > key.pem
          chmod 600 key.pem
          scp -i key.pem docker-compose.yml user@server:/path/
          ssh -i key.pem user@server 'cd /path && docker-compose up -d'
```

## 🧪 自动化测试

### 13.8 后端测试（pytest）

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

### 13.9 前端测试（Jest）

```javascript
// tests/App.spec.js
import { mount } from '@vue/test-utils'
import App from '@/App.vue'

describe('App.vue', () => {
  it('renders title', () => {
    const wrapper = mount(App)
    expect(wrapper.text()).toContain('Vue.js 3 应用')
  })
})
```

## 💻 实践项目

### 项目：全流程CI/CD部署
- 配置Nginx反向代理与HTTPS
- 配置GitHub Actions自动化测试与部署
- 日志与监控集成

## 📝 本章小结

### 重点概念
- ✅ 生产环境部署与安全
- ✅ Nginx反向代理与HTTPS
- ✅ 日志与监控
- ✅ CI/CD自动化部署
- ✅ 自动化测试

### 关键技能
- ✅ 配置Nginx与HTTPS
- ✅ 集成CI/CD流程
- ✅ 编写自动化测试

## 🔗 扩展阅读
- [Nginx官方文档](https://nginx.org/zh/docs/)
- [Let's Encrypt免费证书](https://letsencrypt.org/zh-cn/)
- [GitHub Actions文档](https://docs.github.com/en/actions)
- [pytest文档](https://docs.pytest.org/zh/latest/)

## ❓ 常见问题

**Q: 如何保证生产环境安全？**
A: 关闭调试模式、限制端口、使用HTTPS、定期更新依赖。

**Q: CI/CD失败如何排查？**
A: 查看Actions日志、分步调试、确保环境变量和密钥配置正确。 