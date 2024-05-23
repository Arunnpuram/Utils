# Copyright (C) 2024 Arun Puram
# Licensed under the GPL-3.0 License.
# Created for Utils: https://github.com/afadeofred/Utils

import os
import re
import argparse import ArgumentParser

def sort_pdfs(folder_path):
  """
  Sorts PDF files in a folder by first and last name extracted from the filename.

  Args:
      folder_path (str): Path to the folder containing PDF files.
  """
  for filename in os.listdir(folder_path):
    if not filename.endswith(".pdf"):
      continue

    # Extract first and last name using regular expression
    match = re.search(r"(?P<first_name>\w+)_(?P<last_name>\w+)\.pdf", filename, re.IGNORECASE)
    if not match:
      # Skip files without matching format
      continue

    first_name = match.group("first_name")
    last_name = match.group("last_name")

    # Create a new filename with only first and last name
    new_filename = f"{first_name}_{last_name}.pdf"

    # Rename the file (optional, comment out if you only want sorted list)
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

  # Sort the list of files based on the new filename (assuming renaming is done)
  sorted_files = sorted(os.listdir(folder_path))

  # Print the sorted list of filenames
  print("Sorted filenames:")
  for filename in sorted_files:
    print(filename)

if __name__ == "__main__":
  # Parse arguments
  parser = ArgumentParser(description="Sort PDF files by first and last name in filename.")
  parser.add_argument("folder_path", type=str, help="Path to the folder containing PDF files.")
  args = parser.parse_args()

  # Call the sort function with the parsed folder path
  sort_pdfs(args.folder_path)
