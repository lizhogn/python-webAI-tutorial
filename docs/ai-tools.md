# AI 相关工具

## 大语言模型平台

### OpenAI
- **GPT-4**: 最先进的大语言模型
- **GPT-3.5-turbo**: 性价比高的对话模型
- **DALL-E**: 图像生成模型
- **Whisper**: 语音转文字模型
- **API 文档**: https://platform.openai.com/docs

### Anthropic
- **Claude**: 安全、有帮助的 AI 助手
- **Claude Instant**: 快速响应版本
- **API 文档**: https://docs.anthropic.com/

### Google
- **PaLM**: Google 的大语言模型
- **Bard**: Google 的对话 AI
- **Vertex AI**: 企业级 AI 平台

## 开发框架

### LangChain
- **简介**: 大语言模型应用开发框架
- **功能**: 链式调用、记忆管理、工具集成
- **特点**: 模块化设计、丰富的集成
- **GitHub**: https://github.com/langchain-ai/langchain
- **文档**: https://python.langchain.com/

### LlamaIndex
- **简介**: 数据框架，用于 LLM 应用
- **功能**: 文档加载、索引、查询
- **特点**: 专注于数据集成
- **GitHub**: https://github.com/jerryjliu/llama_index

### AutoGPT
- **简介**: 自主 AI 代理框架
- **功能**: 任务分解、工具使用、自主执行
- **特点**: 实验性项目，展示 AI 代理潜力

## 向量数据库

### ChromaDB
- **简介**: 开源向量数据库
- **特点**: 易用、轻量级、Python 原生
- **用途**: 文档检索、语义搜索
- **GitHub**: https://github.com/chroma-core/chroma

### Pinecone
- **简介**: 云原生向量数据库
- **特点**: 高性能、可扩展、托管服务
- **用途**: 生产环境向量搜索

### Weaviate
- **简介**: 向量搜索引擎
- **特点**: GraphQL API、多模态支持
- **GitHub**: https://github.com/weaviate/weaviate

## 模型社区

### Hugging Face
- **简介**: AI 模型和数据集的中心
- **功能**: 模型托管、数据集分享、社区协作
- **特点**: 开源友好、资源丰富
- **网址**: https://huggingface.co/

### ModelScope
- **简介**: 阿里巴巴的模型社区
- **特点**: 中文模型丰富、国内访问快
- **网址**: https://modelscope.cn/

## 快速原型工具

### Gradio
- **简介**: 快速创建 AI Web 界面
- **特点**: 简单易用、支持多种输入输出
- **GitHub**: https://github.com/gradio-app/gradio
- **文档**: https://gradio.app/

### Streamlit
- **简介**: 数据科学 Web 应用框架
- **特点**: Python 原生、快速开发
- **GitHub**: https://github.com/streamlit/streamlit

### Replicate
- **简介**: 云平台，运行开源 AI 模型
- **特点**: 一键部署、API 调用
- **网址**: https://replicate.com/

## 提示工程工具

### Promptfoo
- **简介**: 提示测试和评估工具
- **功能**: A/B 测试、批量评估
- **GitHub**: https://github.com/promptfoo/promptfoo

### LangSmith
- **简介**: LangChain 的调试和监控平台
- **功能**: 提示调试、性能监控
- **网址**: https://smith.langchain.com/

## 模型微调工具

### LoRA
- **简介**: 低秩适应微调方法
- **特点**: 参数高效、资源需求低
- **实现**: PEFT 库

### QLoRA
- **简介**: 量化 LoRA 微调
- **特点**: 内存效率更高
- **论文**: https://arxiv.org/abs/2305.14314

## 评估工具

### HELM
- **简介**: 语言模型评估基准
- **特点**: 全面评估、标准化
- **GitHub**: https://github.com/stanford-crfm/helm

### OpenLLM
- **简介**: 开源 LLM 服务框架
- **功能**: 模型服务化、API 标准化
- **GitHub**: https://github.com/bentoml/OpenLLM

## 学习资源

- [LangChain 教程](https://python.langchain.com/docs/tutorials/)
- [Hugging Face 课程](https://huggingface.co/course)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 实用技巧

### 提示工程
```python
# 基础提示模板
template = """
你是一个专业的{role}。
请{task}。

输入: {input}
输出: 
"""

# 少样本学习
few_shot_prompt = """
示例1:
输入: "今天天气怎么样？"
输出: "今天天气晴朗，温度25度。"

示例2:
输入: "明天会下雨吗？"
输出: "明天可能有小雨，建议带伞。"

现在请回答:
输入: "{user_input}"
输出: 
"""
```

### 向量检索
```python
import chromadb
from chromadb.config import Settings

# 创建客户端
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

# 创建集合
collection = client.create_collection("documents")

# 添加文档
collection.add(
    documents=["文档内容1", "文档内容2"],
    metadatas=[{"source": "file1"}, {"source": "file2"}],
    ids=["id1", "id2"]
)

# 查询
results = collection.query(
    query_texts=["查询内容"],
    n_results=2
)
``` 