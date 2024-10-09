"""
This file handles the document embeddings (splitting and storing chunks).
"""
import os
from docx import Document

def read_document(file_path):
    if os.path.exists(file_path):
        doc = Document(file_path)
        text = [para.text for para in doc.paragraphs]
        return "\n".join(text)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist")

def split_into_chunks(text, chunk_size=100):
    #TODO: split into chunks in smart way
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

if __name__ == "__main__":
    # Test reading and splitting document
    file_path = ".\data\documento.docx"
    text = read_document(file_path)
    chunks = split_into_chunks(text)
    print(f"Total chunks: {len(chunks)}")
    # Print first 3 chunks to test
    for i, chunk in enumerate(chunks[:3], 1):  
        print(f"Chunk {i}:\n{chunk}\n")
