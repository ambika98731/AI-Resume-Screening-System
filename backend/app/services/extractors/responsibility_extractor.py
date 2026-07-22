import re


def extract_responsibilities(text: str) -> list[str]:
    """
    Extract bullet-point responsibilities from a Job Description.
    """

    responsibilities = []

    lines = text.splitlines()

    capture = False

    for line in lines:

        lower = line.lower().strip()

        if "responsibilit" in lower:
            capture = True
            continue

        if capture:

            if not lower:
                break

            cleaned = line.strip()

            if cleaned.startswith(("-", "•", "*")):
                cleaned = cleaned.lstrip("-•* ").strip()

            responsibilities.append(cleaned)

    return responsibilities