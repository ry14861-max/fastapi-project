from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="InsafAI - Youth AI4SDGs 2027")

class Query(BaseModel):
    question: str
    language: str = "en"

@app.get("/")
def home():
    return {"project": "InsafAI", "challenge": "Youth AI4SDGs Impact Challenge 2027", "status": "running", "sdg": ["SDG 16 - Peace, Justice", "SDG 10 - Inclusion"]}

@app.post("/legal-aid")
def legal_aid(q: Query):
    # Placeholder for AI logic - you will connect LLM here
    answer = f"For your query: '{q.question}', InsafAI will draft a legal guidance response in {q.language}."
    return {"query": q.question, "answer": answer, "next_steps": ["Draft application", "Find relevant law"]}

@app.get("/health")
def health():
    return {"ok": True}
