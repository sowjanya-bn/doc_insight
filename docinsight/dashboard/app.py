from __future__ import annotations

import streamlit as st

from docinsight.batch import run_batch_pipeline
from docinsight.reporting import build_kpi_dataframe

st.set_page_config(page_title="DocInsight Dashboard", layout="wide")

st.title("DocInsight")
st.caption("Document Intelligence for Sustainability Reporting")

uploaded_file = st.file_uploader("Upload sustainability document", type=["txt"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    from docinsight.extraction.extractor import extract_sustainability_fields
    from docinsight.normalization.cleaner import normalize_extracted_data
    from docinsight.kpi.sustainability import compute_sustainability_kpis

    extracted = extract_sustainability_fields(content)
    normalized = normalize_extracted_data(extracted)
    kpis = compute_sustainability_kpis(normalized)

    st.subheader("Extracted Data")
    st.json(normalized)

    st.subheader("Computed KPIs")
    st.json(kpis)

results = run_batch_pipeline("data/samples")
df = build_kpi_dataframe(results)

total_energy = float(df["electricity_kwh"].sum())
total_water = float(df["water_m3"].sum())
total_waste = float(df["waste_kg"].sum())
total_cost = float(df["cost_gbp"].sum())
total_co2 = float(df["estimated_co2_kg"].sum())

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Energy (kWh)", f"{total_energy:,.0f}")
col2.metric("Total Water (m³)", f"{total_water:,.0f}")
col3.metric("Total Waste (kg)", f"{total_waste:,.0f}")
col4.metric("Total Cost (£)", f"{total_cost:,.2f}")
col5.metric("Estimated CO₂ (kg)", f"{total_co2:,.2f}")

st.markdown("---")

st.subheader("Monthly KPI Data")
st.dataframe(df, use_container_width=True)

trend_df = df.set_index("billing_period")

st.subheader("Energy Trend")
st.line_chart(trend_df["electricity_kwh"])

st.subheader("Water Trend")
st.line_chart(trend_df["water_m3"])

st.subheader("Waste Trend")
st.line_chart(trend_df["waste_kg"])

st.subheader("Cost Trend")
st.line_chart(trend_df["cost_gbp"])

st.subheader("Estimated CO₂ Trend")
st.line_chart(trend_df["estimated_co2_kg"])

st.subheader("Key Insight")

energy_change = df["electricity_kwh"].iloc[-1] - df["electricity_kwh"].iloc[0]

if energy_change > 0:
    st.warning(f"Energy usage increased by {energy_change:.0f} kWh over the observed period.")
else:
    st.success(f"Energy usage decreased by {-energy_change:.0f} kWh over the observed period.")