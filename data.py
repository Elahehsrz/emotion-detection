import PyPDF2
import fitz  # PyMuPDF
from PyPDF2 import PdfReader
import json

def extract_text_with_page_numbers(pdf_path, json_output_path):
    """
    Extracts text from each page of the PDF and saves it in a JSON file with page numbers and corresponding text.
    
    Args:
    pdf_path (str): The path to the PDF file.
    json_output_path (str): The path to save the JSON file.
    """
    pdf_text = {
        "pages": {}  # To store text with page numbers
    }

    # Using PyMuPDF
    document = fitz.open(pdf_path)
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text()
        pdf_text["pages"][f"Page {page_num + 1} (PyMuPDF)"] = text
    document.close()

    # Using PyPDF2
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            pdf_text["pages"][f"Page {page_num + 1} (PyPDF2)"] = text

    # Save the text to a JSON file
    with open(json_output_path, "w", encoding="utf-8") as json_file:
        json.dump(pdf_text, json_file, ensure_ascii=False, indent=4)

    print(f"Text extracted and saved to {json_output_path}")


def extract_all_text_as_list(pdf_path):
    """
    Extracts all text from the PDF and returns it as a list containing one element with all the text combined.
    
    Args:
    pdf_path (str): The path to the PDF file.
    
    Returns:
    list: A list containing one element with all the text combined.
    """
    all_text = []

    # Using PyMuPDF
    document = fitz.open(pdf_path)
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text()
        all_text.append(text)
    document.close()

    # Using PyPDF2
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            all_text.append(text)

    # Combine all text into one single string and add it as one element to the list
    combined_text = "\n".join(all_text)
    return [combined_text]




def write_results_to_file(results, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(str(results))



