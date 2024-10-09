"""
This file contains my FastAPI code for the API.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    user_name: str
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    return {"response": f"{request.user_name} asked: {request.question}"}