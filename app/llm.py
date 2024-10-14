"""
This file will interact with Cohere's LLM for generating responses.
"""
import cohere
import os
import langdetect
from dotenv import load_dotenv

load_dotenv('.env')
api_key = os.getenv('COHERE_API_KEY')
if not api_key:
    raise ValueError("API key not found. Set the COHERE_API_KEY in your .env file.")

co = cohere.Client(api_key)

def detect_language(text):
    return langdetect.detect(text)

def ask_llm(question, context):
    """
    This function constructs a prompt that asks the Cohere LLM to answer the user's question
    in the third person, using an emoji, and returning a concise one-sentence response.
    Parameters:
        - question: str: The question posed by the user.
        - context: str: The contextual information that the LLM should consider while generating the response.
    Returns:
        - str: The generated response from the LLM.
    """

    detected_language = detect_language(question)
    prompt_templates = {
    "es": "Responder la pregunta de forma breve en español, en **una sola oración**, utilizando el siguiente contexto. Incluir un emoji que resuma la respuesta: ¿{question}\n\n---\nContexto:\n{context}",
    "en": "Answer the question briefly in English in **one sentence**, using the provided context. Include an emoji that summarizes the answer: {question}\n\n---\nContext:\n{context}"
    }

    # Use the detected language to select the appropriate prompt template
    prompt = prompt_templates.get(detected_language, "Answer the question concisely in only **one sentence**, with an emoji that summarizes the answer. Use the same language as the question and the provided context to respond. \n\nQuestion: {question}.\n\n---\nContext:\n{context}").format(question=question, context=context)
    response = co.generate(
        model='command-xlarge', 
        prompt=prompt,
        max_tokens=50, # Maximum length of response is short
        temperature=0 # Deterministic model: no randomness wanted
    )

    generated_text = response.generations[0].text.strip()

    # Post-process to ensure it only answes in one sentence
    # TODO: This is a temporary solution due to time constraints; 
    # consider implementing a more robust method to handle multi-sentence responses in the future.
    if "\n" in generated_text:
        return generated_text.split("\n")[0]
    
    return generated_text