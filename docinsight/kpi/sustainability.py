from __future__ import annotations

from typing import Any

DEFAULT_ELECTRICITY_EMISSION_FACTOR = 0.233  # kg CO2e per kWh


def compute_sustainability_kpis(data: dict[str, Any]) -> dict[str, Any]:
    """
    Compute simple sustainability KPIs from normalized sustainability data.
    """
    electricity_kwh = float(data.get("electricity_kwh") or 0.0)
    water_m3 = float(data.get("water_m3") or 0.0)
    waste_kg = float(data.get("waste_kg") or 0.0)
    cost_gbp = float(data.get("cost_gbp") or 0.0)

    estimated_co2_kg = electricity_kwh * DEFAULT_ELECTRICITY_EMISSION_FACTOR

    return {
        "total_energy_kwh": electricity_kwh,
        "total_water_m3": water_m3,
        "total_waste_kg": waste_kg,
        "total_cost_gbp": cost_gbp,
        "estimated_co2_kg": round(estimated_co2_kg, 2),
    }