import asyncio

from fastapi import APIRouter
from pydantic import BaseModel

from api_server.routers.categories import CATEGORIES, detect_category, CategoryDetection

detect_router = APIRouter(prefix="/detect", tags=["detections"])


class AnalyzePromptRequest(BaseModel):
    prompt: str


class AnalyzePromptResponse(BaseModel):
    results: list[CategoryDetection]


@detect_router.post("/analyze-prompt")
async def analyze_prompt(
    analyze_request: AnalyzePromptRequest,
) -> AnalyzePromptResponse:
    results = await asyncio.gather(
        *[
            detect_category(category=category, prompt=analyze_request.prompt)
            for category in CATEGORIES
        ]
    )
    return AnalyzePromptResponse(results=results)
