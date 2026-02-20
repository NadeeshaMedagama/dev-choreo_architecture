# ============================================================================
# DevChoreo Architecture — Dockerfile
# ============================================================================
# Lightweight nginx container to serve the architecture diagram HTML file.
# ============================================================================

FROM nginx:alpine

ARG VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

# OCI image labels
LABEL org.opencontainers.image.title="DevChoreo Architecture" \
      org.opencontainers.image.description="System Architecture Diagram for DevChoreo — AI-Powered RAG Assistant for WSO2 Choreo Platform" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.vendor="DevChoreo" \
      org.opencontainers.image.source="https://github.com/NadeeshaMedagama/dev-choreo_architecture"

# Copy the architecture diagram to nginx's default serve directory
COPY architecture-diagram.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:80/ || exit 1
