import os
import PyPDF2
import argparse

def count_pdf_pages(folder_path):
    total_pages = 0
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages += len(pdf_reader.pages)
    return total_pages

def main():
    parser = argparse.ArgumentParser(description='To Count the total number of pages in PDF files within a folder.')
    parser.add_argument('folder_path', type=str)
    args = parser.parse_args()
    
    total_pages = count_pdf_pages(args.folder_path)
    print("Total number of pages in all PDF files:", total_pages)

if __name__ == "__main__":
    main()