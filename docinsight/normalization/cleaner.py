from __future__ import annotations

from datetime import datetime
from typing import Any


def normalize_billing_period(value: str | None) -> str | None:
    """
    Convert billing periods like 'January 2026' into '2026-01'.
    """
    if not value:
        return None

    try:
        parsed = datetime.strptime(value.strip(), "%B %Y")
        return parsed.strftime("%Y-%m")
    except ValueError:
        return value.strip()


def normalize_extracted_data(data: dict[str, Any]) -> dict[str, Any]:
    """
    Normalize extracted sustainability fields into a cleaner schema.
    """
    normalized = data.copy()
    normalized["billing_period"] = normalize_billing_period(data.get("billing_period"))
    return normalized