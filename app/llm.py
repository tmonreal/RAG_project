"""
This file will interact with Cohere's LLM for generating responses.
"""
import cohere
import os
from dotenv import load_dotenv

load_dotenv('.env')
api_key = os.getenv('COHERE_API_KEY')
if not api_key:
    raise ValueError("API key not found. Set the COHERE_API_KEY in your .env file.")

co = cohere.Client(api_key)

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
    prompt = f"Answer the question in the third person in one sentence with an emoji. Context: {context}. Question: {question}"
    response = co.generate(
        model='command-xlarge',  # TODO: choose suitable model
        prompt=prompt,
        max_tokens=30, # Maximum length of response is short
        temperature=0 # Deterministic model: no randomness wanted
    )
    return response.generations[0].text.strip()
