import asyncio
import hashlib

from pydantic import BaseModel
import random

CATEGORIES = ["pii", "phi", "jailbreak", "finance", "security", "violence"]


class CategoryDetection(BaseModel):
    category: str
    detected: bool


async def detect_category(category: str, prompt: str) -> CategoryDetection:
    """
    This is a stub implementation, not relevant for the interview
    """
    detected = hashlib.md5((category + prompt).encode('utf-8')).digest()[0] % 3 != 0
    time_to_sleep = random.random() * 5
    await asyncio.sleep(time_to_sleep)
    return CategoryDetection(category=category, detected=detected)
