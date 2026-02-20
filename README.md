<p align="center">
  <img src="https://img.shields.io/badge/DevChoreo-Architecture-blue?style=for-the-badge&logo=wso2&logoColor=white" alt="DevChoreo Architecture">
</p>

<h1 align="center">🏗️ DevChoreo — System Architecture Diagram</h1>

<p align="center">
  <strong>Interactive Architecture Visualization for the DevChoreo AI-Powered RAG Assistant</strong><br>
  <em>Built for the WSO2 Choreo Platform</em>
</p>

<p align="center">
  <a href="https://dev-choreo-architecture.netlify.app/"><img src="https://img.shields.io/badge/🔗_Live_Demo-dev--choreo--architecture.netlify.app-00C7B7?style=for-the-badge&logo=netlify&logoColor=white" alt="Live Demo"></a>
</p>

<p align="center">
  <a href="https://github.com/NadeeshaMedagama/dev-choreo_architecture/actions/workflows/ci-cd.yml"><img src="https://github.com/NadeeshaMedagama/dev-choreo_architecture/actions/workflows/ci-cd.yml/badge.svg" alt="CI/CD Pipeline"></a>
  <a href="https://github.com/NadeeshaMedagama/dev-choreo_architecture/actions/workflows/docker-build-test.yml"><img src="https://github.com/NadeeshaMedagama/dev-choreo_architecture/actions/workflows/docker-build-test.yml/badge.svg" alt="Docker Build"></a>
  <a href="https://dev-choreo-architecture.netlify.app/"><img src="https://img.shields.io/badge/netlify-deployed-00C7B7?logo=netlify&logoColor=white" alt="Netlify"></a>
  <img src="https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

---

## 🌐 Live Demo

**👉 [https://dev-choreo-architecture.netlify.app/](https://dev-choreo-architecture.netlify.app/)**

Visit the live deployment to explore the interactive architecture diagram — no setup required.

---

## 📖 Overview

This repository contains the **interactive system architecture diagram** for [DevChoreo](https://github.com/NadeeshaMedagama) — an AI-powered Retrieval-Augmented Generation (RAG) assistant purpose-built for the [WSO2 Choreo](https://wso2.com/choreo/) platform.

The architecture diagram is a self-contained HTML file that visualizes the complete system design including:

- **Frontend Layer** — React 18 + Vite + Tailwind CSS
- **Backend API Gateway** — FastAPI + Python 3.12+ + Uvicorn ASGI
- **Core Services** — AI & RAG Pipeline, Data Processing, Quality & Validation
- **External Cloud Services** — Azure OpenAI, Milvus Cloud, GitHub API, Google Vision
- **Observability Stack** — Prometheus, Grafana, Alertmanager

---

## 🚀 Quick Start

### View Locally

Simply open the HTML file in your browser:

```bash
# Open directly in browser
open architecture-diagram.html        # macOS
xdg-open architecture-diagram.html    # Linux
start architecture-diagram.html       # Windows
```

### Docker

Serve the diagram using a lightweight nginx container:

```bash
# Build the image
docker build -t devchoreo-architecture .

# Run the container
docker run -p 8080:80 devchoreo-architecture

# Visit http://localhost:8080
```

---

## 🏗️ Architecture Overview

The diagram visualizes the following layers:

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
└──────┬──────┘ └─────┬──────┘ └────┬──────────┘
       │              │              │
┌──────▼──────────────▼──────────────▼────────────────────┐
│              EXTERNAL CLOUD SERVICES                    │
│  Azure OpenAI · Milvus Cloud · GitHub API · Google OCR  │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
DevChoreo_Architecture/
├── architecture-diagram.html   # Main architecture diagram (interactive HTML)
├── Dockerfile                  # nginx container to serve the diagram
├── action.yml                  # GitHub Action definition
├── README.md                   # This file
└── .github/
    └── workflows/
        ├── ci-cd.yml               # CI/CD pipeline
        ├── docker-build-test.yml   # Docker build & health checks
        ├── codeql.yml              # Security scanning
        ├── publish.yml             # Publish to GHCR
        ├── release.yml             # Release management
        └── dependency-updates.yml  # Dependabot auto-merge
```

---

## 🐳 Docker

The Dockerfile uses **nginx:alpine** to serve the architecture diagram as a static HTML page:

- **Base Image**: `nginx:alpine` (minimal ~8MB)
- **Port**: 80
- **Health Check**: Built-in wget health check
- **Content**: Serves `architecture-diagram.html` at `/`

---

## 🔄 CI/CD

| Workflow | Description |
|----------|-------------|
| **CI/CD Pipeline** | Validates HTML and builds Docker image |
| **Docker Build & Test** | Build, push to Docker Hub, and health checks |
| **CodeQL Analysis** | Automated security scanning |
| **Release Management** | Tag-based releases with changelog |
| **Publish to GHCR** | Multi-platform Docker image publishing |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>DevChoreo Architecture v1.0</strong> · February 2026<br>
  Interactive System Architecture Visualization
</p>

