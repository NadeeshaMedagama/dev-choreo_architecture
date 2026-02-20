# ============================================================================
# DevChoreo — Main Application Entry Point
# ============================================================================
# FastAPI application with health check, metrics, and API endpoints.
# ============================================================================

import os
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse

# ── Application Metadata ────────────────────────────────────
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")
START_TIME = time.time()


# ── Lifespan ────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown events."""
    print(f"🚀 DevChoreo v{APP_VERSION} starting in {APP_ENV} mode...")
    yield
    print("👋 DevChoreo shutting down...")


# ── FastAPI App ─────────────────────────────────────────────
app = FastAPI(
    title="DevChoreo",
    description="AI-Powered RAG Assistant for WSO2 Choreo Platform",
    version=APP_VERSION,
    docs_url="/docs" if APP_ENV != "production" else None,
    redoc_url="/redoc" if APP_ENV != "production" else None,
    lifespan=lifespan,
)

# ── CORS Middleware ─────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Metrics (simple counter-based) ──────────────────────────
_metrics = {
    "requests_total": 0,
    "requests_failed": 0,
}


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    """Track request metrics."""
    _metrics["requests_total"] += 1
    try:
        response = await call_next(request)
        if response.status_code >= 400:
            _metrics["requests_failed"] += 1
        return response
    except Exception:
        _metrics["requests_failed"] += 1
        raise


# ── Health Check ────────────────────────────────────────────
@app.get("/api/health")
async def health_check():
    """Health check endpoint for container orchestration."""
    uptime = time.time() - START_TIME
    return JSONResponse(
        content={
            "status": "healthy",
            "version": APP_VERSION,
            "environment": APP_ENV,
            "uptime_seconds": round(uptime, 2),
        }
    )


# ── Prometheus Metrics ──────────────────────────────────────
@app.get("/metrics")
async def metrics():
    """Prometheus-compatible metrics endpoint."""
    uptime = time.time() - START_TIME
    lines = [
        "# HELP devchoreo_up Whether the DevChoreo service is up.",
        "# TYPE devchoreo_up gauge",
        "devchoreo_up 1",
        "",
        "# HELP devchoreo_uptime_seconds Time since the service started.",
        "# TYPE devchoreo_uptime_seconds gauge",
        f"devchoreo_uptime_seconds {uptime:.2f}",
        "",
        "# HELP devchoreo_requests_total Total number of HTTP requests.",
        "# TYPE devchoreo_requests_total counter",
        f'devchoreo_requests_total {_metrics["requests_total"]}',
        "",
        "# HELP devchoreo_requests_failed_total Total number of failed HTTP requests.",
        "# TYPE devchoreo_requests_failed_total counter",
        f'devchoreo_requests_failed_total {_metrics["requests_failed"]}',
        "",
    ]
    return PlainTextResponse("\n".join(lines), media_type="text/plain")


# ── API Placeholder Endpoints ───────────────────────────────
@app.post("/api/ask")
async def ask(request: Request):
    """Process a user query and return a complete response."""
    body = await request.json()
    return JSONResponse(
        content={
            "response": "DevChoreo is running. Connect AI services to enable full RAG functionality.",
            "query": body.get("query", ""),
            "sources": [],
        }
    )


@app.post("/api/ask/stream")
async def ask_stream(request: Request):
    """Stream a response via SSE for a user query."""
    body = await request.json()
    return JSONResponse(
        content={
            "response": "Streaming endpoint ready. Connect AI services to enable SSE streaming.",
            "query": body.get("query", ""),
        }
    )


@app.post("/api/ask_graph")
async def ask_graph(request: Request):
    """Multi-step graph-based RAG query."""
    body = await request.json()
    return JSONResponse(
        content={
            "response": "Graph RAG endpoint ready. Connect LangGraph to enable multi-step reasoning.",
            "query": body.get("query", ""),
        }
    )


@app.post("/api/ingest/github")
async def ingest_github(request: Request):
    """Ingest documentation from a GitHub repository."""
    body = await request.json()
    return JSONResponse(
        content={
            "status": "ready",
            "message": "Ingestion endpoint ready. Connect services to enable GitHub ingestion.",
            "repo_url": body.get("repo_url", ""),
        }
    )


@app.post("/api/ingest/org")
async def ingest_org(request: Request):
    """Bulk ingest all repos from a GitHub organization."""
    body = await request.json()
    return JSONResponse(
        content={
            "status": "ready",
            "message": "Organization ingestion endpoint ready.",
            "org": body.get("org", ""),
        }
    )


@app.post("/api/webhook/github")
async def webhook_github(request: Request):
    """GitHub webhook endpoint for auto-ingestion."""
    return JSONResponse(
        content={
            "status": "received",
            "message": "Webhook endpoint ready.",
        }
    )

