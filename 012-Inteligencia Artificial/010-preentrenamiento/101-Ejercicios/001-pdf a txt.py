import sys
import pdfplumber

pdf_path = sys.argv[1]
txt_path = sys.argv[2]

with pdfplumber.open(pdf_path) as pdf:
    with open(txt_path, "w", encoding="utf-8") as f:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                f.write(text + "\n")
