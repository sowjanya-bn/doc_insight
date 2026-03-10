from __future__ import annotations

from typing import Any

from docinsight.ingestion.loader import load_text_file
from docinsight.extraction.extractor import extract_sustainability_fields
from docinsight.normalization.cleaner import normalize_extracted_data
from docinsight.kpi.sustainability import compute_sustainability_kpis
from docinsight.extraction.router import extract_with_fallback


def run_sustainability_pipeline(file_path: str) -> dict[str, Any]:
    raw_text = load_text_file(file_path)
    extracted = extract_with_fallback(raw_text)
    normalized = normalize_extracted_data(extracted)
    kpis = compute_sustainability_kpis(normalized)

    return {
        "file_path": file_path,
        "raw_text": raw_text,
        "extracted": extracted,
        "normalized": normalized,
        "kpis": kpis,
    }