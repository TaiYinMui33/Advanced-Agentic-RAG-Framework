# 🚀 Advanced Agentic RAG Framework

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![CI/CD](https://github.com/TaiYinMui33/Advanced-Agentic-RAG-Framework/actions/workflows/ci.yml/badge.svg)](https://github.com/TaiYinMui33/Advanced-Agentic-RAG-Framework/actions)

## 🌟 Overview
**Advanced Agentic RAG Framework** is an enterprise-grade solution for building autonomous document intelligence systems. Unlike traditional RAG, this framework employs **Agentic Reasoning** to dynamically route queries, multi-step plan information retrieval, and self-correct based on retrieved context.

Built for scalability and high-performance, it leverages asynchronous processing and vector-native search to provide precise answers from massive unstructured datasets.

---

## 🏗️ System Architecture
The framework follows a modular, cloud-native architecture:

1.  **API Layer (FastAPI):** High-concurrency asynchronous endpoints for query submission and session management.
2.  **Agentic Orchestrator (LangChain/LlamaIndex):** The brain of the system. It determines if a query needs internal knowledge, external search, or mathematical analysis.
3.  **Vector Intelligence (Qdrant):** Handles high-dimensional semantic search with sub-millisecond latency.
4.  **Embedding & Generation:** Utilizes state-of-the-art models (BGE-Large/GPT-4) for semantic understanding and natural language synthesis.

---

## 🛠️ Key Features
- **Autonomous Routing:** Dynamically chooses between multiple data sources and tools.
- **Multi-Turn Conversation Memory:** Maintains context across complex, multi-step dialogues.
- **Semantic Re-ranking:** Implements Cross-Encoder models to re-rank retrieved documents for maximum relevance.
- **Observability:** Integrated logging for agent thought-processes and tool execution.
- **Enterprise Security:** API Key-based authentication and role-based data isolation.

---

## 📁 Repository Structure
```text
├── api/                # API controllers and schemas
│   ├── main.py         # Application entry point
│   └── routes/         # Versioned API routes
├── core/               # Cross-cutting concerns
│   ├── config.py       # Pydantic-based configuration management
│   ├── security.py     # Auth and encryption logic
│   └── logger.py       # Structured logging setup
├── services/           # Domain logic (The "Heart")
│   ├── rag_agent.py    # Agent definitions and reasoning loops
│   ├── vector_store.py # Vector database abstractions
│   └── tools.py        # Custom tools (Search, Analysis, Python Interpreter)
├── infrastructure/     # Deployment assets
│   ├── Dockerfile      # Optimized multi-stage build
│   └── docker-compose.yml
├── tests/              # Comprehensive test suite (Unit & Integration)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- OpenAI API Key (or local LLM via Ollama)

### Local Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/TaiYinMui33/Advanced-Agentic-RAG-Framework.git
   cd Advanced-Agentic-RAG-Framework
   ```

2. **Setup Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Create a `.env` file based on `core/config.py`:
   ```env
   OPENAI_API_KEY=your_key_here
   QDRANT_HOST=localhost
   ```

4. **Run the API:**
   ```bash
   uvicorn api.main:app --reload
   ```

### Docker Deployment
```bash
docker-compose up --build -d
```

---

## 🔌 API Documentation
Once running, visit `http://localhost:8000/docs` for interactive Swagger UI.

### Querying the Agent
**Endpoint:** `POST /api/v1/query`  
**Payload:**
```json
{
  "query": "What are the specific safety protocols for underwater robotics as per the 2024 manual?",
  "session_id": "user-session-991"
}
```

---

## 🧪 Testing & Validation
We prioritize code quality and reliability.
```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=services tests/
```

---

## 🤝 Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
**Maintained by [Tai Yin Mui](https://github.com/TaiYinMui33)**  
*Expertise in AI Engineering, Computer Vision, and Data Science.*
