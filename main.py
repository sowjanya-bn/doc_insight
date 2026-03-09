from pprint import pprint

from docinsight.ingestion.loader import load_text_file
from docinsight.extraction.extractor import extract_sustainability_fields
from docinsight.normalization.cleaner import normalize_extracted_data
from docinsight.kpi.sustainability import compute_sustainability_kpis


def main() -> None:
    file_path = "data/samples/energy_bill.txt"

    raw_text = load_text_file(file_path)
    extracted = extract_sustainability_fields(raw_text)
    normalized = normalize_extracted_data(extracted)
    kpis = compute_sustainability_kpis(normalized)

    print("=== NORMALIZED FIELDS ===")
    pprint(normalized)

    print("\n=== COMPUTED KPIS ===")
    pprint(kpis)


if __name__ == "__main__":
    main()