from pprint import pprint

from docinsight.batch import run_batch_pipeline
from docinsight.reporting import build_kpi_dataframe
from docinsight.exporters import save_json


def main() -> None:
    results = run_batch_pipeline("data/samples")

    print("=== FIRST DOCUMENT RESULT ===")
    pprint(results[0]["normalized"])
    pprint(results[0]["kpis"])

    df = build_kpi_dataframe(results)

    print("\n=== KPI DATAFRAME ===")
    print(df.to_string(index=False))

    save_json(results, "outputs/pipeline_results.json")


if __name__ == "__main__":
    main()