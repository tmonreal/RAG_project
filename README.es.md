# Desafío RAG con LLMs
[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/tmonreal/RAG_project/blob/main/README.md)

---

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar una solución simple de **RAG (Generación Aumentada por Recuperación)** que permite interactuar con un **LLM (Modelo de Lenguaje de Gran Escala)** para generar respuestas basadas en un documento específico. Los usuarios pueden hacer preguntas a través de una API, y el sistema recupera el contexto relevante del documento usando embeddings y una base de datos vectorial, proporcionando respuestas precisas y contextuales.

![image](https://github.com/user-attachments/assets/32f081ae-c27d-4a13-9f4b-ea5fac5f1c80)

## Componentes
1. **API**: Creada con **FastAPI**, se comunica con el LLM y recibe preguntas de los usuarios en formato JSON.
2. **LLM**: Utilizando **Cohere**, este componente responde las preguntas basadas en fragmentos relevantes del documento.
3. **Embeddings**: El documento se divide en fragmentos, se codifica en embeddings y se almacena en **ChromaDB**.
4. **Prompt**: El sistema genera un prompt que incluye la pregunta del usuario, el contexto relevante y los requisitos para cumplir con los criterios de respuesta.

## Instrucciones de Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/tmonreal/RAG_project.git
   cd RAG_project

2. **Crear y activar un entorno virtual:**
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate
   
   # En Linux/MacOS
   python -m venv venv
   source venv/bin/activate
   
4. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt

6. **Agregar tu clave de API de Cohere:**
   Crea un archivo `.env` en el directorio raíz del proyecto y agrega tu clave de API de Cohere:
   ```bash
   COHERE_API_KEY=your_cohere_api_key
   
8. **Ejecutar la API localmente:**
   ```bash
   cd app
   uvicorn api:app --reload

10. **Acceder a la documentación de la API:**
     Abrí tu navegador y navega a:
    ```bash
    http://127.0.0.1:8000/docs

## Usando la API
Podes utilizar herramientas como Postman o curl para interactuar con la API.

### Formato de Solicitud:
- Endpoint: `POST /ask`
- Tipo de contenido: `application/json`
- Cuerpo:
  - Establecer `"create_embeddings": true` si deseas crear embeddings durante la solicitud.
  ```bash
  {
    "user_name": "Juan Pérez",
    "question": "¿Cuál es el nombre de la flor mágica?",
    "create_embeddings": false
  }

### **Formato de Respuesta:**
- El sistema siempre responderá en el mismo idioma que la pregunta, en una oración, en tercera persona, e incluirá emojis que resuman el contenido.
  ``` bash
  {
      "user_name": "John Doe",
      "question": "What is the name of the magical flower?",
      "response": "The name of the magical flower that illuminates the Amazonian jungle at night is 🌸 Luz de Luna 🌸."
  }
- Si los embeddings no existen y `"create_embeddings": false`, la API devolverá un mensaje de error.

## **Requisitos**
Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

1. **VS Code**: Recomendado para facilitar el desarrollo.
2. **Cuenta de Github**: Para gestionar el control de versiones y colaborar en el proyecto.
3. **GitHub configurado en VS Code**: Asegúrate de tener Git instalado y configurado dentro de VS Code.
4. **Python 3.9.6 o superior**: Asegúrate de tener Python instalado en tu máquina. Puedes verificar tu versión de Python ejecutando:
   ```bash
   python --version
   
5. **Paquetes de Python requeridos**: Asegúrate de instalar los paquetes de Python requeridos que se encuentran en el archivo `requirements.txt`. Podes instalarlos ejecutando:
   ```bash
   pip install -r requirements.txt
  
6. **Clave de API de Cohere**: Asegúrate de tener una clave de API de [Cohere](https://cohere.com/).

