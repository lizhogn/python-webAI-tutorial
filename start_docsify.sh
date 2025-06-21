#!/bin/bash

# Python Web AI 开发教程 - Docsify 启动脚本

echo "🚀 启动 Python Web AI 开发教程文档..."

# 检查是否安装了 docsify-cli
if ! command -v docsify &> /dev/null; then
    echo "📦 正在安装 docsify-cli..."
    npm install -g docsify-cli
fi

# 检查 docs 目录是否存在
if [ ! -d "docs" ]; then
    echo "❌ docs 目录不存在，请确保项目结构正确"
    exit 1
fi

# 进入 docs 目录并启动服务
cd docs

echo "🌐 启动文档服务器..."
echo "📖 文档地址: http://localhost:3000"
echo "🔄 按 Ctrl+C 停止服务"
echo ""

# 启动 docsify 服务
docsify serve . --port 3000 --open 