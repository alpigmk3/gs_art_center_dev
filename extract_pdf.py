import sys
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF is not installed. Please install it first.")
    sys.exit(1)

pdf_path = "c:/WORK/gs_art_center-2026-05-08-17-27-21/gs_art_center/GS아트센터_좌석시야 서비스_화면 기능 및 디자인(안).pdf"
output_path = "c:/WORK/gs_art_center-2026-05-08-17-27-21/gs_art_center/pdf_extracted.txt"

if not os.path.exists(pdf_path):
    print(f"Error: File not found at {pdf_path}")
    sys.exit(1)

text_content = []
doc = fitz.open(pdf_path)
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    text_content.append(f"--- Page {page_num + 1} ---\n{text}")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(text_content))

print(f"Extraction successful. Saved to {output_path}")
