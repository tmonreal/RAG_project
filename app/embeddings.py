"""
This file handles the document embeddings (splitting and storing chunks).
To view chunks and embeddings stored, run:
    py .\\app\\embeddings.py --view .\\data\\documento.docx
To only store in ChromaDB, run:
    py .\\app\\embeddings.py .\\data\\documento.docx
"""
import os
import argparse
import numpy as np
import chromadb
import chromadb.config
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

client = chromadb.Client(chromadb.config.Settings())
collection = client.create_collection('document_chunks')

model = SentenceTransformer('all-MiniLM-L6-v2')

def read_document(file_path):
    """
    Read the contents of a Word document.
    Parameters:
        - file_path: str: The path to the Word document.
    Returns:
        - str: The text content of the document.
    Raises:
        - FileNotFoundError: If the specified file does not exist.
        - ValueError: If the file is not a .docx file.
    """
    if not os.path.exists(file_path): 
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    if not file_path.lower().endswith(('.docx', '.doc')):
        raise ValueError(f"The file {file_path} is not a .docx or .doc file")
    
    # Read the contents of the .docx file
    doc = Document(file_path)
    text = [para.text for para in doc.paragraphs]
    return "\n".join(text)

def split_into_chunks(text):
    """
    Split the text into chunks based on paragraphs.
    Parameters:
        - text: str: The input text to be split into chunks.
    Returns:
        - list: A list of non-empty paragraphs from the input text.
    """
    paragraphs = text.strip().split('\n')
    chunks = [para for para in paragraphs if para.strip()] # Remove empty paragraphs
    return chunks

def store_chunks_in_chroma(chunks):
    """
    Store chunks and their embeddings in ChromaDB.
    Parameters:
        - chunks: list: A list of text chunks to be stored in ChromaDB.
    Returns: None
    Raises:
        - Exception: If there is an issue with embedding generation or storing in ChromaDB.
    """
    # Generate embeddings for each chunk using SentenceTransformer model
    embeddings = model.encode(chunks) 
    for i, chunk in enumerate(chunks):
        # Store in ChromaDB
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            ids=[f"chunk_{i}"]
        )
    print("Chunks stored in ChromaDB")

def view_stored_chunks():
    """
    Retrieve and display stored chunks and embeddings from ChromaDB.
    Parameters: None
    Returns: None
    Raises:
        - Exception: If there is an issue retrieving data from ChromaDB.
    """
    results = collection.get(include=['embeddings', 'documents', 'metadatas'])    
    if results:
        print("\nStored Document Chunks:")
        for i, doc in enumerate(results.get('documents', [])):
            print(f"Chunk {i+1}: {doc}")
        
        print("\nStored Embeddings (only printing first 5 values):")
        for i, embedding in enumerate(results.get('embeddings', [])):
            print(f"Embedding {i+1}: {embedding[:5]}...")
    else:
        print("No data retrieved from ChromaDB")

def check_embeddings_exist():
    """
    Check if embeddings already exist in the ChromaDB collection.
    Returns: bool: True if embeddings exist, False otherwise.
    """
    results = collection.get(include=['documents'])
    return len(results['documents']) > 0 if results else False

def create_embeddings(file_path):
    """
    Creates embeddings from the given file and stores them in ChromaDB.
    Parameters:
        - file_path: str: The path to the Word document.
    Returns: None
    """
    if not check_embeddings_exist():
        text = read_document(file_path)
        chunks = split_into_chunks(text)
        store_chunks_in_chroma(chunks)
    else:
        print("Embeddings already exist in ChromaDB.")

def get_context(question):
    """
    Retrieves the most relevant context from the ChromaDB collection based on the question.
    This function connects to a ChromaDB client, retrieves the stored document chunks and their embeddings,
    and computes the cosine similarity between the question embedding and the embeddings of the stored 
    document chunks. It returns the document that is most similar to the question.
    Parameters:
        question: str: The question for which relevant context is to be retrieved.
    Returns:
        str: The most relevant document from the ChromaDB collection that is similar to the question.
             Returns an empty string if the collection does not exist or if no documents are found.
    Raises:
        chromadb.errors.InvalidCollectionException: If the specified collection 'document_chunks' does not exist.
    """
    client = chromadb.Client(chromadb.config.Settings())
    
    try:
        collection = client.get_collection('document_chunks')
    except chromadb.errors.InvalidCollectionException:
        print("Collection 'document_chunks' does not exist.")
        return ""
    
    # Get the embedding for the question  
    question_embedding = model.encode([question])   
    # Get stored embeddings and documents
    results = collection.get(include=['embeddings', 'documents']) 
    
    if results and results.get('documents'):
        # Calculate similarities
        embeddings = np.array(results['embeddings'])
        similarities = cosine_similarity(embeddings, question_embedding)  # Cosine similarity
        # Get the index of the most similar document
        most_similar_idx = np.argmax(similarities)
        return results['documents'][most_similar_idx] # Return the most similar document as context
    
    return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process document embeddings and optionally view stored chunks.")
    parser.add_argument('--view', action='store_true', help="View stored chunks after processing.")
    parser.add_argument('file_path', type=str, help="Path to the Word document.")
    args = parser.parse_args()

    try:
        text = read_document(args.file_path)
        chunks = split_into_chunks(text)
        store_chunks_in_chroma(chunks)
        if args.view:
            view_stored_chunks()
    except Exception as e:
        print(f"Error: {str(e)}")