# AI Web应用快速开始项目

这是一个简单的AI Web应用示例，展示了如何将AI模型集成到Web应用中。

## 🚀 快速开始

### 1. 安装依赖

```bash
cd quick_start_project
pip install -r requirements.txt
```

### 2. 启动后端服务

```bash
python main.py
```

或者使用uvicorn：

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 访问应用

- **API文档**: http://localhost:8000/docs
- **前端界面**: 打开 `frontend/index.html` 文件

## 📁 项目结构

```
quick_start_project/
├── main.py              # FastAPI后端应用
├── requirements.txt     # Python依赖
├── frontend/
│   └── index.html      # 前端界面
└── README.md           # 项目说明
```

## 🔧 API端点

- `GET /` - 根路径，返回API信息
- `GET /health` - 健康检查
- `POST /predict` - 文本情感分析
- `GET /model-info` - 获取模型信息
- `GET /docs` - API文档 (Swagger UI)

## 🎯 功能特性

- ✅ 文本情感分析
- ✅ RESTful API设计
- ✅ 自动API文档生成
- ✅ CORS支持
- ✅ 错误处理
- ✅ 响应式前端界面
- ✅ 实时预测结果展示

## 🔄 如何集成你的AI模型

### 1. 替换模型类

在 `main.py` 中，将 `SimpleAIModel` 类替换为你的实际模型：

```python
class YourAIModel:
    def __init__(self):
        # 加载你的模型
        self.model = joblib.load('your_model.pkl')
        self.model_version = "1.0.0"
    
    def predict(self, text: str) -> tuple:
        # 你的预测逻辑
        prediction = self.model.predict([text])
        confidence = self.model.predict_proba([text]).max()
        return prediction[0], confidence
```

### 2. 修改数据模型

根据你的模型输入输出格式，修改 `TextInput` 和 `PredictionResponse` 类。

### 3. 更新前端

根据你的模型输出格式，更新前端的结果展示逻辑。

## 🛠️ 开发建议

### 1. 环境管理
```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

### 2. 开发模式
```bash
# 使用热重载
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 测试API
```bash
# 使用curl测试
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "这个产品很棒！"}'
```

## 📚 学习要点

1. **FastAPI基础**: 路由、数据模型、中间件
2. **前后端分离**: API设计、CORS配置
3. **AI模型集成**: 模型加载、预测接口
4. **错误处理**: 异常捕获、用户友好提示
5. **前端交互**: AJAX请求、动态UI更新

## 🔗 下一步学习

完成这个项目后，建议学习：

1. **数据库集成**: SQLAlchemy + PostgreSQL
2. **用户认证**: JWT + 用户管理
3. **异步处理**: Celery + Redis
4. **容器化**: Docker + Docker Compose
5. **部署**: Nginx + Gunicorn

## 🐛 常见问题

### Q: 前端无法连接到后端？
A: 确保后端服务已启动，并检查CORS配置。

### Q: 如何添加更多AI模型？
A: 可以创建多个预测端点，或使用模型路由。

### Q: 如何优化性能？
A: 考虑使用模型缓存、异步处理、负载均衡。

## �� 许可证

MIT License 