from pathlib import Path


def load_text_file(file_path: str) -> str:
    """
    Load and return the contents of a plain text file.

    Args:
        file_path: Path to the input text file.

    Returns:
        File contents as a string.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Not a valid file: {file_path}")

    return path.read_text(encoding="utf-8").strip()