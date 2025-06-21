# 第2章：Flask入门

## 📚 学习目标

通过本章学习，你将掌握：
- Flask框架的基本概念
- 路由和视图函数的使用
- 模板引擎Jinja2的基础
- 表单处理和静态文件管理
- 构建第一个Flask应用

## 🐍 Flask简介

### 2.1 什么是Flask？

Flask是一个轻量级的Python Web框架，具有以下特点：
- **微框架**：核心简单，扩展性强
- **灵活性**：不强制特定的项目结构
- **易学易用**：学习曲线平缓
- **丰富的扩展**：大量第三方扩展

### 2.2 Flask vs 其他框架

| 特性 | Flask | Django | FastAPI |
|------|-------|--------|---------|
| 学习曲线 | 平缓 | 陡峭 | 中等 |
| 灵活性 | 高 | 低 | 高 |
| 性能 | 中等 | 中等 | 高 |
| 适用场景 | 小型项目 | 大型项目 | API服务 |

## 🚀 第一个Flask应用

### 2.3 环境准备

```bash
# 创建虚拟环境
python -m venv flask_env
source flask_env/bin/activate  # Linux/Mac
# 或
flask_env\Scripts\activate     # Windows

# 安装Flask
pip install flask
```

### 2.4 Hello World应用

创建 `app.py` 文件：

```python
from flask import Flask

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由和视图函数
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return '这是关于页面'

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
```

运行应用：
```bash
python app.py
```

访问 http://localhost:5000 查看结果。

## 🛣️ 路由和视图函数

### 2.5 基本路由

```python
from flask import Flask

app = Flask(__name__)

# 基本路由
@app.route('/')
def index():
    return '首页'

# 带参数的路由
@app.route('/user/<username>')
def show_user(username):
    return f'用户: {username}'

# 指定参数类型
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'文章ID: {post_id}'

# 多个参数
@app.route('/user/<username>/post/<int:post_id>')
def show_user_post(username, post_id):
    return f'用户 {username} 的文章 {post_id}'
```

### 2.6 HTTP方法

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'登录: {username}'
    else:
        return '''
        <form method="post">
            <p>用户名: <input type="text" name="username"></p>
            <p>密码: <input type="password" name="password"></p>
            <p><input type="submit" value="登录"></p>
        </form>
        '''
```

## 📄 模板引擎Jinja2

### 2.7 基本模板

创建 `templates` 文件夹，添加 `index.html`：

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    
    {% if user %}
        <p>欢迎, {{ user }}!</p>
    {% else %}
        <p>请 <a href="/login">登录</a></p>
    {% endif %}
    
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

更新 `app.py`：

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                         title='Flask教程',
                         message='欢迎学习Flask!',
                         user='张三',
                         items=['Python', 'Flask', 'Web开发'])
```

### 2.8 模板继承

创建基础模板 `templates/base.html`：

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">首页</a>
        <a href="{{ url_for('about') }}">关于</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Flask教程</p>
    </footer>
</body>
</html>
```

创建子模板 `templates/index.html`：

```html
{% extends "base.html" %}

{% block title %}首页{% endblock %}

{% block content %}
<h1>欢迎来到Flask教程</h1>
<p>这是一个使用模板继承的页面。</p>
{% endblock %}
```

## 📝 表单处理

### 2.9 基本表单

创建 `templates/login.html`：

```html
{% extends "base.html" %}

{% block title %}登录{% endblock %}

{% block content %}
<h1>用户登录</h1>

{% if error %}
<p style="color: red;">{{ error }}</p>
{% endif %}

<form method="post">
    <p>
        <label for="username">用户名:</label>
        <input type="text" id="username" name="username" required>
    </p>
    <p>
        <label for="password">密码:</label>
        <input type="password" id="password" name="password" required>
    </p>
    <p>
        <input type="submit" value="登录">
    </p>
</form>
{% endblock %}
```

更新 `app.py`：

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 用于flash消息

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 简单的验证逻辑
        if username == 'admin' and password == 'password':
            flash('登录成功!', 'success')
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误!', 'error')
    
    return render_template('login.html')
```

## 🎨 静态文件管理

### 2.10 CSS样式

创建 `static/style.css`：

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f5f5f5;
}

nav {
    background-color: #333;
    padding: 10px;
    margin-bottom: 20px;
}

nav a {
    color: white;
    text-decoration: none;
    margin-right: 20px;
}

nav a:hover {
    color: #ddd;
}

main {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

form {
    max-width: 400px;
}

form p {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"], input[type="password"] {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

input[type="submit"] {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}

.flash {
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 4px;
}

.flash.success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.flash.error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}
```

更新 `templates/base.html` 显示flash消息：

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">首页</a>
        <a href="{{ url_for('about') }}">关于</a>
        <a href="{{ url_for('login') }}">登录</a>
    </nav>
    
    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Flask教程</p>
    </footer>
</body>
</html>
```

## 🏗️ 项目结构

### 2.11 推荐的项目结构

```
my_flask_app/
├── app.py                 # 应用入口
├── config.py             # 配置文件
├── requirements.txt      # 依赖包
├── static/              # 静态文件
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # 模板文件
│   ├── base.html
│   ├── index.html
│   └── login.html
└── instance/           # 实例配置
    └── config.py
```

### 2.12 配置文件

创建 `config.py`：

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

更新 `app.py`：

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            if username == 'admin' and password == 'password':
                flash('登录成功!', 'success')
                return redirect(url_for('index'))
            else:
                flash('用户名或密码错误!', 'error')
        
        return render_template('login.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
```

## 💻 实践项目

### 项目：个人博客系统

创建一个简单的个人博客系统，包含以下功能：
- 文章列表页面
- 文章详情页面
- 简单的文章管理

#### 步骤1：创建数据模型

```python
# 模拟数据库
articles = [
    {
        'id': 1,
        'title': 'Flask入门教程',
        'content': '这是Flask入门教程的内容...',
        'author': '张三',
        'date': '2024-01-01'
    },
    {
        'id': 2,
        'title': 'Python Web开发',
        'content': 'Python Web开发指南...',
        'author': '李四',
        'date': '2024-01-02'
    }
]
```

#### 步骤2：创建模板

`templates/blog.html`：
```html
{% extends "base.html" %}

{% block title %}博客{% endblock %}

{% block content %}
<h1>我的博客</h1>

{% for article in articles %}
<article>
    <h2><a href="{{ url_for('article', id=article.id) }}">{{ article.title }}</a></h2>
    <p>作者: {{ article.author }} | 日期: {{ article.date }}</p>
    <p>{{ article.content[:100] }}...</p>
</article>
{% endfor %}
{% endblock %}
```

`templates/article.html`：
```html
{% extends "base.html" %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
<article>
    <h1>{{ article.title }}</h1>
    <p>作者: {{ article.author }} | 日期: {{ article.date }}</p>
    <div class="content">
        {{ article.content }}
    </div>
    <p><a href="{{ url_for('blog') }}">返回博客列表</a></p>
</article>
{% endblock %}
```

#### 步骤3：添加路由

```python
@app.route('/blog')
def blog():
    return render_template('blog.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    article = next((a for a in articles if a['id'] == id), None)
    if article:
        return render_template('article.html', article=article)
    else:
        flash('文章不存在!', 'error')
        return redirect(url_for('blog'))
```

## 📝 本章小结

### 重点概念
- ✅ Flask框架的基本概念和特点
- ✅ 路由和视图函数的使用
- ✅ 模板引擎Jinja2的基础语法
- ✅ 表单处理和静态文件管理
- ✅ Flask项目的组织结构

### 关键技能
- ✅ 创建和运行Flask应用
- ✅ 定义路由和视图函数
- ✅ 使用模板渲染页面
- ✅ 处理表单提交
- ✅ 管理静态文件

## 🔗 扩展阅读

- [Flask官方文档](https://flask.palletsprojects.com/)
- [Jinja2模板引擎](https://jinja.palletsprojects.com/)
- [Flask最佳实践](https://flask.palletsprojects.com/en/2.3.x/patterns/)

## ❓ 常见问题

**Q: Flask和Django有什么区别？**
A: Flask是微框架，灵活性高但需要自己组装；Django是全功能框架，功能完整但学习曲线陡峭。

**Q: 什么时候使用Flask？**
A: 适合小型到中型项目，需要高度定制化的场景。

**Q: 如何调试Flask应用？**
A: 设置 `debug=True`，使用 `print()` 或日志，也可以使用调试器。

---

**下一章：FastAPI进阶** → [第3章：FastAPI进阶](./chapter3_fastapi_advanced.md) 