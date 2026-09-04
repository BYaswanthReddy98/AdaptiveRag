from app.services.pdf_parser import extract_text_from_pdf

pdf_path = "BDA UNIT 2 - Sami.pdf"

text = extract_text_from_pdf(pdf_path)

print(text[:2000])