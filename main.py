from pprint import pprint

from docinsight.pipeline import run_sustainability_pipeline


def main() -> None:
    result = run_sustainability_pipeline("data/samples/energy_bill.txt")

    print("=== EXTRACTED FIELDS ===")
    pprint(result["extracted"])

    print("\n=== NORMALIZED FIELDS ===")
    pprint(result["normalized"])

    print("\n=== COMPUTED KPIS ===")
    pprint(result["kpis"])


if __name__ == "__main__":
    main()