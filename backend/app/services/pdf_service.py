from email.mime import text

import fitz


def extract_text(file_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path: Path to the uploaded PDF.

    Returns:
        Extracted text as a string.
    """
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text

    return text