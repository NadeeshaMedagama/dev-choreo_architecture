# ============================================================================
# DevChoreo — Dockerfile
# ============================================================================
# Multi-stage build for the FastAPI backend with Python 3.12-slim base.
# Produces a minimal, secure production image.
# ============================================================================

# ── Stage 1: Builder ────────────────────────────────────────
FROM python:3.12-slim AS builder

ARG VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

WORKDIR /build

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt* ./
RUN mkdir -p /install && \
    if [ -f requirements.txt ]; then \
        pip install --no-cache-dir --prefix=/install -r requirements.txt; \
    fi

# ── Stage 2: Production ────────────────────────────────────
FROM python:3.12-slim AS production

ARG VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

# OCI image labels
LABEL org.opencontainers.image.title="DevChoreo" \
      org.opencontainers.image.description="AI-Powered RAG Assistant for WSO2 Choreo Platform" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.vendor="DevChoreo" \
      org.opencontainers.image.source="https://github.com/NadeeshaMedagama/dev-choreo_architecture"

# Create non-root user
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy application source
COPY --chown=appuser:appuser . .

# Remove unnecessary files from the image
RUN rm -rf .git .github .idea .venv __pycache__ \
           tests frontend .env *.md .dockerignore \
           Dockerfile docker-compose*.yml

# Environment configuration
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_ENV=production \
    LOG_LEVEL=INFO \
    PORT=8000

# Expose the application port
EXPOSE ${PORT}

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT}/api/health')" || exit 1

# Start the application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

