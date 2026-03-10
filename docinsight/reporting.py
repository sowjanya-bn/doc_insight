from __future__ import annotations

from typing import Any

import pandas as pd


def build_kpi_dataframe(results: list[dict[str, Any]]) -> pd.DataFrame:
    rows = []

    for result in results:
        normalized = result["normalized"]
        kpis = result["kpis"]

        rows.append(
            {
                "billing_period": normalized.get("billing_period"),
                "supplier": normalized.get("supplier"),
                "site": normalized.get("site"),
                "electricity_kwh": normalized.get("electricity_kwh"),
                "water_m3": normalized.get("water_m3"),
                "waste_kg": normalized.get("waste_kg"),
                "cost_gbp": normalized.get("cost_gbp"),
                "estimated_co2_kg": kpis.get("estimated_co2_kg"),
            }
        )

    df = pd.DataFrame(rows)
    df["billing_period"] = pd.to_datetime(df["billing_period"])
    df = df.sort_values("billing_period").reset_index(drop=True)
    return df