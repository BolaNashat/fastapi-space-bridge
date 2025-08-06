from fastapi import FastAPI, Request
from gradio_client import Client

app = FastAPI()

# العملاء
smart_client = Client("BolaNash/openai-gpt-oss-120b")
websearch_client = Client("BolaNash/websearch_Elnasekh")

# الكلمات المفتاحية التي تشير إلى "بحث"
SEARCH_KEYWORDS = ["بحث", "ابحث", "من هو", "ما هو", "من تكون", "عن", "متى", "أين"]

def contains_search_keyword(text):
    return any(keyword in text for keyword in SEARCH_KEYWORDS)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "").strip()

    if contains_search_keyword(question):
        result = websearch_client.predict(question)
        used_model = "websearch"
    else:
        result = smart_client.predict(question)
        used_model = "gpt-oss"

    return {
        "answer": result,
        "model_used": used_model,
        "question": question
    }
