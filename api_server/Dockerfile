FROM python:3.12.4-slim AS prod

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN groupadd -r aim && useradd --no-log-init -r -m -g aim aim

RUN mkdir -p api_server/api_server && chown -R aim:aim api_server
WORKDIR /app/api_server

RUN touch api_server/__init__.py README.md

COPY --chown=aim:aim pyproject.toml /app/api_server/

USER aim

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

COPY --chown=aim api_server /app/api_server/api_server

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "api_server.server:app", "--host", "0.0.0.0", "--port", "8000"]