from pprint import pprint

from docinsight.ingestion.loader import load_text_file
from docinsight.extraction.extractor import extract_sustainability_fields


def main() -> None:
    file_path = "data/samples/energy_bill.txt"

    raw_text = load_text_file(file_path)
    extracted = extract_sustainability_fields(raw_text)

    print("=== EXTRACTED FIELDS ===")
    pprint(extracted)


if __name__ == "__main__":
    main()