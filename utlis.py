import fitz  # PyMuPDF
from typing import List

def extract_text_from_pdf(file) -> str:
    text = ""
    try:
        with fitz.open(stream=file.file.read(), filetype='pdf') as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        raise Exception(f"Error reading PDF file: {e}")
    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks
