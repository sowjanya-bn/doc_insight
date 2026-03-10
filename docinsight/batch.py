from __future__ import annotations

from pathlib import Path
from typing import Any

from docinsight.pipeline import run_sustainability_pipeline


def run_batch_pipeline(samples_dir: str) -> list[dict[str, Any]]:
    base_path = Path(samples_dir)
    results: list[dict[str, Any]] = []

    for file_path in sorted(base_path.glob("*.txt")):
        result = run_sustainability_pipeline(str(file_path))
        results.append(result)

    return results