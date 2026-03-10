# DocInsight

DocInsight is a lightweight **document intelligence pipeline** that
extracts structured sustainability data from semi‑structured operational
documents and converts it into actionable environmental KPIs and
dashboards.

The system demonstrates how AI‑assisted document processing can automate
sustainability reporting by transforming utility documents such as
energy bills, water reports and waste invoices into structured datasets
suitable for analytics and monitoring.

------------------------------------------------------------------------

# Problem

Many organisations track environmental performance using operational
documents such as:

-   Utility bills
-   Water usage reports
-   Waste collection summaries
-   Sustainability statements

These documents contain valuable information, but the data is usually
trapped in semi‑structured formats such as PDFs, reports or emails.

DocInsight demonstrates how a hybrid AI pipeline can automatically:

1.  Extract sustainability fields from documents
2.  Normalize them into a consistent schema
3.  Compute sustainability KPIs
4.  Visualize trends through a dashboard

------------------------------------------------------------------------

# Architecture

The system follows a modular document intelligence architecture:

Documents\
↓\
Document Loader\
↓\
Field Extraction (Regex)\
↓\
LLM Fallback Extraction (Gemini)\
↓\
Normalization\
↓\
KPI Engine\
↓\
Dashboard / Insights

This hybrid approach ensures:

-   deterministic extraction for predictable documents\
-   AI‑assisted extraction for variable formats\
-   consistent downstream analytics

------------------------------------------------------------------------

# Key Features

## Document Ingestion

Loads sustainability‑related documents from the filesystem.

Example input types:

-   utility bills
-   sustainability reports
-   environmental statements

------------------------------------------------------------------------

## Hybrid Field Extraction

DocInsight uses a **two‑stage extraction strategy**.

### Rule‑based extraction

Regex parsing handles structured documents quickly and cheaply.

### LLM fallback extraction

When required fields are missing, the system calls **Google Gemini** to
extract structured fields from more complex documents.

This hybrid approach balances:

-   reliability
-   cost efficiency
-   robustness to format variations

------------------------------------------------------------------------

## Data Normalization

Extracted values are standardized to ensure consistent analytics.

Examples:

  Raw Value      Normalized
  -------------- ------------
  January 2026   2026‑01
  £620.50        620.5
  4250 kWh       4250

------------------------------------------------------------------------

## Sustainability KPI Engine

The system computes environmental KPIs such as:

-   total electricity consumption (kWh)
-   water usage (m³)
-   waste generated (kg)
-   operational cost (£)
-   estimated CO₂ emissions

Example formula:

CO₂ = electricity_kwh × emission_factor

------------------------------------------------------------------------

## Batch Processing

Multiple documents can be processed automatically to build a monthly
dataset suitable for trend analysis.

Example output:

  -----------------------------------------------------------------------
  Period      Energy      Water (m³)  Waste (kg)  Cost (£)    CO₂ (kg)
              (kWh)                                           
  ----------- ----------- ----------- ----------- ----------- -----------
  2026‑01     4250        18          120         620.5       990

  2026‑02     3980        16          105         590.2       927

  2026‑03     4410        19          128         645.8       1027

  2026‑04     4625        21          134         682.4       1077
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Dashboard Prototype

A lightweight **Streamlit dashboard** visualizes sustainability
performance trends including:

-   energy consumption
-   water usage
-   waste generation
-   cost trends
-   estimated CO₂ emissions

------------------------------------------------------------------------

# Project Structure

doc_insight/

├── pyproject.toml\
├── README.md\
├── main.py

docinsight/

├── ingestion/loader.py\
├── extraction/extractor.py\
├── extraction/gemini_extractor.py\
├── extraction/router.py\
├── normalization/cleaner.py\
├── kpi/sustainability.py\
├── batch.py\
├── reporting.py\
├── pipeline.py

data/

└── samples/

dashboard/

└── app.py

------------------------------------------------------------------------

# Setup

Clone the repository:

    git clone <repo_url>
    cd doc_insight

Create a virtual environment:

    python -m venv .docins
    source .docins/bin/activate

Install dependencies:

    pip install -e .

------------------------------------------------------------------------

# Running the Pipeline

    python main.py

This processes all sample documents and generates KPI outputs.

------------------------------------------------------------------------

# Running the Dashboard

    streamlit run docinsight/dashboard/app.py

The dashboard displays sustainability trends derived from processed
documents.

------------------------------------------------------------------------

# LLM Integration

DocInsight integrates **Google Gemini** for AI‑assisted extraction.

Set your API key:

    export GOOGLE_API_KEY="your_api_key"

Gemini is used only when deterministic parsing cannot extract required
fields.

------------------------------------------------------------------------

# Future Improvements

Possible extensions include:

-   PDF document ingestion
-   OCR support for scanned documents
-   structured LLM output validation
-   anomaly detection for sustainability metrics
-   predictive energy usage modelling
-   automated sustainability reports

------------------------------------------------------------------------

# License

MIT License



## Installation
bash
```
python3 -m venv .docins
source .docins/bin/activate
pip install -U pip
pip install -e .
```

## Usage
```bash
python main.py
streamlit run docinsight/dashboard/app.py
```