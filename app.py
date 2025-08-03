from fastapi import FastAPI, Request
from gradio_client import Client

app = FastAPI()

# إنشاء العملاء لكل Space
deepseek_client = Client("BolaNash/deepseek-ai-DeepSeek")
websearch_client = Client("BolaNash/websearch_Elnasekh")

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    # اختيار الأداة حسب طول السؤال
    if len(question.split()) <= 8:
        result = deepseek_client.predict(question)
    else:
        result = websearch_client.predict(question)

    return {"answer": result}
