# 第10章：AI模型集成

## 📚 学习目标

通过本章学习，你将掌握：
- AI模型在Web应用中的集成方法
- 模型序列化和加载技术
- 实时预测和批处理实现
- 模型版本管理和A/B测试
- 性能优化和缓存策略

## 🤖 AI模型集成概述

### 10.1 为什么需要AI模型集成？

AI模型集成是将训练好的机器学习模型部署到Web应用中，使其能够：
- **实时预测**：用户输入数据，立即获得AI预测结果
- **批量处理**：处理大量数据，提高效率
- **服务化**：将AI能力作为API服务提供给其他应用
- **用户体验**：在Web界面中直接使用AI功能

### 10.2 集成架构

```
┌─────────────┐    HTTP请求    ┌─────────────┐
│   前端界面  │ ──────────────→ │   Web API   │
└─────────────┘                └─────────────┘
                                        │
                                        ▼
                               ┌─────────────┐
                               │  AI模型服务 │
                               └─────────────┘
                                        │
                                        ▼
                               ┌─────────────┐
                               │   缓存层    │
                               └─────────────┘
```

## 🔧 模型序列化和加载

### 10.3 模型序列化方法

#### 使用pickle

```python
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# 训练模型（示例）
vectorizer = TfidfVectorizer()
classifier = RandomForestClassifier()

# 假设已经训练好模型
# vectorizer.fit(texts)
# classifier.fit(X_train, y_train)

# 保存模型
def save_model_pickle(model, filename):
    """使用pickle保存模型"""
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

# 加载模型
def load_model_pickle(filename):
    """使用pickle加载模型"""
    with open(filename, 'rb') as f:
        return pickle.load(f)

# 保存模型
save_model_pickle(vectorizer, 'vectorizer.pkl')
save_model_pickle(classifier, 'classifier.pkl')
```

#### 使用joblib（推荐）

```python
import joblib

# 保存模型
def save_model_joblib(model, filename):
    """使用joblib保存模型"""
    joblib.dump(model, filename)

# 加载模型
def load_model_joblib(filename):
    """使用joblib加载模型"""
    return joblib.load(filename)

# 保存模型
save_model_joblib(vectorizer, 'vectorizer.joblib')
save_model_joblib(classifier, 'classifier.joblib')
```

### 10.4 模型加载器类

```python
import joblib
import os
from typing import Any, Dict, Optional
import logging

class ModelLoader:
    """模型加载器类"""
    
    def __init__(self, model_dir: str = "models"):
        self.model_dir = model_dir
        self.models: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)
    
    def load_model(self, model_name: str, model_path: str) -> bool:
        """加载单个模型"""
        try:
            full_path = os.path.join(self.model_dir, model_path)
            if os.path.exists(full_path):
                self.models[model_name] = joblib.load(full_path)
                self.logger.info(f"模型 {model_name} 加载成功")
                return True
            else:
                self.logger.error(f"模型文件不存在: {full_path}")
                return False
        except Exception as e:
            self.logger.error(f"加载模型 {model_name} 失败: {str(e)}")
            return False
    
    def get_model(self, model_name: str) -> Optional[Any]:
        """获取模型"""
        return self.models.get(model_name)
    
    def load_all_models(self) -> bool:
        """加载所有模型"""
        models_to_load = {
            'vectorizer': 'vectorizer.joblib',
            'classifier': 'classifier.joblib'
        }
        
        success = True
        for model_name, model_path in models_to_load.items():
            if not self.load_model(model_name, model_path):
                success = False
        
        return success
    
    def reload_model(self, model_name: str, model_path: str) -> bool:
        """重新加载模型（用于模型更新）"""
        return self.load_model(model_name, model_path)

# 使用示例
model_loader = ModelLoader()
if model_loader.load_all_models():
    print("所有模型加载成功")
else:
    print("部分模型加载失败")
```

## 🚀 FastAPI中的AI模型集成

### 10.5 基本AI服务

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import numpy as np
from model_loader import ModelLoader

app = FastAPI(title="AI预测服务")

# 初始化模型加载器
model_loader = ModelLoader()
model_loader.load_all_models()

# 数据模型
class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    model_version: str

class BatchPredictionRequest(BaseModel):
    texts: List[str]

class BatchPredictionResponse(BaseModel):
    predictions: List[str]
    confidences: List[float]
    model_version: str

# 预测函数
def predict_sentiment(text: str) -> tuple:
    """预测文本情感"""
    try:
        vectorizer = model_loader.get_model('vectorizer')
        classifier = model_loader.get_model('classifier')
        
        if vectorizer is None or classifier is None:
            raise ValueError("模型未加载")
        
        # 特征提取
        features = vectorizer.transform([text])
        
        # 预测
        prediction = classifier.predict(features)[0]
        confidence = np.max(classifier.predict_proba(features))
        
        return prediction, confidence
    except Exception as e:
        raise ValueError(f"预测失败: {str(e)}")

# API端点
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """单条文本预测"""
    try:
        prediction, confidence = predict_sentiment(request.text)
        
        return PredictionResponse(
            prediction=prediction,
            confidence=float(confidence),
            model_version="1.0.0"
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

@app.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_batch(request: BatchPredictionRequest):
    """批量预测"""
    try:
        vectorizer = model_loader.get_model('vectorizer')
        classifier = model_loader.get_model('classifier')
        
        if vectorizer is None or classifier is None:
            raise HTTPException(status_code=500, detail="模型未加载")
        
        # 批量特征提取
        features = vectorizer.transform(request.texts)
        
        # 批量预测
        predictions = classifier.predict(features)
        confidences = np.max(classifier.predict_proba(features), axis=1)
        
        return BatchPredictionResponse(
            predictions=predictions.tolist(),
            confidences=confidences.tolist(),
            model_version="1.0.0"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"批量预测失败: {str(e)}")

@app.get("/health")
async def health_check():
    """健康检查"""
    models_loaded = all([
        model_loader.get_model('vectorizer') is not None,
        model_loader.get_model('classifier') is not None
    ])
    
    return {
        "status": "healthy" if models_loaded else "unhealthy",
        "models_loaded": models_loaded,
        "model_count": len(model_loader.models)
    }
```

## 📝 本章小结

### 重点概念
- ✅ AI模型在Web应用中的集成方法
- ✅ 模型序列化和加载技术
- ✅ 实时预测和批处理实现
- ✅ 模型版本管理和A/B测试
- ✅ 性能优化和缓存策略

### 关键技能
- ✅ 使用joblib序列化和加载模型
- ✅ 在FastAPI中集成AI模型
- ✅ 实现模型缓存和异步处理
- ✅ 设计A/B测试框架
- ✅ 构建完整的AI Web应用

## 🔗 扩展阅读

- [scikit-learn模型持久化](https://scikit-learn.org/stable/modules/model_persistence.html)
- [FastAPI最佳实践](https://fastapi.tiangolo.com/tutorial/)
- [Redis缓存策略](https://redis.io/topics/caching)
- [Celery异步任务](https://docs.celeryproject.org/)

## ❓ 常见问题

**Q: 如何选择模型序列化方法？**
A: joblib通常比pickle更安全，支持大文件，推荐使用joblib。

**Q: 模型文件很大怎么办？**
A: 考虑模型压缩、量化、使用更轻量的模型，或者使用模型服务化。

**Q: 如何监控模型性能？**
A: 记录预测结果、用户反馈、模型指标，定期评估模型效果。

---

**下一章：异步处理** → [第11章：异步处理](./chapter11_async_processing.md) 