import fitz  # PyMuPDF
import docx2txt
import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Extract text from PDF
def extract_pdf_text(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

# Extract text from DOCX
def extract_docx_text(file_path):
    return docx2txt.process(file_path)

# Extract text based on file type
def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)  # Use PDF extraction function
    elif file_path.endswith(".docx"):
        return extract_docx_text(file_path)  # Use DOCX extraction function
    return ""

# Highlight keywords in the text
def highlight_keywords(text, keywords):
    for kw in keywords:
        highlighted = f"<span style='background-color: yellow'>{kw}</span>"
        text = re.sub(f"\\b{re.escape(kw)}\\b", highlighted, text, flags=re.IGNORECASE)
    return text

# Search keywords in the resume
def search_keywords(file_path, keywords):
    text = extract_text(file_path).lower()  # Extract and lowercase the text
    matched = []  # List to store matched keywords

    for kw in keywords:
        if kw.lower() in text:  # Check if keyword is in the text
            matched.append(kw)

    return matched, text  # Return matched keywords and the original text (to highlight keywords)
