#!/bin/bash

echo "🚀 启动AI Web应用..."

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3未安装，请先安装Python3"
    exit 1
fi

# 检查是否在虚拟环境中
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  建议在虚拟环境中运行"
    echo "创建虚拟环境: python3 -m venv venv"
    echo "激活虚拟环境: source venv/bin/activate"
fi

# 安装依赖
echo "📦 安装依赖包..."
pip install -r requirements.txt

# 启动服务
echo "🔥 启动FastAPI服务..."
echo "📍 API地址: http://localhost:8000"
echo "📚 API文档: http://localhost:8000/docs"
echo "🌐 前端界面: 打开 frontend/index.html"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

python main.py 