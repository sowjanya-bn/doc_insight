from __future__ import annotations

import json
import os
from typing import Any

from google import genai

SYSTEM_PROMPT = """
You extract sustainability data from semi-structured business documents.

Return only valid JSON with these fields:
- supplier: string or null
- site: string or null
- billing_period: string or null
- electricity_kwh: number or null
- water_m3: number or null
- waste_kg: number or null
- cost_gbp: number or null

Rules:
- Do not invent values
- Use null if missing
- Strip units from numeric values
- Keep billing_period exactly as written
"""

def extract_sustainability_fields_llm(text: str) -> dict[str, Any]:
    api_key = os.environ["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

    prompt = f"""
{SYSTEM_PROMPT}

Document:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    content = response.text.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Gemini did not return valid JSON. Output was: {content}") from e