# 🚀 Advanced Agentic RAG Framework

An enterprise-grade Retrieval-Augmented Generation (RAG) framework utilizing autonomous agents, designed for highly accurate, scalable, and secure document intelligence.

## 🏗️ Architecture
This framework is built with:
- **FastAPI** for high-performance async REST APIs.
- **LangChain** & **LlamaIndex** for LLM orchestration and Agentic routing.
- **Qdrant / Pinecone** for fast vector similarity search.
- **HuggingFace** / **OpenAI** for embedding models and text generation.

## 📁 Repository Structure
- `api/` - FastAPI routes and request/response models.
- `core/` - Application configurations, security, and logging.
- `services/` - Core business logic, RAG pipelines, and Agent definitions.
- `infrastructure/` - Dockerfiles, docker-compose, and deployment scripts.

## 🚀 Quick Start
```bash
docker-compose up --build
```
Or run locally:
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```
