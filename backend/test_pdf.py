from app.services.pdf_service import extract_text
from app.services.parser_service import parse_resume

pdf_path = "app/uploads/881159f3-c0c9-4b68-9e3a-10d2beac107b.pdf"

text = extract_text(pdf_path)

result = parse_resume(text)

print(result)