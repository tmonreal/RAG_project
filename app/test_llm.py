import os
import numpy as np
import chromadb
import chromadb.config
from llm import ask_llm 
from embeddings import read_document, split_into_chunks, store_chunks_in_chroma
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(file_path):
    """
    Creates embeddings from the given file and stores them in ChromaDB.
    Parameters:
        - file_path: str: The path to the Word document.
    Returns: None
    """
    text = read_document(file_path)
    chunks = split_into_chunks(text)
    store_chunks_in_chroma(chunks)

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
    question_embedding = model.encode([question])[0]    
    # Get stored embeddings and documents
    results = collection.get(include=['embeddings', 'documents']) 
    
    if results and results.get('documents'):
        # Calculate similarities
        embeddings = np.array(results['embeddings'])
        similarities = np.dot(embeddings, question_embedding)  # Cosine similarity
        # Get the index of the most similar document
        most_similar_idx = np.argmax(similarities)
        return results['documents'][most_similar_idx] # Return the most similar document as context
    
    return ""

def test_ask_llm():
    """
    Tests the functionality of the ask_llm function.
    This function serves as an integration test to ensure that the embedding creation, context retrieval,
    and language model response generation work together correctly.
    Returns: None
    """
    # Create embeddings for document
    create_embeddings('./data/documento.docx')

    question = "What is the name of the magical flower?"

    context = get_context(question)  # Get context based on the question
    print(f"Context used: {context}")
    response = ask_llm(question, context)
    print(f"Question: {question}")
    print(f"Response: {response}")

if __name__ == "__main__":
    test_ask_llm()
