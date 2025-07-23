# -------------------------
# 1) Builder stage
# -------------------------
FROM python:3.11-slim AS builder

# Install uv CLI
COPY --from=ghcr.io/astral-sh/uv:0.7.19 /uv /bin/uv

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      git \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/project

# Copy only lockfiles, create venv and install deps
COPY pyproject.toml uv.lock ./
RUN uv venv \
 && uv sync --frozen --no-install-project

COPY src/ src/

# -------------------------
# 2) Runner stage
# -------------------------
FROM python:3.11-slim AS runner

WORKDIR /opt/project

# Copy the prepared virtualenv and app files
COPY --from=builder /opt/project/src ./src
COPY --from=builder /opt/project/.venv .venv

ENV PATH="/opt/project/.venv/bin:$PATH"
ENV PYTHONPATH=src
EXPOSE 1234

CMD ["uvicorn", "almacen:app", "--port", "1234", "--host", "0.0.0.0"]

