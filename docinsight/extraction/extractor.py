import re
from typing import Any, Dict


def _extract_number(pattern: str, text: str) -> float | None:
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        return None
    return float(match.group(1))


def _extract_text(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        return None
    return match.group(1).strip()


def extract_sustainability_fields(text: str) -> Dict[str, Any]:
    """
    Extract sustainability-related fields from a semi-structured document.
    """
    return {
        "supplier": _extract_text(r"Supplier:\s*(.+)", text),
        "site": _extract_text(r"Site:\s*(.+)", text),
        "billing_period": _extract_text(r"Billing Period:\s*(.+)", text),
        "electricity_kwh": _extract_number(r"Electricity Consumption:\s*([\d.]+)\s*kWh", text),
        "water_m3": _extract_number(r"Water Usage:\s*([\d.]+)\s*m3", text),
        "waste_kg": _extract_number(r"Waste Collected:\s*([\d.]+)\s*kg", text),
        "cost_gbp": _extract_number(r"Total Cost:\s*£\s*([\d.]+)", text),
    }