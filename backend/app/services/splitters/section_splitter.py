from app.utils.resume_sections import SECTION_HEADERS


def split_sections(text: str):
    """
    Split resume text into logical sections.
    """

    lines = text.splitlines()

    sections = {
        "general": []
    }

    current_section = "general"

    # Normalize all keywords once
    normalized_headers = {}

    for section, keywords in SECTION_HEADERS.items():
        normalized_headers[section] = [
            keyword.lower()
                   .replace("&", " ")
                   .replace("/", " ")
                   .strip()
            for keyword in keywords
        ]

    # Process resume line by line
    for line in lines:

        clean = line.strip()

        if not clean:
            continue

        normalized_line = (
            clean.lower()
                 .replace("&", " ")
                 .replace("/", " ")
                 .strip()
        )

        matched = False

        # Check if current line is a section heading
        for section, keywords in normalized_headers.items():

            if normalized_line in keywords:

                current_section = section

                if current_section not in sections:
                    sections[current_section] = []

                matched = True
                break

        # If it is not a heading, add it to current section
        if not matched:
            sections[current_section].append(clean)

    # Convert lists to strings
    for section in sections:
        sections[section] = "\n".join(sections[section])

    return sections