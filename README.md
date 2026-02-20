<p align="center">
  <img src="https://img.shields.io/badge/DevChoreo-v1.0-blue?style=for-the-badge&logo=wso2&logoColor=white" alt="DevChoreo v1.0">
</p>

<h1 align="center">🚀 DevChoreo — AI-Powered RAG Assistant</h1>

<p align="center">
  <strong>Intelligent Documentation Assistant for the WSO2 Choreo Platform</strong><br>
  <em>Powered by GPT-4 · RAG Pipeline · Real-time Streaming · Mermaid Diagrams</em>
</p>

<p align="center">
  <a href="https://github.com/YOUR_ORG/DevChoreo/actions/workflows/ci-cd.yml"><img src="https://github.com/YOUR_ORG/DevChoreo/actions/workflows/ci-cd.yml/badge.svg" alt="CI/CD Pipeline"></a>
  <a href="https://github.com/YOUR_ORG/DevChoreo/actions/workflows/codeql.yml"><img src="https://github.com/YOUR_ORG/DevChoreo/actions/workflows/codeql.yml/badge.svg" alt="CodeQL"></a>
  <a href="https://github.com/YOUR_ORG/DevChoreo/actions/workflows/docker-build-test.yml"><img src="https://github.com/YOUR_ORG/DevChoreo/actions/workflows/docker-build-test.yml/badge.svg" alt="Docker Build"></a>
  <img src="https://img.shields.io/badge/python-3.12+-blue?logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/react-18-61dafb?logo=react&logoColor=white" alt="React 18">
  <img src="https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

---

## 📖 Overview

**DevChoreo** is an AI-powered Retrieval-Augmented Generation (RAG) assistant purpose-built for the [WSO2 Choreo](https://wso2.com/choreo/) platform. It ingests documentation from GitHub repositories, processes and indexes content into a vector database, and provides intelligent, context-aware responses through a modern chat interface with real-time streaming.

The system combines the power of **Azure OpenAI GPT-4** for natural language understanding, **Milvus Cloud** for vector similarity search, and a sophisticated multi-stage RAG pipeline to deliver accurate, source-grounded answers about Choreo's developer platform.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 💬 **Intelligent Chat UI** | Modern React-based chat interface with markdown rendering, code highlighting, and source citations |
| ⚡ **Real-time SSE Streaming** | Server-Sent Events for progressive token display with first-token latency of 1–2 seconds |
| 📊 **Mermaid Diagram Generation** | Automatic diagram detection and rendering with interactive zoom and fullscreen support |
| 🧠 **Advanced RAG Pipeline** | Multi-step reasoning with LangGraph and LangChain for context-aware document retrieval |
| 💾 **Conversation Memory** | Smart summarization with 75% token-trigger threshold and persistent chat history |
| 📂 **Multi-Chat Sidebar** | Full CRUD operations, search, and session management for multiple conversations |
| 🔗 **URL Validation & Grounding** | Concurrent HTTP HEAD checks, caching, 404 prevention, and monorepo URL auto-fix |
| 📦 **Automated Ingestion** | GitHub repository content ingestion with SHA-based deduplication and webhook support |
| 👁️ **Image OCR Processing** | Google Cloud Vision API integration for text extraction from documentation images |
| 📡 **Full Observability** | 23+ Prometheus metrics, 8 Grafana dashboard panels, and 7 alert rules |

---

## 🏗️ Architecture

<p align="center">
  <em>See <a href="architecture-diagram.html">architecture-diagram.html</a> for the full interactive architecture visualization.</em>
</p>

```
┌─────────────────────────────────────────────────────────┐
│                    👤 Web Browser (HTTPS)                │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              FRONTEND (React 18 + Vite + Tailwind)      │
│  Chat UI · Message Renderer · Mermaid · Sidebar · SSE   │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│          BACKEND API GATEWAY (FastAPI + Uvicorn)        │
│  /api/ask/stream · /api/ask · /api/ask_graph            │
│  /api/ingest/github · /api/ingest/org · /api/webhook    │
│  /api/health · /metrics                                 │
└──────┬──────────────┬──────────────┬────────────────────┘
       │              │              │
┌──────▼──────┐ ┌─────▼──────┐ ┌────▼──────────┐
│ AI & RAG    │ │   Data     │ │  Quality &    │
│ Pipeline    │ │ Processing │ │  Validation   │
│             │ │            │ │               │
│ LLMService  │ │ Ingestion  │ │ URLValidator  │
│ Memory Mgr  │ │ Chunker    │ │ URL Grounding │
│ Context Mgr │ │ GitHub Svc │ │ Repo Registry │
│ Diagram Det │ │ Markdown   │ │ LLM Matcher   │
│ RAGGraph    │ │ Image Proc │ │ VectorClient  │
└──────┬──────┘ └─────┬──────┘ └────┬──────────┘
       │              │              │
┌──────▼──────────────▼──────────────▼────────────────────┐
│              EXTERNAL CLOUD SERVICES                    │
│  Azure OpenAI · Milvus Cloud · GitHub API · Google OCR  │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance async Python web framework |
| **Python 3.12+** | Core runtime with type hints and modern features |
| **Uvicorn** | ASGI server for production deployment |
| **LangChain** | LLM orchestration and chain composition |
| **LangGraph** | Multi-step reasoning and graph-based RAG workflows |
| **PyMilvus** | Vector database SDK for similarity search |
| **Azure OpenAI SDK** | GPT-4 chat completions and ada-002 embeddings |
| **Google Cloud Vision** | OCR and image text extraction |
| **Prometheus Client** | Metrics instrumentation (23+ custom metrics) |

### Frontend
| Technology | Purpose |
|------------|---------|
| **React 18** | Component-based UI with hooks |
| **Vite** | Lightning-fast build tool and dev server |
| **Tailwind CSS** | Utility-first CSS framework |
| **Mermaid.js** | Diagram rendering with interactive controls |
| **SSE (EventSource)** | Real-time streaming response display |

### Infrastructure
| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization with Python 3.12-slim base |
| **WSO2 Choreo** | Cloud deployment platform with API gateway |
| **Prometheus** | Metrics collection and alerting |
| **Grafana** | Monitoring dashboards (8 panels) |
| **Alertmanager** | Alert routing and notification (7 rules) |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+**
- **Node.js 20+** and **npm**
- **Docker** (optional, for containerized deployment)
- Azure OpenAI API access
- Milvus Cloud (Zilliz) instance

### Environment Variables

Create a `.env` file in the project root:

```env
# Azure OpenAI
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002
AZURE_OPENAI_API_VERSION=2024-02-01

# Milvus / Zilliz Cloud
MILVUS_URI=https://your-instance.zillizcloud.com
MILVUS_TOKEN=your-milvus-token
MILVUS_COLLECTION_NAME=choreo_docs

# GitHub
GITHUB_TOKEN=your-github-token

# Google Cloud Vision
GOOGLE_VISION_API_KEY=your-google-vision-key

# Application
APP_ENV=development
LOG_LEVEL=INFO
```

### Local Development

#### Backend

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build standalone
docker build -t devchoreo:latest .
docker run -p 8000:8000 --env-file .env devchoreo:latest
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/ask/stream` | Stream a response via SSE for a user query |
| `POST` | `/api/ask` | Get a complete response for a user query |
| `POST` | `/api/ask_graph` | Multi-step graph-based RAG query |
| `POST` | `/api/ingest/github` | Ingest documentation from a GitHub repository |
| `POST` | `/api/ingest/org` | Bulk ingest all repos from a GitHub organization |
| `POST` | `/api/webhook/github` | GitHub webhook endpoint for auto-ingestion |
| `GET`  | `/api/health` | Health check endpoint |
| `GET`  | `/metrics` | Prometheus metrics endpoint |

### Example Request

```bash
# Stream a response
curl -X POST http://localhost:8000/api/ask/stream \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I deploy a service on Choreo?", "conversation_id": "abc-123"}'

# Ingest a GitHub repository
curl -X POST http://localhost:8000/api/ingest/github \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/wso2/docs-choreo"}'
```

---

## 🧠 Core Services

### AI & RAG Pipeline

| Service | Responsibility |
|---------|---------------|
| **LLMService** | Manages GPT-4 chat completions and ada-002 embedding generation with streaming support |
| **ConversationMemoryManager** | Tracks token usage, triggers smart summarization at 75% capacity threshold |
| **ContextManager** | Orchestrates the full RAG flow: query → embed → vector search → context retrieval |
| **DiagramDetectionService** | Detects diagram-worthy queries and enhances prompts for Mermaid generation |
| **RAGGraph** | LangGraph-based multi-step reasoning engine with LangChain integration |

### Data Processing

| Service | Responsibility |
|---------|---------------|
| **IngestionService** | Full pipeline: GitHub fetch → chunk → embed → store with SHA-based deduplication |
| **DocumentChunker** | Splits documents into 3000-character chunks with 200-character overlap and pre-split logic |
| **GitHubService** | GitHub API client for repository content fetching, org-level operations, and webhooks |
| **MarkdownProcessor** | Cleans, normalizes, and preprocesses markdown (removes images, fixes formatting) |
| **ImageProcessingService** | Integrates Google Cloud Vision API for OCR text extraction from images |

### Quality & Validation

| Service | Responsibility |
|---------|---------------|
| **URLValidator** | Concurrent HTTP HEAD validation with response caching and 404 prevention |
| **URLGroundingService** | Ensures link correctness through registry lookup and validation |
| **ChoreoRepoRegistry** | Maps 30+ Choreo components with monorepo URL auto-correction |
| **LLMRepoMatcher** | AI-powered intelligent repository search with context-aware matching |
| **VectorClient** | PyMilvus SDK wrapper for cosine similarity search and batch insert operations |

---

## 📊 Observability

DevChoreo includes a comprehensive observability stack:

### Prometheus Metrics (23+ Custom Metrics)
- Request latency histograms (p50, p90, p99)
- Token usage counters (prompt + completion)
- Vector search performance metrics
- Ingestion pipeline throughput
- Error rate tracking by endpoint
- Active connection gauges

### Grafana Dashboards (8 Panels)
- API request rate and latency
- LLM token consumption trends
- Vector search response times
- Ingestion pipeline status
- Error rate monitoring
- System resource utilization
- Active user sessions
- Cache hit/miss ratios

### Alertmanager Rules (7 Alert Rules)
- High error rate detection
- Latency threshold breaches
- LLM API failure alerts
- Vector DB connectivity issues
- Ingestion pipeline failures
- Memory usage warnings
- Health check failures

---

## 🐳 Deployment

### Docker Container
- **Base Image**: `python:3.12-slim`
- **Non-root Execution**: Runs as unprivileged user for security
- **Startup Time**: < 5 seconds with lazy initialization
- **Health Check**: Built-in `/api/health` endpoint

### WSO2 Choreo Platform
- Deployed as a managed service on WSO2 Choreo
- API Gateway integration for traffic management
- Choreo Secrets for secure credential management
- Auto-scaling and monitoring via Choreo dashboard

---

## 🔄 CI/CD Pipeline

This project includes comprehensive GitHub Actions workflows:

| Workflow | Description |
|----------|-------------|
| **CI/CD Pipeline** | Lint, test, and build for both backend and frontend |
| **CodeQL Analysis** | Automated security vulnerability scanning |
| **Docker Build & Test** | Build Docker images and run health checks |
| **Release Management** | Automated releases with changelog generation |
| **Publish to GHCR** | Multi-platform Docker image publishing |
| **Dependabot** | Automated dependency update PRs |

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'feat: add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages
- Ensure all tests pass before submitting a PR
- Add tests for new features
- Update documentation as needed
- Use type hints in Python code
- Follow ESLint rules for frontend code

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [WSO2 Choreo](https://wso2.com/choreo/) — Cloud-native platform
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) — GPT-4 and embeddings
- [Milvus / Zilliz Cloud](https://zilliz.com/) — Vector database
- [LangChain](https://www.langchain.com/) & [LangGraph](https://github.com/langchain-ai/langgraph) — LLM orchestration
- [FastAPI](https://fastapi.tiangolo.com/) — Backend framework
- [React](https://react.dev/) & [Vite](https://vitejs.dev/) — Frontend stack

---

<p align="center">
  <strong>DevChoreo v1.0</strong> · February 2026<br>
  Built with ❤️ using FastAPI + React + Azure OpenAI + Milvus Cloud
</p>

