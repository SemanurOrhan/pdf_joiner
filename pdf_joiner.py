from PyPDF2 import PdfMerger
import os

# PDF dosyalarının sırayla listesi
pdf_list = [
    "1_2.pdf",
    "3.pdf",
    "4.pdf",
    "5.pdf",
    "6.pdf",
    "7.pdf",
]

merger = PdfMerger()

for pdf in pdf_list:
    merger.append(pdf)

# Çıktı dosyası
output_name = "merged.pdf"
merger.write(output_name)
merger.close()

print(f"PDF'ler birleştirildi: {output_name}")
