# Copyright (C) 2024 Arun Puram
# Licensed under the GPL-3.0 License.
# Created for Utils: https://github.com/afadeofred/Utils

import os
import sys
import tempfile
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def convert_images_to_pdf(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)
    # Filter jpeg files
    jpeg_files = [file for file in files if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg') or file.lower().endswith('.png')]]

    # Loop through jpeg files
    for filename in jpeg_files:
        # Open image
        img = Image.open(os.path.join(input_folder, filename))
        # Convert image to RGB (if it's not already in RGB mode)
        img = img.convert('RGB')

        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpgeg','.png' delete=False)
        temp_file_path = temp_file.name
        img.save(temp_file_path)

        # Create PDF file
        pdf_filename = os.path.splitext(filename)[0] + '.pdf'
        pdf_path = os.path.join(output_folder, pdf_filename)
        c = canvas.Canvas(pdf_path, pagesize=A4  
        width, height = letter
        c.drawImage(temp_file_path, 0, 0, width, height)
        c.save()

        # Close and remove temporary file
        temp_file.close()
        os.unlink(temp_file_path)

        print(f"Converted {filename} to {pdf_filename}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing JPEG files: ")
    output_folder = input("Enter the path to the output folder where PDF files will be saved: ")

    convert_images_to_pdf(input_folder, output_folder)
