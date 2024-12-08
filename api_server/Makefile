install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync

run:
	uv run uvicorn --host 0.0.0.0 --port 8000 api_server.server:app
