"""OpenAI vision calls to produce short alt-style descriptions for image URLs."""

import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

IMAGE_ALT_PROMPT = (
    "Give a short alt-text style description of this image."
)

_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def _user_content_for_url(url: str) -> list[dict]:
    return [
        {"type": "input_text", "text": IMAGE_ALT_PROMPT},
        {
            "type": "input_image",
            "image_url": url,
            "detail": "auto",
        },
    ]


async def _describe_image(url: str) -> str:
    response = await _client.responses.create(
        model="gpt-4o-mini",
        max_output_tokens=300,
        input=[
            {
                "role": "user",
                "content": _user_content_for_url(url),
            }
        ],
    )
    return response.output_text


async def generate_image_alts(image_urls: list[str]) -> list[str]:
    """Return one alt-text string per URL, in the same order (requests run concurrently)."""
    return list(await asyncio.gather(*(_describe_image(url) for url in image_urls)))
