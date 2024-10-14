# Challenge RAG with LLMs

[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/tmonreal/RAG_project/blob/main/README.md)
[![Español](https://img.shields.io/badge/lang-Español-red.svg)](https://github.com/tmonreal/RAG_project/blob/main/README.es.md)

---

## Project Description

This project aims to develop a simple **RAG (Retrieval Augmented Generation)** solution that allows interaction with a **LLM (Large Language Model)** to generate answers based on a specific document. Users can ask questions via an API, and the system retrieves relevant context from the document using embeddings and a vector database, providing accurate and context-based answers.

![image](https://github.com/user-attachments/assets/32f081ae-c27d-4a13-9f4b-ea5fac5f1c80)


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

## **Requirements**
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

## Using Docker

This project can be easily run using Docker. Below are the steps to build and run the Docker container, along with necessary modifications to ensure compatibility with Docker.

### Prerequisites

- Ensure that you have [Docker](https://www.docker.com/get-started) installed on your machine.

### Steps to Run the Project in Docker

1. **Clone the Repository**:
   Clone the project repository to your local machine if you haven't done so already:
   ```bash
   git clone https://github.com/tmonreal/RAG_project.git
   cd RAG_Project

2. **Modify `api.py`**: Before building the Docker image, ensure you modify the import statements in `api.py` and the document path as follows:

- Change lines 8 and 9:
   ```bash
   from .embeddings import create_embeddings, get_context, check_embeddings_exist
   from .llm import ask_llm

- Modify line 21 to:
  ```bash
  document_path = 'data/documento.docx'

3. **Build the Docker Image**: Open your terminal and run the following command to build the Docker image:
   ```bash
   docker build -t rag_api:1.0 .

4. **Run the Docker Container**: After the image has been built successfully, run the container with:
   ```bash
   docker run --env-file .env -p 8000:8000 rag_api:1.0

- The `--env-file .env` option loads environment variables defined in the `.env` file (For Cohere API Key).
- The `-p 8000:8000` option maps port 8000 on your local machine to port 8000 in the Docker container.

5. **Access the API**: You can now access the FastAPI application at http://localhost:8000/docs.


