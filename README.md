# Challenge RAG with LLMs

[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english) [![Español](https://img.shields.io/badge/lang-Español-red.svg)](#español)

---

## Project Description

This project aims to develop a simple **RAG (Retrieval Augmented Generation)** solution that allows interaction with a **LLM (Large Language Model)** to generate answers based on a specific document. Users can ask questions via an API, and the system retrieves relevant context from the document using embeddings and a vector database, providing accurate and context-based answers.

## Components
1. **API**: Created using **FastAPI**, it communicates with the LLM and receives user questions in JSON format.
2. **LLM**: Using **Cohere**, this component answers the questions based on relevant document chunks.
3. **Embeddings**: The document is split into chunks, encoded into embeddings, and stored in **ChromaDB**.
4. **Prompt**: The system generates a prompt that includes the user's question, relevant context, and requirements to fulfill the response criteria.

## Installation Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/tmonreal/RAG_project.git
   cd RAG_project

2. **Create and activate a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On Linux/MacOS
   python -m venv venv
   source venv/bin/activate
   
4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt

6. **Add your Cohere API key:**
   Create a `.env` file in the project root directory and add your Cohere API key:
   ```bash
   COHERE_API_KEY=your_cohere_api_key
   
8. **Run the API locally:**
   ```bash
   cd app
   uvicorn api:app --reload

10. **Access the API documentation:**
    Open your browser and navigate to:
    ```bash
    http://127.0.0.1:8000/docs

## Using the API
You can use tools like Postman or curl to interact with the API.

### Request Format:
- Endpoint: `POST /ask`
- Content-Type: `application/json`
- Body:
  - Set `"create_embeddings": true` if you want to create embeddings during the request.
  ```bash
  {
    "user_name": "John Doe",
    "question": "What is the name of the magical flower?",
    "create_embeddings": false
  }

### **Response Format:**
- The system will always respond in the same language as the question, in one sentence, in the third person, and include emojis summarizing the content.
  ``` bash
  {
      "user_name": "John Doe",
      "question": "What is the name of the magical flower?",
      "response": "The name of the magical flower that illuminates the Amazonian jungle at night is 🌸 Luz de Luna 🌸."
  }
- If the embeddings do not exist and `"create_embeddings": false`, the API will return an error message.

## **Requirements:**
To run this project, make sure you have the following installed:

1. **VS Code:** Recommended for ease of development.
2. **Github Account:** To manage version control and collaborate on the project.
3. **GitHub configured in VS Code:** Ensure Git is installed and set up within VS Code.
4. **Python 3.9.6 or higher:** Make sure Python is installed on your machine. You can check your Python version by running:
   ```bash
   python --version
5. **Required Python packages:** Ensure you install the required Python packages listed in the `requirements.txt` file. You can install them by running:
   ```bash
   pip install -r requirements.txt
6. **Cohere API Key**: Make sure you have a [Cohere](https://cohere.com/) API Key.
