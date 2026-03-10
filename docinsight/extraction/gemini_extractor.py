from __future__ import annotations

import json
from typing import Any

from google import genai
from google.genai import types

client = genai.Client()

SYSTEM_PROMPT = """
Extract sustainability data from the document.

Return ONLY valid JSON with the following fields:

{
  "supplier": string or null,
  "site": string or null,
  "billing_period": string or null,
  "electricity_kwh": number or null,
  "water_m3": number or null,
  "waste_kg": number or null,
  "cost_gbp": number or null
}

Rules:
- Remove units from numbers
- Do not invent values
- Use null if not present
"""

def extract_sustainability_fields_llm(text: str) -> dict[str, Any]:

    config = types.GenerateContentConfig(
        #thinking_level="MINIMAL",
        temperature=0.0
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=f"{SYSTEM_PROMPT}\n\nDocument:\n{text}",
        config=config
    )

    content = response.text.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Gemini output was not valid JSON:\n{content}")