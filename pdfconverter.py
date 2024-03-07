import os
import PyPDF2

def convert_pdf_to_text(pdf_file_path, text_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

def convert_pdfs_in_directory(pdf_directory, text_directory):
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)

    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(pdf_directory, filename)
            text_file_path = os.path.join(text_directory, filename.replace('.pdf', '.txt'))
            convert_pdf_to_text(pdf_file_path, text_file_path)
            print(f"Converted {pdf_file_path} to {text_file_path}")

pdf_directory = "docs/all"
text_directory = "docs/textfiles"


convert_pdfs_in_directory(pdf_directory, text_directory)