from fastapi import FastAPI
from api_server.routers.detect import detect_router

app = FastAPI()
app.include_router(detect_router)


@app.get("/ping")
def ping() -> str:
    return "pong"
