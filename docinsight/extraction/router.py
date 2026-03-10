from typing import Any

from docinsight.extraction.extractor import extract_sustainability_fields
from docinsight.extraction.gemini_extractor import extract_sustainability_fields_llm


REQUIRED_FIELDS = [
    "supplier",
    "site",
    "billing_period",
    "electricity_kwh",
    "cost_gbp",
]


def has_missing_fields(data: dict[str, Any]) -> bool:
    return any(data.get(field) is None for field in REQUIRED_FIELDS)


def extract_with_fallback(text: str) -> dict[str, Any]:

    regex_result = extract_sustainability_fields(text)

    if not has_missing_fields(regex_result):
        return regex_result

    print("Using Gemini extraction fallback...")

    return extract_sustainability_fields_llm(text)