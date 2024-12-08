IMAGE_NAME = "workshop/echo_server"
IMAGE_TAG = "1.0.0"
FULL_IMAGE_NAME = ${IMAGE_NAME}:${IMAGE_TAG}

install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync

run:
	uv run uvicorn --host 0.0.0.0 --port 8000 api_server.server:app

build:
	docker build -t ${FULL_IMAGE_NAME} .

run-docker:
	docker run -p 8000:8000 {FULL_IMAGE_NAME}
