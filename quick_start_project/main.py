from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List, Optional

# 创建FastAPI应用
app = FastAPI(
    title="AI Web应用示例",
    description="一个简单的AI Web应用，展示如何集成AI模型",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应该指定具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class TextInput(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    model_version: str

# 模拟AI模型（你可以替换为你的实际模型）
class SimpleAIModel:
    def __init__(self):
        self.model_version = "1.0.0"
    
    def predict(self, text: str) -> tuple:
        # 这里是一个简单的示例，你可以替换为你的AI模型
        # 模拟文本分类：根据关键词判断情感
        positive_words = ['好', '棒', '优秀', '喜欢', '满意', '开心']
        negative_words = ['差', '糟糕', '讨厌', '失望', '难过', '生气']
        
        text_lower = text.lower()
        positive_score = sum(1 for word in positive_words if word in text_lower)
        negative_score = sum(1 for word in negative_words if word in text_lower)
        
        if positive_score > negative_score:
            return "正面", 0.8
        elif negative_score > positive_score:
            return "负面", 0.7
        else:
            return "中性", 0.5

# 初始化模型
model = SimpleAIModel()

@app.get("/")
async def root():
    """根路径，返回API信息"""
    return {
        "message": "欢迎使用AI Web应用API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse)
async def predict_sentiment(input_data: TextInput):
    """文本情感分析预测"""
    try:
        if not input_data.text.strip():
            raise HTTPException(status_code=400, detail="文本不能为空")
        
        prediction, confidence = model.predict(input_data.text)
        
        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            model_version=model.model_version
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"预测失败: {str(e)}")

@app.get("/model-info")
async def get_model_info():
    """获取模型信息"""
    return {
        "model_version": model.model_version,
        "model_type": "文本情感分析",
        "supported_languages": ["中文", "英文"],
        "input_format": "文本字符串",
        "output_format": "情感标签 + 置信度"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 